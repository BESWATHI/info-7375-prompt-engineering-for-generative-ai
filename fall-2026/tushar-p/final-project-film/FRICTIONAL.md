# FRICTIONAL — Agent Proving Ground pitch film

## 2026-10-12 — Choosing the project
I didn't want to extend the Reallocation Engine, because a lot of the class will probably do that. I wanted something I could actually put on my resume. I went through my job search notes and saw the same gaps coming up: Kubernetes, sandboxing agents safely, and tracing. So I picked a sandboxed agent runner with tracing and evals. My worry was that it was too big for the course, so I cut it down to a local version on kind. I plan to add Go and EKS later (not a part of this project for now).



## 2026-10-13 — ai-explainer didn't fit
The closest skill was ai-explainer, but it needs the instructor's channel branding and persona, a rewritten narration style, and Claude's interface on screen. The assignment says to narrate as myself, and I didn't want Claude's output on screen, so I didn't use it.

## 2026-10-13 — Watching the review cut
All the checks passed, but when I watched the film myself I found four problems. B04 talked about E2B and Langfuse as if everyone already knew them. B10 started with "Why this project? It's a mix," which isn't a full sentence. B10 also said I picked the project because of the roles I'm applying for, which isn't really my reason. And the film just stopped on the last list, with no closing. I rewrote B04 and B10 and added B12 as a closing beat. The checks can't catch things like this. I had to watch it.

## 2026-10-13 — No pauses between sentences
The narration sounded like one long sentence. I had each sentence voiced separately, with a 0.35 s gap between them. It sounds a lot more natural now. The runtime went from 2:50 to 3:10, which is still inside the limit.

## 2026-10-13 — Changing B06 and B07
"It won't prove production scale, and I won't claim it" sounded defensive, so I changed it. I also changed "Go and cloud deployment come later, as a side project," because I'm not sure it will be a side project. After that, two on-screen labels no longer matched the narration (a red ✗ and "a side project"), so I fixed those too.

## 2026-10-14 — Gate 11 failed
The toolkit's unit tests failed because matplotlib wasn't installed in the project's .venv. It had nothing to do with my film. I installed it, re-ran the tests, and all 122 passed.

## 2026-10-14 — Gate 12 fails because of a toolkit bug
The smoke test fails on this checkout. The toolkit's own sample reel uses the slug "_smoke", and the toolkit's own safety check rejects slugs that start with an underscore. I tried running it on a copy with the slug fixed, but the script is hardcoded to the original folder. I didn't edit the toolkit, because that's not my code to change. I left the failure in and included the report.

## 2026-10-14 — Present-tense lines
I lost points in Week 1 for one sentence that claimed more than the evidence showed, so I did one last check for tense. Two lines described the project as if it already exists: "It's built for one laptop" (B06) and "It runs locally" (B07). Nothing is built yet, so I changed them to "will be built" and "will run." Then I re-voiced those two beats, re-rendered, and ran all the gates again.

## 2026-10-14 — Making the docs match the film
The README and FACTCHECK said every feature sentence uses "will," but that isn't strictly true. B04 and B08 have present-tense words inside "will" and "you'll" sentences. Instead of re-rendering again, I rewrote the claim so it says exactly what the film does.