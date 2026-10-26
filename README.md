# Viral Video Playbook

**I had AI watch 418 viral AI-made videos frame by frame, then turned what worked into a skill your coding agent can use.**

Install it in Claude Code, Codex or any agent that supports [Agent Skills](https://agentskills.io). Then, when you ask your agent to make a launch video, an explainer or a motion graphic, it plans with real numbers (hooks, pacing, music, look) and pulls reference examples with step-by-step recipes from the 418 videos.

## Install

**Any agent (Claude Code, Codex, Cursor and more):**

```bash
npx skills add tejas3732/viral-video-playbook
```

**Claude Code, as a plugin:**

```
/plugin marketplace add tejas3732/viral-video-playbook
/plugin install viral-video-playbook@viral-video-playbook
```

**By hand:** copy `skills/viral-video-playbook/` into `~/.claude/skills/` (Claude Code) or `~/.agents/skills/` (Codex).

Then just ask: *"Make a 30-second launch video for my app"*, *"How do I make this explainer punchier?"* or *"Find me references for a 3D product reveal."*

## What's inside

| File | What it is |
|---|---|
| [`SKILL.md`](skills/viral-video-playbook/SKILL.md) | Tells your agent when and how to use the playbook: benchmarks, references, a prompt template, a review checklist |
| [`PLAYBOOK.md`](skills/viral-video-playbook/PLAYBOOK.md) | The findings in plain words: hooks, motion recipes, pacing, sound, colour and type, endings, mistakes, prompts, and the top 20 videos to study |
| [`data/videos.jsonl`](skills/viral-video-playbook/data/videos.jsonl) | 418 frame-by-frame breakdowns: hook, every beat with timestamps, palette, fonts, transitions, music arc, what works, weak spots, reusable recipes |
| [`data/index.csv`](skills/viral-video-playbook/data/index.csv) | One row per video, for browsing in a spreadsheet |
| [`scripts/refs.py`](skills/viral-video-playbook/scripts/refs.py) | Search the 418 for reference examples (Python standard library, no install) |
| [`tools/analyze_video.py`](tools/analyze_video.py) | Break down **your own** videos the same way with Google Gemini (free tier works) |

## What 418 viral videos have in common

| Finding | Number |
|---|---|
| Hook with a **visual surprise** in the first 3 seconds (not a logo) | 53% |
| Have **music** / **sound effects** | 94% / 91% |
| Have a **voiceover** | only 12% (28% for explainers) |
| Typical tempo | **120 BPM**, cuts on the beat |
| Typical length | **30 s** |
| Typical pace | **3 cuts per 10 s** (motion graphics 4, 3D 1) |
| Look like an **Apple keynote / minimal** | 53% |
| Have **no call to action** | 46% (an easy edge) |
| Top complaint | **text too fast to read** (42%) |

The moments people remember are **morphs**: one shape, card or screen turning into the next without a cut. Prompts that spelled out music/BPM, sound effects, aspect ratio, fonts and easing scored higher. More in [`PLAYBOOK.md`](skills/viral-video-playbook/PLAYBOOK.md).

## Find references yourself

```bash
cd skills/viral-video-playbook
python3 scripts/refs.py "logo reveal" --n 3
python3 scripts/refs.py "numbers counting up" --type explainer
python3 scripts/refs.py "single dot morph" --long
```

```
287 videos match "logo reveal"; top 3:

1. @Mounnna  (motion, 16 s)  https://x.com/Mounnna/status/2103802871934497266
   What:   A clean tech logo reveal animation transitioning from a wireframe constellation into faceted low-poly shards…
   Hook:   On a dark blue starry background, white constellation-style lines and dots connect together…
   Moment: The low-poly shards collapsing inward from chaotic scatter into a precise app icon shape at 05.7s.
   Recipe: Constellation to Polygon Logo Reveal: Start with random white nodes and thin connecting lines in 3D space.
           Animate them converging toward the center over 3 seconds using ease-out…
```

## Break down your own videos

```bash
export GEMINI_API_KEY=...   # free key: https://aistudio.google.com/apikey
python3 tools/analyze_video.py my_video.mp4 --out breakdowns
```

You get the same JSON breakdown as the 418 in about 20–40 seconds per short video. The tool stays inside the free-tier limits (8 requests a minute, stops cleanly at the daily limit, skips videos it already did) and deletes each upload from Google when it's done. `ffprobe` (part of ffmpeg) is used to read video length if you have it.

## How it was made

- **Videos:** the Claude Opus 5.5 viral video archive collected by Skillry ([@yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)): 418 videos posted on X, in four types (motion graphics 229, explainers 68, interactive 65, 3D 56).
- **Analysis:** each video uploaded to Google Gemini (3.5 Flash-Lite for 402, 3.5 Flash for 16) with the creator's prompt, sampled at 0.5–4 frames per second depending on length, returning a fixed JSON format. Free tier, one day.
- **Playbook:** the numbers were counted across all 418 breakdowns; the write-up was done with Claude.

**Read the scores as a ranking, not grades:** Gemini is generous (median 9/10). Descriptions can contain small mistakes; check the original post before relying on a detail.

## Credits

Every video belongs to its creator; each record links to the original post on X. The top 20 are credited in [`PLAYBOOK.md`](skills/viral-video-playbook/PLAYBOOK.md#10-the-top-20-to-study-credit-to-the-creators). Archive by Skillry / [@yihui-dev](https://github.com/yihui-dev). This repo contains descriptions and analysis only, no videos and no full prompts.

Made by [Tejas Rane](https://x.com/tejas3732). Code under the [MIT licence](LICENSE).
