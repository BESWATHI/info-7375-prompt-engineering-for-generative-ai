# figma/ — Figma's open jobs, saved by date

## Executive summary

**What this is.** A dated copy of every job Figma lists on its public job board, one JSON file per day it was saved.

**Why keep it.** A saved copy is evidence. It shows what the board said on a given day, so later runs can be compared against it and nobody has to trust memory about what was posted.

**What it holds so far.** One file: **160 open jobs on 2026-09-23**. That's the same set of jobs as the snapshot the greenhouse-watch demo took about seven minutes earlier.

---

| File | Fetched | Jobs |
|---|---|---:|
| `figma-jobs-2026-09-23.json` | 2026-09-23 20:01 UTC | 160 |

Each file is Figma's public Greenhouse API response from
`https://boards-api.greenhouse.io/v1/boards/figma/jobs?content=true`.
The API sends it as one minified line, so it is **indented for reading before it is saved**. The data is unchanged; only the whitespace differs, and that was checked by parsing the file before and after.
It has two top-level keys: `jobs`, one record per posting (id, title, location, URL, first-published and updated dates, departments, offices, full posting text), and `meta.total`.

It was fetched with the Reallocation Engine's `greenhouse-watch` skill in dry-run mode: one request to the allow-listed Greenhouse host, with nothing matched or recorded. To add a day:

```bash
python3 .claude/skills/greenhouse-watch/scripts/greenhouse_watch.py \
  --board figma --resume <any example résumé> --state /tmp/figma.state.json \
  --out /tmp/figma-fetch/ --dry-run
python3 -c "import json,sys; d=json.load(open(sys.argv[1])); json.dump(d, open(sys.argv[2],'w'), indent=2, ensure_ascii=False)" \
  /tmp/figma-fetch/raw-*.json figma/figma-jobs-$(date +%F).json
```

Run it from a clone of the-reallocation-engine, and give `figma/` as the path to this folder.
