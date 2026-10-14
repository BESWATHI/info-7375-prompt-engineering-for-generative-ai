# FRICTIONAL — what went wrong, and what I did

Everything below really happened in the build session on **2026-10-14** (times are local EDT, from file
timestamps and logs). Nothing is invented. Entries are in order. "I" is me (Revan); Claude Code ran the
commands and wrote the fixes in my session, as described in SOURCES.md.

---

**2026-10-14 · ~16:10 — `./setup` fails on a fresh clone.**
I ran the toolkit's readiness check right after cloning, and it stopped with "ElevenLabs reference found —
this toolkit is Kokoro-only" and exit code 1. The ten flagged files are example films inside the toolkit's own
`youtube/brutalist/` folder, not mine. It happened again after `./setup --install` (16:26): every download
finished, but the readiness table never printed. **What I did:** checked readiness by hand instead, with the
Python imports (Manim 0.20.1, ManimPango 0.6.1, kokoro-onnx, faster-whisper) and the toolkit's own Kokoro smoke test.

**2026-10-14 · ~16:20 — My brief claimed something Money Map already does.**
The first draft of the brief said a sender "can't ask a follow-up like 'what if I pay by debit card?'". The
Money Map screenshot shows a **Debit Card** filter, so that was wrong. **What I did:** replaced it with a
plain-words "why" question, in the brief and in beat B01, before anything was rendered. Logged in
`FACTCHECK.md` row 5.

**2026-10-14 · ~16:20 — Prices moved while I was making the film.**
Money Map's stablecoin route cost $7.42 for $1,000 when the page was first read (stablecoin prices "updated
15:10 EST"). In the screenshot taken at 16:20 EDT it was $8.99, and Wise ($7.54) had become cheapest. **What I
did:** kept the mock-up's numbers tied to the one dated screenshot. I then used the change itself as the
evidence for my project risk (beat B12): live prices make "known answers" go stale.

**2026-10-14 · 16:26 — Kokoro could not speak.**
The Kokoro smoke test failed with `Error processing file '/Users/runner/work/espeakng-loader/…/phontab'`. The
pip package `espeakng-loader` 0.2.4 looks for its data at a path from the machine it was built on. Two fixes
did not work: setting `ESPEAK_DATA_PATH`, and copying the data to a folder with no spaces and pointing
phonemizer at it. **What worked:** `brew install espeak-ng` (16:27) plus
`PHONEMIZER_ESPEAK_LIBRARY=/opt/homebrew/lib/libespeak-ng.dylib`, saved in `build/env.sh`. The smoke test then
passed (mean volume −21.7 dB).

**2026-10-14 · ~16:30 — First narration was 4:05, over the 4-minute limit.**
**What I did:** trimmed nine lines (612 words), which got it to 3:56, still too close. Then I used Kokoro's own
`--speed 1.05` option, which gave 3:49.

**2026-10-14 · ~16:30 — The show-tell template conflicts with the assignment.**
The skill's default bookends open with the instructor's stand-in narrator greeting, end on a spoken outro
with the instructor's channel handle, and use the instructor's portraits for any person. The outro card
(`ClaudeTitleOutro`) hard-codes the handle, with no way to change it. **What I did:** opened with my own
first-person greeting ("Hola. I'm Revan…"), drew my own end card in Manim, and showed no people.
I also dropped the Claude.ai "Your Turn" composer, so the film shows no Claude interface at all.
**Cost:** the toolkit's bookend check reports 2 failures on the outro. I left them failing rather than
editing data to satisfy the checker; see `gate-reports/GATE-SUMMARY.md`.

**2026-10-14 · ~16:36 — Layout audit caught two problems before rendering.**
B05's source label ran past the safe area, and B09's "step 1" label sat on a moving shape. **What I did:**
moved both, and re-audited until clean.

**2026-10-14 · 16:42 — Gate V failed the first full build.**
Two blocking defects: B00's screenshot filled 55% of the safe area (just under the minimum), and B07's World
Bank tag crossed the right safe edge. **What I did:** enlarged the screenshot, moved the tag, archived the
old clips in `_superseded/`, and re-rendered only those two beats. Gate V passed at 16:45 (0 blockers, 0 majors).

**2026-10-14 · 16:45 — The "synthetic voice" note was too small to read.**
I had put it in the opening card's banner, which the component draws at 18 px and 62% opacity. **What I did:**
moved it to the same component's 28 px full-ink label ("Synthetic voice (Kokoro) · words by Revan") and
re-rendered the opening (16:47).

**2026-10-14 · ~16:50 — Project change: data access is settled; three answers were missing.**
The film had said I would "ask the MIT Digital Currency Initiative first" whether I could use Money Map's
data. I can use it, so I removed that beat. Checking the film against the seven questions showed gaps:
- Q4 never said what a reviewer could conclude or what evidence would back it, so B13 was rewritten to say it.
- Q2 named alternatives but not the benefit to a sender, so B07 now says it.
- Q7 said "a mix" without why I picked the project, so B14 now says it, in a line I confirmed.

Five beats were re-voiced and re-rendered (17:03).

**2026-10-14 · ~17:10 — Second audience added.**
I added researchers and policymakers who study remittance costs as readers (B08 and brief Q3). The first
wording pushed the film to 3:57, so I shortened it to stay at 3:56. I did not claim Remnix covers other corridors:
it covers USD→Mexico only.

**2026-10-14 · 17:24 — The master check skipped its duration test.**
`master_check.py` passed, but its notes say the duration test was skipped because
`runtime/scripts/clock_check.py` is missing from the toolkit checkout. **What I did:** checked by hand. The
master was 235.8 s vs 235.5 s of measured narration, the last 0.9 s is silent (−91 dB), and every clip is
within 0.05 s of its audio.

**2026-10-14 · ~17:30 — Honesty pass found lines that made Remnix sound built.**
Reading every narration sentence turned up:
- 7 lines that sounded built: present tense or no verb in B04, B07, B09, B10, B11 and B13, and B01's "senders
  *often* ask…", which is a claim about users with no data behind it.
- 2 drawings with check marks that looked like results (B09, B13).

**What I did:** changed them to "will", "might", "planned" and "how you'd know". Then I re-voiced 9 beats,
re-drew 8, rebuilt the master (17:36, 3:56) and re-ran every gate. All pass except the 2 intentional bookend items.

**2026-10-14 — Pronunciation was checked by ear, not by machine.**
The skill suggests a Whisper transcript to catch Kokoro mispronunciations. I didn't download a Whisper model.
I watched the review cut myself and asked for no pronunciation fixes.

**2026-10-14 · ~17:50 — My full name was in a folder that stores none.**
Before pushing, I read the course repo's `fall-2026/README.md`: "No IDs and no full names are stored here."
The film said and showed my full name (opening line, terms card, end card) and so did four documents. **What I
did:** switched everything to "Revan C", re-voiced and re-rendered the three beats that carry my name, rebuilt
the master and re-ran the gates, so the Canvas and GitHub copies stay identical. Only the Canvas zip's file
name keeps my last name, because the assignment requires it.
