# SOURCES

## What I used
- **Brutalist toolkit**: https://github.com/nikbearbrown/brutalist.art, commit `b21f625`. Used as the course instructs; no LICENSE file in the repo at that commit. The film's scenes paste the show-tell drawing kit (`skills/make/show-tell/templates/iso_kit.py`) into `film-source/scenes.py`.
- **Kokoro-82M TTS** via kokoro-onnx, voice `am_michael`, run locally (Apache-2.0, per the toolkit's `generate_audio_kokoro.py`).
- **Manim Community 0.18.1** (MIT) and **ffmpeg** for rendering; **EB Garamond** font (SIL OFL), installed by the toolkit's setup.
- **faster-whisper** (base.en) for the pronunciation check only. Nothing it produced is in the film.
- **NYC TLC Trip Record Data**: yellow taxi trips, January 2024, public download. Used in `evidence/` (not shown in the film). Terms: NYC TLC / NYC Open Data terms of use. _Confirm wording before submission._

## What I made
- PROJECT-BRIEF.md, beat_sheet.json, FRICTIONAL.md, README.md (reviewed and rewritten by me — _update when done_).
- The film's visual plan (the beat sheet's picture descriptions) came from the beat sheet I approved. The drawings themselves were coded by Claude (see below).

## What Claude contributed
- **2026-10-09, Claude Code (Opus 5.5):** suggested three project options from my stated target roles; I chose "Seeded Faults". Drafted PROJECT-BRIEF.md, beat_sheet.json and the scaffolding for README, BUILD-PROMPT, SOURCES and FRICTIONAL. I am responsible for checking and rewriting all of it.
- **2026-10-09–10, Claude Code:** wrote the sandbox scripts (`ge_try.py`, `ge_fault.py`, the `dbt_try` project) that I ran; read and summarised the dbt-expectations README, which I checked against the page; made the honesty fixes to B01, B02, B06 and B09.
- **2026-10-10, Claude Code:** at my request, rewrote all ten narration beats so they flow from one to the next and sound conversational. Facts and tense were kept the same. Lines I changed afterwards in my own words: _list them here_.
- **2026-10-10, Claude Code:** built the film. Wrote `film-source/scenes.py` (10 drawn Manim scenes plus the title outro), `make_sheet.py`, FACTCHECK.md, SHOTLIST.md and PROMPTS.md; generated the audio; ran the Whisper pronunciation check and reworded B01/B06; fixed gate failures; rendered the 4K master; copied the gate reports. I chose the voice, the project, the bookend approach, and locked the narration.
- _Add any later contributions with dates._

## Third-party assets
No third-party images, video, music or stock footage. Every visual is drawn in code; the only audio is Kokoro narration.

## Not included
No real résumé, contacts, application data or conversation transcripts are in this folder or the film.
