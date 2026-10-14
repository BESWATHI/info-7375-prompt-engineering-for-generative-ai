#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for riya-k-ground-truth-sql (INFO 7375 final project pitch).

show-tell format (brutalist.art skills/make/show-tell): one drawn isometric picture per beat,
minimal labels, narration carries the idea. Adapted for a course pitch: narrated in the first
person as Riya (Kokoro af_bella, a synthetic voice); no instructor name, persona or credit
line; the outro handle is the author's name. Every number spoken comes from
evidence/run_slice_output*.txt (run 2026-10-09) or from the two alternatives' own pages
(read 2026-10-09). Anything not built yet is said with "will" and stamped CONSTRUCTED on screen.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "riya-k-ground-truth-sql"
TITLE = "Ground Truth SQL"
HANDLE = "Riya Kapadnis"
VOICE = "af_bella"
SPARSE = ("show-tell style: one drawn object or scene on a cream stage per beat, minimal labels, "
          "the voice carries the explanation. Only underfill and clustered are waived; edge-bleed, "
          "empty-frame and contrast still apply.")


def beat(bid, narration, cls, image, show, sparse=True):
    b = {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                  "manim": {"class": cls}, "motion_claim": image}}
    if sparse:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE}
    return b


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Namaste. I'm Riya Kapadnis, and this is my final project pitch for INFO seventy-three seventy-five. "
    "People ask whether an AI can write SQL. The better question is whether its SQL is right on your data, "
    "and how you would know.",
    "BrutalistHesitantWriter",
    {"text": "Is the AI's SQL\nany good", "triggerWords": "any good", "replacementWords": "right on my data",
     "fontSize": 76, "charMs": 24, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": "Ground Truth SQL · final project pitch · Riya Kapadnis · INFO 7375"},
    [{"at": 0.0, "event": "banner with title, name and course; types the naive question"},
     {"at": 0.6, "event": "'any good' corrected to 'right on my data'"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question and corrects it to the real one.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Text to SQL: a model turns a plain English question into a database query. A gold set: questions with answers I checked by hand. And execution match: judging a query by the rows it returns, not its wording."
    ,
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "text-to-SQL", "meaning": "turns English questions into SQL queries"},
               {"term": "gold set", "meaning": "the right SQL, checked by hand"},
               {"term": "execution match", "meaning": "judge SQL by its output table"}],
     "folderLabel": HANDLE.upper()},
    [{"at": 0.12, "event": "'text-to-SQL'"}, {"at": 0.45, "event": "'gold set'"}, {"at": 0.72, "event": "'execution match'"}],
    gate="CARD", qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

B = [
 beat("B00",
    "Here is the project. Ground Truth SQL will be an evaluation harness. You give it your database and a set of questions, "
    "and it tells you which questions the model gets wrong, and why.",
    "B00_WhatItIs",
    "A question page slides toward a dark database tower labelled 'Chinook'; a result tray lands beside it; a small "
    "terracotta mark appears on one wrong row block.",
    [{"at": 0.1, "event": "database tower"}, {"at": 0.3, "event": "question page"}, {"at": 0.6, "event": "result tray, one row flagged"}]),
 beat("B01",
    "When it's done, it will be a public GitHub repository with three parts: about fifty checked questions, a runner that asks Claude each one, and a scorecard listing every failure and its cause. Today, only a first slice exists."
    ,
    "B01_Repo",
    "An open kraft crate tagged 'repo' with a CONSTRUCTED stamp; three objects rise out in a row: a page stack "
    "('gold set'), a dark block ('runner'), a binder ('scorecard').",
    [{"at": 0.1, "event": "crate + CONSTRUCTED stamp"}, {"at": 0.3, "event": "gold set"}, {"at": 0.5, "event": "runner"}, {"at": 0.7, "event": "scorecard"}]),
 beat("B02",
    "Why care? A query can run, look right, and still be wrong. In my first test, a query I wrote by hand to copy a common join mistake put US revenue at four thousand six hundred sixty seven dollars. The real number is five hundred twenty three. Nine times too high, and no error."
    ,
    "B02_LooksRight",
    "Two bars side by side on a plinth: a short one '523' (checked) and a tall one '4,667' (join mistake) that grows "
    "about nine times taller; caption 'real run · 2026-10-09'.",
    [{"at": 0.1, "event": "plinth + checked bar 523"}, {"at": 0.45, "event": "wrong bar grows to 4,667"}, {"at": 0.8, "event": "9x"}]),
 beat("B03",
    "I looked at two alternatives. BIRD is a benchmark of over twelve thousand questions, but on its own ninety five databases, not yours. Vanna writes SQL for your own database, but I didn't find a way in it to test that SQL against checked answers. Mine does that: your schema, checked answers, and a reason for every failure."
    ,
    "B03_Alternatives",
    "Left: a tall shelf of many pages labelled 'BIRD'. Middle: a workstation labelled 'Vanna'. Right: the project's crate "
    "with a check, labelled 'your schema'.",
    [{"at": 0.1, "event": "BIRD shelf"}, {"at": 0.35, "event": "Vanna workstation"}, {"at": 0.7, "event": "your schema + check"}]),
 beat("B04",
    "The check is simple. Run the checked query and the model's query on the same read only database, and compare the rows. On my first eight questions, comparing the SQL text rejected all three correct rewrites. Comparing rows judged all nine test queries the way I did."
    ,
    "B04_CompareRows",
    "Two trays side by side, 'gold' and 'model'; matching row blocks drop into each; a scan line passes and a check lands; "
    "a counter reads '9/9'.",
    [{"at": 0.1, "event": "two trays"}, {"at": 0.3, "event": "rows drop in"}, {"at": 0.7, "event": "check, 9/9"}]),
 beat("B05",
    "It also caught me. My first gold answer asked about revenue in twenty twenty three, but this data stops in twenty "
    "thirteen. The checked answer was empty, so a broken query matched it. Now the runner rejects any empty gold answer.",
    "B05_EmptyGold",
    "The gold tray sits empty; a broken query's empty tray slides beside it and they 'match'; then a barrier drops "
    "in front of the empty gold tray.",
    [{"at": 0.15, "event": "empty gold tray"}, {"at": 0.4, "event": "empty broken tray matches"}, {"at": 0.75, "event": "barrier: rejected"}]),
 beat("B06",
    "Who opens it? A hiring manager or engineer screening AI engineers. In the first minute, they'll read the scorecard, replay the saved results with one command and no key, and open one failure beside its checked answer."
    ,
    "B06_Reviewer",
    "A review desk; a binder ('scorecard') opens on it; one page slides out ('one failure'); CONSTRUCTED stamp because "
    "the scorecard does not exist yet.",
    [{"at": 0.1, "event": "desk + CONSTRUCTED"}, {"at": 0.35, "event": "scorecard"}, {"at": 0.7, "event": "one failure page"}]),
 beat("B07",
    "What should it prove? That I evaluate models instead of trusting them: a prompt contract that allows one read only select, verification by running the SQL, failures sorted by cause, and later a repair loop I'll measure. The evidence will be dated logs anyone can re-run."
    ,
    "B07_Proves",
    "A row of four objects light up in turn: a contract page, a scanner gate, a sorted shelf, a loop arrow around a block.",
    [{"at": 0.15, "event": "contract"}, {"at": 0.35, "event": "verification"}, {"at": 0.55, "event": "failure list"}, {"at": 0.75, "event": "repair loop (later)"}]),
 beat("B08",
    "In: one public sample database, Chinook, about fifty questions, and Claude. Out: no chat app, no write queries, no claims about production data. First: the slice that runs today. Next: the first real Claude run on those eight questions, saved with its date."
    ,
    "B08_Scope",
    "A permission gate: 'Chinook' crate passes through; 'chat app' and 'write' blocks stay outside; a small 'first' tag "
    "on the existing slice.",
    [{"at": 0.15, "event": "in: Chinook"}, {"at": 0.45, "event": "out: blocked"}, {"at": 0.75, "event": "first: the slice"}]),
 beat("B09",
    "What could sink it? I write both the questions and the answers, so the test could be too easy, or wrong, like twenty twenty three. So a classmate will check a sample of my answers, unclear questions will be marked unclear, and each question will run three times."
    ,
    "B09_Risk",
    "One hand-held page ('my answers') on a desk; a second inspection lamp swings over it ('second check'); three small "
    "tokens appear in a row ('3 runs').",
    [{"at": 0.15, "event": "my answers"}, {"at": 0.45, "event": "second check"}, {"at": 0.75, "event": "3 runs"}]),
 beat("B10",
    "Why this project? It's a mix. SQL, Python, and building language model features into a BI product are skills I use in my AI engineer co-op, but that code is private, so my public evidence is this course's work. Evaluation sets, failure analysis, and measured repair loops are new to me, and that's what I want to learn."
    ,
    "B10_Why",
    "Two shelves: left 'have' with a stack of pages and a check; right 'learning' with an empty slot a block slides into.",
    [{"at": 0.15, "event": "have"}, {"at": 0.5, "event": "learning"}, {"at": 0.8, "event": "block slides into the slot"}]),
 beat("BCON",
    "So, what exists today is eight questions, one comparator, and one bug I caught in my own answers. Everything else is "
    "still to build. Models that write SQL are easy to find. Knowing when to trust them is the project.",
    "BCON_Close",
    "The crate from B01 returns, small and mostly empty: one page stack inside with a check ('exists'); the other slots "
    "ghosted ('will exist').",
    [{"at": 0.15, "event": "exists"}, {"at": 0.5, "event": "will exist (ghosted)"}, {"at": 0.8, "event": "closing line"}]),
]

OUTRO = {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
         "narration_text": f"{TITLE}.", "estimated_duration_s": 3.0, "voice": VOICE, "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates"}],
                  "remotion": {"pattern": "ClaudeTitleOutro",
                               "props": {"title": TITLE, "slug": SLUG, "handle": HANDLE, "subline": ""}}},
         "kind": "outro_voice", "tail_silence_s": 1.0}

# BOUT dropped (2026-10-10): ClaudeTitleOutro hardcodes @NikBearBrown + mascot; the assignment forbids the
# instructor credit line, so the film ends on BCON. See FRICTIONAL.md.
beats = OPEN + B
sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · FINAL PROJECT PITCH", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "riya-kapadnis", "channel_title": HANDLE, "persona": "Riya Kapadnis (synthetic voice, Kokoro af_bella)",
    "voice": VOICE, "voice_kokoro": VOICE, "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Plain", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hindi/Marathi (Namaste)",
    "bookend_exempt": ["cold-open", "bvdt", "bhtf"],
    "bookend_exempt_reason": ("Course pitch, not a channel explainer: opens on the hesitant writer + terms card per the show-tell "
                              "skill; no verdict card; no Your Turn (a pitch has no viewer task); ends on a spoken conclusion "
                              "beat (BCON) then the title outro. Instructor persona and credit line removed as the assignment requires."),
    "audience": "INFO 7375 instructor and TAs; a hiring manager screening AI Engineer candidates",
    "source_doc": "PROJECT-BRIEF.md; evidence/run_slice_output.txt and evidence/run_slice_output_v0_first_run.txt (run 2026-10-09); "
                  "bird-bench.github.io and github.com/vanna-ai/vanna (read 2026-10-09)",
    "tags": ["text-to-SQL", "evaluation", "Claude", "INFO 7375"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(beats), "beats; est", round(sum(b["estimated_duration_s"] for b in beats)), "s")
