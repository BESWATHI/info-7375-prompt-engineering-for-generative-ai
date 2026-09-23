# FRICTIONAL — Professor Bear's process log

## Executive summary

**What this is.** The honest process log for the work in this folder, written the way the course asks students to write theirs: what was tried, what went wrong, what changed, and who did what, the human or the AI.

**Why read it.** It's a real example of the log, not a constructed one. It shows the instructor's own work run through the same record students keep.

**What it records so far.** One working session on 2026-09-23: turning the CV into a facts file, and running the Reallocation Engine's job-board watcher on Figma with that CV. The session hit three points of friction. The first match looked wrong because it was wrong. The results didn't add up to the score because of a real bug. And the demo's first choice of résumé got replaced mid-session. Every push to GitHub is listed at the bottom with its date and commit note.

---

## Entries

### 2026-09-23 — greenhouse-watch demo on Figma, and the CV as facts

- **Date and what I was working on:** Building a small worked example in my course folder. It runs the Reallocation Engine's `greenhouse-watch` skill (new jobs on one company's board, matched to a résumé) so students can see the recipe-plus-prototype assignment done end to end.
- **I tried / expected:** A two-day watch on Figma's board, using a saved snapshot from 2026-09-19 as the first look and a live fetch on 2026-09-23 as the second. I expected a handful of new postings and one or two matches for an example student.
- **What happened:** Figma posted 11 new jobs in the four days and took down 3. For the example student Aarav, the one match was a **London** machine-learning job, flagged for a Boston F-1 student. The report's reasons for it also didn't add up: the lines summed to 6.0 and the score said 3.5. Partway through, I switched the demo to my own CV as "Professor Bear." With that résumé, **none** of the 11 new jobs matched. Treating the whole board as new, 3 of 160 matched, and the roles I'd actually look at (Designer Advocate, the agentic-experiences researcher) scored 0 and 0.5.
- **What I did:**
  - Had the skill's scoring checked against its rules. The score was right; the report hid one bonus line and printed the title credit twice.
  - Fixed the report lines in the skill and added a test proving the lines now add up to the score. The test failed on the old code and passes on the new; all 23 skill tests pass.
  - Replaced the example-student runs with Professor Bear runs.
  - Wrote the CV as `facts/professor-bear-cv.json`, with contact details, links, DOIs, grant numbers, and other people's names removed, and derived the matching résumé from it.
  - Linked the duplicate board downloads to the two snapshots instead of storing four copies.
- **What Claude or another person contributed:** Claude Code (Opus 5.5) ran every command, wrote the files, traced the scoring bug to its two causes, wrote the fix and the test, and drafted this entry. I chose the direction:
  - build something simple in my folder;
  - use the greenhouse-watch skill;
  - use my CV with personal information removed, as "Professor Bear";
  - keep the CV as a facts file;
  - keep this log, one line per push.

  I have not yet checked the CV conversion line by line; both JSON files say `attested: false`.
- **What I understand now / still do not understand:** A keyword scheme is honest but narrow. It explains every match, and it can't see that "teaches, runs workshops, builds AI tutors" describes an advocate. Its misses are exactly the roles I'd pick by hand, so the scheme is where students have to do the thinking. Still open:
  - whether the default scheme's rule of dropping every Director role is right for anyone but students;
  - how much a daily watch catches that a weekly one misses (only two snapshots so far).
- **Evidence and next step:**
  - Evidence: the demo is in `greenhouse-watch-demo/` (README, the run records and reports, both board snapshots) and the facts file is `facts/professor-bear-cv.json`. The skill fix and its test are in the-reallocation-engine repo, not yet pushed.
  - Next: attest or correct the CV conversion; write a Professor Bear scheme (hard location gate, no Director exclusion, teaching-to-advocacy phrases) and re-run; run a third live fetch to get a real daily diff.

---

## GitHub pushes

One line per push to GitHub: the date and the commit note. The commit ID for each push is in `git log`; a commit can't contain its own ID.

| Date | GitHub note |
|---|---|
| 2026-09-23 | feat(fall-2026): add greenhouse-watch Figma demo, Professor Bear CV facts, and Frictional log |
