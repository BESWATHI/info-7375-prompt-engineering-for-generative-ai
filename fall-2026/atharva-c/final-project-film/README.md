# Final Project Pitch Film — Seeded Faults

- **Name:** Atharva C
- **Course:** INFO 7375, Fall 2026
- **Working title:** Seeded Faults — data-quality tests, tested
- **Target role:** Data Engineer / BI Engineer
- **Runtime:** _TBD after render (target 2:30–3:20)_
- **Film:** `seeded-faults-pitch.mp4` _(not rendered yet)_

## What's in this folder
| File | What it is |
|---|---|
| `PROJECT-BRIEF.md` | The seven answers, plus *exists today* / *will exist* |
| `beat_sheet.json` | Narration and visual plan, one idea per beat |
| `BUILD-PROMPT.md` | Prompts and commands that rebuild the film |
| `SOURCES.md` | What I used, what I made, what Claude contributed, licences |
| `FRICTIONAL.md` | Dated work log |
| `evidence/` | Scripts and logs behind every past-tense claim in the film |
| `gate-reports/` | Brutalist quality-gate reports _(after render)_ |

## How to rebuild the film
See `BUILD-PROMPT.md`. In short: install the Brutalist toolkit (free local pipeline, Kokoro narration), point it at `beat_sheet.json`, render, then run the toolkit's gates and copy their reports into `gate-reports/`.
