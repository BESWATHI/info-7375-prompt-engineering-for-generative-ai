"""The watch: fetch one allow-listed board, save the raw response, report new ids.

Usage:
    python3 watch.py                      # live fetch of the Databricks board
    python3 watch.py --from-file RAW.json # SEEDED run: replay a saved response

The first run (no state file) is a baseline: it records every posting id and
reports none as new. Later runs report only ids absent from the previous run.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
import urllib.parse
import urllib.request

import persona
import rule

HERE = Path(__file__).resolve().parent
BOARD = "databricks"
BOARD_URL = f"https://boards-api.greenhouse.io/v1/boards/{BOARD}/jobs"
ALLOWED_HOSTS = frozenset({"boards-api.greenhouse.io"})
USER_AGENT = "js1-contract-and-watch/1 (INFO 7375 coursework; read-only, polite polling)"
STATE_PATH = HERE / "state" / "seen_ids.json"
RAW_DIR = HERE / "runs" / "raw"
REPORT_DIR = HERE / "runs" / "reports"
CLAUDE_JUDGE = "not built in this layer"


class HostNotAllowed(ValueError):
    pass


def check_allowed(url):
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise HostNotAllowed(f"refusing to fetch {url!r}: host not on allow-list {sorted(ALLOWED_HOSTS)}")
    return url


class _AllowListRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_allowed(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url, timeout=30):
    check_allowed(url)
    opener = urllib.request.build_opener(_AllowListRedirects)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with opener.open(request, timeout=timeout) as response:
        return response.status, response.read()


def stamp(moment):
    return moment.strftime("%Y-%m-%dT%H-%M-%S%z")


def save_raw(body, fetched_at, url, status, raw_dir=RAW_DIR, name=BOARD):
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / f"{name}_{stamp(fetched_at)}.json"
    path.write_bytes(body)
    meta = {"url": url, "http_status": status, "fetched_at": fetched_at.isoformat(),
            "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    path.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return path


def parse_postings(body):
    jobs = json.loads(body)["jobs"]
    postings = [{"id": job["id"], "title": job["title"], "location": (job.get("location") or {}).get("name", ""),
                 "absolute_url": job.get("absolute_url"), "first_published": job.get("first_published"),
                 "updated_at": job.get("updated_at")} for job in jobs]
    ids = [p["id"] for p in postings]
    if len(ids) != len(set(ids)):
        raise ValueError("response repeats a posting id; ids are not usable as keys")
    return postings


def load_state(path=STATE_PATH):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(postings, run_at, raw_path, label, path=STATE_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    state = {"board": BOARD, "host": sorted(ALLOWED_HOSTS)[0], "run_at": run_at.isoformat(),
             "run_label": label, "raw_response": _relative(raw_path),
             "seen_ids": sorted(p["id"] for p in postings)}
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def new_since(previous_ids, postings):
    seen = set(previous_ids)
    return [p for p in postings if p["id"] not in seen]


def build_report(new_postings, targets):
    return [{"posting_id": p["id"], "title": p["title"], "location": p["location"],
             "absolute_url": p["absolute_url"], "first_published": p["first_published"],
             "rule": rule.judge(p["title"], p["location"], targets), "claude_judge": CLAUDE_JUDGE}
            for p in new_postings]


def pairing_errors(postings, report, targets):
    """Wrong version 1: every verdict must belong to the posting it is reported against."""
    by_id = {p["id"]: p for p in postings}
    errors = []
    if len(report) != len(postings):
        errors.append(f"{len(report)} report entries for {len(postings)} new postings")
    for entry in report:
        posting = by_id.get(entry["posting_id"])
        if posting is None:
            errors.append(f"report entry for unknown posting id {entry['posting_id']}")
            continue
        if (entry["title"], entry["location"]) != (posting["title"], posting["location"]):
            errors.append(f"posting {posting['id']}: entry title/location do not match the posting")
        expected = rule.judge(posting["title"], posting["location"], targets)
        if entry["rule"]["verdict"] != expected["verdict"] or entry["rule"]["justification"] != expected["justification"]:
            errors.append(f"posting {posting['id']}: verdict or justification belongs to a different posting")
    return errors


def _relative(path):
    try:
        return str(Path(path).resolve().relative_to(HERE))
    except ValueError:
        return str(path)


def run(from_file=None, now=None, state_path=STATE_PATH, raw_dir=RAW_DIR, report_dir=REPORT_DIR):
    now = now or datetime.now().astimezone()
    _, targets = persona.load_persona()
    if from_file:
        raw_path = Path(from_file)
        body, kind = raw_path.read_bytes(), "seeded"
    else:
        status, body = fetch(BOARD_URL)
        raw_path, kind = save_raw(body, now, BOARD_URL, status, raw_dir), "live"
    postings = parse_postings(body)
    state = load_state(state_path)
    baseline = state is None
    new = [] if baseline else new_since(state["seen_ids"], postings)
    report = build_report(new, targets)
    errors = pairing_errors(new, report, targets) + [e for r in report for e in rule.justification_errors(r["rule"])]
    if errors:
        raise RuntimeError("refusing to write a report that fails its own checks: " + "; ".join(errors))
    label = "baseline" if baseline else kind
    summary = {"run_at": now.isoformat(), "run_label": label,
               "seeded": kind == "seeded", "board_url": BOARD_URL, "raw_response": _relative(raw_path),
               "previous_run_at": None if baseline else state["run_at"], "postings_in_response": len(postings),
               "new_postings": len(new), "relevant_by_rule": sum(r["rule"]["verdict"] == rule.RELEVANT for r in report),
               "claude_judge": CLAUDE_JUDGE, "report": report}
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{BOARD}_{stamp(now)}_{label}.json"
    report_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    save_state(postings, now, raw_path, label, state_path)
    summary["report_path"] = _relative(report_path)
    return summary


def print_summary(summary, out=sys.stdout):
    if summary["seeded"]:
        print(f"SEEDED RUN: replayed saved response {summary['raw_response']}; this is not a live fetch.", file=out)
    print(f"run_at:      {summary['run_at']}  ({summary['run_label']})", file=out)
    print(f"source:      {summary['board_url']}", file=out)
    print(f"raw saved:   {summary['raw_response']}", file=out)
    print(f"postings:    {summary['postings_in_response']} in response", file=out)
    if summary["run_label"] == "baseline":
        print("BASELINE: no previous state; every id recorded, 0 reported as new.", file=out)
    else:
        print(f"new since {summary['previous_run_at']}: {summary['new_postings']} "
              f"({summary['relevant_by_rule']} relevant by the written rule)", file=out)
    for entry in summary["report"]:
        print(f"\n- [{entry['posting_id']}] {entry['title']} | {entry['location']}", file=out)
        print(f"  rule verdict (record): {entry['rule']['verdict']}", file=out)
        print(f"  justification: {entry['rule']['justification']}", file=out)
        print(f"  Claude verdict (judgment): {entry['claude_judge']}", file=out)
        print(f"  {entry['absolute_url']}", file=out)
    print(f"\nreport:      {summary['report_path']}", file=out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--from-file", help="replay a saved raw response (labelled SEEDED)")
    args = parser.parse_args(argv)
    print_summary(run(from_file=args.from_file))


if __name__ == "__main__":
    main()
