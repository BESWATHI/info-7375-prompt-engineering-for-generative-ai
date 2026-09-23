# CLAUDE.md — nik-bear-brown/ (Professor Bear's example folder)

This folder is the instructor's public example work for INFO 7375, Fall 2026. It keeps the same process record students keep. **Every substantive change here is logged in `FRICTIONAL.md`, and every push adds a line to it.** The repo-root `AGENTS.md` still governs everything else.

## Rule 1 — log every substantive change in FRICTIONAL.md

Before you report a task in this folder as done, update `FRICTIONAL.md` in the same change set.

**Substantive** means anything a reader of the log would need in order to understand the work:
- a new or deleted file or folder (other than regenerated run output);
- a change to what a result says (a new run, a different count or verdict, a new snapshot);
- a change to the résumé, the facts file, a matching scheme, or any rule or setting;
- a bug found or fixed, here or upstream, that this folder's work depends on;
- a decision, a reversal, or something that went wrong.

**Not substantive:** typo, wording, or formatting fixes that don't change meaning; re-running something and getting the identical result. Leave those out rather than padding the log.

**How to log it:**
- **Same day, same work:** extend that day's entry. Add to *What happened*, *What I did*, and *Evidence and next step* as needed. Don't start a second entry for the same session.
- **New day or new piece of work:** add a new entry under `## Entries`, newest last, headed `### YYYY-MM-DD — <what it was>`, using the course's seven fields, verbatim and in order:
  - Date and what I was working on
  - I tried / expected
  - What happened
  - What I did
  - What Claude or another person contributed
  - What I understand now / still do not understand
  - Evidence and next step
- **Write what happened, not what was hoped.** Include what failed. Name the files and commands that serve as evidence. Never invent a prediction, a result, an approval, or an understanding the human didn't state.
- **Credit honestly.** Say what Claude Code did and what Professor Bear decided. Direction, choices, and approvals are his; if he hasn't reviewed something, say so.
- Keep the executive summary at the top current if the new work changes what the log "records so far."

## Rule 2 — one line per GitHub push

Every push that touches this folder adds a row to the `## GitHub pushes` table, **in the same commit being pushed**:

```
| YYYY-MM-DD | <commit subject, exactly as committed> |
```

- The note is the commit subject, copied exactly. The repo uses conventional subjects (`feat(fall-2026): …`, `fix(fall-2026): …`, `docs(fall-2026): …`).
- No commit ID in the row: a commit can't contain its own ID, and `git log` holds it.
- A push is not a substantive change by itself; it only gets its row. If the pushed work was substantive, Rule 1 already logged it.

## Pushing from this folder

- **Push only when Professor Bear says to.** Authorization covers that push, not later ones.
- Stage **only** `fall-2026/nik-bear-brown/`. The repo often has other uncommitted instructor edits; never sweep them in.
- Run `python3 scripts/validate_course.py` from the repo root before committing.
- End the commit message with the co-author line the session specifies.

## Privacy

This repo is public.
- The person here is **"Professor Bear."**
- No contact details, profile links, DOIs, grant tracking numbers, or other people's names, in the facts file, the résumé, the reports, or the log.
- No absolute local paths (`/Users/…`) in anything committed. Run tools with relative paths.
- `facts/professor-bear-cv.json` stays `attested: false` until he checks it himself.
