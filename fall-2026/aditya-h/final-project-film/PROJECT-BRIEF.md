# PROJECT-BRIEF: AI Product Failure Lab

Aditya Hasija · INFO7375 · Final project pitch · Draft 1, 2026-10-14
Target role: **AI Product Manager / Product Manager**

## 1. What is it?
A tool that runs a pre-mortem on a product idea and labels every claim as either *sourced* or *a guess*.
When it's done, it will be a **GitHub repository** containing a small web app and a command-line runner. You give it an idea and a pack
of public source documents. Four Claude agents (orchestrator, market, customer, risk) and an evaluator return a report
with the top five failure risks, an evidence label on each claim, and three validation experiments. The repository will also hold
a **test set** of synthetic ideas and an **evaluation log** that scores the tool against a plain chat assistant.

## 2. Why would anyone care?
It's for a PM holding a raw idea before there is a team or a budget. They need to know which risks rest on evidence and which rest on guesses.
- **Plain chat assistants (tested 2026-10-14):** both gave sharp pre-mortems and both caught a fake statistic we planted.
  Plain Claude (3 runs) cited **zero sources** while stating claims like "conversion typically happens at low single-digit
  rates" as facts, and its format changed every run. Logged-out ChatGPT (1 run) did better: it attached web sources to 2 paragraphs and
  labeled its thresholds "not benchmarks". Most of its claims were still unlabeled, and nothing checked the citations.
- **Atlassian's pre-mortem play:** it needs 3–11 people and about 70 minutes, it targets delivery risk, and nothing checks the evidence.
- **The difference:** every factual claim will either point to a passage that really exists in the source pack (checked by
  code, not by the model) or be labeled *hypothesis*. The report format is fixed, so runs and ideas can be compared.

## 3. Who opens it, and what do they do?
A **hiring manager for an AI PM role**. In the first 60 seconds they will read the README, open one real sample
report, and see the evaluation table: the Failure Lab vs. plain chat on the same test ideas, including where the Failure Lab lost.
The end user is a PM or founder who pastes in an idea and reads the report in about five minutes.

## 4. What does it prove about me?
That I can write a spec a machine follows and then measure whether it did. The course skills involved are **prompt contracts** (one
versioned contract per agent with a Zod output schema), **agent loops** (an orchestrator plus an evaluator allowed one bounded retry),
**source grounding** (citation checks against the pack), **verification and evaluation** (a planted-flaw test set
scored against a baseline). The evidence will be versioned prompts, saved run logs, the evaluation table, and a FAILURES.md listing
where it was wrong. A reviewer could fairly conclude I can scope an AI feature and evaluate it honestly. They could **not** conclude I'm a
production ML engineer.

## 5. What's in, what's out, what comes first?
- **In:** 4 agents + evaluator, evidence labels, citation check, 8–10 synthetic test ideas with source packs, a baseline comparison, a simple UI.
- **Out (deliberately):** **no "chance of success" score.** It will never turn guesses into a probability. Also out: live web search,
  accounts, financial models, PDF export.
- **First to run:** the Risk agent plus the evaluator on one test idea, from the command line. *How you'd know it ran:* a JSON run log saved
  in `runs/`, validated against the schema, with the evaluator's flags in it.
- **Build constraint:** the whole thing will be built with Claude Code from my prompts, within two weeks. The prompts will be logged
  in the repo.

## 6. What could sink it?
**The evaluator rubber-stamps.** It's the same model grading its own team, so it may wave weak claims through. Plain Claude already
catches *obvious* planted flaws, so the test set will need subtler ones, such as a price that contradicts the audience or a plausible
number with no source. *What I'll do:* measure the catch rate. If it's low, I'll move checks out of the model and into code
(does the cited quote exist in the pack? does the claim contain a number with no citation?) and report the result either way.

## 7. Why this project?
It's a mix of both reasons.
- **Skills I already have:** product requirements and user flows, competitive analysis, risk management, and Next.js/React. Evidence: the WorkShip
  requirements and wireframes (team of five), the SkillPort and portfolio repositories on GitHub (AdityaHasija37).
- **New to me:** multi-agent orchestration, building an evaluation harness, schema-validated LLM output, and grounding checks.
  I picked it to learn how to *measure* an AI feature, which is the part of AI product work I haven't done yet.

---
**Exists today**
- The idea and a blueprint doc (written with ChatGPT from my notes, 2026-10-14)
- A baseline test of one synthetic idea: 3 plain-Claude runs and 1 logged-out ChatGPT run, with the prompt, outputs and a screenshot (`research/`, 2026-10-14)
- Notes on the Atlassian pre-mortem play (`research/alternatives.md`)

**Will exist**
- Agent prompt contracts and Zod schemas
- The orchestrator, evaluator and retry loop
- The citation checker
- 8–10 synthetic test ideas with planted flaws and source packs
- The evaluation log vs. baseline
- FAILURES.md
- The web UI
- The README with a sample report
