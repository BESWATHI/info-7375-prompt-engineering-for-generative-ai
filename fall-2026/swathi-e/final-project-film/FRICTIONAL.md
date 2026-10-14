# FRICTIONAL — INFO 7375 Final Project Pitch Film

**Project:** Cite or Refuse — A Source-Grounded Tax Helper for International Students

## October 9, 2026 (Friday)

At first, I was not sure what project to choose. I looked at ideas Claude suggested, like the Reallocation Engine, SEC filings, bank failures, MBTA, hospital prices, and H-1B salaries, but I wanted something that felt more personal and worth building. I finally chose a tax helper for international students because I have faced that confusion myself.

I thought that asking the same tax questions to different chatbots would give me mostly similar answers. I tested three questions in ChatGPT, Gemini, and Claude, using a new chat for each question. I noticed ChatGPT was using personal details I hadn't typed in the question. I tried a temporary chat and then logged out to check again, but the answers still made me question how much I could trust them.

The biggest surprise was that ChatGPT gave me two different numbers for the same tax year: $15,750 and $15,000. I went to the IRS website and found the 2025 Form 1040-NR instructions. Claude helped me locate the passage on page 7, and I [confirmed it myself / EDIT THIS TO WHAT YOU DID]. That helped me understand why my project should show the actual IRS source and tax year instead of just giving a confident answer. I also learned to be careful with the wording: the $15,750 figure on that page is a filing threshold for eligible students.

## October 10, 2026 (Saturday)

I thought updating the Brutalist toolkit would be simple, but `git pull` kept timing out. Instead of spending more time on that, I decided to continue with the Week 1 version I already had.

I found my old Week 1 files and started setting up a separate folder for this film. Downloading and moving files from the chat was more frustrating than I expected. I learned that even organizing the files and tools properly takes time, and that using a working version was better than getting stuck trying to update everything.

## October 13, 2026 (Tuesday)

I first tried to use Claude Code from Terminal, but the `claude` command was not installed. I was confused about how to continue, so I switched to the Code tab in the desktop app. I also checked Canvas and saw that the deadline had moved to Wednesday, which gave me some more time to review the film.

Claude Code helped with the actual video build, including the Manim scenes, narration, rendering, and checks. When I first watched the film, I did not see any problems. Claude suggested three fixes, and I approved them: making the wording about the IRS filing threshold more precise, clarifying a cell in the comparison table, and making the audio louder.

I also realized the male narration voice didn't feel right for a film that was supposed to be narrated as me, so I changed it to a female voice. While listening again, I caught that "AI" was being pronounced like "ia" around 2:22. The automated checks had not caught that. I listened to five samples before choosing the version that sounded right.

The main thing I learned was that passing technical checks does not mean a video is ready. I still had to watch it, listen carefully, and make decisions myself. The tax helper itself has not been built yet; this film is only my proposal for it.

## What Claude contributed vs. what I decided

- **Claude (chat)** suggested project ideas, drafted PROJECT-BRIEF.md, TEST-NOTES.md, beat_sheet.json, and the build prompt, and helped me locate the page 7 passage in the IRS instructions.
- **Claude Code** wrote the scenes, generated the narration, rendered the film, ran the quality gates, and drafted README.md, SOURCES.md, and BUILD-PROMPT.md.
- **I** chose the project and the personal reason for it, ran all nine chatbot tests and the reruns, found the IRS instructions, reviewed the brief and narration, approved each fix, chose the female voice, caught the "AI" pronunciation problem, and picked the final spelling by listening.
