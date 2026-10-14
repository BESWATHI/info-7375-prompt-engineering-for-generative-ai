# FACTCHECK — bitecheck-pitch

Status: every row was checked by Claude Code on 2026-10-12 and updated 2026-10-13 against the evidence named. Rows 4, 23 and 24 depended on facts only Omkar could confirm; he confirmed them in chat on 2026-10-13.

Evidence: `evidence/los_smoke_test.txt` (a live run of the local InstaLoan backend, 2026-10-12 11:48 EDT, synthetic applicant). The rule values were read from `LOS/backend/src/constants.ts` (`MIN_MONTHLY_INCOME: 15000`, `STAGE_PRECONDITION`). Tool descriptions come from the vendors' docs and reviews read on 2026-10-12 (URLs in SOURCES.md). Stryker figures come from `evidence/stryker/` (StrykerJS 8.7.1, run 2026-10-13). Pronunciation was checked with Whisper-tiny (`evidence/pronunciation_check.txt`).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Claude can draft a whole suite of API tests that all come back green | EXEMPT | Framing: a possibility, not a measured result. No number is claimed. | Was "in minutes", which is unmeasured, so it was cut |
| 1b | B00 | BiteCheck tells an engineer reviewing AI-written tests which ones would catch a broken business rule | PASS (future) | Design goal, PROJECT-BRIEF §2; tagged PROPOSED | — |
| 2 | B00 | A green test only means something if it would turn red when the code is wrong | PASS | Definition of mutation testing (StrykerJS docs) | — |
| 3 | B01 | BiteCheck *will be* a public repo with a prompt, a bug list, a runner and a report | PASS (future) | PROJECT-BRIEF §1, "Will exist" list; tagged PROPOSED on screen | — |
| 4 | B02 | A loan application API "I built earlier with Claude's help" | PASS | `~/Desktop/LOS` exists. Omkar confirmed in chat on 2026-10-13: "Yes" (built with Claude's help). | — |
| 5 | B02 | It uses made-up applicants and mock vendors | PASS | LOS README ("mock adapters"); smoke test used a synthetic applicant | — |
| 6 | B02 | It checks a minimum income and the order of steps | PASS | `constants.ts` RULES.MIN_MONTHLY_INCOME = 15000; STAGE_PRECONDITION map | — |
| 7 | B03 | On 2026-10-12, income ₹14,999 was rejected | PASS | `los_smoke_test.txt`: REJECTED, "Monthly income below minimum ₹15000" | — |
| 7a | B03 | "On October twelfth, I ran it on made-up applicants with Claude Code" | PASS | Claude Code ran the smoke test during the build Omkar asked for (`evidence/los_smoke_test.txt`). | Was "I ran it", which wrongly suggested Omkar ran it himself, so "with Claude Code" was added on 2026-10-14 |
| 8 | B03 | ₹15,000 got an offer | PASS | `los_smoke_test.txt`: status OFFER_GENERATED | — |
| 9 | B03 | Paying out before the earlier steps was refused (409) | PASS | `los_smoke_test.txt`: HTTP 409, "expected 'ESIGN_COMPLETED'" | — |
| 10 | B03 | It has no tests yet | PASS | `find LOS -name '*.test.*' -o -name '*.spec.*'` (excluding node_modules) returned nothing on 2026-10-12 | — |
| 11 | B04 | Example mutant: minimum income 15,000 → 1,500 | PASS (future) | Hypothetical example; tagged PROPOSED. No mutant exists yet. | — |
| 12 | B05 | A test failing on correct code means Claude got it wrong; these go into a log | PASS (future) | Design statement, PROJECT-BRIEF §4 | — |
| 13 | B06 | From their docs, Postbot generates test scripts | PASS | Postman Postbot page and reviews (read 2026-10-12) | — |
| 14 | B06 | Schemathesis checks an API against its schema | PASS | Schemathesis docs (read 2026-10-12) | — |
| 15 | B06 | On Oct 13, I ran Stryker on my loan rules with Claude Code | PASS | `evidence/stryker/stryker_run.log`, `stryker_summary.txt`. Claude Code ran it on a scratch copy at Omkar's request. Omkar can re-run it with the command in BUILD-PROMPT §4. | Was "I ran Stryker myself", which was untrue, so it was changed |
| 16 | B06 | It made 92 mutants (on-screen hero "92") | PASS | `stryker_summary.txt`: TOTAL mutants: 92 (bre.ts 90, constants.ts 2) | — |
| 17 | B06 | None changed the 15,000 limit (on screen "15,000 changed: 0") | PASS | `stryker_summary.txt`: numeric-literal mutants 0; no mutant on constants.ts L46 `MIN_MONTHLY_INCOME: 15000` | — |
| 17b | B06 | Its one step-order mutant deletes every guard at once | PASS | `stryker_summary.txt`: the only mutant on STAGE_PRECONDITION is ObjectLiteral → `{}` (constants.ts L33). routes.ts was not in the mutate set, so this is scoped to the rules files. | Scope noted |
| 17c | B06 | BiteCheck adds those business-rule bugs, one at a time | PASS (future) | PROJECT-BRIEF §2/§5; tagged on screen | — |
| 18 | B07 | The first-minute flow (one command, one page) | PASS (future) | Design; tagged PROPOSED; `npm run bitecheck` does not exist yet | — |
| 19 | B08–B09 | Prompt contract, source grounding, bounded agent loop, evaluation | PASS (future) | PROJECT-BRIEF §4; course topics | — |
| 20 | B09 | "It won't prove this works on every API" | PASS | Scope limit, PROJECT-BRIEF §4–5 | — |
| 21 | B10 | Out: not a general tool, never fixes app code. First: the income rule in GitHub Actions | PASS (future) | PROJECT-BRIEF §5 | — |
| 22 | B11 | Risk: I write the bugs. Mitigation: commit the bug list first, report survivors | PASS (future) | PROJECT-BRIEF §6 | — |
| 23 | B12 | I've done API testing and CI gates at my last job; that work is private | PASS | Checked against Omkar's résumé (private; not in this folder): automated Postman API test collections and GitHub Actions CI with staged quality gates. Omkar confirmed on 2026-10-13: "i have already worked on api testing". | — |
| 23b | B12 | My public Reallocation Engine pull request, a Claude workflow with a run log | PASS | nikbearbrown/the-reallocation-engine#37 (opened 2026-10-03; includes `logs/runs/2026fa-o7580-1.md`) | — |
| 24 | B12 | Mutation testing and evaluation design are new to me | PASS | Omkar confirmed in chat on 2026-10-13: "Yes". | — |
| 25 | B13 | Exists: the loan API (ran), the brief, the film. Everything else will exist. | PASS | PROJECT-BRIEF "Exists today" / "Will exist" | — |
