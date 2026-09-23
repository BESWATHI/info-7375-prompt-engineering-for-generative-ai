# Ch1 components — the chassis and the eight scenes

These are the React/Remotion components written for this reel. They are **copies**;
the live ones sit in the Brutalist toolkit at `runtime/remotion/src/scenes/`, which is
where the render pipeline looks for them.

## Installing them into a fresh toolkit clone

1. Copy all nine `.tsx` files into `runtime/remotion/src/scenes/`.
2. Register the eight compositions in `runtime/remotion/src/Root.tsx`, inside a
   `<Folder name="Ch1-Pretraining">`. Each needs the `calculateMetadata` hook — without
   it, any beat whose audio is shorter than the registered `durationInFrames` is
   silently truncated and loses its late reveals (`FRICTIONAL.md` #13):

   ```tsx
   <Composition id="Ch1PretrainLogits" component={Ch1PretrainLogits}
     durationInFrames={720} fps={30} width={1920} height={1080}
     schema={ch1PretrainLogitsSchema} defaultProps={ch1PretrainLogitsSchema.parse({})}
     calculateMetadata={({props}) => ({
       durationInFrames: Math.max(1, Math.round(props.durationS * 30)),
     })} />
   ```

3. `npx tsc --noEmit -p .` then `./art scene-index` — a component missing from the index
   cannot be found by the scene search, including by you next week.

## The chassis

`Ch1Chrome.tsx` is the shared frame. It exports `Ch1Stage`, which owns the reel's
furniture so no scene repeats it: the `#F2F0E9` ground, the spark line (SPARK-LINE LAW),
the `CONSTRUCTED EXAMPLE` honesty banner, and the low-opacity course bug (LOGO LAW) —
all positioned from the shared `SAFE` inset rather than nudged by pixels. It also
exports the timing helpers (`cue`, `remap`, `ease`, `useBeatProgress`) and the
primitives `Ch1Token` and `Ch1Bar`.

Every scene is a **pure function of normalized beat progress**, which is what lets the
pipeline conform it to the measured audio. Nothing reads a wall clock or a frame number
directly.

| Component | Beat | What it shows |
|---|---|---|
| `Ch1Chrome.tsx` | all | the chassis — ground, spark line, honesty banner, bug, helpers |
| `Ch1PretrainCorpus.tsx` | B02 | the false corpus line, tokenized; the slot opens after `green` |
| `Ch1PretrainLogits.tsx` | B04 | raw logits and `exp(z)`; bars drawn from `exp(z)`, not `z` |
| `Ch1PretrainSoftmax.tsx` | B05 | the division, and a stacked unit bar that tiles to exactly 1 |
| `Ch1PretrainTarget.tsx` | B06 | the one-hot target beside the truth vector nothing builds |
| `Ch1PretrainLoss.tsx` | B07 | the sum collapsing to one term; incurred vs counterfactual loss |
| `Ch1PretrainGradient.tsx` | B08 | `p − y` per row, with direction arrows; column sums to zero |
| `Ch1PretrainBoundary.tsx` | B09 | what this does not establish |
| `Ch1PretrainOutro.tsx` | — | title-restate outro; **used by the 3:16 cut only** |
| `Ch1PretrainHook.tsx` | B00 | Act 1 — the false sentence in plain English, the question, the guess pause |
| `Ch1PretrainLadder.tsx` | B03–B07 | Act 2 — all five softmax steps in ONE component, driven by `step` (1..5) |
| `Ch1PretrainContrast.tsx` | B08 | Act 3 — the same model against a true corpus; both answer keys side by side |
| `Ch1PretrainTakeaway.tsx` | B11 | Act 6 — one sentence, plus the title restate and credit rail |

## Why a custom outro

`ClaudeTitleOutro` hardcodes the `@NikBearBrown` handle with no prop override, and
`OUTRO-LOCK.md` scopes it to claude-liam reels: *"Other channels use their own outro
components — never this one."* `Ch1PretrainOutro` is this channel's own, keeping the
law's substance — exact title restate, poster-plain serif, terracotta period, handle
beneath.

---

## The 2026-09-23 six-act cut

Twelve beats. The beats and the components they use are listed in `../SHOTLIST.md`.
Two components are registered and indexed but **not used** by this cut:
`Ch1PretrainGradient` (the `p − y` beat, which is not one of the six acts) and
`Ch1PretrainOutro` (act 6 carries the outro function). They are left in place because a
component missing from the scene index cannot be found by anyone later.

### `Ch1PretrainLadder` is the load-bearing one

It renders all five softmax steps. The beat sheet varies only `step` and `stepNote`;
everything numeric comes from `softmax_values.json` via `build_beat_sheet.py`. Columns
already established render at 0.62 opacity (the `CH1.DIM` floor is 0.45, so they stay
fully readable); the column being introduced takes the terracotta header and full-weight
values.

Two layout constraints are load-bearing and worth not breaking:

- **Column widths must sum inside SAFE.** `250 + 150 + 200 + 200 + 380 + 190 + 150 =
  1520px`, plus `6 × 26px` of gaps = `1676px`, inside SAFE's `1728px`. The `÷ Σ` column is
  380px and its cell renders at 32px rather than 40px, because `1.0000 ÷ 1.0792` at 40px
  is ~340px and overflowed a 300px column into `p` — a collision GATE V cannot detect
  (see `../FRICTIONAL.md` #26).
- **`durationS` must come from the measured audio.** Without the `calculateMetadata` hook
  a beat whose audio is shorter than the registered `durationInFrames` is silently
  truncated and loses its late reveals (`../FRICTIONAL.md` #13).
