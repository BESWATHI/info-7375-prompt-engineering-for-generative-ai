# SOURCES — Readback pitch film

_Work in progress; completed in Phase 6._

## Used

### AMI Meeting Corpus — manual annotations (CC BY 4.0)

- **What:** AMI manual annotations, file `ami_public_manual_1.6.2.zip`. The download page labels it v1.6.2 (10-Apr-2017); its `00README_MANUAL.txt` calls itself release 1.7 (16 June 2014).
  - Source: https://groups.inf.ed.ac.uk/ami/download/
  - Direct URL: https://groups.inf.ed.ac.uk/ami/AMICorpusAnnotations/ami_public_manual_1.6.2.zip
- **Downloaded:** 2026-10-14, 13:52 EDT. 22,887,865 bytes; SHA-256 `b56e5babb2496b8795deeeda7e71178d7fbc9963f94276cf2a3f4b56ebbc9f9d`.
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/
- **Coverage of the summaries (checked 2026-10-14):**
  - The licence page (https://groups.inf.ed.ac.uk/ami/corpus/license.shtml) and the zip's own `LICENCE.txt` both say: "The AMI corpus and its annotations are released under the Creative Commons Attribution 4.0 … (CC BY 4.0)."
  - The download page lists this zip as "license altered to CC BY 4.0".
  - The annotation documentation (https://groups.inf.ed.ac.uk/ami/corpus/annotation.shtml) lists "Abstractive and Extractive Summaries" as one of the corpus annotations. They ship inside this zip under `abstractive/` (142 `*.abssumm.xml` files) and `extractive/`.
  - The summaries are therefore covered.
- **Attribution:** AMI Meeting Corpus, AMI Consortium. Distributed by the University of Edinburgh at https://groups.inf.ed.ac.uk/ami/, under CC BY 4.0. The corpus site introduces it with Carletta, J. (2006), "Announcing the AMI Meeting Corpus", *The ELRA Newsletter* 11(1), pp. 3–5.
- **Changes I make:** I select excerpts from scenario meetings and convert them to plain text. The full raw download stays local and is not redistributed (it is git-ignored under `case-study/data/raw/`).

## Contributed by Claude

- **PROJECT-BRIEF.md** (final, 2026-10-14): drafted by Claude (Claude Code) from my inputs; I reviewed it.
- **Alternative checks** (FRICTIONAL.md, 2026-10-14): Claude found and summarized the Maxim AI, orq.ai and GitHub Spec Kit pages; I opened each one on 2026-10-14 and confirmed the summary.
- **Constructed case-study docs** (`case-study/constructed/`: `recap-prd.md`, `recap-system-prompt.md`, `rubric-v0.md`): drafted with Claude; clause decisions by me (Aravind), 2026-10-14. C1's wording, the leakage rule and the decision to keep the 250-word cap are mine. C5 is my wording. C2–C4 and the system prompt text are Claude's drafts, which I kept.
- **Code:** `case-study/scripts/select_ami_sample.py` and `case-study/run_feature.py` were written by Claude Code. The selection rule (whole meetings, under 35 minutes, non-empty DECISIONS) is mine.
