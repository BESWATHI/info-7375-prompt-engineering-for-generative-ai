# PROJECT-BRIEF — BiteCheck
**Omkar Salian · INFO 7375 Fall 2026 · updated 2026-10-13** · Target role: new-grad Software / AI Engineer · Stack: TypeScript, Express, Jest + Supertest, Claude Code, GitHub Actions

**1. What is it?** BiteCheck will be a Claude Code workflow that writes API tests for my InstaLoan loan demo (Express + TypeScript, synthetic data, no tests today) and checks that each test **fails when a business rule is broken on purpose**. When it is done, it will be a public GitHub repo containing a test-writing prompt contract, a hand-written bug list ("mutants"), a runner, a one-page report and an evaluation log.

**2. Why would anyone care?** It tells an engineer reviewing a pull request full of AI-written API tests which of those tests would actually catch a broken business rule. *Postbot* and *Schemathesis* (docs read 2026-10-12) generate test scripts and check an API against its schema. Neither one checks business rules. *StrykerJS* I ran on my loan rules through Claude Code on 2026-10-13 (`evidence/stryker/`). It made 92 mutants, but **none changed the ₹15,000 limit**, and its only stage-order mutant deletes every guard at once. BiteCheck adds mutants that each break one business rule and are tied to a rule ID.

**3. Who opens it?** A hiring manager or engineer screening a new-grad SWE or AI engineer. In 60 seconds they run `npm run bitecheck` and read one page: did the tests pass on the real API, which mutants were caught or survived, and which tests Claude got wrong.

**4. What does it prove?** Prompt contracts (each test cites a rule ID), source grounding (no rule, no test), a bounded agent loop (Claude edits tests, never the API, with a fixed number of tries) and evaluation (a mutation score plus a mistake log). The evidence will be the repo, its CI runs and the log. It will not show that it works on every API, because it is measured on one.

**5. In / out / first.** *In:* one API, about 20 mutants, a runner, a report and a log. *Out:* not a general tool, and it never fixes application code. *First:* one mutant (minimum income 15,000 → 1,500) run in GitHub Actions. You'd know it ran from a committed CI report showing the real API passing and the mutant caught.

**6. What could sink it?** I write the mutants, so I could make them too easy. I'll commit the mutant list before Claude writes any test, include hard boundary cases, and report every survivor.

**7. Why this project?** A mix, mostly learning. *Have (private):* API testing and CI gates at my last job, and TypeScript/Express (the InstaLoan API, built with Claude's help). *Have (public):* a Claude workflow with run logs, in my Reallocation Engine PR ([nikbearbrown/the-reallocation-engine#37](https://github.com/nikbearbrown/the-reallocation-engine/pull/37)). *New:* mutation testing and evaluation design. How well Claude's tests will do, I don't know yet. Finding out is the point.

**Exists today (2026-10-13)**
- InstaLoan API (local, private), run 2026-10-12 on synthetic applicants: ₹14,999 rejected, ₹15,000 offered, out-of-order payout refused with HTTP 409 (`evidence/los_smoke_test.txt`)
- A StrykerJS run on its rules: 92 mutants, none on the 15,000 limit (`evidence/stryker/`)
- This brief, the beat sheet and the film

**Will exist**
- The prompt contract, the rules file and the mutant list (committed first)
- Claude-written tests, the runner, the report, the log and CI
- The public repository
