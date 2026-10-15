# TYPECHECK.md — GATE T

Reel: `datasentry-pitch`  |  Checked: 2026-10-14T20:13  |  Overall: PASS  |  Beats checked: 19  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BIDEA | manim | light | min-size §8.1: min text-run height 69px >= floor 41px | PASS | — |
| BDEFS | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B00 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B01 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 72px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 58px >= floor 41px | PASS | — |
| B10A | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 58px >= floor 41px | PASS | — |
| BEND | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 19 | 0 |
| overflow §8.2 | 19 | 0 |
| contrast §8.3 | 19 | 0 |
| contrast-local §8.3b | 19 | 0 |
| bbox-overlap §8.6b | 19 | 0 |
| card-clip §8.13 | 19 | 0 |
| kerning §8.4 | 18 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
