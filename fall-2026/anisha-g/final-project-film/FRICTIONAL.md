# FRICTIONAL — what actually happened
Anisha Gaikar

**2026-10-10, ~8:00 am** — Started the assignment. Asked Claude to pick an easy topic because I was short on time. Chose "JobPost Contracts", a prompt-contract library with a test harness, from the assignment's own example list.

**2026-10-10, ~8:10 am** — Claude drafted PROJECT-BRIEF.md. I didn't get further that day.

**2026-10-10, ~6:30 pm** — Asked Claude for step-by-step help. It read Brutalist's docs: the show-tell builder needs Manim, Remotion, Node 20+, ffmpeg, a 340 MB voice model, and a hand-written Manim animation per beat that must pass several quality gates. Its default narrator and outro use the instructor's persona, which the assignment says not to use. Claude made a beat sheet and simple slides as a fallback.

**2026-10-13, ~8:20 am** — Came back to finish. Claude filled in my name and questions 2 and 7 after I asked it to.

**2026-10-13, ~8:32 am** — Decided to use an AI voice instead of recording myself. The assignment says to narrate as myself (not the instructor's persona), not that it must be my recorded voice. Using the free built-in macOS voice (Samantha) reading my first-person script, generated locally. Noted in SOURCES.md.

**2026-10-13, ~8:35 am** — Built a first version (static slides + voice), 3:18 long. It felt too plain: I couldn't see the explanation on screen.

**2026-10-13, ~8:40 am** — Showed Claude a classmate's film made in the show-tell style and asked for the same format with my own topic and a different design. Claude couldn't install Manim in its workspace, so it wrote its own Python drawing script (`tools/render.py`) that draws isometric scenes in a teal/coral palette and animates them to the narration. Added a typing intro and a "Terms In This Film" card like the show-tell format. Every drawing says "CONSTRUCTED · not built yet".

**2026-10-13, ~9:05 am** — Watched the draft: there were stretches where the voice kept going but the picture had stopped. Asked Claude for more visuals, writing and colour. It added on-screen subtitles that write in with each sentence, a numbered title per question, looping motion (a dot travelling along the arrows, scan lines), a slow camera drift, extra drawings (an invented salary being crossed out, a pile of postings, handwritten reasons), and a brighter palette. It also made each scene stretch to the real length of the voice so pictures stay in sync.

**2026-10-13, ~9:33 AM** — Brutalist on my Mac: did not install it locally (not enough time to set up Manim, Remotion and the voice model).

**2026-10-13, ~9:33 AM** — Ran `bash make_film.sh Gaikar` on my Mac. Runtime: 3:33. (first build, before the gate fixes below)

**2026-10-13, ~9:50 am** — Asked Claude to check the submission against the rubric. It ran the toolkit's own Gate V (`runtime/qc/final_frame_check.py`) on a test build and it FAILED: the soft corner shading made the gate read the whole background as content (edge-bleed + low-contrast on every frame), and the subtitle box sat below the title-safe line. Fixed: shading made subtler (within the gate's tolerance), subtitles raised, camera drift reduced. Check frames then passed (0 blockers, 0 major). Also: the class repo's GitHub check emailed me a failure; it comes from another student's `.tsx` files (the repo only allows Python), not from my folder.

**2026-10-13, ~10:00 am** — Question 2 originally said I had looked at a chatbot, but I hadn't actually tried one yet, so I did. ChatGPT could not open the LinkedIn link. With the posting text pasted (Staples, Financial Analytics Intern) it summarised well and said "Salary: Not disclosed", but showed no source for any field and added "Staples is headquartered near Boston", which is not in the posting. Screenshots in `evidence/` (cropped to remove my personal details). Updated question 2 and the narration to say what I actually saw.

**2026-10-13, ~10:05 am** — Question 7 said my Python evidence was "earlier course assignments", which was vague. Replaced it with my MBTA Transit Reliability Pipeline (github.com/anishagaikar0420/mbta-reliability-pipeline), a Python ELT pipeline with tests and a quality gate.

**2026-10-13, ~11:15 AM** — Ran the toolkit's Gate V on the final film with `tools/run_gate_v.sh` (brutalist.art commit 6a8380a): PASSED. Report in `reports/GATE-V-REPORT.md`.

**What I'd do differently:** Start earlier, so there's time to get Brutalist running and use its quality gates.
