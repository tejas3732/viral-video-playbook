# The Video Playbook: what 418 viral AI-made videos have in common

**Source:** every video in the [Skillry "Claude Opus 5.5" gallery](https://skillry.dev/ai-videos/opus-5-5): 418 videos posted on X by 387 creators, with the creators' prompts from the open dataset at [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) (211 full prompts; 207 post text only). Each video was watched frame by frame by Google Gemini (3.5 Flash-Lite for 402 videos, 3.5 Flash for 16) on the free tier, on 26 Oct 2026. The full notes for every video are in `data/videos.jsonl` (search them with `scripts/refs.py`).

**How to read the scores:** Gemini scores generously (the median is 9 out of 10). Use the scores to **rank** videos against each other, not as absolute grades.

---

## 1. The short version (read this if nothing else)

1. **Open on a visual surprise, not a logo.** 53% of the videos hook with something unexpected happening in the first 3 seconds. Next most common: a problem the viewer feels (17%) and an instant product demo (14%).
2. **Music almost always; voice rarely.** 94% have music and 91% have sound effects, but only 12% have a voiceover. These videos tell the story with **motion + text + beat**.
3. **Lock the cuts to the beat.** The most common tempo is **120 BPM** (median 120; 110 is next). More than half the videos are described as cutting or animating on the beat.
4. **Short.** The median is **30 seconds**. Explainers run a little longer (39 s).
5. **One thing should *become* another.** The moments people remember are **morphs**: one shape, card or screen turning into the next without a cut (a Poké Ball becoming a Pokédex, a heartbeat line becoming a baby, a chart shrinking into a search bar).
6. **Clean and premium beats busy.** "Apple keynote / minimal" is the most common look (53%). The top complaints are "too fast to read" (42%) and "cluttered" (25%).
7. **End on a brand lockup** (logo plus tagline or URL). Almost half the videos (46%) have **no CTA at all**, which is an easy edge to take.
8. **More detailed prompts got better results.** Prompts that mention music/BPM, sound effects, aspect ratio, fonts or easing all scored higher. Prompts of 400+ words averaged **9.5** versus **9.0** for prompts under 150 words.

---

## 2. Benchmarks by video type

| Type | Videos | Typical length | Cuts per 10 s | Voiceover | Notes | Median score |
|---|---|---|---|---|---|---|
| **Motion graphics** (promos, showreels) | 229 | 30 s | **4** (fast) | 12% | music 97%, sound effects 96% | 9.5 |
| **Explainer** | 68 | 39 s | 2 | **28%** | captions 65% | 9.0 |
| **3D** | 56 | 27 s | **1** (slow, long camera moves) | 4% | | 9.0 |
| **Interactive** (web demos, tools) | 65 | 32 s | 2 | 3% | | 8.5 |
| **All 418** | 418 | **30 s** | **3** | 12% | music 94%, sfx 91%, captions 50% | 9.0 |

**Shape of the frame:** 16:9 = 310 (74%), 9:16 = 84 (20%), 1:1 = 24 (6%).

**What this means for a 5-minute YouTube video:** these are short pieces. Use them as **scene recipes**: a 5-minute video is roughly ten 30-second "viral-grade" scenes joined by a story. Keep motion-graphics scenes at about 4 cuts per 10 s and explainer stretches at about 2.

---

## 3. Hook library (the first 3 seconds)

| Hook type | How many | Best example | Why it works |
|---|---|---|---|
| **Visual surprise** | 222 (53%) | @eyadnour: a 3D QR code gets a literal *bite* taken out of it, and the voice says "it still reads." | A strange physical action plus a fact you didn't expect. |
| **Problem** | 70 (17%) | @vahidf24: a messy investor spreadsheet full of red "Bounced" errors, with the text "You're about to spend months emailing investors…" | The viewer recognises their own pain within a second. |
| **Demo** | 60 (14%) | @miskinho_: "One idea." on white, then typing "Launch our summer menu" makes everything appear instantly. | Input to payoff in under 3 seconds. |
| **Bold claim** | 37 (9%) | @davidmarcus: "Money still moves like it's 1973." then "Not anymore." | A dated comparison creates instant tension. |
| **Question** | 21 (5%) | @emollick: "HOW DO YOU EXPLAIN RECURSION?" then on the beat, "EASY." on red. | A hard question answered with total confidence. |
| **Countdown / timer** | 7 (2%) | @arthurkatcher: "How a coding agent works in 40 seconds." | Tells the viewer the time cost up front. |

**Opening tricks that come up again and again:**
- **A single glowing dot in the dark** (@kloss_xyz, @marklaunches, @nolkeeg) that grows into the whole world of the video. This is the most "cinematic" cold open in the set.
- **A typing cursor**: a search bar or terminal that types the premise (`npx …`, "Ask me anything.", "What do you want to make?").
- **A flat line that turns into something**: an ECG line becoming a character, a red line becoming a headline.

---

## 4. Motion recipes

### Transitions (how often each was seen)
| Transition | Videos | When to use it |
|---|---|---|
| Zoom / scale through | 149 | Into a detail, or "push through" a screen into the next scene |
| Whip / swipe / push | 92 | Fast energy between beats; good on the kick drum |
| Mask or wipe reveal | 85 | Before/after, revealing a headline |
| Camera fly-through / dolly / orbit | 80 | 3D and product scenes |
| Crossfade | 69 | Calm or emotional moments only |
| Particle burst / shatter | 46 | Big reveals, the "drop" |
| White flash | 35 | Hard scene change on an impact hit |
| Glitch | 35 | Tech or dystopian tone (keep it off the end card) |
| **Morph** (one shape becomes the next) | 30 | **Signature moments.** Rarer, but over-represented in the top 20 |
| Match cut | 14 | The same shape in two scenes |

### Text animation
Fade (169), **scale pop with spring bounce** (164), **counting numbers** (109), typewriter (102), word-by-word stagger (98), slide-up behind a mask (75), highlighter or underline sweep (42), scramble/decode (24).

### Feel of the motion
"Snappy" (213), "smooth" (199) and "spring" (191) dominate; linear is rare (49). **Default: fast-in, soft-settle springs.** Nothing should move at a constant speed except long camera glides.

### Ten reusable techniques worth stealing
(Picked from the 638 unique techniques Gemini pulled out.)

1. **Single-shape UI morph.** Keep one container and animate its width, height, corner radius and colour from state to state while the contents crossfade. Don't cut between screens. (@TheGrootDev, @AnnaCher___)
2. **Infinite scale zoom.** One continuous camera move from room scale down to atoms, with a ruler on the right edge whose units change (m → cm → µm → nm). (@ai_ba_reza)
3. **Beat-synced style montage.** Cut between 5 to 8 different visual styles every 0.5 to 1 s, locked to the kick drum. (@heyiamnick)
4. **Orb singularity.** Shrink all the clutter into one glowing dot, hit a sub-bass impact, then expand into a clean accent-coloured background.
5. **Exponential node growth.** One dot duplicates (2, 8, 32 and so on) while a counter races up, until the screen is full. This is the go-to visual for "scale".
6. **Visual stat proof.** Don't *say* "80%". Show 100 blocks and turn 80 of them dark one by one. (@melvynx: thousands of contact dots switching to "unopened")
7. **Spring-stretched tabs.** The leading edge of a sliding tab indicator moves ahead of the trailing edge, so it stretches like liquid.
8. **HUD chrome.** Thin monospace text in the corners (`TC 00:00:12`, crop marks, coordinates) over a dark, grainy background. It looks "pro" instantly.
9. **3D lock-on.** A product rotates inside a targeting reticle with changing data (Rot X/Y/Z, "Solving…") that snaps to `0.0°` and locks. (@0xValure)
10. **Pattern break.** Set up three classic examples, then make the fourth a modern or meme twist. It works because it is funny and surprising.

---

## 5. Sound

| What | Finding |
|---|---|
| Music style | Electronic/synth (301 mentions), lo-fi/ambient beds (187), trap/hip-hop beats (159), "tech/corporate upbeat" (153), synthwave/retro (96), cinematic (60) |
| Tempo | **Median 120 BPM.** 120s: 160 videos, 110s: 82, 90s: 44 |
| Music arc | **Build → drop → resolve** is the standard: a quiet drone or pulse at the start, a beat drops when the product or idea appears, and it ends on a **resolving chord** at the logo |
| Sync | 56% of videos are described as syncing to beats/kicks/hits |
| Sound effects | 91% use them: whooshes on transitions, clicks on UI, pops on text, sub-bass hits on reveals |
| Voice | Only 12% (28% for explainers). Text on screen does the talking |

**The template the best ones follow** (for example @kloss_xyz, @marklaunches, @melvynx):
`0 to 3 s` atmospheric drone plus one pulse → `3 to 6 s` beat enters on the first real visual → middle: steady 120 BPM, one SFX per UI action → `about 75%` one beat of silence or a pause → `final` big swell and resolving chord on the end card.

---

## 6. Look: colour and type

- **Overall look:** Apple keynote / minimal (223), editorial/Swiss (98), terminal/hacker (66), retro pixel (61), cyberpunk neon (43), cinematic (37), playful cartoon (30).
- **Backgrounds:** dark and light are both near-universal because most videos **switch between them**. A black ↔ white flip is a common beat marker.
- **Accent colours:** blue (197), green (172), orange (136), neon cyan (119), purple (88). **Pick one accent** and keep it everywhere.
- **Type:** sans-serif (346), heavy/bold weights (234), monospace for data and HUD (93), serif for editorial or documentary (78). The common pairing is **heavy sans headline + mono labels**.
- **Two strong alternatives to dark-tech:** *editorial cream* (off-white `#F6F1EA`, elegant serif, terracotta accent) and *neo-brutalist* (pastel fills, thick black outlines, hard offset shadows).

---

## 7. Endings

- Brand lockup (logo, wordmark) in 150 videos; URL in 61; tagline in 58; **seamless loop** back to the opening in 27 (great for X, where videos autoplay on repeat).
- **192 of 418 (46%) have no call to action.** A clear one-line CTA (URL or "follow for part 2") is a cheap advantage.
- For X: the post shows an early frame as the preview, so open on the clean, settled end card for at least 10 frames, then cut into the film.

---

## 8. What viewers would criticise (avoid these)

| Weak spot | Videos |
|---|---|
| Too fast / text too small to read | **174** |
| Cluttered, too much at once | 104 |
| Abrupt ending | 34 |
| Too long or drags | 26 |
| Generic stock-sounding music | 19 |

**Rule of thumb:** each line of text stays on screen for at least **(word count × 0.3 s) + 0.5 s**, and only **one thing moves at a time** in the focal area.

---

## 9. Prompt patterns (what the creators asked for)

- The median prompt is short (**37 words**), and many are just the X post. Only 23 prompts are 400+ words, and those averaged **9.5** versus **9.0** for short prompts.
- Tools named in prompts: **Remotion 99**, Three.js 25, **HyperFrames 22**, After Effects 12, ElevenLabs 8, GSAP 7, Suno 4.

| What the prompt included | Prompts | Avg score with | Avg score without |
|---|---|---|---|
| Music or BPM | 73 | **9.49** | 8.90 |
| Sound effects | 20 | **9.53** | 8.98 |
| Aspect ratio / resolution | 23 | **9.51** | 8.97 |
| Easing / spring words | 39 | 9.31 | 8.97 |
| Font names | 58 | 9.28 | 8.96 |
| Exact seconds / timestamps | 53 | 9.22 | 8.97 |
| Names a tool (Remotion, etc.) | 127 | 9.15 | 8.94 |

**A prompt skeleton built from what scored best:**
```
Make a [30 s] [16:9] [motion graphics / explainer] video in [Remotion / HyperFrames] about [X].
Look: [Apple-keynote minimal | editorial cream serif | dark HUD terminal], one accent colour [#hex],
fonts [heavy sans headline + mono labels].
Hook (0 to 3 s): [visual surprise / problem / instant demo].
Beats: [4 to 6 scenes with rough timestamps]; signature moment = [one element MORPHS into the next].
Motion: snappy springs, about [4] cuts per 10 s, one thing moving at a time, text on screen long enough to read.
Sound: [electronic, 120 BPM], build → drop on the reveal → resolving chord on the end card;
whoosh on transitions, click on UI, sub-bass hit on reveals.
End: logo + tagline + URL + one-line CTA, held still for 2 s.
```

---

## 10. The top 20 to study (credit to the creators)

Ranked by the sum of Gemini's six sub-scores (hook, polish, motion, sound, story, overall). Watch for the "moment to study".

| # | Creator | Type | Length | What it is | The moment to study |
|---|---|---|---|---|---|
| 1 | [@TheGrootDev](https://x.com/TheGrootDev/status/2103516567824966114) | motion | 14 s | A sleek, continuous UI morphing animation turning a Poké Ball into an interactive modern Pokédex for Pikachu and Eevee. | The container morphing and compressing from the full stat chart down into a compact search bar at 00:09.000 |
| 2 | [@ceowinkz](https://x.com/ceowinkz/status/2103647124126683602) | motion | 15 s | A dynamic 15-second B2B motion graphics pitch for Winkz Brands targeting e-commerce brands. | The Before/After listing rebuild comparison card wipe at 07.75s to 09.00s |
| 3 | [@chrisjdimarco](https://x.com/chrisjdimarco/status/2103606498928808196) | motion | 60 s | A polished 60-second motion graphics showreel advocating for an informed public and democratic vigilance against crony capitalism and the ruling class. | The chess piece dot simulation at 0:42.5 where chaotic colored dots snap into rigid rows on a grid and then burst into independent paths ( |
| 4 | [@davidmarcus](https://x.com/davidmarcus/status/2103275618045686217) | motion | 23 s | A punchy, brutalist-editorial vertical promo for Lightspark Grid highlighting instant cross-border payments for humans and AI agents. | The AI agent code block typing out and instantly showing 'Settled' at 14.5s synchronized with a success click SFX. |
| 5 | [@emollick](https://x.com/emollick/status/2103688362960019567) | explainer | 75 s | A self-referential, endlessly recursive explainer video about recursion where each style change drills one layer deeper into a nested video player stack. | The exact moment the video reaches Depth 9 ('Base case') at 00:46.0, hits the absolute bottom of the call stack, clicks 'return', and violently unwinds every single genre layer back out in reverse order. |
| 6 | [@eyadnour](https://x.com/eyadnour/status/2108314868189172216) | explainer | 106 s | An interactive explainer video demonstrating how QR codes store data, handle error correction, and repair themselves when damaged. | The 3D paper QR code literally getting chunks bitten and torn out with real-time damage percentage counters (0:58 - 1:07) |
| 7 | [@heyiamnick](https://x.com/heyiamnick/status/2109174851412119558) | motion | 30 s | A continuous 30-second motion design showreel introducing 'CLAUDE' through transforming technical blueprints, wireframes, and holograms. | The UI panel activation at 14.5s where bars and toggles transform dynamically to music beats |
| 8 | [@kloss_xyz](https://x.com/kloss_xyz/status/2103652674336067876) | explainer | 172 s | A cinematic, 83-year historical timeline explainer of artificial intelligence milestones from 1943 to 2026. | The 1943 neuron firing pulse expanding into an entire swirling neural galaxy at 2:37 |
| 9 | [@loicRambo](https://x.com/loicRambo/status/2103428454355980558) | motion | 20 s | A seamless 20-second motion graphics showreel depicting the complete cycle of human life from birth to death and looping back. | The final transition at 18.2s where the elderly characters dissolve back into the horizontal line as the heartbeat flatlines, seamlessly looping to the beginning. |
| 10 | [@marklaunches](https://x.com/marklaunches/status/2103811146411041046) | motion | 44 s | A viral promo video for a pedometer app that gamifies step counting through races and team mountain climbs, combining a cinematic minimalist aesthetic with emotional storytelling. | The final summit celebration at 00:35.000 where all 5 avatars reach the peak, confetti/flags pop, and 'SUMMIT TOGETHER' glows in massive neon letters. |
| 11 | [@melvynx](https://x.com/melvynx/status/2103714680577638493) | motion | 45 s | A dynamic 45-second motion graphics promotional video for Lumail (by @melvynx), contrasting outdated email marketing tools with AI-native workflows. | The 10s-14s grid transformation where thousands of black contact dots dynamically turn into hollow outlines and red open/unopened indicators. |
| 12 | [@miskinho_](https://x.com/miskinho_/status/2103847584531956105) | motion | 15 s | A sleek, Apple-style product showreel demonstrating how Quetzal transforms a single idea into scheduled, published, and optimized multi-platform social media posts. | The 3D card fan-out at 04.0s where one central post smoothly multiplies and fans out into branded formats for 6 different social platforms. |
| 13 | [@nolkeeg](https://x.com/nolkeeg/status/2103841917603635633) | motion | 45 s | A high-end cinematic motion graphics short film exploring the staggering scale of what happens in the universe in just one second. | The lightning storm section (020.000 - 025.000) where lightning bolts strike the 3D Earth in precise sync with audio crackles and fast-counting statistics. |
| 14 | [@nummanali](https://x.com/nummanali/status/2103565570310340931) | motion | 62 s | A high-energy, data-dense motion graphics visualization of 2026 large language model progression from January to September, tracking 101 releases, benchmarks, and capabilities. | The 3D orbital helix spiral filling up with 101 glowing colored nodes as months progress (0:09 - 0:35) |
| 15 | [@salmanr2d2](https://x.com/salmanr2d2/status/2103608284825661615) | explainer | 47 s | A fast-paced historical explainer video tracing the evolution of money from barter to stablecoins, created with Opus 5.5 and Remotion. | The dramatic color inversion and time-acceleration at 00:25 where historical cards blur by in reverse before stopping at the hourglass 'TODAY' and shifting to dark-mode stablecoin speed. |
| 16 | [@twoclipping](https://x.com/twoclipping/status/2103835273813496100) | 3d | 29 s | An Apple-keynote style interactive web-to-physical print mockup animation showcasing photo relighting, UI morphing, and product ordering in one continuous take. | The e-commerce order sequence morphing seamlessly from button states ('Ordered' -> 'Printing' -> 'On its way' -> checkmark) at 19.5s - 21.5s |
| 17 | [@vahidf24](https://x.com/vahidf24/status/2103258346690121886) | motion | 70 s | A slick, dark-mode SaaS product demo showcasing Evalyze, an AI tool for startup fundraising. | The interactive email drafting sequence at 0:36-0:48 where AI highlights source tags (from deck vs. investment history) and edits text in real time. |
| 18 | [@wani_shola](https://x.com/wani_shola/status/2103769906638459278) | motion | 102 s | A high-end developer relations portfolio showreel showcasing open-source contributions, technical writing, and AI tooling built with Remotion. | The interactive AI chat typing sequence at 00:36 where real portfolio questions and answers generate instantly. |
| 19 | [@0xValure](https://x.com/0xValure/status/2103603025579331584) | explainer | 10 s | A high-end, futuristic tech brand reveal video for PayBox featuring a search bar prompt, kinetic typography, and a 3D isometric cube logo animation. | The 3D cube solving and locking into isometric alignment inside the targeting reticle with HUD data readouts at 4.5s - 6.0s. |
| 20 | [@AnnaCher___](https://x.com/AnnaCher___/status/2103571096549433425) | motion | 42 s | A Dribbble-level UI motion promo for Sprites.ai showcasing continuous single-element morphing through ad management states. | The liquid tab indicator sliding across channel tabs with leading-edge spring stretch (00:08.500) |

---

## 11. Files

- `PLAYBOOK.md`: this file.
- `data/videos.jsonl`: the full frame-by-frame notes for each video (hook, every beat with timestamps, palette, fonts, transitions, music arc, reusable techniques, scores), one JSON object per line.
- `data/index.csv`: one row per video (creator, link, type, length, hook type, score, one-line summary) for browsing in a spreadsheet.
- `scripts/refs.py`: search the notes: `python3 scripts/refs.py "3d product reveal"`.

*Credits: videos and prompts by their creators on X (linked above and in every record); archive collected by Skillry / [@yihui-dev](https://github.com/yihui-dev/awesome-opus5-5-videos). Analysis by Google Gemini; playbook written with Claude.*
