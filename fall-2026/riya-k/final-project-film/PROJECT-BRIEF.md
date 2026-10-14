# Project brief — Ground Truth SQL

Riya Kapadnis · INFO 7375 · Final project pitch · written 2026-10-09, revised 2026-10-14
Target role: **AI Engineer** (also readable for Data Analyst roles)
Stack: Python 3 (standard library + `sqlite3`), Claude via Claude Code, the public Chinook sample database.

## 1. What is it?
An evaluation harness that tells you, on your own database, which plain-English questions a
text-to-SQL model answers wrongly and why. Done, it will be a **public GitHub repository**:
a gold set of about 50 questions with hand-checked SQL over Chinook, a runner that sends each
question to Claude and checks the result by executing it, and a Markdown scorecard listing
every failure, its cause, and the model's SQL beside the checked answer.

## 2. Why would anyone care?
It is for an analyst deciding whether to trust an AI SQL assistant on their own schema. The
danger is a query that runs, looks right, and returns the wrong number. In my first test
(2026-10-09), a hand-written query with a common join mistake reported USA revenue as 4,667.06
instead of 523.06, about nine times too high, with no error.

Alternatives I looked at (2026-10-09):
- **BIRD** (bird-bench.github.io): 12,751 question–SQL pairs over 95 databases, scored by
  execution accuracy. It measures a model on *its* databases, not your schema or questions.
- **Vanna** (github.com/vanna-ai/vanna, MIT): generates SQL for your own database. I did not
  find a way in it to test that SQL against hand-checked answers and report where it fails.

What mine adds: checked answers on *your* schema plus a written failure analysis. The output
is not one accuracy number but the specific questions the model got wrong, sorted by cause
(join fan-out, wrong key, unit error, date handling, and so on).

## 3. Who opens it, and what do they do with it?
A hiring manager or engineer screening for an AI Engineer role, and later the analyst above.
In the first sixty seconds they read the scorecard at the top of the README, run one command
that replays the saved model results offline (no key needed), and open one failure to see
the model's SQL next to the checked SQL and both result sets.

## 4. What does it prove about me?
That I can evaluate a model instead of trusting it, using the course's skills:
- **Prompt contract:** exactly one read-only `SELECT`; anything else is logged as a violation, not fixed.
- **Verification:** both queries run on a read-only database and the rows are compared, not the SQL text.
- **Evaluation:** a gold set, a failure taxonomy, and repeated runs to show variance.
- **Agent loop** (stretch): generate → run → read error → repair, capped, and *measured* for
  whether repair fixes answers or only hides errors.
- **Source grounding:** every reported number traces back to its rows.

A reviewer could fairly conclude I can build and honestly report an evaluation on a small
public database, and **not** anything about production warehouses: Chinook is 11 tables and
50 questions is small. Evidence: dated run logs and a scorecard anyone can re-run.

## 5. What is in, what is out, what comes first?
- **In:** Chinook, about 50 questions, Claude as the model, an execution checker, a failure analysis.
- **Out (deliberately):** no chat app or UI, no write queries (the connection is read-only),
  no claims about production data or other models.
- **First (already runs):** `evidence/run_slice.py`: 8 questions, gold SQL, and an execution
  comparator tested on 9 hand-written variants. It ran if it prints
  `execution comparator agreed with the hand label on 9/9 variants` and exits 0.
- **Next:** the first real Claude run on those 8 questions, saved with its date and raw output.

## 6. What could sink it?
I write both the questions and the answers, so the test can be too easy or the answers wrong.
It already happened once: my Q08 gold asked about 2023 revenue, but Chinook's invoices run
2009–2013, so the gold result was NULL and a broken query "matched" it
(`evidence/run_slice_output_v0_first_run.txt`). What I will do: the runner now rejects any
empty or all-NULL gold answer; a classmate will independently check a sample of the gold SQL;
ambiguous questions get marked ambiguous; and every question runs three times.

## 7. Why this project?
It's a mix. The SQL and Python side is something I already do and can show; checking, with
evidence, whether a model's answer is actually right is the part I want to learn, and it is
what AI Engineer roles screen for.
- **Already have:** SQL, Python, and building LLM features into a BI product (AI Engineer
  co-op, TwinAI, Jan–Jun 2026). That code is private, so the public evidence is this course:
  the Week 1 film (a claim checked across 10,000 seeds, not one run) and my Reallocation
  Engine recipe (PR #7 on nikbearbrown/the-reallocation-engine).
- **New to me:** designing an evaluation set, execution-based checking, a failure taxonomy,
  and measuring whether a repair loop actually helps.

## Exists today (2026-10-09)
- `evidence/gold_set.json`: 8 questions with gold SQL and 9 hand-written variants (not model output)
- `evidence/run_slice.py`: runs the gold set and the execution comparator (standard library, offline)
- `evidence/run_slice_output.txt`: 9/9 variants judged as hand-labelled; exact-string matching rejected all 3 correct rewrites
- `evidence/run_slice_output_v0_first_run.txt`: the first run, showing the Q08 gold-answer bug
- `evidence/data/Chinook_Sqlite.sqlite`: Chinook v1.4.5 (MIT, Luis Rocha)

## Will exist
- A gold set of about 50 questions, including ones marked ambiguous
- The Claude runner with a prompt contract and saved, dated raw outputs
- An offline replay command and a scorecard in the README
- A failure taxonomy with counts, and three-run variance per question
- (Stretch) A measured repair loop
- An independent check of a sample of the gold answers by a second person
