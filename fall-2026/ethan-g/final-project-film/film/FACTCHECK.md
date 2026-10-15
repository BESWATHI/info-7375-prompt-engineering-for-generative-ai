# FACTCHECK — DataSentry: A Project Pitch

Status: 29 claims checked 2026-10-14 by Claude (Opus 5.5) against the sources below and against the honesty rule
(past tense only for things that exist and can be shown; everything else "will"). Reviewed and approved by Ethan
Gomes, 2026-10-14 (watched the final film and read the subtitles).

Verdict key: **PASS** = true as spoken today. **EXEMPT** = a plan in future tense ("will"), not a claim that anything
exists; it is honest as long as it stays future tense. **CORRECTED** = wording changed during the check.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 0 | BIDEA | "This is a Final Project Pitch Film created by Ethan Gomes. The project is called DataSentry." | PASS | Ethan's requested opening line (2026-10-14); DataSentry is the working title (renamed from the earlier working title, 2026-10-14). | — |
| 0a | BIDEA | On screen: "DataSentry" / "Scoring AI-written data checks with planted defects" | EXEMPT | Describes the planned project (PROJECT-BRIEF.md §1); the narration over it says "Nothing is built yet; everything here is a plan." | Replaced the typed question card (Ethan, 2026-10-14). |
| 1 | BIDEA | "Nothing is built yet; everything here is a plan." | PASS | State of work on 2026-10-14: no DataSentry code, data sample, or score exists (see PROJECT-BRIEF.md, "Exists today"). | — |
| 2 | BDEFS | Definitions of data check, planted defect, catch rate | PASS | Definitions used by this project; they describe terms, not results. | — |
| 3 | B00 | DataSentry "will be" a Claude Code workflow that writes checks and scores them with planted defects | EXEMPT | Plan, future tense. PROJECT-BRIEF.md §1. | Name now spoken in BIDEA first (Ethan, 2026-10-14). "Claude" transcribes as the homophone "clawed" in whisper; not a voice error. |
| 4 | B00 | On-screen "DataSentry" | PASS | Working title chosen 2026-10-14. | — |
| 5 | B01 | It "will be" a public GitHub repository with three parts | EXEMPT | Plan. No repository exists yet. | — |
| 6 | B02 | Public data, "for example" one month of NYC yellow taxi trips | PASS | NYC TLC publishes yellow taxi trip records monthly as public data (nyc.gov/site/tlc/about/tlc-trip-record-data.page, read 2026-10-14). Framed as an example dataset. | "for example" added 2026-10-14. |
| 7 | B02 | Sample of "about ten thousand rows"; on-screen "~10,000 rows" | EXEMPT | Planned sample size; not yet drawn. Future tense ("It will start from…"). | — |
| 8 | B02 | Columns: pick-up time, drop-off time, passengers, distance, fare | PASS | Fields in the TLC yellow trip data dictionary (pickup/dropoff datetime, passenger_count, trip_distance, fare_amount). nyc.gov TLC data dictionary PDF. | — |
| 9 | B03 | pandera is "an open-source Python library for testing data frames" | PASS | pandera project (github.com/unionai-oss/pandera): open-source data-frame validation library for Python. | — |
| 10 | B03 | Claude Code "will" see only column names and types; "will never see" the defect list | EXEMPT | Design rule of the plan (PROJECT-BRIEF.md §6, leakage). | — |
| 11 | B04 | A script "will" break the copy five ways (list of five) | EXEMPT | Planned defect types, PROJECT-BRIEF.md §5. On-screen "5" counts the five named. | — |
| 12 | B05 | Every check runs twice; pass on clean, fail on broken; catch rate per defect | EXEMPT | Planned method, present tense describing the design ("Then every check runs twice"). No run has happened. | — |
| 13 | B06 | "I looked at two tools data teams already use." | PASS | The two tools: dbt data tests (docs.getdbt.com/docs/build/data-tests) and Great Expectations / GX Cloud ExpectAI (GX blog, 2026-01-09). Links in SOURCES.md. | — |
| 14 | B06 | dbt's built-in tests: unique, not null, accepted values, relationships; they check what you write | PASS | docs.getdbt.com/docs/build/data-tests (read 2026-10-14): four built-in generic tests; a test passes when its query returns zero failing rows. | — |
| 15 | B07 | GX Cloud is Great Expectations' paid product | PASS | greatexpectations.io: GX Core is open source (Apache 2.0); GX Cloud is the hosted product. | — |
| 16 | B07 | GX Cloud has ExpectAI, which suggests checks for you to review and approve | PASS | GX blog "2025 In Review" (2026-01-09): ExpectAI "analyzes real dataset patterns and generates suggested Expectations you can review, refine, and approve." | — |
| 17 | B07 | "So checks suggested by AI already exist." | CORRECTED | Follows from #16. | Was "So A I written checks already exist"; voiced as "So I've written…" — reworded. |
| 18 | B08 | "What I didn't find, in what I read, was a way to measure how good those checks are." | PASS | Scoped to what was read: the dbt data-tests page and the GX 2025 review post describe no defect seeding or per-defect catch-rate report (checked 2026-10-14). Not a claim that no tool anywhere does this. | Kept the qualifier "in what I read" on purpose. |
| 18a | B08 | "Data Sentry will tell a data engineer which bad rows their checks would let through." | EXEMPT | The benefit, stated as a plan in future tense (PROJECT-BRIEF.md §2). | Added 2026-10-14 so Q2 states the user benefit outright. |
| 19 | B09 | A hiring manager "will" run one command and see a short table | EXEMPT | Planned first-minute experience. The terminal drawing is labelled **constructed** on screen; its rows carry empty status rings, not results. | — |
| 20 | B10 | Four skills from this class: prompt contract, agent loop, verification, evaluation | EXEMPT | Plan: skills the project is designed to show (PROJECT-BRIEF.md §4). | Evidence sentence moved to B10A. |
| 20a | B10A | "Once it's built, a reviewer could fairly conclude that I test an AI's output instead of trusting it." | EXEMPT | Conditional on the build ("Once it's built"); matches PROJECT-BRIEF.md §4. Not a claim about today. | Added 2026-10-14 so Q4 says what a reviewer could conclude. |
| 20b | B10A | "The evidence will be in the repo: the scorecard, the log of every round, and the prompts behind each check." | EXEMPT | Future tense; none of it exists yet (B14). On screen: "planned evidence". | — |
| 21 | B11 | In / out of scope / first run | EXEMPT | Plan, PROJECT-BRIEF.md §5. | — |
| 22 | B12 | Risk: loose checks; both copies required every time | EXEMPT | Plan, PROJECT-BRIEF.md §6. | — |
| 23 | B13 | "It will help me land a data job, like a Data Engineer or Data Analyst role. It will highlight the skills I'm working on: Python, pandas, pandera, and Claude Code in a loop that fixes its own checks." | EXEMPT | Stated as a goal and skills in progress; no claim of finished skill, so no evidence is claimed (Ethan, 2026-10-14). PROJECT-BRIEF.md §7. | Replaced "Mostly, to show off… work I already know" (2026-10-14), which needed evidence. |
| 24 | B14 | Date; exists = this pitch, a written brief, notes on the two tools; not yet = code, planter, any score | PASS | True on 2026-10-14: PROJECT-BRIEF.md, this film, SOURCES.md exist; nothing else does. | Earlier "notes on D B T and Great Expectations" reworded (Kokoro voiced "grade expectations"). |
