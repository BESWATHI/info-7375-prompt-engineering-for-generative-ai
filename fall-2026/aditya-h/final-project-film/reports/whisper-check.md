# Whisper check (faster-whisper small.en), 2026-10-14

| Beat | Words not heard | Transcript |
|---|---|---|
| BIDEA | hasija | Hi, I'm Aditya Hasidja. Every product starts with one question. Will it work? I think the more useful question is how it will fail. |
| BDEFS | — | Two terms, a pre-mortem, you imagine the product has already failed and ask why, and an evaluator, an agent that checks the other agent's work. |
| B00 | want, to | Most ideas don't fail on day one. They fail months later on an assumption nobody checked. I wanna catch that assumption before anyone builds. |
| B01 | pre, mortem, labelled | I'm proposing the AI Product Failure Lab. A product manager gives it an idea in public sources, and it will return a premortem. Five failure risks, every claim labeled, and three tests to run first. |
| B02 | — | It will live in a GitHub repository, a small web app, a test set of made-up product ideas, and a log that scores it. |
| B03 | — | Inside, an orchestrator will pass the idea to market, customer, and risk agents. An evaluator will challenge what they found and can send one back once. One retry, never a loop. |
| B04 | chatgpt | Before pitching it, I tested the obvious alternative, just asking a chatbot. I gave plain Claude and chat GPT the same idea with a fake statistic planted in it. Both caught the fake number. |
| B05 | chatgpt, unlabelled | But in three runs, plain Claude cited no sources, yet stated claims as facts. Chat GPT sourced just two paragraphs and left most claims unlabeled. You can't tell evidence from guesses. |
| B06 | dimeadozens, hundred | Paid tools exist, too. DIME, a dozen's homepage, promises 100-page validation reports with hundreds of citations. I haven't bought one, so I can't judge them. |
| B07 | — | Here's what will be different. Every claim will get a label and code, not the model, will check each citation against the sources. The test scores will be public, including where it loses. |
| B08 | readme | who opens it, a hiring manager for AI product roles. In the first minute, they'll read the read me, one real sample report, and the score table against plain chat. |
| B09 | — | What should it prove? That I can write prompt contracts, instructions plus a schema each agent's output must pass, and then measure whether they held. It won't prove I'm a machine learning engineer. |
| B10 | — | The evidence will be saved run logs, the score table, and a written list of where it failed. |
| B11 | — | What comes first? The risk agent and the evaluator on one test idea from the command line. You'll know it ran when a run log appears that passes the schema check. |
| B12 | — | What it will never do, give a percent chance of success, turning guesses into a probability. Live web search, accounts and forecasts are out too. |
| B13 | — | What could sink it? The evaluator rubber stamps, the same model grading its own team. Chatbots already catch obvious fakes, so my test ideas will plant subtler flaws, like a price that contradicts the audience. |
| B14 | — | so I'll count how many planted flaws it catches. If that number is low, I'll move checks out of the model and into plain code and report the result either way. |
| B15 | — | Why this project? It's a mix. Requirements and challenging assumptions are years of my product work. Workship and Skillport are on my GitHub. New to me. Agent orchestration and evaluation design. |
| B16 | chatgpt | So where it stands, what exists today? The idea, a blueprint I drafted with chat GPT and those chatbot tests, everything else I will build with Claude code in two weeks. |
| BOUT | hasija | AI Product Failure Lab, Aditya Haseedjaw. |

## Verdict (reviewed by Claude, 2026-10-14)
All 20 beats were voiced in full. Every "not heard" word is a spelling difference in the transcript, not a dropped or misspoken word:
ChatGPT → "chat GPT", labelled → "labeled", pre-mortem → "premortem", README → "read me", "I want to" → "I wanna",
DimeADozen's → "DIME, a dozen's", hundred-page → "100-page". "Hasija" is spoken via the voice-only rewrite "Ha-see-jah"
(version A, picked by Aditya), so the transcript spells it as Whisper heard it.
