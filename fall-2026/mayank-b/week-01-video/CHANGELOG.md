# CHANGELOG — Temperature Is Not a Fact Checker.

Every change to the video since generation started, newest last. Times are local
(from file timestamps where noted). FRICTIONAL.md records *what went wrong*; this
file records *what changed*.

## 2026-09-23 — v1: first build

- **~18:39 — Evidence.** Copied the chapter's `probabilities()` and `sample()` verbatim into
  `code/main.py`; wrote `code/run_temperature.py`. Output `code/temperature_results.json`
  matches the chapter's tables exactly (Python 3.11.16).
- **~18:40 — Beat sheet v1.** `code/author_sheet.py` → `beat_sheet.json`: 12 beats
  (B00 cold open, B01 hesitant-writer summary, B02–B08 body, BVDT recap, BHTF your turn,
  BOUT outro), 480 words, Kokoro `am_onyx`, title "Temperature Is Not a Fact Checker."
- **18:43 — Audio.** Kokoro narration generated for all 12 beats (158.5 s total).
- **~18:44 — B01 lead silence.** Prepended 0.8 s of silence to `mp3/beat-B01.mp3`
  (10.58 s → 11.38 s). Total 159.3 s.
- **18:45 — Word clock.** `align.py` → `mp3/words.json` (12/12 beats aligned).
- **~18:46 — Props.** `code/build_props.py`: animation cues from word timings, typeset math
  SVGs (softmax, ratio, gap, three ratio rows), real seed-7 draw sequences.
- **~18:47 — New scenes.** Added `TemperatureConcentration.tsx` (7 components: TcScoresToOdds,
  TcTemperatureDial, TcRatio, TcCode, TcSampleCounts, TcWrongAnswer, TcBoundary) and registered
  them in the toolkit's `Root.tsx`. Copied the NBB logo into `public/temperature-concentration/`.
- **18:50 — Layout fixes from test stills (before the full render):**
  - B04: max ratio-bar length 760 → 520 px (the "54.60×" label was clipped).
  - B06: dot cell 19 → 20 px; count legend redesigned as label-over-number columns (the legends collided);
    added the "outcome 2 share vs assigned p" line.
  - B07: honesty stamp forced onto one line; footer caption shortened.
  - B08: bigger claim cards (font 44 → 54, card height 130 → 180, row spacing 170 → 215).
- **18:51–19:05 — Render.** All 12 beats rendered with Remotion at 4K.
- **~19:06 — Review cut v1** compiled (159.5 s).

## 2026-09-23 — v2: fixes from visual QC

- **B01 (hesitant writer):** the correction never appeared on screen in v1.
  - Trigger `how creative the model is` → `creative`; replacement → `concentrated`.
  - Text line 1 changed to "Temperature sets how creative the choices are." (after the fix it reads
    "…how concentrated the choices are.").
  - Typing sped up and made more even: `charMs` 50 → 32, `mistakeRate` 10 → 3,
    `hesitateWithin` 3 → 1, `hesitateBetween` 20 → 8.
- **B00, BHTF (composer bookends):** `largeText: true` (text was undersized).
- **19:10** Re-rendered B00, B01, BHTF. **19:13** Review cut v2 compiled
  → `temperature-concentration-slate.mp4` (159.5 s).
- Narration and audio are unchanged from v1.

## 2026-09-25 — v3: clean master + submission files

- **Clean master:** `compile.py --height 1080` (no review overlays) → `temperature-concentration.mp4`
  (159.5 s, 9.4 MB). The first attempt was refused by Gate V: B01 "underfill" (text covers 7–23% of
  the safe area mid-typing). Added the toolkit's `qc.sparse_by_design` declaration with a written
  reason to B01 only (it waives the fill checks; edge, empty-frame and contrast checks still run).
  Gate V then passed: 0 BLOCKER, 0 MAJOR.
- Added `README.md`, `SOURCES.md`, `.gitignore`, `_qc/MANUAL-QC.md` (my hand QC table; Gate V
  overwrites `_qc/REPORT.md` on every compile, its first failing run is kept in
  `_qc/GATE-V-REPORT-first-run.md`).
- No change to narration, audio, or any visual. **← current version**
- Pushed to `nikbearbrown/info-7375-prompt-engineering-for-generative-ai`,
  `fall-2026/mayank-b/week-01-video/`.
