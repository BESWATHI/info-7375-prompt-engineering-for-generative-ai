#!/usr/bin/env python3
"""make_sheet.py: writes beat_sheet.json for the AI Product Failure Lab pitch film (show-tell style).

Authorship (see SOURCES.md):
- Narration ideas and first-draft script: Aditya Hasija (storyboard doc, 2026-10-14).
- Scene flow and visual direction of that storyboard: drafted by ChatGPT from Aditya's notes.
- This revision: Claude (Claude Code), 2026-10-14. It fits the script to the updated scope, the seven assignment
  questions, the honesty rule, the baseline tests in research/, and the Brutalist show-tell format.

Honesty conventions used in every beat:
- Past tense only for things that exist: the idea, the blueprint doc, and the baseline tests in research/.
- Every drawing of the unbuilt product carries the on-screen tag "constructed" (assignment: mock-ups labelled).
- Beats that show the real baseline test carry "real test · Oct 14".
- No instructor persona: narrated in first person as Aditya. The outro handle is his name.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "ai-product-failure-lab-pitch"
TITLE = "AI Product Failure Lab"
NAME = "Aditya Hasija"
VOICE = "am_michael"   # chosen by Aditya 2026-10-14 from voice-samples/. Not am_onyx (the instructor persona's voice).

TAG_C = "constructed"            # drawing of something that does not exist yet
TAG_R = "real test · Oct 14"     # drawing that summarises the real baseline in research/


def beat(bid, narration, cls, image, show, tag, labels):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": VOICE, "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image,
                     "labels": labels, "honesty_tag": tag}}


B = [
 beat("B00",
  "Most ideas don't fail on day one. They fail months later, on an assumption nobody checked. "
  "I want to catch that assumption before anyone builds.",
  "B00_IdeaBox",
  "A kraft idea box drops onto the stage. Its lid lifts and three pages rise; one page's outline turns terracotta and a crack line draws across it.",
  [{"at": 0.1, "event": "box drops"}, {"at": 0.4, "event": "pages rise"}, {"at": 0.75, "event": "one page cracks"}],
  TAG_C, ["idea", "assumption"]),

 beat("B01",
  "I'm proposing the AI Product Failure Lab. A product manager gives it an idea and public sources, "
  "and it will return a pre-mortem: five failure risks, every claim labelled, and three tests to run first.",
  "B01_InOut",
  "The idea box and a source binder slide into a dark machine block; three report pages slide out on the other side, one after another.",
  [{"at": 0.15, "event": "box + binder enter"}, {"at": 0.5, "event": "machine lights"}, {"at": 0.7, "event": "three pages out"}],
  TAG_C, ["sources", "pre-mortem"]),

 beat("B02",
  "It will live in a GitHub repository: a small web app, a test set of made-up product ideas, and a log that scores it.",
  "B02_Repo",
  "A release parcel opens; a browser window, a fan of test cards and a log page rise out of it.",
  [{"at": 0.15, "event": "parcel opens"}, {"at": 0.4, "event": "app"}, {"at": 0.6, "event": "test cards"}, {"at": 0.8, "event": "log"}],
  TAG_C, ["GitHub repo"]),

 beat("B03",
  "Inside, an orchestrator will pass the idea to market, customer and risk agents. "
  "An evaluator will challenge what they found, and can send one back once. One retry, never a loop.",
  "B03_Agents",
  "A junction routes the idea packet to three dark agent blocks; their pages travel to a review desk under a lamp; one page goes back to one block exactly once, then returns.",
  [{"at": 0.15, "event": "packet splits to three blocks"}, {"at": 0.5, "event": "pages reach review desk"}, {"at": 0.8, "event": "one page sent back once"}],
  TAG_C, ["market", "customer", "risk"]),

 beat("B04",
  "Before pitching it, I tested the obvious alternative: just asking a chatbot. "
  "I gave plain Claude and ChatGPT the same idea, with a fake statistic planted in it. Both caught the fake number.",
  "B04_Baseline",
  "Two comparison trays, each holding one idea page with a planted number; a terracotta check lands on the planted number in each tray.",
  [{"at": 0.2, "event": "two trays"}, {"at": 0.5, "event": "planted number appears"}, {"at": 0.8, "event": "both checks land"}],
  TAG_R, ["Claude", "ChatGPT"]),

 beat("B05",
  "But in three runs, plain Claude cited no sources, yet stated claims as facts. "
  "ChatGPT sourced just two paragraphs and left most claims unlabelled. You can't tell evidence from guesses.",
  "B05_Gap",
  "The same two trays: lines of claims fill each page in grey; source dots appear next to claims: none in the Claude tray; in the ChatGPT tray, dots beside just two paragraphs. A large ink 0 rises over the Claude tray.",
  [{"at": 0.2, "event": "claim lines fill"}, {"at": 0.5, "event": "source dots: 0 and 2"}, {"at": 0.75, "event": "hero 0"}],
  TAG_R, ["0"]),

 beat("B06",
  "Paid tools exist too. DimeADozen's homepage promises hundred-page validation reports with hundreds of citations. "
  "I haven't bought one, so I can't judge them.",
  "B06_PaidReport",
  "A very thick stack of report pages builds up beside a price tag; a question mark draws over the stack.",
  [{"at": 0.2, "event": "stack builds"}, {"at": 0.55, "event": "price tag"}, {"at": 0.8, "event": "question mark"}],
  TAG_C, ["paid report"]),

 beat("B07",
  "Here's what will be different. Every claim will get a label, and code, not the model, will check each citation against the sources. "
  "The test scores will be public, including where it loses.",
  "B07_Scanner",
  "Claim pages ride a conveyor through a checkpoint scanner beside the source binder; each page gets a tag, ink for sourced, grey for guess; one page fails the scan and is tagged guess.",
  [{"at": 0.15, "event": "pages ride in"}, {"at": 0.4, "event": "scan beam"}, {"at": 0.7, "event": "tags: sourced / guess"}],
  TAG_C, ["sourced", "guess"]),

 beat("B08",
  "Who opens it? A hiring manager for AI product roles. In the first minute, they'll read the README, "
  "one real sample report, and the score table against plain chat.",
  "B08_FirstMinute",
  "Three pages land on a desk in order, each with a one-word label; a cursor touches each in turn.",
  [{"at": 0.2, "event": "README"}, {"at": 0.45, "event": "report"}, {"at": 0.7, "event": "scores"}],
  TAG_C, ["README", "report", "scores"]),

 beat("B09",
  "What should it prove? That I can write prompt contracts, instructions plus a schema each agent's output must pass, "
  "and then measure whether they held. It won't prove I'm a machine learning engineer.",
  "B09_Contract",
  "A skill page and a gate: an agent's output parcel reaches the gate; the barrier lifts only after the parcel's shape matches the outline on the page.",
  [{"at": 0.2, "event": "contract page"}, {"at": 0.5, "event": "parcel at gate"}, {"at": 0.75, "event": "shape matches, barrier lifts"}],
  TAG_C, ["contract", "schema"]),

 beat("B10",
  "The evidence will be saved run logs, the score table, and a written list of where it failed.",
  "B10_Binder",
  "The evidence binder's cover opens; three tabbed sections slide out: logs, scores, failures.",
  [{"at": 0.2, "event": "cover opens"}, {"at": 0.5, "event": "logs, scores"}, {"at": 0.8, "event": "failures tab"}],
  TAG_C, ["logs", "failures"]),

 beat("B11",
  "What comes first: the risk agent and the evaluator, on one test idea, from the command line. "
  "You'll know it ran when a run log appears that passes the schema check.",
  "B11_FirstRun",
  "One idea parcel rides a short conveyor past one agent block and the review desk; a single log page drops out and a check draws on it.",
  [{"at": 0.15, "event": "one parcel"}, {"at": 0.5, "event": "agent + evaluator"}, {"at": 0.8, "event": "log page + check"}],
  TAG_C, ["first run"]),

 beat("B12",
  "What it will never do: give a percent chance of success, turning guesses into a probability. "
  "Live web search, accounts and forecasts are out too.",
  "B12_NoScore",
  "A parcel stamped with a percent sign rides up to a permission gate; the barrier drops and blocks it; it slides off the stage.",
  [{"at": 0.2, "event": "% parcel"}, {"at": 0.5, "event": "barrier drops"}, {"at": 0.8, "event": "parcel removed"}],
  TAG_C, ["no score"]),

 beat("B13",
  "What could sink it? The evaluator rubber-stamps, the same model grading its own team. "
  "Chatbots already catch obvious fakes, so my test ideas will plant subtler flaws, like a price that contradicts the audience.",
  "B13_RubberStamp",
  "A flawed page (a hairline terracotta crack) slides under an approval stamp; the stamp comes down and approves it anyway.",
  [{"at": 0.2, "event": "flawed page"}, {"at": 0.5, "event": "stamp descends"}, {"at": 0.8, "event": "approved anyway"}],
  TAG_C, ["rubber stamp"]),

 beat("B14",
  "So I'll count how many planted flaws it catches. If that number is low, I'll move checks out of the model "
  "and into plain code, and report the result either way.",
  "B14_CatchRate",
  "Sample cards with planted flaws slide into an experiment bench one by one; a tally of marks grows; a small dark code block docks next to the review desk.",
  [{"at": 0.2, "event": "samples in"}, {"at": 0.5, "event": "tally grows"}, {"at": 0.8, "event": "code block docks"}],
  TAG_C, ["catch rate"]),

 beat("B15",
  "Why this project? It's a mix. Requirements and challenging assumptions are years of my product work; "
  "WorkShip and SkillPort are on my GitHub. New to me: agent orchestration and evaluation design.",
  "B15_Shelves",
  "Two shelves: the left one already holds three filled blocks; on the right shelf, three outlined empty slots draw in.",
  [{"at": 0.2, "event": "have shelf"}, {"at": 0.6, "event": "new shelf outlines"}],
  None, ["have", "new"]),

 beat("B16",
  "So, where it stands. What exists today: the idea, a blueprint I drafted with ChatGPT, and those chatbot tests. "
  "Everything else I will build with Claude Code, in two weeks.",
  "B16_Status",
  "Two trays: a small 'exists' tray with three items, and a long 'will build' tray whose slots are dashed outlines that draw in one by one.",
  [{"at": 0.2, "event": "exists tray"}, {"at": 0.55, "event": "will build outlines"}],
  None, ["exists", "will build"]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
  "Hi, I'm Aditya Hasija. Every product starts with one question: will it work? "
  "I think the more useful question is how it will fail.",
  "BrutalistHesitantWriter",
  {"text": "Will my product idea work?", "triggerWords": "work?", "replacementWords": "fail?",
   "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
   "seed": SLUG, "banner": ""},
  [{"at": 0.0, "event": "types 'Will my product idea work?'"}, {"at": 0.6, "event": "backspaces 'work?' → 'fail?' on the spoken correction"}],
  lead_silence_s=0.8, motion_claim="The writer types the hopeful question and corrects it to the useful one: how will it fail.",
  qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 beat("BDEFS",
  "Two terms. A pre-mortem: you imagine the product has already failed, and ask why. "
  "And an evaluator: an agent that checks the other agents' work.",
  "BDEFS_Terms",
  "Left: a cracked idea crate with a question mark rising from it (pre-mortem). Right: a review desk where a page lands under a lamp (evaluator). One label each.",
  [{"at": 0.15, "event": "cracked crate + ?"}, {"at": 0.6, "event": "review desk + page"}],
  None, ["pre-mortem", "evaluator"]),
]

SPARSE_REASON = ("show-tell style: one drawn object or scene on a cream stage per beat, minimal labels, voice carries the "
                 "explanation. Only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B + [OPEN[1]]:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

BEATS = OPEN + B
BEATS.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
              "narration_text": f"{TITLE}. {NAME}.", "estimated_duration_s": 4.0, "voice": VOICE, "engine": "kokoro",
              "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; name"}],
                       "remotion": {"pattern": "ClaudeTitleOutro",
                                    "props": {"title": TITLE, "slug": SLUG, "handle": NAME, "subline": ""}}},
              "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "PITCH · FINAL PROJECT", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "aditya-hasija", "channel_title": NAME, "persona": f"{NAME} (first person)",
    "voice": VOICE, "voice_kokoro": VOICE, "voice_note": "Synthetic local Kokoro voice reading Aditya's script in first person (disclosed in SOURCES.md).",
    "engine": "kokoro", "clock": "narration", "palette": "claude", "register": "Plain", "fps": 24, "aspect_ratio": "16:9",
    "width": 3840, "height": 2160, "caption_policy": "none",
    "bookend_exempt": ["cold-open", "bvdt", "bhtf"],
    "bookend_exempt_reason": ("Course pitch film (INFO7375 final project pitch, 2–4 min): opens on the hesitant writer + terms card, "
                              "no verdict card, and no Your Turn beat, which would spend runtime on a viewer exercise "
                              "instead of the seven required pitch answers. The spoken outro stays."),
    "audience": "INFO7375 instructor and TAs; hiring managers for AI product manager roles",
    "source_doc": "PROJECT-BRIEF.md; research/ (baseline tests 2026-10-14); dimeadozen.ai homepage (read 2026-10-14)",
    "honesty": "Past tense only for the idea, the blueprint doc and the baseline tests. Drawings of the unbuilt product are tagged 'constructed'.",
    "tags": ["AI product management", "pre-mortem", "multi-agent", "evaluation", "Claude"]},
    "beats": BEATS}

# Carry measured audio forward (show-tell trap 4): a re-run of this script must not drop audio_file / actual_duration_s.
_old = HERE / "beat_sheet.json"
if _old.exists():
    prev = {b["beat_id"]: b for b in json.loads(_old.read_text())["beats"]}
    for b in BEATS:
        p = prev.get(b["beat_id"], {})
        if p.get("narration_text") == b["narration_text"]:
            for k in ("audio_file", "actual_duration_s"):
                if k in p:
                    b[k] = p[k]
for b in BEATS:
    if b["beat_id"] == "BDEFS" and "actual_duration_s" in b and "remotion" in b["shot"]:
        b["shot"]["remotion"]["props"]["durationSeconds"] = b["actual_duration_s"]

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
words = sum(len(b["narration_text"].split()) for b in BEATS)
print(f"{len(BEATS)} beats; {words} narration words; est {round(sum(b['estimated_duration_s'] for b in BEATS))} s at 2.5 words/s")
for b in BEATS:
    print(f"  {b['beat_id']:6} {len(b['narration_text'].split()):3}w  {b['estimated_duration_s']:5.1f}s")
