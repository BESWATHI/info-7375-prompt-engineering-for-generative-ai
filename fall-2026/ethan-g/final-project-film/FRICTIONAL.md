# FRICTIONAL — DataSentry pitch film (working title until 2026-10-14: DefectBench)

Dated entries, newest last. Honest log of what got in the way and what I did about it.

---

This is Ethan Gomes. I have manually written this part in this Frictional.md file as a summary of all the work done.
Initially, I cloned the Brutalist repo on my local repo followed by selecting a relevant topic.
I have selected the project topic named "DataSentry". I researched the tech stack and requirements necessary for this project and generated the pitch film for this project. After that I added subtitles and re-rendered the pitch film several times to make corrections and changes in the pitch film.
All the prompts I used to generate the pitch video and make changes are listed.

### 2026-10-12 — Local Brutalist checkout was stale and missing the show-tell skill

**What happened.** The assignment points to the `show-tell` skill as the right format for a pitch. My local copy of
the toolkit didn't have it. It was 49 commits behind `github.com/nikbearbrown/brutalist.art` and had uncommitted edits
from an earlier project (Sep 26–27) in five files the update also changed.
**What I did (2026-10-14).** Dropped the old edits (that work had already been submitted) and fast-forwarded to `519fcbb`.

### 2026-10-12 — `./setup` reported everything blocked

**What happened.** `./setup` said Kokoro, Manim, captions, and slates were all blocked. Cause: the script calls whatever
`python3` is first on PATH. On this Mac that's the system Python 3.9, which has none of the packages. The project's
`.venv` (Python 3.11) had them all.
**What I did.** Activated the venv first. Rule for this machine: `source .venv/bin/activate` before any Brutalist command.

### 2026-10-14 — Manim version mismatch after updating

**What happened.** The update pins Manim to `0.20.x` (requirements.txt: 0.18 renders every scene one frame short, and
the compiler then refuses the film). My venv had 0.18.1.
**What I did.** `pip install -r requirements.txt` → Manim 0.20.1, ManimPango 0.6.1, Pillow 12.3.

### 2026-10-14 — `./setup --install` exits before checking anything (toolkit bug)

**What happened.** At `519fcbb`, setup's "no ElevenLabs" guard greps the whole repo and finds the word in the toolkit
author's own example films under `youtube/`. It exits 1 before printing the readiness table, on any machine.
**What I did.** Didn't edit the toolkit. Ran a temporary copy of `setup` from a scratch folder with only that guard
removed. Every real check still ran: all features READY, cost $0.00. Then `./art smoke` passed end to end (size, stream,
and audio gates on a decoded mp4), and I rendered one `ShowTellCard` at 4K and looked at a frame.

### 2026-10-14 — The house show-tell bookends conflict with the assignment

**What happened.** show-tell defaults to the instructor's persona ("Hallo. This is Liam, in for Bear"), the `am_onyx`
"Liam" voice, an `@NikBearBrown` label on the cards, and a spoken "At Nik Bear Brown" outro card. The assignment says
narrate as yourself, with no instructor name, persona, or credit line. The outro component (`ClaudeTitleOutro`)
hard-codes `@NikBearBrown` with no prop to change it.
**What I did.** First-person narration as me. A different stock Kokoro voice (`am_michael`). `@EthanGomes14` on the terms
card. No composer cold open, verdict card, or Your Turn (declared in `bookend_exempt`). The film closes on a drawn beat
(`BEND`) with the title and my name instead of the outro card. Consequence: the toolkit's manual bookend gate
(`bookend_check.py`) reports the missing `ClaudeTitleOutro`. That failure is expected and deliberate; see
`gate-reports/`.
**Still true.** The narration is a synthetic voice reading my script, not a recording of me.

### 2026-10-14 — The "unique" part of the pitch had to change

**What happened.** My first framing was "AI writes data-quality checks." While checking the alternatives I found that
Great Expectations' paid GX Cloud already has ExpectAI, which "generates suggested Expectations you can review, refine,
and approve" (GX blog, 2026-01-09). "AI writes checks" is not new.
**What I did.** Moved the value claim to what I didn't find in what I read: planting known defects and reporting a catch
rate per defect type, with a clean-data control. The film says "in what I read," not "nothing does this."

### 2026-10-14 — First narration ran 4:06, over the 4-minute cap

**What happened.** Measured audio (the master clock) came to 246 s.
**What I did.** Tightened ten beats over two passes without dropping any of the seven answers. Final narration:
234.8 s including the 0.8 s lead and 1.0 s tail.

### 2026-10-14 — Kokoro mispronunciations caught by a whisper check

**What happened.** A `small.en` whisper transcript of every clip flagged: "Claude Code" heard as "clawed code" (not a
real error: "Claude" and "clawed" sound the same, and the transcriber guesses the spelling from context; I confirmed
this later when `base.en` and `small.en` disagreed on the same clip), "A I written checks" heard as "I've written checks," "course skills" heard as "core skills," and "Great
Expectations" heard as "grade expectations" after "D B T and."
**What I did.** Reworded each line, re-voiced only those beats (`--only`), re-padded and re-measured, then transcribed
again until each one read correctly.

### 2026-10-14 — Visual fixes before the 4K render

**What happened.** On the low-resolution contact sheet: one label sat far from its object (B00), two parcels overlapped
(B05), a parcel ran into the "GX Cloud" label (B08), parcels in the risk beat didn't pass through the gate (B12), and a
dot floated in mid-air (B10). Gate A also failed the closing scene: "shapes never change."
**What I did.** Moved and re-pathed each one, then re-checked the stills. Added one new shape (a light on the parcel)
to the closing scene. Gate A, Gate W, and the layout audit then passed on all 16 scenes before rendering.

### 2026-10-14 — Gate V failed the first 4K cut on contrast

**What happened.** The first full render passed Gates F, L, A, W, and B, but Gate V (frame-level QC on the compiled
cut) failed 6 frames in B02, B04, B06, and B14 as "low contrast": ink-vs-background separation of 0.22 to 0.30
against a 0.30 floor. Cause: those frames were mostly pale grey rows, kraft trays, and ghost-grey slots.
**What I did.** Didn't override the gate. Darkened the table rows, set the kraft trays on a grey plinth (the skill's
documented fix; applied to B07, B08, and B13 too so the trays stay consistent), and darkened the "will exist" slots.
Ran Gate V's own contrast function on 1080p stills (0.52 to 0.73) before re-rendering. Moved the seven old clips to
`film/_superseded/run1/`. The second cut passed Gate V: 36 frames, 0 blocker, 0 major. The failed report is in
`gate-reports/earlier-runs/`.

### 2026-10-14 — Gate T blocked the final master on three beats

**What happened.** `./art final` runs Gate T (type lock) first. It failed B09 (no label on screen at the clip midpoint,
where the gate samples) and B10 and B14 (the drawn "handwriting" strokes on the pages measured 40 px, under the 41 px
floor at 4K).
**What I did.** Added a "hiring manager" label at the start of B09. Wrote a local `tall_scribbles()` with taller strokes
for B10 and B14. Re-ran the pre-flight gates, re-rendered the three scenes, and recompiled (Gate V still clean). Gate T
then passed 18/18 and the verified master was written: 3840×2160, 235.3 s (superseded by the 236.0 s master below).

### 2026-10-14 — Changed the opening line after the first master

**What happened.** I wanted the film to open with "This is a Final Project Pitch Film created by Ethan Gomes," then the
project name. That changed the narration of the opener (BIDEA) and made B00's "The project is called DefectBench"
repeat it.
**What I did.** Rewrote BIDEA, trimmed B00 to "DefectBench will be a workflow…", re-voiced only those two beats, and
re-padded and re-measured (235.5 s). Moved the old clips to `film/_superseded/run3/`, re-rendered the two beats, and
re-ran every gate and the final master: Gate V 0/0, Gate T PASS, master 3840×2160, 236.0 s. While re-checking B00, whisper wrote "clawed code" again. Two whisper models
disagreed on the same clip, which showed it's a homophone ("Claude" sounds like "clawed"), not a voice error. I
corrected the earlier entry above.

### 2026-10-14 — Adding subtitles: no way to burn them in

**What happened.** The film had no subtitles (the sheet's `caption_policy` was `none`). My Homebrew ffmpeg is built
without `libass`, so it has no `subtitles` filter and can't burn text into the picture. Burning them in would also
have meant re-encoding the verified master and putting caption text over the bottom labels in several beats.
**What I did.** Built the subtitles from the known narration, not a blind transcript: `align.py` timed each word,
`make_captions.py` grouped them into 86 cues (max 42 characters a line), shows spelled-for-the-voice words the way a
reader expects ("D B T" → "dbt", "G X Cloud" → "GX Cloud", "Expect A I" → "ExpectAI"), and asserts no narrated
word was dropped. The toolkit's SRT gate passed (86 cues, 0 errors). Embedded the track in the mp4 as a soft English
subtitle track, stream-copied: the video and audio MD5s match the verified master exactly. Spot-checked two cues
against the audio with whisper; both line up. Also wrote `.srt` and `.vtt` sidecars.
**Note.** I didn't re-run `make_sheet.py` to change `caption_policy`, because that would wipe the final build stamps
in `beat_sheet.json` (show-tell SKILL.md). The README records that subtitles exist.

### 2026-10-14 — Q4 didn't say what a reviewer could conclude

**What happened.** Checking the film against the seven questions, Q4 ("What does it prove about you?") named the four
course skills and the planned evidence but never said what a reviewer could fairly conclude. That part was only in
the brief.
**What I did.** Split Q4 into two beats. B10 keeps the four skills. The new B10A says: "Once it's built, a reviewer
could fairly conclude that I test an AI's output instead of trusting it. The evidence will be in the repo: the
scorecard, the log of every round, and the prompts behind each check." It's worded conditionally and in future tense so
it doesn't overclaim, with "planned evidence" on screen. That added about 14 s and pushed the film to 4:03, over the
cap, so I trimmed filler words from B01, B02, B04, B05, B06, B07, B09, B11, B12, B13, and B14 (no idea removed) and
landed at 235.3 s of narration. Re-voiced and whisper-checked every changed beat, re-synced each scene's cues to the
new wording, re-rendered the 13 affected scenes, re-ran every gate and the final master (Gate V 38 frames 0/0, Gate T PASS, master 235.8 s),
and re-timed and re-embedded the subtitles (86 cues, SRT gate PASS; video and audio MD5 unchanged by the embed).

### 2026-10-14 — Renamed to DataSentry; reframed "Why this project"

**What happened.** I renamed the project from DefectBench to DataSentry. I also changed my answer to Q7. The film had
said "Mostly, to show off… work I already know," which the rubric expects to be backed by evidence of earlier work. I
don't want to show proof of past work right now.
**What I did.** Q7 now says the project will help me land a Data Engineer or Data Analyst role and will highlight the
skills I'm working on (Python, pandas, pandera, Claude Code in a loop). That's an honest "learning" answer, so no
existing-skill evidence is claimed. New B13 picture: a "working on" tray fills with four skill blocks, and an arrow
carries them to the hiring desk labelled Data Engineer / Data Analyst. Re-voiced BIDEA, B00, B08, B13, and BEND. The
narration spells the name "Data Sentry" so the voice says it clearly; screen and subtitles show "DataSentry." A whisper
check heard "Data Century" in some clips. Kokoro's phonemes for "Sentry" (/ˈsɛntɹi/) are distinct from "century"
(/ˈsɛntʃɚɹi/), and base.en heard "Data Sentry" in isolated tests, so I treated it as transcriber bias, but I'll
listen to the opening myself to confirm. Old DefectBench clips and exports are in `film/_superseded/run5-rename/`.

### 2026-10-14 — Title card instead of the typed question

**What happened.** I wanted the opener to show the project name with one line about it, instead of the typed question
"Can Claude write checks I can measure." The toolkit's title-style card (`ShowTellCard`, `masked`) draws the word at
340 px. "DataSentry" ran to the card's edge, and the card's clip cut the descender of the "y" down to an outline
(seen on a test still).
**What I did.** Didn't edit the toolkit. Drew the opener as my own Manim scene (`BIDEA_Title`): "DataSentry," a ruled
line with one terracotta dot, and "Scoring AI-written data checks with planted defects." Narration and runtime are
unchanged. Gates A, W, and layout passed on the scene before rendering. The old typed opener is in
`film/_superseded/run6-title/`.

### 2026-10-14 — Moved the tick in B10A

**What happened.** In B10A the check mark sat above "tested, not trusted" instead of beside it.
**What I did.** Moved it to the left of the label, on the same line. Re-ran Gates A, W, and layout on the scene,
re-rendered only B10A, rebuilt the master, and re-embedded the subtitles.

### 2026-10-14 — Shortened the scanner's right leg

**What happened.** I wanted the scanner arch's right (far) leg shorter, hanging under the top bar. In the approved
prop both legs are the same height; the right one only looks higher because it stands at the back of the platform
(isometric perspective).
**What I did.** Didn't edit the toolkit prop. Made a film-only variant, `checkpoint-scanner-short`, in
`film/scenes_body.py` (`SHORT_LEG = 0.6`: the far leg's two faces end 0.6 units higher) and used it in B00, B05, and
BEND. Gates A, W, and layout passed on all three scenes. Re-rendered them, rebuilt the master, and re-embedded the
subtitles. The film with the original leg is kept at
`film/_superseded/run8-shortleg/DataSentry_Pitch_EthanGomes-original-leg.mp4` in case I revert.

### 2026-10-14 — Reverted the scanner leg to the original

**What happened.** After seeing the shortened right leg, I preferred the original prop.
**What I did.** Removed the `checkpoint-scanner-short` variant from `film/scenes_body.py`, so B00, B05, and BEND use
the approved prop again. Restored their original clips (same SHA-256 as before the change) instead of re-rendering,
re-ran the compile and every gate, rebuilt the master, and re-embedded the subtitles. The short-leg film is kept at
`film/_superseded/run9-revert/DataSentry_Pitch_EthanGomes-shortleg.mp4`.

### 2026-10-14 — Left leg of the scanner now sits under the top bar

**What happened.** In the approved scanner prop, the near (left) leg's square top face is drawn over the left end of
the top bar, so the leg looks like it pokes up through the bar.
**What I did.** Added a film-only variant, `checkpoint-scanner-under`, in `film/scenes_body.py`. It's the same prop
with the near leg's top face dropped, so the bar reads as resting on the leg. Used it in B00, B05, and BEND; the
right leg is the original. Gates A, W, and layout passed. Re-rendered the three scenes, rebuilt the master, and
re-embedded the subtitles. The film from just before this change is kept at
`film/_superseded/run10-leftleg/DataSentry_Pitch_EthanGomes-before-leftleg.mp4`.

### 2026-10-14 — Q2 now states the benefit outright

**What happened.** Q2 ("Why would anyone care?") named both alternatives and the gap, but the benefit to the person
using DataSentry was only implied.
**What I did.** Rewrote B08: "What I didn't find, in what I read, was a way to measure how good those checks are. Data
Sentry will tell a data engineer which bad rows their checks would let through." It's future tense and slightly
shorter than before. Re-voiced and whisper-checked B08, re-synced its two scene cues, re-rendered it, rebuilt the
master, and re-timed and re-embedded the subtitles.

### 2026-10-14 — The block passed in front of the scanner's top bar

**What happened.** As the block (the table) started sliding under the scanner, it was drawn over the top bar's left
end. The prop layers its parts as base, arch, block, near leg, so the block covered the bar.
**What I did.** Added a `scanner()` helper in `film/scenes_body.py` that sets the layering explicitly: far leg at the
back, then the block, then the top bar and its light, then the near leg in front. The terracotta dots on the block sit
just above it. Used it in B00, B05, and BEND, and checked zoomed frames at the start of each motion. Gates A, W, and
layout passed. Re-rendered the three scenes, rebuilt the master, and re-embedded the subtitles.

### 2026-10-14 — Framed the taxi data as an example

**What happened.** B02 presented NYC taxi trips as the dataset. I want it to read as one example of the public data
DataSentry can use.
**What I did.** B02 now says "It will start from public data, for example one month of New York City yellow taxi
trips…" Updated PROJECT-BRIEF.md to match. Re-voiced and whisper-checked B02, re-rendered it, rebuilt the master,
and re-timed and re-embedded the subtitles. Runtime is now about 3:58.
