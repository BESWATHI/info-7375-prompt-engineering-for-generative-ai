# PROJECT BRIEF — The Reallocation Engine CLI

## 1. What is it?
This is an evidence-first, automated job-application filtering CLI and workflow designed specifically for F-1 STEM OPT students (with a focus on Information Systems and Computer Science backgrounds). It targets broad software engineering roles (SWE, DevOps, QA, Cloud Infrastructure). It evaluates job postings against authentic public immigration and corporate filings—outputting an evidence-backed decision report with clear `Apply` or `Skip` verdicts.

## 2. Why would anyone care?
International students on F-1 STEM OPT face strict 90-day unemployment clocks and limited application capacity. Millions of applications are wasted on companies that never sponsor visas or roles with phantom postings. Unlike opaque "black-box AI" tools that paste descriptions into raw LLMs, this system delivers **zero-hallucination provenance and transparency**. Every single claim is explicitly labeled: verified against database records (`[record]`), flagged as deterministic rule gates (`[rule-gate]`), or explicitly isolated as model reasoning (`[model-judgment]`). It restores trust by telling the user exactly what it did.

## 3. Who opens it, and what do they do with it?
**Target User:** F-1 STEM OPT job seekers.  
**First 60 Seconds:** The student opens their local Terminal, runs the CLI command with a target job posting URL (e.g., `reallocate score <job-url>`), and receives an instant, structured markdown summary showing gate status, DOL H-1B filing track record, SEC Form D funding evidence, deduplication status, and an actionable `Apply` or `Skip` recommendation.

## 4. What does it prove about you?
It demonstrates mastery of **source-grounded AI workflows**:
1. Architecting strict **Prompt Contracts** that enforce structural constraints and prevent hallucination.
2. Integrating verified multi-source external datasets (DOL LCA disclosures, SEC Form D) as immutable deterministic gates rather than relying on probabilistic LLM memory.
3. Building observable AI pipelines with clear audit logs, architectural decision records (ADRs), and friction logs.

## 5. What is in, what is out, what comes first?
* **In Scope:**
  - Visa sponsorship verification using DOL H-1B disclosure data.
  - Role quality scoring and title matching for SWE/DevOps/QA tracks.
  - Lightweight duplicate suppression using hash keys (`company_normalized + title_normalized`).
  - Strict provenance tagging (`[record]`, `[model-judgment]`, `[rule-gate]`).
* **Out of Scope:**
  - Automated resume spamming or auto-apply bots (aggressively rejected to protect applicant reputation).
  - Heavy multi-user SaaS databases or web frontends (kept as a local CLI script).
* **What Comes First:**
  - Core data matching against verified local files and the lightweight deduplication tracker.

## 6. What could sink it?
1. **False Rejections (LLM Over-filtering):** The model might misread nuanced job language (e.g., confusing "must be authorized to work" with "will not sponsor visas").  
   *Countermeasure:* Strict Prompt Contracts requiring **Quote Proof** (exact quotation from posting text) before any disqualification gate can trip.
2. **UX Friction:** If duplicate job postings from aggregators clutter the evaluation log, the user abandons the tool.  
   *Countermeasure:* Silent hash deduplication intercepting identical postings before LLM scoring runs.

## 7. Why this project?
* **The Mindset Shift:** Moving from naive, uncritical trust in conversational LLMs to defensive, verification-driven engineering. Fluency is treated as a warning sign, not proof of truth.
* **Demonstrated Skills & Evidence:** Demonstrates structured AI governance. Reviewers can independently inspect: (1) in-repo `AI_Task_Logs/`, ADRs, and `FRICTIONAL.md` tracing human-agent collaboration; (2) provenance metadata emitted on every CLI evaluation.
* **Skills Being Acquired:** Learning how to design automated verification gates, multi-agent linting pipelines, and ruthless anti-hallucination guardrails.

---

### Exists Today (Verified Prototype)
* Working recipe `tisaac-swe-stem-opt` in *The Reallocation Engine*.
* In-repo verification against DOL H-1B CSV records and SEC Form D data.
* Structured provenance tagging (`[record]`, `[model-judgment]`, `[rule-gate]`).
* Integrated role scorer scoring SWE, DevOps, and QA profiles.

### Will Exist (Planned CLI Extensions)
* Standalone single-command CLI interface with instant terminal output.
* Automatic quote-proof extraction harness for human verification gates.
* Local persistent hash cache for instant aggregator deduplication.
