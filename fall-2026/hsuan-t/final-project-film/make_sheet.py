import json
from pathlib import Path

HERE = Path(__file__).parent
SLUG = "final-project-pitch"
TITLE = "The Reallocation Engine Pitch"

def card_beat(bid, narration, kind, heading, sub, word, show, **custom_props):
    card_props = {
        "kind": kind,
        "heading": heading,
        "sub": sub,
        "word": word,
        "onTwos": True
    }
    card_props.update(custom_props)
    return {
        "beat_id": bid,
        "act": "show-tell",
        "lane": "card",
        "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_puck",
        "engine": "kokoro",
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "show": show,
            "remotion": {
                "pattern": "ShowTellCard",
                "props": card_props
            }
        }
    }

B = [
    card_beat("B01", "This is a command-line workflow that scores software development roles—from SWE to DevOps and QA—for F-1 STEM OPT students, outputting a clear Apply or Skip based on real visa data.", 
              "search", "F-1 Tech Role Filter", "SWE · DevOps · QA", "",
              [{"at": 0.2, "event": "type"}, {"at": 0.6, "event": "results"}],
              items=[
                  {"label": "Software Engineer (SWE)", "sub": "Backend / Systems · In-Scope", "value": ""},
                  {"label": "DevOps / SRE Engineer", "sub": "Cloud & CI/CD · In-Scope", "value": ""},
                  {"label": "QA & Test Automation", "sub": "Testing Frameworks · In-Scope", "value": ""},
                  {"label": "Machine Learning / Data", "sub": "Specialized · Configured Out", "value": ""}
              ]),
    
    card_beat("B02", "Instead of a black box AI that hallucinates sponsorship, this tool grounds every score in verified public filings. We verify historical DOL H-1B approval numbers and SEC Form D venture funding, giving students concrete proof behind every single pass or skip decision.",
              "tabs", "Evidence > Black Box", "H-1B Record Found", "",
              [{"at": 0.22, "event": "tab switches from AI to Evidence"}],
              labels=["Black-Box AI", "Verified Data"],
              cues=[0.22],
              items=[
                  {"label": "ChatGPT Guess", "value": "Hallucinated", "sub": ""},
                  {"label": "Visa Sponsorship", "value": "Unverified", "sub": ""},
                  {"label": "Rejection Risk", "value": "High", "sub": ""}
              ],
              items2=[
                  {"label": "DOL H-1B Filings", "value": "15 Approved", "sub": ""},
                  {"label": "SEC Form D (Series B)", "value": "$24M Raised", "sub": ""},
                  {"label": "True Sponsorship", "value": "VERIFIED", "sub": ""}
              ]),
              
    card_beat("B03", "An F-1 student runs the CLI with a job URL. The pipeline extracts and cleans the company, title, and description, feeding them to the engine so the student gets a decision in under sixty seconds.",
              "workspace", "Job Extraction Pipeline", "Paste URL -> Instant Decision", "",
              [{"at": 0.2, "event": "workspace expands"}],
              items=[
                  {"label": "1. Extract", "value": "", "sub": ""},
                  {"label": "2. Clean", "value": "", "sub": ""},
                  {"label": "3. Score", "value": "", "sub": ""}
              ]),
              
    card_beat("B04", "It proves I can build source-grounded agent workflows: using prompt contracts to prevent hallucinations, phase gates to short-circuit bad roles, and automated evaluation suites to benchmark decision accuracy.",
              "paths", "Source-Grounded Workflows", "Prompt Contracts · Eval", "",
              [{"at": 0.2, "event": "paths connect data to AI"}],
              items=[
                  {"label": "Job URL", "value": "", "sub": ""},
                  {"label": "Phase Gates", "value": "", "sub": ""},
                  {"label": "Decision", "value": "", "sub": ""},
                  {"label": "DOL & SEC", "value": "", "sub": ""},
                  {"label": "Eval Suite", "value": "", "sub": ""}
              ]),
              
    card_beat("B05", "It includes a lightweight hash-tracker for duplicates, but it is deliberately not an auto-apply bot. The first piece to run is the sponsor lookup, verifying company names against actual H-1B filing records.",
              "stack", "Project Scope", "Sponsor Lookup", "",
              [{"at": 0.2, "event": "stack of features"}],
              items=[
                  {"label": "Sponsor Lookup", "value": "FIRST (Core)", "sub": ""},
                  {"label": "Hash Deduplication", "value": "NEXT (UX)", "sub": ""},
                  {"label": "Auto-Apply Bot", "value": "OUT OF SCOPE", "sub": ""}
              ]),
              
    card_beat("B06", "To prevent false rejections, the AI must quote exact proof. And to cut UX friction, a background hash tracker skips duplicate postings, so students never waste time re-evaluating the same job.",
              "dashboard", "Duplicate Postings Filtered (SHA-256)", "Background Hash Cache · Zero Wasted Evaluations", "3",
              [{"at": 0.2, "event": "drops in list of duplicate postings skipped"}],
              items=[
                  {"label": "Meta — Software Engineer (Backend)", "value": "SKIP", "sub": "Hash: 7f2a9c1e · Match Found in Cache"},
                  {"label": "Amazon — DevOps / SRE Engineer", "value": "SKIP", "sub": "Hash: 3c1b84e0 · Match Found in Cache"},
                  {"label": "Stripe — Infrastructure Engineer", "value": "SKIP", "sub": "Hash: 9e4d01b8 · Match Found in Cache"}
              ]),
              
    card_beat("B07", "I used to trust AI blindly. I'm showing off the open friction logs and provenance tags that prove my AI workflow to any reviewer, while learning to replace naive prompt-pasting with strict verification gates.",
              "focus", "Audit Trail & Provenance", "Friction Logs · Provenance Tags", "",
              [{"at": 0.2, "event": "lens focuses on model judgment"}],
              items=[
                  {"label": "[record] DOL H-1B", "value": "15 Approved", "sub": ""},
                  {"label": "[record] SEC Form D", "value": "$24M Raised", "sub": ""},
                  {"label": "[model-judgment]", "value": "Quote Proof", "sub": ""},
                  {"label": "FRICTIONAL.md Log", "value": "Auditable", "sub": ""}
              ],
              focus=2),
]

def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_puck", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b

OPEN = [
    remotion("BIDEA", "the question",
        "Hallo. This is Isaac. I'm building an AI workflow for F-1 STEM OPT students. The question is: how do we stop AI from guessing visa sponsorships?",
        "BrutalistHesitantWriter",
        {"text": "How do we stop AI from\nguessing visa sponsorships?", "triggerWords": "guessing", "replacementWords": "hallucinating",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
         "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types"}, {"at": 0.6, "event": "backspaces on the spoken correction"}],
        lead_silence_s=0.8, motion_claim="The writer types the naive question and corrects it.",
        qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."})
]

B = OPEN + B
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. Isaac Tai.", "estimated_duration_s": 4.0, "voice": "am_puck", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@IsaacTai", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "PITCH FILM", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Isaac (in for Bear)", "voice": "am_puck", "voice_kokoro": "am_puck", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Plain", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt", "your-turn"],
    "bookend_exempt_reason": "Pitch film structure. No your-turn required.",
    "playlist": "INFO7375 Pitch", "chapter_number": 1,
    "tags": ["Pitch", "The Reallocation Engine"]},
    "beats": B}

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"Generated {len(B)} beats for the Pitch Film.")
