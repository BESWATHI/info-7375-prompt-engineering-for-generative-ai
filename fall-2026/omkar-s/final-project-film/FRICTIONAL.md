# FRICTIONAL — BiteCheck pitch film

Dated log of the build. **Who wrote what:** every entry marked **(Claude)** was written by Claude Code. In those entries the subject is named: "Claude" for work Claude Code did, "Omkar" for decisions I made. The section **"My entries — Omkar"** holds my own answers, quoted exactly as I typed them.

## 2026-10-11 — reading the assignment (Claude, from the chat record)
- Omkar pasted the Canvas text into Claude Code (desktop app) and asked for an explanation. Then he gave it his résumé, privately, so it could suggest projects that match his background. The résumé is **not** in this folder or the film.
- Claude suggested three options: (A) an agent that writes API tests plus a check that the tests catch bugs, (B) a document checker for the loan app, (C) extending the Reallocation Engine recipe. **Omkar chose A** (2026-10-12).

## 2026-10-12 — brief, evidence, alternatives (Claude)
- **Picking the system under test.** Claude chose Omkar's InstaLoan demo (`~/Desktop/LOS`) has clear, numbered rules (`MIN_MONTHLY_INCOME 15000`, `MIN_CREDIT_SCORE 650`, a stage-order map) and zero test files. It is not a git repository yet and is not public. The brief says so.
- **Real evidence, not claimed evidence.** Claude Code started the backend locally and sent three synthetic requests (`evidence/los_smoke_test.txt`). This wrote three rows into the local demo SQLite database (`backend/prisma/los.db`), which holds only synthetic data. At this point it was the only run the film called REAL. *(Updated 2026-10-13: the Stryker run was added; see below.)*
- **Alternatives.** Claude read the Schemathesis docs, the StrykerJS docs, and Postman/third-party pages on Postbot. None of the three had been run on the API yet, and the film said "docs only, not run". *(Resolved 2026-10-13: Claude Code ran Stryker; Postbot and Schemathesis stay docs-only and are labelled so.)*
- **Wording cut for honesty.** The B00 draft said Claude can write a suite of tests "in minutes". Nothing measured that, so Claude changed it to "can draft". FACTCHECK row 1.

## 2026-10-12 — Brutalist friction (Claude)
- **Two clones.** The Week 1 clone (`6a8380a`) has no `show-tell` skill. Claude made a fresh clone (`b21f625`), which has it, and linked in the Week 1 Python venv and Kokoro model files rather than downloading them again.
- **The show-tell skill conflicts with the assignment.** It requires a "Liam, in for Bear" greeting, Professor Bear portraits, a reconstructed Claude.ai composer, and a `ClaudeTitleOutro` whose handle is **hard-coded to @NikBearBrown**. The assignment says not to use the instructor's name, persona or credit line, and not to show a Claude response that wasn't actually given. So Claude:
  - wrote the narration in the first person for a Kokoro voice that is not the Liam default (`am_michael`, not `am_onyx`)
  - removed the portrait helpers from the pasted kit
  - left out the composer cards; the film ends on Omkar's name in B13
  - `bookend_check.py` **fails on OUTRO** by design (there is no ClaudeTitleOutro beat). It is a house-format check, not a render-integrity check. The report is included in `reports/`. `art run` does not call it.
- **"Narrate as yourself."** The voice is synthetic Kokoro (free, local), reading a first-person script that Claude drafted and Omkar approved. It is not Omkar's recorded voice. If the graders read "as yourself" as his actual voice, re-recording the 14 lines over the same beat sheet is the fix. *(Omkar decided on 2026-10-13 to keep the voice; see Q5.)*
- **No pronunciation check.** The skill recommends a whisper transcript to catch Kokoro mispronunciations. No speech-to-text model was installed, and Claude didn't download one at this point. "A P I" is spelled out in the narration on purpose. Omkar must listen to the whole film once, especially "Schemathesis", "Postbot" and "BiteCheck". *(Resolved 2026-10-13: the Whisper check ran (`evidence/pronunciation_check.txt`), and Omkar watched the full film; see Q4.)*
- **First stills.** `Scene.play()` refused bare labels. Claude fixed that in the helper by wrapping them in `FadeIn`. Five labels sat under or behind their objects (repo box, loan API ×2, correct code, API), so Claude moved them before any full render.

## 2026-10-12 — gates (Claude)
- **Review cut, first pass:** Gate A (static) 14/14 clean, Gate B (layout audit) 14/14 clean, Gate W 14/14 clean, Gate V 28 frames with 0 BLOCKER and 0 MAJOR.
- **GATE T blocked the final three times.** (1) B13: the labels "loan API" and "brief + film" sat inside their filled boxes, which GATE T reads as two overlapping labels. Claude moved them beside small blocks. (2) B01 and B08: "smallest text run 40px < floor 41px". Making the labels bigger didn't help. Measuring the midpoint frame with GATE T's own functions showed the culprit was the **wavy handwriting lines on the small pages**, not the words. Claude raised their wave height in those two beats (`tpage(..., amp=0.09)`). Since that changed the shared page helper, Claude re-rendered **all 14 scenes** from the current source, so `scenes.py` reproduces the film exactly.
- **Bookend check:** `bookend_check.py` BLOCKS on "no ClaudeTitleOutro beat", as expected. The outro hard-codes @NikBearBrown, which the assignment forbids. This is a house-format rule, not a render-integrity check, and `art run`/`art final` don't run it. The report is in `reports/bookend_check.txt`.

## 2026-10-13 — requirements audit (Claude)
- At Omkar's request, Claude checked every item in the assignment against the folder. Three gaps are fixed:
  - the brief was ~990 words (about two pages), so Claude cut it to ~660 words with the same seven answers and two lists
  - the layout report only kept the last scene, so I added `reports/GATE-SUMMARY.md` with every gate line from the final build
  - the course repo's `.gitignore` excludes `*.mp4`, so the GitHub folder can't hold the film; the README now gives the film's sha256 and says it is in the Canvas zip only
- The film did not change in this step (same sha256 as on 2026-10-12). It was re-rendered later the same day; see the next entry.

## 2026-10-13 — mock TA review and fixes (Claude)
- Omkar asked Claude to grade the pitch as a TA. It scored it **≈ 32/50 as it stood**. The biggest content gaps were (a) unique value: "isn't this just Claude + Stryker?" was never answered; (b) why-me: Omkar's existing skills had no evidence a grader could open; (c) the log was all Claude-written; (d) GitHub not posted.
- **(a) Stryker actually ran, instead of "docs only".** With Omkar's OK, Claude Code ran StrykerJS 8.7.1 on a scratch copy of `constants.ts` + `bre.ts` (the LOS folder was not touched). It made **92 mutants**. It does flip `<` to `<=` on the income check, but it made **zero mutants on the 15,000 value** (no numeric-literal mutator), its only stage-order mutant **empties the whole guard map**, and 18 only change message strings. That's now the concrete differentiator in B06 and brief §2. Scope note: `routes.ts` was not in the mutate set. Evidence: `evidence/stryker/`.
- **Honesty catch in Claude's own script.** A pronunciation rewrite had made B06 say "I ran Stryker myself", but Claude Code ran it. Claude changed it to "I ran Stryker on my loan rules with Claude Code" (FACTCHECK row 15).
- **(b) Public evidence.** None of Omkar's public GitHub repos is an API or TypeScript project, and Omkar chose to keep the loan app private. B12 and brief §7 now say plainly that the API-testing experience is private, and point to the one public thing that shows a related skill: his Reallocation Engine PR (nikbearbrown/the-reallocation-engine#37). B12's tag changed from PROPOSED to SELF-REPORT.
- **UVP person sharpened:** "an engineer reviewing a pull request full of AI-written API tests" (B00, brief §2).
- **Pronunciation.** With Omkar's OK, Claude ran Whisper-tiny on every beat. Spelled-out "A P I" lost its "A" (heard as "a pi" / "of pi"), and "Stryker I ran" was heard as "striker Iran". Claude switched to plain "API"/"AI"/"CI" and reworded. After re-voicing, every "API" transcribes correctly. The remaining differences are Whisper writing numbers as digits, plus tiny-model spellings of names ("striker", "bite check"). Log: `evidence/pronunciation_check.txt`.
- **Length.** The new lines pushed the film to 4:01, over the cap, so Claude trimmed B00, B06, B09 and B12. Final narration total: 236.6 s.
- Every beat was re-voiced or re-cued, so all 14 scenes were re-rendered and all gates re-run: Gate A 14/14 clean, Gate W 14/14 clean, Gate V 28 frames 0 BLOCKER / 0 MAJOR, GATE T PASS. New master 236.9 s, sha256 `ae0a9e4c013351ce…` (full hash in README).

## 2026-10-13 — brief trimmed (Claude)
- At Omkar's request, Claude cut `PROJECT-BRIEF.md` from ~755 to ~560 words so it fits one page. All seven answers and both closing lists are kept. The film is unchanged.

## 2026-10-14 — what the course repo accepts (Claude)
- Claude tested all 24 submission files against the course repo's current `.gitignore` with `git check-ignore`. Only `bitecheck-pitch.mp4` is blocked (rule `*.[mM][pP]4`), and the other 23 are accepted. Omkar decided not to force-add the film ("if github doesnt take then dont force add"). The GitHub folder therefore holds everything except the mp4. The film is in the Canvas zip, and the README gives its sha256 so the two can be matched.

## 2026-10-14 — attribution pass and push (Claude)
- Omkar's previous assignment lost marks for AI-typed work labelled as his. So Claude re-checked this one for the same pattern and found it in four places: (1) B03 said "On October twelfth I ran it" about a run Claude Code did. The narration now says "…with Claude Code"; B03 was re-voiced and re-rendered, and the gates were re-run: Gate V 0 BLOCKER / 0 MAJOR, GATE T PASS. New master 238.0 s, sha256 `235d146d608672f2…`. (2) The Claude-written entries in this log used "I" for Claude's work. Each now names who did it. (3) `SOURCES.md` listed that run under "What I made", so it moved to Claude's list. (4) The README said the narration was "in my words"; it now says the script was drafted by Claude and approved by Omkar.
- First push 2026-10-14 (commit `197f6da`, at Omkar's request). It was followed by this corrected version; the final commit hash is in the Canvas submission.

## My entries — Omkar
*On 2026-10-13 Claude asked me these questions in chat, and I typed the answers. The questions are Claude's wording. The answers are mine, pasted unedited (including lowercase).*

**Q1. Did you build the InstaLoan app with Claude's help?**
A: "Yes"

**Q2. Are mutation testing and evaluation design new to you?**
A: "Yes"

**Q3. Why did you pick option A (API tests plus bug-checking) over the loan document checker or the Reallocation Engine recipe?**
A: "because i have already worked on api testing"
*(Claude's note, not my words: this fits the "mix" answer in brief §7. API testing is the existing skill, and mutation testing and evaluation design are the new part.)*

**Q4. Watch the film once with sound. Anything to change?**
A: "i have watched the video". One thing I'd change: "nothing".

**Q5. Keep the synthetic voice, or re-record the narration yourself?**
A: "keep the voice"

**Q6 (2026-10-13). Look at the Stryker report. What do you notice about the income rule?**
A: "stryker flips the < sign but never changes 15000"
*(Claude's note: Omkar answered after reading the income-rule lines Claude showed him from `evidence/stryker/stryker_summary.txt`. The full report is `evidence/stryker/mutation.html`.)*

## Checklist — Omkar
- [x] Watch the final film once with sound. Done 2026-10-13; I told Claude "i have watched the video" and reported no problems.
- [x] Confirm or correct FACTCHECK rows 4, 23 and 24. Confirmed 2026-10-13.
- [x] Look at the Stryker report myself and write a dated line under "My entries". Done 2026-10-13 (Q6).
- [x] Write 2–4 short entries under "My entries" in my own words. Done 2026-10-13.
- [x] Decide on the voice: keep the synthetic first-person narration, or re-record the 14 lines myself over the same timing. Decided 2026-10-13: "keep the voice".
- [x] Commit `final-project-film/` to `fall-2026/omkar-s/` in the course repo and push. Done 2026-10-14 by Claude at my request; the final hash goes in the Canvas submission.
