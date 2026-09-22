# What to Write in FRICTIONAL.md

**What this page is.** The seven entry prompts in [prerequisites/frictional.md](../prerequisites/frictional.md), what each one is actually asking for, and which rubric row it feeds.

**The short version.** Short dated entries, written while you work. One entry per work session. Fragments are fine; the log is not prose. Three or four entries for a ten-day Assignment is normal.

**The one thing that decides your score.** Specificity. Every row of the rubric awards 2 for *specific and sufficient*, 1 for *vague or incomplete*, 0 for *absent*. Nearly every point lost in this component is lost to vagueness, not to dishonesty or to bad results.

---

## The prompt-to-rubric map

The entry prompts are not arbitrary. Each one feeds a rubric row.

| Entry prompt | Rubric row | Points |
|---|---|---:|
| I tried / expected | Your attempts | 2 |
| What happened · What I did | Friction and response | 2 |
| What Claude or another person contributed | Human and AI contributions | 2 |
| What I understand now / still do not understand | Learning and uncertainty | 2 |
| Date and what I was working on · Evidence and next step | Traceable process | 2 |

Use the prompts that fit the episode, covering the rubric across the Assignment — that is what
[prerequisites/frictional.md](../prerequisites/frictional.md) asks for. Skipping a prompt for the whole
Assignment is volunteering a zero.

---

## Prompt by prompt

### Date and what I was working on
The date you did the work, and the goal for that session. If you are writing the entry later than the
session it describes, label it: `2026-10-03 (retrospective, written 10-05)`. Labelling costs nothing, and
an unmarked retrospective that reads as contemporaneous is a fabrication problem, not a style problem.

### I tried / expected → *Your attempts*
The attempt, and the prediction that went with it. The prediction is the part people skip and it is half the row.

> Weak: *Worked on the sampling code.*
>
> Strong: *Implemented temperature scaling, then ran the same prompt at temperature 0 twice as a sanity check. Expected byte-identical output.*

An attempt that failed earns the same 2 points as one that worked. This row scores whether you can say what
you were doing and what you thought would happen.

### What happened → *Friction and response* (first half)
The place the work resisted. **Name the object.** "It was confusing" names a category of experience, not an
experience.

> Weak: *Temperature was confusing at first.*
>
> Strong: *Two different completions at temperature 0. I assumed a missing seed or scaling applied after sampling, and checked both.*

A check you ran counts here too, even when it found nothing.

### What I did → *Friction and response* (second half)
What you did about it, including approaches you abandoned and why. Dead ends are worth more than the fix,
because a dead end you can describe is proof you were somewhere.

> *Neither. Greedy decoding still breaks ties between equal-probability tokens. Recorded both outputs in `runs/` rather than picking one.*

### What Claude or another person contributed → *Human and AI contributions*
Who or what helped, what it produced, and what you **accepted, changed, rejected, or still do not
understand**. That last clause is the graded part. Naming the tool without naming the disposition is a 1,
not a 2. Prompt excerpts are enough — the rubric says complete chat transcripts are unnecessary.

> Weak: *Used Claude for the sampling code.*
>
> Strong: *Asked Claude for a seeding recipe. Accepted it for the test harness; rejected its framing that a seeded run is deterministic, because seeding makes my run repeatable and says nothing about the decoder.*

### What I understand now / still do not understand → *Learning and uncertainty*
What changed, and what is still open, plus your next question or step. **"Nothing is unresolved" is almost
never true** and reads as the least credible available answer.

> *Understand that temperature 0 constrains the sampling rule, not the output. Do not know how often ties actually occur — I found one by accident and have no way to count them.*

### Evidence and next step → *Traceable process*
The link between this entry and something inspectable: a commit hash or subject, a test name, a preserved
run file, a prompt excerpt.

> *`test_temp_zero_is_not_guaranteed_identical`; commit `test: record observed variation at temperature 0`. Next: the contracts.*

---

## How much to write

An entry is three to six lines. A ten-day Assignment usually produces three to five entries. If an entry is running past a paragraph per field you are writing an essay about your process instead of logging it.

The floor that works: **one entry per work session, dated, with the prompts that fit answered, even when the answer is short.** "Nothing resisted today; ran the tests, all passed, checked the endpoint case by hand" is a legitimate entry and will not cost you points.

## Before you submit

- [ ] Every entry is dated, and retrospective entries are labelled
- [ ] At least one entry names a specific object — a value, a test, a line, a filename — not a category
- [ ] At least one thing that did not work is written down, with why you moved off it
- [ ] Every AI and human contribution says what you accepted, changed, or rejected
- [ ] Something is named as still unresolved
- [ ] Entries point at commits, tests, or outputs a reviewer can open
- [ ] `FRICTIONAL.md` is in `fall-2025/first-name-last-initial/assignment-XX/` and the Canvas version matches
