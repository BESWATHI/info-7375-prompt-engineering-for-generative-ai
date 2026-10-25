# CONTRACT.md — Job-Search Agent 1: The Contract and the Watch

**Author:** Prasad [LastName]  
**Date written (before any run):** 2026-10-25  
**Version:** Draft v0.1 — written before implementation  
**Board:** Greenhouse — `[BOARD_TOKEN_TO_FILL_IN]`  
**Language / toolchain:** [TO FILL IN: e.g., Python 3.12, stdlib only + `requests`, `pytest` — name exact version before first run]

> This contract was written before I asked Claude to implement anything.
> Implementation must match this document. If implementation and contract
> disagree, the contract is wrong or the code is wrong — I will note which
> I changed, when, and why in FRICTION_LOG / FRICTIONAL.md. I will not
> silently edit this contract after a run to make the results look correct.

---

## 1. In — What the agent takes in

1. **Board name (one board only)**
   - A single Greenhouse board token, e.g. `boards.greenhouse.io/<token>`,
     given as a command-line argument or config value.
   - The token identifies *one* company board. The agent does not discover
     other boards, search Greenhouse, or follow links to other companies.

2. **Résumé as JSON (fictional persona only)**
   - A local file path to a résumé in JSON, e.g. `resume_persona.json`.
   - Required fields, all required — if any is missing or empty, the agent
     stops with an error and produces no verdicts:
     - `name` (string) — fictional name only
     - `email` (string) — must end in `@example.com`
     - `phone` (string) — must be a `555-` number
     - `target_titles` (list of strings, at least 1) — e.g. 
       `["Associate Product Manager", "Product Manager", "Product Analyst"]`
     - `skills` (list of strings, at least 3) — e.g.
       `["Python", "SQL", "A/B testing", "roadmapping", "user research"]`
     - `locations` (list of strings, at least 1) — e.g.
       `["Remote - United States", "Boston, MA", "New York, NY"]`
     - `max_years_required` (integer) — maximum years of experience the
       persona will consider, e.g. `3`
   - Example fictional persona in the repo (invented, not me):
     - Name: Alex Rivera
     - Email: alex.rivera@example.com
     - Phone: 555-0142
     - The repo and all screenshots use this persona only.

3. **State file**
   - A local JSON file, e.g. `state.json`, containing the list of posting
     `id`s seen on previous runs. If it does not exist, it is created as
     empty and that run is the baseline (see §2).
   
4. **What it needs to run**
   - Network access to the allow-listed host only (see §3).
   - Read access to the résumé JSON and the state file.
   - Write access to: the raw-evidence directory, the updated state file,
     and the run report. No other writes, no sending, no applying.

## 2. Out — What it returns

For **each new posting only** — a posting whose `id` was not in the state
file at the start of the run — the agent returns one record with:

- `posting_id` (string, copied exactly from the board response)
- `title` (string, copied exactly)
- `absolute_url` (string, copied exactly)
- `location.name` (string, copied exactly, or `"not stated"` if absent)
- `rule_verdict`: `"relevant"` or `"not_relevant"` — from §4, recomputable
- `rule_justification`: an object that **must** name both sides:
  - `resume_fields`: the exact field names and values used, e.g.
    `target_titles: ["Product Analyst"]`, `skills: ["Python", "SQL"]`
  - `posting_fields`: the exact field names and values used, e.g.
    `title: "Product Analyst, Growth"`, 
    `content: "...python... sql..."`
  - `conditions`: for each condition in §4, `true` / `false` and why
- `claude_verdict`: `"relevant"` or `"not_relevant"` — **labeled in every
  output as `judgment (Claude)`, never as a fact or as the rule verdict**
- `claude_justification`: Claude's text, validated to the fixed format in
  §6. If it does not validate, the record is rejected, not repaired silently.

Other outputs for a run:
- The raw board response, saved unchanged as evidence, with fetch date/time
  and URL in the filename or a sidecar note.
- An updated state file containing all ids seen up to and including this run.
- A run summary: `total_fetched`, `new_count`, and the list of new ids.
- **Baseline rule:** On the first run (empty state), the agent saves all
  ids and reports **0 postings as new**. It does not judge the baseline set.

If there are no new postings, the agent returns an empty new-postings list
and says so. It does not re-judge old postings to fill the report.

## 3. Refuses — What it will not do

The agent **will not**:

1. Fetch any host not on the allow-list. Allow-list for v1 is exactly:
   - `boards-api.greenhouse.io`
   Any other host — including a redirect to another host, a link inside a
   posting, or a board on Ashby / Lever / SmartRecruiters — is refused and
   logged, not followed.
2. Show a real résumé on screen, in logs, in tests, or on GitHub. Only the
   fictional persona résumé may be printed, committed, or screenshotted.
   If the résumé email is not `@example.com` or the phone is not a `555-`
   number, the agent refuses to run.
3. Present a model's judgment as a fact. Claude verdicts are always labeled
   `judgment (Claude)`. Only the rule verdict in §4 is a record that anyone
   can recompute from the saved raw response and the persona résumé.
4. Apply to a job, send email or messages, create accounts, or contact an
   employer or a person named in a posting.
5. Infer facts not in the posting or the résumé — e.g. salary, visa
   sponsorship, whether a company is "good," or whether the persona would
   "like" the job — and use an inferred fact in a verdict.
6. Store credentials, cookies, or API keys, or read files outside the
   résumé path, the state file, and the raw-evidence directory it was given.

A refusal is an output: the agent stops or skips that item, logs the reason,
and does not produce a substitute verdict.

## 4. The Rule — How relevance is judged

A TA must be able to predict the rule verdict by hand from the saved raw
response and `resume_persona.json` alone, without running code or asking a model.

All text matching is case-insensitive. A "contains" match means the exact
term, as a whole substring, appears in the field — no synonyms, no stemming,
no model interpretation. `APM` does not count as `Product Manager` unless
`APM` is listed in `target_titles`.

A posting is **`relevant` if and only if ALL three conditions are true**:

- **C1 — Title:** `posting.title` contains at least one string from
  `resume.target_titles`.
- **C2 — Location:** `posting.location.name` contains at least one string
  from `resume.locations`, **or** `posting.location.name` is exactly
  `"Remote"` and `resume.locations` contains a string starting with `"Remote"`.
- **C3 — Skills:** The posting's text (`posting.content` with HTML tags
  removed, or `posting.description` if `content` is absent) contains at
  least **2 distinct** strings from `resume.skills`. The same skill counted
  twice counts once.

Otherwise — if any of C1, C2, or C3 is false — the posting is
**`not_relevant`**.

Notes for hand-checking:
- If a field is missing, that condition is `false`. Missing data is not
  guessed.
- The rule does not use Claude, scores, approval counts, posting date,
  company size, or any field not listed above.
- `max_years_required` is recorded in the résumé for later assignments;
  it is **not** part of the v1 rule, specifically so a TA does not have to
  parse experience requirements from free text by hand. If I add it later,
  I will change this contract, change the version, and re-run the tests.

**Worked example (invented, for hand-checking):**
- Résumé: `target_titles=["Product Analyst"]`, 
  `locations=["Boston, MA"]`, `skills=["Python","SQL","Tableau"]`
- Posting: `title="Product Analyst"`, `location.name="Boston, MA"`,
  content contains "Python" and "SQL"
- C1 true, C2 true, C3 true (2 skills) → `relevant`, and the justification
  must list exactly those résumé values and those posting fields.

## 5. Wrong Versions — Plausible-but-wrong implementations tests must catch

Tests written from this section must fail on these versions and pass on
the correct one. These are not bugs in general — they are specific wrong
implementations of *this* contract.

- **W1 — Mismatched pairing (labels paired with the wrong postings)**
  The code computes verdicts correctly for a set of postings, but attaches
  each verdict / justification to a different `posting_id` (e.g. by sorting
  verdicts and postings independently, or by zipping two lists in different
  orders). Output looks plausible — every posting has a verdict — but the
  verdict for posting A is actually the verdict for posting B.
  *Test that must catch it:* Two postings with opposite hand labels and
  distinct ids/titles; assert each id carries its own hand-computed verdict
  and cites its own title. Reordering the input must not change which
  verdict belongs to which id.

- **W2 — Justification that cites nothing (or cites what is not there)**
  The code returns the correct `relevant` / `not_relevant` label, but the
  justification is empty, generic ("matches the résumé"), or cites a skill /
  title / location that is not in the résumé or not in that posting.
  Under this contract, a right label with a wrong justification is a failure.
  *Test that must catch it:* For every record, assert every term in
  `rule_justification.resume_fields` is present in the résumé file and every
  term in `rule_justification.posting_fields` is present (case-insensitive)
  in that posting's saved fields; assert a relevant record cites at least
  1 target title and at least 2 skills.

## 6. Two Judges — Rule vs. Claude

- **Rule judge (a record):** Implements §4 exactly. Deterministic. Anyone
  with the raw response + résumé can recompute it by hand or by re-running
  the function. Disagreement with the hand label means the code or the
  hand label is wrong — investigate, do not average them away.
- **Claude judge (a judgment):** Claude receives one new posting and the
  persona résumé fields, under a prompt contract that requires exactly:
  ```
  VERDICT: relevant | not_relevant
  RESUME_FIELDS: <comma-separated field names and values used>
  POSTING_FIELDS: <comma-separated field names and values used>
  REASON: <one sentence naming a match or a failed condition>
  ```
  A validator checks the output line-by-line. Anything else — extra labels,
  missing lines, a verdict word outside the two allowed values, empty
  fields — is **rejected** and recorded as `claude_verdict: "rejected"`.
  No free-form Claude output is presented as a verdict.

The two verdicts are reported side by side and never merged into one score.

## 7. What a Failure Looks Like

**Dated sentence, written before any run:**

> On 2026-10-25, before running anything, I will call this a failure if,
> on the run I submit, the agent reports an already-seen posting as new,
> or labels a posting `relevant` whose justification does not cite a
> target-title match from the résumé and that title in the posting itself.

Other failures are possible; this is the minimum I commit to checking first.

---

## To fill in before first run (do not leave blank in the submitted version)

- [ ] Real Greenhouse board token I chose, and why I chose that company/board
- [ ] Exact language, version, libraries, and commands in README.md
- [ ] Final persona values in `resume_persona.json` — if they differ from the
      examples above, update §4's example and §1's list to match exactly
- [ ] My name and the date I signed / withheld the final sign-off in README.md
