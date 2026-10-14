# SOURCES.md — agent-reliability-audit pitch film

## Executive summary

This document lists what this pitch is built on: the external source behind
its core metric, what data it uses (none private), what Claude contributed
versus what I decided, and the toolkit's own license terms. Read it to check
that nothing here is presented as original research when it isn't, and that
no private or restricted data appears anywhere.

## The core metric: pass@k vs. pass^k

The framing this entire project is built around — that pass@k is the
flattering, commonly-reported metric and pass^k (all-k-succeed consistency)
is the honest one almost nobody reports by default — is **not my own
discovery**. I found it via Claude's web search while researching this
project idea, in a 2026 agent-evaluation methodology article:

- **Source:** "Building an AI Agent Evaluation Pipeline: 2026 Methodology,"
  digitalapplied.com, published June 2, 2026 (retrieved and read directly
  via Claude's web search/fetch while researching this project idea).
- **What the source actually states** (verified by reading the article's
  own content, not just a search snippet): for "pass@3 vs. pass^3," it
  reports **97%** vs. **~34% for the same agent**, a **−63 percentage
  point gap**. These two figures are quoted directly from the source.
- **What I do NOT attribute to the source:** an earlier draft of this
  project's materials additionally stated the two figures imply a flat
  70%-per-trial success rate (mathematically consistent: 0.7³≈34%,
  1−0.3³≈97%) and described that 70% figure as if the source itself stated
  it. The source does not state a per-trial rate anywhere — only the two
  headline percentages above. That inferred 70% figure has been removed
  from the film's narration and from `PROJECT-BRIEF.md`; only the two
  directly-quoted figures (97%, ~34%) are used.
- **What is mine:** the decision to build a tool that actually reports
  pass^k by default against a real tool-using agent, and to pair it with a
  fault-injection harness — the article does not propose or describe this
  specific tool.

## Real alternatives checked

`PROJECT-BRIEF.md` names two real tools I looked at (not invented
competitors): LangChain's agent-evaluation documentation and OpenAI's
public Evals repository. Both were checked for whether they report pass^k
by default; as of this writing, neither does. This is a factual claim about
public documentation, checkable by anyone, not an assertion about a
private competitive analysis.

## Data used

- **`docs.python.org`** — public, official Python documentation. The demo
  agent's one tool fetches real pages from this source (scoped to
  `functools`, `itertools`, and `pathlib` for the standard-library
  reference pages). No authentication, no private data, no scraping beyond
  normal page fetches.
- **No real résumé, contact information, application data, or private
  conversation transcripts** appear anywhere in this submission, per the
  assignment's own data-privacy rule.
- **Reallocation Engine PR reference** (beat B07): the pull request named
  is real and public — `nikbearbrown/the-reallocation-engine` PR #3 — and
  contains no private data of mine beyond what was already built for that
  assignment's own submission (a fictional persona, not real personal
  information).

## What Claude contributed vs. what I decided

| Claude did | I decided |
|---|---|
| Searched for and found the real pass@k/pass^k methodology source, rather than inventing a framing | To build the project around this specific, cited distinction |
| Proposed several project-scope options (protocol-based ideas, then the reliability-auditor idea) | Which concept to pursue, and to reject the protocol-based options as riskier to finish in five days |
| Drafted `PROJECT-BRIEF.md`'s prose against the seven required questions | What each answer actually says; reviewed and can defend every claim in it |
| Proposed `docs.python.org` as the real tool target, scoped to three stable standard-library pages | Confirmed this scope; named the "page structure could change" risk explicitly |
| Drafted `beat_sheet.json`'s narration and `BUILD-PROMPT.md`'s commands | Will review and must be able to explain every beat and command before submitting |

No film has been rendered yet, no toolkit gates have run yet, and no
software for the actual `agent-reliability-audit` tool exists yet as of
this writing. This file will be updated once a build happens.

## Narration disclosure

The narration is a synthetic voice (Kokoro `am_onyx`, generated locally,
free), not my own recorded voice. It speaks in first person, as me, about
my own project — never as the toolkit's default instructor persona ("Liam,"
"Bear," or "in for Bear"), which does not appear anywhere in this film's
narration or on-screen branding. The outro bookend this toolkit normally
uses (`ClaudeTitleOutro`) is deliberately not used at all in this build,
specifically because its component hardcodes the handle `@NikBearBrown`
and ignores its own `handle` prop — confirmed by reading the component's
source directly rather than assuming. The film ends on a plain drawn beat
instead.

## Third-party software and licenses

- **Brutalist toolkit** (`nikbearbrown/brutalist.art`) — used per the
  assignment's instructions: free pipeline only (Kokoro narration, local
  Manim/Remotion rendering), no paid generation, no API keys.
- **Kokoro** (local, free TTS voice) — no ElevenLabs, no paid narration
  service, per the toolkit's own stated policy.
- No other third-party media, stock footage, or externally-licensed assets
  are used.
