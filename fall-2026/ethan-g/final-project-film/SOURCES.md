# SOURCES — DataSentry: A Project Pitch

Ethan Gomes · INFO 7375 · compiled 2026-10-14

## What I used (read, not copied)

| Source | What it supports | Read |
|---|---|---|
| dbt docs, "Add data tests to your DAG" — https://docs.getdbt.com/docs/build/data-tests | dbt's four built-in generic tests (unique, not_null, accepted_values, relationships); a test passes when its query returns zero failing rows. The page does not describe a report of what tests would miss. | 2026-10-14 |
| Great Expectations home page — https://greatexpectations.io/ | GX Core is open source under Apache 2.0. | 2026-10-14 |
| GX blog, "2025 In Review: Building Trust Into Your Data Work" (dated 2026-01-09) — https://greatexpectations.io/blog/2025-in-review-building-trust-into-your-data-work/ | ExpectAI, in GX Cloud, "analyzes real dataset patterns and generates suggested Expectations you can review, refine, and approve." No defect seeding or per-defect catch rate described. | 2026-10-14 |
| GX community forum, "Is there any alternative for GX v1 Data Profiler?" — https://discourse.greatexpectations.io/t/is-there-any-alternative-for-gx-v1-data-profiler/2083 | Background only: GX 1.0 removed the older profilers / Data Assistants. Not stated in the film. | 2026-10-14 |
| NYC TLC Trip Record Data — https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page | Yellow taxi trip records are published monthly as public data (Parquet). | 2026-10-14 |
| NYC TLC yellow trip data dictionary — https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf | Column names named in B02 (pick-up/drop-off time, passengers, distance, fare). | 2026-10-14 |
| pandera — https://github.com/unionai-oss/pandera | Described in B03 as an open-source Python library for testing data frames. | 2026-10-14 |

**Alternatives named in the film.** dbt data tests, and Great Expectations (GX Core, and GX Cloud's ExpectAI feature). Sources are listed above.

No data was downloaded. No TLC sample, no pandera code, and no DataSentry run exists yet.

## What I made

- `PROJECT-BRIEF.md` — the seven answers (my topic choice and my answer to Q7; drafted with Claude, see below).
- `film/make_sheet.py` → `beat_sheet.json` — narration and visual plan, 19 beats.
- `film/scenes_body.py` — the 18 drawn scenes (Manim), including the title card.
- `film/finish_audio.py`, `film/build_scenes.sh` — small build helpers.
- The rendered film, and its subtitles (`.srt` / `.vtt` and the embedded track), timed from my narration.

## What Claude contributed

Claude (Claude Code, model Opus 5.5) worked with me on 2026-10-12 and 2026-10-14. Claude:

- suggested four candidate topics for data roles; **I chose** the data-quality test generator (topic 2);
- researched dbt and Great Expectations on the web and summarised what the pages say (above);
- drafted `PROJECT-BRIEF.md` from my choices and my answer to Q7 (revised 2026-10-14: the project will help me land a Data Engineer or Data Analyst role and highlight skills I am working on);
- wrote the narration, the beat sheet, all scene code, and the build paperwork (`FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`);
- ran the toolkit's audio, render, and quality gates, looked at frames, and fixed what failed;
- built and embedded the subtitles (`film/make_captions.py`).

I reviewed and approved the topic, the scope, and the Q7 answer. I still need to read every narration line and
sign off on FACTCHECK.md before submitting. No Claude response is shown in the film.

## Tools and third-party assets (all free, all local)

| Asset | Use | Licence |
|---|---|---|
| Brutalist toolkit (github.com/nikbearbrown/brutalist.art, commit 519fcbb, 2026-10-12) | pipeline, gates, show-tell drawing kit, the 25 approved original isometric props, the `ClaudeDefinitions` Remotion terms card | No LICENSE file found in the repository at that commit; used as the course directs ("make a short film with Brutalist"). |
| Kokoro-82M via kokoro-onnx, voice `am_michael` | narration (a stock synthetic voice, speaking my script in first person) | Kokoro-82M model: Apache 2.0 (as stated in the toolkit's generate_audio_kokoro.py) |
| faster-whisper (`small.en`, `base.en`) | pronunciation check of each narration clip | MIT |
| Manim Community v0.20.1 | drawn scenes | MIT |
| Remotion | the two bookend cards | Remotion licence (free for individuals) |
| EB Garamond | on-screen type | SIL Open Font License 1.1 (`runtime/fonts/EB_Garamond/OFL.txt`) |
| ffmpeg | audio padding, encode | LGPL/GPL |

No paid generation, API keys, stock media, music, or third-party images were used.
