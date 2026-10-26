# Viral Video Playbook

**I had AI watch 418 viral AI-made videos frame by frame, wrote down what the best ones do, and turned it into a skill your coding agent can use.**

Install it in Claude Code or Codex. Next time you ask your agent for a launch video, an explainer or a motion graphic, it plans with real numbers (hooks, pacing, music, look) and pulls real examples with step-by-step recipes from these 418 videos.

**Contents:** [Where the videos come from](#where-the-videos-come-from) · [How we analysed them](#how-we-analysed-them) · [What we found](#what-we-found) · [How to use it](#how-to-use-it) · [What's in this repo](#whats-in-this-repo) · [Credits](#credits)

---

## Where the videos come from

When Claude Opus 5.5 came out, people on X started posting short videos they had made with it: product promos, explainers, 3D scenes, small games. Many went viral.

**[Skillry](https://skillry.dev/ai-videos/opus-5-5)** collected **418** of them in one gallery, with the prompt each creator used where they shared it. The prompt text is also published as an open dataset at **[yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos)**.

- **387 creators**, every one linked to their original post on X
- **4 types:** motion graphics (229), explainers (68), interactive pieces and games (65), 3D (56)
- **211** came with the creator's full prompt; for the other **207** only the post text was available

All credit for the videos goes to their creators, and for collecting them to Skillry and [@yihui-dev](https://github.com/yihui-dev). This repo holds **our notes about the videos only**: no videos, no full prompts. Every note links back to the original post.

## How we analysed them

In plain words: we showed every video to an AI that can watch video, asked it the same detailed questions each time, then counted the answers.

1. **Watched with Google Gemini.** Each video was uploaded to Gemini (3.5 Flash-Lite for 402 videos, 3.5 Flash for 16), together with the creator's prompt. Gemini looked at 0.5 to 4 frames per second depending on the length (more frames for short videos) and listened to the sound.
2. **Same questions every time.** Gemini answered in a fixed format: the first 3 seconds (the hook), every scene with timestamps, colours and fonts, transitions and text animation, pacing, music and sound effects, the ending, what works, what doesn't, reusable recipes, how the prompt shaped the result, and scores out of 10.
3. **Free and fast.** Everything ran on Gemini's free tier, so it cost $0. The main run of 402 videos took about 70 minutes. Requests were spaced out to stay under the free limits, and each upload was deleted once its video was done.
4. **Checked and counted.** Any answer that came back broken was re-run until all 418 were clean. Then we counted patterns across all of them (how many open with a surprise, typical tempo, length, cuts per 10 seconds, and so on) and wrote up the findings with Claude.

Want to do the same with your own videos? See [Break down your own videos](#4-break-down-your-own-videos).

## What we found

| Finding | Number |
|---|---|
| Open with a **visual surprise** in the first 3 seconds (not a logo) | 53% |
| Have **music** / **sound effects** | 94% / 91% |
| Have a **voiceover** | only 12% (28% for explainers) |
| Typical tempo | **120 BPM**, with cuts on the beat |
| Typical length | **30 seconds** |
| Typical pace | **3 cuts every 10 seconds** (motion graphics 4, 3D 1) |
| Look like an **Apple keynote** (clean, minimal) | 53% |
| Have **no call to action** at the end | 46%, an easy edge |
| Most common complaint | **text too fast to read** (42%) |

The moments people remember are **morphs**: one shape, card or screen turning into the next without a cut. Prompts that spelled out music, sound effects, screen shape, fonts and motion style scored higher.

The full write-up, with a hook library, motion recipes, sound, colour, endings, mistakes to avoid, a prompt template and the top 20 videos to study, is in **[PLAYBOOK.md](skills/viral-video-playbook/PLAYBOOK.md)**.

---

## How to use it

### 1. Install it (one command)

You need [Node.js](https://nodejs.org) for this command. Run it in your terminal:

```bash
npx skills add tejas3732/viral-video-playbook
```

It asks which agents to add it to (Claude Code, Codex, Cursor and others). Pick yours and you're done.

<details>
<summary>Other ways to install</summary>

**Claude Code plugin.** Type these inside Claude Code:

```
/plugin marketplace add tejas3732/viral-video-playbook
/plugin install viral-video-playbook@viral-video-playbook
```

**By hand.** Download this repo and copy the folder `skills/viral-video-playbook` into:
- Claude Code: `~/.claude/skills/`
- Codex: `~/.agents/skills/` (or `.agents/skills/` inside one project)

</details>

### 2. Just ask your agent

You don't have to call anything. When you ask for a video, your agent reads the skill on its own. Try:

- *"Make a 30-second launch video for my app."*
- *"Plan an explainer about how our product works. What should the first 3 seconds be?"*
- *"This video feels slow. How do I make it punchier?"*
- *"Find me 3 references for a 3D product reveal."*
- *"Review my render against the viral video playbook."*

If you want it every time, name it: *"use the viral-video-playbook skill"*.

What your agent then does:
1. Reads the benchmarks (hook, pace, music, length) before planning.
2. Finds 1–2 real reference videos that fit your idea and credits them in the plan ("Inspired by @creator").
3. Writes the prompt or storyboard using the template that scored best.
4. Checks the finished video against the most common mistakes (text too fast, clutter, weak ending, no call to action).

It's meant as **inspiration, not rules**: borrow an idea or two, keep your own style.

### 3. Search the examples yourself

No install needed, just Python 3:

```bash
cd skills/viral-video-playbook
python3 scripts/refs.py "logo reveal"                      # top 5 matches
python3 scripts/refs.py "numbers counting up" --type explainer --n 3
python3 scripts/refs.py "single dot morph" --long          # adds scene timings, colours, music
python3 scripts/refs.py --stats                            # the headline numbers
```

Each result shows the creator, a link to the post, the hook, the standout moment and a recipe you can copy:

```
287 videos match "logo reveal"; top 3:

1. @Mounnna  (motion, 16 s)  https://x.com/Mounnna/status/2103802871934497266
   What:   A clean tech logo reveal animation transitioning from a wireframe constellation into faceted low-poly shards…
   Hook:   On a dark blue starry background, white constellation-style lines and dots connect together…
   Moment: The low-poly shards collapsing inward from chaotic scatter into a precise app icon shape at 05.7s.
   Recipe: Constellation to Polygon Logo Reveal: Start with random white nodes and thin connecting lines in 3D space.
           Animate them converging toward the center over 3 seconds using ease-out…
```

Prefer a spreadsheet? Open [`data/index.csv`](skills/viral-video-playbook/data/index.csv): one row per video with the creator, link, type, length, hook type, score and a one-line summary.

### 4. Break down your own videos

Get the same frame-by-frame notes for any video: yours, a competitor's ad, a draft you're stuck on.

1. Get a free Gemini API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey).
2. Run:

```bash
export GEMINI_API_KEY=your-key-here
python3 tools/analyze_video.py my_video.mp4
```

You get `breakdowns/my_video.json` in about 20–40 seconds for a short video. You can pass many videos at once (`*.mp4`) or add `--prompt-file prompt.txt` if you have the prompt the video was made from. The tool stays inside the free limits on its own: it spaces requests out, stops cleanly at the daily limit (run it again the next day and it carries on), and deletes each upload from Google when it's done. It uses `ffprobe` (part of [ffmpeg](https://ffmpeg.org)) to read video length if you have it.

---

## What's in this repo

| File | What it is |
|---|---|
| [`SKILL.md`](skills/viral-video-playbook/SKILL.md) | The instructions your agent reads: when to use the playbook and how |
| [`PLAYBOOK.md`](skills/viral-video-playbook/PLAYBOOK.md) | The findings in plain words, plus the top 20 videos with credits |
| [`data/videos.jsonl`](skills/viral-video-playbook/data/videos.jsonl) | All 418 frame-by-frame notes, one video per line |
| [`data/index.csv`](skills/viral-video-playbook/data/index.csv) | One row per video, for spreadsheets |
| [`scripts/refs.py`](skills/viral-video-playbook/scripts/refs.py) | The search tool |
| [`tools/analyze_video.py`](tools/analyze_video.py) | Break down your own videos with Gemini |

## Good to know

- **Scores are for ranking, not grading.** Gemini is generous (the median is 9 out of 10), so compare videos with each other rather than reading a 9 as "excellent".
- **AI notes can be slightly off.** Before you rely on a detail, open the original post (every note has the link).
- **Credit when you borrow.** If a recipe came from someone's video, a shout-out to the creator is the nice thing to do.

## Credits

- **Videos and prompts:** their 387 creators on X. Every note links to the original post, and the top 20 are credited by name in [PLAYBOOK.md](skills/viral-video-playbook/PLAYBOOK.md#10-the-top-20-to-study-credit-to-the-creators).
- **Collection:** [Skillry](https://skillry.dev/ai-videos/opus-5-5) and [@yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos).
- **Video analysis:** Google Gemini. **Write-up:** made with Claude.
- **Made by** [Tejas Rane](https://x.com/tejas3732). Code under the [MIT licence](LICENSE).
