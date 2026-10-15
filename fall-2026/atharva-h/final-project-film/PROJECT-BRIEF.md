# Project Brief — SponsorSQL (working title)

**Atharva Hambir · INFO 7375 · Target role: Data Analyst · Stack: Python, DuckDB, Claude**

This is a pitch. Nothing in this project has been built yet. Everything below is written as "will" unless it is listed under *Exists today*.

## 1. What is it?
SponsorSQL will let an international student ask a question about public H-1B filing data in plain English, then show the SQL Claude wrote, the answer, and whether that answer matched a hand-checked answer key. When it is done, it will be a GitHub repository with the question tool, a fixed test set, and an evaluation log that records every question Claude got wrong and why.

## 2. Why would anyone care?
An international student looking for work needs to know which employers have filed for H-1B workers in their field and city, and at what wages. That information is public in the U.S. Department of Labor's LCA disclosure files, but each file is a large spreadsheet most students cannot easily query. I have looked at two alternatives. ChatGPT can write SQL from a plain-English question and help analyze data, but a query it writes is not guaranteed to be correct, and the user still has to check the logic and the result. Vanna.ai is built for turning questions into SQL using database context, which makes it a more focused workflow, but its queries still need checking too. I have not run a structured, hands-on comparison of either tool for this project, so I am not claiming SponsorSQL will be more accurate than they are. The difference is that SponsorSQL will make its accuracy measurable and its mistakes visible. Every test question will have the SQL Claude wrote, an expected answer I worked out independently, a recorded pass or fail, and a written explanation whenever it fails.

## 3. Who opens it, and what do they do?
The reader is a hiring manager for a Data Analyst role. In the first sixty seconds they will open the README and see the evaluation table: how many test questions there are, how many Claude answered correctly, and a link to the failure log. Then they will be able to run one command, ask their own question, and see the SQL and the answer. The end user is an international student looking for a sponsoring employer.

## 4. What does it prove about me?
It will show SQL and data cleaning on a real, messy public dataset. It will also show four things this course teaches. **Prompt contracts:** Claude gets the table schema and written rules for the SQL it may write. **Verification:** each answer is compared with an answer I wrote and checked by hand. **Evaluation:** a failure rate on a fixed test set, with every failure sorted by its cause. **Source grounding:** every answer names the filing year, the source file and the query. A reviewer could fairly conclude that I can query real data and that I measure where an AI's SQL is wrong instead of trusting it. The evidence will be the test set, the run logs and the failure log in the repository.

## 5. What is in, what is out, what comes first?
**In:** one complete fiscal year of LCA disclosure data (FY2025, October 2024 to September 2025, from the Department of Labor's OFLC Performance Data page), loaded into DuckDB, with questions about employers, job titles, locations and wages.
**Out:** it will not tell anyone whether they will be sponsored, and it will not give immigration or legal advice. An LCA filing is not a job offer or a visa approval, and the tool will say so.
**First:** ten questions, a hand-checked answer key, Claude's SQL run against both, and a printed pass/fail table. Someone will know it ran because the run log will record the date, the command, every query and the result, and running the same command will reproduce the table.

## 6. What could sink it?
The data is messy. The same company can appear under slightly different spellings of its name, and the file has a separate field for trade names (`TRADE_NAME_DBA` in the FY2025 record layout). The same role also appears under many job titles. Claude's SQL could look correct and still undercount. This is the failure most likely to fool a user. To catch it, I will write test questions built around these name and title variations, compare the counts Claude gets with my hand-checked ones, and log every mismatch. If Claude keeps failing on them, the tool will show the matching rows it used instead of a single total, so the user can check the answer for themselves.

## 7. Why this project?
It is a mix of showing off and learning. **Skills I already have:** SQL, Python and pandas, and dashboards/BI, from earlier academic and professional work. That earlier work includes a SQL and Power BI data-modelling project and a crime-data analysis in Snowflake. It is separate from this project and is not shown in the film. SponsorSQL's own SQL and evaluation results will be the evidence for these skills. **Skills that are new to me:** building an evaluation harness for LLM-written SQL, writing prompt contracts for code generation, and measuring and reporting failure rates honestly. I picked this domain because I am an international student. Finding employers that have filed H-1B applications in the past matters to international students looking for work in the U.S., and I want them to be able to explore that public data through simple questions instead of having to understand a complex dataset or write SQL. The tool will say clearly that an H-1B Labor Condition Application is not proof of a job offer, of sponsorship being available, or of an approved visa petition.

---

### Exists today
- This brief (written 2026-10-13).
- The chosen data source: the Department of Labor's OFLC Performance Data page, which lists the FY2025 LCA disclosure files and record layouts (opened 2026-10-13). Nothing has been downloaded yet.

### Will exist
- The DuckDB database built from one year of LCA disclosure data
- The prompt contract (schema plus SQL rules)
- The ten-question test set with its hand-checked answer key
- The run script and its dated run logs
- The pass/fail table and the failure log
- A README that shows the evaluation table first
