# API Impact — final project pitch film

- **Name:** Chethan Gowda (GitHub: chethangowda-git)
- **Course:** INFO 7375, fall 2026
- **Working title:** API Impact
- **Target role:** AI Software Development Engineer
- **Runtime:** 3:58 (238 s), 3840×2160
- **Film:** `api-impact-pitch.mp4`
- **Status:** a pitch. The tool is not built yet. The film labels everything REAL, CONSTRUCTED or PLANNED.

**One sentence:** Before a backend change merges, API Impact will find the frontend lines it breaks and open a draft fix PR in each frontend repo, linked to the backend PR.

## What's in this folder
| File | What it is |
|---|---|
| `api-impact-pitch.mp4` | the rendered film |
| `PROJECT-BRIEF.md` | the seven answers, plus "exists today" and "will exist" |
| `beat_sheet.json` | narration and visual plan (the build's source of truth) |
| `BUILD-PROMPT.md` | the prompts and commands that rebuild it |
| `SOURCES.md` | what I made, what Claude contributed, third-party material and licences |
| `FRICTIONAL.md` | dated log |
| `_qc/REPORT.md`, `_qc/contact_sheet.png` | Gate V visual-QC report |

## How to rebuild
You need the brutalist.art toolkit cloned next to `fall-2026/`, with its `.venv` and Kokoro model set up (`./setup --install`). Then:

```bash
cd brutalist.art && source .venv/bin/activate
# the film's custom scenes live in the toolkit: runtime/remotion/src/ApiImpactPitch.tsx, registered in Root.tsx
python3 runtime/scripts/generate_audio_kokoro.py ../fall-2026/chethan-t/final-project-film
./art run   ../fall-2026/chethan-t/final-project-film --height 1080
./art final ../fall-2026/chethan-t/final-project-film --out ../fall-2026/chethan-t/final-project-film
```

Full steps are in `BUILD-PROMPT.md`.
