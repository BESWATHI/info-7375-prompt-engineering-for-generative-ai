# BUILD-PROMPT — Readback pitch film

Prompts and commands only; no conversation transcripts. The film was built in one Claude Code session (2.1.283, Opus 5.5) on 2026-10-14, driven by the prompt below and by the amendments listed after it.

## 1. The build prompt (my prompt, verbatim)

Placeholders as filled in during the session:

| Placeholder | Value |
|---|---|
| LAST_NAME | Ravi |
| last-initial | r |
| REPO | `aravindravi7/prompt-engineering-and-agentic-ai` (fork of `nikbearbrown/info-7375-prompt-engineering-for-generative-ai`); branch `final-project-film-aravind-r` |
| BRUTALIST_PATH | `Assignments/A01/brutalist.art` @ `cd4bf20` |
| WEEK1_FOLDER | `fall-2026/aravind-r/week-01-video` |
| TITLE | Readback |
| WEEK1_LINK | https://github.com/nikbearbrown/info-7375-prompt-engineering-for-generative-ai/pull/8 (open) |
| WEEK2_LINK | https://github.com/nikbearbrown/the-reallocation-engine/pull/23 (open, not merged) |

````text
# Claude Code prompt — INFO 7375 Final Project Pitch Film

You are helping me (Aravind {{LAST_NAME}}) build my INFO 7375 Final Project Pitch Film and its submission folder. The assignment description governs everything; where this prompt and the assignment disagree, the assignment wins, and you tell me about the conflict. Work in phases. At every **STOP**, halt, summarize what you did and what you need from me, and wait. Never skip a STOP. Never make a judgment call that the rubric grades me on (wording of my claims, labels, which alternatives I looked at) without asking.

## Placeholders (ask me for any I left unfilled before Phase 0)

- `{{LAST_NAME}}`, `{{last-initial}}` (lowercase, for the GitHub path)
- `{{REPO}}` — the GitHub repo the course folder lives in
- `{{BRUTALIST_PATH}}` — the existing Brutalist checkout from Week 1
- `{{WEEK1_FOLDER}}` — my Week 1 submission folder (read-only reference)
- `{{TITLE}}` — working title (current candidate: "Second Reading")
- `{{WEEK1_LINK}}`, `{{WEEK2_LINK}}` — links to my Week 1 film folder and Week 2 Reallocation Engine PR, plus that PR's actual status (open / merged / not submitted)

## The project being pitched (context, not a script)

**Thesis.** PMs on AI features now write instructions that AI executes: a PRD a coding agent builds from, a system prompt that *is* the feature, and an eval rubric a judge model scores against. All three fail the same way: the PM knows what they meant, the model reads something else.

**Engine.** Send the same PM-written instruction to several independent judges (different models, or different role prompts), compare their interpretations, and turn each disagreement into a clarifying question in product language.

**Module 1 (what gets built): rubric stress testing.** A PM writes an eval rubric for an AI feature and labels outputs pass/fail. Several judges apply the rubric. The tool measures judge–PM agreement and judge–judge agreement, traces disagreements to the rubric clause that caused them, the PM revises, and agreement is re-measured on a held-out set. Modules 2 (PRDs) and 3 (system prompts) are future work and must be described only with "will".

**Case study.** A meeting-recap feature (decisions + action items) of the kind Google Meet, Zoom and Teams ship. It is *my* prompt running on Claude. It is not affiliated with any of those companies, and the film must never imply it is. No company logos anywhere. Inputs come from the public AMI Meeting Corpus (CC BY 4.0), whose scenario meetings are role-played product design teams and which ships human-written abstractive summaries with DECISIONS and ACTIONS sections.

**Target role.** AI Product Manager. **Reader.** An AI PM hiring manager. **End user.** A PM who owns an AI feature and writes its eval rubric.

## Non-negotiable rules (apply in every phase)

1. **Honesty rule.** Past tense only for things that exist and that I can show. Everything else is "will". Never present proposed work as done.
2. **No invented numbers, users, employers, metrics, testimonials or results.** Never put a placeholder or example number on screen or in the brief. If a number doesn't exist yet, the film says it will be measured.
3. **Constructed material** (mock-ups, sketches, the fictional feature's PRD/prompt/rubric) is labelled `CONSTRUCTED` on screen.
4. **Real material** (AMI excerpts, terminal output, repo screenshots) is shown with the date I made or got it.
5. **Any Claude response shown is one actually received**, shown with its date and model.
6. **Labels are mine.** You never write, suggest or pre-fill pass/fail labels. Labels are committed to git *before* any judge runs, so the commit order proves it.
7. **Privacy.** No real résumé, contacts, application tracker, private conversation transcripts, credentials or caches in the film or the repo. Only public (AMI) or synthetic data.
8. **Brutalist.** Free pipeline only: local narration and rendering, no paid generation, no API keys for the film, no media account, no public upload. Work from the toolkit's own README; do not assume commands. Narration is first-person as me. Never use the instructor's name, persona or credit line.
9. **Gates.** Run the toolkit's own quality gates and keep their reports. A film that fails render-integrity gets fixed and re-rendered, never submitted over.
10. **Git.** Do **not** add `Co-Authored-By`, "Generated with Claude Code", or any other attribution trailer to any commit message or PR description. Before the first commit, check the current Claude Code docs for the setting that disables commit attribution and set it in this project's `.claude/settings.json` (older versions used `"includeCoAuthoredBy": false`). Regardless of the setting, verify with `git log --format=%B` after every commit and amend if a trailer slipped in.
11. **Alternatives.** The film may only claim a difference from a named alternative (Braintrust, Confident AI, GitHub Spec Kit's clarify step) after I have looked at it myself and logged what I saw in FRICTIONAL.md with a date. Phrase differences as "as far as I could find in their docs on <date>".
12. **Runtime 2–4 minutes.** Shorter only if the pitch is complete.

## Phase 0 — Setup

1. Create `fall-2026/aravind-{{last-initial}}/final-project-film/` inside a clone of `{{REPO}}`.
2. Add a `.gitignore` covering `.venv/`, `node_modules/`, `__pycache__/`, `.env*`, render caches and intermediates, the full raw AMI download, and anything the Brutalist README says is a cache.
3. Brutalist is already cloned and installed from my Week 1 assignment at `{{BRUTALIST_PATH}}`. Do not re-clone it, and do not move the submission folder inside it.
   - Run `git -C {{BRUTALIST_PATH}} status` and report any local modifications.
   - Record the current commit hash.
   - Run `git fetch` and show me what changed upstream since that commit. **Do not pull until I approve.**
   - After any pull, re-read the README end to end and report the exact install, build, narration, render and gate commands it documents, and whether a `show-tell` skill now exists in the checkout.
   - Record the final toolkit commit hash in README.md and FRICTIONAL.md, so the film can be rebuilt against the same version.
   - Read `{{WEEK1_FOLDER}}/FRICTIONAL.md` (read-only) for toolkit problems I already hit, and list any that apply here. Do not modify anything in the Week 1 folder.
4. Start `FRICTIONAL.md` with a dated first entry. Every later problem, workaround or decision gets a dated entry as it happens, not reconstructed at the end.
5. Apply the git attribution setting from rule 10.

**STOP.** Show me the Brutalist command list, whether show-tell exists, and anything that failed to install.

## Phase 1 — PROJECT-BRIEF.md

Write `PROJECT-BRIEF.md` (one page) from the draft answers in the appendix. Plain sentences, one section per question, in the assignment's order. End with two lists: **Exists today** and **Will exist**. "Exists today" contains only items that are real right now. Re-check it again after Phase 2.

Mark every sentence that came from the appendix draft with `<!-- draft -->` so I can see what I still need to rewrite in my own voice.

**STOP.** I will rewrite the brief in my own words, check the three alternatives myself, and fill in the Week 1/Week 2 evidence. Do not proceed until I say the brief is final.

## Phase 2 — The "exists today" slice (recommended; skip only if I say so)

This moves real items into "Exists today". Keep it small.

1. **Data.** Download the AMI manual annotations from the official site. Confirm from the corpus documentation that the summary annotations specifically are covered by CC BY 4.0, and log the finding with the date in SOURCES.md and FRICTIONAL.md. If they aren't clearly covered, STOP and tell me.
2. Select 10–20 decision-heavy segments of 10–15 minutes each from scenario meetings. Save transcripts and the matching human summaries under `case-study/data/sample/` with a README stating the source, licence, attribution and download date.
3. **Constructed docs.** Draft `case-study/constructed/recap-prd.md`, `recap-system-prompt.md` and `rubric-v0.md` (three to five clauses, including at least two subjective ones such as "unresolved disagreements are reported as unresolved"). Head each file with `CONSTRUCTED — drafted with Claude, edited by Aravind on <date>`.
4. **STOP.** I edit the rubric and the system prompt myself.
5. **Feature run.** Write `case-study/run_feature.py`, which runs the recap prompt on each segment using `claude -p` (headless Claude Code, my subscription, no API key) and saves each output as JSON with the date, `claude --version`, and the model reported in the output. If nested invocation fails, give me the exact command to run in another terminal. Commit the outputs.
6. **STOP.** I label every output pass/fail per rubric clause in `case-study/labels.csv`. I commit the labels myself. You do not touch labels.
7. **Optional, only if I ask:** a single judge pass with three judges (Claude with two distinct role prompts, plus one free local open-weight model via Ollama if I approve the install). Output an agreement table: per-clause judge–me agreement and judge–judge agreement. No revision or held-out step yet; those are "will".

**STOP.** List exactly what exists now, with paths and dates. Update "Exists today" in the brief to match.

## Phase 3 — beat_sheet.json

Build a beat sheet in the toolkit's expected schema (use show-tell format if it exists): one simple drawn picture per beat, one idea per beat, minimal on-screen text, narration carrying the explanation. Target 2:45–3:30, about 150 words per minute.

Beat order:

1. **Hook.** A PM writes a rubric; the judge reads it differently.
2. **Q1** What it is, plus the artifact form.
3. **Q2** Why anyone would care, with the alternatives and the specific difference.
4. **Q3** Who opens it and what they do in the first 60 seconds.
5. **Q4** What it proves about me, and the evidence planned.
6. **Q5** What's in, what's out, and what comes first, with how you'd know it ran.
7. **Q6** One concrete risk and the mitigation.
8. **Q7** Why this project: new skills versus existing skills, with evidence for the existing ones.
9. **Close.** "Exists today" versus "will exist", stated plainly.

Every beat carries extra fields:

- `question_ids` — which of the seven questions it answers;
- `claim_status` — `exists` / `will` / `constructed`;
- `evidence` — file path plus date for anything shown as real;
- `on_screen_label` — e.g. `CONSTRUCTED`, `Real output — Claude <model>, <date>`.

If the toolkit's schema rejects extra fields, keep them in a sidecar file, `beat_claims.json`.

**STOP.** I review every narration line.

## Phase 4 — Build the film

Use only the toolkit's documented commands. Local narration (Kokoro or whatever the README specifies). No instructor name or persona anywhere, including credits and file metadata. Any screenshot of real output must be taken from the actual files produced in Phase 2.

## Phase 5 — Gates and honesty audit

1. Run every quality gate the toolkit provides. Save the reports under `gates/`. If render-integrity fails, fix it, re-render, re-run the gates, and log each cycle in FRICTIONAL.md.
2. Check the runtime is between 2:00 and 4:00.
3. Write `gates/honesty-audit.md` (labelled as my own check, not a toolkit gate). It's a table with a row for every narration sentence and every on-screen claim, with columns for:
   - the sentence or claim;
   - its tense;
   - its `claim_status`;
   - the evidence path and date, or "will".

   Flag any past-tense sentence without evidence, any number without a source file, any constructed item missing its label, and any implied affiliation with Google, Zoom, Microsoft or Anthropic.
4. Spot-check frames: extract one frame per beat and confirm labels are legible and there are no logos.

**STOP.** Show me the gate results and every honesty-audit flag. I decide fixes.

## Phase 6 — Paperwork and submission

1. **README.md:** my name, `{{TITLE}}`, target role (AI Product Manager), exact runtime, and step-by-step rebuild instructions. Note that narration is synthesized locally from my own script.
2. **SOURCES.md:**
   - **Used:** Brutalist toolkit, Kokoro and other components with their licences, and AMI with its full CC BY 4.0 attribution.
   - **Made by me:** brief edits, labels, rubric, final narration.
   - **Contributed by Claude:** be specific — drafts of the brief, beat sheet, code, constructed docs.
   - **Third-party assets:** each with its licence.
3. **BUILD-PROMPT.md:** this prompt plus every command that rebuilds the film. Prompts and commands only, no conversation transcripts.
4. **FRICTIONAL.md:** confirm the entries are dated and in order, and that they include my alternative-checking entries.
5. **Check the folder contents.** It must contain:
   - README.md
   - the `.mp4`
   - PROJECT-BRIEF.md
   - beat_sheet.json (plus beat_claims.json if used)
   - BUILD-PROMPT.md
   - SOURCES.md
   - `gates/`
   - FRICTIONAL.md
   - `case-study/` (if Phase 2 ran)

   It must not contain caches, credentials, `.env` files, the full raw AMI download, or private data.
6. Commit and push to `{{REPO}}`, then check `git log --format=%B` for trailers.
7. Build `{{LAST_NAME}}_Aravind_INFO7375_FinalProjectFilm.zip` with contents identical to the GitHub folder (diff the zip listing against `git ls-files`).
8. Print the GitHub folder URL and the final commit hash for my Canvas submission.

**STOP.** Final check with me before I submit.

## Rubric checklist (verify each before the final STOP)

| Component | Points | Where it is satisfied |
|---|---|---|
| What and who | 7 | Q1 + Q3 beats; brief sections 1 and 3 |
| Unique value | 5 | Q2 beat; at least one alternative I checked personally; no invented market claims |
| What it proves | 5 | Q4 beat; skills tied to course topics; evidence plan; no overclaiming |
| Why this project | 4 | Q7 beat; new versus existing skills separated; existing skills linked to Week 1/Week 2 evidence |
| Scope and honest risk | 5 | Q5 + Q6 beats; in/out/first separated; one concrete risk; exists/will lists |
| Shown, not asserted | 4 | Pictures carry ideas; CONSTRUCTED labels; honesty audit clean; gates pass |
| Frictional | 5 | Dated entries throughout, written as I went |
| GitHub matches Canvas | 5 | Zip contents equal `git ls-files`; commit hash recorded |
| Relative quartile | 10 | Specificity, real evidence, honest verification. Polish counts only as communication |

## Appendix — draft seven answers (Claude's draft; I rewrite in my own voice)

[The appendix draft answers are superseded by the final `PROJECT-BRIEF.md` and are not repeated here.]
````

## 2. Amendments I gave during the session (all 2026-10-14)

- **Repo:** push only to my fork, never to origin. Branch `final-project-film-aravind-r`. Ask before opening a PR to origin.
- **Title:** "Readback" (tagline "Hear how AI reads your instructions before it acts on them."). Use `readback-pm` as the package/repo name, because `readback` is taken on PyPI. Add Maxim AI to the alternatives to check.
- **Attribution:** turn it off in the project and user Claude settings, and check `git log --format=%B` after every commit.
- **Toolkit:** don't pull; stay on `cd4bf20` as the final toolkit commit.
- **Outro and persona:** reuse my Week 1 patched `ClaudeTitleOutro` with my handle. Replace the show-tell "Liam, in for Bear" greeting and the "At Nik Bear Brown" outro with my own narration. No instructor name, persona or credit anywhere.
- **Brief:** my final brief replaces the draft. It names Maxim AI and orq.ai (checked 2026-10-14), keeps Spec Kit as the spec-side comparison, and drops Braintrust and Confident AI.
- **Q5 out:** "Readback will never rewrite a rubric itself; it only asks the PM clarifying questions, and the PM decides."
- **Step 2 change:** don't cut segments. Select 10 whole scenario meetings under ~35 minutes with a non-empty DECISIONS section.
- **Scope cap (deadline):** Phase 2 steps 1–5 only. Labels (step 6) and judges (step 7) stay "will".
- **Rubric edit pass:**
  - C1 becomes "Every decision listed in the AMI human summary's DECISIONS section appears in the recap in substance (paraphrase is fine). Reference: that meeting's summary.txt."
  - C5 stays as written; C2–C4 stay as drafted.
  - Leakage rule: the feature sees the transcript only.
  - Keep the 250-word cap.
  - Header: "CONSTRUCTED — drafted with Claude; clause decisions by Aravind, 2026-10-14".
- **Narration:** approved as written; voice `am_onyx`.
- **Honesty-audit fixes:**
  - F3: "the question Readback will ask".
  - F5: "That I'll evaluate…".
  - F8: "I think e-vals are becoming core…".
  - F9: B05 "planned" labels.
  - F7: kept as disclosed.

## 3. Commands

Run from `fall-2026/aravind-r/final-project-film/` unless a line `cd`s elsewhere.
- `ART` = `Assignments/A01/brutalist.art`, at `cd4bf20` with the patch applied.
- `REEL` = the absolute path of this folder.
- Run `source Assignments/A01/brutalist-env.sh` first.

**Data: AMI sample**

```bash
mkdir -p case-study/data/raw && cd case-study/data/raw
curl -sSL -o ami_public_manual_1.6.2.zip https://groups.inf.ed.ac.uk/ami/AMICorpusAnnotations/ami_public_manual_1.6.2.zip
shasum -a 256 ami_public_manual_1.6.2.zip     # b56e5babb2496b8795deeeda7e71178d7fbc9963f94276cf2a3f4b56ebbc9f9d
mkdir -p extracted && cd extracted && unzip -q ../ami_public_manual_1.6.2.zip && cd ../../../..
python3 -I case-study/scripts/select_ami_sample.py case-study/data/raw/extracted case-study/data/sample 10
```

**Feature run** (headless Claude Code on my subscription; no API key). It writes new outputs, and the committed ones from 2026-10-14 are the record:

```bash
python3 -I case-study/run_feature.py            # all 10 meetings → case-study/outputs/feature-run/*.json
```

**Toolkit patch**

```bash
git -C "$ART" apply "$REEL/toolkit-patches/ClaudeTitleOutro-handle-hideMascot.patch"
```

**Film**

```bash
python3 make_sheet.py
(cd "$ART" && python3 runtime/scripts/generate_audio_kokoro.py "$REEL")
python3 add_holds.py
(cd "$ART" && python3 runtime/scripts/align.py "$REEL")
(cd "$ART" && ./art run "$REEL" --height 1080)
(cd "$ART" && ./art final "$REEL" --height 1080 --out "$REEL/exports/landscape")
cp exports/landscape/aravind-r-readback-pitch.mp4 .
```

**Gates not run by `art run` / `art final`**

```bash
(cd "$ART" && python3 runtime/scripts/bookend_check.py "$REEL")
(cd "$ART" && python3 runtime/qc/factcheck_check.py "$REEL")
for c in B01_WhatItIs B02_Difference B03_FirstMinute B04_Proves B05_InOutFirst B06_Risk B07_WhyMe B08_ExistsWill; do
  (cd "$ART" && python3 runtime/qc/wcag_margin_check.py "$REEL/scenes.py" --class $c --quiet)
done
```

**Checks used along the way**

```bash
manim -ql -s --disable_caching --media_dir <scratch> scenes.py <SceneClass>      # low-res last-frame still
ffmpeg -ss <t> -i aravind-r-readback-pitch.mp4 -frames:v 1 gates/frames/<beat>.png   # frame spot-check
```

A whisper pronunciation check (`faster_whisper.WhisperModel("small.en")`) was run over `mp3/beat-*.mp3`.
