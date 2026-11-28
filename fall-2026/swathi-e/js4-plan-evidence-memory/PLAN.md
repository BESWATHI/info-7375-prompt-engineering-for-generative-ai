# JS4 — The Plan, the Evidence, and the Memory

**Version:** 1  
**Date:** November 27, 2026  
**Author:** Swathi Baba Eswarappa  
**Status:** Version 1, written before any JS4 implementation or agent execution. Not yet reviewed.  
**Authorship:** Section outline and questions from Claude Chat (2026-11-27); initial text drafted with ChatGPT assistance based on my approved design decisions. I reviewed and approved the final text before committing.

## 1. Goal and Boundaries

My goal is to extend my JS3 job-search agent so that it follows a reviewed plan before running, checks important claims against independent evidence, and remembers postings across runs without silently losing information.

I will reuse parts of my completed JS3 project, including the collectors, filtering rules, saved responses, and existing tests. JS4 will be developed in a separate folder without changing the submitted JS3 project.

The agent will use the fictional job seeker Priya Nair and three job boards:

- Databricks through Greenhouse.
- Stripe through Greenhouse.
- Plaid through Ashby.

A run will collect or replay postings, filter them, produce limited claims, check available evidence, update versioned memory, and create a report explaining what was verified and what remains uncertain.

The agent will never apply for jobs, send emails or messages, log into accounts, or access private job-search information. It will not use a language model during execution. Network requests will be limited to approved public endpoints, and writes will be restricted to approved JS4 directories.

I will not make pay claims because the existing JS3 implementation does not consistently extract compensation information across these boards. This limitation will be explicit in the evidence matrix and output.

**Starting point:** JS3 final commit `c2e624eed28e441adfd9d7fce69168f7247529b0`.

## 2. Steps, Inputs, Outputs, and Permissions

The agent will follow these steps:

| Step | Inputs | Outputs | Permissions |
|---|---|---|---|
| S0. Validate setup | Approved configuration, source commit, state schema | Setup report | Local reads only |
| S1. Load postings | Saved November 17 responses or approved live board APIs | Identified source records and run metadata | Read saved Git blobs or GET allow-listed URLs |
| S2. Normalize and filter | Source records, fictional persona, JS3 rules | Filter decisions and initial claims | Local processing only |
| S3. Verify claims | Source evidence, claims, stored traces | Check results and uncertainty labels | Local reads; limited approved GET requests for liveness |
| S4. Prepare memory changes | Checked records and current state | Proposed changes and expected version | Read current state |
| S5. Commit memory changes | Proposed changes and expected version | New version or stale-write rejection | Controlled writes to `state/` |
| S6. Record worker notes | Worker results and verification outcomes | Shared notes and provenance | Controlled writes to `notes/` |
| S7. Reconcile and report | Traces, checks, state history, notes | Final report, counts, diff and stop reason | Controlled writes to `evidence/` |

All runtime files must remain within the JS4 folder. The approved write directories will be `state/`, `notes/`, and `evidence/`. Temporary writes must also remain inside approved locations.

S1 will support two modes:

- **Replay:** Read previously committed JS3 response bytes without making live requests. Record the original collection date and the actual replay date separately.
- **Live:** Contact only approved public board endpoints, with GET requests, request limits, and no login.

The two watchers may process different boards concurrently, but memory updates and shared-note writes must be coordinated.

If a prerequisite fails, the agent must not continue as though the step succeeded.

## 3. Dependencies and Executability

The main dependency graph is:

```text
S0 Validate setup
       |
       v
S1 Load postings
       |
       v
S2 Normalize and filter
       |
       v
S3 Verify claims
       |
       v
S4 Prepare memory changes
       |
       v
S5 Commit memory changes
       |
       v
S6 Record worker notes
       |
       v
S7 Reconcile and report
       |
       v
      STOP
```

The graph is acyclic because every step depends only on an earlier step. No step needs a later result to begin.

However, an acyclic graph alone does not prove that the workflow is executable.

Before execution, S0 must confirm the required code, configuration, saved responses, state schema, and output directories are available. Replay mode must verify that the referenced JS3 Git objects exist. Live mode requires network permission and an available allow-listed endpoint.

The first state version must be initialized before concurrent memory writes begin. If a required input is missing, the run must refuse to proceed.

Greenhouse and Ashby watchers can execute source-specific processing in parallel, but they cannot overwrite each other's shared state. Each memory write must use the current version and reject stale versions.

A failure in one watcher must be reported independently. The other watcher's verified work can be retained, but the overall run must be marked partial rather than complete.

A Greenhouse per-ID endpoint is a conditional capability, not an assumption. It must be verified through a separately approved request before the agent relies on it.

## 4. Evidence on Every Dependency Edge

Every dependency must have a condition that another person can test.

| Edge | Required evidence condition |
|---|---|
| S0 → S1 | Configuration passes validation; required saved objects or approved endpoints are identified; allowed directories and limits are recorded |
| S1 → S2 | Every source record has a board identifier and posting identifier; saved input hashes match the referenced trace, or live responses have a recorded fetch time and source |
| S2 → S3 | Every produced claim identifies its posting, source field or evidence reference, and producing rule |
| S3 → S4 | Check results are recorded as passed, failed, or insufficient; unresolved claims are not silently treated as verified |
| S4 → S5 | The proposed change records the exact state version it was calculated against |
| S5 → S6 | A successful write records a new version and hash; a rejected write records the expected and actual versions without overwriting state |
| S6 → S7 | Worker notes contain worker ID, run ID, posting reference, source provenance and verification status |
| S7 → STOP | Summary counts reconcile with the trace, run status is recorded, and no unresolved failure is hidden |

These conditions are based on inspectable files, hashes, records and version numbers. Terms such as "looks correct" or "seems reliable" are not sufficient acceptance conditions.

If an edge condition fails, the next dependent step must stop or follow a documented refusal path.

## 5. Claims and Independent Checks

The JS4 agent may produce these claims:

- Whether a posting is currently retrievable through an independently verified source check.
- Whether a posting ID is new relative to stored memory.
- Whether its location or remote status satisfies the fictional persona's requirements.
- What the posting explicitly says about sponsorship or work authorization.
- Whether its role matches the existing filter.
- Whether its experience requirements match the early-career rules.

The full evidence matrix will be written separately.

I plan four checks:

| Check | What it catches | Why it can fail differently |
|---|---|---|
| Greenhouse per-ID liveness lookup | A stale listing or memory entry that is no longer retrievable | Makes a separate source request rather than trusting the collected board listing or memory |
| Sponsorship quote verification | Incorrect quotations, paraphrase drift or quotes attributed to the wrong posting | Checks independently normalized source text against the claimed quotation rather than accepting the filter's interpretation |
| Location recomputation | Incorrect location interpretation or source-field parsing | Uses an independently implemented path through alternative raw location fields rather than rerunning the original parser |
| Trace-summary reconciliation | Incorrect reported counts, including a planted 42-versus-99 error | Recomputes the count directly from the saved trace rather than trusting the summary writer |

The checks must not reuse the same implementation path where that would repeat the claim producer's error.

If the raw data does not support a claim, the output must say **insufficient evidence**, not verified.

For Ashby, an independent per-posting liveness endpoint has not been established. I will not claim independent Ashby liveness verification unless that capability is actually demonstrated.

The agent will make no pay claims. The evidence matrix will explicitly identify pay as out of scope.

## 6. Versioned Memory and Revision Rule

The existing JS3 `seen_ids.json` stores posting IDs, but it does not implement versioned writes or compare-and-swap protection. JS4 will introduce a new state format rather than overwrite JS3's state.

The new state will record:

- A monotonically increasing version number.
- A content hash.
- Posting identifiers and board names.
- First-seen and last-observed dates.
- Verification status and timestamps.
- Source references for remembered facts.
- Relevant run identifiers.

Each remembered fact must identify its source, such as a saved response reference, source field, collection time, or verification record.

Every proposed update will declare the version it expects.

A writer must acquire exclusive access to the state before checking the version and committing its update. If the current version differs from the expected version, the write must be rejected without modifying the existing state.

The rejection will be recorded with the expected version, actual version, worker and run identifier. The writer may reread and recompute a new proposal, but it must not blindly retry the same stale update.

Successful versions will be retained in an append-only history so the changes can be inspected.

A remembered posting's previous live status must not be assumed to remain true indefinitely.

For a posting that is no longer present, the agent should use precise wording such as:

**"Previously listed; not present in the latest board response. Current availability not verified."**

If a separate source lookup confirms non-retrievability, the report can additionally state:

**"Direct posting lookup returned HTTP 404 on [actual date]."**

Neither observation alone proves that the employer filled or permanently closed the position.

## 7. Two Workers and Shared Notes

I will use two watcher types:

**Greenhouse watcher:** Processes Databricks and Stripe.

**Ashby watcher:** Processes Plaid.

The watchers are independent at the source level because they read different companies and board APIs. They are not independent opinions about relevance because they share the same project design, normalization approach, and filtering rules.

Both watchers will write results into one shared notes file.

Each note will include the worker identifier, board, posting ID, run identifier, source reference, evidence status, and timestamp.

The notes will use structured JSON records rather than executable instructions. An exclusive lock or equivalent coordinated writing mechanism will prevent simultaneous writes from corrupting or overwriting the file.

Untrusted posting text will be stored only as data. It must not be interpreted as a new system instruction, command, policy, or authorization to change scoring rules.

A deliberately seeded posting containing instruction-like text will be used to test this boundary. The fixture will be clearly labelled as seeded.

## 8. Stop Conditions and Refusal Paths

A run stops normally after processing the approved boards, completing available checks, committing permitted state changes, reconciling counts, and writing the final report.

The agent must refuse or stop the affected operation if:

- The requested host is not allow-listed.
- The network request would exceed the configured budget.
- An input file is missing or its hash differs from the recorded value.
- A required state version is stale.
- The state schema is invalid.
- A verification check fails.
- A requested operation would write outside approved directories.
- A live liveness endpoint has not been verified.
- A source response cannot be interpreted safely.

The report will distinguish completed, partial, refused, and failed runs.

A failed check will not trigger an identical automatic retry. The agent must record the failure, preserve relevant evidence, and either stop the dependent action or use a separately justified recovery path.

For example, a stale memory write requires rereading the latest state and recomputing the proposed update. Repeating the old write without recomputation is prohibited.

## 9. Budgets and Authority

The following are proposed initial maximum limits, subject to approval before the first run:

| Resource | Proposed limit |
|---|---|
| Boards | 3 approved boards |
| Live HTTP requests | 15 total |
| Requests to either allowed host | 8 maximum |
| Direct posting-ID liveness requests | 5 maximum |
| Network timeout | 15 seconds per request |
| Overall live run | 120 seconds maximum |
| Automatic retries | No identical retry after a failed verification |
| Applications, emails, logins | 0 |

The agent may process all postings returned by the approved board requests, but must not expand its search to additional boards automatically.

Only I may approve changes to these budgets. Changes must be reflected in configuration and documented in a Git commit with a reason.

The agent, workers and AI development tools cannot independently increase the budgets.

## 10. Two-Day Evidence

I plan to use two distinct collection dates.

**Day 1: November 17, 2026**

Replay the real saved JS3 responses from the original commit, with their existing source hashes verified.

The evidence will be labelled:

"Replayed from saved responses originally collected November 17, 2026; replay executed on [actual date]."

The replay date and original source collection date must remain separate.

**Day 2: November 28, 2026**

With my approval, run a live collection against the approved public board endpoints. Record actual timestamps, results, request counts and failures.

If the live run cannot complete safely because of endpoint failures, permission concerns or budget limits, use the existing real November 19 collection as a fallback. Label both historical collections correctly and do not call this a new live run.

For the diff, compare stable posting IDs per board and report:

- IDs observed on both dates.
- IDs newly observed on the second date.
- IDs present only on the first date.
- Changes in relevant fields, where evidence supports comparison.

An ID missing from the later collection is not automatically closed.

For Greenhouse postings, I plan to test a per-ID lookup capability using one explicitly approved request. The endpoint format and behavior must be verified before it is used as a liveness check.

If it works, I will test selected previously listed postings that are absent from the later results.

If it does not work, I will record the limitation rather than claim that the liveness check succeeded. A separately labelled seeded case may demonstrate the memory behavior, but it must not be presented as proof of a real posting disappearing.

The required fresh-is-not-true demonstration will show a remembered live status being challenged by later evidence, with the evidence's actual strength clearly identified.

## 11. Seeded and Planted Evidence

Two deliberate test cases are planned.

**Planted incorrect claim**

A seeded run summary will report 99 records where its saved trace contains 42. The independent reconciliation check must detect and report the difference.

Both the planted summary and the trace must be preserved. The planted result must never be mixed with real collection statistics.

**Instruction-injection fixture**

A seeded job description will contain instruction-like language asking the agent to change its behavior.

The expected outcome is that the text is stored as untrusted posting data and does not change the filtering rules, permissions, memory policy or allowed operations.

Seeded and planted files will have explicit labels, including the fixture identifier and actual test date.

Reports must distinguish:

- Real historical source responses.
- Live source responses.
- Replays of historical responses.
- Seeded fixtures.
- Deliberately planted errors.

No simulated outcome will be described as a real external event.

## 12. Premortem Timing

A separate `PREMORTEM.md` will be written and committed before the deliberately triggered shared-memory failure.

My planned failure area is a lost update caused by two workers reading the same memory version and then attempting to write conflicting updates.

The premortem will predict the failure mechanism, expected consequence and intended protection before the test is run.

After committing the premortem, I will trigger the conflict using a deterministic interleaving test. The test should demonstrate whether version checking prevents one worker from silently overwriting the other's update.

The actual result will be documented separately after execution.

The commit history must show that the premortem existed before the failure experiment.

I will not write a prediction after observing the failure and present it as a premortem.

## 13. Privacy, Security, and Terms of Use

I will use only fictional persona information in the public JS4 project.

My real résumé, personal contacts, credentials, private tracker and conversation transcripts will remain outside the submission.

The JS3 inspection found that some raw saved responses contain recruiter-related information and an email-like contact string. I will avoid duplicating those full raw responses into JS4. Instead, the replay can reference existing JS3 Git objects by commit and path, with their hashes verified.

Only the minimal derived evidence needed to explain JS4 results should be included in the new submission.

Allowed public hosts:

- `boards-api.greenhouse.io`
- `api.ashbyhq.com`

Network access will use HTTPS GET requests only, with exact host checks, request limits and no login.

The implementation must respect the relevant sites' published terms of use. Public accessibility by itself is not proof that an endpoint may be used without restrictions.

Posting descriptions are untrusted data and must never authorize additional network requests, commands or changes to agent policy.

Before submission, I will inspect the new files for private paths, credentials, personal contact details and unnecessary copied source content.

## 14. Reuse and Provenance

The JS4 project will reuse only the JS3 components needed for this assignment.

The initial candidates are:

- `loop.py` — collection workflow and injectable transport.
- `parsers.py` — Greenhouse and Ashby parsing.
- `job_filter.py` — version 1.1 filtering.
- `descriptions.py` and `rule.py` — supporting filtering logic.
- `persona.py` and the fictional persona configuration.
- `policy.py` — security and write rules, requiring modifications.
- Relevant existing test patterns.

The final list will be recorded after checking which dependencies are actually needed.

For each reused file, the project will distinguish:

- Copied unchanged.
- Copied and modified.
- Newly written for JS4.

The provenance record will include the original JS3 commit, source path, original file SHA-256, destination path, resulting SHA-256 and any modifications.

A copied-then-modified file will retain both hashes and a description of the changes.

The submitted JS3 folder and original evidence will remain unchanged.

The JS4 README will name the source project, programming language, dependencies, exact commands, tests and executed runs.

## 15. Review and Change Log

*Intentionally left unfilled in Version 1. The formal review will take place after this initial version is preserved.*

### Reviewer

### Review date

### Criticisms and counterexamples

### My evaluation of each criticism

### Counterexample that changed the plan

### Changes made in Version 2

### Later findings that reopened a decision

If no genuine counterexample is discovered during the first review, I will not invent one. I will continue reviewing or seek an additional reviewer.

Later changes will be logged with their actual dates and reasons rather than rewriting the earlier plan to make it appear that I anticipated them.

## 16. Open Questions and Assumptions

The following questions remain unresolved before implementation:

1. **Greenhouse per-ID lookup:** I have not yet verified that an approved endpoint supports the independent liveness check. The agent must not rely on it before testing its behavior.

2. **Ashby liveness:** No independent per-posting endpoint has been established. I may need to leave this claim unchecked.

3. **Historical replay:** The JS4 code must be able to read the exact saved JS3 Git objects and verify their hashes without duplicating full raw responses.

4. **Memory coordination:** The locking and versioning design must be tested to demonstrate that concurrent workers cannot silently overwrite each other's updates.

5. **Independent checking:** Separate checks must actually use different source paths or algorithms. Merely wrapping the existing JS3 parser in another function will not be enough.

6. **Terms of use:** Live collection must not proceed until the applicable endpoint restrictions have been checked.

7. **Source disappearance:** November 17 and November 19 ID differences provide candidates, but absence alone does not establish that a job is closed or unavailable.

8. **Fallback evidence:** A historical two-date comparison or a seeded demonstration must be labelled accurately and cannot be presented as a fresh live observation.

9. **Privacy:** Derived output must be checked to ensure it does not unintentionally reproduce unnecessary personal details from source descriptions.

10. **Environment and dependencies:** The final implementation must remain compatible with the available Python environment and course repository conventions.

Any finding that changes one of these assumptions must be recorded with the affected step, evidence, revised decision and date.

---

**End of PLAN.md — Version 1 draft**

This document describes intended behavior and planned tests. It does not claim that JS4 has been implemented, that an endpoint has been verified, or that the planned evidence checks and failure experiments have already run.