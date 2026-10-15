# Source Check for Support AI — Project Brief

**Mayank B. · INFO 7375 Final Project · Target role: AI automation engineer · Brief written 2026-10-14**
**Stack:** n8n (workflow and routing) · Python (the checker and its tests) · Claude (claim extraction under a prompt contract)

**Status:** this is a pitch. Nothing in this project has been built yet. Every sentence about the tool uses "will".

## 1. What is it?
Source Check for Support AI will check a support chatbot's policy answer against the company's current policy documents before the answer reaches the customer, and hold it for a human when it can't find support.
When it is done, it will be a public GitHub repository containing:
- an importable n8n workflow
- a Python checker with offline tests
- a synthetic help center for a fictional company
- an evaluation log
- a README with a one-command demo

## 2. Why would anyone care?
It will stop a support bot from promising a refund, fee or eligibility rule that the company's current policy doesn't contain. This happens in practice. In *Moffatt v. Air Canada* (BC Civil Resolution Tribunal, February 2024), the airline's chatbot told a customer he could claim a bereavement fare after travelling, but the actual policy required the request before travel. The tribunal held Air Canada responsible for what its chatbot said.

Alternatives I looked at, on 2026-10-14:
- **Intercom Fin.** Its public page says it works from your policies, has "a full testing suite to run simulations, regression testing", and hands off to humans.
- **Zendesk AI agents.** It answers from help-center articles and hands off to a live agent when no article matches. That description comes from third-party guides; I did not verify it in Zendesk's own documentation.
- **Manual review.** A support lead spot-checks bot transcripts, after the answers have already been sent.

What I did not find on those public pages: a check of each policy answer, at send time, against the current dated version of the policy. Source Check will hold the answer for approval when the source is missing, outdated or contradicted, and log which policy version each answer relied on. It will be vendor-neutral, sitting between any bot and the customer.

## 3. Who opens it, and what do they do in the first sixty seconds?
The reader is a hiring manager or engineer hiring an AI automation engineer. In the first sixty seconds they will:
1. Open the README and see three example decisions.
2. Run one command.
3. Watch an answer that relies on an outdated refund policy get **HELD**, with the reason and the policy line it contradicts.

The intended end user is a support team lead whose AI agent answers policy questions.

## 4. What does it prove about me?
That I can build an automation that knows when **not** to act. Course skills, and the planned evidence for each:
- **Prompt contracts:** Claude must return each claim as structured JSON mapped to a policy section, and the reply is validated before it is used.
- **Source grounding:** every claim is tied to a dated document.
- **Verification:** deterministic checks for numbers, dates and conditions. The model only extracts claims; it does not judge them.
- **Human approval gates:** a HOLD queue in Slack through n8n.
- **Evaluation:** a labelled synthetic test set of correct, outdated and invented answers, with the miss rate measured and reported.

A reviewer could fairly conclude that I design gates and measure them. They could not conclude that it is production-ready, and I will not report any accuracy figure until it has been measured.

## 5. What is in, what is out, what comes first?
- **In:** policy answers (refunds, fees, eligibility) for one fictional company's synthetic help center, in English.
- **Out:** it will **not** write answers or replace the support bot. It only checks answers that another bot drafted.
- **First:** the Python checker plus one test, the Air Canada-shaped case. The answer says "claim after travel"; the policy says "before travel"; the result must be HOLD. Someone will know it ran because `pytest` passes and the run log shows HOLD with the cited policy line.

## 6. What could sink it?
**Missed conditions.** The most dangerous error is a dropped timing or condition word ("after" instead of "before", "within 90 days"), which is exactly the shape of the Air Canada error. If Claude's claim extraction loses the condition, the checker could PASS a wrong answer.
What I will do about it:
- run deterministic checks on numbers, dates and condition words
- default to HOLD whenever extraction is uncertain
- seed the evaluation set with condition-flip cases
- report the miss rate honestly

A second risk is too many HOLDs, so a support team learns to ignore them. I will measure the hold rate as well.

## 7. Why this project?
It is a mix of showing off and learning.
- **Skills I already have, with evidence:**
  - n8n workflows with Claude: my public repos *AI-Marketing-Ad-Review* (Claude reviews ad copy, with a rule-based fallback, routed to HubSpot and Slack) and *Madison-Project* (n8n + Claude Haiku routing to a CRM, INFO7375 Assignment 4)
  - n8n data pipelines: *Applications-Made-Easy* and *One-Pipe*
  - Python: my Week 1 film's evidence code in the course repo
- **New to me:**
  - building and labelling an evaluation set, and measuring misses
  - validating a prompt contract
  - designing a hold-for-approval gate that records the policy version behind every decision

I picked it because Week 1 taught me that a fluent, confident output is not a checked one, and the Air Canada case shows what that costs a real company.

---
**Exists today (2026-10-14):** this brief · the research notes and sources behind sections 2 and 6 · this pitch film · my earlier public repos listed in section 7 (evidence of skills, not of this project).

**Will exist:** the n8n workflow · the Python checker and its tests · the synthetic help center · the labelled evaluation set and log · the demo command · the README.
