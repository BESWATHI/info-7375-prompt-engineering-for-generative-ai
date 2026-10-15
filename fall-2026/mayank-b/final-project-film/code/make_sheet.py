#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for the Final Project Pitch Film
"Source Check for Support AI" (Mayank B., INFO 7375, 2026-10-14).

Built on the toolkit's show-tell skill (one drawn picture per beat, minimal labels, the voice
explains), with the assignment's overrides:
  * narrated as myself (first person, "I"); no instructor name, persona or credit line, so no
    "Liam, in for Bear" and no @NikBearBrown outro (the outro is the reel-local TcTitleOutro, @Mayank);
  * it is a pitch: nothing is built yet, so every sentence about the tool says "will", and every
    drawn body beat carries an on-screen "proposed design" tag;
  * no Your Turn beat (a pitch has no viewer prompt).
Every factual claim is listed in FACTCHECK.md. Run from anywhere: writes ../beat_sheet.json.
"""
import json
from pathlib import Path

REEL = Path(__file__).resolve().parents[1]
SLUG = "source-check-pitch"
TITLE = "Source Check for Support AI"
NAME_SPOKEN = "Muh-yunk"     # Kokoro reads "Mayank" as "May-ink"; the screen always shows "Mayank"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
    remotion("BIDEA", "the question",
             f"Hola, I'm {NAME_SPOKEN}, and this is my final project pitch. It starts with one question. "
             "Can a support bot answer policy questions from a current source?",
             "BrutalistHesitantWriter",
             {"text": "Can a support bot answer\npolicy questions safely", "triggerWords": "safely",
              "replacementWords": "from a current source", "fontSize": 70, "charMs": 24,
              "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
              "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'Can a support bot answer policy questions safely'"},
              {"at": 0.6, "event": "'safely' is deleted and retyped as 'from a current source'"}],
             lead_silence_s=0.8,
             motion_claim="The writer corrects a vague goal (safely) into the checkable one (from a current source).",
             qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms. A policy answer: anything a bot tells a customer about refunds, fees, or eligibility. "
             "A source: the dated policy document that answer relies on. "
             "And a hold: the answer waits for a person instead of being sent.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "policy answer", "meaning": "the bot's claims about refunds, fees, eligibility"},
                        {"term": "source", "meaning": "the dated policy behind the reply"},
                        {"term": "hold", "meaning": "the reply waits until staff decide"}],
              "folderLabel": ""},
             [{"at": 0.12, "event": "'policy answer' lands"}, {"at": 0.5, "event": "'source' lands"},
              {"at": 0.78, "event": "'hold' lands"}], gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "Terms card: three prerequisites, one line each."}),
]

BODY = [
    beat("B00", "This really happened. In 2024, a Canadian tribunal ruled on a case against Air Canada. "
                "The airline's chatbot told a customer he could claim a bereavement fare after he travelled. "
                "The policy said the request had to come before. The tribunal held the airline responsible for its chatbot.",
         "B00_RealCase", "A conveyor carries an answer parcel straight out to the customer with no check; a policy page beside it; a case caption.",
         [{"at": 0.1, "event": "conveyor and policy page"}, {"at": 0.3, "event": "answer parcel rides out unchecked"},
          {"at": 0.75, "event": "caption: Moffatt v. Air Canada, 2024"}]),
    beat("B01", "So my project is Source Check for Support AI. It will sit between a support bot and the customer, "
                "and check every policy answer against the company's current policy before it is sent.",
         "B01_Scanner", "The same conveyor, now with a checkpoint scanner arch over it; label 'Source Check'.",
         [{"at": 0.15, "event": "scanner arch rises over the conveyor"}, {"at": 0.65, "event": "label"}]),
    beat("B02", "Step one. Claude will break the bot's answer into claims, like 'refund after travel', "
                "and return them in a fixed format that my code checks before using them.",
         "B02_Claims", "The answer parcel opens; three claim pages rise out of it in a row.",
         [{"at": 0.2, "event": "parcel lid lifts"}, {"at": 0.35, "event": "three claim pages rise"}]),
    beat("B03", "Step two. Python code, not the model, will look up the current, dated version of the policy, "
                "and compare each claim with it: the numbers, the dates, and conditions like before or after.",
         "B03_Versions", "Version shelves; the newest policy page slides out; it lands beside a claim page in comparison trays.",
         [{"at": 0.2, "event": "shelves"}, {"at": 0.35, "event": "current version slides out"},
          {"at": 0.7, "event": "claim and policy side by side"}]),
    beat("B04", "If every claim matches, the answer goes out, and a log records which policy version it relied on.",
         "B04_Pass", "A permission gate barrier lifts; the parcel passes; a check and a log page appear.",
         [{"at": 0.2, "event": "barrier lifts"}, {"at": 0.6, "event": "log page with a check"}]),
    beat("B05", "If a claim has no source, relies on an outdated version, or contradicts the policy, the answer is held. "
                "A person sees the reason in Slack and decides.",
         "B05_Hold", "The parcel is diverted to a human handoff desk; label 'HOLD'; a person marker appears.",
         [{"at": 0.2, "event": "handoff desk"}, {"at": 0.35, "event": "parcel slides to the person"}, {"at": 0.7, "event": "HOLD label"}]),
    beat("B06", "An n8n workflow will run all of this: answer in, check, then pass or hold. "
                "It works in front of any bot, so it doesn't replace one.",
         "B06_Router", "A branch junction: the packet chooses the pass route or the hold route; labels 'pass' and 'hold'.",
         [{"at": 0.2, "event": "junction"}, {"at": 0.35, "event": "packet routes"}, {"at": 0.7, "event": "labels"}]),
    beat("B07", "I looked at three alternatives: Intercom Fin, Zendesk's AI agents, and manual review of transcripts. "
                "The two products answer from your help content and hand off to people. Manual review happens after the answer is sent. "
                "What I didn't find on their public pages is a check of each answer against the current policy version before it goes out.",
         "B07_Alternatives", "Three trays labelled Fin, Zendesk, manual; a fourth tray with the scanner mark; the gap is the check before sending.",
         [{"at": 0.15, "event": "three trays"}, {"at": 0.7, "event": "the fourth tray: check before sending"}]),
    beat("B08", "Who opens it? A hiring manager for an AI automation engineer. "
                "In the first minute they'll run one command and watch an outdated refund answer get held, with the reason.",
         "B08_Demo", "A workstation monitor; a terminal line appears; a HOLD tag comes back.",
         [{"at": 0.2, "event": "workstation"}, {"at": 0.35, "event": "command"}, {"at": 0.7, "event": "HOLD returns"}]),
    beat("B09", "What it will prove: prompt contracts, source grounding, verification, approval gates, and evaluation. "
                "The evidence will be tests and a labelled test set, with the miss rate reported. It won't prove it's ready for production.",
         "B09_Evidence", "An evidence binder opens; test pages and an evaluation page come out.",
         [{"at": 0.2, "event": "binder"}, {"at": 0.35, "event": "cover opens"}, {"at": 0.7, "event": "evidence pages"}]),
    beat("B10", "The scope. It will only check policy answers for one fictional company, on synthetic data. It won't write answers. "
                "The first piece will be the checker and one test: the Air Canada case must come out held.",
         "B10_FirstTest", "An experiment bench; one test sample slides in; a terracotta light comes on.",
         [{"at": 0.2, "event": "bench"}, {"at": 0.35, "event": "test sample inserted"}, {"at": 0.75, "event": "light"}]),
    beat("B11", "What could sink it: a dropped condition word. If extraction turns before into after, a wrong answer could pass. "
                "So uncertain answers will default to hold, and my test set will be full of condition flips.",
         "B11_Risk", "An inspection lamp swings onto a claim page; labels 'before' and 'after'.",
         [{"at": 0.2, "event": "lamp and page"}, {"at": 0.35, "event": "lamp head focuses"}, {"at": 0.7, "event": "before / after"}]),
    beat("B12", "Why this project? I've already built n8n workflows with Claude in my public repos. "
                "What's new for me is building an evaluation set and measuring the misses. "
                "And Week one taught me that a confident answer isn't a checked one.",
         "B12_Skills", "A skill stack; one page lifts out (new); labels 'have' and 'new'.",
         [{"at": 0.2, "event": "stack of pages (have)"}, {"at": 0.4, "event": "one page lifts (new)"}]),
    beat("B13", "Today, three things exist: the project brief, the research behind it, and this film. "
                "The workflow, the checker, and the tests will come next.",
         "B13_ExistsWill", "Two trays: 'exists' holds three real pages; 'will exist' holds three ghost outlines.",
         [{"at": 0.2, "event": "two trays"}, {"at": 0.35, "event": "three pages in 'exists'"}, {"at": 0.7, "event": "three ghost outlines in 'will exist'"}]),
]

SPARSE_REASON = ("show-tell style: one drawn object or scene on a cream stage per beat, minimal labels, with the voice "
                 "carrying the explanation. Only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in BODY:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

OUT = {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
       "narration_text": f"{TITLE}. At {NAME_SPOKEN}.", "estimated_duration_s": 4.0,
       "voice": "am_onyx", "engine": "kokoro",
       "tts_note": "'Mayank' respelled for Kokoro; the screen shows @Mayank.",
       "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; @Mayank; mascot"}],
                "remotion": {"pattern": "TcTitleOutro", "props": {"title": TITLE + ".", "slug": SLUG + "-film", "handle": "@Mayank",
                                                          "showMascot": False, "inkPeriod": True}}},
       "kind": "outro_voice", "tail_silence_s": 1.0}

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "FINAL PROJECT PITCH", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "mayank", "persona": "Mayank (narrating as myself)", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "engine": "kokoro", "clock": "narration", "palette": "claude", "register": "plain", "fps": 24, "aspect_ratio": "16:9",
    "caption_policy": "none", "greeting_language": "Spanish (Hola)", "folderLabel": "@Mayank", "in_for_bear": False,
    "bookend_exempt": ["cold-open", "bvdt", "handoff"],
    "bookend_exempt_reason": ("Pitch film (INFO 7375 Final Project Pitch): show-tell bookends (hesitant writer + terms card) "
                              "with no verdict card and no Your Turn prompt; the assignment requires narrating as myself, "
                              "so no instructor persona or credit line; the outro is the reel-local TcTitleOutro (@Mayank)."),
    "audience": "hiring managers for AI automation engineers; INFO 7375 reviewers",
    "source_doc": "PROJECT-BRIEF.md (2026-10-14); Moffatt v. Air Canada (BC CRT, 2024); fin.ai public page (read 2026-10-14)",
    "honesty": "pitch only: nothing is built; tool described in 'will'; body beats tagged 'proposed design' on screen",
    "tags": ["AI automation", "n8n", "Claude", "support AI", "source grounding", "INFO 7375"]},
    "beats": OPEN + BODY + [OUT]}

(REEL / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(sheet["beats"]), "beats; est", round(sum(b["estimated_duration_s"] for b in sheet["beats"])), "s;",
      sum(len(b["narration_text"].split()) for b in sheet["beats"]), "words")
