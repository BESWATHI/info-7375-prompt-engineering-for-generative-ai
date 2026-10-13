# JobPost Contracts — Final Project Pitch Film

**Name:** Anisha Gaikar
**Course:** INFO7375
**Working title:** JobPost Contracts
**Target role:** Junior AI / prompt engineer
**Runtime:** 3:33

## What this is
A pitch film for my final project: a Python library of prompt contracts that turns job postings into structured summaries, with a test set that catches Claude inventing details. **Nothing in the project is built yet;** this folder only contains the pitch.

Format: show-tell style (as in the Brutalist toolkit's show-tell skill): a typing intro, a "Terms In This Film" card, then one animated isometric drawing per beat with short labels, a numbered title for each of the seven questions, and the narration written on screen as subtitles. Own colour palette (teal, coral, mustard, sky blue). Every drawing is labelled "CONSTRUCTED · not built yet".

## Files
| File | What it is |
|---|---|
| `Gaikar_pitch.mp4` | The film |
| `PROJECT-BRIEF.md` | The seven questions answered in text |
| `beat_sheet.json` | Narration and visual plan, one beat per idea |
| `RECORDING-SCRIPT.txt` | The narration, one block per beat |
| `clips/` | The ten animated scenes (silent), B00–B09 |
| `audio/` | Narration audio, one file per beat |
| `make_film.sh` | Makes the narration and joins it with the scenes (ffmpeg) |
| `tools/render.py`, `tools/fonts/` | The script that draws and animates the scenes, and its fonts (SIL OFL) |
| `BUILD-PROMPT.md` | Prompts and commands that rebuild the film |
| `SOURCES.md` | What I used, what I made, what Claude contributed |
| `FRICTIONAL.md` | Dated log of what happened while making it |

## How to rebuild the film
```bash
# 1. (optional) redraw the scenes - needs Python 3 + Pillow + ffmpeg
python3 tools/render.py beat_sheet.json tools/fonts clips
# 2. narration (macOS voice) + join scenes into the film
bash make_film.sh Gaikar
```
