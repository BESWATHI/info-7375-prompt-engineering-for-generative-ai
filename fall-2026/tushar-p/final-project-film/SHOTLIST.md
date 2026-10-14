# SHOTLIST — agent-proving-ground

Typed work order. Every beat is `shot.type GRAPHIC · source own ·
graphic.engine manim`, rendered by the pipeline from `scenes.py` to
`manim/<BEAT_ID>.mp4`. `run.sh` discovers scenes by the regex
`class ([A-Z][A-Za-z0-9]*_\w+)\(Scene\)` and takes the beat id from the prefix
before the first underscore. Each scene's length is its measured mp3
(`mp3/timings.json`, written back to `actual_duration_s`).

Audio is voiced one sentence at a time by `sentence_audio.py` (in this
folder): 0.35 s of silence between sentences, none added at a beat's start
or end, plus a 1.5 s silent tail on B12. It records each sentence's speech
onset in the sheet (`sentences`), which `scenes.py` uses for cue timing.
Re-voice with `python3 sentence_audio.py [--only B04]`, not
`generate_audio_kokoro.py` (that would drop the pauses and sentence times).

| Beat | Scene class | Owner | Slot | Audio | Mock-up |
|---|---|---|---|---|---|
| B00 | `B00_ClaimVsTests` | pipeline | `manim/B00.mp4` | 10.37s | Constructed |
| B01 | `B01_ThreeBoxes` | pipeline | `manim/B01.mp4` | 12.80s | |
| B02 | `B02_RepoTree` | pipeline | `manim/B02.mp4` | 11.97s | Constructed |
| B03 | `B03_ThreeQuestions` | pipeline | `manim/B03.mp4` | 15.50s | |
| B04 | `B04_TwoPieces` | pipeline | `manim/B04.mp4` | 24.94s | |
| B05 | `B05_SixtySeconds` | pipeline | `manim/B05.mp4` | 15.57s | Constructed |
| B06 | `B06_FourSkills` | pipeline | `manim/B06.mp4` | 16.65s | |
| B07 | `B07_InAndOut` | pipeline | `manim/B07.mp4` | 13.23s | |
| B08 | `B08_FirstRun` | pipeline | `manim/B08.mp4` | 11.36s | Constructed |
| B09 | `B09_DockerFirst` | pipeline | `manim/B09.mp4` | 14.86s | |
| B10 | `B10_HaveAndNew` | pipeline | `manim/B10.mp4` | 21.96s | |
| B11 | `B11_ExistsVsWill` | pipeline | `manim/B11.mp4` | 11.68s | |
| B12 | `B12_ThankYou` | pipeline | `manim/B12.mp4` | 9.76s | |

## Open slots (human)

None. No screenshots, recordings or pantry media are needed — every beat is
drawn. The one human task is verification: FACTCHECK.md C1 and C2 (B04).
