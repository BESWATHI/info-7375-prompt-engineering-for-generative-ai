# PROJECT-BRIEF — Co-op Sponsor Check

Arundhati Kandelkar · INFO 7375 Final Project pitch · drafted 2026-10-10

> **Status:** final for submission, 2026-10-12. §2 records a search I asked Claude to run; §7 is my own choices. Claude drafted the rest from my
> existing repo; every past-tense claim below is checked against `evidence/recipe-rerun-2026-10-10.txt`.

## 1. What is it?

**A command-line tool that tells an international student whether a company has a public record of
sponsoring *software* jobs — and says "unknown" instead of "no" when the record is missing.**

When it is done, it will be a public GitHub repository (Python, inside my fork of the Reallocation Engine)
containing: the checker; a second public data source to fill the gaps in the first; an evaluation set of
25 real companies I check by hand; an evaluation log; and a written failure analysis.

## 2. Why would anyone care?

It saves an F-1 master's student, choosing a co-op, from treating "this company isn't in my spreadsheet" as
"this company won't sponsor me." It answers one question per company — *has this employer sponsored the kind
of work I would do?* — and labels every answer as a record, a judgment, or the student's own input.

Alternative looked at: **the official USCIS H-1B Employer Data Hub** (searched 2026-10-12 by Claude in its
browser on my instruction; record in `evidence/uscis-hub-search-2026-10-12.md`).

- *What it does well:* it is the government's own record — first petition decisions FY2009–FY2026 Q3, every
  employer, free, downloadable as Excel/CSV, and it **does list JPMorgan Chase**, which my current dataset lacks.
- *What it does not do:* its search filters are fiscal year, employer name, industry code, city, state and ZIP —
  **no job title**, so it cannot say whether a company sponsored *software* work. It is searched one employer at a
  time (the full download exists, but then the student does the join). And name search is loose: typing "Mellon"
  for FY2026 listed **three BNY entities and Carnegie Mellon University**.
- *What mine will do that it does not:* take a whole list of companies, check for **software titles**, check the
  **co-op dates against two graduation scenarios**, keep **"not in data" separate from "zero"**, and refuse
  part-of-a-name matches (a test for exactly the "MELLON" trap exists today: `test_substring_does_not_match`).
- *Honest note:* the hub is the better source of truth; my tool's value is the question it asks, not better data.
  The hub is the likeliest "second public data source" in §Will exist.

## 3. Who opens it, and what do they do in the first sixty seconds?

**Target role:** software developer / full-stack developer (co-op now, full-time after).
**Reader:** a hiring manager or engineer at a bank or fintech. In sixty seconds they will read the README's
first screen, run one command, and see a report where JPMorgan Chase comes back *not in dataset → unknown*
rather than *0*, next to an evaluation table showing where the tool was right and wrong.

## 4. What does it prove about me?

- **Verification:** every value in the report is labelled `record` / `model-judgment` / `your-input`
  (exists today, tested by `test_every_scorer_term_is_labeled`).
- **Evaluation:** a hand-checked set of 25 companies with match / mismatch / needs-a-human counts (will exist).
- **Source grounding:** every "sponsors software" answer will cite the data row it came from.
- **Tests:** 17 unit tests pass today; the evaluation adds a check that the tool's answers match my hand checks.

A reviewer could fairly conclude I can build a small, tested data tool and say honestly where it fails. They
could **not** conclude it is accurate for every company — the evaluation will report exactly where it is not.

## 5. What is in, what is out, what comes first?

- **Out:** it will not give immigration or legal advice, and will not predict whether anyone gets an H-1B.
- **In:** sponsorship *history* for software titles, from public government-derived data, with labels.
- **First:** the 25-company evaluation set. *How you'll know it ran:* a table of tool answer vs. hand check per
  company, with totals, committed with its date. **The first 6 rows ran on 2026-10-12** (`evidence/`).

## 6. What could sink it?

**Company names don't match across sources.** "BNY Mellon", "The Bank of New York Mellon" and
"BNY Mellon NA" can be the same employer or different ones. A bad match silently turns a sponsor into
"unknown", or attaches the wrong company's record. **What I'll do:** no automatic fuzzy matching — candidate
matches are shown to a human (gate G2, which exists today); the evaluation set deliberately includes
name-variant traps; and I will report how many of the 25 needed a human to decide.

Known limit today: the current dataset's own README says it starts from an SEC list of funded companies, so
large banks like JPMorgan Chase, Goldman Sachs and Morgan Stanley are not in it (found 2026-10-02).

## 7. Why this project?

*(Chosen 2026-10-12 from options Claude offered; the choices and the no-evidence wording are mine.)*

It is my own question: I am an international student, and this is what I face when choosing a co-op.
It is **a mix** of showing and learning.

- **Already have:** Java, Spring Boot, microservices, Angular, cloud and AI — full-stack work. **Nothing in this
  project shows that**, so the film says so instead of claiming it.
- **New to me:** joining a second public data source (the USCIS H-1B Employer Data Hub) into a small Python tool.

---

## Exists today (I can show it)

- Recipe and prototype `coop_sponsor_check.py`, pushed to my fork at commit `03784b0` (2026-10-03).
- Pull request [nikbearbrown/the-reallocation-engine#40](https://github.com/nikbearbrown/the-reallocation-engine/pull/40),
  open, marked DRAFT, awaiting review (checked 2026-10-12). Not merged.
- 17 unit tests, passing — re-run 2026-10-10.
- A sample run over 7 roles (one fake posting is a deliberate test case; Ananya Rao is a fictional persona)
  covering the six failure cases F1–F6, re-run 2026-10-10 with the same results as 2026-10-03.
- Gates G1–G5, including the human check for ambiguous company names (G2).
- Finding: JPMorgan Chase, Goldman Sachs and Morgan Stanley are missing from the dataset.
- **First 6 of 25 evaluation rows** (2026-10-12, `evidence/eval-first-rows-2026-10-12.md`): all six employers are
  FY2026 petitioners in the USCIS hub, my dataset has a record for none, the tool said unknown every time, and the
  check found a matcher defect ("…AND CO LLC" → "GOLDMAN SACHS AND").

## Will exist

- A second public data source to cover companies missing from the first.
- The remaining 19 evaluation rows, and a fix for the "AND" matcher defect.
- Source citations on every "sponsors software" answer.
- A failure analysis: where the tool was wrong and how I caught it.
- A README written for a hiring manager, with a one-command demo.
