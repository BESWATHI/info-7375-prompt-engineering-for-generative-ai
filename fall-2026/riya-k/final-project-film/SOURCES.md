# SOURCES

## What I used
| Thing | What it is | Licence / terms | When |
|---|---|---|---|
| Chinook database v1.4.5 (`Chinook_Sqlite.sqlite`) | Public sample database (music store), Luis Rocha, github.com/lerocha/chinook-database | MIT, copy in `evidence/data/CHINOOK-LICENSE.md` | downloaded 2026-10-09, sha256 `bdf635be…a61a` |
| brutalist.art toolkit | Pipeline, show-tell skill, iso kit and approved original props, Remotion bookends, quality gates | per the toolkit repository | commit `22264a33`, pulled 2026-10-09 |
| Kokoro TTS, voice `af_bella` | Local text-to-speech, runs offline | model ships with the toolkit | 2026-10-09 |
| Manim Community 0.18.1, Remotion, FFmpeg | Rendering | open source | — |
| BIRD benchmark page, bird-bench.github.io | Cited in B03: 12,751 question–SQL pairs, 95 databases, execution accuracy | cited, nothing copied | read 2026-10-09 |
| Vanna README, github.com/vanna-ai/vanna | Cited in B03 as an alternative (MIT) | cited, nothing copied | read 2026-10-09 |

No third-party images, footage, music or fonts beyond what the toolkit ships. No private
data: no résumé, contacts, job tracker, TwinAI code, or conversation transcripts appear in
the film or this folder.

## What I made
- The project idea, its scope, and the choice of target role
- Review and approval of every narration line and every claim: I watched the full cut with
  sound on 2026-10-14

## What Claude contributed
Claude (Opus 5.5, in Claude Code), 2026-10-09:
- Recommended the AI Engineer framing when I asked which role would help more on a resume
- Drafted `evidence/gold_set.json` and `evidence/run_slice.py`. The draft's Q08 gold answer
  had a wrong year, which the first run exposed (see FRICTIONAL.md)
- Read the BIRD and Vanna pages and summarised them; I am responsible for checking them myself
- Drafted PROJECT-BRIEF.md, the narration, `make_sheet.py` (beat sheet), `scenes.py`
  (all drawings), FACTCHECK.md, SHOTLIST.md, and this folder's documents
- Ran the toolkit pipeline and gates, and fixed what the gates flagged

No Claude *response* is shown in the film. The film shows no model output at all,
because no model has been run on the gold set yet.
