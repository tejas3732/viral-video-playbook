#!/usr/bin/env python3
"""Break down your own videos frame by frame with Google Gemini, in the same format as the playbook.

    export GEMINI_API_KEY=...                       # free key: https://aistudio.google.com/apikey
    python3 tools/analyze_video.py my_video.mp4 other.mp4
    python3 tools/analyze_video.py *.mp4 --out breakdowns --prompt-file prompt.txt
    python3 tools/analyze_video.py clip.mp4 --model gemini-3.5-flash

Writes one <name>.json per video into --out (default: ./breakdowns), skipping videos already done.
Uses the Gemini Interactions API + Files API (standard library only). Free tier friendly: requests
are paced to 8 per minute, per-minute limits are retried, and a daily limit stops the run cleanly
(run it again tomorrow; finished videos are skipped). Uploaded files are deleted after each video.
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

BASE = 'https://generativelanguage.googleapis.com'
GAP = 60 / 8  # seconds between requests

SCHEMA_HINT = r'''
Return ONLY a JSON object (no markdown fences) with exactly these keys:
{
 "one_line": "what this video is, in one sentence",
 "format": {"aspect": "16:9|9:16|1:1|other", "duration_s": number, "has_voiceover": bool, "has_music": bool, "has_sfx": bool, "has_captions": bool},
 "hook": {"first_3s": "exactly what is on screen and heard in the first 3 seconds", "hook_type": "question|bold claim|visual surprise|problem|demo|countdown|other", "why_it_grabs": "..."},
 "structure": [{"t_start": number, "t_end": number, "beat": "short name", "on_screen": "what is shown", "audio": "what is heard"}],
 "visual_style": {"palette": "main colours with hex guesses", "typography": "type style, weights, sizes, how text animates", "backgrounds": "...", "graphic_elements": "...", "overall_look": "e.g. Apple keynote, brutalist, neon, editorial"},
 "motion": {"transitions": ["each distinct transition technique, with a timestamp example"], "text_animation": ["techniques"], "camera_moves": ["..."], "easing_feel": "snappy/springy/smooth/linear ...", "pacing_cuts_per_10s": number, "signature_moment": "the single most impressive animated moment, with timestamp"},
 "sound": {"music_genre": "...", "tempo_feel": "slow|mid|fast, approx BPM if you can tell", "music_arc": "how the music evolves (build, drop, silence...) with timestamps", "sync": "how visuals sync to beats or voice, with examples", "sfx": ["sound effects used and when"], "voice": "voice type, pace, tone, or none"},
 "copy": {"on_screen_text": ["key lines of on-screen text in order"], "narration_summary": "..."},
 "ending": {"what_happens": "...", "cta": "the call to action or none"},
 "what_works": ["3-6 specific, reusable reasons this video is effective"],
 "weak_spots": ["anything that hurts it"],
 "reusable_techniques": [{"name": "short name", "how_to": "concrete, implementable recipe: timings, easing, layout, colours, sound"}],
 "prompt_vs_result": "how the creator's prompt (if given) maps to what was produced, or none",
 "quality_score": {"hook": 1-10, "visual_polish": 1-10, "motion": 1-10, "sound": 1-10, "story": 1-10, "overall": 1-10}
}
Be specific and timestamped. Describe what you actually see and hear; don't guess at things you can't perceive.
'''


class DailyLimit(Exception):
    pass


def req(key, url, data=None, headers=None, method=None, raw=False, timeout=600):
    r = urllib.request.Request(url, data=data, headers={'x-goog-api-key': key, **(headers or {})}, method=method)
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        body = resp.read()
        return (resp.headers, body) if raw else json.loads(body or b'{}')


def duration(path):
    try:
        out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                             capture_output=True, text=True, check=True).stdout
        return float(out.strip())
    except Exception:
        return 30.0  # no ffprobe: assume a short video


def upload(key, path):
    hdrs, _ = req(key, f'{BASE}/upload/v1beta/files',
                  data=json.dumps({'file': {'display_name': os.path.basename(path)}}).encode(),
                  headers={'X-Goog-Upload-Protocol': 'resumable', 'X-Goog-Upload-Command': 'start',
                           'X-Goog-Upload-Header-Content-Length': str(os.path.getsize(path)),
                           'X-Goog-Upload-Header-Content-Type': 'video/mp4', 'Content-Type': 'application/json'},
                  raw=True)
    with open(path, 'rb') as f:
        info = req(key, hdrs['x-goog-upload-url'], data=f.read(),
                   headers={'X-Goog-Upload-Offset': '0', 'X-Goog-Upload-Command': 'upload, finalize'})
    f = info['file']
    while f.get('state') != 'ACTIVE':
        if f.get('state') == 'FAILED':
            raise RuntimeError('upload processing failed')
        time.sleep(4)
        f = req(key, f"{BASE}/v1beta/{f['name']}")
    return f


def analyze(key, path, model, prompt=''):
    dur = duration(path)
    # more frames for short videos, fewer for long ones (keeps long videos inside the free token limits)
    fps = 4 if dur <= 30 else 2 if dur <= 90 else 1 if dur <= 240 else 0.5
    f = upload(key, path)
    body = {'model': model, 'input': [
        {'type': 'video', 'uri': f['uri'], 'mime_type': 'video/mp4', 'processing': {'type': 'static', 'fps': fps}},
        {'type': 'text', 'text': (
            'You are a senior motion designer and video editor studying videos to learn reusable craft. '
            + (f'The creator\'s prompt:\n"""{prompt[:6000]}"""\n' if prompt else '')
            + 'Watch and listen to the whole video carefully, frame by frame, then break it down.\n' + SCHEMA_HINT)},
    ]}
    try:
        for attempt in range(4):
            try:
                res = req(key, f'{BASE}/v1beta/interactions', data=json.dumps(body).encode(),
                          headers={'Content-Type': 'application/json'}, timeout=900)
                break
            except urllib.error.HTTPError as e:
                msg = e.read().decode()[:300]
                if 'per day' in msg.lower():
                    raise DailyLimit(msg)
                if e.code in (429, 500, 503) and attempt < 3:
                    time.sleep(30 * (attempt + 1))
                    continue
                raise RuntimeError(f'HTTP {e.code}: {msg}')
    finally:
        try:
            req(key, f"{BASE}/v1beta/{f['name']}", method='DELETE')
        except Exception:
            pass
    text = ''.join(c.get('text', '') for s in res.get('steps', []) if s.get('type') == 'model_output'
                   for c in s.get('content', []))
    t = text.strip()
    if t.startswith('```'):
        t = t.split('\n', 1)[1].rsplit('```', 1)[0]
    try:
        analysis = json.loads(t)
    except json.JSONDecodeError:
        analysis = {'raw': text}
    return {'file': os.path.basename(path), 'duration_s': round(dur, 2), 'model': model, 'fps_sampled': fps, 'analysis': analysis}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('videos', nargs='+', help='.mp4 files')
    ap.add_argument('--out', default='breakdowns')
    ap.add_argument('--model', default=os.environ.get('GEMINI_MODEL', 'gemini-3.5-flash-lite'))
    ap.add_argument('--prompt-file', help='the prompt the video was made from (optional, same for all videos)')
    o = ap.parse_args()
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        sys.exit('Set GEMINI_API_KEY first (free key: https://aistudio.google.com/apikey).')
    prompt = open(o.prompt_file).read().strip() if o.prompt_file else ''
    os.makedirs(o.out, exist_ok=True)
    last = 0.0
    for path in o.videos:
        dest = os.path.join(o.out, os.path.splitext(os.path.basename(path))[0] + '.json')
        if os.path.exists(dest):
            print(f'skip {path} (done)')
            continue
        time.sleep(max(0.0, last + GAP - time.time()))
        last = time.time()
        try:
            rec = analyze(key, path, o.model, prompt)
        except DailyLimit as e:
            sys.exit(f'Daily free limit reached for {o.model}: run again tomorrow, or pass another --model. ({e})')
        except Exception as e:
            print(f'FAILED {path}: {e}', flush=True)
            continue
        with open(dest, 'w', encoding='utf-8') as f:
            json.dump(rec, f, indent=1, ensure_ascii=False)
        q = rec['analysis'].get('quality_score', {}) if isinstance(rec['analysis'], dict) else {}
        print(f"ok {path} -> {dest}  ({time.time() - last:.0f}s, overall {q.get('overall')})", flush=True)


if __name__ == '__main__':
    main()
