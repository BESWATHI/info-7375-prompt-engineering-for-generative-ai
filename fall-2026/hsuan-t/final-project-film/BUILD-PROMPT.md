# BUILD PROMPTS & REPRODUCTION — The Reallocation Engine Pitch Film

This document records the exact command pipeline, build prompts, and parameters used to author, render, and verify the final pitch film.

## 1. Pipeline Environment
* **Platform**: macOS (Apple Silicon Darwin)
* **Framework**: Brutalist (`~/IsaacPARA/Projects/info7375_prompt_eng_agentic_ai/brutalist.art`)
* **Target Project**: `film/youtube/final-project-pitch-film`
* **Resolution**: Native 4K UHD (3840 × 2160), 24 fps

## 2. Key Authoring Prompts & Decisions
The film was structured around the 7 mandatory pitch questions and the strict **Honesty Rule**:
- **Cold Open (`BIDEA`)**: Hesitant writer typing the core question and correcting "guessing" to "hallucinating".
- **Product Scope (`B01` - `B03`)**: Showing real tech role filters (SWE/DevOps/QA), contrasting raw black-box AI with source-grounded SEC/DOL records, and demonstrating the 3-stage workspace.
- **Dataflow (`B04`)**: Visualizing URL ingest through verification gates and DOL/SEC databases to the final decision.
- **Scope Discipline (`B05`)**: Demonstrating In-Scope items (Sponsor lookup, Hash deduplication) while explicitly marking "Auto-Apply Bot" as OUT OF SCOPE.
- **Honesty in Deduplication (`B06`)**: Grounded in reality—listing 3 realistic duplicates (`Meta`, `Amazon`, `Stripe`) with SHA-256 hash keys rather than inflated metrics.
- **Proof & Provenance (`B07`)**: Audit trail freezing on `[model-judgment] Quote Proof` with exact quote backing.
- **Outro (`BOUT`)**: Creator card crediting Isaac Tai with portfolio links.

## 3. Reproduction Commands

### Step 1: Generate Kokoro Audio
```bash
python3 runtime/scripts/generate_audio_kokoro.py ../film/youtube/final-project-pitch-film
```

### Step 2: Render Beats & Check Gates (Review Cut)
```bash
./art run ../film/youtube/final-project-pitch-film --height 2160
```

### Step 3: Verify Deterministic Typography (Gate T)
```bash
python3 runtime/scripts/type_check.py ../film/youtube/final-project-pitch-film
```

### Step 4: Export Verified 4K Master Final Cut
```bash
./art final ../film/youtube/final-project-pitch-film --height 2160 --out ../film/youtube/final-project-pitch-film/exports/landscape
```
Output artifact: `exports/landscape/final-project-pitch.mp4` (111.2s, 4K, 0 Gate Failures).
