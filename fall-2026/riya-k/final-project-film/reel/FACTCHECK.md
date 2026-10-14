# Fact check — Ground Truth SQL (pitch film)

Status: checked by Claude (Opus 5.5, Claude Code), 2026-10-09, against the sources named. Riya Kapadnis's sign-off: APPROVED 2026-10-14. Watched the full cut with sound; confirmed claims 5 and 10 personally.
Rule used: past tense only for things that exist and can be shown; everything else is "will".

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | The harness, repository, runner and scorecard "will" exist; "only a first slice exists" | EXEMPT (plan, future tense) | `evidence/` folder contents, 2026-10-09 | B01 and B06 carry an on-screen "CONSTRUCTED · not built yet" label |
| 2 | B02 | A hand-written join-fan-out query reported US revenue 4,667.06 vs checked 523.06; ran without error | PASS | `evidence/run_slice_output.txt`, Q03 | Narration says "a query I wrote by hand", not model output; on-screen "real run · 2026-10-09" |
| 3 | B02 | "Nine times too high" | PASS | 4667.06 / 523.06 = 8.92 | Said as "nine times", drawn 8.92× |
| 4 | B03 | BIRD: over 12,000 questions (12,751 pairs) on its own 95 databases | PASS | bird-bench.github.io, read 2026-10-09 | — |
| 5 | B03 | Vanna writes SQL for your own database; "I didn't find a way in it to test that SQL against checked answers" | PASS (search-limited: what I did not find) | github.com/vanna-ai/vanna README, read 2026-10-09 | Worded as what I did not find, not as "Vanna cannot". Riya confirmed 2026-10-14 that she read the README herself |
| 6 | B04 | Execution comparison judged 9/9 hand-labelled variants correctly; exact-text comparison rejected all 3 correct rewrites | PASS | `evidence/run_slice_output.txt` (9/9; string 6/9 = the 3 equivalents missed) | — |
| 7 | B05 | First gold answer asked about 2023; Chinook data stops in 2013; empty gold let a broken query match; runner now rejects empty gold | PASS | `evidence/run_slice_output_v0_first_run.txt` (Q08 WRONG JUDGEMENT); `sqlite3` min/max InvoiceDate 2009-01-01..2013-12-22; `run_slice.py` assert | — |
| 8 | B06–B09 | Reader's first minute, prompt contract, repair loop, classmate check, three runs | EXEMPT (plan, future tense) | PROJECT-BRIEF.md §3–§6 | All said with "will"/"should"; B06 stamped CONSTRUCTED |
| 9 | B08 | Chinook is a public sample database | PASS | github.com/lerocha/chinook-database, MIT licence (`evidence/data/CHINOOK-LICENSE.md`) | — |
| 10 | B10 | SQL, Python and LLM features in a BI product are skills used in Riya's AI Engineer co-op; that code is private | EXEMPT (personal account; Riya confirmed 2026-10-14) | Riya's own account (TwinAI co-op, Jan–Jun 2026) | No co-op code, screenshots or metrics shown |
| 11 | BCON | "Exists today: eight questions, one comparator, and one bug I caught in my own answers" | PASS | `evidence/gold_set.json` (8), `run_slice.py`, v0 output | — |
