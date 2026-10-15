# FRICTIONAL — honest build log (Final Project Pitch Film)

Dates are local. Each entry: what I tried → what broke or changed → what I did instead.

## 2026-10-11
- First direction: build the pitch on my Reallocation Engine recipe (PR #28, `swe-network-targets`),
  since its own TODO list was a ready roadmap.

## 2026-10-14
- **Deadline moved up to tonight 23:59.** The brief's five-day shape is compressed into one evening.
- **Changed the project** (the brief allows this): from the Reallocation Engine extension to
  **Source Check for Support AI**, a workflow that checks a support bot's policy answers against current
  policy before they are sent. Reason: I wanted a project that applies to companies in general, not
  only to the course's engine.
- **Researched real problems before choosing.** Most search results for "automation pain points" were
  vendor marketing, which the honesty rule doesn't let me use as evidence. I kept only sources I could
  stand behind: the *Moffatt v. Air Canada* tribunal ruling (Feb 2024), and the alternatives' own public
  pages, checked 2026-10-14.
- **Zendesk:** I could only find third-party guides describing Zendesk AI agents, not Zendesk's own
  docs, so the brief says that explicitly instead of making a claim about the product.
- My project folders were reorganised (`Week_1/`, `Reallocation_Engine/`), so I re-pointed the tooling
  copied from Week 1.
- **Kokoro audio padding hung.** `ffmpeg` waits on stdin when run in the background; I had left out
  `-nostdin`. Killed it and re-padded with `-nostdin`.
- **Disk at 92% again (16 GB free)** — the condition that made iCloud offload the toolkit last time.
  Noted; the run completed.
- **Gate B** rejected a strike-through line drawn across a label (B11). Replaced it with an ✕ beside it.
- **GATE T blocked the final three times** (B06 overlapping prop plates; BOUT terracotta contrast;
  BDEFS a row caught mid-animation, then 40 px lowercase words). Fixed each in the content, not by
  loosening the gate: the toolkit exempts its own outro by name, and I chose not to add my copy to that list.
- **My own frame check caught what no gate did:** the "proposed design" tag also sat on beats showing
  real things (alternatives, my skills, what exists today). Removed it there.

## 2026-10-14 — submitting
- The toolkit patch failed to apply to the newest upstream (`4115560`): upstream had changed the two
  smoke-test files. They now contain the same fix I had made, so I dropped those hunks; the scene changes
  still apply cleanly.
- My name still comes out "Mayunk" in Kokoro. Accepted for today; noted for later films.
