# SOURCES — BiteCheck pitch film

## What I used
| Item | What it is | Licence / terms | When |
|---|---|---|---|
| [brutalist.art](https://github.com/nikbearbrown/brutalist.art) @ `b21f625` | Film toolkit: show-tell drawing kit (pasted into `scenes.py` minus the portrait helpers), Kokoro audio script, `art run` / `art final`, QC gates | course toolkit (see its repo) | cloned 2026-10-12 |
| Kokoro-82M (`kokoro-onnx`, voice `am_michael`) | Free local text-to-speech for the narration | Apache-2.0 | 2026-10-12 |
| Manim Community v0.18.1 | Renders every drawing | MIT | 2026-10-12 |
| EB Garamond, Menlo | On-screen type | SIL OFL (EB Garamond); Menlo ships with macOS | — |
| ffmpeg | Encoding / frame sampling | LGPL/GPL | — |
| [Schemathesis docs](https://schemathesis.readthedocs.io/en/stable/) | What Schemathesis does (B06) | read only | read 2026-10-12 |
| [StrykerJS docs](https://stryker-mutator.io/docs/) | What Stryker does (B06) | read only | read 2026-10-12 |
| StrykerJS 8.7.1 (`@stryker-mutator/core`) + TypeScript 5.5.4 | **Ran** on a scratch copy of the InstaLoan rules files, 2026-10-13 (`evidence/stryker/`) | Apache-2.0 | 2026-10-13 |
| Whisper-tiny (`mlx-community/whisper-tiny`, via `mlx-whisper` 0.4.2) | Pronunciation check of the narration (`evidence/pronunciation_check.txt`) | MIT | 2026-10-13 |
| [Postman Postbot page](https://getpostman.com/product/postbot/) plus hands-on reviews ([NashTech](https://blog.nashtechglobal.com/postbot-in-postman/), [DEV](https://dev.to/lengochoangminh/simplify-api-testing-with-postbot-postmans-ai-assistant-56b)) | What Postbot does (B06) | read only | read 2026-10-12 |

## What I made
- The project idea (I chose option A from Claude's three suggestions), the target role, and the decision to use my own InstaLoan demo as the system under test.
- The InstaLoan loan-origination demo (`~/Desktop/LOS`, Express + TypeScript + Prisma/SQLite, synthetic data, mock vendors), built earlier with Claude's help. It is not in this folder.
- `evidence/los_smoke_test.txt`: a live run of that demo on 2026-10-12 with a synthetic applicant.

## What Claude contributed (Claude Code, Opus 5.5, desktop app, 2026-10-11 → 2026-10-13)
- Explained the assignment and proposed three project options from my résumé (read privately; not stored here).
- Drafted `PROJECT-BRIEF.md`, the narration and `make_sheet.py` / `beat_sheet.json`, all 14 Manim scenes in `scenes.py`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, this file, `BUILD-PROMPT.md`, `README.md`, and the Claude-marked entries in `FRICTIONAL.md`.
- Ran the LOS smoke test (2026-10-12), read the three tools' docs, ran StrykerJS on a scratch copy of the loan rules (2026-10-13, at my request), ran the Whisper pronunciation check, and ran the toolkit's gates and renders.
- On 2026-10-13, acting as a mock TA, reviewed the pitch against the rubric. I then asked it to close the gaps, which led to the Stryker run, the sharper unique-value line, the public-evidence line and the honesty fixes logged in FRICTIONAL.md.
- **No Claude response is shown in the film.** Nothing on screen is presented as Claude output.

## Third-party assets in the film
None. Every picture is drawn in code (`scenes.py`). No stock images, icons, music or footage. Tool names (Postbot, Schemathesis, Stryker) appear only as text labels.

## Left out on purpose
My résumé, my job tracker, conversation transcripts, the original loan-walkthrough document, and build caches (`mp3/`, `manim/`, `media/`, `clips/`, `_qc/`).
