# Readback — Final Project Pitch Film

**Aravind Ravi** · INFO 7375 · Fall 2026
**Working title:** Readback. *Hear how AI reads your instructions before it acts on them.*
**Target role:** AI Product Manager
**Runtime:** 3:02 (182.46 s) · 1920×1080, 24 fps · `aravind-r-readback-pitch.mp4`
**Master SHA-256:** `18f0d50c8eac125f1c44ad71c72b0c0f2d3951a82d590f60075e254d581c131c`

The film pitches Readback: a tool that will show a product manager which clause of their eval rubric an AI judge reads differently than they meant. It answers the assignment's seven questions; the same answers are written out in [`PROJECT-BRIEF.md`](PROJECT-BRIEF.md). It is a pitch, not a build. What exists today and what will exist are listed at the end of the brief and in the film's last beat.

**Narration** is synthesized locally from my own approved script, using the free Kokoro voice `am_onyx`, and the film says so in its first line. No paid generation, API key, media account or public upload was used.

## What's in this folder

| Path | What it is |
|---|---|
| `aravind-r-readback-pitch.mp4` | The film |
| `PROJECT-BRIEF.md` | The seven answers, with **Exists today** and **Will exist** lists |
| `beat_sheet.json` | Narration and visual plan, in show-tell format. Each beat carries `question_ids`, `claim_status`, `evidence` and `on_screen_label` |
| `make_sheet.py`, `scenes.py`, `add_holds.py` | The beat-sheet generator, the Manim scenes for B01–B08, and the per-beat hold padding |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` | The toolkit's required paperwork: claims, work order, prompts |
| `gates/` | Toolkit gate reports (A, W, B, V, T, bookend, factcheck, render logs), my own `honesty-audit.md`, and one frame per beat |
| `case-study/` | Real data and runs: 10 AMI meetings (CC BY 4.0), the constructed recap PRD, system prompt and rubric (labelled CONSTRUCTED), and 10 real recap outputs from Claude Opus 5.5 (14 Oct 2026) |
| `toolkit-patches/` | My patch to the toolkit's outro: my own handle, and no mascot |
| `FRICTIONAL.md`, `SOURCES.md`, `BUILD-PROMPT.md` | Dated log, sources and credits, and the prompts and commands that rebuild the film |

## Rebuild the film

**Toolkit:** [brutalist.art](https://github.com/nikbearbrown/brutalist.art), pinned at commit **`cd4bf20904be4e7d63babd9622b17963c2361b27`**. Don't use current upstream: it pins Manim 0.20, and this film was rendered with Manim 0.18.1.

**Machine setup** (my Week 1 install; see `FRICTIONAL.md` there):
- Python 3.12 venv with the toolkit's `requirements.txt` (manim 0.18.1).
- Homebrew `ffmpeg`, `cairo`, `pango` and `espeak-ng`.
- Node ≥ 20.
- The toolkit's `youtube/` folder moved out of the checkout, so `./setup` passes its ElevenLabs guard.
- `A01/brutalist-env.sh`, which activates the venv and sets `PHONEMIZER_ESPEAK_LIBRARY=/opt/homebrew/lib/libespeak-ng.1.dylib`.

From this folder (`REEL` = its absolute path; `ART` = the toolkit checkout):

```bash
git -C "$ART" checkout cd4bf20 && git -C "$ART" apply "$REEL/toolkit-patches/ClaudeTitleOutro-handle-hideMascot.patch"
source "$ART/../brutalist-env.sh"
python3 make_sheet.py                                          # beat_sheet.json (narration + plan)
(cd "$ART" && python3 runtime/scripts/generate_audio_kokoro.py "$REEL")   # Kokoro am_onyx → mp3/, the clock
python3 add_holds.py                                           # hold after each beat → actual_duration_s
(cd "$ART" && python3 runtime/scripts/align.py "$REEL")       # word timings → mp3/words.json
(cd "$ART" && ./art run "$REEL" --height 1080)                 # Gates F, L, A, W, B, V + review cut
(cd "$ART" && ./art final "$REEL" --height 1080 --out "$REEL/exports/landscape")   # Gate T + master
cp exports/landscape/aravind-r-readback-pitch.mp4 .
(cd "$ART" && python3 runtime/scripts/bookend_check.py "$REEL" && python3 runtime/qc/factcheck_check.py "$REEL")
```

These steps only rebuild the film from the committed case-study files. The data and the feature run have their own steps; see `case-study/data/sample/README.md` and `BUILD-PROMPT.md`. Re-running `case-study/run_feature.py` asks Claude again, so the recaps it writes will differ. The committed outputs dated 14 Oct 2026 are the record the film quotes.
