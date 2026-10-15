# FACTCHECK: AI Product Failure Lab pitch film

Every factual claim in the narration, checked 2026-10-14. Statements about the future ("will …") are plans, not facts; they're
listed as EXEMPT, with the tense checked.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B04 | I gave plain Claude and ChatGPT the same idea with a planted fake statistic | PASS | research/baseline-prompt.md; baseline-claude-run1–3.md; baseline-chatgpt.md | Claude Code ran the tests at Aditya's direction (stated in SOURCES.md) |
| 2 | B04 | Both caught the fake number | PASS | Claude 3/3 runs flag the 68% figure in their first section; ChatGPT "one important correction to your premise" | — |
| 3 | B05 | In three runs, plain Claude cited no sources | PASS | 0 URLs and no named sources in run1–3 (grep checked) | — |
| 4 | B05 | …yet stated unsourced claims as facts | PASS | e.g. run2: "Survey willingness-to-pay is consistently inflated"; run1: "Fitness apps already churn heavily" | First draft said "guesses as facts"; changed to "unsourced claims", which is observable |
| 5 | B05 | ChatGPT attached sources to just two paragraphs | CORRECTED | baseline-chatgpt.md: chips "FitSpace +2", "Federal Trade Commission +1" | First draft said "cited two"; the chips bundle more than two sources |
| 6 | B05 | ChatGPT left most claims unlabelled | PASS | baseline-chatgpt.md §2: labels only on thresholds, experiments, churn table | — |
| 7 | B06 | DimeADozen's homepage promises hundred-page reports with hundreds of citations | PASS | dimeadozen.ai homepage, read 2026-10-14: "typically 100+ pages with 500+ URL citations" | Attributed to its homepage aloud; not verified by us |
| 8 | B06 | I haven't bought one | PASS | research/alternatives.md §4 | — |
| 9 | B15 | Years of requirements / gap analysis / challenging assumptions in product work | PASS | Aditya's portfolio source: "4+ years across B2B product & technology", Business Analysis skills list | Aditya to confirm wording |
| 10 | B15 | WorkShip and SkillPort are on my GitHub | PASS | github.com/AdityaHasija37/Workship, /SkillPort (linked from the portfolio) | Aditya to confirm both repos are public |
| 11 | B16 | Exists today: the idea, a blueprint drafted with ChatGPT, the chatbot tests | PASS | ~/Downloads blueprint docx (2026-10-14); research/ | — |
| 12 | B01–B03, B07–B14, B16 | Everything about the Failure Lab's design | EXEMPT | Plans, all phrased "will"; drawings tagged "constructed" | Tense checked; fixed B03 "challenges" → "will challenge" |
| 13 | B00 | "Most ideas don't fail on day one" | EXEMPT | Framing, not a statistic; no number is claimed | — |
