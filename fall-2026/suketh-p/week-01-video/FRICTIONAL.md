# FRICTIONAL.md — Week 1 Explainer Video

> **Current state (2026-09-24).** Runtime **195.16 s (3:15)** · Gate V **0 BLOCKER / 0
> MAJOR** · GATE T **0 FAIL · 1 WARN · 29 PASS** · **28** tests · 4/4 mutations caught.
>
> The entries below are **dated as they happened** and quote the numbers that were true
> on each day — 0/3/27, "two digits out of sixty", and so on. They are left standing on
> purpose: this is a log of what actually occurred, and a log that edits its own past is
> not evidence of anything. Where an entry differs from the block above, the block above
> is current.

**Student:** Suketh Produtoor
**Assignment:** Week 1 Explainer Video — Explain One Concept from Chapter 1
**Course AI policy:** [AI Policy for Professor Bear's Courses | Using AI Responsibly in Class](https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz)

Per [`prerequisites/frictional.md`](../../../prerequisites/frictional.md): this is an honest
log of what was tried, what broke, and what was decided — not a timesheet and not a
performance of difficulty. Entries are dated as they happened.

**Method disclosure, stated once and plainly.** All work below was done in a single
Claude Code session on 2026-09-15, with Claude Opus 5 driving the terminal under my
direction. Claude read the chapter and the toolkit doctrine, ran the reference code,
diagnosed the install failures, authored the beat sheet and the Remotion components, and
rendered the film. Where an entry says "Claude found" or "Claude proposed", that is
literal. Entries marked **`[MINE — to complete]`** are reflection prompts that only I can
answer honestly; I fill those in after watching the cut, and I do not let the assistant
write them for me. Nothing in this file claims an approval, a test result, or an
understanding that did not occur.

---

## 2026-09-15 — Picking a concept small enough to finish

**I tried / expected:** The brief warns that the usual failure is a three-minute tour of
the whole chapter. I expected the hard part to be production; it was actually scoping.

**What happened:** Claude read Chapter 1 end to end and shortlisted three candidates from
the brief's own list: the expected-count-versus-observed-count pair (665.24 vs 630),
temperature as a ratio, and the max-subtraction. All three are legitimate. The
max-subtraction is the smallest — it is literally one subtraction — and it is the only one
of the three that has a *provable* core (the factor cancels) sitting next to a *runnable*
failure (the raw exponential actually raises).

**What I did:** Chose the max-subtraction. Rejected the 665.24-vs-630 concept specifically
because the brief lists it first and it is the most likely thing for a cohort to converge
on; the distribution-versus-sample point still appears, but as one context line in the
verification script rather than as the subject.

**What Claude contributed:** The shortlist, the argument that max-subtraction is the
smallest of the three, and the observation that it uniquely pairs a proof with a
demonstrable crash.

**Evidence:** [`beat_sheet.json`](beat_sheet.json) `metadata.concept`; Chapter 1 §"The
subtraction that changes nothing important".

---

## 2026-09-15 — The toolkit would not install (four separate causes)

**I tried / expected:** `git clone` the toolkit, run `./setup --install`, start building. I
expected one install step.

**What happened:** Four failures in sequence.

1. `./setup` reported **6 of 7 features blocked**. Only slates/previz/compile were ready.
2. `./setup --install` failed the entire Python dependency step. The actual root cause was
   one line deep in the pip output: `pycairo` could not build because
   `Pkg-config for machine host machine not found`. `cairo` itself was already present via
   Homebrew (1.18.4) — only `pkg-config` was missing. Because `pip install -r
   requirements.txt` is a single transaction, that one package took **Kokoro and
   faster-whisper down with it**. The blocked-audio message was a symptom, not the cause.
3. I had also installed into the **Anaconda base environment**, which
   [`prerequisites/brutalist-video.md`](../../../prerequisites/brutalist-video.md) explicitly
   warns against ("Avoid the system Python environment"). I had skipped the venv step in
   the documented setup sequence.
4. Rebuilt the venv — and it landed on **Python 3.14**, for which `manim>=0.18,<0.19` has
   no distribution at all (`No matching distribution found`). So the fix for (2) exposed a
   fresh incompatibility.

**What I did:** `brew install pkgconf` for the real cause, then rebuilt the venv on
**Python 3.12.7** and installed the audio pipeline *without* Manim. That last decision is
the one worth defending: the prerequisite says a first video should "use existing
chart/diagram components and avoid equation beats", and that "the doctor may still report
that unused feature as blocked: record it honestly". Manim stays blocked in this
environment and this film never calls it — all the mathematics renders as Remotion scenes
instead. Final readiness: audio ✅, captions ✅, Remotion ✅, slates/compile ✅, fonts ✅,
**Manim ❌ (blocked, unused)**.

**What Claude contributed:** Found the `pkg-config` line in ~200 lines of pip output,
identified that a single-transaction install was masking the cause, caught that I had
violated the prerequisite's venv instruction, and made the call to drop Manim rather than
fight a version conflict for a feature the film does not use.

**What I still do not fully understand:** Why `requirements.txt` pins `manim<0.19` when
0.19+ exists. I did not investigate, because I removed the dependency instead of
satisfying it. If a later assignment needs equation beats, this is the first thing to go
back to.

**Evidence:** `./setup` readiness table; [`BUILD-PROMPT.md`](BUILD-PROMPT.md)
"Environment" section, which records the exact working recipe.

---

## 2026-09-15 — The finding I did not go looking for

**I tried / expected:** I only wanted to verify that the shift is harmless — that
`probabilities([1,2,3])` matches the chapter's published table. I expected a clean tick and
a short beat.

**What happened:** Two results I did not predict.

- **The two paths are not bit-identical.** I assumed shifted-then-normalize and
  direct-exponentiate-then-normalize would return the same floats. They do not. They
  differ by `1.1102230246251565e-16` — one machine epsilon, in exactly **two digits out of
  fifty-three** (character positions 19 and 60; I first wrote "sixty" here from the
  62-character string length — corrected 2026-09-24, `SOURCES.md` §5.12). Mathematically the cancellation is exact; in
  float64 it is only indistinguishable. I had been about to narrate "the same numbers".
- **The subtraction only protects one end.** Checking that the denominator can never
  underflow (it cannot — the peak's weight is exactly 1, so the total is always ≥ 1) made
  me ask the mirror question about the *numerator*. `probabilities([0, -800])` returns
  `[1.0, 0.0]` — an **exact zero** for an outcome whose true share is about `1e-348`.
  Walking the second score down found the cliff: `-745` still returns `5e-324` (the last
  denormal), and `-746` is where it becomes a hard `0.0`.

**What I did:** Rebuilt the video around the second finding. It became B07 and the
"NOT ESTABLISHED" line of the verdict — which is exactly the rubric's "name one thing your
explanation does not establish", except demonstrated on the real function instead of
hedged in a sentence. The first finding became B06, and it changed a claim I was about to
make on camera.

This also connects to the chapter's own warning, which I had read past the first time:
*"Keep the tested claim narrower than the slogan 'numerically stable.'"* I now think that
sentence is the point of that whole section, and I had been treating it as a caveat.

**What Claude contributed:** Ran the boundary sweep, located the `-746` tipping point, and
pushed back when I wanted to state the two paths were equal.

**Evidence:** [`evidence/verify_claims.py`](evidence/verify_claims.py) claims 4 and 5;
[`evidence/run-output.txt`](evidence/run-output.txt) — the recorded run every on-screen
number is read from.

---

## 2026-09-15 — Three places the doctrine and the tooling disagree

All found while following `skills/make/ai-explainer/SKILL.md` literally. A fourth — the
one that actually broke a beat — is in the QC entry below.

**1. `lead_silence_s` is required but not implemented.** The SKILL.md's
EXECUTIVE-SUMMARY LAW requires beat 2 to carry an explicit `lead_silence_s: 0.8` so the
hesitant-writer typing gets a head start. `grep -rn "lead_silence" runtime/scripts/*.py`
returns **nothing** — the free toolkit's audio script does not read that field. I left it
in the beat sheet because the doctrine asks for it, and instead guaranteed the ≥9 s window
by writing B01 long enough to earn it on measured audio. Recorded here rather than
silently dropped.

**2. The locked outro card would have been an impersonation.** `OUTRO-LOCK.md` hardcodes
the handle `@NikBearBrown` into `ClaudeTitleOutro` and says the handle is "a constant, not
a lookup". Using the shipped outro would have stamped the instructor's channel onto a
student submission. The lock's own scope clause resolves it: it applies to
`claude-liam-*` reels only, and "Other channels … NEVER get this card, handle, or mascot."
So this reel has its own `ShiftOutro`, its own corner bug, and no mascot — and the
narration deliberately omits the IN-FOR-BEAR line ("this is Liam, in for Bear") that every
worked example carries.

**3. GATE T cannot be run at all in this checkout.** The SKILL.md says "**GATE T
(type-lock) — ALWAYS RUN**, like factcheck. `scripts/type_check.py` asserts §8.1 min-size,
§8.2 overflow, §8.3 contrast … then writes `TYPECHECK.md`. No `./art run` and no
`./art final` may report success while `TYPECHECK.md` has any FAIL." That script is not in
the public cut — there is no `scripts/` directory at the toolkit root, and
`find . -name type_check.py` returns nothing. So the gate the doctrine calls mandatory is
unrunnable here. I did the type checks it describes by hand instead: min type size, the
overflow/edge-safe check, and contrast are all covered by the Gate V pass and the band
arithmetic I worked out for B02 and B04. Recording it because a missing mandatory gate is
exactly the kind of thing that should not be discovered silently.

**Why the outro one mattered more than it looks:** the prerequisite's own rule is "Do not imply a
synthetic narrator is me, Bear, or an official endorsement." Copying the exemplar's
bookends faithfully would have broken that rule *by being faithful*. The synthetic voice
therefore never says "I am" anyone; authorship is carried on screen, and the disclosure is
on the outro card, in `SOURCES.md`, and in the README.

**What Claude contributed:** Caught both conflicts by reading the lock file's scope clause
rather than just its rules, and proposed the own-outro fix.

---

## 2026-09-15 — Library-first, and a miss that became components

**I tried / expected:** GATE L in the SKILL.md requires asking the scene library before
authoring anything: "A miss is never a licence to slate." I expected to find a
numbers-transforming component among the 610 registered scenes.

**What happened:** Genuine miss. `./art scenes` returned leads for pipelines, code blocks
and comparisons, but every candidate was reel-local to someone else's film with its
content hardcoded and only a `sparkLine` prop — nothing parameterized for arbitrary
figures.

**What I did:** Treated it as the PUNT the doctrine describes — a design card, not a slate.
Authored six reel-local components in
`brutalist.art/runtime/remotion/src/ShiftedNotChanged.tsx` and registered them in
`Root.tsx`, then ran `./art scene-index` so they are discoverable (index went 610 → 616
renderable). Every component takes its numbers as **props**, so a wrong figure is a
beat-sheet fix and never a component fix.

**Evidence:** `./art scenes --check ShiftPipeline` → `RENDERABLE 16:9`; the six scenes now
in `scenes.json`.

---

## 2026-09-15 — The first cut compiled cleanly and was still wrong

**I tried / expected:** `./art run` finished, reported 11/11 slots filled, 186.0 s, zero
BLOCKER defects. I expected to be done and to go write the README.

**What happened:** Gate V flagged 4 MAJOR `underfill` defects, so I opened the contact
sheet — and found **two more problems no gate reported**, both inside the safe area where
no automated rule looks:

1. **B01's correction never fired.** The beat types "…makes softmax numerically stable."
   and the phrase just *stays there*. The entire video argues that "numerically stable" is
   the wrong word, and my overview beat was leaving the wrong word uncorrected on screen.
   Cause: `BrutalistHesitantWriter` matches `triggerWords` **per whitespace token**, so my
   two-word trigger `numerically stable.` could never match anything. It failed silently.
   Fixed by moving the misconception onto one token: `stable` → `overflow-safe`.
2. **B04's verdict line overlapped the fraction above it.** "The shift never reaches the
   ratio." was sitting on top of the denominator.

And the `underfill` on B10 turned out not to be a layout mistake at all.
`remotion_scenes.py` renders the *registered* composition length and then conforms to the
audio — freeze-holding a short clip but **truncating** a long one. My outro was registered
at 7 s against a 2 s narration, so only the first 29% ever played and the author line and
the disclosure were never in the file. Fixed by pinning every registered duration to the
measured mp3 and giving the outro a real sign-off.

**What I did:** Re-banded B02 and B04 with explicit vertical gaps, scaled B01 and B10 up,
relabelled the motion field honestly (I had tagged every body beat `illustrate` when the
scenes do different things — the label was the defect, not the motion), cleared `media/`
and `clips/`, and re-rendered. Full write-up with severities in
[`REVIEW.md`](REVIEW.md).

**What Claude contributed:** Read the sampled frames, spotted the two collisions the gate
missed, and traced the B10 underfill to the truncation rule in `remotion_scenes.py` rather
than treating it as a font-size problem. It also reproduced the token-matching bug outside
the renderer to prove the cause instead of guessing.

**What changed in my understanding:** I had been reading "VISUAL QC LAW" as bureaucracy —
a box to tick after the render. It is the opposite. A successful compile told me 11/11
slots were filled; it could not tell me that one of those slots contained the exact
misconception the film exists to demolish. **The mp4 probe and the gate agreed the film
was fine. Looking at it was what disagreed.** That is the same distinction the chapter
keeps making — a passing check is evidence for its stated property, and nothing more —
and I hit it in my own build within an hour of narrating it.

**Evidence:** `_qc/REPORT.md` (round 1: BLOCKER 0, MAJOR 4), `_qc/contact_sheet.png`,
`REVIEW.md` R1-1 through R1-6.

---

## 2026-09-15 — A submission-path conflict I did not invent a rule for

**What happened:** The Canvas brief says to post under
`fall-2025/first-name-last-initial/week-01-video/`.
[`prerequisites/github-submission.md`](../../../prerequisites/github-submission.md) says
`fall-2025/first-name-last-initial/assignment-XX/`. They disagree, and the folder also
says `fall-2025` while the course is Fall 2026.

**What I did:** Followed **Canvas verbatim** (`week-01-video`, `fall-2025`), because the
brief states "Canvas is the authority on which version applies to your section" and the
same policy note logs the unreconciled wording under instructor decisions, item 7. Flagged
rather than silently normalized — I am not going to quietly pick a grading rule.

---

## 2026-09-18 — Second pass, after re-reading the AI policy

**I tried / expected:** I had a clean film on 2026-09-15 and thought I was done. Then I
went back to the [AI policy](../../../prerequisites/ai-policy.md) and the instructor's policy
video, and one line reframed the whole thing: *"Iterate: examine the first result,
identify weaknesses, revise, test, and improve it."* Treating the first clean render as
the deliverable is exactly what that sentence warns against. So I went looking for the
weakest part of my own submission rather than polishing the strong parts.

**What I found — the weakest claim was my best one.** B07 said the cliff is at −746. True,
but I had found it by *sweeping inputs*. Poking a function until it breaks proves a
boundary exists; it does not explain why it sits there, and it would not transfer to
another float format or another function. That is a thinner kind of evidence than the rest
of the film, and it was sitting on the film's most important beat.

**What I did:**

1. **Derived it instead.** binary64's smallest subnormal is 2⁻¹⁰⁷⁴; under round-to-nearest
   anything below half of that has no nearer representable neighbour than zero, so
   `exp(z)` returns `0.0` once `z < ln(2⁻¹⁰⁷⁵) = −1075·ln 2 = −745.133219102`. Bisecting
   the real boundary agrees **to nine decimal places**, and −746 is simply the first
   integer past it. B07 now shows the closed form. The number went from discovered to
   predicted.
2. **Measured what the boundary actually costs.** I had been saying "a small probability
   becomes zero", which undersells it. `probabilities([0, −800, −900])` returns
   `[1.0, 0.0, 0.0]` — two outcomes **100 nats apart** reported as the same number. That
   is not a rounding nuisance, it is a loss of ordering.
3. **Showed the remedy.** Carrying the same distribution in log space keeps
   `[0.0, −800.0, −900.0]` — correctly ranked, nothing lost — and reproduces the reference
   to 1e-12 on `[1,2,3]`, so it is the same mathematics and not a different answer. This
   is what production libraries do, and it is the practical end of the film's boundary.
4. **Kept it out of the film.** All of (2) and (3) live in `evidence/boundary_analysis.py`,
   not as beats. The brief says pick the smallest idea and explain it completely; adding a
   remedy act would have been a second concept. Only the one-line derivation went on
   screen, because it deepens the claim already there.

**The correction I did not expect to have to make.** I wrote into `mutation_check.py` that
removing the max-subtraction would leave "the sum-to-one and chapter-table tests" green.
Then I ran it. **Wrong.** The 8 survivors are almost entirely the tests that never call
`probabilities()` at all — my own closed-form derivation tests, plus the raw `math.exp`
overflow test. Those verify the *mathematics* and are structurally blind to a defect in
the *implementation*.

That is a real coverage boundary in my own test suite, and I only saw it because I ran the
check instead of trusting my reasoning about it. The script now prints the survivor list
from the run rather than asserting it, so the claim cannot drift from the evidence again.

**What changed in my understanding:** I had been treating "28 tests, all green" as the
evidence. It is not — it is a claim *about* evidence. Mutation testing is what turns it
into evidence, and when I ran it the suite was still sound (4/4 mutations caught) but my
*description* of it was false. That is the film's own distinction — a passing check is
evidence for its stated property and nothing more — arriving a third time, in my own
paperwork, after I had already narrated it twice.

**What Claude contributed:** the derivation, the log-space demonstration, and
`mutation_check.py` itself — including the run that corrected my claim about it. Per-portion
breakdown in [`SOURCES.md`](SOURCES.md) §4.

**Evidence:** `evidence/boundary-output.txt`, `evidence/mutation-output.txt`,
`FACTCHECK.md` rows 17–18, `SOURCES.md` §5.5–5.6, `REVIEW.md` round 6.

---

## 2026-09-20 — I stopped using a missing script as an excuse

**I tried / expected:** Three times now I had written a version of "GATE T could not be
run — the script is not in the public checkout." It is a true sentence. It is also an
excuse, and the SKILL.md is blunt that the gate is mandatory: *"No `./art run` and no
`./art final` may report success while `TYPECHECK.md` has any FAIL."* My film was
reporting success with no TYPECHECK.md at all.

**What I did:** Wrote the gate. `evidence/gate_t_typecheck.py` implements the parts of §8
that can be checked honestly from the scene source and the beat sheet — §8.1 min-size,
§8.3 WCAG contrast, §8.5 word budget, §8.6 figure-wiring — and writes `TYPECHECK.md`. The
header states plainly what it does **not** cover (§8.2 overflow and §8.4 kerning need
rendered frames and font metrics; §8.6 checks wiring, not pixels) so it cannot be mistaken
for the real gate.

**What happened — it failed on the first run, and it was right.**

1. **The worst one.** `GHOST` (`#B0AD9A`) on the cream stage measures **1.98:1**. WCAG
   AA-large wants 3:1. And `GHOST` was the colour of the **synthetic-narration
   disclosure** on the outro card — the single line in this film that has an ethical
   reason to be readable, rendered almost invisibly. I had picked it by eye for
   "quiet" and never measured it. All three `GHOST` text uses are now `SOFT` (4.37:1).
2. **`ACC` on cream is 2.74:1**, also under AA-large. This one I cannot fix:
   `CLAUDE-BRAND.md` says the palette replicates the real product and must not be
   retinted. So the gate now records it as a brand-locked WARN and **checks the
   mitigation** instead (§8.3b) — every terracotta element must also differ by weight,
   size, or a rule, so colour is never the only signal. That check immediately found
   B03's focal cells were colour-only; they gained `fontWeight: 700`.
3. **Two figures flagged as "not in any recorded run" — a false positive in my own
   check.** `0.3678794412` and `0.6652409558` are correct 10-dp roundings of
   full-precision values, and the second is verbatim Chapter 1's published table. The
   check now accepts a correct rounding and prints which value it rounded, instead of
   demanding a substring match.

State on this date: **0 FAIL · 3 WARN · 27 PASS** — the brand-locked accent plus two beats
1–2 words over the soft word budget. (The two word-budget warnings were cleared on
2026-09-24 when I rewrote those beats for precision; the gate now reads **0 FAIL · 1 WARN ·
29 PASS**, with only the un-retintable accent remaining.)

**What Claude contributed:** wrote the gate, and ran it. The GHOST contrast defect had
survived five rounds of visual QC and my own frame-by-frame review — I had *looked* at
that outro card repeatedly and read the disclosure as "appropriately subtle" rather than
"failing contrast." An arithmetic check caught what looking could not.

**What changed in my understanding:** this is the third time in this project the same
shape has appeared. A green gate, a passing test suite, and now my own eyes all reported
"fine" about something that was measurably not. The film argues that ranking a
continuation highly is not evidence it is true; the build kept teaching me the same
lesson about my own checks. I now think the interesting question for any check is not
"did it pass" but "what would still be wrong if it did."

**Evidence:** [`TYPECHECK.md`](TYPECHECK.md), `evidence/gate_t_typecheck.py`,
`CHECKS-REPORT.md` §GATE T, `REVIEW.md` round 7.

---

## 2026-09-24 — Preparing the GitHub posting, and a claim I could stop conceding

**I tried / expected:** I went to push to
`nikbearbrown/info-7375-prompt-engineering-for-generative-ai/fall-2026/suketh-p`. I
assumed I had write access.

**What happened — four things I did not know:**

1. **I do not have push access.** `gh api` reports
   `{"pull": true, "push": false, "admin": false}`. A direct push is impossible; the
   route is fork → branch → PR. Two forks and one open PR already exist on the repo, so
   that is how it is being done in practice.
2. **The path is `fall-2026`, not `fall-2025`.** The Canvas brief says
   `fall-2025/first-name-last-initial/week-01-video/` and I had flagged that as an
   unreconciled conflict. The live repo settles it: `fall-2026/`, one folder per person,
   and `suketh-p/` already exists with a stub README the instructor seeded.
3. **CI runs on every pull request** — `.github/workflows/course.yml` executes
   `scripts/validate_course.py` on Python 3.11, 3.12 and 3.13. A submission that breaks
   it lands with a red X on a category explicitly graded for *proper* posting. I ran the
   validator locally with my folder in place: **exit 0, 13 tests OK**.
4. **No classmate has submitted yet.** Every other `fall-2026/*` folder is still the stub
   README.

**The refinement that came out of it.** Checking the CI matrix made me run my evidence
under more than one interpreter — and that is something `FACTCHECK.md` had explicitly
*conceded*: "Not claimed: that these figures reproduce on any other interpreter." It was
an honest concession, but it was a **testable** claim I had simply never tested.

So I wrote `evidence/cross_check.py`. Every figure the film displays — the weights, the
distribution, the `1.1102230246251565e-16` difference, the boundary cases, the seeded
counts `[102, 268, 630]` — is **byte-identical across CPython 3.10.19, 3.12.7, 3.13.3 and
3.14.6**. And 3.14.6 is the interpreter **Chapter 1 records its own run on**, so this also
checks my numbers against the book's published environment, not just my own.

**What I was careful not to do:** turn that into "platform independent". All four
interpreters run on one machine, one architecture. The script prints the platform and
says so in its own output, and FACTCHECK now states the claim at exactly that size.

**And I did it again, smaller.** I wrote "Three interpreters" into the script's scope
note. It found **four**. A hardcoded count in a script whose entire job is checking
numbers — the note is now generated from the actual run. That is the fifth time this
project has caught me asserting a figure I had not re-derived, and by now I read it less
as carelessness than as the default failure mode the film is about.

**What Claude contributed:** found the permissions and path facts with `gh`, ran the
validator, wrote `cross_check.py`, and caught the hardcoded "three".

**Evidence:** `evidence/cross_check.py`, `evidence/crosscheck-output.txt`,
`FACTCHECK.md` §"Claims deliberately NOT made" (now measured), `S7`.

---

## 2026-09-24 — The repo rejected my submission, and it was right to

**I tried / expected:** Stage the folder, run the repo's own validator as a formality,
open the PR.

**What happened:** `python3 scripts/validate_course.py` **exited 1**:

```
Non-Python implementation: fall-2026/suketh-p/week-01-video/components/ShiftedNotChanged.tsx
```

Not a warning — a hard failure, and `.github/workflows/course.yml` runs that validator on
**every push and pull request** across Python 3.11/3.12/3.13. Committing my Remotion
source would have put a red CI check on the submission, in the one category
(`GitHub version posting`) that exists specifically to assess *proper* posting.

And the validator is only enforcing what `AGENTS.md` already says: *"use an external
brutalist.art checkout for its Node/Remotion and Python packages, **never vendor that
stack into the course**."* I had read that line during the build and applied it to
`node_modules` — it also covers my own `.tsx`.

**The tempting fix and why I did not take it.** Renaming to `ShiftedNotChanged.tsx.txt`
slips past the extension check in one second. That is gaming a validator whose rule I
agree with: the point is keeping a Node stack out of a Python-and-Claude course, not
policing suffixes. Writing the workaround would have been a small dishonesty aimed at a
grader's automation.

**What I did instead:** dropped the `.tsx` and wrote
`components/README.md` (in the posted repo folder) — why it is not vendored (quoting both
AGENTS.md and the validator's actual source), where the file lives in the external
checkout, and the three excerpts a reviewer needs to judge the work: the no-hardcoded-
figures contract, the palette with the GHOST accessibility note, and the single frame
clock. The excerpts are **generated from the real file** at staging time, so they cannot
drift from it.

**Then the validator caught me a second time.** My new `components/README.md` linked to
`../../../AGENTS.md`. From `week-01-video/components/` the repo root is **four** levels
up, not three. My own link checker had reported "14 resolve, 0 broken" — because I ran it
*before* writing that file. The repo's validator found what my check had already passed.

**Final state:** `validate_course.py` exit **0**. CI will be green.

**What changed in my understanding:** I had been treating the submission as "my folder,
dropped into their repo." It is not — it is a contribution to a repository with a stated
contract and automated enforcement, and the contract disagreed with my layout. Reading
`AGENTS.md` as *rules for the course authors* rather than *rules for anything in this
tree* was the actual mistake.

**What Claude contributed:** ran the validator before proposing the PR rather than after,
read the rejection back to its source rule, and declined the `.tsx.txt` workaround when I
raised it.

**Evidence:** `scripts/validate_course.py` lines 22–26; `.github/workflows/course.yml`;
`components/README.md` (in the posted repo folder).

---

## 2026-09-24 — Six drifts is a process problem, not six accidents

**I tried / expected:** A last read-through before submitting. I expected to be tidying.

**What happened:** I counted how many times a number in the paperwork had drifted from
the thing it described. **Five.** The test-survivor claim, the body-beat word counts, the
"no component hardcodes a number" overreach, "two digits out of sixty", and "Three
interpreters" in a script whose whole job is checking numbers. Every one was found by
accident — because I happened to run the thing, or because an unchanged duration looked
suspicious.

Five accidents is not luck running out. It is the absence of a check.

**What I did:** Wrote `evidence/doc_consistency.py`. It derives runtime, caption-cue
count, GATE T tally and test count **live** from `beat_sheet.json`, the `.srt`,
`TYPECHECK.md` and the test file, then asserts the seven current-state documents agree.

It found a **sixth** on its first run: `README.md` still said the master was `195.44 s`
when it is `195.16 s`. That figure had survived nine rounds and three find-and-replace
sweeps.

**The design decision worth defending.** `REVIEW.md` and `FRICTIONAL.md` are *dated logs*.
They quote 195.46 s, 111 cues, 0/3/27 — all true on the day they were written. The easy
implementation would have "fixed" those too, and that would have been the worst possible
outcome: a review log that edits its own history is not evidence of a review. So both
files are **exempt by design**, each now carries a current-state header at the top, and
the script verifies *that header* instead of policing the entries beneath it.

**What changed in my understanding:** I had been treating each drift as a small slip to
correct. Six of them says the artifact and its description were never mechanically
coupled — the documents were hand-maintained prose about a thing that kept changing
underneath them. That is the same shape as the film's own argument: a fluent description
and a supported one are different objects, and only one of them is checked.

**What Claude contributed:** counted the drifts, wrote the checker, and argued for
exempting the dated logs when I was ready to normalise them.

**Evidence:** `evidence/doc_consistency.py`, `SOURCES.md` §5.14, the current-state headers
at the top of this file and `REVIEW.md`.

---

## 2026-09-24 — My tooling fabricated a quotation, and I nearly published it

**This is the most serious error in the project**, so it gets its own entry rather than a
line in a list.

**What happened:** Staging for GitHub, I ran a script to rewrite paths for the new folder
depth. One rule changed every `fall-2025/…/week-01-video/` into
`fall-2026/suketh-p/week-01-video/`. Comparing the Canvas and GitHub copies before
submitting, I found what that rule had done to **this file**. The GitHub copy read:

> *"The Canvas brief says to post under `fall-2026/suketh-p/week-01-video/`."*

**Canvas never said that.** It says `fall-2025/first-name-last-initial/week-01-video/` —
that discrepancy is the entire point of the entry it appeared in. The rewrite didn't just
introduce an error; it **fabricated what a source document said**, and turned a passage
about a real conflict into a self-contradiction. In the Frictional log. Which exists
specifically to be an honest record, and which the AI policy says must not contain
fabricated citations.

**Why it happened.** A find-and-replace cannot tell a *navigation instruction* ("run this
from the posted folder at …" — safe, and correct, to update) from a *quotation of a
source* ("Canvas says …" — must never change). I wrote one rule and it treated both the
same.

**What I did:**

1. **Removed the rule entirely.** Retargeting is now link depth and the video note —
   nothing else. The two genuine navigation instructions were fixed **at the source**,
   so both the Canvas and GitHub copies are right without any rewriting.
2. **Added an invariant to the staging step.** After normalising link depth, every
   staged document must equal its source except for the known, additive video section.
   Any other difference fails the stage.
3. **Proved the guard works** instead of assuming it: I reintroduced the original
   falsifying rule into a copy and ran the check. It caught **all four** changed lines —
   both quotations, before and after. A guard I have never seen fail is a claim, not
   evidence.

**What changed in my understanding:** every earlier drift in this log was a number that
fell *out of date*. This was different in kind — a tool I wrote produced a *false
statement about a source* and would have put my name on it. The film argues that fluent
output and supported output are different objects. My own staging script produced fluent,
plausible, wrong text about what a document said, and nothing about its output looked
wrong. I only caught it because I diffed the two copies before submitting.

**What Claude contributed:** noticed the Canvas/GitHub copies differed where they should
not, traced the difference to the substitution rule, removed it, and wrote and
mutation-tested the invariant.

**Evidence:** the staging invariant; the verbatim quotations at the two passages above
(`grep "The Canvas brief says" FRICTIONAL.md`).

---

## `[MINE — to complete after watching the cut]`

These are the entries the rubric wants from me, not from the assistant. I complete them
after watching the full review cut with sound, and before I submit:

- **The change I requested after watching, and how it improved understanding rather than
  appearance.** Timestamp, the problem in plain language, what I asked for, and what the
  re-render fixed. (The prerequisite asks for exactly this, and
  [`REVIEW.md`](REVIEW.md) is where the timestamped version goes.)
- **My unaided explanation of why the cancellation is exact but the floats still differ.**
  Written without re-reading B04 or B06.
- **What I still cannot defend.** The brief warns a TA may ask me to explain any part of
  the video, the beat sheet, or the build. The honest answer today: I can defend the
  algebra, the boundary, and the beat structure. The part I would struggle with is the
  Remotion motion math inside the components — Claude wrote that, I read it, and I have not
  yet written one from scratch.
