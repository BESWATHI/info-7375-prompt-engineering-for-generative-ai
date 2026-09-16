# Assignment — Build One Recipe Step and Film What Claude Code Did

**Due:** Canvas · **Points:** 100 · **Course:** INFO 7375 · Fall 2026

Assignments follow the ten-day cadence published in Canvas. The syllabus's 10% daily late penalty applies.

Read the [course AI policy](../prerequisites/ai-policy.md) and watch [AI Policy for Professor Bear's Courses | Using AI Responsibly in Class](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz) before beginning graded work.

## Your task

Start with **the-reallocation-engine** (https://github.com/nikbearbrown/the-reallocation-engine). Every recipe in `recipes/` has six steps, and every step names a script that does not exist yet. Each is marked `[TODO: DEV]` with a declared input, a declared output schema, and a destination folder. Pick one step. Have Claude Code build that script from its contract, run it for real against the repo's shipped sample data, verify it with the repo's own checks, and stop at the recipe's human gate. Then explain the result in a rendered film using Brutalist's **cc-explainer** workflow: a film that shows not just what the script outputs, but exactly what Claude Code did to get there.

This is a contribution to an existing repository, not a new project. Work in your own fork or course-authorized repository, in the namespaces `CONTRIBUTING.md` assigns you. Your branch name must begin with `contrib/2026fa-`, for example `contrib/2026fa-maya-k-oferta-step3`. Do not push directly to the instructor's repository.

Claude Code assistance is expected. Use your Northeastern access; no purchased API credits or paid voice or media service is required (the film uses the free Kokoro voice, Liam in for Bear). You remain responsible for the implementation and must be able to explain the code, the recipe contract, the tests, the session, and the film.

## 1. Predict

Before implementation, claim your step in the Canvas discussion thread as `<recipe> step <N>` (first claim wins). Then write a short brief in `CHANGE-BRIEF.md`:

- The recipe and step you chose, quoted from the recipe: the script path it names, its declared input, its declared output fields, and its destination.
- Which shipped sample data you will run it against (`data/examples/`, `search/examples/`, `resumes/`, `data/bls/compact/`) and why that data can support every declared output field. Where it cannot, say which fields will be `null` and why.
- What must remain unchanged: the maintained `scripts/` tree, `logs/RUN_LOG.md`, `chapters/`, other students' namespaces, and every other step of your recipe (they stay `[TODO: DEV]`).
- The phase gate your step ends at, and what a human would need to see to clear it.
- At least two predicted failure cases (a missing input file, a record that fails to parse, an empty input, a field the sample cannot support) and how you will check each.
- At least one prediction about what Claude Code will do wrong or out of scope on the first pass.

Retain the original predictions. Add later revisions rather than rewriting the record to make every prediction look correct.

## 2. Build It

### Read the governing files first

`SNICKERDOODLE.md` (the constitution), `DOMAIN.md`, `CONTRIBUTING.md`, `DATA_CONTRACT.md` (Zero-Conditions), `recipes/README.md`, `recipes/_shared.md`, and your recipe. Confirm the toolchain with `npm install`, `npm run doctor`, and `npm run verify` before you touch anything.

### Implement the step from its contract

Your script lives at `scripts/contrib/2026fa/<handle>-<recipe>-step<N>/` with at least one test (`unittest` for Python, `node --test` for JavaScript) and any fixture it needs. It must:

- accept the input the recipe declares and emit **every field in the declared output schema** as JSON;
- write its output under your contrib folder in sample mode, never into `data/verified/`, `data/raw/`, or `logs/`;
- handle the failure cases without crashing and without inventing a value. A count the data cannot support is `null` with a reason, not a plausible number;
- pass `node scripts/conformance.mjs <your folder>`, your tests, and `npm run verify`.

Do not hardcode the expected numbers. Do not weaken a check to pass it. Do not fetch anything from the network: the ATS scrapers, SEC downloads, BLS fetches, and liveness checks are out of scope, and the shipped samples are the input.

### Update the recipe, honestly

Copy the recipe to `recipes/cases/2026fa/<handle>-<recipe>-step<N>.md` with its `.card.md`. Your step's `[TODO: DEV]` becomes a pointer to your script. Every other step stays `[TODO: DEV]`. The frontmatter `status` may not exceed `RUNNABLE-SAMPLE`, and `attestation` stays `null` unless a named human signed it.

### Work in inspectable increments, in a real session

The film is cut from the actual session, so run Claude Code headless with a locked tool list and keep every transcript in `evidence/`:

```
claude -p "<what you typed>" --output-format stream-json --verbose --max-turns 40 \
  --permission-mode acceptEdits \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(node:*),Bash(npm:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/turn1.jsonl
```

Use `--session-id` on the first turn and `--resume` on later ones. Ask Claude to propose a plan before editing, then implement one bounded change at a time. For example:

```
Read SNICKERDOODLE.md, DOMAIN.md, and recipes/<recipe>.md. Locate step <N>: the script it
names, its declared input, its declared output fields, and its destination. Then read my
CHANGE-BRIEF.md. Propose the smallest plan to implement that script under
scripts/contrib/2026fa/<handle>-<recipe>-step<N>/ in sample mode against
data/examples/<fixture>.json, with a unittest covering a valid input, a missing file, and a
record that fails to parse. Do not edit yet.
After I approve a step, implement only that step, show the diff, run the test and
node scripts/conformance.mjs on my folder, and tell me what the phase gate requires a
human to judge. Do not touch any file outside my folder. Stop at the gate.
```

This is a prompt to Claude Code, not an installed shell command. You decide whether to accept the plan. After every run, verify with your own commands (`git diff --stat`, `wc`, your test, `cat` of the output JSON) and keep those in the transcript. Never let the agent proceed past the gate.

## 3. Use It

Run the finished script yourself from a clean checkout of your branch. Record the actual result of each check in `TEST-REPORT.md`, with the commit hash, Node and Python versions, and operating system:

| Check | Evidence to collect |
|---|---|
| Toolchain baseline | `npm run doctor` and `npm run verify` output before and after your change. |
| Contract conformance | The output JSON with every declared field present; `conformance.mjs` result on it. |
| Sample run | The real command and its real output on the shipped sample data. |
| Failure cases | Each predicted failure case exercised: the command, what happened, what the script emitted. |
| Scope | `git diff --stat` against `main` showing only your namespaced paths. |
| The gate | What the step produced, what a human must judge, and the run log entry recording the gate as reached and uncleared. |
| Automated checks | Your tests and any failed or updated test, with an explanation. |

Do not delete a failing assertion or weaken an expected result merely to obtain a green report. Include at least one documented inspect-and-revise cycle based on an observation from the session: something Claude Code got wrong, out of scope, or fabricated, and what you changed. A session with no correction is a session you did not look at closely enough.

Write the run entry as `logs/runs/2026fa-<handle>-1.md` using the template in `recipes/_shared.md`. Never edit `logs/RUN_LOG.md`.

## 4. Ship It — source and explainer

### Make one required Brutalist cc-explainer

Use the course-provided Brutalist **cc-explainer** skill. Ask Claude Code to read the installed `SKILL.md` and follow it; do not assume the skill name is a standalone executable. If your checkout lacks the skill, request the course-provided version before proceeding.

Make one landscape film that:

- Identifies the repository, the recipe, the step, and the contract you built against.
- Shows the actual session: what Claude read, what it wrote or changed, what it ran, and what **you** verified with your own command after each run. The VERIFY beat is your command, never Claude's own checkmark.
- Shows at least one correction cycle: a real failure and what changed to fix it.
- Ends its body on the phase gate: what the machine produced, what the human has to judge, and why the machine cannot judge it.
- Scores the agent's conduct (stayed in scope, read the recipe instead of guessing, touched nothing it should not have) and states plainly what remained human work.
- States what you tested, what remains uncertain, and one concrete next improvement.
- Identifies human and AI contributions and the source revision being demonstrated.

Use the Claude cold open, the idea and definitions beats, the session loop, CONDUCT and HUMAN, then Verdict → Your Turn → regular outro. Liam, in for Bear, narrates; Teardown register; no model names, version numbers, or prices spoken. Every tool name, path, diff line, and output shown in the film must be traceable to `SESSION.md`, the trimmed verbatim transcript, and recorded in `FACTCHECK.md`. Label reconstructed views and held frames accurately. Do not invent output the session did not produce, and do not change the script solely to conceal a defect in the film.

Follow the skill's native rendering and quality checks, then watch the final export. Duration should follow the explanation; there is no minimum runtime to fill. A vertical Short, paid media generation, a paid voice, and public YouTube publication are not required.

The film is part of the 60-point implementation-and-explanation category below. It is not a fifth grading category and does not substitute for a working script.

### Post the version on GitHub

Your submitted branch includes:

- `scripts/contrib/2026fa/<handle>-<recipe>-step<N>/` — script, tests, fixtures, sample output.
- `recipes/cases/2026fa/<handle>-<recipe>-step<N>.md` and `.card.md`.
- `logs/runs/2026fa-<handle>-1.md`.
- `course/2026fa/submissions/<handle>/` — `README.md` (step, starter credit, run instructions, changes, known limitations, film link), `CHANGE-BRIEF.md`, `TEST-REPORT.md`, `FRICTIONAL.md`, `SOURCES.md`, and the film's `beat_sheet.json`, `SESSION.md`, `evidence/`, `FACTCHECK.md`, `BUILD-LOG.md`, and prompts.
- One open PR from `contrib/2026fa-<handle>-<recipe>-step<N>` with the PR template fully filled. CI checks every box.

Keep MP3, MP4, and files over 25 MB out of GitHub. Store them in the designated course media storage and link them from your README. Identify the exact film by filename and SHA-256 checksum so its version can be checked. Test reviewer access to the source and media.

No real résumé, email, phone, tracker, or contact anywhere in the branch's history. Fictional personas from `search/examples/` and `resumes/` only. Deleting a file later does not remove it from history; the only fix is re-cutting the branch. CI scans the full branch diff.

Use commit messages that describe a meaningful change and its purpose or check. For example: `Implement oferta step 3 validator; add parse-failure test`. When useful, add a commit-body note distinguishing your decision from Claude's implementation. Commit count is not a measure of learning.

## 5. Verify and submit to Canvas

Run the script from a fresh clone of the revision you are submitting. Confirm the output JSON, the tests, and `npm run verify` reproduce, and that the film depicts that revision. Do not treat a working local folder as proof that everything was posted.

Submit a source ZIP of that same GitHub revision, excluding caches, `node_modules`, credentials, and large media, together with a short `SUBMISSION.md` containing:

```
Assignment: Build One Recipe Step and Film What Claude Code Did
Student:
GitHub handle:
Recipe and step:
Script path:
GitHub repository / branch / PR URL:
Submitted commit SHA:
Source revision shown in the film:
Node, Python, and operating system:
Final film URL and filename:
Final film SHA-256:
Summary of my changes:
Known limitations:
```

It is fine to render from a source commit and then make a final submission commit adding the film documentation. Identify both revisions and verify that the final commit does not change the demonstrated script. Put the final submitted SHA in the Canvas note; do not try to embed a commit's own SHA into that same commit.

Canvas, GitHub, and the film must refer to the same submitted work. Identify later changes as a new revision rather than silently replacing the submitted evidence.

## Rubric — 100 points

| Component | Points |
|---|---|
| Implementation and explanation | 60 |
| Frictional — honest log | 10 |
| GitHub version posting matching Canvas | 10 |
| Relative Quartile | 20 |
| **Total** | **100** |

### Implementation and explanation — 60 points

| Criterion | Points |
|---|---|
| Script: emits every declared output field from the declared input in sample mode (10); handles the failure cases without crashing or inventing a value (5). | 15 |
| Contract and scope: recipe case and card updated honestly with correct lifecycle frontmatter (6); diff touches only namespaced paths, other steps untouched (6); conformance and `npm run verify` pass (4); the gate is reached, recorded, and not cleared by the agent (4). | 20 |
| Verification: documented baseline and tests (5); real sample run and failure cases exercised with pasted output (5); evidence-based revision from the session and an honest limitation (5). | 15 |
| Brutalist cc-explainer: accurate account of what Claude Code did, traceable to `SESSION.md` (4); the session loop, a correction cycle, and the gate actually shown (3); conduct and human-work beats honest, limits stated (2); readable, audible final film using the required workflow (1). | 10 |
| **Subtotal** | **60** |

Award partial credit for demonstrated work within each criterion. Claims must be defensible; attractive presentation does not repair an incorrect explanation. A script that produces the right numbers by hardcoding them earns nothing in the first row.

### [Frictional](../prerequisites/frictional.md) — honest log — 10 points

In `FRICTIONAL.md`, record actual attempts, expectations, difficulties or checks, responses, and learning. Distinguish your work from the AI's work.

- 3 points: Specific, honest accounts of what you tried and what happened.
- 3 points: What you checked, changed, or learned in response, including unresolved questions.
- 2 points: Explicit human/AI contributions, including what you accepted, modified, or rejected.
- 2 points: Traceability to relevant commits, prompts, transcripts in `evidence/`, tests, or observations.

An unsuccessful attempt can earn full Frictional credit. More hours, more entries, or invented struggle do not earn extra credit. If something worked immediately, say so and explain how you checked it. Label retrospective notes honestly. AI may organize your notes; it must not manufacture experience or understanding.

### [GitHub version posting](../prerequisites/github-submission.md) matching Canvas — 10 points

- 4 points: Required, accessible source and documentation are actually posted in the assigned namespaces, with one open PR and CI green.
- 3 points: Canvas identifies the exact submitted commit and supplies the matching source files and clear run instructions.
- 3 points: Accessible film link, identified media version and checksum, and the film's beat sheet and `SESSION.md` correspond to the submitted source. No MP3 or MP4 in the repository.

### [Relative Quartile](../prerequisites/relative-quartile.md) — 20 points

Assigned after the instructor and TAs review the full comparison group. It compares specificity, substantive contribution, demonstrated understanding of the recipe contract and the governing rules, evidence, honesty about verification and about what the agent did, and professional communication. These are comparative considerations, not extra point categories.

Meeting the stated criteria can earn the other 80 points; it does not guarantee these 20 points. The course's announced comparison-group and tie/late-work rules govern placement. Production polish matters only as professional communication. A plain, precise explanation outranks a beautiful one that misrepresents the work. Paid-tool access and simply using Brutalist earn no automatic comparative bonus.

## You must be able to explain it

Use `SOURCES.md` to credit the repository, its governing documents, the sample data, collaborators, and tools. Describe what AI contributed to the script, the tests, the recipe update, the beat sheet, the visuals, and the narration, along with what you personally decided, checked, changed, or rejected.

The instructor or a TA may ask you to explain any part of your submission, including any line of the script and any beat of the film. Inability to explain reduces points under the relevant criteria. Misrepresenting authorship, verification, or what the agent actually did is an academic-integrity matter under the course AI policy video and the course/university policies.
