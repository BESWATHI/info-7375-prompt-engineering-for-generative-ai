# FRICTIONAL — honest work log

Dated entries, newest at the bottom. What I tried, what broke, what changed.

## 2026-10-08 (written 2026-10-09, from memory)
- Read the assignment brief.
- Watched the course AI-policy video.
- Thought about possible project ideas; did not pick one yet.
- Looked at the Brutalist repository.

## 2026-10-09
- Read the assignment. Chose project idea: **Seeded Faults** — Claude-generated data-quality tests scored against planted faults. Picked it because it fits Data Engineering / BI roles and can be verified by a stranger.
- Used Claude Code (Opus 5.5) to help choose the project from three options and to draft PROJECT-BRIEF.md, beat_sheet.json and the scaffolding files. I need to review and rewrite every line in my own words before submission.
- I wanted the folder under "Projects"; there is no `~/Desktop/Projects`, so the work lives in `~/Projects/INFO7375/fall-2026/atharva-c/final-project-film/`.
- Brutalist: my local checkout (`~/Applications/brutalist.art`, commit 29ba0e8) is behind GitHub (22264a3). The `show-tell` skill is not in my checkout. Next: pull and check whether `show-tell` appears.
- Open item: the alternatives (Great Expectations, dbt-expectations) are named from general knowledge, not yet checked hands-on. I must try them before the film states what they do or don't do.
- Open item: confirm which of my GitHub repos are public before citing them as evidence.
- Set up a practice sandbox (`~/Projects/seeded-faults-sandbox`, not part of this submission). Installed great_expectations 1.24.0, dbt-core 1.12.5, dbt-duckdb 1.11.0, pandas 3.0.6. No install errors.
- Downloaded NYC TLC yellow taxi trips, January 2024 (public; 2,964,624 rows, 19 columns). Kept the first 2,000 rows as `trips_sample.csv`.
- Great Expectations: ran one hand-written check (`passenger_count` not null) on the 2,000-row sample → passed, 0 unexpected. I had to write the rule myself.
- First planted-fault test (script drafted by Claude, run by me): blanked `passenger_count` in 50 random rows. Same check → clean file passed (0 unexpected); faulted file failed with exactly 50 unexpected. This is the project's core idea done once by hand, for one fault type.
- Checked whether GX Core 1.x (free library) suggests expectations automatically:
  - Searching the docs for "profiler" returned only tutorial pages (dbt tutorial, SQL connection, uniqueness use case) — none answered the question.
  - The "Create an Expectation" page (https://docs.greatexpectations.io/docs/core/define_expectations/create_an_expectation/, read 2026-10-09) describes choosing an Expectation from the Gallery and setting its parameters by hand. No automatic-suggestion step.
  - Searched the installed great_expectations 1.24.0 package for "data_assistant", "DataAssistant" and "onboarding": no matches.
  - **Finding:** in GX Core 1.24.0 I wrote each check by hand; I found no automatic suggestion feature in the docs page or the installed library. GX Cloud not checked — the docs site no longer has Cloud pages, so the film will not make any claim about Cloud.
  - This changes the brief: section 2 said GX "can propose expectations from your data". That was from general knowledge (older versions) and is not supported by what I checked. Brief and beat B03 must be corrected.
