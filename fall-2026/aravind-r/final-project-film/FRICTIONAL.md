# FRICTIONAL — Final Project Pitch Film (Readback)

Machine: MacBook (Apple Silicon), macOS (Darwin 25.5.0). Claude Code 2.1.283.
Entries were drafted by Claude Code from the session as it happened; decisions marked (Aravind) are mine; I reviewed all entries.
Toolkit: brutalist.art checkout at `/Users/aravindravi/Desktop/Northeastern/Coursework/Fall 26/Prompt_Engineering_Agentic_AI/Assignments/A01/brutalist.art`, starting commit `cd4bf20904be4e7d63babd9622b17963c2361b27`. Final toolkit commit: `cd4bf20904be4e7d63babd9622b17963c2361b27` (not pulled; see the 2026-10-14 entry "decision: no pull").

Claude Code ran the setup steps on my machine at my request. Command output quoted below is copied from its terminal.

---

## 2026-10-14 — Phase 0: where the submission folder lives

- **Repo:** my existing local clone of the course repo, `/Users/aravindravi/Desktop/Northeastern/Coursework/Fall 26/Prompt_Engineering_Agentic_AI/info-7375-prompt-engineering-for-generative-ai`. Remotes: `origin` = nikbearbrown (never pushed to), `fork` = aravindravi7/prompt-engineering-and-agentic-ai.
- **Week 1 branch check:** `git log --oneline -- fall-2026/aravind-r/week-01-video` → one commit, `e3fc591`. `git branch -r --contains e3fc591` → only `fork/week-01-video-aravind-r`. The local `main` also points at `e3fc591`, which is not on `origin/main`.
- **Decision:** cut a new branch `final-project-film-aravind-r` from `origin/main` (`42d8c48`), so a later PR to origin carries only this folder and not a duplicate of the Week 1 commit (Week 1 is already open as its own PR, #8).
- **Problem:** checking the new branch out in the existing working tree would have removed the tracked Week 1 files from disk while I'm on it, and the Week 1 folder is my read-only reference. **Did instead:** `git worktree add -b final-project-film-aravind-r ../info-7375-final-project-film origin/main`. Same clone and object store, second working directory at `/Users/aravindravi/Desktop/Northeastern/Coursework/Fall 26/Prompt_Engineering_Agentic_AI/info-7375-final-project-film`. The branch's upstream was unset so a bare `git push` can't go to origin.

## 2026-10-14 — Phase 0: Brutalist checkout state (no pull yet)

- `git status` shows the Week 1 local changes still in place: `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` (my 3-line `handle` patch), `runtime/remotion/package-lock.json`, 3,413 deleted files under `youtube/` (parked in `A01/_toolkit-youtube-parked/` to get past the setup ElevenLabs guard), untracked `.venv/` and `media/`.
- `git fetch`: upstream moved `cd4bf20..519fcbb` (2026-10-12), 46 commits, 1,837 files changed. `cd4bf20` is an ancestor of `origin/main`, so a pull would be a fast-forward apart from my local changes.
- Things in that range that affect this film:
  - `requirements.txt` now pins `manim>=0.20,<0.21`. The comment says 0.18 renders each scene one frame short and `compile.py` then refuses the film. My venv has manim 0.18.1 on Python 3.12.14, so a pull means reinstalling.
  - `ClaudeTitleOutro.tsx` changed upstream and now says the handle is `HARDCODED — no prop, no lookup, no override`. A pull will conflict with my Week 1 patch.
  - `youtube/` upstream still holds archived scene sources that mention ElevenLabs, and `setup` still has the guard, so restoring `youtube/` would bring the Week 1 setup failure back.
  - `show-tell` already exists in my checkout. Upstream added a card family, prop packs and more gate traps to it.
  - New `professor-bear/` folder and `runtime/scripts/professor_bear.py` (instructor portrait library). I won't use it, since the assignment forbids the instructor's persona.

## 2026-10-14 — Phase 0: conflict between show-tell and the assignment

The show-tell skill defaults to "Liam, in for Bear" (Kokoro `am_onyx`), a spoken "At Nik Bear Brown" outro and the `@NikBearBrown` handle. The assignment says to narrate as myself and not use the instructor's name, persona or credit line. The assignment wins: the persona lines, the greeting and the outro handle will need replacing. How I handle the outro (patch again, or drop the stock outro) is a decision for after the pull question.

## 2026-10-14 — Phase 0: is the name "Readback" free?

- PyPI: `https://pypi.org/pypi/readback/json` → 200. `readback` 0.1.0 is taken (coldbricks/readback, "Validation via echo-confirmation"). `readback-pm` → 404, free.
- GitHub: a repository-name search for "readback" returned 141 repos (e.g. cbothner/readback, borisdiakur/readback). A search for "readback-pm" returned 0. `aravindravi7/readback` doesn't exist.
- **Decision (from my instructions before the check):** "Readback" stays the display title, and `readback-pm` becomes the package/repo name.

## 2026-10-14 — Phase 0: commit attribution turned off

- The current Claude Code settings reference says `includeCoAuthoredBy` has been deprecated since v2.0.62 and replaced by `attribution` (`commit`, `pr`, `sessionUrl`).
- Set `{"attribution": {"commit": "", "pr": "", "sessionUrl": false}}` in `~/.claude/settings.json` (new file) and in `Assignments/A03/.claude/settings.json`, the project this session runs from. I'll still check `git log --format=%B` after every commit.

## 2026-10-14 — Phase 0: assignment file missing

`Assignments/A03/ASSIGNMENT.md` doesn't exist (A03 was empty). The assignment text was pasted into the session, so the prompt check before Phase 1 will use that copy unless I add the file.

## 2026-10-14 — decision: no pull, stay on `cd4bf20`

**Decided (Aravind):** don't pull upstream. Stay on `cd4bf20904be4e7d63babd9622b17963c2361b27`, the version Week 1 already built on, and record it as the final toolkit commit for this film.
**Why it's workable:** the show-tell skill is already in this checkout. The working install from Week 1 (manim 0.18.1 on Python 3.12.14, Homebrew espeak-ng via `A01/brutalist-env.sh`) stays as it is, and the Week 1 outro `handle` patch doesn't conflict with anything.
**What I give up:** upstream's later show-tell changes (card family, prop packs, extra gate traps) and its Manim 0.20 pin. The film has to be rebuilt against `cd4bf20` with manim 0.18.x, not against current upstream.
**Side note:** this checkout's show-tell `SKILL.md` says "Short, 60–180 s". The assignment requires 2–4 minutes, and the assignment governs, so the film will run longer than the skill suggests.

## 2026-10-14 — Phase 1: brief drafted, not final

- Claude drafted `PROJECT-BRIEF.md` from the appendix answers in my build prompt. Every sentence taken from that draft is marked `<!-- draft -->`, and I'll rewrite them in my own voice.
- **Gaps left for me (TODO markers):** the date I check the alternatives; which one or two alternatives go in the film; which "out" item leads; confirming the Week 1 links open.
- **Flagged, not changed:** Q1's first sentence says Readback "shows" (present tense) although nothing exists yet.
- "Exists today" lists only real things: the draft brief, this log, the toolkit checkout, and the Week 1/Week 2 PRs (#8 and #23, both open). It says explicitly that nothing of Readback is built yet.

## 2026-10-14 — Alternative check: Maxim AI (Aravind)

   Looked at: getmaxim.ai FAQ "What is LLM-as-a-Judge evaluation" and the Maxim article "LLM as a Judge: a practical, reliable path...".
   What it does: multiple LLMs as judges with compared assessments; judge–human agreement via percent agreement, Cohen's kappa, Krippendorff's alpha; human annotation.
   Clause-level disagreement localization: not found in these docs.
   Effect on Q2: measuring agreement is not a differentiator; claim narrowed to clause attribution.

## 2026-10-14 — Alternative check: orq.ai (Aravind; added, found while checking Maxim)

   Looked at: docs.orq.ai "Align an Evaluator with Human Judgement" cookbook.
   What it does: compares a pass/fail evaluator against human labels, measures self-consistency by re-running, then proposes a rewritten evaluator prompt.
   Clause-level localization: the docs describe a rewritten prompt, not attribution to a specific rubric clause.
   Effect on Q2: Readback's difference is clause attribution plus returning a question to the PM instead of auto-rewriting, which matches my Q5 "out" item.

## 2026-10-14 — Alternative check: Spec Kit clarify (Aravind)

   Looked at: github.com/github/spec-kit.
   What it does: an optional /speckit.clarify step that resolves ambiguity in a spec before planning. Applies to specs, not eval rubrics.
   Effect on Q2: kept only as the spec-side comparison for the later PRD module.

## 2026-10-14 — Braintrust and Confident AI (Aravind)

   Not checked in time; removed from the brief's claims.

Note for all four entries: Claude found and summarized these pages; I opened each one on 2026-10-14 and confirmed the summary.

## 2026-10-14 — Q5 lead "out" item decided (Aravind)

My decision, in my words: "Readback will never rewrite a rubric itself; it only asks the PM clarifying questions, and the PM decides." It goes into the brief as the lead "out" item. "No UI" and "PRDs and system prompts are later modules" stay as secondary lines, still in draft.

## 2026-10-14 — brief marked final too early (Aravind)

Marked the brief final before editing it; Claude Code caught it by comparing file timestamps and didn't proceed. Brief stays draft until my rewrite is on disk.

## 2026-10-14 — decision: outro, greeting and persona (Aravind)

Outro: reuse my Week 1 patched ClaudeTitleOutro with my handle. Also replace show-tell's 'Liam, in for Bear' greeting and the spoken 'At Nik Bear Brown' outro line with my own narration. Drop the 'Liam' persona name. The Kokoro voice choice is decided in Phase 3. No instructor name, persona or credit anywhere in the film or its metadata.

## 2026-10-14 — Phase 1 complete: brief final (Aravind)

Replaced `PROJECT-BRIEF.md` with my final text, with no draft markers left. It was drafted by Claude from my inputs and reviewed by me (noted in `SOURCES.md`). Changes from the draft:
- Q2 now names Maxim AI and orq.ai, checked 14 October 2026, and narrows the claim to clause attribution plus returning a question to the PM.
- Braintrust and Confident AI are out.
- Spec Kit stays as the spec-side comparison for the later PRD module.

## 2026-10-14 — Phase 2: AMI annotations downloaded; summaries are CC BY 4.0

- **Downloaded** `ami_public_manual_1.6.2.zip` from the official download page into `case-study/data/raw/` (git-ignored; `git check-ignore` confirms it). 22,887,865 bytes, HTTP 200, `Last-Modified: Mon, 10 Apr 2017`, SHA-256 `b56e5bab…9f9d`.
- **Licence check:**
  - The licence page and the `LICENCE.txt` inside the zip both say "The AMI corpus and its annotations are released under … CC BY 4.0".
  - The annotation documentation lists abstractive and extractive summaries as annotations.
  - The zip contains them: 142 `abstractive/*.abssumm.xml` files (headings ABSTRACT, DECISIONS, PROBLEMS/ISSUES, ACTIONS) and the `extractive/` files.
  - **Conclusion:** the summaries are clearly covered, so there is no reason to STOP.
- **Small inconsistencies, logged rather than resolved:**
  - The download page says v1.6.2, but the README inside says "release 1.7" (16 June 2014). The download page says the annotations are unchanged since 2014 and only the licence changed.
  - `LICENCE.txt` opens with the CC BY 4.0 statement but includes the older CC "THE WORK (AS DEFINED BELOW)…" preamble before the 4.0 sections. Neither affects coverage.
- **Recorded in `SOURCES.md`:** licence, attribution, URLs and hash.

## 2026-10-14 — Phase 2 step 2: whole meetings instead of cut segments (Aravind)

- **Change:** my build prompt asked for 10–20 decision-heavy segments of 10–15 minutes each. I changed that to **10 whole scenario meetings under about 35 minutes with a non-empty DECISIONS section**.
- **Reason:** the AMI abstractive summaries are written per meeting, so a cut segment wouldn't match its reference summary.
- **What Claude Code had done before the change:** extracted the zip and inspected the formats. It was considering a window-based selection that used the summary-to-dialogue-act links (`extractive/*.summlink.xml`). That approach was dropped before any segment was cut.
- **Result** (`case-study/scripts/select_ami_sample.py`):
  - 73 meetings were eligible, across 35 teams.
  - The selection takes one meeting per team, ranked by DECISIONS count, and keeps the top 10: IS1004d, ES2006d, IS1009d, ES2008c, ES2010b, ES2011b, ES2013d, IS1003c, IS1005c, ES2007a.
  - The sample is 412 KB. The full rule is in `case-study/data/sample/README.md`.
- **Hit while building:** `meetings.xml` stores durations as decimals (`972.64`), so the first run crashed on `int()`. Fixed by parsing them as floats.
- **Borderline case:** ES2008c is 2098 s (34.97 min). It's inside the "under 35 minutes" cut, but only just.
- **Reproducibility:** a second run produced byte-identical files.
- **Phase 2 scope cap (Aravind, deadline):** steps 1–5 only. Step 6 (my labels) and step 7 (judges) are skipped and stay "will".

## 2026-10-14 — Phase 2 step 3: constructed docs drafted

- Claude drafted three files in `case-study/constructed/`: `recap-prd.md`, `recap-system-prompt.md` and `rubric-v0.md`.
- Each starts with the line `CONSTRUCTED — drafted with Claude, edited by Aravind on <date>`; I fill in the date after my edit pass.
- **Rubric v0** has five pass/fail clauses:
  - C1 decisions complete;
  - C2 claims trace to the transcript;
  - C3 action items have owners;
  - C4 unresolved stays unresolved (subjective);
  - C5 useful to someone who missed it (subjective).
- **The PRD** doesn't name any meeting product, and it says the feature is unaffiliated.
- **Next:** my 5-minute edit pass on the rubric and the system prompt (STOP), then the feature run.

## 2026-10-14 — Phase 2 step 5: script written, not run

- Re-checked before the run: `recap-system-prompt.md`, `rubric-v0.md` and `recap-prd.md` were still Claude's 13:55 drafts, and their headers still read `<date>`. My edit pass wasn't on disk yet, so Claude Code didn't run the feature.
- It wrote `case-study/run_feature.py` in the meantime:
  - It uses headless `claude -p --output-format json` with my system prompt as `--system-prompt`, tools disabled, no session persistence, and an empty temporary working directory. No API key is involved.
  - It doesn't use `--bare`, because that mode skips the subscription login.
  - It saves one JSON file per meeting, with the date, `claude --version`, the model(s) reported and SHA-256 hashes of the prompt and transcript.

## 2026-10-14 — Phase 2 step 4: my edit pass (Aravind)

- **C1 rewritten:** "Every decision listed in the AMI human summary's DECISIONS section appears in the recap in substance (paraphrase is fine). Reference: that meeting's summary.txt." Still objective-leaning.
- **C5 is my wording**, kept exactly. C2–C4 stay as Claude drafted them.
- **Leakage rule:** the recap feature gets the transcript only, never `summary.txt`. Only the C1 judge gets the AMI DECISIONS list. It's stated in `recap-prd.md` and `run_feature.py`; the script reads only `transcript.txt`.
- **Known tension:** 250-word cap vs C1 on dense meetings (IS1004d has 12 decisions). Kept deliberately; expected to cause C1 failures.
- **Header on all three constructed files:** "CONSTRUCTED — drafted with Claude; clause decisions by Aravind, 2026-10-14".
- My edits arrived as instructions in chat; Claude Code wrote them into the files.

## 2026-10-14 — Phase 2 step 5: feature run on all 10 meetings

- Ran `python3 -I case-study/run_feature.py`. It did one test meeting first (ES2007a, 17.7 s), then the other nine in the background, between 18:00:29 and 18:03:22 UTC.
- **Nested `claude -p` worked from inside this session**, so no second terminal was needed.
- **Every record** reports `claude-opus-5-5` and `2.1.283 (Claude Code)`, with `is_error: false`. All ten used the same system-prompt SHA-256 (`6a047888…`). That hash covers only the prompt text below the `---` line; my header edit isn't part of the prompt.
- **Recap lengths** by plain whitespace count, which includes headings and timestamps: 224–276 words. This is a crude count, not a rubric judgment. Pass/fail on any clause waits for my labels, which are out of scope for this deadline.
- **Updated** "Exists today" in `PROJECT-BRIEF.md` to list the AMI sample, the constructed docs and the feature outputs, with dates.

## 2026-10-14 — Phase 3: beat sheet drafted (awaiting my narration review)

- **Generator:** `make_sheet.py` writes `beat_sheet.json` in the show-tell format: the hesitant-writer hook, then 8 drawn Manim body beats (Q1 to Q7, then exists vs will), then the outro.
- **Extra fields** `question_ids`, `claim_status`, `evidence` and `on_screen_label` sit inline on each beat. The toolkit schema (`runtime/schema/beat_sheet.schema.json`) allows additional properties on a beat, so no `beat_claims.json` sidecar is needed.
- **Bookends:** `bookend_exempt: ["cold-open", "bvdt", "bhtf"]`. These are valid values in `bookend_check.py` and drop the Claude.ai composer and verdict card. The outro check can't be exempted, so BOUT keeps `ClaudeTitleOutro` with my handle (`channel_title` "Aravind Ravi · INFO 7375"). The terms card is left out, because my beat order doesn't include it.
- **Too long at first:** the first draft was 703 words, about 4:40 at 150 wpm, which is over the 4:00 limit. Tightened to 567 words.
- **Expected runtime:** Week 1's sheet measured 604 words over 203.5 s of audio including added holds, about 2.97 words per second. At that rate this script comes to about 3:10 before holds.
- **Kokoro pronunciation:** written out as "A I", "P M", "A M I", "Ork dot A I", "Tech for Dev", "Koine Arth" and "Claude Opus five point five". The whisper check comes after audio.
- **Still mine to decide:** the Kokoro voice. The sheet uses `am_onyx` as a placeholder (it's the toolkit default; the "Liam" persona name is dropped).

## 2026-10-14 — Phase 4: audio, pronunciation, scenes, paperwork

- **Narration approved as written (Aravind); voice `am_onyx`.** It's synthesized locally with Kokoro: `generate_audio_kokoro.py`, then `add_holds.py` (my Week 1 script, copied in) adds a 1.0 s hold after each beat and 1.5 s after B08.
- **First whisper check (base.en) found real mispronunciations:**
  - "A I" came out as "eye" ("an eye feature", "IPM").
  - "Maxim A I" came out as "Maxima I".
  - "to-dos" came out as "Todas".
- **Testing variants** with `small.en` showed that plain "AI", "AMI", "Maxim AI" in context, "E-vals" and "to-do items" are voiced correctly. I applied only those spelling changes; the wording is unchanged except "to-dos" → "to-do items".
- **New runtime:** 557 words, 171.6 s of speech, 181.66 s with holds (about 3:02).
- **scenes.py:** the show-tell iso kit pasted unchanged, plus 8 scenes, a midpoint guard (`P()`), a question marker top-left and an honesty tag bottom-left on every beat.
  - B08's excerpt is asserted as a verbatim substring of `case-study/outputs/feature-run/ES2007a.json`.
- **Low-res stills** (`manim -ql -s`) showed overlaps and fixes were needed:
  - "per clause" was on top of the table (B03).
  - "10 AMI meetings" was on top of the pages, and the B05 tag ran off-frame.
  - The B06 padlock shackle was hidden behind its body; fixed with `arc_center`.
  - The B07 PR tags collided.
  - The B08 excerpt overflowed its card.
  - The judge blocks were packed so tightly they'd fuse under GATE T.
  - All fixed and re-rendered.
- **Week 1 claim checked before it went in FACTCHECK:** "verified every on-screen number". Week 1's `verify_numbers.py` docstring says "Print every number that appears on screen in the video, from a real run", and every Week 1 FACTCHECK row is PASS, CORRECTED or EXEMPT.
- **Wrote** `FACTCHECK.md` (20 rows; future-tense lines marked EXEMPT), `SHOTLIST.md` and `PROMPTS.md` before the first `art run`, because Gate F refuses to render without them.
- **Render height 1080, not the skill's 2160:** that's what Week 1 used, and it's quicker against the deadline.

## 2026-10-14 — Phase 4: first `art run` blocked by Gate A

- **Broke:** `GATE A FAILED: B02_Difference has static errors — nothing rendered`. Running `static_scene_check.py` on each class showed the cause in B02 and B08: "explicit coord(s) outside the frame, e.g. (7.8,-3.0) in move_to". My `tag()` and `marker()` helpers placed text at `-6.0 + t.width / 2`. Gate A's stub gives text a placeholder width that's far too big (the same stub quirk as Week 1), so the computed x landed off-frame.
- **Fix:** `move_to([0, y, 0]).align_to([-6.0, 0, 0], LEFT)`. Real Manim left-aligns the text exactly, and the stub treats `align_to` as a no-op. All 8 scenes are then clean in Gate A. The log is kept as `gates/art-run-1-gateA-fail.log`.

## 2026-10-14 — Phase 4: render–gate–fix cycles (logs in `gates/`)

1. **`art-run-2`: Gate B (strict) didn't slot B05.**
   - Problem: "outside safe area": the B05 tag text box ran to x = 6.92, past the ±6.3 limit.
   - Fix: shortened it to "AMI data · CC BY 4.0 · downloaded 14 Oct 2026" and moved "CONSTRUCTED" under B05's rubric page. The B08 tag, which was almost as long, was shortened too; it now reads "real output · Claude Opus 5.5 · 14 Oct 2026 · grey = will". The model ID `claude-opus-5-5` stays in FACTCHECK and the output JSON.
2. **`art-run-3`: Gate V MAJOR.**
   - Problem: `low-contrast` 0.28 < 0.30 on the B02 midpoint frame, caused by the pale grey tool boxes.
   - Fix: kraft fill (`BOX_R`); the old clip was moved to `_superseded/`. **`art-run-4`: Gate V clean** (20 frames, 0 BLOCKER, 0 MAJOR).
3. **Watching the review cut found two problems no gate caught:**
   - **(a) The hook never corrected.** The hesitant writer stayed on "Does my feature pass the rubric". `BrutalistHesitantWriter` matches `triggerWords` one word at a time (comma-separated list), so my three-word trigger never fired. Changed the typed line to "Does the judge score my rubric", with `score` → `misread`. The narration is unchanged.
   - **(b) The stock outro draws the Claude mascot.** That conflicts with my no-logos / no-affiliation rule, and `ClaudeTitleOutro` had no switch for it. I extended my Week 1 toolkit patch with an optional `hideMascot` prop and set it on BOUT. The combined patch against `cd4bf20` is in `toolkit-patches/ClaudeTitleOutro-handle-hideMascot.patch`.
   - **`art-run-5`: all gates clean.** Frames confirm "Does the judge misread my rubric" and an outro with no mascot.
4. **`art-final-1`: GATE T FAIL.**
   - Problem: B02 "bbox-overlap §8.6b … two labels are printing on top of" each other. The tool names sat inside ink-outlined boxes, which breaks the show-tell law "labels beside objects, never inside an outline".
   - Fix: names moved above the boxes. Then `art-run-6` was clean, and **`art-final-2` gave GATE T: PASS**.
5. **Master:** `exports/landscape/aravind-r-readback-pitch.mp4`, copied to `aravind-r-readback-pitch.mp4`.
   - 1920×1080, 24 fps, H.264/AAC, 181.92 s (3:02).
   - SHA-256 `4ed0aba1…f8e60e`; `verified.json` status "ready".
   - Advisory only: "SKIN LINT: COLD OPEN LAW" on BIDEA, which the skill says to expect under `bookend_exempt`.

## 2026-10-14 — Phase 5: gates, runtime, honesty audit, frame spot-check

- **Toolkit gates on the final build, reports in `gates/`:**
  - F: paperwork present; `factcheck_check.py` clean, 20 rows.
  - L: clean.
  - A: 8/8 clean.
  - W: 8/8 clean.
  - B: 0 errors, 0 warnings.
  - V: 20 frames, 0 BLOCKER, 0 MAJOR.
  - T: PASS.
  - `bookend_check.py`: PASS.
  - Master: `verified.json` status "ready".
- **Runtime:** 181.92 s (3:02), inside 2:00–4:00.
- **Honesty audit** (`gates/honesty-audit.md`, my own check, not a toolkit gate): every narration sentence and on-screen claim is checked. It raises 10 flags, none applied yet: 5 medium (F3, F5, F7, F8, F9) and 5 low. **I decide the fixes.**
- **Frame spot-check:** one frame per beat from the master, in `gates/frames/` and `gates/frame-spotcheck.png`. Every label is legible, there are no logos, and no review overlays remain in the master.

## 2026-10-14 — Phase 5: audit fixes, then re-render and re-gate (Aravind's decisions)

- **Decided:**
  - Fix F3 (B03 "the question Readback asked" → "will ask").
  - Fix F5 (B04 "That I evaluate" → "That I'll evaluate").
  - Reword F8 as my own view (B07: "I think e-vals are becoming core to AI PM work").
  - Fix F9 (B05: "3 judges · planned" and a "planned" label before the commit line).
  - Keep F7 as disclosed.
- **Rebuilt:**
  - Re-ran `make_sheet.py`, Kokoro, `add_holds.py` and `align.py`. Only B03, B04 and B07 changed length; whisper hears all three as written.
  - Moved `manim/B03`, `B04`, `B05` and `B07` and the Manim media cache to `_superseded/`.
  - `art-run-7`: the four scenes were re-rendered; Gate B 0/0, Gate V 0 BLOCKER, 0 MAJOR.
  - Gate A and Gate W re-run on all 8 scenes, all clean (`gates/gateA-gateW-all-scenes.txt`).
  - `art-final-3`: GATE T PASS. Bookend check PASS; factcheck clean (row 20a added for the reworded B07 line).
- **New master:** 1920×1080, 182.46 s (3:02), SHA-256 `18f0d50c…581c131c`, `verified.json` "ready".
- **Updated:** `gates/honesty-audit.md` (second pass and a Resolution table) and `gates/frames/` + `gates/frame-spotcheck.png` (re-extracted from the new master).
