# FACTCHECK.md — gistgap-pitch

One row per factual claim in the narration (`beat_sheet.json`). Every verdict is
PENDING until Prasad verifies it against the cited source; the final export must not
run before every row reads PASS, CORRECTED or EXEMPT. B01 (a hypothetical) and B14
(the title) make no factual claim.

Sources:

- **Brief**: `PROJECT-BRIEF.md` in this folder (committed 50cecd6).
- **AP2 spec**: Google's Agent Payments Protocol (AP2) v0.2 specification, main page only.
- **AP2 post**: Google's AP2 announcement post, September 16, 2025.
- **Repo README**: the Razorpay buildathon repository "Mandate Mirror", README only.
- **git log**: `git log --format='%h %s' -- fall-2026/prasad-s/`, run 2026-10-09; four of Prasad's commits (1a6aa5b, 2eb73eb, 2a1f40f, fe9c16c), newest first, frozen as literal text in `make_sheet.py`.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02 | The exact signed terms are called a mandate. | PENDING | AP2 spec; Brief §1 | — |
| 2 | B03 | The $50 / $500-a-month contract is an invented example. | PENDING | Brief §5 (all mandates and summaries constructed) | — |
| 3 | B04 | GistGap will be a web demo that tests whether the text shown to someone approving an agent's payment matches the signed terms. | PENDING | Brief §1 | — |
| 4 | B04 | It will be a public GitHub repository with a demo page, a test set, and a results table. | PENDING | Brief §1 | — |
| 5 | B05 | It is for whoever owns an agent-payment approval screen. | PENDING | Brief §2 | — |
| 6 | B05 | Before launch, they will be able to test, with synthetic data, whether the text drops or changes a cap, an amount, an expiry, or a recurrence. | PENDING | Brief §2 | — |
| 7 | B06 | For AP2, I read the announcement post and the main spec page. | PENDING | Brief §2(a) | — |
| 8 | B06 | For the buildathon repo, I read its README only. | PENDING | Brief §2(b) | — |
| 9 | B06 | AP2 defines how mandates are signed and checked. | PENDING | AP2 spec; AP2 post; Brief §2(a) (verifiers check closed mandates against the constraints in open ones) | — |
| 10 | B06 | The repo checks payments against its own mandates. | PENDING | Repo README; Brief §2(b) (checks each payment request against a mandate and the spend already used) | — |
| 11 | B06 | In what I read, neither tests the text a person is shown. | PENDING | AP2 spec; Repo README; Brief §2 | — |
| 12 | B07 | The target role is product manager for AI agent products; the reader is a hiring manager or an engineer. | PENDING | Brief §3 | — |
| 13 | B07 | In the first sixty seconds, they will click three constructed examples and read the results table. | PENDING | Brief §3 | — |
| 14 | B08 | It will show four skills from this course: prompt contracts, verification, evaluation, and source grounding. | PENDING | Brief §4 | The brief lists the four skills; "from this course" needs a course source (syllabus or lesson list). |
| 15 | B08 | The evidence will be the test set, the results table, dated Claude outputs, and predictions committed before each run. | PENDING | Brief §4 | — |
| 16 | B08 | It will not show that this works on real payments. | PENDING | Brief §4 | — |
| 17 | B09 | In scope: five fields (amount, merchant, spending cap, expiry date, one-time versus recurring). | PENDING | Brief §5 | — |
| 18 | B10 | Out of scope: real signing, real payments, protocol compliance, and checking what the user originally asked for. | PENDING | Brief §5 | The brief says "signature verification"; the narration says "real signing". |
| 19 | B10 | The first run is ten constructed mandates, three with planted errors; it ran if it flags exactly those three; the prediction is committed first. | PENDING | Brief §5 | — |
| 20 | B11 | AP2 requires the display to be non-agentic. | PENDING | AP2 spec: "The following role MUST be non-agentic: Trusted Surface." Quoted from the v0.2 spec main-page text Prasad supplied; still PENDING verification against the live page. Also Brief §2(a) and §6 | — |
| 21 | B11 | I haven't examined any implementation. | PENDING | Brief §6 | — |
| 22 | B11 | Matching text is brittle, because the same amount can be written several ways. | PENDING | Brief §6 (the checker may miss paraphrases such as "five hundred" versus "$500") | — |
| 23 | B12 | Payments and agent-payment protocols are new to me. | PENDING | Brief §7 | — |
| 24 | B12 | I already have the Assignment 1 film. | PENDING | Brief §4 and §7; `fall-2026/prasad-s/week-01-video/` | — |
| 25 | B12 | The commit trail is on screen. | PENDING | git log (B12 rows): four of Prasad's commits in `fall-2026/prasad-s/` (1a6aa5b, 2eb73eb, 2a1f40f, fe9c16c), frozen 2026-10-09 in `make_sheet.py`; on screen labelled "COPIED from git log, Oct 9 (re-typeset)" | — |
| 26 | B13 | Today the brief, the beat sheet, and this film exist. | PENDING | Brief, EXISTS TODAY; this folder | The brief's EXISTS TODAY list is the folder skeleton, the brief, and the toolkit; the beat sheet and film are new since. |
| 27 | B13 | The project itself does not exist yet; it will be the generator, the checker, the test set, the demo page, and the results table. | PENDING | Brief, WILL EXIST | — |
| 28 | B04 | (picture) B04 shows a constructed example of a flagged mismatch: the cap row differs and is crossed and flagged; it is not output from a real checker. | PENDING | Brief §5 (all mandates and summaries constructed); `scenes.py` B04_Browser; label "CONSTRUCTED · WILL EXIST" | — |
| 29 | B10 | (picture) B10 shows an illustration of the planned first test (ten mandates, three planted errors, three flagged), not a result. | PENDING | Brief §5; `scenes.py` B10_ScopeTest; label "CONSTRUCTED · WILL EXIST" | — |
| 30 | B12 | (picture) The B12 rows are COPIED from `git log` on Oct 9 and re-typeset (wrapped, set in the film's serif), not a screen capture. | PENDING | git log; `make_sheet.py` B12_ROWS; label "COPIED from git log, Oct 9 (re-typeset)" | — |
