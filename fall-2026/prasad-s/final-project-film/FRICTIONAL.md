## 10/08/2026 — Choosing the final project and checking for existing work
What I tried: In a planning session with Claude (claude.ai), I compared project
ideas and chose one: a demo that tests whether the text shown to a person
approving an AI agent's payment matches the signed terms. I read Google's AP2
announcement post and the v0.2 specification main page, and I found and opened
the Razorpay-buildathon repository's README myself.
What happened: My working title was "Mandate Mirror". A name-collision search
during planning found products called "Mandate" and "MandatePay" but missed a
repository with the exact name, which I found. Its README describes a payment
firewall that checks requests against a mandate and cumulative spend, not a
check on the text shown to the person (README only; I did not read the code).
My first draft of the alternatives also included a Stripe entry that blended two
different protocols and made claims I had not checked against Stripe's own
docs, so it was dropped.
What I did instead, or decided: I kept the project, renamed it "GistGap" (picked
from a shortlist), and narrowed my claims. I read only the AP2 main spec page.
It requires a non-agentic Trusted Surface, so the problem may be smaller than I
first thought. I recorded that as the main risk in the brief. A single
exact-string search for "GistGap" during planning found no match; I have not
yet searched GitHub or domain names myself.
What I'd check next time: Search GitHub for an exact name myself before adopting
it, open candidate repositories instead of relying on summaries, and confirm
each claim against the primary source before writing it down.

## 10/08/2026 — Git blocked by the Xcode license
What I tried: I asked Claude Code to create the project folder skeleton and
check my git settings.
What happened: Every git command failed with "You have not agreed to the Xcode
license agreements." The tool stopped without changing anything and said it
needed my password.
What I did instead, or decided: I ran "sudo xcodebuild -license" in Terminal
and typed "agree." Git then worked and the setup finished.
What I'd check next time: If git fails with a license message, accept the
license first. Stopping instead of working around the error was the right
behavior.

## 10/08/2026 — Placeholder email set as my git email
What I tried: I set my git commit email to my GitHub no-reply address.
What happened: The command I was given contained a placeholder address, and I
ran it unchanged, so my global git email became the placeholder. I was told to
get my real no-reply address from GitHub Settings, then ran the same
placeholder command a second time. Checking the setting showed the placeholder
again, my real no-reply address was looked up with the gh tool, and I set it.
Nothing was committed with the placeholder.
What I did instead, or decided: I set the real address globally, replacing my
previous global email for all repositories, and confirmed it with
"git config user.email".
What I'd check next time: Replace placeholders before running any copied
command, read the whole message before running it, and check "git config
user.email" before the first commit.
