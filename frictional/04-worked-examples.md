# Worked Examples: A Thin Log and a Strong One

**What this page is.** Two Frictional logs for the same Assignment, scored row by row on the [official rubric](../prerequisites/frictional.md). One earns 2/10. One earns 10/10. Read this page before your first submission — it is the fastest way to see what *specific and sufficient* means.

**Both students shipped working code.** On the 60% implementation share they would score within a few points of each other. The Frictional gap is 8 of 10 — most of a letter grade once it is scaled.

> **These are constructed teaching examples, not real student work.** They were written to illustrate the rubric. No student wrote either one.

---

## The Assignment both students did

[Assignment 01 — Randomness and Prompt Contracts](../assignments/assignment-01-randomness-and-prompt-contracts.md): probability normalization, temperature controls, sampling and failure checks in Python; a baseline and a revised prompt contract with explicit inputs, output format and validation; development and held-out runs with raw results preserved and actual Claude runs distinguished from fixtures.

---

## Log A — 2/10

> **FRICTIONAL.md**
>
> **10/12** — Started the assignment. Implemented normalization and temperature and got sampling working. It was a bit confusing at first but I figured it out.
>
> **10/14** — Wrote the baseline and revised contracts. Used Claude to help with the sampling code. Ran the cases and the revised one did better. Temperature was tricky but it works now. Pushed everything. Overall I learned a lot about prompt contracts.

### Scoring

| Row | Score | Why |
|---|---:|---|
| Your attempts | 1 | Names activities but no expectation anywhere. Nothing was predicted, so nothing can have been violated. |
| Friction and response | 0 | "A bit confusing," "tricky." Categories of experience, not experiences. No object, no check, no response. |
| Human and AI contributions | 1 | Claude is disclosed, which is honest and worth something. "Help with the sampling code" does not say what was accepted, changed, or rejected. |
| Learning and uncertainty | 0 | "Learned a lot" is content-free and nothing is named as unresolved. |
| Traceable process | 0 | Two dates, no commits, no test names, no preserved runs. Nothing a reviewer can open. |
| **Total** | **2** | |

**"The revised one did better" is the line to notice.** Better on which set? The Assignment separates development from held-out precisely so that sentence has to pick one. This log reports a result whose meaning depends entirely on a distinction it never makes.

**The point of Log A:** this student may have done every bit of the work. That is the problem. They submitted an artifact indistinguishable from a generated one and a log indistinguishable from a generated one. The 2 is not an accusation — it is the honest statement that the evidence does not support more.

---

## Log B — 10/10

> **FRICTIONAL.md**
>
> **10/12** — *I tried / expected:* Implemented normalization and temperature scaling, then ran the same prompt at temperature 0 twice as a sanity check. Expected byte-identical output.
> *What happened:* Two different completions. I assumed I had left a seed unset or was scaling after sampling instead of before, and spent about half an hour checking both.
> *What I did:* Neither. Greedy decoding still has to break ties between equal-probability tokens, and on this prompt there is a tie early enough to change the rest of the completion. Recorded both outputs in `runs/temp0-a.json` and `temp0-b.json` rather than picking one.
> *What Claude or another person contributed:* Nothing yet.
> *What I understand now / still do not understand:* Understand that temperature 0 constrains the sampling rule, not the output, and that "deterministic" was my assumption rather than a property I had checked. Do not understand how often ties actually occur — I found one by accident and have no way to count them.
> *Evidence and next step:* `test_temp_zero_is_not_guaranteed_identical`; commit `test: record observed variation at temperature 0`. Next: the contracts.
>
> **10/14** — *I tried / expected:* Wrote the baseline contract, then a revised one with an explicit output schema and a validation step. Predicted the revised contract would win on both dev and held-out.
> *What happened:* It won on dev — 17/20 against 12/20 — and lost on held-out, 11/20 against 13/20. I re-ran held-out twice assuming I had loaded the wrong file.
> *What I did:* I had not. Two of the three revisions were written while looking at the dev failures, so the contract encodes the shape of those specific failures. The third revision — the output schema — helps on both sets. Reported all four numbers and named which revision I think generalizes and why.
> *What Claude or another person contributed:* Nothing on this entry; the revisions were mine.
> *What I understand now / still do not understand:* Understand that I was tuning against the set I was measuring on, and that the dev/held-out split exists to catch exactly the move I made without noticing. Do not know how many revisions is too many before dev stops being informative at all.
> *Evidence and next step:* `runs/dev-baseline.json`, `runs/dev-revised.json`, `runs/heldout-*.json` all preserved; commit `fix: report held-out regression instead of the dev improvement`.
>
> **10/15** — *I tried / expected:* Asked Claude how to make the temperature-0 behaviour reproducible for the write-up. Expected a seeding recipe.
> *What happened:* I got one. It also proposed presenting the run as deterministic once seeded.
> *What I did:* **Accepted** the seeding recipe for the test harness, because pinned runs make the tests meaningful. **Rejected** the framing — seeding makes *my* run repeatable, it does not make the decoder deterministic, and reporting it as determinism would state a property the system does not have. Kept both unseeded outputs in the conclusion as the evidence for the repeatability limit, and used seeding only inside tests.
> *What Claude or another person contributed:* Claude — recipe accepted for the harness, framing rejected with reason. Transcript excerpt in `evidence/claude-seeding-1015.md`.
> *What I understand now / still do not understand:* Understand that repeatability and determinism are different claims and that seeding buys the first one only. Still unresolved: whether a seeded run is honest evidence for anything beyond "my harness is stable."
> *Evidence and next step:* commit `test: seed the harness without claiming determinism`.
>
> **10/16 (retrospective, written 10-17)** — *I tried / expected:* Final pass; expected only README edits.
> *What happened:* Two of the rows I had described as Claude runs in the conclusion are fixtures I wrote while the API call was failing. The numbers are fine; the labels were wrong, and the conclusion read as if four live runs supported it when two do.
> *What I did:* Relabelled both in `runs/` and rewrote the conclusion sentence to say two live runs and two fixtures. The claim is weaker and it is now true.
> *What Claude or another person contributed:* Nothing.
> *What I understand now / still do not understand:* Understand why the brief asks for the fixture distinction explicitly — I blurred it without intending to, in the write-up rather than in the code. Do not know how to make the labelling automatic so it cannot drift again.
> *Evidence and next step:* commit `fix: relabel two fixtures misreported as live runs`; VERIFICATION.md limits section.

### Scoring

| Row | Score | Why |
|---|---:|---|
| Your attempts | 2 | Every entry states what was tried and what was expected. The 10/14 prediction is specific enough to be *wrong* in an informative direction, which is what makes it worth 2. |
| Friction and response | 2 | Four frictions, each anchored to an object — two different temperature-0 completions, 17/20 vs 11/20, the determinism framing, two mislabelled runs — each with what was done next. |
| Human and AI contributions | 2 | Claude's contribution is bounded precisely: recipe accepted for one use, framing rejected with a reason, transcript preserved. The three entries with no AI use say so. |
| Learning and uncertainty | 2 | Something changed in every entry and every entry names something still open. "I was tuning against the set I was measuring on" is the strongest line in the log. |
| Traceable process | 2 | Every entry cites a test, a commit subject, or a preserved run file. The retrospective entry is marked. |
| **Total** | **10** | |

---

## What actually separates them

Log B is not longer because the student worked harder or wrote better. It took roughly twelve minutes across four sessions. It is longer because it is **anchored**: every claim points at a specific object in the actual work.

Three moves do nearly all of the work, and you can copy all three:

1. **Write the expectation before the run.** You cannot record a violated prediction if you never recorded a prediction — and this Assignment already asks you to preserve the original expectation.
2. **Name the object, not the category.** Not "temperature was tricky" — `17/20 against 12/20 on dev, 11/20 against 13/20 on held-out`, `test_temp_zero_is_not_guaranteed_identical`.
3. **Say what you did with the help.** Accepted, changed, or rejected. Log B's highest-value entry is the one where Claude's recipe was useful and its framing was worth refusing.

Before you submit, take any sentence in your log and ask whether a classmate who never opened your repository could have written it. If they could, you have written about the Assignment. Write about what happened instead.
