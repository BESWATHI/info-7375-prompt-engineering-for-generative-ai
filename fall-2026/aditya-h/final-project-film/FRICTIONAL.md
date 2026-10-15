# FRICTIONAL: Final Project Pitch Film

Dated log of what was tried, what broke, and what changed.

## 2026-10-14
- **Brutalist checkout was out of date.** My local `~/brutalist.art` (Sep 20) had no `show-tell` skill. I pulled to
  `519fcbb` (Oct 12). I had a local, uncommitted change to `runtime/remotion/package-lock.json` (it adds `zod` and
  `@remotion/zod-types`), so I set it aside before pulling, put it back afterwards, and saved a backup patch outside the repo.
- **show-tell's default voice and outro belong to the instructor's persona.** The skill opens with "This is Liam, in for Bear"
  and ends with a spoken "At Nik Bear Brown" outro. The assignment says to narrate as myself and not use the instructor's
  name, persona or credit line, so the greeting, the outro and the voice will need changing. (To do in the build phase.)
- **Portfolio site wasn't reachable.** The guessed Vercel URL returned `404 DEPLOYMENT_NOT_FOUND`, so the skills list
  came from the portfolio's source code instead.
- **Project chosen: AI Product Failure Lab.** The idea and feature list are mine; ChatGPT turned my notes into a blueprint doc.
  Claude (Claude Code) reviewed it against the assignment and suggested scope changes, which I accepted: a planted-flaw
  test set, source packs instead of live web search, no success score, the command-line engine first, and a two-week build with Claude Code.
- **Baseline test surprised us.** I planned to show that a plain chat assistant builds on a fake statistic. It didn't:
  plain Claude flagged the planted "68% would pay" in 3 of 3 runs. I changed the pitch: the difference is now
  per-claim evidence labels, a fixed format and measured evaluation, not "catches what chat misses". The test set will also
  need subtler flaws.
- **Claude in Chrome wasn't connected**, so the baseline ran through the Claude Code CLI (`claude -p`, no tools,
  minimal system prompt) instead of the claude.ai app. That is close to, but not the same as, the chat product.
  ChatGPT isn't tested yet.
- **ChatGPT baseline (later the same evening, 00:24 UTC on the 15th).** I ran the same prompt on logged-out ChatGPT in
  the app's built-in browser and accepted its terms for this test. It also caught the fake stat, and it was stronger than
  plain Claude: web sources attached to 2 paragraphs, and some "not a benchmark" labels. That narrowed my claim again: the Failure Lab's
  difference is *every* claim labeled, citations checked by code, and a scorable fixed format. The model wasn't shown,
  and the citation URLs weren't visible, so I recorded only the source names.

## 2026-10-14 (beat sheet)
- **Turned my storyboard into a show-tell beat sheet.** The narration ideas are mine; ChatGPT drafted the storyboard's
  visual direction and scene flow. Claude revised the script to the new scope: real baseline results, the DimeADozen
  check, one honest risk, the exists/will-build split, and a tag on every drawing (`constructed` / `real test · Oct 14`).
  Neo-brutalist kinetic type from the storyboard was swapped for show-tell drawings (toolkit format: labels only, no text slides).
- **DimeADozen turned out closer than expected.** Its homepage advertises 100+ page reports with 500+ source-linked
  citations, so "citations" alone isn't a difference. I didn't buy a report, so the film only quotes its homepage and says
  I can't judge it. The difference I claim is openness: a published test set and scores, including losses.
- **Fact-check caught my own error.** "ChatGPT cited two sources" was wrong; its chips read "+2" and "+1", so more
  sources sat behind them. Corrected to "attached sources to two paragraphs" everywhere.
- **Dropped the "Your Turn" bookend** (declared `bhtf` exempt) to keep runtime under 4 minutes. The estimate is about 3:50 at 2.5 words/s,
  and the real length gets measured from the audio.

## 2026-10-14 (narration)
- **Voice:** Aditya picked Kokoro `am_michael` from three local samples (`voice-samples/`). It's a synthetic voice reading his
  script in first person, disclosed in SOURCES.md. It isn't `am_onyx`, the instructor persona's voice.
- **Surname:** every voice said "Hasija" wrong. Aditya picked respelling A ("Ha-see-jah"). I added it as a voice-only
  rule (`pronunciation/aditya.json`, also copied into `~/brutalist.art/runtime/pronunciation/` as a new untracked file),
  so on-screen text and the script keep the real spelling.
- **First full voicing ran 3:51** (231 s) before padding, too close to the 4:00 limit, and B15 ran 16.9 s against the 15 s
  guideline. I trimmed six beats; it now measures 3:44 with lead silence and the 1 s outro tail.
- **Whisper check:** all 20 beats were voiced in full; the only differences were spelling (`reports/whisper-check.md`).

## 2026-10-14 (scenes, first stills)
- Wrote 17 body scenes (`scenes_body.py`; `build_scenes.sh` pastes the toolkit kit and approved props above it to make `scenes.py`).
  The props come from the approved 25-object set; no person icons were used.
- **Parallel still renders crashed** (5 of 17, `ParseError`/missing file): the scenes shared one text cache folder.
  Re-running them one at a time fixed it.
- **First contact sheet had 5 layout problems.** B01 had an orphaned "sources" label, B06 a "?" on the stack, B08 a label on the desk,
  B12 a stray bar where the gate's own barrier should drop, and B13 a crack off the document. All five were fixed and re-rendered
  (`reports/stills-contact-v1.png`). These are low-res last frames only; no motion or gate checks have run yet.

## 2026-10-14 (render, first pass)
- **First full 4K review render failed Gate V**: 5 blockers, all edge-bleed. B06's report stack was too tall at the top,
  B10's "failures" tab ran off the right, and B16's box ran off the left. I didn't submit over it: I shrank the stack, shifted the tabs and the box,
  moved B06's label off the stack, and re-rendered only those three scenes. Gates L, A and W had passed, and Gate B passed per scene.
- The `--height 1080` flag still produced 2160p scene renders, so the "quick pass" was effectively a full 4K pass (~35 min).
- **Second review render passed Gate V** (0 blockers). But its midpoint frames showed B00's label mid-fade and B01's copies
  mid-move, which is exactly what Gate T samples. The kit's guard example (`show-tell-context-is-a-budget`) isn't in this
  checkout, so I wrote my own `GuardScene`: any animation that would overlap a clip's midpoint ±0.3 s waits until just after it.
  The first version recursed (`Scene.wait` calls `play`) and crashed 11 scenes; I fixed it to pass waits through. Low-res check:
  every clip is within 0.06 s of its audio and every midpoint is settled. Re-rendered all 17 at 4K for the final.
- **Gate T blocked the final** with 1 FAIL: the terms card's corner label ("Aditya Hasija") is drawn at 32 px by the toolkit
  component, under the 41 px floor at 4K. I didn't edit the toolkit; I left that one label empty (the name is still on the
  opening and outro cards) and re-rendered only that card.
- **Caught a silent failure.** After I switched the scenes to `GuardScene`, two "passing" runs had compiled *placeholder slates*
  instead of the drawings ("slots: 3/20 filled"). run.sh finds scenes with a regex for `class X(Scene)`, so it saw none.
  That Gate V "clean" was on slates, not the film. Fix: I rebound the name `Scene` to the guarded class so the source says
  `(Scene)` again (17 discoverable), and now I check the "slots: 20/20" line before trusting any gate.
- **Gate T's 40 px run wasn't the name label.** It was "an" in "an agent that checks…", which has no tall letters, so its
  x-height is below the floor. I reworded the card to "the agent that checks the others' work" (the narration is unchanged).
- **Gate T still failed on the terms card after two fixes** (an empty name label, then earlier row cues). Measuring the frame
  showed the real cause: the component's fixed 48 px lowercase definitions ("as", "ow") render at 40 px, under the 41 px floor,
  and the component has no size prop. Rather than edit the toolkit, I redrew the terms beat as a show-tell drawing (cracked
  crate + "?" for pre-mortem, review desk + checked page for evaluator), with the same narration and audio.
- **FINAL: all gates pass.** Gate T PASS (20 beats, 0 FAILs), Gate V clean (0 blockers), and slots 20/20 filled with real drawings.
  Master: `ai-product-failure-lab-pitch.mp4`, 3840×2160, 24 fps, H.264 + AAC, 3:43.9, 17.3 MB,
  sha256 `7d9e4d7d5739114f379c0043d8111354d0979dc01e333dd8e26b070ab0d14bd2`.
  Lint note (not a gate): "COLD OPEN LAW wants ClaudeComposerAsk". The show-tell skill itself specifies the hesitant writer
  as the opening, so I left it.

## 2026-10-14 (packaging)
- Built the submission set: 30 files, 18 MB. Left out caches and regenerable output (`media/`, `manim/`, `mp3/`, `_qc/`,
  `exports/`, the generated 4,770-line `scenes.py`, slate cut, toolkit status files) and the surname voice samples. I swapped the raw
  `claude -p` JSON (it carries session ids) for `research/baseline-claude-metrics.json`. A scan found no email, keys or passwords.
- **The course repo ignores every `.mp4`** (`.gitignore` line 33), which is why my Week 01 film was never committed. The film is in the
  Canvas zip. Aditya decided to leave it out of GitHub, as with Week 01; README says where it is.
