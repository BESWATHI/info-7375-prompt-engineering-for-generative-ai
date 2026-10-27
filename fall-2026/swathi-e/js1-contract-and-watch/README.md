# Job-Search Agent 1 — The Contract and the Watch

Drafted by Claude Code from the committed records; reviewed by Swathi.

Labels used below: **record** = recomputable by anyone from the committed
files and code; **judgment** = a Claude verdict, never a fact; **my input** =
a decision or label made by me (Swathi).

## What the agent does

The agent watches one public job board, Databricks on Greenhouse, for Priya
Nair, a fictional F-1 OPT candidate targeting AI/ML and data engineering roles.
Each run fetches the board from an allow-listed host only, saves the raw
response as evidence, and reports only postings whose ids were not in the
previous run; the first run is a baseline that reports none. Each new posting
gets two verdicts: one from my written title-and-location rule (a record,
`CONTRACT.md`), and, only when asked with `--judge-live`, one from Claude
under my judge contract (a judgment, `JUDGE-CONTRACT.md`), whose reply must
pass a validator. It never applies, emails, messages, or logs in anywhere.

## Language, toolchain, versions

- Python, standard library only; no packages to install. Ran with Python
  3.12.2 (Anaconda); the test suite also passes with macOS's Python 3.9.6.
  Other versions not tested.
- Claude Code 2.1.308, installed with `brew install --cask claude-code`
  (stable channel, no auto-update), signed in with my Claude account.
- Model pinned to `claude-opus-5-5` for every `claude -p` call, and recorded
  with the model Claude Code reports.
- No API key is used: every Claude call runs with an environment holding only
  `HOME`, `USER` and `PATH`, so `ANTHROPIC_API_KEY` is never present.
- Only network host the code fetches from: `boards-api.greenhouse.io`.

## Commands

Run from this folder (`fall-2026/swathi-e/js1-contract-and-watch/`).
Everything is offline unless it says `--live` or `--judge-live`; offline
commands make no Claude call and print what a live run would do.

```bash
python3 -m unittest discover -s tests -v
```

```bash
python3 watch.py
```
Live fetch of the board, rule verdicts only (no Claude call). Add
`--judge-live` to also ask Claude about each new posting, or replay a saved
response as a labelled seeded run with `--from-file runs/raw/<file>.json`.

```bash
python3 watch.py --judge-report runs/reports/<report>.json --judge-live
```
Adds live Claude judgments to an earlier report's new postings, into a new
`*_judged.json` file.

```bash
python3 judge.py --fetch-posting 8546367002
```
Saves one posting's detail from the allow-listed host (no Claude call).

```bash
python3 judge.py --posting runs/postings/<file>.json
```
Offline: prints the exact command and message the judge would send. Add
`--live` for one real call.

```bash
python3 experiments/run_sampling.py
```
Offline plan of the sampling report's 20 calls; add `--live` to run them.

```bash
python3 experiments/run_prompt_experiment.py --set development
```
Offline plan; add `--live` to run. `--set held_out` must be named explicitly.

```bash
python3 experiments/score_experiment.py --set development
```
Scores measures A and B from the saved records (no Claude call).

```bash
python3 experiments/action_surface.py --mode file
```
Offline view of the file surface; `--mode agent` for the agent surface; add
`--live` to run. The chat surface is run by hand by pasting
`experiments/action_surface/chat_paste.txt` into a new claude.ai chat.

```bash
python3 labels/select_postings.py
```
Recomputes the 20 labeling postings and the development/held-out split
(seeds 7375 and 20261026); never overwrites `labels/LABELS.csv`.

## What actually ran

All times Eastern (EDT, UTC−4).

| When | What ran | Result | Commit |
|---|---|---|---|
| Oct 25, 21:17:50 | Live baseline of the board | 896 ids recorded, 0 reported as new | `6125288` |
| Oct 25, 22:24 | Two `claude -p` smoke-test calls ("reply OK"), from an empty folder | both returned OK; **not saved in the repo** | — |
| Oct 26, 10:20:47 | Second live run of the board (run by me) | 892 postings, 3 new | `2b15260` |
| Oct 26, 10:23 | Detail fetch for 8546367002 (offline judge input) | HTTP 200 | `996dac7` |
| Oct 26, 10:26:58–10:27:11 | Live judge on the 3 new postings, with their detail fetches | 3 replies, all accepted | `cf08060` |
| Oct 26, 12:40:53–12:41:17 | Detail fetches for the 20 labeling postings | 20 × HTTP 200 | `36f9842` |
| Oct 26, 22:13:07–22:15:09 | Sampling report: 5 development postings × 4 calls, baseline prompt | 20 replies, all accepted | `cc49592` |
| Oct 26, 22:38:10–22:41:53 | Prompt experiment, development set: baseline + revision × 10 | 20 replies, all accepted | `a12c802` |
| Oct 26, 22:43:58–22:45:33 | Prompt experiment, held-out set, once: baseline + revision × 10 | 20 replies, all accepted | `a9056ca` |
| Oct 26, 22:54:11 | Action surface 2, file (Read tool only) | 1 Read; reply accepted | `4d9a39a` |
| Oct 26, 22:54:37 | Action surface 3, agent (WebFetch + Write) | 2 WebFetch + 1 Write; reply accepted | `4d9a39a` |
| Oct 26, 23:07 | Action surface 1, chat (run by me in claude.ai, pasted back) | rejected: not valid JSON | `e069d8e` |

## Results

| Number | Value | Kind | Source |
|---|---|---|---|
| Postings in the baseline | 896 | record | `runs/raw/databricks_2026-10-25T21-17-50-0400.json` |
| Postings passing my rule (Revision 2) in the baseline | 8 of 896 | record | recomputable: `rule.py` on the baseline file |
| My verdict on those 8, after reading their descriptions | 0 fit Priya | my input | `FRICTIONAL.md`, Oct 25 |
| New postings in the second run | 3 (8908544002, 8902290002, 8029679002) | record | `runs/reports/databricks_2026-10-26T10-20-47-0400_live.json` |
| Rule verdicts on those 3 | 3 not relevant | record | same report |
| Claude verdicts on those 3 | 3 not_relevant (all replies accepted) | judgment | `runs/judge/` |
| My hand labels | 20 of 20 not relevant (development 10, held-out 10) | my input | `labels/LABELS.csv` |
| Sampling: verdicts across 20 calls | 20 of 20 not_relevant; 20 of 20 agree with my labels | judgment | `runs/sampling/` |
| Sampling: quotes that changed between calls | experience_found on 3 of 5 postings; authorization_found on 1 of 5 | record | `runs/sampling/` |
| Sampling: Compliance paragraph quoted as authorization_found | 15 of 20 calls | record | `runs/sampling/` |
| Experiment, development: measure A (verdict = my label) | baseline 10/10, revision 10/10 | judgment scored against my input | `experiments/results_development.json` |
| Experiment, development: measure B (authorization quote correct) | baseline 2/10, revision 10/10 | judgment scored by a fixed rule | `experiments/results_development.json` |
| Prompt kept | revision (A tied, B decided) | my input | `experiments/prompt_choice.json` |
| Experiment, held-out: measure A | baseline 10/10, revision 10/10 | judgment scored against my input | `experiments/results_held_out.json` |
| Experiment, held-out: measure B | baseline 1/10, revision 10/10 | judgment scored by a fixed rule | `experiments/results_held_out.json` |
| Action surfaces on 8546367002 | file: accepted, not_relevant; agent: accepted, not_relevant; chat: rejected (not valid JSON) | judgment (verdicts) / record (validation) | `runs/action_surface/`, `experiments/action_surface/comparison.md` |
| Least autonomy that suffices | file surface | my input | `experiments/action_surface/AUTONOMY-CHOICE.md` |
| Test suite | 50 tests pass, also with `claude` not on PATH | record | `tests/` |

Measure A cannot separate the prompts: all 20 of my labels are "not
relevant", so a judge that always answers not_relevant also scores 10/10.

## Known limits

- **Action-surface comparison, agent surface: the text it judged can't be shown.**
  The agent run (`runs/action_surface/agent_2026-10-26T22-54-37-0400.json`,
  commit `4d9a39a`) records each tool call's input but not the WebFetch
  output, so the text the agent actually judged was not saved and can't be
  shown. Its quote does appear word for word in the 12:40 ET Oct 26 saved
  description, and its reply passed the validator, but that does not show
  what WebFetch returned. Claude Code also reported a second model,
  `claude-haiku-5-5`, alongside the pinned `claude-opus-5-5` for that run.
  The runner was deliberately not changed after the run.

## Sign-off, driver's seat, and my own notes

- Sign-off and driver's seat: see [SIGNOFF.md](SIGNOFF.md).
- What I tried and what happened: [FRICTIONAL.md](FRICTIONAL.md).
- My least-autonomy choice and defense: [AUTONOMY-CHOICE.md](experiments/action_surface/AUTONOMY-CHOICE.md).
