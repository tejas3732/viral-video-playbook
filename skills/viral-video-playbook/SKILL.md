---
name: viral-video-playbook
description: What 418 viral AI-made videos (motion graphics, explainers, 3D, interactive demos made with Claude, Remotion, HyperFrames, Three.js) have in common, broken down frame by frame — hooks, transitions, text animation, pacing, music arcs, sound effects, colour, type, endings — plus a search over all 418 for real reference examples with step-by-step recipes. Use when planning, scripting, storyboarding, building or reviewing any short video, launch video, promo, explainer, product demo, motion graphic, title card or animation, or when the user asks how to make a video more engaging, more viral, punchier or better paced. Inspiration, not rules.
---

# Viral video playbook

418 viral videos made with AI (posted on X), each watched frame by frame by Google Gemini and broken down into hook, beats with timestamps, look, motion, sound, ending, what works, weak spots and reusable recipes.

- `PLAYBOOK.md`: the findings in plain words, with numbers. Read section 1 ("the short version") before planning a video.
- `data/videos.jsonl`: one record per video (`handle`, `post` link, `category`, `duration_s`, `analysis`).
- `scripts/refs.py`: search the records (standard library only).

Treat everything here as **inspiration, not rules**. Borrow one or two ideas that fit the brief; don't force a pattern that fights it, and skip this skill if the user already has a clear vision.

## How to use it

### 1. Before the storyboard: get the benchmarks

Read `PLAYBOOK.md` section 1, plus the section for the decision at hand (2 pacing by video type, 3 hooks, 4 motion, 5 sound, 6 look, 7 endings, 8 mistakes, 9 prompts).

The short version:
- **Hook in the first 3 s with a visual surprise** (53%), a problem the viewer feels (17%) or an instant demo (14%). Not a logo.
- **Music 94%, sound effects 91%, voiceover only 12%** (28% for explainers): motion + on-screen text + beat carry the story.
- **Median 120 BPM**, cuts and reveals on the beat; arc = quiet pulse → build → **drop on the reveal** → resolving chord on the end card.
- **Median 30 s**; about 3 cuts per 10 s (motion graphics 4, explainers 2, 3D 1).
- **Signature moments are morphs**: one shape, card or screen becoming the next without a cut.
- **Clean beats busy**: Apple-keynote minimal is the top look; one accent colour; heavy sans headlines + mono labels.
- **End on a brand lockup + one clear CTA** (46% have none — an easy edge).

### 2. Find references for the specific beats

```bash
python3 scripts/refs.py "<topic, effect or style>"            # top 5 matches with hook, key moment, recipe
python3 scripts/refs.py "logo reveal" --type motion --n 3     # --type: motion | explainer | 3d | interactive
python3 scripts/refs.py "single dot morph" --long             # + beats with timestamps, look, motion, sound
python3 scripts/refs.py --stats                               # headline numbers
```

Paths are relative to this skill's folder. Query with plain words for what you need ("counter", "terminal typing", "before after wipe", "beat synced text", "3d exploded view", "chat ai answer", "paper cutout"). Each result gives the creator, a link to the original post, the hook, the standout moment and a concrete recipe (timings, easing, layout, colours, sound).

Pick 1–2 ideas per video and note them in the storyboard as **"Inspired by: @creator (moment, link)"**, so borrowing stays visible and credited. Don't copy a whole video.

### 3. Write the brief / prompt

Prompts that specified music or BPM, sound effects, aspect ratio, fonts and easing scored higher. Skeleton (from `PLAYBOOK.md` section 9):

```
Make a [30 s] [16:9] [motion graphics / explainer] video in [Remotion / HyperFrames] about [X].
Look: [Apple-keynote minimal | editorial cream serif | dark HUD terminal], one accent colour [#hex],
fonts [heavy sans headline + mono labels].
Hook (0–3 s): [visual surprise / problem / instant demo].
Beats: [4–6 scenes with rough timestamps]; signature moment = [one element MORPHS into the next].
Motion: snappy springs, about [4] cuts per 10 s, one thing moving at a time, text on screen long enough to read.
Sound: [electronic, 120 BPM], build → drop on the reveal → resolving chord on the end card;
whoosh on transitions, click on UI, sub-bass hit on reveals.
End: logo + tagline + URL + one-line CTA, held still for 2 s.
```

### 4. Review the render against the most common mistakes

The top criticisms across the 418: **text too fast to read (42%)**, **cluttered (25%)**, abrupt ending, too long, generic music. Check:
- Every text line is on screen for at least **(words × 0.3 s) + 0.5 s**.
- Only one thing moves at a time in the focal area.
- The first 3 s show something happening, not a logo or a blank frame.
- Cuts and reveals land on the beat; there is at least one sound effect per UI action.
- The ending is settled (no glitch on the final frame) with one clear CTA.
- For X: the first frames are a clean branded card, because X shows an early frame as the preview.

## Notes on the data

- Scores come from Gemini and are generous (median 9/10): use them to rank, not as grades.
- Analysed with Gemini 3.5 Flash-Lite (402 videos) and 3.5 Flash (16) on 26 Oct 2026. Descriptions can contain small errors; open the original post before relying on a detail.
- Videos and prompts belong to their creators on X; every record links to the original post. Credit creators when you borrow from them.
