# Ground Truth SQL — final project pitch film

**Riya Kapadnis** · `kapadnis.ri@northeastern.edu`
INFO 7375 — Prompt Engineering for Generative AI · Final Project Pitch Film

| | |
|---|---|
| **Working title** | Ground Truth SQL: an evaluation harness for text-to-SQL |
| **Target role** | AI Engineer (also readable for Data Analyst roles) |
| **Runtime** | **3:52 (232.0 s)** · 3840×2160 · 24 fps · 14 beats |
| **Film** | [`riya-k-ground-truth-sql.mp4`](riya-k-ground-truth-sql.mp4), in this folder and in the Canvas zip. sha256 `5cce0d4d…adad`, matching `gate-reports/verified.json`. The root `.gitignore` excludes `*.mp4`, so it was added with `git add -f` |
| **Narration** | Written in the first person by me; voiced by a **synthetic** local voice (Kokoro `af_bella`), not a recording of my voice |
| **Cost** | $0.00. Kokoro, Manim, Remotion and FFmpeg, all local. No API key, no account, no upload |

## What the film pitches

An evaluation harness that tells you, on your own database, which plain-English questions a
text-to-SQL model answers wrongly and why. The full answers to the seven questions are in
[`PROJECT-BRIEF.md`](PROJECT-BRIEF.md).

**What exists today** is a small first slice, and the film says so. That slice is
`evidence/run_slice.py` with 8 gold questions over the public Chinook database, plus an
execution comparator tested on 9 hand-written variants. **No model has been run yet.** The
film shows no model output, and every future part is said with "will" and stamped
`CONSTRUCTED · not built yet` on screen.

| Beat | Answers | On screen |
|---|---|---|
| BIDEA | (opening) | Title, name, course; the naive question corrected to the real one |
| BDEFS | (terms) | text-to-SQL, gold set, execution match |
| B00–B01 | Q1 What is it | database → question → rows; the repo's three parts (CONSTRUCTED) |
| B02–B03 | Q2 Why care | **real run**: a join mistake reports 4,667 vs 523; BIRD and Vanna compared |
| B04–B05 | (evidence) | **real run**: rows-not-text check, 9/9; the empty-gold bug I caught in my own answers |
| B06 | Q3 Who opens it | reviewer's first minute (CONSTRUCTED) |
| B07 | Q4 What it proves | contract, verification, failure taxonomy, repair loop (later) |
| B08 | Q5 In / out / first | Chinook in; chat app and write queries out; the slice first |
| B09 | Q6 What could sink it | I write both questions and answers; the second check and three runs |
| B10 | Q7 Why this project | existing skills vs new ones |
| BCON | conclusion | exists today vs still to build |

## Verify the evidence (about 1 second, offline)

```bash
cd evidence
python3 -I run_slice.py      # last lines: 9/9 and 6/9; exit code 0
```

`data/Chinook_Sqlite.sqlite` sha256 `bdf635be69850bd3be09c9a2dbeef7ddfb80036bd3ef3381383cd03b61e4a61a`.

## Rebuild the film

Full commands and prompts are in [`BUILD-PROMPT.md`](BUILD-PROMPT.md). Short version, with a
brutalist.art checkout at `22264a33` and its Python 3.11 venv:

```bash
cp -r reel/ <work>/riya-k-ground-truth-sql/      # make_sheet.py, beat_sheet.json, scenes.py, paperwork
cd <brutalist.art> && export PATH="$PWD/.venv/bin:$PATH"
python3 runtime/scripts/generate_audio_kokoro.py <work>/riya-k-ground-truth-sql   # regenerates the narration
./art run   <work>/riya-k-ground-truth-sql
./art final <work>/riya-k-ground-truth-sql
```

`reel/beat_sheet.json` is the sheet the master was built from (with measured durations). Running
`make_sheet.py` regenerates it without durations, which the audio step then restores.

## Quality gates

Reports are in [`gate-reports/`](gate-reports/). Summary:

| Gate | Result | Report |
|---|---|---|
| Gate F (fact check, shot list, prompts present before render) | passed, render allowed | `FACTCHECK.md` |
| Gate V (frame QC, 28 frames) | **PASS**: 0 BLOCKER, 0 MAJOR | `gate-V-REPORT.md` |
| GATE T (type size, contrast, kerning, 14 beats) | **PASS**: 0 FAILs | `TYPECHECK.md` |
| Layout audit (12 snapshots) | **PASS**: 0 errors, 0 warnings | `layout_audit.md` |
| Render integrity (`verified.json`) | **ready**, sha256 `5cce0d4d…adad`, 232.0 s | `verified.json` |
| Bookend check | **1 failure, deliberate**: no `ClaudeTitleOutro` beat | `bookend_check.txt` |

The bookend failure is on purpose. The toolkit's `ClaudeTitleOutro` hardcodes "@NikBearBrown",
and the assignment forbids the instructor's credit line, so the film ends on its conclusion
beat instead. It is a house-style check, not a render-integrity check; see FRICTIONAL.md.
Home-directory paths in `verified.json` and `final.log` are shortened to `<INFO7375>/`.

## Folder

| File | What it is |
|---|---|
| `riya-k-ground-truth-sql.mp4` | the rendered film (3:52) |
| `PROJECT-BRIEF.md` | the seven answers, plus "exists today" and "will exist" |
| `beat_sheet.json` | narration and visual plan (copy of `reel/beat_sheet.json`) |
| `BUILD-PROMPT.md` | prompts and commands that rebuild it |
| `SOURCES.md` | what I used, what I made, what Claude contributed, licences |
| `FRICTIONAL.md` | dated log |
| `evidence/` | the runnable slice, its outputs, Chinook + licence |
| `reel/` | film source: `make_sheet.py`, `scenes.py`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` |
| `gate-reports/` | toolkit gate outputs |
