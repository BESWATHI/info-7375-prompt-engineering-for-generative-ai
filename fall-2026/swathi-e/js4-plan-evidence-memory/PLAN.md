# JS4 — The Plan, the Evidence, and the Memory

**Version:** 2.1  
**Date:** 2026-11-27 (Version 1: `9d81c4b3`; Version 2: `acf59c14`)  
**Author:** Swathi Baba Eswarappa  
**Status:** Version 2.1, records later findings from the terms-of-use review (see `TERMS-GATE.md` and section 15). Written before any JS4 implementation or agent execution.  
**Authorship:** Version 1: section outline and questions from Claude Chat (2026-11-27); initial text drafted with ChatGPT assistance based on my approved design decisions; I reviewed and approved it. Version 2: first review by Claude Chat (2026-11-27, recorded in `REVIEW.md`); I decided every finding myself; the revised wording was drafted by Claude Chat from my decisions, and I reviewed and approved it before committing. Version 2.1: research on terms of use by Claude Chat; the decisions recorded in `TERMS-GATE.md` are mine; the revised wording was drafted by Claude Chat from those decisions and approved by me.

## 1. Goal and Boundaries

My goal is to extend my JS3 job-search agent so that it follows a reviewed plan before running, checks important claims against independent evidence, and remembers postings across runs without silently losing information.

I will reuse parts of my completed JS3 project, including the collectors, filtering rules, saved responses, and existing tests. JS4 will be developed in a separate folder without changing the submitted JS3 project.

The agent will use the fictional job seeker Priya Nair and three job boards:

- Databricks through Greenhouse.
- Stripe through Greenhouse.
- Plaid through Ashby.

A run will collect or replay postings, filter them, produce limited claims, check available evidence, update versioned memory, and create a report explaining what was verified and what remains uncertain.

The agent will never apply for jobs, send emails or messages, log into accounts, or access private job-search information. It will not use a language model during execution. Network requests will be limited to approved public endpoints, and writes will be restricted to approved JS4 directories.

I will not make pay claims. Pay is out of scope for this agent: the JS3 implementation does not extract compensation, and both providers return compensation only through optional parameters (Greenhouse `pay_transparency=true` on the per-job endpoint; Ashby `includeCompensation=true`) that this agent does not request. This limitation will be explicit in the evidence matrix and output.

**Starting point:** JS3 final commit `c2e624eed28e441adfd9d7fce69168f7247529b0`.

## 2. Steps, Inputs, Outputs, and Permissions

| Step | Inputs | Outputs | Permissions |
|---|---|---|---|
| S0. Validate setup | Approved configuration, budget file, source commit, state schema; in live mode, the terms-of-use and endpoint-permission record | Setup report with mode, budget sha256 and gate results | Local reads only |
| S1a. Greenhouse watcher | Databricks and Stripe listings (saved JS3 blobs in replay mode, or allow-listed GET requests in live mode) | Per-board source records and fetch metadata | Read saved Git blobs, or GET to `boards-api.greenhouse.io` only |
| S1b. Ashby watcher | Plaid listing from saved JS3 blobs only (November 17 and November 19 collections) | Per-board source records and fetch metadata | Read saved Git blobs only; no live Ashby requests in JS4 (terms gate decision) |
| G1. Completeness gate (per board) | Fetch metadata and raw records for one board | Board status: complete, incomplete or suspect | Local processing only |
| S2. Normalize and filter | Source records, fictional persona, JS3 rules | Filter decisions and claims per posting | Local processing only |
| S3. Verify claims | Raw source evidence, claims, raw response files | Check outcomes for quote, location and reconciliation checks | Local reads only |
| S3L. Greenhouse liveness | Day-2 complete Greenhouse listings, Day-1 memory | Positive-control results and per-ID lookup results | GET to `boards-api.greenhouse.io` only, within budget |
| S4. Prepare memory changes | Checked records, board statuses, current state | Proposed changes with expected version | Read current state |
| S5. Commit memory changes | Proposed changes and expected version | New version, or stale-write rejection | Locked writes to `state/` |
| S6. Record worker notes | Worker results and check outcomes | Shared notes with provenance | Locked writes to `notes/` |
| S7. Reconcile and report | Raw response files, checks, state history, notes | Final report, diff, counts and run status | Writes to `evidence/` |

All runtime files must remain within the JS4 folder. The approved write directories are `state/`, `notes/` and `evidence/`. Temporary writes must also remain inside approved locations.

S1a and S1b support two modes:

- **Replay:** Read previously committed JS3 response bytes from commit `c2e624e` without making live requests. Record the original collection date and the actual replay date separately.
- **Live:** Greenhouse only. Contact only approved public board endpoints, with GET requests, the budget below, and no login. Live mode requires the S0 terms-of-use gate to have passed for that provider. Ashby has no live mode in JS4.

If a prerequisite fails, the agent must not continue as though the step succeeded.

## 3. Dependencies and Executability

The dependency graph is:

```text
S0 Validate setup (+ terms-of-use and endpoint-permission gate in live mode)
 ├──> S1a Greenhouse watcher (Databricks, Stripe) ──> G1a completeness gate (per board)
 └──> S1b Ashby watcher (Plaid) ─────────────────────> G1b completeness gate
                    │                                          │
                    └──────────────┬───────────────────────────┘
                                   v
                    S2 Normalize and filter (claims per posting)
                                   v
              S3 Verify claims: quote · location · reconciliation
                 └── S3L Greenhouse liveness (only after that board's control returned 200)
                                   v
              S4 Prepare memory changes (board status decides what may change)
                                   v
              S5 Commit memory (lock + compare-and-swap on version)
                                   v
              S6 Record worker notes (lock; posting text stored as data)
                                   v
              S7 Reconcile and report ──> STOP (complete | partial | refused)
```

The graph is acyclic: every step depends only on earlier steps, and no step needs a later result to begin.

An acyclic graph alone does not prove the workflow is executable. Before each step runs, everything it needs must already exist:

- S0 must confirm the code, configuration, budget file, state schema and output directories. Replay mode must confirm that each referenced JS3 Git object exists and matches its recorded hash. Live mode must confirm the terms-of-use record and the allow-list.
- The first state version must be initialized before any memory write.
- S1a and S1b may run in parallel because they write separate per-board outputs. They merge only after their completeness gates.
- A failure in one watcher is reported for its own boards. The other watcher's verified work is kept, and the run is marked partial.
- S3L is conditional: it runs for a Greenhouse board only after that board's positive-control lookup succeeds. The per-ID endpoint is never assumed to work.

## 4. Evidence on Every Dependency Edge

Every dependency has a condition another person can test from the files.

| Edge | Required evidence condition |
|---|---|
| S0 → S1a/S1b (live) | A terms-of-use record exists with source, date and note; every URL host is on the allow-list; the budget file is loaded and its sha256 recorded |
| S0 → S1a/S1b (replay) | Each referenced JS3 blob exists at `c2e624e:<path>`, and its sha256 equals the value recorded in the November 17 trace |
| S1a/S1b → G1 | Per board: HTTP 200 (live) or hash match (replay); parse succeeded; posting count greater than 0; response sha256 recorded; the count is computed from the raw records |
| G1 → S2 | Each board is labelled **complete**, **incomplete** (error, parse failure or 0 postings) or **suspect** (count below 50% of the previous complete count for that board). Only complete boards may produce absence or "new" results; postings on other boards are recorded as "not observed this run" |
| S2 → S3 | Every claim identifies its posting, source field or evidence reference, and producing rule |
| S3L control | For each Greenhouse board, the per-ID request for the control posting returns 200 with the same ID and title as the listing. Otherwise every lookup on that board is recorded as "not run (control failed)" |
| S3L lookup | Each lookup result records HTTP status, date and that board's control result. A 404 is used only if that board's control passed |
| S3 quote | Each quote receives exactly one outcome: exact, normalized match or absent, under the rule in section 5 |
| S3 reconcile | Counts recomputed from the raw response files equal the summary's counts; any mismatch, including the planted 42-versus-99 case, is recorded as a claim-check failure |
| S3 → S4 | Every check outcome is recorded as passed, failed or insufficient; unresolved claims are never treated as verified |
| S4 → S5 | The proposal records `expected_version` and each board's status; it changes no availability for postings on incomplete or suspect boards |
| S5 → S6 | Success: version increased by 1, new sha256 recorded, history file written. Stale: the rejection records expected and actual versions, and the state file's sha256 is identical before and after |
| S6 → S7 | Each note has worker, run, board, posting ID, source, status and timestamp; posting text appears only inside a JSON `data` string |
| S7 → STOP | Run status is partial if any board was incomplete or suspect; the report lists every failed or insufficient claim; summary counts equal the raw recomputation |

Terms such as "looks correct" or "seems reliable" are not acceptance conditions. If an edge condition fails, the dependent step stops or follows a documented refusal path (section 8).

## 5. Claims and Independent Checks

The JS4 agent may produce these claims:

- Whether a posting is listed in the latest complete board response.
- Whether a posting ID is new relative to stored memory (complete boards only).
- Whether its location or remote status satisfies the fictional persona's requirements.
- What the posting explicitly says about sponsorship or work authorization.
- Whether its role matches the existing filter.
- Whether its experience requirements match the early-career rules.

The full evidence matrix will be written separately in `EVIDENCE-MATRIX.md`.

I plan four checks:

| Check | What it catches | Why it fails differently |
|---|---|---|
| Greenhouse per-ID liveness lookup, with a positive control per board | A remembered or listed posting that is no longer retrievable | Uses a separate per-posting request instead of the board listing or memory. It is independent of the listing, but not independent of Greenhouse itself: a Greenhouse-wide outage affects both, which is why the positive control must pass first |
| Sponsorship quote verification | Incorrect quotations, paraphrase drift or quotes attributed to the wrong posting | Matches the claimed quote against the raw source using a separately written normalization, not JS3's `descriptions.py` |
| Location recomputation | Incorrect location interpretation or field parsing | Uses an independently written path through alternative raw fields (Greenhouse `offices`, Ashby `address.postalAddress`) instead of rerunning the original parser on `location.name` |
| Trace-summary reconciliation | Incorrect reported counts, including the planted 42-versus-99 error | Recomputes counts from the raw response files, not from counters recorded by the same loop that wrote the summary or trace |

**Quote match rule.** Each quote gets one outcome:

- **Exact:** the quote appears unchanged in the raw source field.
- **Normalized match:** it appears after this normalization, applied to both quote and source: unescape HTML entities, strip tags, apply Unicode NFKC, collapse runs of whitespace to single spaces. Case is kept.
- **Absent:** it does not appear even after normalization.

If the raw data does not support a claim, the output says **insufficient evidence**, not verified.

For Ashby, no per-posting liveness endpoint has been established. I will not claim independent Ashby liveness verification.

The agent makes no pay claims. The evidence matrix lists pay as out of scope.

## 6. Versioned Memory and Revision Rule

JS3's `seen_ids.json` stores posting IDs but has no versioned writes or compare-and-swap protection. JS4 introduces a new state format and does not modify JS3's state.

The new state records:

- A monotonically increasing version number.
- A content hash.
- Posting identifiers and board names.
- First-seen and last-observed dates.
- Each board's status for each run (complete, incomplete or suspect).
- Verification status and timestamps.
- Source references for every remembered fact.
- Relevant run identifiers.

Each remembered fact identifies its source: a saved response reference, source field, collection time or verification record.

Every proposed update declares the version it expects. A writer must acquire exclusive access to the state before checking the version and committing its update. If the current version differs from the expected version, the write is rejected and the state is not modified.

The rejection records expected version, actual version, worker and run identifier. The writer may reread the state and recompute a new proposal, but it must not retry the same stale update.

Successful versions are kept in an append-only history.

**Availability is only changed for complete boards.** The agent uses exactly these status phrases:

- **"Listed in the latest complete board response."**
- **"Not observed this run (board incomplete or suspect)."** Memory for that board is left unchanged.
- **"Previously listed; not present in the latest complete board response. Current availability not verified."**
- If a Greenhouse lookup was made: **"Direct posting lookup returned HTTP 404 on [date]; this board's positive control returned 200 on the same day."**

None of these proves that the employer filled or permanently closed a position.

## 7. Two Workers and Shared Notes

I will use two watchers:

**Greenhouse watcher:** Processes Databricks and Stripe.

**Ashby watcher:** Processes Plaid.

The watchers are independent at the source level because they read different companies and board APIs. They are not independent opinions about relevance because they share the same project design, normalization approach and filtering rules.

Both watchers write results into one shared notes file. Each note includes the worker identifier, board, posting ID, run identifier, source reference, evidence status and timestamp.

The notes use structured JSON records rather than executable instructions. An exclusive lock prevents simultaneous writes from corrupting or overwriting the file.

Untrusted posting text is stored only as data inside a JSON string. It must never be interpreted as a system instruction, command, policy or authorization to change scoring rules.

A deliberately seeded posting containing instruction-like text will test this boundary. The fixture will be clearly labelled as seeded.

## 8. Stop Conditions and Refusal Paths

A run stops normally after processing the approved boards, completing the available checks, committing permitted state changes, reconciling counts and writing the final report.

Failures are handled in two different ways.

**Integrity failures stop the dependent operation:**

- The requested host is not allow-listed.
- A request would exceed the configured budget.
- An input file is missing or its hash differs from the recorded value.
- A required state version is stale.
- The state schema is invalid.
- An operation would write outside approved directories.
- Live mode is requested without a passed terms-of-use gate, or for Ashby (no-go in `TERMS-GATE.md`).
- The per-ID endpoint is used before that board's positive control has passed.

**Claim-check failures are recorded and the run continues:**

- A quote is absent from its source.
- A recomputed location disagrees with the claim.
- Recomputed counts disagree with the summary (including the planted 42-versus-99 case).
- A liveness lookup returns 404 or cannot be completed.

A failed claim check marks that claim as failed or insufficient, keeps it out of verified memory, and is reported. This allows a planted error to be detected without invalidating the rest of the demonstration.

**Network retries and check failures are different.** A transient network error (timeout, HTTP 5xx, connection reset) may be retried once, and the retry counts against the budget. A 4xx response is never retried. A failed evidence check is never retried.

A stale memory write requires rereading the latest state and recomputing the proposed update. Repeating the old write is prohibited.

The report distinguishes complete, partial, refused and failed runs.

## 9. Budgets and Authority

Day-2 live run limits:

| Resource | Limit |
|---|---|
| Boards | 3 approved boards |
| `boards-api.greenhouse.io` | 8 requests maximum: 2 listings + 2 positive controls (one per board) + up to 4 per-ID lookups (2 per board); no `questions=true` or `pay_transparency=true` parameters |
| `api.ashbyhq.com` | 0 requests (live access is no-go in JS4; see `TERMS-GATE.md`) |
| Total live requests | 8 maximum |
| Network retries | At most 1 per request, transient errors only, counted in the budget |
| Network timeout | 15 seconds per request |
| Overall live run | 120 seconds maximum |
| Evidence-check retries | None |
| Applications, emails, logins | 0 |

If the Greenhouse budget runs short, priority is: listings, then positive controls, then lookups. Lookups are optional; a retry uses a lookup's slot, and skipped lookups are reported as "not run (budget)".

The endpoint verification and the positive control are the same request: the first per-ID request for a posting that is present in that board's Day-2 listing.

The agent may process all postings returned by the approved board requests, but must not expand its search to additional boards.

Only I may approve changes to these budgets. Changes must be reflected in the configuration and documented in a Git commit with a reason. The agent, the workers and AI development tools cannot increase the budgets.

## 10. Two-Day Evidence

Each board keeps its own actual collection dates. The comparison is per board.

| Board | First observation | Second observation |
|---|---|---|
| Databricks (Greenhouse) | November 17, 2026 — replay of saved real responses | November 28, 2026 — live run, if the S0 gate and the run succeed |
| Stripe (Greenhouse) | November 17, 2026 — replay of saved real responses | November 28, 2026 — live run, if the S0 gate and the run succeed |
| Plaid (Ashby) | November 17, 2026 — replay of saved real responses | November 19, 2026 — replay of saved real responses (historical) |

**Labels.** Every replayed observation is labelled:

"Replayed from saved responses originally collected [original date]; replay executed on [actual date]."

The live Greenhouse observation is labelled with its actual request timestamps. Plaid's November 19 observation is historical and is never described as a November 28 or live result.

**Greenhouse fallback.** If the Greenhouse live gate or collection fails, the Greenhouse boards use the saved November 19 responses instead, labelled historical, and no live liveness lookups are made.

**Diff.** Compare stable posting IDs per board, only for boards that are complete on both of their dates, and report:

- IDs observed on both dates.
- IDs newly observed on the second date.
- IDs present only on the first date.
- Changes in relevant fields, where evidence supports comparison.

Boards that are incomplete or suspect on either date are listed as "not compared" with the reason. The report states each board's two dates next to its results.

**Liveness lookups (Greenhouse live run only).** For each Greenhouse board:

1. **Positive control:** look up the lowest posting ID present in that board's November 28 listing. It must return 200 with the same ID and title.
2. **Lookups:** only if the control passed, look up the 2 lowest posting IDs that were present on November 17 and absent from the complete November 28 listing.

These selection rules are fixed in advance to prevent choosing favourable examples. Plaid has no liveness check: its absences are reported only as "previously listed; not present in the latest complete board response" with the November 19 date.

If a control fails, the lookups for that board are not run, and I record the limitation rather than claim a liveness result. A separately labelled seeded case may demonstrate the memory behaviour, but it will not be presented as proof of a real posting disappearing.

The fresh-is-not-true demonstration will show a remembered "listed" status being challenged by later evidence, with the evidence's strength and date stated exactly.

## 11. Seeded and Planted Evidence

Two deliberate test cases are planned.

**Planted incorrect claim.** A seeded run summary will report 99 records where the saved raw responses contain 42. The independent reconciliation check must detect and report the difference as a claim-check failure. The planted summary and its source data are preserved and never mixed with real collection statistics.

**Instruction-injection fixture.** A seeded job description will contain instruction-like language asking the agent to change its behaviour. The expected outcome is that the text is stored as untrusted data and does not change the filtering rules, permissions, memory policy or allowed operations.

Seeded and planted files carry explicit labels, including the fixture identifier and actual test date.

Reports distinguish:

- Real historical source responses.
- Live source responses.
- Replays of historical responses.
- Seeded fixtures.
- Deliberately planted errors.

No simulated outcome will be described as a real external event.

## 12. Premortem Timing

A separate `PREMORTEM.md` will be written and committed before the deliberately triggered shared-memory failure.

My planned failure area is a lost update caused by two workers reading the same memory version and then attempting to write conflicting updates.

The premortem will predict the failure mechanism, expected consequence and intended protection before the test is run. After committing it, I will trigger the conflict with a deterministic interleaving test. The actual result will be documented separately.

The commit history must show that the premortem existed before the failure experiment. I will not write a prediction after observing the failure and present it as a premortem.

## 13. Privacy, Security, and Terms of Use

I will use only fictional persona information in the public JS4 project.

My real résumé, personal contacts, credentials, private tracker and conversation transcripts will remain outside the submission.

The JS3 inspection found that some raw saved responses contain recruiter-related information and an email-like contact string. I will not duplicate those full raw responses into JS4. The replay references the existing JS3 Git objects by commit and path, with their hashes verified.

Only the minimal derived evidence needed to explain JS4 results will be included.

Allowed public hosts for live requests:

- `boards-api.greenhouse.io`

`api.ashbyhq.com` remains on the allow-list for recognising saved responses, but live requests to it are refused in JS4.

Network access uses HTTPS GET requests only, with exact host checks, the budget in section 9, and no login.

Before any live run, S0 checks the terms-of-use and endpoint-permission record in `TERMS-GATE.md`: which published terms or documentation were read, the date, and the conclusion. The current decisions are: Greenhouse conditional go (at most 8 read-only GET requests, no optional question or pay parameters); Ashby no-go for live requests. Public accessibility alone is not proof that an endpoint may be used.

Posting descriptions are untrusted data and must never authorize additional network requests, commands or policy changes.

Before submission, I will inspect the new files for private paths, credentials, personal contact details and unnecessary copied source content.

## 14. Reuse and Provenance

The JS4 project will reuse only the JS3 components needed for this assignment. The initial candidates are:

- `loop.py` — collection workflow and injectable transport.
- `parsers.py` — Greenhouse and Ashby parsing.
- `job_filter.py` — version 1.1 filtering.
- `descriptions.py` and `rule.py` — supporting filtering logic.
- `persona.py` and the fictional persona configuration.
- `policy.py` — security and write rules, requiring modifications.
- Relevant existing test patterns.

The final list will be recorded after checking which dependencies are actually needed.

For each reused file, the project distinguishes copied unchanged, copied and modified, and newly written. The provenance record includes the original JS3 commit, source path, original file SHA-256, destination path, resulting SHA-256 and any modifications. The checks in section 5 are newly written and do not import the producer's parsing code.

The submitted JS3 folder and original evidence remain unchanged.

The JS4 README will name the source project, programming language, dependencies, exact commands, tests and executed runs.

## 15. Review and Change Log

### Reviewer

Claude Chat, as first reviewer. The full review and my decisions are in `REVIEW.md`.

### Review date

November 27, 2026. The review covered Version 1, commit `9d81c4b3`.

### Criticisms and counterexamples

- **R1:** A failed or empty board fetch would look like every remembered posting had disappeared.
- **R2:** A 404 from the per-ID lookup is not trustworthy without a positive control.
- **R3:** The Greenhouse host budget did not fit the planned requests, and network retries were mixed up with check retries.
- **R4:** Stopping the run on any failed check conflicted with the planted-error demonstration.
- **R5:** Reconciling against the trace may not be independent of the summary.
- **R6:** The quote check had no defined match rule.
- **R7:** The graph did not show the parallel watchers.
- **R8:** The terms-of-use check was not a step.

### My evaluation of each criticism

I accepted all eight. I verified R3's arithmetic myself (2 + 1 + 1 + 5 = 9, exceeding 8) and chose to reduce optional lookups rather than raise the budget. My decision and reason for each finding are recorded in `REVIEW.md`.

### Counterexample that changed the plan

**R1.** Scenario: on Day 2, the Ashby request times out, fails, or returns HTTP 200 with zero postings, while Greenhouse succeeds. Version 1 would have reported all 142 Plaid postings as present only on the first date and changed their remembered status, which would be false for every one of them.

Version 1 allowed this because absence was computed over all remembered postings without requiring that board's fetch to be complete.

The resulting architectural change is the per-board completeness gate G1, the complete / incomplete / suspect board status, the rule that availability changes only for complete boards, and the "not observed this run" status.

### Changes made in Version 2

- Watchers shown as two branches (S1a, S1b) with per-board completeness gates (R1, R7).
- Large count drops (below 50% of the previous complete count) treated as suspect (R1).
- Positive control per Greenhouse board before any 404 is used; honest statement of what the liveness check is independent of (R2).
- Budget rebalanced to 8 Greenhouse and 2 Ashby requests; endpoint verification combined with the positive control; network retries separated from check failures (R3).
- Integrity failures separated from claim-check failures (R4).
- Reconciliation recomputed from raw response files (R5).
- Quote outcomes defined as exact, normalized match or absent, with a documented normalization rule (R6).
- Terms-of-use and endpoint-permission gate added to S0 (R8).

### Later findings that reopened a decision

**2026-11-27 — Terms-of-use review (recorded in `TERMS-GATE.md`).** Found before any implementation or live request.

- **Ashby live access → no-go.** Ashby documents its public posting API for an organization's own careers page and offers a separate partner-feed channel, with customer opt-in, for third parties that ingest postings. Permission for third-party reading is uncertain, so S1b is replay-only, the Ashby live budget is 0, and Plaid's second observation is the saved November 19 collection (sections 2, 9, 10, 13).
- **Greenhouse live access → conditional go.** The Job Board API documents its GET endpoints as public and unauthenticated, including the per-job endpoint. Permission for third-party reading is not explicit, so live use is limited to 8 read-only requests without optional question or pay parameters (sections 9, 13).
- **Pay rationale corrected.** Version 2 said Plaid's response has no compensation field. That is true only for the request this agent makes: both providers offer compensation through optional parameters. The no-pay-claims decision is unchanged; its reason now says pay is out of scope and those parameters are not used (section 1).
- **Per-board dates.** Greenhouse compares November 17 with November 28 (live), with November 19 as fallback; Plaid compares November 17 with November 19 (section 10).
- **Total live budget reduced** from 10 to 8 requests (section 9).

Later changes will be logged here with their actual dates and reasons, rather than rewriting earlier versions.

## 16. Open Questions and Assumptions

1. **Greenhouse per-ID lookup:** Documented by Greenhouse but not yet verified in practice. The positive control in section 10 tests it on November 28 before any lookup result is used.
2. **Ashby liveness:** No per-posting endpoint is documented, and live Ashby access is no-go in JS4. This claim remains unchecked.
3. **Historical replay:** The JS4 code must read the exact saved JS3 Git objects and verify their hashes without duplicating full raw responses.
4. **Memory coordination:** Locking and versioning must be tested to show that concurrent workers cannot silently overwrite each other's updates.
5. **Independent checking:** The checks must use different source paths or algorithms. Wrapping the JS3 parser in another function is not enough.
6. **Terms of use:** Recorded in `TERMS-GATE.md`. Live collection proceeds only for Greenhouse, within its conditions.
7. **Source disappearance:** November 17 and November 19 ID differences provide candidates. Absence is only computed for complete boards, and even then does not establish that a job is closed.
8. **Fallback evidence:** A historical two-date comparison or a seeded demonstration must be labelled accurately and not presented as a fresh live observation.
9. **Privacy:** Derived output must not reproduce unnecessary personal details from source descriptions.
10. **Environment and dependencies:** The implementation must remain compatible with the available Python environment and course repository conventions, including `scripts/validate_course.py`.

Any finding that changes one of these assumptions will be recorded with the affected step, evidence, revised decision and date.

---

**End of PLAN.md — Version 2.1**

This document describes intended behaviour and planned tests. It does not claim that JS4 has been implemented, that an endpoint has been verified, or that the planned evidence checks and failure experiments have already run.
