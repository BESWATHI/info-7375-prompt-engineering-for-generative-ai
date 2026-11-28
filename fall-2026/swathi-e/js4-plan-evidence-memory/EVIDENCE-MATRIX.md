# EVIDENCE-MATRIX — JS4 Tool Evidence Matrix

**Version:** 1  
**Date:** 2026-11-27  
**Written before:** any JS4 implementation, test run or agent run  
**Based on:** `PLAN.md` Version 2.1 (sections 4, 5, 6, 9, 10) and `TERMS-GATE.md`  
**Authorship:** Drafted by Claude Chat from my approved plan; I reviewed every row, decided what is checked and what is not, and approved it before committing.

This matrix lists every claim the agent makes about a posting or a run, what produces it, what checks it, and why that check fails differently from the producer. Where a claim is not checked, the matrix says so and why.

---

## 1. The matrix

| # | Claim | Producer (generator) | Check | Failure the check catches | Why it fails differently | Runs in JS4? | Expected on real data | Expected on seeded data |
|---|---|---|---|---|---|---|---|---|
| C1 | **Listed** — posting is listed in the latest complete board response | Watcher S1a/S1b + completeness gate G1 (presence of the ID in that board's listing) | **K1 Greenhouse liveness:** per-job `GET /v1/boards/{board}/jobs/{id}`, only after that board's positive control returned 200 with matching ID and title | A remembered or listed posting that is no longer retrievable; a wrong URL or board name (caught by the control) | Separate per-posting request instead of the list. Independent of the listing, **not** of Greenhouse itself (an outage affects both, which is why the control must pass first) | Greenhouse: yes, November 28 live run only, at most 2 lookups per board. Plaid: **no** (no per-posting endpoint; live Ashby is no-go) | See `PREDICTIONS.md` P8, P9 | Control-failure fixture: all lookups "not run (control failed)" |
| C2 | **New** — posting ID not in memory before this run | Memory diff in S4 | **K4 reconciliation (part b):** new and first-date-only counts recomputed from the raw response files of both dates | A diff bug, a stale memory version, or an incomplete board producing false "new" or false "gone" | Recomputes set differences directly from raw bytes with separately written ID extraction, instead of reading memory | Yes, per board, only for boards complete on both dates | P3, P4 | Incomplete-board fixture: no new or gone results for that board |
| C3 | **In the US / remote in the US** | JS3 filter v1.1 rule (location from `location.name` / Ashby `location`) | **K3 location recomputation** from alternative raw fields: Greenhouse `offices[].location`/`offices[].name`; Ashby `address.postalAddress.addressCountry` and `secondaryLocations[].address` | Misreading of the location string; a parser error; a location the filter mis-classified | Independently written code reading different fields; does not import `parsers.py`, `descriptions.py` or `job_filter.py` | Yes, every posting on replayed and live boards | P6 | Fixture with conflicting fields: disagreement reported, not hidden |
| C4 | **Sponsorship statement** — the filter's "no sponsorship restriction" claim, with its quote when contradicted | JS3 filter v1.1 (claims with label and quote) | **K2 quote verification:** each quote matched against the raw source field; outcome exact / normalized match / absent (rule in `PLAN.md` section 5) | A quote that is not in the posting, belongs to another posting, or drifted from the source | Matches against raw source with separately written normalization (entities unescaped, tags stripped, Unicode NFKC, whitespace collapsed; case kept), not JS3's `html_to_text` | Yes, on every claim that carries a quote. Claims labelled insufficient have no quote; they are reported as insufficient, never as verified | P5 | Misquote fixture: absent; wrong-posting fixture: absent |
| C5 | **Role match** (AI/ML or data engineering) | JS3 filter v1.1 | K2 checks that any supporting quote exists in the source | A misquoted supporting phrase | Same as K2 | Quote existence only. **Not checked:** whether the filter's judgement of relevance is right. No independent source exists for that; JS3's 48-posting hand audit is prior evidence, not a JS4 check | Covered by P5 | — |
| C6 | **Asks 0–1 years of experience** | JS3 filter v1.1 | K2, as for C5 | A misquoted requirement | Same as K2 | Quote existence only. **Not checked:** the interpretation of the requirement | Covered by P5 | — |
| C7 | **Run summary counts** (postings per board, verdict totals, new, first-date-only) | Summary writer in S7 | **K4 reconciliation (part a):** counts recomputed from raw response files | A wrong summary, including the planted 42-versus-99 error | Counts from raw bytes, not from the counters the same loop used to write the summary or trace | Yes, every run | P2, P3 | **Planted:** summary says 99, raw fixture holds 42 → claim-check failure; run continues |
| C8 | **Board status** (complete / incomplete / suspect) | Completeness gate G1 | Edge conditions in `PLAN.md` section 4 (HTTP 200 or hash match; parse OK; count > 0; count not below 50% of previous complete count) | An error, empty list or large drop silently treated as real absence | Rule applied before any memory change; tested with fixtures | Yes, every board, every run | P2, P7 | 0-posting fixture → incomplete; 40%-of-previous fixture → suspect |
| C9 | **Pay** | — | — | — | — | **Not claimed.** Out of scope; compensation is only available through optional parameters (Greenhouse `pay_transparency`, Ashby `includeCompensation`) that this agent does not request | — | — |
| C10 | **Ashby / Plaid liveness** | — | — | — | — | **Not checked.** No per-posting endpoint is documented, and live Ashby access is no-go in JS4. Plaid absences are reported only as "previously listed; not present in the latest complete board response" with the November 19 date | — | — |

---

## 2. Checks actually run (at least three required)

| Check | Claims covered | Data |
|---|---|---|
| K1 Greenhouse liveness with positive control | C1 | November 28 live run (Databricks, Stripe) |
| K2 Quote verification | C4, C5, C6 | November 17 replay (all boards) and November 28 live (Greenhouse) |
| K3 Location recomputation | C3 | All replayed and live boards |
| K4 Reconciliation (counts and set differences from raw bytes) | C2, C7 | Every run, plus the planted fixture |

If the Greenhouse live run cannot happen, K1 is recorded as "not run" with the reason, and three checks (K2, K3, K4) still run.

---

## 3. Independence statement

- **K2, K3 and K4** are written separately from the producer and must not import `parsers.py`, `descriptions.py` or `job_filter.py`. A test enforces this by scanning their imports.
- **K1** uses a different endpoint but the same provider, so it can share a provider-wide failure. The per-board positive control is the guard against that.
- **What no check covers:** whether the filter's relevance judgements (role match, years of experience) are correct. The checks verify that quoted evidence exists, not that it was interpreted correctly. This limit is stated in the sign-off.

---

## 4. Labels used in outputs

Every check result carries one of: **passed**, **failed**, **insufficient**, **not run (reason)**. Every observation carries its source label: **replay of saved responses (original date)**, **live (timestamp)**, **seeded fixture (ID)**, or **planted error (ID)**.
