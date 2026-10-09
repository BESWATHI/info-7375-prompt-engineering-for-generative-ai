# BUILD-PROMPT — how to rebuild the film

Fill in the exact commands as they are run on Day 3. Only list commands that actually worked; failures go in FRICTIONAL.md.

## Toolkit
```bash
git clone https://github.com/nikbearbrown/brutalist.art
cd brutalist.art
./setup --install     # deps + Remotion + Kokoro model (~340MB, local)
./art --list          # confirm available skills (look for show-tell)
```
Toolkit commit used: _TBD_

## Free pipeline only
Kokoro narration and local rendering. No Higgsfield login, no API keys, no upload.

## Prompts given to Claude Code
1. _2026-10-09_ — Project selection and drafting of PROJECT-BRIEF.md / beat_sheet.json (see SOURCES.md for what Claude contributed).
2. _TBD_ — Build prompt for the film, e.g. "Using the show-tell skill, build the reel from `beat_sheet.json` …" (paste the exact prompt used).

## Render and gate commands
```bash
# TBD — paste the exact render command(s) used
# TBD — paste the exact gate / render-integrity command(s) used
```
Output: `seeded-faults-pitch.mp4`, gate reports copied to `gate-reports/`.
