# PROJECT-BRIEF — DataSentry (working title)

**Ethan Gomes · INFO 7375 · Final Project Pitch · written 2026-10-14**
**Target role:** Data Engineer (also relevant to Data Analyst and BI roles)
**Stack (planned):** Python, pandas, pandera, Claude Code. Public data, for example NYC TLC yellow taxi trip records.

Nothing in DataSentry is built yet. Everything about the tool below is written as "will."

---

## 1. What is it?

DataSentry will be a Claude Code workflow that writes data-quality checks for a table, then scores those checks by planting known defects and counting how many the checks catch.

When it is done it will be a public GitHub repository with three parts: a check writer (Claude Code, writing pandera checks from the table's column names and types), a defect planter (a plain Python script that copies a clean sample and breaks it on purpose), and a scorecard (a report of caught and missed defects for each defect type, plus a log of every round).

## 2. Why would anyone care?

It answers the question a data engineer actually has about a test suite: which bad rows will these checks let through?

I looked at two tools data teams already use (notes dated 2026-10-14 in SOURCES.md):

- **dbt data tests.** dbt ships four built-in generic tests (unique, not_null, accepted_values, relationships). A test passes when its query returns zero failing rows. It checks only what you wrote, and the docs page I read does not report what your tests would miss.
- **Great Expectations.** GX Core is open source (Apache 2.0). Its paid GX Cloud has a feature called ExpectAI that, in GX's words, "analyzes real dataset patterns and generates suggested Expectations you can review, refine, and approve" (GX blog, 2026-01-09). So AI-written checks already exist. In what I read, I did not find a measured report of which defect types those suggested checks catch or miss.

What DataSentry will do that they do not: plant known defects, run the checks against both a clean copy and a broken copy, and publish a catch rate per defect type, with the misses written down. It is not a replacement for either tool. It is a way to grade a set of checks, including AI-written ones.

## 3. Who opens it, and what do they do with it?

The reader is a hiring manager or senior engineer for a data engineering role. In the first sixty seconds they will read the README, run one command on a broken sample file, and see a table: each defect type, caught or missed, plus the clean-control result. Then they can open the log to see which prompt produced which check.

## 4. What does it prove about me?

It is meant to show four things this course teaches:

- **Prompt contracts:** a written contract for what a generated check must look like (pandera schema, one rule per column property, no access to the defect list).
- **Agent loops:** Claude Code writes checks, runs them, reads what was missed, and revises, for one or two rounds, each round logged.
- **Verification:** every check must pass on the clean sample and fail on the broken one; a check that rejects clean data is counted as a failure.
- **Evaluation:** catch rate per defect type, reported with the misses, not just a single score.

A reviewer could fairly conclude that I can build a small, testable data-quality pipeline and measure an AI tool's output instead of trusting it. The evidence will be the scorecard, the round-by-round log, and the prompts in the repo. Until those exist, this is a plan, not a result.

## 5. What is in, what is out, what comes first?

- **In:** one public table (for example, a sample of about 10,000 rows from one month of NYC yellow taxi trips), five defect types (duplicate rows, missing values, impossible values such as a negative fare, a drop-off time before its pick-up time, wrong data types), one scorecard.
- **Out, on purpose:** orchestration and scheduling (no Airflow), dashboards or a web app, more than one dataset, dbt and warehouses.
- **First piece that runs:** one defect type, one generated check, and one printed line that says CAUGHT or MISSED. Someone will know it ran because that line prints, and because the same check also prints PASS on the clean sample.

## 6. What could sink it?

**Risk:** checks that are too loose. A check that passes everything also catches nothing, and a catch rate built on loose checks would be meaningless. The opposite failure is checks so strict they reject clean data.

**What I will do about it:** every check runs twice, on the clean control and on the broken copy, and both results are reported. A second, related risk is leakage: if Claude can see the defect list, the score means nothing. The check writer and the defect planter will be kept separate, and every prompt will be logged so a reviewer can confirm it.

## 7. Why this project?

This project will help me land a data job, like a Data Engineer or a Data Analyst role. Data quality and pipeline
testing are part of that work, and the same approach can be pointed at the kind of data a specific company works with.

It will highlight the skills I am working on. I am not claiming any of them as finished skills yet, and the project is
how I will build and show them:

- **Skills I am working on:** Python, pandas, cleaning and validating tabular data, pandera, running Claude Code as an
  agent loop that writes and revises checks, and scoring generated checks against planted defects.
- **Evidence:** none is claimed today. The evidence for these skills will be the DataSentry repository itself: the
  scorecard, the round-by-round log, and the prompts.

---

## Exists today (2026-10-14)

- This brief.
- The pitch film, its beat sheet, and its build files in this folder.
- Notes on dbt data tests and Great Expectations / GX Cloud ExpectAI, with links and dates, in SOURCES.md.

## Will exist

- The DataSentry GitHub repository.
- The check-writer prompt contract and the Claude Code workflow.
- The defect-planter script and the clean 10,000-row sample.
- The scorecard (catch rate per defect type) and the round-by-round log.
- A write-up of where Claude's checks were wrong and how that was caught.
