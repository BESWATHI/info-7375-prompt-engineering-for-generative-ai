# Frictional — DryRun pitch film

Pavithra Prasad · INFO 7375 · Final Project Pitch Film

Prompts: `BUILD-PROMPT.md`, section 3 · Evidence: `evidence/` · Gate reports: `reports/`

## 2026-10-10 — Choosing the project

- Compared project ideas against the rubric and against tools that already exist.
- Chose DryRun: test an AI's terminal command on a throwaway copy before it touches real files.

## 2026-10-11 — Existing tools

- `try` previews a command's file changes (Linux only). InterCode and NL2SH score AI shell commands offline.
- DryRun's difference: compare the changes with the request and with the AI's own prediction.

## 2026-10-11 — A real example

- Asked Claude (claude.ai) for one command to delete `.log` files older than 7 days. Reply: `find logs -type f -name "*.log" -mtime +7 -delete`, with advice to preview it without `-delete`.
- Used this reply in the film instead of a made-up example. Screenshot: `evidence/claude-reply-2026-10-11.png`.

## 2026-10-11 — Building the film (v1–v3)

- Free local pipeline: course toolkit, Kokoro voice `af_heart`, Manim, ffmpeg.
- Checked an outside review of the script: kept the real fixes, rejected three factual errors (wrong tool, FastAPI instead of Flask, wrong employer).
- Changes made: Week 1 style with short synced phrases, planned features in future tense, mock-ups labelled CONSTRUCTED, shorter opening.
- All quality gates passed (v3, 3:33).

## 2026-10-13 — Testing the preview myself

- Ran the preview in my Terminal on files 6.5, 7.5 and 8.5 days old. Output: `logs/eight-and-a-half-days.log`. The 7.5-day file was not matched, although it is older than 7 days (`evidence/mtime-test.md`).
- **What I learned:** I understood why checking whether a command runs successfully is not enough. The important part is verifying whether its actual changes match the user's request.

## 2026-10-13 — Final cut (v4)

- Checked the film against the rubric and added one narration line for each gap: what a reviewer could fairly conclude, how you would know the first piece ran, and evidence for the skills I already have (PR #33, 32 passing tests).
- Checked an outside review of the film: raised the audio to −19 LUFS (its −16 target would fail the toolkit's −18 ceiling); its faint-text and slow-opening points were not real.
- Removed all orange accents. Redrew the throwaway-copy picture and added a workflow diagram, from reference images I provided.
- All quality gates passed. Final cut: `dryrun-pitch.mp4`, 3:53.
- **What I would do differently:** I would define the expected results and test cases before creating the storyboard, so the film is built around something I can verify.
