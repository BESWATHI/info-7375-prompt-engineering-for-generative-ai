# FRICTIONAL — Marino Desk Assistant pitch film

Dated entries, written as the work happened on 2026-10-13 (times EDT, approximate to a few minutes). I worked with Claude Code (Opus 5.5). "Claude" below means that session; "I" means me, Shubham.

**~13:30 — Start.** I pasted the assignment instructions and asked Claude to go through it line by line, plan, and build, in a new folder called `Final Project Pitch Film/`. My Week 1 Brutalist checkout no longer existed, so Claude re-cloned the toolkit at commit `519fcbb`.

**~13:38 — Setup failed the same way as Week 1.** `./setup --install` in a Python 3.14 venv installed everything, then exited 1 with "ElevenLabs reference found". The flagged files are the toolkit's own example reels. Claude ran the readiness checks by hand instead, and all passed. Python 3.14 worked this time because the toolkit now pins Manim 0.20.

**~13:40–14:45 — First attempt: the wrong project.** Claude recommended pitching my Reallocation Engine recipe (swe-opt-clock, PR #49), and I agreed at first. It built a complete film that passed every gate. Then three reviews ran: a fresh-context grader agent, a five-advisor "LLM council", and its peer reviews. They kept finding the same weakness: the code was Claude's, so the pitch proved little about me. The lessons that carried over:
- never present Claude-written code as my skill evidence;
- say "written with Claude";
- use "will" for anything unbuilt, including rules not yet implemented;
- label who ran each check;
- the toolkit's `channel_title` stamp fails Gate V;
- faster-whisper needs ffmpeg decoding with PyAV 19;
- Kokoro mispronounces "Bagwe".

**~14:38 — TA ruling on the video.** I asked a TA on Teams whether the mp4 goes to Git. The answer: "Only beat sheet to git. Video to Canvas." The film goes in the Canvas zip only. The GitHub folder holds the beat sheet and the rest of the required documents.

**~15:05 — I rejected the first pitch.** What I told Claude: "The career-ops and Reallocation Engine are not my projects." The assignment asks for "a portfolio piece … that shows you can do the work you want to be hired for." I asked Claude to start over with one of my own projects, using my project bank. Claude archived the first version locally (`_archive/`, not submitted), removed the untracked copy from the course repo (nothing had been committed), and read my repos and my project bank.

**~15:10 — Choosing again.** Claude found two strong candidates. EventFlow Engine (`robust-data-processor`) is mine, a GCP pipeline with no AI part yet. marino-rag is a citation-backed Q&A assistant for the Marino front desk. Claude flagged two problems with marino-rag as it stands: it reads SharePoint training documents (restricted data under the assignment's rules), and it calls OpenRouter models. **My decisions:**
- marino-rag, rescoped to the public site only, with answers moved to Claude;
- target role: new-grad full-stack SWE;
- alternatives I really looked at: manual lookup and the site's own search;
- disclosed Kokoro narration.

I also told Claude the honest authorship: EventFlow is mine; marino-rag's code is mostly AI-generated under my direction.

**~15:17 — Real checks before writing anything.** Claude:
- re-ran marino-rag's tests: 60 passed at `dd3205e`;
- confirmed the SharePoint exports are gitignored and were never committed;
- ran the site's own search: "guest pass" → 5 pages, Home first;
- fetched the Alumni page through marino-rag's own parser: 782 words, and five annual prices for one membership by start date, $480 down to $120.

The parser check turned up a surprise that changed the risk I named. The page's raw HTML hides old 2023–24 prices in comments, and the parser already drops them. So hidden stale prices are *not* the risk. The real risk is the date-dependent price table. All of this is in `evidence/`, labelled as run by Claude.

**~15:21 — Script length.** The first draft came to 627 words and 234.5 s of measured Kokoro audio (3:54), so no cuts were needed. Whisper caught "EventFlow" being heard as "a vent flow", so B14 now says "the EventFlow Engine" and was re-voiced. My surname is respelled "Baag-way" in the spoken text only.

**~15:27 — Look before 4K.** Gate A was clean for all 16 scenes. Low-res renders all fit their audio. Contact sheets at 30/50/95 % showed seven layout fixes, all made before the 4K build:
- B01: the label crowded the corner tag.
- B02: "60 tests pass" overlapped the server stack.
- B03: the scrolled lines ran into the window's title bar.
- B10: the padlock sat off the box, and the windows' title bars overlapped.
- B12: the "?" was detached from its marker.
- B13: the label overlapped the tag, and the stamp touched the card.
- B14: the EventFlow dot was off-centre.

The Gate B pre-audit then flagged the outro title past the safe area (x = 6.35), so it was shrunk from 76 to 68.

**~15:30 — 4K build.** `./art run ../final-project-film --height 2160` (`gate-reports/art-run-1.log`).

**15:35–15:43 — Build 1: all `art run` gates passed (Gate V 0/0), but `art final` was blocked by Gate T on 3 beats** (stamped 15:35; still failing 15:38; PASS 15:41; first master written 15:43). The cause was decorative ink squiggles: inside the ink-outlined search pill (B04) and the contract slip (B13), and small ones on B07's page cards. Gate T read them as overlapping or too-small text, which the low-res review couldn't show. Fix: the squiggles are drawn in grey, which isn't counted as text. Re-rendering B04, B07 and B13 left B07 still failing, because its page cards' squiggles were on screen at the midpoint. After greying those too and re-rendering B07, Gate T passed (16/16). The first master was 234.8 s (3:55), sha256 `be93a1dd…`. Master, loudness and sharpness checks pass; `bookend_check.py` keeps its one documented failure (`gate-reports/GATES.md`). Claude looked at every beat's 50% and 97% frames in the master.

**~15:50 — A fresh-context review of this version.** A reviewer agent re-checked the facts and confirmed them: 60 tests, the five Alumni prices, the site-search results, the EventFlow load-test screenshot, and the sha256. It then flagged what was still wrong:
- B01 and B05 spoke the planned behaviour in the present tense ("answers", "gives"). That breaks "everything else is will".
- My portfolio site was cited as front-end evidence, but 17 of its 38 commits mention Claude.
- FACTCHECK cited my PRD's author line ("Suhas Bagwe") without explaining the name.
- B09's "I can build a full-stack AI app" overclaimed, given that the repo's code is mostly AI-generated.
- B14's "this repo" was ambiguous right after EventFlow.
- The B12 and B02 tags didn't match their pictures.
- MASTERCHECK's skipped sub-check wasn't disclosed.
- The brief was over a page.

**~18:05 — My answers, and the fixes.**
- **My answers:** I confirmed that I work as a Facility Assistant at Marino, and that people there call me "Suhas" because it's easier to say. That's the name on the PRD. I chose to drop the portfolio site and rest my existing-skill evidence on EventFlow alone.
- **Re-voiced (B01, B05, B09, B14):**
  - "will answer… and quote", "it will give…";
  - "I can specify, ground and evaluate an AI app";
  - "The Marino repo's current code was mostly AI-generated".
- **Re-labelled and re-drawn:**
  - B02 tag: "planned repo · real: 60 tests pass";
  - B12 tag: "real prices · wrong pick illustrated";
  - B14: the React/TS crate removed.
- **The 4:00 cap:** the narration is now 237.1 s.
- **One stop on the way:** Gate B stopped the rebuild at B13, because the "today's date" label I'd nudged touched the calendar. After moving the calendar instead, every gate passed. Gate T PASS at 18:14; the new master is 237.4 s (3:57), sha256 `ea18ed8b…`.

**2026-10-14 — My own review before submitting (Shubham).** These were the checks I had left for myself, and I did them, not Claude:
- **Watched the whole film with sound** (3:57, sha256 `ea18ed8b…`). My name comes through right as "Baag-way", and I'm happy with every sentence. No changes to the film.
- **B14, "I work the Marino front desk":** true. I'm a Facility Assistant there, as I confirmed at ~18:05.
- **Re-opened all four files in `evidence/` myself:** the test run (60 passed at `dd3205e`), the site search ("guest pass" → 5 pages, Home first), the Alumni page (782 words; $480 down to $120), and the Whisper transcript. They match what the film and the brief say.
- **One change, docs only.** My main viewer is a hiring manager who may not know what Marino is. The film's first sentence already says "Northeastern's Marino Recreation Center", but the README and brief only said "Marino Recreation". I had Claude change both to say it is Northeastern University's campus gym. I chose not to re-voice B01 to add "University", because that would have meant a new master, a new sha256 and re-running every gate for half a second of narration. While editing that line, the README's "answers" became "will answer", to match the honesty rule.
- **Times fixed.** A rubric review found entry times out of order (setup after the first attempt began; "Look before 4K" stamped after the 4K build). Claude checked them against the timestamps of the commands in the Claude Code session and I approved the corrections: setup 13:38, script draft 15:21, look before 4K 15:27, 4K build 15:30.
- **Unresolved:** `bookend_check.py` still fails on purpose (the `@NikBearBrown` handle; see `gate-reports/GATES.md`), and the master check's duration sub-check stays skipped because `clock_check.py` isn't in the toolkit at `519fcbb`.

