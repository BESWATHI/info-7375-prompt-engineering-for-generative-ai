#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for the DataSentry final-project pitch (Ethan Gomes, INFO 7375).

show-tell format: one drawn isometric picture per beat, a label or two, the narration explains.
Assignment rules override the skill's house bookends: narrated as Ethan (first person), no
instructor name, persona, or credit line — so no "Liam, in for Bear" greeting, no @NikBearBrown
outro card (ClaudeTitleOutro hard-codes that handle), no Your Turn composer. The film closes on a
drawn beat (BEND) with the project title and Ethan's name instead.

Honesty rule: nothing in DataSentry exists yet. Past tense only for what exists today
(this pitch, the brief, the notes on dbt / GX). Everything about the tool is "will".
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "datasentry-pitch"
TITLE = "DataSentry: A Project Pitch"
VOICE = "am_michael"   # a stock Kokoro voice, not the toolkit's Liam persona (am_onyx)
SPARSE = ("show-tell: one drawn object on a cream stage, a label or two; the voice explains. "
          "Only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")


def beat(bid, act, narration, cls, intent, show, sparse=True, **extra):
    b = {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW", "narration_text": narration,
         "estimated_duration_s": round(len(narration.split()) / 2.6, 1), "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": intent, "show": show,
                  "manim": {"class": cls}, "motion_claim": intent}}
    if sparse:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE}
    b.update(extra)
    return b


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate, "narration_text": narration,
         "estimated_duration_s": round(len(narration.split()) / 2.6, 1), "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 beat("BIDEA", "title",
    "This is a Final Project Pitch Film created by Ethan Gomes. The project is called Data Sentry. "
    "Nothing is built yet; everything here is a plan. "
    "The question isn't whether Claude can write data checks. It's whether anyone can measure what they miss.",
    "BIDEA_Title", "Title card: 'DataSentry' large and centred; a thin rule draws beneath it with one terracotta dot; one line below: 'Scoring AI-written data checks with planted defects'.",
    [{"at": 0.05, "event": "DataSentry"}, {"at": 0.2, "event": "rule + dot"}, {"at": 0.3, "event": "one-line description"}],
    lead_silence_s=0.8),
 remotion("BDEFS", "terms",
    "Three terms. A data check: a rule a table must pass. A planted defect: a mistake put into a copy of the "
    "data on purpose. And a catch rate: the share of planted defects the checks find.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "data check", "meaning": "a rule a table must pass, like no missing fares"},
               {"term": "planted defect", "meaning": "a mistake put into a copy of the data on purpose"},
               {"term": "catch rate", "meaning": "the share of planted defects the checks find"}],
     "folderLabel": "@EthanGomes14"},
    [{"at": 0.12, "event": "'data check' lands"}, {"at": 0.45, "event": "'planted defect' lands"},
     {"at": 0.75, "event": "'catch rate' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

BODY = [
 # Q1 — what is it
 beat("B00", "what it is",
    "Data Sentry will be a workflow, built in Claude Code, that writes data checks for a table, then scores "
    "those checks by planting defects they have to catch.",
    "B00_Scanner", "A checkpoint scanner arch lands on the stage with its floor shadow; the name 'DataSentry' sits beside it; a parcel (the table) slides under the arch.",
    [{"at": 0.1, "event": "scanner lands"}, {"at": 0.35, "event": "label"}, {"at": 0.7, "event": "parcel rides in"}]),
 beat("B01", "what it is",
    "When it's done, it will be a public GitHub repo with three parts: a check writer, a defect planter, "
    "and a scorecard of what was caught and what was missed.",
    "B01_Repo", "A kraft crate (the repo) opens; three parts rise beside it one by one, a check page, a dark planter block, a binder; each labelled once.",
    [{"at": 0.15, "event": "crate opens"}, {"at": 0.45, "event": "check writer"}, {"at": 0.6, "event": "defect planter"}, {"at": 0.75, "event": "scorecard"}]),
 # how it will work
 beat("B02", "how it will work",
    "It will start from public data, for example one month of New York City yellow taxi trips, about ten thousand rows. "
    "Pick-up time, drop-off time, passengers, distance, and fare.",
    "B02_Table", "A flat table card lands; five column headers block in; grey rows stack down it as the columns are named.",
    [{"at": 0.15, "event": "table lands"}, {"at": 0.5, "event": "rows stack"}, {"at": 0.7, "event": "columns"}]),
 beat("B03", "how it will work",
    "Claude Code will see only the column names and types, and write checks in pandera, an open-source Python "
    "library for testing data frames. It will never see the list of defects.",
    "B03_Writer", "An agent workstation; check pages drop beside it; at right a sealed box marked 'defect list' sits behind a closed barrier.",
    [{"at": 0.1, "event": "workstation"}, {"at": 0.45, "event": "check pages drop"}, {"at": 0.8, "event": "sealed defect list"}]),
 beat("B04", "how it will work",
    "Separately, a plain Python script will copy the clean sample and break it five ways: "
    "duplicates, missing values, impossible numbers like a negative fare, a drop-off before its pick-up, "
    "and the wrong type.",
    "B04_Planter", "Two table cards side by side, clean and broken copy; five terracotta marks land on the broken copy, one per defect named.",
    [{"at": 0.15, "event": "copy appears"}, {"at": 0.45, "event": "defects land one by one"}, {"at": 0.9, "event": "five"}]),
 beat("B05", "how it will work",
    "Then every check runs twice. On the clean copy, it must pass. On the broken copy, it must fail. Out comes "
    "a catch rate for each kind of defect, with every miss written down.",
    "B05_TwoRuns", "The scanner from B00; the clean parcel rides through and gets a check; the broken parcel is stopped at the arch with a terracotta light.",
    [{"at": 0.15, "event": "clean parcel passes"}, {"at": 0.5, "event": "broken parcel stopped"}, {"at": 0.8, "event": "tally"}]),
 # Q2 — why care, real alternatives
 beat("B06", "why care",
    "Why would anyone care? I looked at two tools data teams already use. First, D B T. Its built-in tests "
    "check exactly what you write: unique, not null, accepted values, relationships.",
    "B06_Dbt", "Two comparison trays; the left tray fills with four small test blocks, one per built-in test named; label 'dbt'.",
    [{"at": 0.3, "event": "trays"}, {"at": 0.6, "event": "four test blocks drop"}]),
 beat("B07", "why care",
    "The second is Great Expectations. Its paid G X Cloud has a feature, Expect A I, that suggests checks "
    "for you to review and approve. So AI-suggested checks already exist.",
    "B07_Gx", "The right tray fills with suggested check pages; an approval stamp comes down on the top page; label 'GX Cloud'.",
    [{"at": 0.2, "event": "right tray"}, {"at": 0.5, "event": "suggested pages"}, {"at": 0.75, "event": "stamp"}]),
 beat("B08", "why care",
    "What I didn't find, in what I read, was a way to measure how good those checks are. Data Sentry will tell "
    "a data engineer which bad rows their checks would let through.",
    "B08_Gap", "Both trays stay; a broken parcel with a terracotta mark slides past both trays untouched; a question-mark tag lands beside it.",
    [{"at": 0.25, "event": "broken parcel slides past"}, {"at": 0.7, "event": "the gap"}]),
 # Q3 — who opens it
 beat("B09", "who opens it",
    "Who opens it? A hiring manager for a data engineering role. In the first minute, they'll run one "
    "command on a broken file and see each defect type: caught, or missed.",
    "B09_FirstMinute", "A terminal window (dark title bar) opens; a cursor types one grey command bar; five result rows land with a mark each; tagged 'constructed'.",
    [{"at": 0.2, "event": "window opens"}, {"at": 0.45, "event": "one command"}, {"at": 0.7, "event": "result rows"}]),
 # Q4 — what it proves
 beat("B10", "what it proves",
    "What would it prove? Four skills from this class: a prompt contract for each check, an agent loop that "
    "writes, runs, and revises, verification against a clean copy, and evaluation by catch rate.",
    "B10_Proves", "An evidence binder; its cover opens; four record sheets fan out in a row with ink numerals 1 to 4, one per skill named.",
    [{"at": 0.15, "event": "binder opens"}, {"at": 0.3, "event": "1"}, {"at": 0.45, "event": "2"}, {"at": 0.62, "event": "3"}, {"at": 0.75, "event": "4"}]),
 beat("B10A", "what it proves",
    "Once it's built, a reviewer could fairly conclude that I test an AI's output instead of trusting it. "
    "The evidence will be in the repo: the scorecard, the log of every round, and the prompts behind each check.",
    "B10A_Conclude", "A review desk; a check mark lands with 'tested, not trusted'; then three pieces of planned evidence (scorecard binder, log sheet, prompt page) slide onto the desk; tagged 'planned evidence'.",
    [{"at": 0.1, "event": "desk + reviewer"}, {"at": 0.35, "event": "tested, not trusted"}, {"at": 0.7, "event": "evidence lands"}]),
 # Q5 — in / out / first
 beat("B11", "scope",
    "In scope: one table, five defect types, one scorecard. Out of scope, on purpose: orchestration, so no "
    "Airflow. First to run: one defect, one check, one printed line. If it prints, it ran.",
    "B11_Scope", "A task queue; the waiting tasks stay ghosted; the next task slides forward onto the rail, a single printed line appears beside it with a check; label 'first run'.",
    [{"at": 0.15, "event": "queue"}, {"at": 0.5, "event": "out of scope stays back"}, {"at": 0.75, "event": "first run"}]),
 # Q6 — risk
 beat("B12", "risk",
    "What could sink it? Checks that are too loose. A check that passes everything catches nothing, and the "
    "score would still look fine. So the clean copy and the broken copy are both required, every time.",
    "B12_Loose", "A permission gate with its barrier raised; a broken parcel rides straight through; then the barrier comes down and the next broken parcel stops.",
    [{"at": 0.2, "event": "barrier up"}, {"at": 0.45, "event": "broken parcel slips through"}, {"at": 0.8, "event": "barrier down"}]),
 # Q7 — why this project
 beat("B13", "why this project",
    "Why this project? It will help me land a data job, like a Data Engineer or Data Analyst role. It will "
    "highlight the skills I'm working on: Python, pandas, pandera, and Claude Code in a loop that fixes its own "
    "checks.",
    "B13_Why", "A tray labelled 'working on' fills with four skill blocks, one per skill named; an arrow draws from the tray to the hiring manager's desk (from B10A), labelled 'Data Engineer' and 'Data Analyst'.",
    [{"at": 0.15, "event": "desk + roles"}, {"at": 0.5, "event": "skills drop in"}, {"at": 0.9, "event": "arrow to the role"}]),
 # exists vs will exist
 beat("B14", "honesty",
    "Where this stands today, October fourteenth, twenty twenty-six. What exists: this pitch, a written brief, "
    "and my notes on the two tools. What doesn't exist yet: the code, the defect planter, and any score.",
    "B14_Exists", "Two shelves: the left fills with three solid pages ('exists'); the right holds three dashed outlines that stay empty ('will exist').",
    [{"at": 0.3, "event": "exists"}, {"at": 0.65, "event": "will exist"}]),
 beat("BEND", "close",
    "That's Data Sentry. I'm Ethan Gomes. Thanks for watching.",
    "BEND_Close", "The scanner from B00 returns; the title and Ethan's name land beside it.",
    [{"at": 0.2, "event": "scanner"}, {"at": 0.5, "event": "title and name"}], tail_silence_s=1.0),
]

BEATS = OPEN + BODY

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "FINAL PROJECT · PITCH", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "ethan-gomes", "channel_title": "@EthanGomes14", "persona": "Ethan Gomes (narrated in first person; synthetic Kokoro voice)",
    "voice": VOICE, "voice_kokoro": VOICE, "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Plain", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none",
    "bookend_exempt": ["cold-open", "bvdt", "bhtf"],
    "bookend_exempt_reason": ("Course assignment (INFO 7375 Final Project Pitch Film): narrate as yourself, no instructor name, "
                              "persona, or credit line. No composer cold open, no verdict card, no Your Turn. The house outro "
                              "card (ClaudeTitleOutro) hard-codes @NikBearBrown, so the film closes on a drawn beat (BEND) instead; "
                              "bookend_check.py is expected to report the missing ClaudeTitleOutro, and that is recorded in FRICTIONAL.md."),
    "audience": "INFO 7375 instructor and TAs; a data engineering hiring manager",
    "source_doc": "PROJECT-BRIEF.md (2026-10-14); docs.getdbt.com/docs/build/data-tests (read 2026-10-14); "
                  "greatexpectations.io blog '2025 In Review' (2026-01-09, read 2026-10-14); nyc.gov TLC trip record data page",
    "playlist": "", "chapter_number": 0,
    "tags": ["data engineering", "data quality", "pandera", "Claude Code", "evaluation", "final project pitch"]},
    "beats": BEATS}

# carry measured audio forward when the narration is unchanged (show-tell gate trap 4)
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in BEATS:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
    dur = b.get("actual_duration_s")
    props = (b["shot"].get("remotion") or {}).get("props")
    if dur and props is not None and b["shot"]["remotion"]["pattern"] == "ClaudeDefinitions":
        props["durationSeconds"] = dur

p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
words = sum(len(b["narration_text"].split()) for b in BEATS)
print(len(BEATS), "beats;", words, "words; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in BEATS)), "s")
