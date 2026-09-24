# SOURCES.md — "Shifted, Not Changed"

**Author:** Suketh Produtoor · INFO 7375, Week 1
**Reel:** `week-01-shifted-not-changed`
**Built:** 2026-09-15

Per [`prerequisites/brutalist-video-sources.md`](../../../prerequisites/brutalist-video-sources.md):
what I used, what I made, what Claude contributed, and every third-party asset with its
licence.

---

## 1. Synthetic narration — disclosed

**Every spoken word in this video is synthetic.** It is
[Kokoro-82M](https://github.com/thewh1teagle/kokoro-onnx) voice `am_onyx`, generated
locally by `runtime/scripts/generate_audio_kokoro.py`. No API key, no cloud call, no voice
cloning, $0.00.

The voice is **not mine and does not claim to be**. It is not Nik Bear Brown's, and this
reel is **not** a @NikBearBrown / `claude-liam` episode:

- The narration deliberately **omits the IN-FOR-BEAR line** ("…this is Liam, in for Bear")
  that every worked example in the toolkit carries.
- The locked `@NikBearBrown` outro card, handle and mascot are **not used**.
  `OUTRO-LOCK.md` scopes them to `claude-liam-*` reels and states that other channels
  "NEVER get this card, handle, or mascot". This reel ships its own `ShiftOutro`.
- The disclosure appears **on screen** on the outro card, not only in this file.
- Nothing here implies endorsement by the instructor, the channel, Northeastern, or
  Anthropic.

This follows the prerequisite's rule verbatim: *"Do not imply a synthetic narrator is me,
Bear, or an official endorsement."*

## 2. The concept and its source text

| Item | Source |
|---|---|
| Concept | Chapter 1, Part 2 — §"The subtraction that changes nothing important" |
| Chapter file | [`chapters/01-randomness-and-first-prompts.md`](../../../chapters/01-randomness-and-first-prompts.md) |
| Reference implementation | [`lessons/01-randomness-and-first-prompts/code/main.py`](../../../lessons/01-randomness-and-first-prompts/code/main.py) — imported, **never modified** (AGENTS.md: "Do not modify reference solutions") |
| Chapter's own probability table | Chapter 1, §"Temperature is a concentration control", T = 1.0 row |
| Quoted on screen (B07) | Chapter 1: "Keep the tested claim narrower than the slogan 'numerically stable.'" — the one verbatim quote in the film, attributed on the card |

The algebraic cancellation shown in B04 is the chapter's own derivation, re-set as a
Remotion scene rather than reproduced as an image.

## 3. Every number on screen — and where it came from

Every figure the film renders is supplied as a **prop** from `beat_sheet.json`. The same values also appear as Zod schema defaults inside each component so a composition can be previewed standalone in Remotion Studio; the beat sheet overrides every one of them at render time. So a wrong figure is fixed in the beat sheet, never in the component. Each prop value was read out of one recorded run:

- **Script:** [`evidence/verify_claims.py`](evidence/verify_claims.py) — standard library
  only, offline, imports the course reference implementation by path.
- **Recorded output:** [`evidence/run-output.txt`](evidence/run-output.txt)
- **Environment of record:** Python 3.12.7 (CPython), macOS 26.6.2 arm64.

| Shown in | Figure | Claim it supports |
|---|---|---|
| B02 | `OverflowError: math range error` | verbatim exception from `math.exp(1000)` |
| B02 | `709.7827`, `1.797693e+308` | `ln(sys.float_info.max)` and `sys.float_info.max` |
| B03 | `[-2, -1, 0]`; `0.1353352832`, `0.3678794412`, `1.0`; total `1.5032147244` | the intermediates the shift rewrites |
| B03 | `0.0900305732`, `0.2447284711`, `0.6652409558` | matches the chapter's published T = 1.0 table to 10 dp |
| B06 | both 62-character vectors, differing at indices 19 and 60 | shifted path vs direct exponentiation, full precision |
| B06 | `1.1102230246251565e-16` | measured max absolute difference between the two paths |
| B07 | `9.85967654375977e-305`, `5e-324`, `0.0`, `0.0` | `probabilities([0, n])` for n = −700, −745, −746, −800 |
| B08 | `~1e-348` | the true share of the outcome that returns a hard `0.0` |
| B07 | `−1075 · ln 2 = −745.133219102`, `−746` | the cliff in closed form — derived, then confirmed by bisection to 9 dp. Source: [`evidence/boundary-output.txt`](evidence/boundary-output.txt) |

**Reproduce all of it:**

```bash
python3 evidence/verify_claims.py             # prints every claim beside its value
python3 evidence/boundary_analysis.py         # derives the cliff; shows what it costs
python3 -m unittest discover -s evidence -v   # 28 tests; fail if any figure drifts
python3 evidence/mutation_check.py            # proves those tests bite (4/4 caught)
python3 evidence/gate_t_typecheck.py          # GATE T -> TYPECHECK.md (0 FAIL)
python3 evidence/cross_check.py               # every figure, every python3.N on PATH
python3 evidence/doc_consistency.py           # the docs vs the artifact (0 mismatches)
```

**Captions.** `final/week-01-shifted-not-changed.srt` — 112 cues. Timing comes from the
toolkit's `align.py` word clock (faster-whisper word-level timing, sequence-aligned to the
known narration; 11 beats aligned, 0 fallback), converted to an SRT by
`evidence/make_srt.py`. The public toolkit ships the aligner but not the SRT writer, which
lived in the removed publishing module — so that script is mine. Captions are a sidecar,
never burned in.

**Nothing in this film is a constructed illustration**, so there is nothing to label as
constructed. The exponent axis in B02 is drawn to scale from the two real figures on it
(709.78 against a score of 1000); it is a diagram of measured values, not an invented
distribution. Chapter 1's own hypothetical answer-key counterexample is **not** used, and
no Claude conversation transcript is shown, quoted, or reconstructed anywhere in the reel.

## 4. What Claude contributed — portion by portion

The [AI policy](../../../prerequisites/ai-policy.md) requires identifying **which portions**
were AI-assisted and **describing the usage method**. Prose is too vague for that, so this
is per artifact. Claude Opus 5 via Claude Code, NEU access, one session 2026-09-15 plus an
iteration pass 2026-09-18. No direct API credits.

| Artifact | AI-assisted? | How I used it (the method) | What I checked myself |
|---|---|---|---|
| Concept choice | Shortlist AI, decision mine | Asked for candidates from Chapter 1's own list with an argument for each, then rejected the 665.24-vs-630 option as the one the cohort would converge on | Read Chapter 1 end to end; confirmed max-subtraction is the smallest of the three |
| `evidence/verify_claims.py` | Written by Claude | "Import the reference unmodified; print each claim beside the value it actually returns; round nothing" | Ran it; every probability cross-checked against Chapter 1's published T=1.0 table |
| The boundary finding (`[0,-800]` → `0.0`) | **Found by Claude** | After it established the denominator can never underflow, I asked the mirror question about the numerator; it swept the small end | Re-ran the sweep; confirmed −745 returns `5e-324` and −746 returns `0.0` |
| The derivation (`−1075·ln 2`) | Derived by Claude | Asked "is −746 arbitrary, or predictable from the float64 format?" | Confirmed by bisection to 9 dp; checked `2**-1074` and `2**-1075` independently |
| `evidence/boundary_analysis.py` | Written by Claude | Asked it to derive the cliff, measure what the boundary costs, and demonstrate the log-space remedy | Ran it; verified the remedy reproduces the reference to 1e-12 on `[1,2,3]` |
| `evidence/test_verify_claims.py` (28 tests) | Written by Claude | "One job per check; name the beat each test defends; no aggregate 'it works' test" | Ran them, then ran the mutation check below to confirm they bite |
| `evidence/gate_t_typecheck.py` | Written by Claude | "The SKILL.md calls GATE T mandatory and the script is missing — implement the parts you can check honestly, and state what you cannot" | Ran it; it failed on first run and found the disclosure contrast defect. Verified the WCAG maths by hand against the palette hexes |
| `evidence/mutation_check.py` | Written by Claude | Asked it to implement Chapter 1's Assessment 10 against my own suite | Ran it; **it corrected a claim I had accepted** — see §5.5 |
| `evidence/doc_consistency.py` | Written by Claude | "Five numbers have drifted between the docs and the artifact and I found every one by accident — write the check that should have existed from the start" | Ran it; it immediately found a sixth stale figure in this very submission (recorded in §5.14). Checked that it exempts the dated logs and the corrections ledger rather than policing their history |
| `evidence/cross_check.py` | Written by Claude | "FACTCHECK concedes the figures might not reproduce on another interpreter — that is testable, so test it and report the scope honestly" | Ran it; confirmed 3.14.6 (the chapter's own) was among those tested, and checked the scope wording does not overreach to other architectures |
| `evidence/make_srt.py` + captions | Written by Claude | Asked it to close the gap left by the toolkit's removed publishing module | Spot-checked cue timing against the audio |
| `beat_sheet.json` | Authored by Claude | SHOW blocks first, narration second, per SHOW-DON'T-TELL LAW | Read every narration line against `evidence/run-output.txt` |
| `components/ShiftedNotChanged.tsx` (6 scenes) | Written by Claude | Asked for parameterized scenes that take every figure as a prop | Read the props contract; confirmed the beat sheet supplies and overrides every figure-bearing default — and corrected my own over-broad wording, §5.8 |
| Visual QC (5 rounds) | Run by Claude | Asked it to read the sampled frames, not just the gate report | Reviewed the contact sheets; two defects were found this way that no gate reported |
| This file, `FACTCHECK.md`, `SHOTLIST.md`, `CHECKS-REPORT.md`, `BUILD-PROMPT.md` | Drafted by Claude | Asked for paperwork keyed to the specific laws in the SKILL.md | Checked each claim against the artifact it describes |
| `FRICTIONAL.md` / `REVIEW.md` — `[MINE]` sections | **Not AI.** Deliberately left blank | — | Mine to write after watching the cut; I will not have the assistant invent my reflection |

**What I did that is not in the table:** chose the concept, set the honesty constraints
(no channel branding, no impersonation, no fabricated run), decided what the evidence
supports, and own the decision to submit.

## 5. Corrections applied (DOUBLE-CHECK LAW)

The SKILL.md requires the source be fact-checked and rewritten rather than parroted, with
corrections logged here.

1. **"The two paths give the same numbers" → corrected before it was narrated.** The
   cancellation is exact in algebra, so I expected bit-identical floats. Measured, they
   differ by `1.1102230246251565e-16`. B06 now states "identical in algebra,
   indistinguishable in floating point" and shows the two digits that differ. Had this not
   been measured, the film would have asserted something false.
2. **"Numerically stable" → "overflow-safe".** The common gloss on max-subtraction
   overstates it. The film narrows the claim on screen and demonstrates the counterexample
   (B07, B08). This follows the chapter's own instruction to keep the tested claim
   narrower than the slogan.
3. **No model version numbers, no drifting counts.** Per DOUBLE-CHECK LAW the script avoids
   anything that dates the video. The only version stated is the Python interpreter, which
   is stated *because* the chapter makes a point of distinguishing a concrete execution
   environment from a universal repeatability claim.
4. **Scope kept narrow.** Chapter 1's temperature table, the stochastic-parrot argument,
   and the 665.24-vs-630 sampling comparison were all cut from the film. The sampling
   comparison survives only as one context line in the verification script. One concept,
   per the brief.

5. **"The sum-to-one tests survive removing the max-subtraction" → measured, and it was
   wrong.** I wrote that claim into `mutation_check.py` from reasoning, then ran it. The
   8 survivors are almost entirely the tests that never call `probabilities()` at all —
   the closed-form derivation tests and the raw `math.exp` overflow test. The script now
   **prints the survivor list from the run** instead of asserting it, so the claim cannot
   drift from the evidence again. The honest finding is sharper than the one I guessed:
   my derivation tests verify the mathematics and are blind to the implementation, which
   is a real coverage boundary in my own suite.

6. **The cliff went from discovered to derived.** The first cut stated `−746` as a swept
   result. It is `−1075 · ln 2 = −745.133219102`, confirmed by bisection to 9 decimal
   places, and `−746` is simply the first integer past it. B07 now shows the closed form.
   Predicting a number is stronger evidence than finding it.

7. **I published word counts I had not counted.** `CHECKS-REPORT.md` claimed the body
   beats ran "65 / 63 / 66 / 30 / 66 / 62 words". Measured from `beat_sheet.json` they are
   **69 / 67 / 72 / 35 / 71 / 67** — and two beats are 1–2 words over the soft 70-word
   target rather than comfortably inside it. The row is now marked ⚠ with the real
   numbers and computed from the sheet instead of asserted. Small, but it is the same
   failure mode as §5.5 and exactly what this film is about: a confident number that no
   one had checked.

8. **"No component hardcodes a number" → too strong, corrected.** I had written that in
   three files. Checking the source, the figures *do* appear inside the components as Zod
   schema defaults — that is how each composition stays previewable in Remotion Studio
   without a beat sheet. The accurate claim is narrower: the beat sheet supplies every
   figure as a prop and **overrides** all of those defaults at render time, which is what
   makes a wrong number a beat-sheet fix. Verified: B02 `logits`, B03 `rows`, B06 `rows`
   and B07 `steps` are all supplied explicitly. The wide version of the claim was the kind
   of sentence this film exists to object to.

9. **The synthetic-narration disclosure was nearly unreadable.** `GHOST` (`#B0AD9A`) on
   the cream stage is **1.98:1** — WCAG AA-large wants 3:1. That colour was carrying the
   disclosure on the outro card, which is the one line in this film with an ethical reason
   to be legible. I had chosen it by eye for "quiet" and never measured it, and it
   survived five rounds of visual QC because looking at it read as *appropriately subtle*
   rather than *failing contrast*. Moved to `SOFT` (4.37:1), along with the two other
   `GHOST` text uses. Found by `gate_t_typecheck.py`, which I only wrote because I was
   tired of recording the missing gate as an excuse.

10. **Terracotta was the only signal in B03.** `ACC` on cream is 2.74:1 and cannot be
    changed — `CLAUDE-BRAND.md` forbids retinting a fidelity palette. The mitigation is
    that the accent must never be the *sole* carrier of meaning, and B03's focal cells
    were exactly that: same size, same weight, distinguished only by hue. They now carry
    `fontWeight: 700`, and §8.3b of the gate checks the mitigation on all four accent
    beats rather than trusting it.

11. **The film broke `[1000, 1000]` and never showed it working.** B02 raised
    `OverflowError` to motivate the subtraction, then B03 switched to `[1, 2, 3]` and the
    motivating failure was never resolved on screen — the viewer had to take the fix on
    trust. This was the largest teaching gap in the film and I only saw it by reading the
    eleven narration blocks as one continuous script instead of beat by beat. B02 now
    holds the break and its resolution **side by side**: the real error on the left, and
    the same input returning `[0.5, 0.5]` on the right. That pair is Chapter 1's own
    canonical test — *"The lesson tests this choice with equal large scores, `[1000,
    1000]`, and expects `[0.5, 0.5]`."*

12. **"two digits out of sixty" was wrong.** The two vectors are 62-character strings
    containing **53** digit characters. I had said "sixty" from the string length, in a
    film whose subject is the difference between a figure and a rounded impression of
    one. Corrected to "two digits out of fifty-three."

13. **Two smaller overclaims in the narration, both fixed before re-recording.**
    B05 said *"I did not want to take my own proof on faith"* — the cancellation is
    Chapter 1's derivation, not mine; now "the algebra". B07 said the cliff sits at
    "minus one thousand seventy-five times **log two**", which is ambiguous spoken aloud
    (log base 10 vs natural log); now "the **natural** log of two". B03 stated
    "sixty-seven percent" as a value while the screen showed `0.6652409558`; now
    "**roughly** nine, twenty-four, and sixty-seven percent".

14. **A sixth number had drifted, and this time a script found it.** `README.md` still
    said the master was `195.44 s`; it is `195.16 s`. That one survived nine rounds and
    three separate find-and-replace sweeps. It was found by
    `evidence/doc_consistency.py`, written specifically because five earlier drifts
    (§5.5, §5.7, §5.8, §5.12, and the "Three interpreters" slip in `cross_check.py`) were
    each caught by luck rather than by method. The script derives runtime, cue count,
    GATE T tally and test count **live** and asserts the current-state documents agree.
    `REVIEW.md` and `FRICTIONAL.md` are exempt as dated logs — they are supposed to quote
    the numbers that were true on the day — so both now carry a verified current-state
    header instead, and the script checks that header rather than rewriting their history.

15. **My staging script falsified two quotations — the most serious error here.** A
    path-rewriting rule changed every `fall-2025/…` to `fall-2026/…`, including two places
    in `FRICTIONAL.md` that **quote** the Canvas brief. The GitHub copy would have claimed
    Canvas said something it never said. The rule is gone, navigation text is corrected at
    the source instead, and the staging step now asserts that staged documents differ
    from their sources only by link depth and the video note. The guard was verified by
    reintroducing the original rule and confirming it catches all four changed lines.

## 6. Third-party assets and licences

| Asset | Source | Licence / terms |
|---|---|---|
| Kokoro-82M voice model (`am_onyx`) | `kokoro-onnx` releases, model-files-v1.0 | Apache-2.0 (kokoro-onnx); model weights per upstream Kokoro-82M release |
| `brutalist.art` toolkit | [github.com/nikbearbrown/brutalist.art](https://github.com/nikbearbrown/brutalist.art) @ `ba2d0e0` | Per repository LICENSE. Used as an external checkout, not vendored into this repo (AGENTS.md). |
| `BrutalistHesitantWriter` (B01) | Toolkit component. Its own header credits an auto-converted `brik/base44` canvas component, author unknown — see the toolkit's `SOURCES.md`. | Used as shipped, props only; motion math untouched. |
| `ClaudeComposerAsk`, `ClaudeVerdictArtifact` (B00, B05, B08, B09) | Toolkit components | Used as shipped, props only. |
| EB Garamond | Google Fonts, installed by `./setup --install` | SIL Open Font License 1.1 |
| `ShiftOverflow`, `ShiftPipeline`, `ShiftCancellation`, `ShiftReceipt`, `ShiftBoundary`, `ShiftOutro` | **Mine** — written for this reel | Contributed to the toolkit checkout under its licence |
| `verify_claims.py`, `test_verify_claims.py`, `make_srt.py` | **Mine** — written for this reel | Standard library only |

**No** paid service, no stock footage, no AI-generated imagery, no screen recordings, no
lifted figures, no Higgsfield, no ElevenLabs. Total spend: **$0.00**.

## 7. Not included, deliberately

- **No YouTube upload.** The brief states no upload is required or expected, and the
  toolkit never publishes. The file is submitted, not posted.
- **No private conversation transcripts**, no credentials, no `.env`, no caches — per the
  GitHub-posting rubric's safe-sharing row.
- **No Manim.** Blocked in this environment and unused; all mathematics renders as
  Remotion. Recorded honestly per the prerequisite rather than hidden.
