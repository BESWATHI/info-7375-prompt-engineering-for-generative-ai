# DayThread — Final Project Pitch Film

**Aditya Raj** · INFO 7375 Prompt Engineering and Agentic AI · Fall 2026
**Project:** DayThread, a *proposed* AI check-in assistant that connects details across daily
conversations and brings concerning changes to a home care coordinator for review.
**Target role:** AI Engineer
**Status:** proposal. No DayThread prototype or evaluation results exist yet. This folder holds the
pitch film's documents, build source and evidence.

> **Where the film is.** The finished film is **not in this GitHub folder**, because the course repo's
> `.gitignore` excludes `*.mp4` and `*.mp3`. It is in the Canvas ZIP
> **`Raj_Aditya_INFO7375_FinalProjectFilm.zip`**, at
> `final-project-film/Raj_Aditya_INFO7375_FinalProjectFilm.mp4`, with
> **SHA-256 `be9d096cca7525d938707551a6652d9434a7a1d13de467c81a89e4cd57a5e8eb`**. See *GitHub folder vs
> Canvas ZIP* below for the full list of media files that exist only in the ZIP.

## The film

| | |
|---|---|
| File | `Raj_Aditya_INFO7375_FinalProjectFilm.mp4` (in the Canvas ZIP only) |
| Measured runtime | **3:18.7 (198.71 s)** (ffprobe) |
| Format | 3840×2160, 24 fps, H.264 + AAC 48 kHz stereo |
| Size | 22.1 MB (22,087,344 bytes) |
| SHA-256 | `be9d096cca7525d938707551a6652d9434a7a1d13de467c81a89e4cd57a5e8eb` |
| Voice | synthesized (Kokoro `am_onyx`, local) reading Aditya's script, disclosed on screen and aloud |

The seven pitch questions are answered in the film (map in `gate-reports/questions-coverage.md`) and
on one page in `PROJECT-BRIEF.md`.

## Contents

| Path | What it is |
|---|---|
| `Raj_Aditya_INFO7375_FinalProjectFilm.mp4` | the final film (4K master from `art final`); **Canvas ZIP only** |
| `PROJECT-BRIEF.md` | one-page answers to the seven questions; ends with *exists today* and *will exist* |
| `SCRIPT.md` | narration source (v3) and the template exceptions table |
| `beat_sheet.json` | the toolkit beat sheet with measured audio durations and build stamps |
| `BUILD-PROMPT.md` | Aditya's actual prompts, the commands run, and the toolkit revision |
| `SOURCES.md` | sources (read by Aditya 2026-10-14), licenses, who contributed what |
| `FRICTIONAL.md` | dated log of decisions, attempts, fixes, checks and unresolved items |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` | the toolkit's paperwork set (claims, shots, no generation prompts) |
| `TOOLKIT-CHANGES.md` | toolkit state and changes (none to source files for this film) |
| `gate-reports/` | final-render gate reports (GATE T, Gate V, run/final logs, verification JSON), plus the checks run on the master (probe, transcripts, frame sheets, question coverage) |
| `source/` | everything needed to rebuild: `make_sheet.py`, `audio_post.py`, `assemble_scenes.py`, `scenes_body.py`, the assembled `scenes.py`, the narration audio `mp3/` (**Canvas ZIP only**), `mp3/timings.json`, pre-audit reports, script drafts |
| `preview/` | the 15-second preview Aditya approved before the full film (`daythread-preview.mp4`, **Canvas ZIP only**), with its checks and source |

## Toolchain (as used, macOS arm64)

- **Toolkit:** brutalist.art at `main` `519fcbb96e9e1898d374c8794117cab494ffc5cb`, skill `show-tell`.
  This film needed no change to toolkit source files (see `TOOLKIT-CHANGES.md`).
- **Python:** conda env `brutalist-daythread`, Python 3.12.14.
- **Packages:** Manim 0.20.1, manimpango 0.6.1, kokoro-onnx 0.6.1 with Kokoro v1.0 model files,
  faster-whisper 1.2.1 (checks only), numpy 2.5.3, Pillow 12.3.0, scipy 1.18.1.
- **Other:** FFmpeg 9.0.2 (Homebrew); MacTeX via `path_helper`; EB Garamond Regular and Italic
  installed in `~/Library/Fonts`.
- **Cost:** $0.00. No API keys, no paid services, no network calls while rendering.

## Rebuild (exact)

Put this folder's `source/` contents into a reel folder outside the toolkit, e.g.
`~/Desktop/Brutalist/my-videos/youtube/daythread/film/`. Keep `SCRIPT.md` one level above it, because
`make_sheet.py` reads `../SCRIPT.md`. Then:

```bash
eval "$(/usr/libexec/path_helper)" && export PATH="/opt/anaconda3/envs/brutalist-daythread/bin:/opt/homebrew/bin:$PATH"
cd ~/Desktop/Brutalist/brutalist.art && git checkout 519fcbb && ./setup        # expect all features ready
REEL=~/Desktop/Brutalist/my-videos/youtube/daythread/film
cd $REEL
python make_sheet.py              # beat_sheet.json from ../SCRIPT.md (keeps measured audio if unchanged)
# The narration audio is in the Canvas ZIP (source/mp3). From the GitHub folder alone, regenerate it:
#   python ~/Desktop/Brutalist/brutalist.art/runtime/scripts/generate_audio_kokoro.py . && rm -rf mp3/raw && python audio_post.py
python assemble_scenes.py         # scenes.py = toolkit iso_kit.py + 11 props (verbatim) + scenes_body.py
cd ~/Desktop/Brutalist
./brutalist.art/art run   "$REEL" --height 2160                    # Gates F, L, A, W, B, V + review cut
./brutalist.art/art final "$REEL" --height 2160 --out "$REEL/exports"   # GATE T + verified 4K master
```
`art run` renders only scenes whose `manim/<BID>.mp4` is missing. To re-render, move `manim/` and
`media/` aside first. The master comes out at `exports/daythread-pitch-film.mp4`, and this folder's
MP4 is a renamed copy of it.

## GitHub folder vs Canvas ZIP

Both come from the same package build (`package.py`), and every shared file is byte-identical
(checked by sha256). The **only** difference is media that the course repo's `.gitignore` keeps out
of Git (`*.[mM][pP]3`, `*.[mM][pP]4`). These 38 files are in the ZIP only:

- `Raj_Aditya_INFO7375_FinalProjectFilm.mp4`: the film (sha256 above)
- `preview/daythread-preview.mp4`: the approved 15-second preview
  (sha256 `37f9d008407f48c2c537a63aada4cd342dec376200989d1034fe90659db2c1fc`)
- `source/mp3/beat-*.mp3` (18 files): the narration as compiled, with BOUT padded by 1.0 s
- `source/mp3/raw/beat-*.mp3` (18 files): Kokoro's raw output before `audio_post.py`

The ZIP's own checksum cannot be written inside the ZIP, because this README is part of it. It is given
in the Canvas submission text instead.

## Honesty notes

- Every drawn workflow beat is captioned **"Constructed — proposed workflow"**. Nothing shows an
  observed result.
- Lifeline and DailyCall are described only from their own documentation, which Aditya read on
  2026-10-14. Neither product was tested, and the film does not claim they lack anything.
- **What Aditya contributed and what Claude contributed:** see `SOURCES.md`.

## Credits

Built with the brutalist.art toolkit (show-tell skill, iso kit and props), Manim Community, and Kokoro
TTS. Licenses are in `SOURCES.md`.
