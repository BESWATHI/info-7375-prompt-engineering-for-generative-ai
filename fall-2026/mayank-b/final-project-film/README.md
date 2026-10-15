# Final Project Pitch Film — Source Check for Support AI

**Author:** Mayank B. · INFO 7375, Fall 2026
**Working title:** Source Check for Support AI
**Target role:** AI automation engineer
**Runtime:** 3 min 1 s (181.3 s) · 17 beats · 1920×1080
**Stack (planned):** n8n · Python · Claude

> **This is a pitch, not a build.** Nothing in the project exists yet except this brief, its research
> and this film. Every drawn beat about the planned tool carries an on-screen "proposed design" tag; beats showing real things (the Air Canada case, the alternatives, my skills, what exists today) do not. The seven answers are in
> [PROJECT-BRIEF.md](PROJECT-BRIEF.md).

## What the film says
| Beat | Idea |
|---|---|
| BIDEA, BDEFS | The question, and three terms (policy answer, source, hold) |
| B00 | The real case: *Moffatt v. Air Canada* (2024) |
| B01–B06 | What Source Check will do: break the answer into claims, compare them with the current policy version, then pass (and log) or hold for a person, run by an n8n workflow |
| B07 | Alternatives I looked at: Intercom Fin, Zendesk AI agents, manual review |
| B08–B11 | The reader and the first minute, what it will prove, the scope and first test, the main risk |
| B12–B13 | Why this project; what exists today vs what will exist |
| BOUT | Title outro |

## Rebuild the film
Free and local (Kokoro narration, Manim drawings, Remotion bookends). Full steps: [BUILD-PROMPT.md](BUILD-PROMPT.md).

```bash
source ../../brutalist.art/.venv/bin/activate
python3 code/make_sheet.py && python3 code/build_scenes.py
../../brutalist.art/art run . --height 1080
```

## Files
- `source-check-pitch.mp4` (the film, clean master): Canvas only, not on GitHub (see note below)
- `PROJECT-BRIEF.md` · `beat_sheet.json` · `BUILD-PROMPT.md` · `SOURCES.md` · `FRICTIONAL.md` · `CHANGELOG.md`
- `FACTCHECK.md` · `SHOTLIST.md` · `PROMPTS.md`: the toolkit's required paperwork
- `_qc/`: the toolkit's gate reports, plus my own frame checks
- `scenes.py` (assembled by `code/build_scenes.py`) · `code/`: the sheet and scene sources

Note: the instructor asked us not to publish videos on GitHub, so the mp4 is submitted on Canvas only.
