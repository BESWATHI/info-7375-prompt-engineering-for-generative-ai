# CONTRACT.md — Job-Search Agent 1

Written by Swathi Baba Eswarappa, 2026-10-25, before any code was written.
The decisions below are mine. Claude (chat) helped me phrase the rule from the
choices I made; the failure statement is in my own words.

## In
- Board: Databricks, via the public Greenhouse endpoint
  https://boards-api.greenhouse.io/v1/boards/databricks/jobs
- Résumé: Priya Nair's fictional résumé (JSON) from the Reallocation Engine's
  search/examples/priya-nair/, using her target roles and location preference.
- State: the list of posting ids seen on the previous run.

## Out
For each posting that is NEW since the last run:
- verdict: relevant or not relevant
- justification: names the posting fields used (title, location) and the
  résumé fields they were compared with (target roles, location preference)
- two verdicts: one from my written rule (a record, anyone can recompute it)
  and one from Claude (labelled as a judgment)

The first run is a baseline and reports no postings as new.

## Refuses
- Fetching any host not on the allow-list (only boards-api.greenhouse.io).
- Showing a real résumé on screen or on GitHub (fictional persona only).
- Presenting Claude's judgment as a fact.
- Applying, emailing, messaging anyone, or logging in anywhere.
- Checking H-1B sponsorship (one company only, so it would not vary;
  planned for a later layer).

## The rule

A posting is RELEVANT only if all three checks pass. Checks are case-insensitive
and match whole words.

1. Role match: the title contains EITHER
   (a) at least one of: Machine Learning, ML, AI, Artificial Intelligence,
       Data Engineer, Data Engineering, Data Scientist, Analytics, Analyst;
   OR
   (b) "Software Engineer" together with an early-career word:
       New Grad, Early Career, Entry, Associate
       (e.g. "New Grad Software Engineer" counts; "Software Engineer" alone
       or "New Grad Marketing" does not).

2. Not too senior: the title does NOT contain any of:
   Senior, Sr., Staff, Principal, Manager, Director, Head, Lead.

3. Location: the location is in the United States (it names "United States",
   "USA", "US", or a US state), or it is Remote without naming a non-US country.

Otherwise the posting is NOT RELEVANT.

Early-career words (New Grad, Early Career, Entry, Associate) count only as
described in check 1(b); on their own, or with any other title, they do not make
a posting relevant. When present, the justification notes them as an
early-career signal.

Every verdict's justification must name the posting fields used (title, location)
and the résumé fields they were compared with (Priya's target roles and location
preference).

## Wrong versions my tests must catch
1. Verdicts paired with the wrong postings (labels shifted by one or shuffled),
   so a correct verdict is reported against a different posting.
2. A justification that cites no posting fields or no résumé fields, even when
   the verdict itself is correct.

## What a failure looks like (2026-10-25)
A failure would be if my agent misses a new job that actually matches Priya's
profile or marks an unsuitable job as relevant without giving a proper
explanation. This would make the results unreliable and could cause Priya to
miss a good opportunity or waste time on the wrong jobs.

## Revision (2026-10-25, before any agent code)
After working through eight example postings by hand, I decided that
"New Grad Software Engineer"-type roles should count for Priya even without a
data/AI word, because early-career software roles are realistic for her.
Check 1 now has a second path, 1(b). Nothing else changed.
