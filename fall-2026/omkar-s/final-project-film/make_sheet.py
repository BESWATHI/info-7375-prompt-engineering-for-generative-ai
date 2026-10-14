#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for the BiteCheck pitch film (Omkar Salian, INFO 7375).

Format: Brutalist show-tell (one drawn isometric picture per beat, minimal labels, the voice
explains). Deliberate deviations from the skill, required by the assignment ("Narrate as yourself.
Do not use the instructor's name, persona, or credit line"): no Liam persona or greeting, no
Professor Bear portraits, no @NikBearBrown outro, and no reconstructed Claude.ai composer (no
fabricated Claude responses). Every beat is Manim. See FRICTIONAL.md.

Honesty tags: each beat carries an on-screen corner tag, either REAL (it ran and I can show it)
or PROPOSED (a drawing of something that does not exist yet).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "bitecheck-pitch"
TITLE = "BiteCheck: Do Claude's API Tests Actually Catch Bugs?"
VOICE = "am_michael"


def beat(bid, cls, tag, narration, image, show):
    return {"beat_id": bid, "act": "pitch", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration,
            "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": VOICE, "engine": "kokoro",
            "honesty_tag": tag,
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image},
            "qc": {"sparse_by_design": True,
                   "sparse_reason": "show-tell style: one drawn object per beat on a cream stage; only underfill/clustered are waived."}}


B = [
 beat("B00", "B00_GreenCrate", "PROPOSED",
      "Claude can draft a whole suite of API tests that all come back green. "
      "But a green test only means something if it would turn red when the code is wrong. "
      "BiteCheck tells an engineer reviewing AI written tests which ones would catch a broken business rule.",
      "A crate of test pages drops in; check marks pop on each page; a question mark appears beside the crate.",
      [{"at": 0.1, "event": "crate drops"}, {"at": 0.35, "event": "checks pop"}, {"at": 0.75, "event": "question mark"}]),
 beat("B01", "B01_Repo", "PROPOSED",
      "It's called BiteCheck. When it's done, it will be a public GitHub repository with four parts: "
      "a prompt that tells Claude how to write the tests, a list of bugs I put into the code on purpose, a runner, and a one page report.",
      "A box labelled 'GitHub repo' opens; four parts rise out of it in turn: prompt page, bug block, runner server, report page.",
      [{"at": 0.15, "event": "box opens"}, {"at": 0.45, "event": "prompt, bugs"}, {"at": 0.8, "event": "runner, report"}]),
 beat("B02", "B02_LoanApi", "REAL",
      "The tests will run against a small loan application API that I built earlier with Claude's help. "
      "It uses made up applicants and mock vendors, and it checks rules like a minimum income and the order of each step.",
      "A server stack labelled 'loan API' lights up; two rule tags clip onto it: 'min income', 'step order'.",
      [{"at": 0.15, "event": "server"}, {"at": 0.55, "event": "rule tags"}]),
 beat("B03", "B03_SmokeRun", "REAL",
      "This part exists. On October twelfth, I ran it on made up applicants with Claude Code. An income of fourteen thousand, nine hundred and ninety nine rupees was rejected. "
      "Fifteen thousand got an offer. And paying out a loan before the earlier steps was refused. It has no tests yet.",
      "Three applicant cards ride up to the server one at a time: one gets an X, one a check, one a stop bar with '409'.",
      [{"at": 0.25, "event": "card 1, X"}, {"at": 0.5, "event": "card 2, check"}, {"at": 0.75, "event": "card 3, 409"}]),
 beat("B04", "B04_BreakARule", "PROPOSED",
      "Here's the core idea. I break one rule on purpose. Say the minimum income drops from fifteen thousand to fifteen hundred. "
      "Then I run the tests again. If a test goes red, it bites. If everything stays green, the tests just missed a real bug.",
      "The rule block '15,000' is swapped for '1,500' with a spark; the test crate rides through a gate; one page flips to an X.",
      [{"at": 0.2, "event": "rule swaps"}, {"at": 0.5, "event": "crate through gate"}, {"at": 0.7, "event": "one page red X"}]),
 beat("B05", "B05_ClaudeLog", "PROPOSED",
      "It works the other way too. A test that fails on the correct code means Claude got something wrong. "
      "Every one of those goes into a dated log, with how I caught it.",
      "A test page with an X on a green server; a quill writes lines onto a log page beside it.",
      [{"at": 0.2, "event": "X on correct code"}, {"at": 0.55, "event": "quill writes the log"}]),
 beat("B06", "B06_Alternatives", "MIXED",
      "From their docs, Postbot generates test scripts, and Schemathesis checks an API against its schema. "
      "On October thirteenth, I ran Stryker on my loan rules with Claude Code. It made ninety two mutants, but none changed the fifteen thousand limit, "
      "and its one step order mutant deletes every guard at once. BiteCheck adds those business rule bugs, one at a time.",
      "Two closed boxes (docs only), the Stryker box with the hero number 92 and '0 change 15,000', then the open BiteCheck box with a rule page.",
      [{"at": 0.15, "event": "Postbot"}, {"at": 0.3, "event": "Schemathesis"}, {"at": 0.42, "event": "Stryker"}, {"at": 0.65, "event": "BiteCheck box"}]),
 beat("B07", "B07_FirstMinute", "PROPOSED",
      "The reader is a hiring manager or engineer screening me for a new grad software or AI role. "
      "In the first minute, they run one command and read one page: did the tests pass on the real API, which bugs were caught, which survived, and where Claude was wrong.",
      "A terminal window types one command; a report page slides out with three bars growing.",
      [{"at": 0.3, "event": "command"}, {"at": 0.55, "event": "report page"}, {"at": 0.75, "event": "bars grow"}]),
 beat("B08", "B08_Contract", "PROPOSED",
      "What would it show about me? First, a prompt contract: every test Claude writes must name the rule it checks. "
      "That's source grounding. A test that can't point to a rule gets thrown out.",
      "A rule page and a test page; a cable draws from the test to the rule; a test page with no cable drops into a bin.",
      [{"at": 0.2, "event": "pages"}, {"at": 0.45, "event": "cable to rule"}, {"at": 0.75, "event": "orphan test to bin"}]),
 beat("B09", "B09_Loop", "PROPOSED",
      "Second, an agent loop with limits. Claude Code may edit the tests, never the API, and stops after a fixed number of tries. "
      "Third, evaluation: a score, plus every miss. It won't prove this works on every API. I'll measure it on one.",
      "A loop arrow circles between Claude's test pages and the runner; a lock clicks onto the API server; a score bar fills.",
      [{"at": 0.2, "event": "loop"}, {"at": 0.4, "event": "lock on API"}, {"at": 0.7, "event": "score bar"}]),
 beat("B10", "B10_OutAndFirst", "PROPOSED",
      "What's out: it won't be a tool for any API, and it will never fix application code. "
      "What comes first: the income rule. One bug, run in GitHub Actions. You'll know it ran when a committed report shows the real API passing and that bug caught.",
      "A wrench over the API is crossed out; then a three-gate CI belt carries one bug block to a check.",
      [{"at": 0.15, "event": "wrench crossed out"}, {"at": 0.5, "event": "CI belt"}, {"at": 0.85, "event": "check"}]),
 beat("B11", "B11_Risk", "PROPOSED",
      "The biggest risk is me. I write the bugs, so I could make them easy to catch without meaning to. "
      "So I'll commit the full bug list before Claude writes any test, and the git history will show the order. "
      "The report will list every bug that survived, not just the score.",
      "A timeline: the 'bugs' commit dot lands first with a lock, then the 'tests' dot; a survivors page slides out.",
      [{"at": 0.3, "event": "bugs commit + lock"}, {"at": 0.55, "event": "tests commit"}, {"at": 0.8, "event": "survivors page"}]),
 beat("B12", "B12_WhyMe", "PROPOSED",
      "Why this project? Mostly learning. I've done API testing and CI gates at my last job, but that work is private. "
      "What I can show is my public Reallocation Engine pull request, a Claude workflow with a run log. "
      "Mutation testing and evaluation design are new to me. Finding out how well Claude's tests do is the point.",
      "Two shelves: 'have' with two private blocks and one public PR block; 'new to me' with two outlined blocks.",
      [{"at": 0.2, "event": "have shelf"}, {"at": 0.6, "event": "new shelf"}]),
 beat("B13", "B13_ExistsWill", "REAL",
      "So, where it stands today. The loan API exists, and it ran. This brief and this film exist. "
      "Everything else, the prompt, the bugs, the tests, the runner and the report, is still to be built. "
      "This is BiteCheck. I'm Omkar Salian.",
      "Two columns: 'exists' with two solid blocks; 'will exist' with five dashed outlines; the title lands.",
      [{"at": 0.2, "event": "exists column"}, {"at": 0.5, "event": "will-exist column"}, {"at": 0.85, "event": "title"}]),
]

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · FINAL PROJECT PITCH",
    "author": "Omkar Salian", "skill": "show-tell", "style_preset": "show-tell",
    "channel_title": "Omkar Salian", "persona": "Omkar Salian (first person; synthetic Kokoro voice)",
    "voice": VOICE, "voice_kokoro": VOICE, "engine": "kokoro", "clock": "narration",
    "palette": "claude", "register": "Plain", "fps": 24, "aspect_ratio": "16:9", "width": 1920, "height": 1080,
    "caption_policy": "none",
    "bookend_exempt": ["cold-open", "bvdt", "bhtf"],
    "bookend_exempt_reason": "Course assignment forbids the instructor's name, persona or credit line and any fabricated Claude response, so the Liam greeting, the composer cards and the @NikBearBrown outro are dropped. The film closes on the narrator's own name in B13 instead of ClaudeTitleOutro.",
    "audience": "INFO 7375 graders; hiring managers screening new-grad SWE / AI engineers",
    "source_doc": "PROJECT-BRIEF.md (2026-10-12); evidence/los_smoke_test.txt",
    "tags": ["INFO 7375", "pitch", "mutation testing", "API testing", "Claude Code"]},
    "beats": B}

old = HERE / "beat_sheet.json"
if old.exists():   # keep measured audio across re-runs
    prev = {b["beat_id"]: b for b in json.loads(old.read_text())["beats"]}
    for b in B:
        p = prev.get(b["beat_id"])
        if p and p.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file"):
                if k in p:
                    b[k] = p[k]
old.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b["estimated_duration_s"] for b in B)), "s")
