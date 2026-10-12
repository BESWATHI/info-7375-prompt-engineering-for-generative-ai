# FACTCHECK — Co-op Sponsor Check (pitch film)

Status: checked 2026-10-12 by Claude against the files named below; Arundhati Kandelkar to confirm on review.
Rule: past tense only for what exists and is shown in evidence; everything else is "will". Every frame audited, bookends included.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | "I'm Arundhati Kandelkar"; a pitch, not a finished build | PASS | my name; voice is synthetic Kokoro `bf_emma`, disclosed in README.md and SOURCES.md | spoken disclosure removed at my request 2026-10-12; written disclosure kept |
| 2 | BDEFS | A sponsor record is a public record of an employer filing for a work visa | PASS | dataset README: built from DOL LCA disclosure data and the USCIS H-1B Employer Data Hub | — |
| 3 | B00 | Pushed a recipe to my fork on October third; tag "commit 03784b0" | PASS | `git log -1 03784b0` → Sat Oct 3 16:55 2026, branch `contrib/2026fa-arundhatik26-coop-sponsor-swe-15-1252` | — |
| 4 | B01 | It checks three things: software-title record, co-op before graduation, posting live | PASS | CHANGE-BRIEF gates G2–G4; run output shows `matched`/`liveness=`/`DEPENDS ON GRADUATION DATE` (evidence/recipe-rerun-2026-10-10.txt) | — |
| 5 | B02 | A missing company is not treated as zero; it says unknown and tells you to ask a person | PASS | `test_F1_not_in_dataset_is_unknown_not_zero`; jpmc row → "NETWORK: … ask an alum or recruiter directly" | worded "does not treat that as zero", not "never prints zero" |
| 6 | B03 | JPMorgan Chase, Goldman Sachs, Morgan Stanley not in the dataset | PASS | CHANGE-BRIEF F1: searched 2026-10-02, none found; jpmc → `not-in-dataset` in re-run | — |
| 7 | B03 | Dataset built from a list of funded startups taken from SEC filings | PASS | `data/80-days-to-stay/README.md`: "mapped our SEC startup list against … DOL LCA … USCIS H-1B Employer Data Hub" | spoken as "would explain", not as a proven cause |
| 8 | B04 | 17 tests passed at build and on re-run October tenth; tag "17 / 17" | PASS | TEST-REPORT §5 (2026-10-03); evidence/recipe-rerun-2026-10-10.txt "Ran 17 tests … OK" | — |
| 9 | B04 | Six failure cases incl. a fake posting and two names that may be one firm | PASS | TEST-REPORT §4: F1–F6; F6 fake Databricks id; F3 SoFi `ambiguous` | — |
| 10 | B06 | A second public data source | EXEMPT | proposal, spoken as "will exist"; tag PLANNED on screen | — |
| 11 | B07 | The first six of twenty-five rows ran on October twelfth | PASS | evidence/eval-first-rows-2026-10-12.md + eval-first-rows-dataset-2026-10-12.json | tag "6 RAN · 2026-10-12 · 19 PLANNED"; run by Claude on my instruction |
| 26 | B07 | All six companies file in the official hub; dataset had a record for none; tool said unknown, not zero, every time | PASS | same files: hub FY2026 name lists for all six; statuses 5× not-in-dataset, 1× no-sponsorship-record (both reported as unknown by design) | "file in" = listed as an FY2026 petitioner |
| 27 | B07A | Hub lists "Goldman Sachs and Co LLC"; my matcher shortens it to "Goldman Sachs and" | PASS | `norm_name("GOLDMAN SACHS AND CO LLC")` → "GOLDMAN SACHS AND" (printed 2026-10-12; recipe at 03784b0) | — |
| 28 | B07A | Fixed before the hub is joined; other nineteen rows next | EXEMPT | plan ("gets fixed", "next"); not claimed as done | — |
| 12 | B08 | "BNY Mellon" and "The Bank of New York Mellon" may be one employer or two | PASS | stated as a possibility, not a finding; gate G2 human check exists today (CHANGE-BRIEF §3) | — |
| 13 | B09 | Will not give immigration advice; every answer labelled record / judgment / your input | PASS | labels exist today: `test_every_scorer_term_is_labeled`; scope statement is a plan (PLANNED tag) | — |
| 14 | B10 | Reader runs one command, sees unknown rows and a right/wrong table | EXEMPT | proposal; drawing tagged "CONSTRUCTED · not built yet"; ticks/crosses illustrative, no counts | — |
| 15 | BHTF | USCIS H-1B Employer Data Hub is public | PASS | uscis.gov H-1B Employer Data Hub (public, no login) | — |
| 16 | BHTF | Composer shows only a prompt for the viewer; no Claude response is displayed | PASS | ClaudeComposerAsk props: `output` lines are the viewer's two checks | — |
| 17 | BOUT | Title and my name; no instructor handle | PASS | ClaudeTitleOutro `handle` = "Arundhati Kandelkar" (local toolkit edit, FRICTIONAL.md) | — |
| 18 | B05 | USCIS H-1B Employer Data Hub, searched October twelfth, lists JPMorgan Chase | PASS | evidence/uscis-hub-search-2026-10-12.md: FY2026 name list shows "JPMORGAN CHASE AND CO" | search run by Claude in its browser on my instruction; SOURCES.md says so |
| 19 | B05 | Searched one employer at a time, by name, place or industry, not by job title | PASS | same file: filters are Fiscal Year, Employer Name, NAICS, City, State, Zip — no job-title filter | the hub's CSV download is acknowledged in PROJECT-BRIEF §2 |
| 20 | B05A | "Mellon" returned four employers: three BNY companies and Carnegie Mellon University | PASS | same file, FY2026 list for `MELLON` | names shown in title case for legibility; the hub lists them in capitals |
| 21 | B05A | My tool already has a test that refuses a match on part of a name | PASS | `test_substring_does_not_match` ("MELLON", "ACME"), TEST-REPORT §4 | — |
| 22 | B05A | My tool will check a whole list for software titles and co-op dates | PASS | list input + title match + timeline exist today (rows 4, 9); "will" covers the hub-backed version | — |
| 23 | B11 | I'm an international student; this is the question I face choosing a co-op | PASS | my own statement, chosen 2026-10-12 from options Claude offered (SOURCES.md) | — |
| 24 | B11A | I've worked in Java, Spring Boot, microservices, Angular, cloud and AI; this project doesn't show it | EXEMPT | my own statement; deliberately not claimed as evidenced here (rubric: existing skills need evidence) | no-evidence wording chosen by me |
| 25 | B11A | New for me: joining a second public data source into a small Python tool | PASS | my own statement; matches "Will exist" in PROJECT-BRIEF | — |
