#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for gistgap-pitch (the GistGap final-project pitch film).

Show-tell style: one drawn picture per beat (B01-B13, Manim, scenes.py) and one
ShowTellCard (B14, the title). Voice: Kokoro af_bella. No persona, no channel handle,
no outro beat, no composer bookends.

Re-run after audio generation: it keeps each beat's measured actual_duration_s and
audio_file, and writes the card's durationSeconds from the measured audio.
Do NOT re-run after `art final`: it rewrites the sheet and drops the build stamps.

B12's rows are frozen literal text: four of Prasad Shinde's commits in fall-2026/prasad-s/
(1a6aa5b, 2eb73eb, 2a1f40f, fe9c16c), newest first, as `git log --format='%h %s' --
fall-2026/prasad-s/` printed them on 2026-10-09. This script does not run git.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "gistgap-pitch"
TITLE = "GistGap: What You See Is What You Sign"

old = {}
if (HERE / "beat_sheet.json").exists() and (HERE / "beat_sheet.json").stat().st_size:
    old = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}


def carry(b):
    """Keep measured audio from a previous run (the audio script writes these)."""
    o = old.get(b["beat_id"], {})
    for k in ("actual_duration_s", "audio_file"):
        if k in o:
            b[k] = o[k]
    return b


def est(narration):
    return round(len(narration.split()) / 2.5, 1)


SPARSE = ("show-tell style: one drawn picture per beat on a cream stage with minimal labels; "
          "the voice carries the explanation. Only underfill and clustered are waived; "
          "edge-bleed, empty-frame and contrast still apply.")


def drawn(bid, narration, cls, tag, intent, show):
    return carry({
        "beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration, "estimated_duration_s": est(narration),
        "voice": "af_bella", "engine": "kokoro",
        "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": intent, "show": show,
                 "manim": {"class": cls, "tag": tag}, "motion_claim": intent},
        "qc": {"sparse_by_design": True, "sparse_reason": SPARSE}})


def card(bid, narration, props, show, why):
    return carry({
        "beat_id": bid, "act": "show-tell", "lane": "card", "proof_gate": "CARD",
        "narration_text": narration, "estimated_duration_s": est(narration),
        "voice": "af_bella", "engine": "kokoro", "why_a_card": why,
        "shot": {"type": "REMOTION", "source": "own", "show": show,
                 "remotion": {"pattern": "ShowTellCard", "props": props}}})


# Frozen 2026-10-09: four of Prasad Shinde's commits in fall-2026/prasad-s/, newest first,
# hash and subject exactly as `git log --format='%h %s' -- fall-2026/prasad-s/` prints them.
B12_ROWS = [
    "1a6aa5b docs(prasad-s): close out FRICTIONAL log - B03 fix, final-path patch, export",
    "2eb73eb docs(prasad-s): checkpoint 3 - week-01 video built, exported (1080p final) and reviewed",
    "2a1f40f docs(prasad-s): checkpoint 2 - evidence packet (temp 1.0 vs 0.5) and pipeline check",
    "fe9c16c docs(prasad-s): checkpoint 1 - brutalist.art environment stood up",
]


N = {
 "B01": "Imagine an AI agent about to spend your money. You tap Approve. But what, exactly, are you approving?",
 "B02": "Two things matter here. What you're shown: the plain-English text on the screen. And what you sign: the exact terms, called a mandate. They should match.",
 "B03": "Here's an invented example. The cover page says fifty dollars, but page twelve says five hundred a month. That's the gap between the gist and the signed terms.",
 "B04": "GistGap will be a web demo that tests whether the text shown to someone approving an agent's payment matches the signed terms. It will be a public GitHub repository with a demo page, a test set, and a results table.",
 "B05": "It's for whoever owns an agent-payment approval screen. Before launch, they will be able to test, with synthetic data, whether the text drops or changes a cap, an amount, an expiry, or a recurrence.",
 "B06": "I looked at two existing things. Google's AP2: I read the announcement post and the main spec page. And a buildathon repo: I read its README only. AP2 defines how mandates are signed and checked, and the repo checks payments against its own mandates. In what I read, neither tests the text a person is shown. GistGap will.",
 "B07": "The target role is product manager for AI agent products. The reader is a hiring manager or an engineer. In the first sixty seconds, they will click three constructed examples and read the results table.",
 "B08": "It will show four skills from this course: prompt contracts, verification, evaluation, and source grounding. The evidence will be the test set, the results table, dated Claude outputs, and predictions I commit before each run. It will not show that this works on real payments.",
 "B09": "In scope: five fields. Amount, merchant, spending cap, expiry date, and one-time versus recurring.",
 "B10": "Out of scope: real signing, real payments, protocol compliance, and checking what the user originally asked for. First, I will run ten constructed mandates, three with planted errors. I will know it ran if it flags exactly those three. I'll commit my prediction first.",
 "B11": "The biggest risk: AP2 requires the display to be non-agentic, so the problem may be smaller than I think. I haven't examined any implementation. If so, I'll narrow the project. A second risk: matching text is brittle, because the same amount can be written several ways.",
 "B12": "This is a mix, mainly learning. Payments and agent-payment protocols are new to me. What I already have is the Assignment 1 film and the commit trail you can see here. I want to learn fintech and break into fintech product management.",
 "B13": "Today, what exists is the brief, the beat sheet, and this film. The project itself does not exist yet. It will be the generator, the checker, the test set, the demo page, and the results table.",
 "B14": "GistGap: what you see is what you sign.",
}

B = [
 drawn("B01", N["B01"], "B01_Agent", "SKETCH",
       "A robot holding a shopping bag stands beside a phone; a cursor taps the Approve button; a question mark appears.",
       [{"at": 0.0, "event": "robot with bag"}, {"at": 0.2, "event": "phone with Approve"},
        {"at": 0.5, "event": "cursor taps Approve"}, {"at": 0.8, "event": "?"}]),
 drawn("B02", N["B02"], "B02_ShownSigned", "SKETCH",
       "A box labelled SHOWN appears, then a taped box labelled SIGNED; a question mark lands between them.",
       [{"at": 0.15, "event": "SHOWN box"}, {"at": 0.5, "event": "SIGNED box"}, {"at": 0.9, "event": "?"}]),
 drawn("B03", N["B03"], "B03_Contract", "CONSTRUCTED",
       "A contract stack: the cover page reads $50; page 12 slides out and reads $500 / month; a curve joins them.",
       [{"at": 0.2, "event": "cover, $50"}, {"at": 0.45, "event": "page 12, $500 / month"}, {"at": 0.75, "event": "curve joins them"}]),
 drawn("B04", N["B04"], "B04_Browser", "WILL EXIST",
       "A browser window: the mandate's fields on the left, the shown text on the right, and a check lands between each matching row.",
       [{"at": 0.0, "event": "window, mandate, text"}, {"at": 0.4, "event": "checks land between rows"}]),
 drawn("B05", N["B05"], "B05_Checklist", "SKETCH",
       "A launch checklist: two rows get checks; the third box, 'approval text tested?', stays empty and a dot marks it.",
       [{"at": 0.0, "event": "checklist"}, {"at": 0.3, "event": "two checks"}, {"at": 0.55, "event": "approval text tested?"}]),
 drawn("B06", N["B06"], "B06_Landscape", "SKETCH",
       "Two boxes, AP2 and buildathon repo, appear; arrows run from both to a taped GistGap box.",
       [{"at": 0.1, "event": "AP2"}, {"at": 0.35, "event": "buildathon repo"}, {"at": 0.8, "event": "arrows to GistGap"}]),
 drawn("B07", N["B07"], "B07_Examples", "CONSTRUCTED / WILL EXIST",
       "Three example cards; a cursor clicks; a check lands on 'clean' and crosses on 'hidden cap' and 'changed amount'.",
       [{"at": 0.0, "event": "three cards"}, {"at": 0.75, "event": "check, cross, cross"}]),
 drawn("B08", N["B08"], "B08_Skills", "WILL EXIST",
       "Four icons arrive one by one: prompt contracts (a page), verification (a check), evaluation (bars), source grounding (a linked page and field).",
       [{"at": 0.15, "event": "prompt contracts"}, {"at": 0.22, "event": "verification"},
        {"at": 0.28, "event": "evaluation"}, {"at": 0.35, "event": "source grounding"}]),
 drawn("B09", N["B09"], "B09_Fields", "WILL EXIST",
       "Five dark bases; a box drops onto each as its field is named: amount, merchant, cap, expiry, recurring.",
       [{"at": 0.25, "event": "amount"}, {"at": 0.4, "event": "merchant"}, {"at": 0.55, "event": "cap"},
        {"at": 0.7, "event": "expiry"}, {"at": 0.9, "event": "recurring"}]),
 drawn("B10", N["B10"], "B10_ScopeTest", "WILL EXIST",
       "Left: four out-of-scope items, each with a cross beside it. Right: ten dots; three turn terracotta; rings mark exactly those three.",
       [{"at": 0.05, "event": "out-of-scope items crossed"}, {"at": 0.4, "event": "ten dots"},
        {"at": 0.5, "event": "three terracotta"}, {"at": 0.75, "event": "rings on those three"}]),
 drawn("B11", N["B11"], "B11_Shrink", "SKETCH",
       "A large box shrinks inside the outline of its old size; 'smaller problem?' appears beside it.",
       [{"at": 0.0, "event": "box"}, {"at": 0.3, "event": "box shrinks, outline stays"}, {"at": 0.3, "event": "smaller problem?"}]),
 drawn("B12", N["B12"], "B12_GitLog", "REAL - git log, Oct 9",
       "A panel lists four of Prasad's commits in this folder, frozen on Oct 9 (hash and subject); a trail line with a dot per commit draws beside them.",
       [{"at": 0.0, "event": "five commit rows"}, {"at": 0.6, "event": "commit trail draws"}]),
 drawn("B13", N["B13"], "B13_Columns", "EXISTS TODAY / WILL EXIST (column headers)",
       "Two columns: EXISTS TODAY (the brief, the beat sheet, this film) and WILL EXIST (the generator, the checker, the test set, the demo page, the results table), each item arriving as it is spoken.",
       [{"at": 0.0, "event": "EXISTS TODAY items"}, {"at": 0.6, "event": "WILL EXIST items, one per phrase"}]),
 card("B14", N["B14"],
      {"kind": "masked", "word": "GistGap", "sub": "What you see is what you sign"},
      [{"at": 0.1, "event": "GistGap fills from below inside its outline"}, {"at": 0.3, "event": "the line rises in"}],
      "Card test: (1) the idea is a name and a title; (2) the word filling its own outline IS the beat; "
      "(3) no drawing of the film's objects says a name more clearly."),
]

for b in B:
    if b["beat_id"] == "B12":
        b["shot"]["manim"]["rows"] = B12_ROWS
    if b["lane"] == "card":
        b["shot"]["remotion"]["props"]["durationSeconds"] = max(2.0, b.get("actual_duration_s") or b["estimated_duration_s"])

sheet = {"metadata": {
    "slug": SLUG,
    "title": TITLE,
    "topic": "GISTGAP · FINAL PROJECT PITCH",
    "skill": "show-tell",
    "style_preset": "show-tell",
    "channel": "gistgap",
    "voice": "af_bella",
    "voice_kokoro": "af_bella",
    "engine": "kokoro",
    "clock": "narration",
    "fps": 24,
    "aspect_ratio": "16:9",
    "width": 3840,
    "height": 2160,
    "caption_policy": "none",
    "bookend_exempt": ["cold-open", "bvdt", "bhtf"],
    "bookend_exempt_reason": ("Course pitch film, not a channel episode: it opens on the problem (B01) instead of a "
                              "composer cold open, has no verdict card and no Your Turn composer, and carries no "
                              "channel handle or persona. It also has no BOUT outro, which bookend_check.py cannot "
                              "exempt; that script is not called by art run or art final."),
    "audience": "a hiring manager or an engineer reviewing a product-management portfolio project",
    "source_doc": "PROJECT-BRIEF.md (this folder); sources in FACTCHECK.md",
}, "beats": B}

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
words = sum(len(b["narration_text"].split()) for b in B)
print(f"{len(B)} beats; {words} words; est {round(sum(b['estimated_duration_s'] for b in B))} s at 2.5 words/s")
