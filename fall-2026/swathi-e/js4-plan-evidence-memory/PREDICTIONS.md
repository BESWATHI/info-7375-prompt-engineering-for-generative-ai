# PREDICTIONS — JS4 (recorded before tests and runs)

**Version:** 1  
**Date:** 2026-11-27  
**Committed before:** any JS4 test run, implementation or agent run  
**Authorship:** Proposed by Claude Chat from the JS3 inspection and my plan; I reviewed each prediction, adjusted what I disagreed with, and approved the final values. The predictions are mine.

Each prediction states what I expect, how confident I am, and what it is based on. Results will be compared against these in a separate file after the runs. A wrong prediction will be reported as wrong, not edited.

---

## A. Tests before implementation (C3c)

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P1 | When the new tests are run against interface stubs (functions that raise `NotImplementedError`), **every behavioural test fails**. The only tests expected to pass are the static checks that need no implementation: (a) the check modules do not import `parsers.py`, `descriptions.py` or `job_filter.py`; (b) every seeded and planted fixture carries a `SEEDED` or `PLANTED` label. | High | Stubs contain no logic; static checks only read source and fixture files |

## B. Day 1 — replay of saved November 17 responses

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P2 | All three boards pass the completeness gate as **complete**. Counts recomputed from raw bytes: **Databricks 901, Stripe 789, Plaid 142**. Each raw file's sha256 matches the November 17 trace. | High | JS3 inspection of commit `c2e624e` (counts and hash matches) |

## C. Plaid second observation — replay of saved November 19 responses

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P3 | Plaid is complete on both dates. Recomputed from raw IDs: **3** IDs present only on November 17, **2** present only on November 19. The memory diff and the raw recomputation agree. | High | JS3 inspection's offline comparison |
| P4 | Plaid's 3 first-date-only postings are reported as "previously listed; not present in the latest complete board response" with the November 19 date, and **none** is reported as closed or as verified gone. | High | Plan rule; Plaid has no liveness check |

## D. Checks on replayed data

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P5 | Quote verification: **0 quotes absent**. Every quote is an exact or normalized match. I expect most to be normalized rather than exact, because JS3 quotes came from converted text, not raw HTML. | Medium–high | JS3 test confirmed quotes are exact substrings of converted text for Plaid; the separate normalizer may still differ on edge cases |
| P6 | Location recomputation agrees with the filter's US claim for **at least 95%** of postings. Every disagreement is listed with both values. | Medium (a guess) | Alternative fields usually match the location string, but multi-office and remote postings may differ |

## E. Day 2 — Greenhouse live run (November 28), if the gate and run succeed

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P7 | Both Greenhouse boards are **complete**, with counts within 20% of November 17 (Databricks 901, Stripe 789), so neither is suspect. At most **8** requests are made; **0** requests go to Ashby. | Medium | Two days of drift between November 17 and 19 was small (34/33 and 44/25 IDs). November 17 to November 28 is an 11-day interval, so that two-day drift is supporting evidence, not proof that the longer interval will behave the same way |
| P8 | Both positive controls return **200** with matching ID and title. | Medium–high | The per-job endpoint is documented; not yet observed |
| P9 | At least one Greenhouse posting listed on November 17 is absent from the complete November 28 listing (**fresh is not true**), and at least one of the up to 4 per-job lookups returns **404**. | Medium | Eleven days of drift; but an absent posting might still resolve by direct link |

## F. Seeded and planted cases

| # | Prediction | Confidence | Basis |
|---|---|---|---|
| P10 | The planted summary (99) disagrees with the raw fixture (42): reconciliation records a **claim-check failure**, and the run still finishes (it is not refused). | High | Plan section 8 |
| P11 | The injection fixture is stored only as data; the filter's verdict and score for the fixture are **identical** with and without the instruction-like text. The fixture is built so that the instruction-like text adds no role, experience, location or sponsorship keywords and does not change the posting's legitimate requirements; the only difference between the two versions is the instruction-like text. This isolates whether the instruction is followed from normal keyword matching. | High | No model in the loop; text is never executed |
| P12 | A write against a stale memory version is **rejected**, and the state file's sha256 is identical before and after. | High | Compare-and-swap rule |
| P13 | Any attempt to contact `api.ashbyhq.com` live, an unlisted host, or a ninth Greenhouse request is **refused** before the request is sent. | High | Policy and budget rules |

---

## G. Not predicted here

The two-worker shared-memory failure is predicted in `PREMORTEM.md`, which will be written and committed before that failure is triggered.
