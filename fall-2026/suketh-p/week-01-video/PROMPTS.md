# PROMPTS — week-01-shifted-not-changed

## Open slots: NONE

GATE F asks for beat-prefixed prompts for open slots. **This reel has no open slots.**

There is no `pantry/` manifest to generate, because every beat renders natively as a
deterministic Remotion scene. No image generation, no AI video, no stock footage, no
screen capture, no human-supplied asset — so there is no generation prompt to record and
nothing to shop for. REBUILD LAW is satisfied by construction: there was never a
screenshot to replace.

The `pantry/` directory exists and is empty. That is the finished state, not a pending one.

---

## What this file records instead

Two things worth keeping for reproducibility.

### 1. The two prompts that appear *on screen* (they are content, not build instructions)

These are shown in the film itself and read aloud. They are reproduced here verbatim so a
reviewer can run them without transcribing from video.

**B05 — the verification ask** (shown typed into the composer; its result is B06):

```text
Import Chapter 1's probabilities() unmodified. Run it on [1, 2, 3], and separately
compute the same softmax by direct exponentiation with no max-subtraction. Print both
vectors at full precision and the maximum absolute difference. Round nothing.
```

This is the prompt that produced `evidence/verify_claims.py` claim 2 — the beat's result
is a real recorded run, not a dramatization.

**B09 — the handoff prompt** (HANDOFF LAW: read aloud verbatim, then discussed):

```text
Chapter 1's softmax subtracts the largest score before exponentiating, and this is
widely called 'numerically stable'. Find me an input where the subtraction does NOT
save the result. Tell me which end of the float64 range breaks and why the subtraction
cannot reach it. Then state the narrowest claim the subtraction actually supports —
and say what evidence would be needed to support the wider one.
```

Why this prompt rather than a bland "learn more about softmax": it extends the episode's
move into the viewer's own hands. It is answerable, it has a checkable answer (underflow
at the small end; the cliff near −746 on float64), and it rewards a prediction made before
running. The narration asks the viewer to commit to where the floor sits first — and then
to notice whether Claude names underflow or merely repeats the word *stable*.

### 2. The build prompt

The single paste-ready prompt that rebuilds this film end to end lives in
[`BUILD-PROMPT.md`](BUILD-PROMPT.md), per the SKILL.md's step 6 ("a reel without its build
prompt is unfinished"). It is not duplicated here.

---

## Beat-by-beat: what filled each slot

Recorded so that "no open slots" is auditable rather than asserted.

| Beat | Slot filled by | Needed a human asset? |
|---|---|---|
| B00 | `ClaudeComposerAsk` (toolkit), props only | No |
| B01 | `BrutalistHesitantWriter` (toolkit), props only, seeded | No |
| B02 | `ShiftOverflow` — authored for this reel | No |
| B03 | `ShiftPipeline` — authored for this reel | No |
| B04 | `ShiftCancellation` — authored for this reel | No |
| B05 | `ClaudeComposerAsk` (toolkit), props only | No |
| B06 | `ShiftReceipt` — authored for this reel | No |
| B07 | `ShiftBoundary` — authored for this reel | No |
| B08 | `ClaudeVerdictArtifact` (toolkit), props only | No |
| B09 | `ClaudeComposerAsk` (toolkit), props only | No |
| B10 | `ShiftOutro` — authored for this reel | No |

Every authored component takes its figures as **props**, sourced from
`evidence/run-output.txt`. The components also carry those values as Zod schema defaults
so each scene previews standalone in Remotion Studio, but the beat sheet overrides all of
them at render time — so a wrong figure is a beat-sheet edit and never a component edit,
and re-running the evidence script is enough to re-verify the whole film.
