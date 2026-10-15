# FACTCHECK — atharva-sponsorsql-pitch

Every factual claim in the narration or on screen, with its source. Project claims are all future tense ("will"): nothing in SponsorSQL exists yet.

| # | Claim | Beat | Source / status |
|---|---|---|---|
| F1 | The U.S. Department of Labor publishes LCA (H-1B, H-1B1, E-3) disclosure files. | B02 | DOL OFLC Performance Data page, https://www.dol.gov/agencies/eta/foreign-labor/performance (opened 2026-10-13) |
| F2 | The FY2025 file covers October 1, 2024 – September 30, 2025; the Q4 file is cumulative for the year. | B07, B10 | Same page ("Each data set is cumulative for the fiscal year"); LCA_Record_Layout_FY2025_Q4.pdf, page 1 (read 2026-10-14) |
| F3 | An LCA is filed by an employer on Form ETA-9035. | B02 | LCA_Record_Layout_FY2025_Q4.pdf, page 1 |
| F4 | Fields include EMPLOYER_NAME, JOB_TITLE, WORKSITE_CITY, WAGE_RATE_OF_PAY_FROM, and a separate TRADE_NAME_DBA field. | B02, B08 | LCA_Record_Layout_FY2025_Q4.pdf (field names extracted 2026-10-14) |
| F5 | The data may contain typos and other anomalies from employer or internal data entry. | B08 (risk) | DOL Performance Data page, "Disclosure Data" section |
| F6 | ChatGPT can write SQL from a question; its query is not guaranteed correct. | B04 | Author's own use of the tool; described as a reading, not a tested comparison (said on screen) |
| F7 | Vanna.ai turns questions into SQL using database context; its queries still need checking. | B04 | Author's own use of the tool; same caveat |
| F8 | An LCA filing is not a job offer, not proof that sponsorship is available, and not an approved visa petition. | B07 | Scope statement from PROJECT-BRIEF.md; an LCA is an employer attestation to DOL, separate from a USCIS petition decision |
| F9 | "EXAMPLE DATA LLC" and its variants, and the 1-vs-3 count. | B08 | CONSTRUCTED: invented to illustrate the risk; labelled on screen |
| F10 | "questions 10, passed —, failed —" table. | B05 | CONSTRUCTED mock-up; 10 is the planned first test set; no results exist; labelled on screen |
| F11 | The cold-open composer reply. | B00 | CONSTRUCTED: not a Claude response; labelled on screen |

No Claude response appears anywhere in the film.
