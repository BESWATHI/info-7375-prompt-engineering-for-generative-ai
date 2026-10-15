# SOURCES: AI Product Failure Lab pitch film

Who made what, what was used, and under which licence. Everything here is local and free: no paid generation, no API keys,
no media account.

## What Aditya Hasija made
- **The project idea** (AI Product Failure Lab) and its feature list.
- **The narration script's ideas and first draft**: storyboard doc, 2026-10-14.
- **Every decision in this folder**: project choice, scope changes accepted, voice (`am_michael`), pronunciation of his surname,
  approval of the stills, and the instruction to run the ChatGPT baseline.

## What ChatGPT contributed (from Aditya's notes, 2026-10-14)
- The project blueprint doc (`AI_Product_Failure_Lab_No_Roadmap.docx`), written from Aditya's idea and features. Its report
  mock-up and CampusFit example are fictional.
- The storyboard's visual direction, design and scene flow (`AI_Product_Failure_Lab_Film_Storyboard.docx`).
- One baseline answer in `research/baseline-chatgpt.md`, which is a real response, logged-out chatgpt.com, 2026-10-15 00:24 UTC.

## What Claude (Claude Code, model claude-opus-5-5) contributed, 2026-10-14
- **Scope review** against the assignment, and the changes Aditya accepted: a planted-flaw test set, a fixed source pack instead of live web,
  no success score, and the command-line engine first.
- **PROJECT-BRIEF.md** drafting, from Aditya's doc and answers.
- **Running the baseline tests** at Aditya's direction: 3 plain-Claude runs via the Claude Code CLI
  (`claude -p --system-prompt "You are a helpful assistant." --tools ""`), and the ChatGPT run in the app's built-in browser.
  The 3 Claude answers in `research/baseline-claude-run*.md` are real responses, 2026-10-14 (00:18 UTC on the 15th).
- **Reading the alternatives**: the Atlassian pre-mortem play page, DimeADozen's homepage and example-reports page, and
  Aditya's portfolio source code for his skills.
- **Revising the script** to the new scope and the rubric, and finding the honesty error ("cited two" → "sourced two paragraphs").
- `make_sheet.py`, `beat_sheet.json`, `scenes_body.py`, FACTCHECK.md, SHOTLIST.md, the README, BUILD-PROMPT.md, and the
  FRICTIONAL.md drafts, which Aditya reviewed.

## Toolkit and assets used (third party)
| What | Source | Licence / terms |
|---|---|---|
| Brutalist toolkit (show-tell skill, iso drawing kit, 25 original props, Remotion bookend scenes, QC gates) | github.com/nikbearbrown/brutalist.art, commit `519fcbb` | Course toolkit, used per the assignment. The instructor's persona, name and credit line are **not** used. |
| Kokoro-82M voice model, voice `am_michael` | kokoro-onnx model files v1.0 | Apache-2.0 |
| Manim Community 0.18.1 | manim.community | MIT |
| Remotion 4 | remotion.dev | Remotion licence (free for individuals) |
| EB Garamond, Lato fonts | bundled with the toolkit | SIL Open Font License |
| faster-whisper (transcript check only) | github.com/SYSTRAN/faster-whisper | MIT |

**The voice is synthetic.** A local Kokoro voice reads Aditya's script in the first person. It isn't Aditya's recorded voice.

## Facts used in the film
See FACTCHECK.md. The only outside facts are DimeADozen's own homepage claims, which are attributed aloud and not verified by us.
Every other number comes from our own baseline tests in `research/`.

## Not included
No real résumé, contacts, application tracker or private transcripts. CampusFit and the "68%" statistic are made up on purpose
(it's a planted flaw), and they're labelled as such in `research/baseline-prompt.md`.
