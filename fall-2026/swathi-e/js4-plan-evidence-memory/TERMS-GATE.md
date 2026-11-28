# TERMS-GATE — Terms-of-Use and Endpoint-Permission Gate (JS4)

**Required by:** `PLAN.md` step S0 and section 13  
**Review finalized:** 2026-11-27  
**Decisions by:** Swathi Baba Eswarappa  
**Research:** Claude Chat read the official pages listed below and summarised them; I read the summary and made each decision myself.  
**Method:** Official documentation and terms pages read in a browser-like fetch. No request was made to either job-board API for this review.

This record states what each document says, separately from my interpretation. A public GET endpoint was not treated as automatic permission.

---

## 1. Greenhouse — `boards-api.greenhouse.io` (Databricks, Stripe)

### Sources read

- Job Board API documentation: https://docs.greenhouse.io/job-board
- My Greenhouse User Agreement (effective January 29, 2025): https://my.greenhouse.io/users/agreement
- Greenhouse legal index: https://greenhouse.com/legal

### What the documents say

- The Job Board API is described as giving a company access to a JSON representation of its offices, departments and published jobs, so it can build its own careers pages.
- The documentation states that Job Board data is publicly available and that no authentication is required for any GET endpoint. Only the application-submission POST requires an API key.
- Documented read-only endpoints used by this project:
  - List jobs: `GET https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs` (optional `content=true` adds descriptions, departments and offices).
  - Retrieve a job: `GET https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs/{job_id}`.
- The per-job endpoint has optional parameters: `questions=true` adds the job's application questions (which can include location, compliance and demographic questions), and `pay_transparency=true` adds pay ranges.
- The My Greenhouse User Agreement governs "My Greenhouse", the job-seeker account service at my.greenhouse.io. It prohibits using automated means such as spiders, robots or crawlers to access or use that service.
- The legal index lists a privacy policy, a cookie notice, and customer agreements (Master Subscription Agreement, SLA and related terms). No separate terms of use for the public Job Board API were found.
- **Rate limits:** I viewed the Job Board API page (https://docs.greenhouse.io/job-board, section Introduction → Authentication) in my browser on 2026-11-27 and saw this sentence: "Requests may be rate limited for security and traffic reasons." A text copy of the same page retrieved by Claude Chat on 2026-11-27 did not contain this sentence. I record both observations. Either way, I treat rate limiting as possible; the budget in `PLAN.md` section 9 already keeps live use to at most 8 requests, and an HTTP 429 (too many requests) response is handled like any other 4xx under `PLAN.md` section 8: it is not retried, and the affected board or lookup is recorded as incomplete or not run.
- No statement about storage or redistribution of Job Board data was found.

### My interpretation

- The read-only endpoints this agent needs are documented and unauthenticated.
- The My Greenhouse anti-automation clause applies to the job-seeker account service, not to the Job Board API. It still shows that Greenhouse cares about automated access, so I keep use minimal.
- The documented purpose is an employer building its own careers page. Third-party reading is neither explicitly permitted nor prohibited. Permission is therefore **uncertain, with low risk at the planned volume**.
- Customer agreements (MSA, SLA) do not apply to me; I am not a Greenhouse customer.

### Decision

**CONDITIONAL GO** for live read-only requests in JS4, under all of these conditions:

- At most 8 HTTPS GET requests to `boards-api.greenhouse.io` in one November 28 run, as budgeted in `PLAN.md` section 9 (2 listings, 2 positive controls, up to 4 per-job lookups; retries count against the 8).
- No `questions=true` and no `pay_transparency=true`.
- No login, no application submission, no POST of any kind.
- Raw responses are not redistributed; only the minimal derived evidence is committed.
- This decision is a precondition for S0, not authorization to run the collector. The live run still needs every other S0 check and my explicit go-ahead at that time.

If the live gate or collection fails, the Greenhouse boards use the saved November 19 responses, labelled historical.

---

## 2. Ashby — `api.ashbyhq.com` (Plaid)

### Sources read

- Ashby Job Postings API: https://developers.ashbyhq.com/docs/public-job-posting-api
- Dedicated Partner Job Feeds: https://developers.ashbyhq.com/docs/dedicated-partner-job-feeds
- Ashby Customer Terms of Service (last updated September 29, 2025): https://www.ashbyhq.com/resources/terms
- Ashby Terms and Policies index: https://www.ashbyhq.com/resources/terms-and-policies

### What the documents say

- The Job Postings API is described as returning all currently published job postings for an organization, for use if it hosts its own careers page.
- The single documented request is `GET https://api.ashbyhq.com/posting-api/job-board/{JOB_BOARD_NAME}`, with an optional `includeCompensation=true` parameter that adds compensation data.
- No per-posting endpoint is documented. The page does not mention authentication, rate limits, storage or redistribution.
- A job with `isListed: false` should only be available via direct link.
- Ashby can provision a dedicated job-posting feed for a partner that wants to ingest job postings; Ashby customers opt in to share their jobs with that partner.
- The Customer Terms of Service are an agreement between Ashby and a business entity that purchases from Ashby or logs into the Service, where the Service is Ashby's recruiting or analytics product.
- The Terms and Policies index lists customer terms, privacy, SLA, GDPR, AI terms and related documents. No terms for visitors or for anonymous use of the posting API were found.

### My interpretation

- The Customer Terms do not apply to me; I am not an Ashby customer.
- No published terms cover anonymous third-party use of the posting API.
- Ashby documents the public API for an organization's own careers page and names a separate partner-feed route, with customer opt-in, for third parties that ingest postings. Permission for my reading is therefore **more uncertain than for Greenhouse**.

### Decision

**NO-GO** for live requests to `api.ashbyhq.com` in JS4.

- Live Ashby budget: 0 requests.
- Plaid's two observations are the real saved collections from November 17 and November 19, 2026 (JS3 commit `c2e624e`), each labelled as a replay of saved responses with its original collection date.
- The November 19 Plaid observation is never presented as a November 28 or live result.
- No Ashby liveness check is made.

---

## 3. Not checked (limitations of this review)

- `robots.txt` on either API host (checking it would require a request to those hosts).
- Greenhouse's and Ashby's privacy policies.
- Ashby's Product Specific Terms.
- Any rate limit the servers apply in practice. No rate limit is documented on the pages read, which does not mean none exists.
- Whether the employers themselves (Databricks, Stripe, Plaid) publish their own terms covering their job boards.

---

## 4. Effect on PLAN.md

These decisions are logged in `PLAN.md` Version 2.1, section 15 ("Later findings that reopened a decision"), with the changes to sections 1, 2, 9, 10, 13 and 16.

---

*This record describes a documentation review and my decisions. It does not claim that any live request has been made or that any endpoint has been verified in practice.*
