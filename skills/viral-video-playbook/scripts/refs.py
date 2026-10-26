#!/usr/bin/env python3
"""Find reference videos among 418 viral AI-made videos, each broken down frame by frame.

    python3 refs.py "3d product reveal"
    python3 refs.py "numbers counting up" --type explainer --n 3
    python3 refs.py "morph" --long          # also print the beats, look, motion and sound
    python3 refs.py --stats                 # headline numbers across all 418

Matches every word of the query against each video's notes (hook, look, motion, sound, recipes...),
ranks by how well it matches, then by the scores. Standard library only. Inspiration, not rules.
"""

import argparse
import json
import os
import re
import statistics
from collections import Counter

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'videos.jsonl')

# where a match counts more: the parts you would actually borrow
WEIGHTS = {'reusable_techniques': 3, 'motion': 3, 'hook': 2, 'one_line': 2, 'visual_style': 2,
           'sound': 2, 'structure': 1, 'what_works': 1, 'ending': 1, 'copy': 1}


def flat(x):
    if isinstance(x, dict):
        return ' '.join(flat(v) for v in x.values())
    if isinstance(x, list):
        return ' '.join(flat(v) for v in x)
    return str(x)


def total(a):
    q = a.get('quality_score') or {}
    return sum(float(v) for v in q.values() if isinstance(v, (int, float)))


def load():
    with open(DATA, encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]


def stats(rows):
    a = [r['analysis'] for r in rows]
    fmt = [x.get('format') or {} for x in a]
    pct = lambda k: round(100 * sum(bool(f.get(k)) for f in fmt) / len(fmt))
    hooks = Counter(str((x.get('hook') or {}).get('hook_type', '')).replace('_', ' ') for x in a)
    cuts = [x['motion']['pacing_cuts_per_10s'] for x in a if isinstance((x.get('motion') or {}).get('pacing_cuts_per_10s'), (int, float))]
    print(f"{len(rows)} videos · median {statistics.median(float(r['duration_s']) for r in rows):.0f} s · "
          f"median {statistics.median(cuts):.0f} cuts per 10 s")
    print(f"music {pct('has_music')}% · sound effects {pct('has_sfx')}% · voiceover {pct('has_voiceover')}% · captions {pct('has_captions')}%")
    print('hooks: ' + ', '.join(f'{k} {v}' for k, v in hooks.most_common(6)))
    print('types: ' + ', '.join(f'{k} {v}' for k, v in Counter(r['category'] for r in rows).most_common()))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('query', nargs='*')
    ap.add_argument('--type', choices=['motion', 'explainer', '3d', 'interactive'])
    ap.add_argument('--n', type=int, default=5)
    ap.add_argument('--long', action='store_true')
    ap.add_argument('--stats', action='store_true')
    o = ap.parse_args()
    rows = load()
    if o.stats or not o.query:
        stats(rows)
        return
    words = [w for w in re.findall(r'[a-z0-9]+', ' '.join(o.query).lower()) if len(w) > 1]

    hits = []
    for r in rows:
        a = r['analysis']
        if not isinstance(a, dict) or (o.type and r['category'] != o.type):
            continue
        score, found = 0, set()
        for key, w in WEIGHTS.items():
            text = flat(a.get(key, '')).lower()
            for word in words:
                n = len(re.findall(r'\b' + re.escape(word), text))
                if n:
                    score += w * min(n, 3)
                    found.add(word)
        if found:
            # videos that match every word of the query come first
            hits.append((len(found), score, total(a), r))

    hits.sort(key=lambda h: (-h[0], -h[1], -h[2]))
    if not hits:
        print('No matches. Try fewer or simpler words (e.g. "morph", "counter", "3d", "terminal").')
        return
    print(f'{len(hits)} videos match "{" ".join(o.query)}"; top {min(o.n, len(hits))}:\n')
    for i, (_, _, _, r) in enumerate(hits[:o.n], 1):
        a = r['analysis']
        m, h = a.get('motion') or {}, a.get('hook') or {}
        print(f"{i}. {r['handle']}  ({r['category']}, {round(float(r['duration_s']))} s)  {r['post']}")
        print(f"   What:   {a.get('one_line', '')}")
        print(f"   Hook:   {h.get('first_3s', '')}")
        print(f"   Moment: {m.get('signature_moment', '')}")
        techs = [t for t in a.get('reusable_techniques') or [] if isinstance(t, dict)]
        # show the technique that matches the query best
        techs.sort(key=lambda t: -sum(w in flat(t).lower() for w in words))
        for t in techs[:len(techs) if o.long else 1]:
            print(f"   Recipe: {t.get('name', '')}: {t.get('how_to', '')}")
        if o.long:
            s, v = a.get('sound') or {}, a.get('visual_style') or {}
            print(f"   Look:   {v.get('overall_look', '')} | {v.get('palette', '')} | {v.get('typography', '')}")
            print(f"   Motion: {flat(m.get('transitions', ''))} | {m.get('easing_feel', '')}")
            print(f"   Sound:  {s.get('music_genre', '')}, {s.get('tempo_feel', '')}. {s.get('music_arc', '')}")
            for b in a.get('structure') or []:
                if isinstance(b, dict):
                    print(f"     {b.get('t_start', '')}-{b.get('t_end', '')}  {b.get('beat', '')}: {b.get('on_screen', '')}")
        print()


if __name__ == '__main__':
    main()
