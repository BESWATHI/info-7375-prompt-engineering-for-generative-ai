# BUILD-PROMPT

How this film and its evidence were built on 2026-10-09, in the order it happened. Every
command below was actually run on macOS 14 (Darwin 23.6.0, Apple Silicon).

## Environment

| Component | Version | Note |
|---|---|---|
| Python (toolkit venv) | 3.11.14 (Homebrew) | Manim 0.18 requires `<3.13` |
| Python (evidence) | system `python3`, standard library only | `run_slice.py` needs no packages |
| Manim Community | 0.18.1 | no LaTeX needed |
| Kokoro TTS | voice `af_bella` | local, free |
| brutalist.art | `22264a332f6bf8825cdd639bcd33864563801f55` | show-tell skill |
| Font | EB Garamond (OFL), from `brutalist.art/runtime/fonts/EB_Garamond/static/` | had to be copied to `~/Library/Fonts`, see FRICTIONAL.md |

## Stage 1: evidence before script

```bash
cd evidence
mkdir -p data && cd data
curl -fsSL -o Chinook_Sqlite.sqlite https://github.com/lerocha/chinook-database/releases/download/v1.4.5/Chinook_Sqlite.sqlite
curl -fsSL -o CHINOOK-LICENSE.md https://raw.githubusercontent.com/lerocha/chinook-database/master/LICENSE.md
shasum -a 256 Chinook_Sqlite.sqlite   # bdf635be69850bd3be09c9a2dbeef7ddfb80036bd3ef3381383cd03b61e4a61a
cd ..
python3 -I run_slice.py | tee run_slice_output.txt     # prints 9/9, exits 0
```

`run_slice_output_v0_first_run.txt` is the first run (8/9), before the Q08 gold fix. It is
kept on purpose. It cannot be regenerated from the current `gold_set.json`. The v0 Q08 used
`'2023'` in both queries, and the `note` field in `gold_set.json` records what changed.

**Prompt used (to Claude Code):**
> Build the first runnable slice of a text-to-SQL evaluation harness over the public Chinook
> SQLite database: about 8 questions with gold SQL, plus hand-written variants, some
> equivalent (different SQL, same answer) and some plausible wrong queries, each labelled with
> its mistake. Write a stdlib-only runner that executes everything read-only, judges each
> variant by comparing result rows (not SQL text), and also reports what exact-string
> matching would have said. Do not call any model. Nothing here may be presented as model output.

## Stage 2: brief and beat sheet

**Prompt used:**
> Write PROJECT-BRIEF.md answering the assignment's seven questions for this project, framed for
> AI Engineer roles. Past tense only for what exists in evidence/; everything else "will".
> Name BIRD and Vanna as alternatives, using only what their own pages say. End with
> "Exists today" and "Will exist" lists. Then turn it into a show-tell beat sheet: one drawn
> picture per beat, narrated in the first person as me with Kokoro af_bella, no instructor
> name/persona/credit line, a conclusion beat before the outro, 2–4 minutes.

```bash
# in the reel folder (built outside the toolkit, as its CLAUDE.md requires)
python3 make_sheet.py                                            # -> beat_sheet.json
~/Documents/INFO7375/brutalist.art/.venv/bin/python \
  ~/Documents/INFO7375/brutalist.art/runtime/scripts/generate_audio_kokoro.py .   # audio = the clock
```

First pass measured 257.8 s, over the limit. The narration was cut and re-voiced to 233.1 s.

## Stage 3: drawings and render

`scenes.py` = `iso_kit.py` + `iso_originals_25.py` pasted at the top (Gate A copies only
`scenes.py`), then one `class BNN_Name(Scene)` per body beat. Every scene lands its labels
by 40% of the beat and holds still until 58%, so nothing is mid-motion at the 50% frame that
GATE T and Gate V sample.

```bash
cd ~/Documents/INFO7375/brutalist.art
export PATH="$PWD/.venv/bin:$PATH"
./art run   <reel>      # Gates F, L, A, W, then render + compile the review cut
./art final <reel>      # GATE T type check, then the clean master
```

## Stage 4: checks

- Whisper transcript of the key beats (`faster_whisper`, `base.en`) to catch mispronunciations.
- The toolkit's gate reports, copied into `gate-reports/`.
- Watching the cut end to end. See FRICTIONAL.md for what that found.
