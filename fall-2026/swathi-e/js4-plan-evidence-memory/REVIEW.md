# REVIEW — JS4 PLAN.md Version 1

**Reviewed:** `PLAN.md` Version 1, commit `9d81c4b3`  
**Reviewer:** Claude Chat (first reviewer)  
**Review date:** November 27, 2026  
**Decisions by:** Swathi Baba Eswarappa, November 27, 2026

The review below is reproduced as Claude Chat gave it. My decision on each finding follows it, in my own words. I verified each criticism myself before deciding.

---

## Part 1 — The review (Claude Chat, 2026-11-27)

### R1. Counterexample: a failed or empty board fetch would look like "every posting disappeared" (high)

**Scenario:** On Day 2, the Ashby request times out, returns an error, or returns HTTP 200 with an empty list (for example, a changed board slug). Greenhouse succeeds. S5 commits the new state, and the S7 diff reports all 142 Plaid postings as "present only on the first date". Memory then marks them with the §6 wording, "previously listed; not present in the latest board response", 142 times, and every one is false.

**Where v1 allows it:** §3 says a failed watcher makes the run "partial", but §6 and §10 compute absence over all remembered postings, with no condition that that board's fetch was complete. The S1→S2 edge checks record IDs, not completeness, and a 200 with zero postings passes every v1 condition.

**Suggested change:** add per-board completeness evidence (status 200, parse succeeded, posting count > 0, response hash recorded). Compute absence only for boards whose fetch was complete. For any other board, record "not observed this run" and leave its memory unchanged. Decide whether a large drop in count (e.g. > 50%) is treated as suspect rather than real absence.

### R2. A 404 from the per-ID lookup isn't trustworthy without a positive control (high)

A wrong URL template, a board-slug mistake, or an outage also returns 404 or an error, and that would falsely "confirm" postings are gone.

**Suggested change:** before trusting any 404, the same per-ID request must return 200 for a posting present in the same day's listing. That is the positive control. Record both results. And since it is the same host and API family, say honestly that the check is independent of the listing, not of Greenhouse itself.

### R3. The budget arithmetic doesn't fit (medium)

On the Greenhouse host on Day 2: 2 list requests + 1 endpoint verification + 1 positive control (R2) + up to 5 per-ID lookups = 9, but v1 caps each host at 8. Also, JS3 had one network retry, while v1 says "no identical retry", which mixes up retrying a failed check with retrying a transient network error.

**Suggested change:** rebalance the limits, and define network-retry and check-failure behaviour separately.

### R4. "Stop if a verification check fails" conflicts with the plan's own tests (medium)

§8 lists "a verification check fails" as a refusal condition. But the planted 42-vs-99 error must fail, and sponsorship-quote mismatches are expected outcomes. Stopping the run would prevent the evidence needed.

**Suggested change:** separate integrity failures (hash mismatch, stale write, host not on the allow-list, invalid schema), which stop the run, from claim-check failures, which mark the claim failed or insufficient, keep it out of "verified" memory, and let the run continue.

### R5. The reconciliation check may not be independent of the summary (medium)

§5 recomputes counts "directly from the saved trace". If the trace and the summary are both written by the same loop from the same in-memory counter, one bug corrupts both, and they still agree.

**Suggested change:** recompute counts from the raw response bytes (number of posting IDs in each saved response file), not from counts the trace recorded.

### R6. The quote check needs a defined "match" rule (low–medium)

The quoted text was produced through JS3's `html_to_text`. A separately written normalizer may legitimately differ on whitespace, entities, or line breaks, giving false "mismatch" results.

**Suggested change:** define what counts as a match in advance (e.g. whitespace-collapsed, entity-unescaped substring), and report three outcomes: exact, normalized match, absent.

### R7. The graph doesn't show the parallel watchers (low)

§3's graph is a single line, but the text runs two watchers in parallel with separate failure handling.

**Suggested change:** draw S1 as two branches (Greenhouse, Ashby) that merge before S4 and S5, with per-board evidence on each branch. That also makes R1's per-board completeness visible.

### R8. The terms-of-use gate isn't a step (low)

§13 and §16 say live collection waits for a terms-of-use check, but no step or edge enforces it.

**Suggested change:** make it a recorded precondition of S0 for live mode, with date and source.

**Reviewer's note on the counterexample:** R1 was proposed as the counterexample that changes the plan, with the decision left to the author.

---

## Part 2 — My decisions (Swathi Baba Eswarappa, 2026-11-27)

**R1 — ACCEPT.** This is a genuine counterexample that changes my plan. If a board fetch fails or unexpectedly returns zero postings, my original design could incorrectly interpret all remembered postings as disappeared. I want per-board completeness evidence before computing absence or changing remembered availability. Treat a large count drop, such as more than 50%, as suspect and requiring investigation rather than automatically proving disappearance.

**R2 — ACCEPT.** Require a successful positive-control per-ID lookup for a posting present in the same day's Greenhouse listing before relying on a 404 for a missing posting. Explain that this checks independently of the listing but not independently of Greenhouse itself.

**R3 — ACCEPT.** I verified the arithmetic: 2 listing requests + 1 endpoint verification + 1 positive control + 5 per-ID lookups = 9, exceeding the host budget of 8. I prefer reducing optional lookups instead of raising the budget. Endpoint verification and the positive control should be one request if possible. Distinguish transient network retries from failed evidence checks.

**R4 — ACCEPT.** Separate integrity failures that stop a dependent operation from claim-check failures that are recorded as failed or insufficient evidence. A planted error must be detected without invalidating the entire test demonstration.

**R5 — ACCEPT.** Recompute posting counts independently from the saved raw response records rather than reusing trace or summary counters.

**R6 — ACCEPT.** Define exact match, normalized match and absent outcomes using an explicitly documented normalization rule.

**R7 — ACCEPT.** Revise the graph to show two board-specific watcher branches, per-board evidence gates and coordinated memory updates.

**R8 — ACCEPT.** Add a documented terms-of-use and endpoint-permission gate to S0 before live collection.

**Counterexample:** I accept R1 as the genuine review counterexample that changed the plan.

---

## Part 3 — How the decisions were applied

- On R3's question, endpoint verification and the positive control were combined into one request per Greenhouse board. The positive control is needed per board because the board name is part of the URL. The final Greenhouse budget is 8: 2 listings + 2 positive controls + up to 4 per-ID lookups.
- The changes are in `PLAN.md` Version 2, section 15 summarises them, and Version 1 is preserved in Git history at commit `9d81c4b3`.
- Version 2 wording was drafted by Claude Chat from my decisions above. I reviewed and approved it before committing.
