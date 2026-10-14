# FACTCHECK.md — agent-reliability-audit-pitch

| # | Beat | Claim | Verdict | Source | Fix |
|---|------|-------|---------|--------|-----|
| 1 | BIDEA | "Nothing in this film has been built yet" | PASS | Self-attested: at time of writing, no code under `agent-reliability-audit` exists; confirmed by the state of this submission folder | — |
| 2 | BDEFS | pass@k = succeeded at least once in k tries; pass^k = succeeded every time | PASS | Standard definitions used throughout the cited methodology source (see #3) and general agent-evaluation literature | — |
| 3 | BDEFS | "tool contract: the deal a tool makes about what it will return" | PASS | My own working definition for this project, stated as a definition, not an external citation | — |
| 4 | B02 | "an agent can look ninety-seven percent successful under pass-at-three" | PASS | Quoted directly from "Building an AI Agent Evaluation Pipeline: 2026 Methodology," digitalapplied.com, published 2026-06-02 — the article's own stat block states "pass@3 vs pass^3 / 97% / vs ~34% for the same agent / −63 pp gap" | — |
| 5 | B03 | "the all-three-times number for that same agent at around thirty-four percent — a sixty-three point gap" | PASS | Same source as #4, same stat block, quoted directly | — |
| 6 | B03 | Implicit per-trial success rate (~70%) | **CORRECTED** | An earlier draft stated this as if the source itself reported a 70%-per-trial figure. The source reports only the two headline percentages (97%, ~34%); the 70% figure is my own back-calculation from those two numbers (mathematically consistent: 0.7³≈34%, 1−0.3³≈97%), not something the source states. Removed from the final narration entirely — see `SOURCES.md` | Narration in `make_sheet.py` rewritten to cite only the two directly-quoted figures |
| 7 | B04–B05 | Description of fault-injection testing (malformed data, stale page, timeout; safe-refuse vs. silent-pass-through) | EXEMPT | This describes planned future work ("I'll deliberately feed it..."), not a claim about something that has already happened | — |
| 8 | B06 | Scope claims: "one real tool, ten real questions, one documentation source" | EXEMPT | Stated as a plan ("I'm keeping this small on purpose"), not a completed fact | — |
| 9 | B07 | "a real pull request I have open right now, I deliberately tried to break a different scoring system and found a real flaw in it" | PASS | `nikbearbrown/the-reallocation-engine` PR #3, public and open as of this writing; the described break-attempt (a constructed 0-approvals/2-denials company scoring 0.699 and outranking Microsoft) is documented in that PR's own `WORKED-RUN.md` and attestation | — |
| 10 | BHTF | The "Your Turn" prompt itself | EXEMPT | A suggested prompt for the viewer to try, not a factual claim | — |
| 11 | BCLOSE | "the repo link is in the description" | EXEMPT | A pointer to where the (not-yet-public) repo will be linked once created; not a claim being made now | — |

**Summary:** 2 numeric claims verified directly against the source's own published stat block (not a search snippet); one earlier inaccuracy (an inferred per-trial rate attributed to the source) caught and corrected before the film was built; all forward-looking "will" claims marked EXEMPT rather than fact-checked as if they were completed work.
