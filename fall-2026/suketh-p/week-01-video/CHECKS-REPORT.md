# CHECKS-REPORT.md — week-01-shifted-not-changed

Written **before** the first compile, per the PROOF GATE in
`skills/make/ai-explainer/SKILL.md` ("CHECKS-REPORT — write before the slate, not after").

Measured on audio lock, 2026-09-15. Total runtime **195.16 s (3 m 15 s)** — inside the
brief's 2–4 minute target with no padding beat.

## Beat classification

**11 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

Every beat names its on-screen artifact in `shot.show` as an ordered list of visual
events, so no beat is a bare CARD and none is a PUNT. There are no slates: every visual
is renderable in this environment.

| Beat | Act | Class | On-screen artifact | Audio |
|---|---|---|---|---:|
| B00 | ASK | SHOW | Claude composer; ask types, three result lines land | 20.18 s |
| B01 | BLUF | SHOW | Hesitant writer; `stable` → `overflow-safe` | 16.36 s |
| B02 | THE BREAK | SHOW | Exponent axis, float64 ceiling, real `OverflowError` card | 20.67 s |
| B03 | THE MOVE | SHOW | Four-stage table; score → shifted → weight → probability | 19.61 s |
| B04 | THE PROOF | SHOW | The shared `exp(−m/T)` factor struck through on both lines | 18.69 s |
| B05 | ASK | SHOW | Composer; the verification prompt (ask half of ask→result) | 9.13 s |
| B06 | THE RECEIPT | SHOW | Two output vectors aligned; the 2 differing digits marked | 20.50 s |
| B07 | THE BOUNDARY | SHOW | Descending score rail; hard-zero cliff, then the closed form `−1075·ln 2` | 20.57 s |
| B08 | VERDICT | SHOW | Claude artifact page; four verdict lines stagger | 21.40 s |
| B09 | HANDOFF | SHOW | Composer, greeting `Your turn.`; prompt read aloud | 18.92 s |
| B10 | OUTRO | SHOW | Title restate, author, synthetic-narration disclosure | 9.13 s |

## Teaching arc

```
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples ✓** — B01 states the whole claim in one breath before any
  specific number appears; B02 supplies the motivation (why the subtraction exists at all)
  before B03 performs it.
- **WORKED EXAMPLE ✓** — B03 walks `[1, 2, 3]` through every intermediate value to the
  finished distribution, with the denominator shown. Nothing is skipped or summarized.
- **FALSIFIABILITY ✓** — B07 is an input where the popular claim about this code is false:
  `probabilities([0, −800])` → `[1.0, 0.0]`. The claim is narrowed on screen from
  "numerically stable" to "overflow-safe", and the boundary is shown in closed form
  (`−1075 · ln 2`) so it is predicted rather than merely observed.
- **SCAFFOLDED TASK ✓** — B09's prompt is read aloud verbatim and then discussed (what it
  does, what to look for in the answer), and it asks the viewer to write a prediction
  before running it. Per HANDOFF LAW, a prompt that only appears on screen is a defect.
- **BOOKENDS ✓** — cold open (B00) → hesitant-writer BLUF (B01) → body → verdict page
  (B08) → handoff (B09) → title-restate outro (B10). Typing appears in exactly three
  beats: B00 (the ask), B01 (the overview being thought through), B09 (the viewer's
  prompt).
- **NO-SOURCE-NO-VERDICT ✓** — every figure on screen is traceable to
  `evidence/run-output.txt`, the recorded output of `evidence/verify_claims.py` run
  against the course's unmodified `lessons/01-randomness-and-first-prompts/code/main.py`.
  Figures are beat-sheet props that override the components' schema defaults.

## Law compliance

| Law | Status | Note |
|---|---|---|
| COLD OPEN | ✓ | B00 is `ClaudeComposerAsk` with RESULT lines — the ask lands answered. |
| EXECUTIVE-SUMMARY (Beat 2 ≥ 9 s) | ✓ | B01 measured **16.36 s**. `lead_silence_s: 0.8` authored (see note below). |
| Hesitant-writer correction | ✓ | `stable` → `overflow-safe`, verified firing on screen. The trigger **must be a single whitespace token** — a multi-word phrase silently never matches (see `REVIEW.md` R1-1). Corrected sentence reads "Subtracting the max makes softmax overflow-safe. Every number in the middle changes. The answer does not." — stands alone as the reel's claim, no dangling fragment. |
| ILLUSTRATE | ✓ | UI appears only at B00, B05 (ask half of an ask→result pair), B08 (verdict artifact), B09 (handoff). All five body beats illustrate their concept. No two consecutive beats share a visual scheme. |
| ASK → RESULT | ✓ | One genuine receipt pair: B05 asks for the two-path check, B06 shows what it returned. |
| SHOW-DON'T-TELL / PPT TEST | ✓ | No beat could be exported as a static slide: B02 draws an axis and stamps an error, B03 reveals four columns, B04 strikes a factor out, B06 marks digits, B07 draws a cliff. |
| NARRATION BUDGET (~45–70 words, body) | ✓ | Measured B02–B07 from `beat_sheet.json`: **70 / 68 / 70 / 34 / 69 / 70**. Every body beat inside the 45–70 target; B05 (34) is an ask micro-beat, short by design. Bookends exempt. Counts are computed by GATE T §8.5 on each run, not estimated — an earlier version of this row listed numbers I had not measured (`SOURCES.md` §5.7). |
| SPARK-LINE | ✓ | Every illustration beat carries one short serif line; none shows a lone asterisk. |
| FILL-THE-CANVAS | ✓ | Verified at Gate V: all 22 sampled frames clear the 55% bbox floor. B01 and B10 failed the first two rounds and were fixed at the root — see `REVIEW.md` R1-2, R3-1. |
| LOGO | ✓ | No channel logo file applies; per the law's fallback the author's wordmark renders as a low-opacity corner bug inside title-safe on every body beat. |
| OUTRO | ✓ | Title restated poster-style with the terracotta period. Own card — see below. |
| DOODLE-BANNED | ✓ | No `DoodleScene` / `DoodleChart`. |
| REBUILD (no screenshots) | ✓ | Every visual is a native animated Remotion scene; no lifted images, no screen recordings. |
| DOUBLE-CHECK | ✓ | Chapter 1 fact-checked and rewritten, not parroted; two corrections logged in `SOURCES.md`. |
| Free pipeline / never publish | ✓ | Kokoro `am_onyx` local, $0.00, no API key, no upload. |
| VISUAL QC | ✓ | **BLOCKER 0 · MAJOR 0** across 22 frames (`_qc/REPORT.md`). Took six rounds; two defects were found by reading frames, not by the gate. |

**Two deviations, both deliberate and logged in `FRICTIONAL.md`** (a third — the
unrunnable GATE T — was resolved on 2026-09-20 by implementing it; see below):

1. **`lead_silence_s` is authored but inert.** The law requires it on B01;
   `grep -rn "lead_silence" runtime/scripts/*.py` shows the free toolkit's audio script
   never reads it. Kept in the sheet for doctrine, and the ≥9 s window was instead earned
   by writing B01 long enough — measured 16.36 s.
2. **The locked `@NikBearBrown` outro card is not used.** `OUTRO-LOCK.md` hardcodes that
   handle and scopes the card to `claude-liam-*` reels ("Other channels … NEVER get this
   card, handle, or mascot"). Stamping it on a student submission would imply channel
   endorsement, which the course prerequisite forbids. This reel therefore ships its own
   `ShiftOutro`, omits the IN-FOR-BEAR narration line, and carries the synthetic-narration
   disclosure on the card itself.

## GATE T — implemented, because the shipped script is missing

The SKILL.md calls `scripts/type_check.py` mandatory ("ALWAYS RUN"; no build "may report
success while `TYPECHECK.md` has any FAIL"). That script is **not in the public
checkout** — there is no `scripts/` at the toolkit root. Rather than keep recording that
as an excuse, this reel implements the checkable parts:
`evidence/gate_t_typecheck.py` → [`TYPECHECK.md`](TYPECHECK.md).

**Result: 0 FAIL · 1 WARN · 29 PASS.** It found three real defects on its first run:

| Found | Fix |
|---|---|
| `GHOST` on cream measures **1.98:1** — far below WCAG AA-large (3:1) — and was carrying the **synthetic-narration disclosure**, the one line that must be readable | All three `GHOST` text uses moved to `SOFT` (4.37:1). `GHOST` is now unused as a text colour, with a comment saying why. |
| `ACC` on cream is **2.74:1**, also under AA-large | Cannot be fixed: `CLAUDE-BRAND.md` forbids retinting a fidelity palette. Mitigated instead, and the mitigation is now **checked** (§8.3b): every terracotta element also differs by weight, size or a rule, so the accent is never the sole carrier of meaning. B03's focal cells were colour-only and gained `fontWeight: 700`. |
| Two §8.6 figures flagged as "not in any recorded run" | **False positive in my own check** — `0.3678794412` and `0.6652409558` are correct 10-dp roundings (the latter is verbatim Chapter 1's published table). The check now accepts a correct rounding of a full-precision recorded value, and says which. |

What it deliberately does **not** cover is stated in the script header and in
`TYPECHECK.md`: §8.2 overflow and §8.4 kerning need rendered frames and font metrics
(Gate V covers overflow), and §8.6 is verified as *wiring*, not pixels — confirming
legibility in the image would need OCR.

## GATE L — library-first

Searched before authoring, per GATE L. Genuine miss: the 610 registered scenes offered
leads (`HaiBrutalistE01Pipeline`, `MedhavyCodeBlock`, `ReqRingWord`) but each is
reel-local to another film with its content hardcoded behind a `sparkLine`-only prop.
Treated as a PUNT → design card, not a slate. Six parameterized components authored in
`runtime/remotion/src/ShiftedNotChanged.tsx`, registered in `Root.tsx`, and indexed with
`./art scene-index` (610 → **616 renderable**). All six verify as
`RENDERABLE 16:9` via `./art scenes --check`.
