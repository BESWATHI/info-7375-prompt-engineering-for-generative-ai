# The Reallocation Engine — Final Project Pitch Film

**Course:** INFO7375 Prompt Engineering & Agentic AI  
**Author:** Isaac Tai  
**Project:** The Reallocation Engine CLI (`tisaac-swe-stem-opt`)  
**Duration:** 111.2 seconds (1m 51s, 4K UHD 3840×2160 @ 24fps)  
**Deliverable File:** `Tai_Isaac_INFO7375_FinalProjectFilm.zip`  

---

## Executive Summary
This submission presents the final project pitch film for **The Reallocation Engine CLI**, an evidence-first, automated job-application filtering tool engineered for F-1 STEM OPT international students.

The film was authored using **Brutalist** (`brutalist.art`), rendered via Remotion, narrated by an on-device Kokoro TTS neural voice (`am_puck`), and verified through an automated quality gate harness.

### Key Highlights
1. **The 7 Pitch Questions**: Fully answered in [PROJECT-BRIEF.md](PROJECT-BRIEF.md) and demonstrated across the 9 beats.
2. **The Honesty Rule**: Strictly observed. Past tense is used exclusively for verified, working prototypes (`tisaac-swe-stem-opt` in *The Reallocation Engine*); future tense ("will") is reserved for planned CLI extensions.
3. **Zero Fabricated Metrics**: No inflated numbers or phantom users. Deduplication shows 3 realistic duplicate postings with SHA-256 hash proofs.
4. **All Verification Gates Passed**:
   - **Gate L (Beat Lint)**: Clean beat-mix structure.
   - **Gate T (Typography & OCR)**: All 9 beats pass WCAG 4.5:1 contrast, text-floor sizing, and bounding-box overlap checks ([TYPECHECK.md](TYPECHECK.md)).
   - **Gate V (Visual QC)**: 18-frame inspection reports 0 Blockers, 0 Majors (`_qc/REPORT.md`).

---

## Submission Package Contents
The submission archive `Tai_Isaac_INFO7375_FinalProjectFilm.zip` contains:
- `README.md`: This project overview and execution summary.
- `final-project-pitch.mp4`: Verified 4K master pitch film (111.2s).
- `PROJECT-BRIEF.md`: Complete answers to the 7 mandatory pitch questions.
- `beat_sheet.json`: Machine-readable beat sheet with audio timings and shot definitions.
- `BUILD-PROMPT.md`: Exact prompt logs and CLI reproduction commands.
- `SOURCES.md`: Full provenance of local engines, models, and public datasets.
- `FRICTIONAL.md`: Complete development friction log documenting architectural choices.
- `TYPECHECK.md` & `_qc/`: Automated quality gate validation reports.

---

## Reproduction Quick Start
To reproduce the film from source:
```bash
# In brutalist.art directory:
python3 runtime/scripts/generate_audio_kokoro.py ../film/youtube/final-project-pitch-film
./art final ../film/youtube/final-project-pitch-film --height 2160 --out ../film/youtube/final-project-pitch-film/exports/landscape
```
