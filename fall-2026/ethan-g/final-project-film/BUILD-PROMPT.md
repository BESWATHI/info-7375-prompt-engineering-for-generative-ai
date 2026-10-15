# BUILD-PROMPT — how to rebuild this film

Everything is free and local: no API keys, no paid generation, no upload.

## 1. Toolkit (one time)

```bash
git clone https://github.com/nikbearbrown/brutalist.art Brutalist     # built against commit 519fcbb
cd Brutalist
python3.11 -m venv .venv && source .venv/bin/activate              # macOS system python3 (3.9) lacks the deps
pip install -r requirements.txt                                     # Manim 0.20.x pinned
./setup --install                                                   # see FRICTIONAL.md: its ElevenLabs guard trips on
                                                                    # the toolkit's own youtube/ examples at 519fcbb
./art smoke                                                         # end-to-end proof that a video renders
```

Put this folder beside the toolkit (`Final_Project_Pitch/` next to `Brutalist/`), or set `ART_HOME` to the toolkit.

## 2. Film (from `Final_Project_Pitch/film/`)

```bash
source ../../Brutalist/.venv/bin/activate
T=../../Brutalist

python make_sheet.py                                         # beat_sheet.json from the narration + visual plan
python $T/runtime/scripts/generate_audio_kokoro.py .         # narration first: the measured mp3s are the clock
python finish_audio.py                                       # 0.8 s lead on BIDEA, 1.0 s tail on BEND; re-measure
./build_scenes.sh                                            # scenes.py = iso_kit + original props + scenes_body.py
cd $T && ./art run   ../Final_Project_Pitch/film             # Gates F, L, A, W, B; 4K renders; review cut; Gate V
         ./art final ../Final_Project_Pitch/film --out ../Final_Project_Pitch/film/exports   # Gate T + verified master
```

Subtitles (after `art final`):

```bash
python $T/runtime/scripts/align.py .                 # word clock from the known narration
python make_captions.py                              # ../DataSentry_Pitch_EthanGomes.srt + .vtt, all words kept
python $T/runtime/scripts/srt_check.py . --srt datasentry-pitch.srt
ffmpeg -i exports/datasentry-pitch.mp4 -i ../DataSentry_Pitch_EthanGomes.srt -map 0:v -map 0:a -map 1:0 \
  -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=eng -disposition:s:0 default \
  -movflags +faststart ../DataSentry_Pitch_EthanGomes.mp4  # soft track; picture and sound are stream-copied
```

Re-voicing one beat: `generate_audio_kokoro.py . --only B07` then `python finish_audio.py`.
Re-rendering one scene: move `manim/<BID>.mp4` (and `media/videos/`) into `_superseded/`, then `./art run` again.

## 3. The prompts (Claude Code, model Opus 5.5)

The film was planned and built in one Claude Code session. My prompts, in order (lightly trimmed):

1. *"New Assignment using Brutalist. Read through all the assignment requirements and instructions first. Then tell me
   what needs to be done:"* followed by the full assignment text.
2. *"ignore the 5 day plan — all the steps need to be done in 1 day"*
3. *"suggest a few topics for me … I am looking for Data related full time roles like Data Engineer, Data Analyst and
   Business Intelligence roles. Provide a topic that is related to my full time job search. Also check if the topics
   suggested can answer all these questions for the 2–4 min film"* followed by the seven questions and the
   "Choosing a project" criteria.
4. *"I want to follow topic 2 [Data-Quality Test Generator, Scored on Planted Defects] — will it satisfy the 7
   questions? will you be able to make a 3:30 to 4 min video? does this topic satisfy all the criteria?"*
5. *"what is great expectations?"* · *"is the scope and size of this project satisfy the requirements?"*
6. *"for question 7 — this is something you already know how to do and want to show off. I think this will help me
   create relevant things to the job posting and data processing required by a particular company."*
7. *"go ahead and start generating a 3:30 to 4 min video on this topic in a new folder under the Prompt Engineering
   folder … name the new folder Final_Project_Pitch. Make sure to include visuals along with text … follow all the
   steps: brief, beat sheet, build, gates + honesty check + re-render, Frictional + assemble."*
8. *"Start the video by saying 'This is a Final Project Pitch Film Created by Ethan Gomes' and then say the project
   name and then continue with the rest"* (after the first master; the opener and B00 were re-voiced and re-rendered).
9. *"are there subtitles for the video? if not add subtitles for the video"*
10. *"[Q4 — What it proves — only partly answered: it doesn't say what a reviewer could fairly conclude.] Provide
    additional content and make changes to answer this question clearly in the video"*
11. *"Change the name to DataSentry. Also in 'Why this project' do not include 'Mostly to show off'; say that 'This
    project will help me land a Data job like a Data Engineer or a Data Analyst role.' Also change the visuals
    accordingly. Say that this project will highlight the skills I am working on like python, pandas and the rest …
    I do not want to give proof of the work done right now, so say that I am working on these skills."*
12. *"Instead of this [the typed 'Can Claude write checks I can measure' opener] write 'DataSentry' and below that
    write a short 1 line about the project which is being pitched"*
13. *"Put the Tick mark next to the 'tested, not trusted' not above it"*
14. *"Can you level the right lower side of the frame with the other side?"* then *"is it possible to make the right
    lower side shorter and under the top bar? Generate it and I'll let you know if I want to revert back to the original"*
15. *"revert back to the original"*
16. *"Can you change the lower left leg to go under top bar?"*
17. *"[Q2] Add this: 'it tells a data engineer which bad rows their checks would let through.'"*
18. *"Can you make sure the block is behind the bar and doesn't overlap it when the transition starts"*
19. *"so say for example before the nyc taxi trips data part"*

Claude's working rules for prompt 7 came from the toolkit's `CLAUDE.md` and `skills/make/show-tell/SKILL.md`, overridden
where the assignment says otherwise (narrate as yourself; no instructor name, persona, or credit line).
