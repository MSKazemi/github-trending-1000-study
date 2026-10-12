"""F01/T02 observed-only sampling audit. Standard-library, offline, fail-closed."""
import argparse
from collections import Counter, defaultdict
from datetime import date, datetime
import hashlib
from html import escape
import json
from pathlib import Path
import re

REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA256 = re.compile(r"^[a-fA-F0-9]{64}$")
WINDOWS = {"daily", "weekly", "monthly"}
REQUIRED = ("repository", "observation_date", "window", "rank", "source_sha256",
            "source_file", "collected_at_utc", "trending_url")


def load_observations(path):
    observations = []
    for line_no, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Line {line_no}: invalid JSON") from exc
        if not isinstance(row, dict):
            raise ValueError(f"Line {line_no}: expected object")
        if any(key not in row for key in REQUIRED):
            raise ValueError(f"Line {line_no}: missing required provenance")
        repository = row["repository"]
        if not isinstance(repository, str) or not REPOSITORY.fullmatch(repository):
            raise ValueError(f"Line {line_no}: invalid repository")
        try:
            date.fromisoformat(row["observation_date"])
            timestamp = datetime.fromisoformat(row["collected_at_utc"].replace("Z", "+00:00"))
            if timestamp.utcoffset() is None:
                raise ValueError("timezone missing")
        except (TypeError, ValueError, AttributeError) as exc:
            raise ValueError(f"Line {line_no}: invalid UTC/date metadata") from exc
        if timestamp.utcoffset().total_seconds() != 0:
            raise ValueError(f"Line {line_no}: collection timestamp must be UTC")
        if row["window"] not in WINDOWS or type(row["rank"]) is not int or row["rank"] < 1:
            raise ValueError(f"Line {line_no}: invalid window/rank")
        if not isinstance(row["source_sha256"], str) or not SHA256.fullmatch(row["source_sha256"]):
            raise ValueError(f"Line {line_no}: invalid source SHA256")
        if not isinstance(row["source_file"], str) or not row["source_file"]:
            raise ValueError(f"Line {line_no}: missing source file")
        if not isinstance(row["trending_url"], str) or not row["trending_url"].startswith("https://github.com/trending"):
            raise ValueError(f"Line {line_no}: non-Trending source URL")
        repo_id = row.get("repository_id")
        if repo_id is not None and (type(repo_id) is not int or repo_id <= 0):
            raise ValueError(f"Line {line_no}: invalid GitHub repository ID")
        observations.append(row)
    if not observations:
        raise ValueError("No observed rows: refuse to produce a misleading empty study figure")
    return observations


def summarize(rows):
    names = defaultdict(set)
    ids_to_names = defaultdict(set)
    snapshots = {}
    appearances = Counter()
    for row in rows:
        name = row["repository"].lower()
        rid = row.get("repository_id")
        if rid is not None:
            names[name].add(rid)
            ids_to_names[rid].add(name)
        key = (row["observation_date"], row["window"], row["source_sha256"])
        snapshot_meta = (row["source_file"], row["trending_url"])
        if key in snapshots and snapshots[key] != snapshot_meta:
            raise ValueError("Conflicting capture metadata for a dated source hash")
        snapshots[key] = snapshot_meta
        appearances[row["window"]] += 1
    # A name may be reassigned after a rename. Escalate for manual ID reconciliation.
    if any(len(ids) > 1 for ids in names.values()):
        raise ValueError("One canonical name resolves to multiple IDs; manual reconciliation needed")
    resolved = set(ids_to_names)
    unresolved_names = {r["repository"].lower() for r in rows
                        if r.get("repository_id") is None and r["repository"].lower() not in names}
    return {
        "evidence_status": "OBSERVED_ONLY_NOT_COHORT",
        "observed_occurrences": len(rows),
        "distinct_displayed_names": len({r["repository"].lower() for r in rows}),
        "unique_resolved_repository_ids": len(resolved),
        "unresolved_displayed_names": len(unresolved_names),
        "observed_capture_groups": len(snapshots),
        "occurrences_by_window": dict(sorted(appearances.items())),
        "first_observation_date": min(r["observation_date"] for r in rows),
        "last_observation_date": max(r["observation_date"] for r in rows),
        "missing_collection_dates": None,
        "eligible_repository_count": None,
        "followup_30d_complete": None,
        "followup_90d_complete": None,
        "followup_180d_complete": None,
        "caveats": [
            "Counts describe input rows only: cannot establish scheduled capture completeness.",
            "Resolved IDs may be fewer than the final eligible cohort; names are mutable.",
            "No exclusion/eligibility register, independent controls or longitudinal followups provided.",
            "A synthetic fixture is not evidence of real Trending activity."
        ]
    }


def table_markdown(summary):
    fields = (
        ("Observed occurrence rows", summary["observed_occurrences"]),
        ("Distinct displayed names (mutable)", summary["distinct_displayed_names"]),
        ("Resolved unique repository IDs", summary["unique_resolved_repository_ids"]),
        ("Unresolved displayed names", summary["unresolved_displayed_names"]),
        ("Observed capture groups", summary["observed_capture_groups"]),
        ("Eligible cohort", "NOT MEASURED"),
        ("Scheduled capture completeness", "NOT MEASURED"),
        ("30/90/180-day follow-up completeness", "NOT MEASURED"),
    )
    lines = [
        "# T02 — observed input counts (NOT a validated 1,000-repository cohort)",
        "",
        "| Measure | Value |",
        "|---|---:|",
    ]
    lines += [f"| {name} | {value} |" for name, value in fields]
    lines += ["", "## Observed occurrences by selected window", "",
              "| Window | Rows |", "|---|---:|"]
    lines += [f"| {window} | {n} |" for window, n in summary["occurrences_by_window"].items()]
    lines += ["", "Only supplied observation rows were audited. These are not inferred total GitHub counts.",
              "Missing, historical, failed and unauthorized capture attempts cannot be inferred from this input.",
              "A validated eligibility, stable-ID and capture manifest is needed before cohort claims.", ""]
    return "\n".join(lines)


def figure_svg(summary):
    occ = summary["observed_occurrences"]
    names = summary["distinct_displayed_names"]
    ids = summary["unique_resolved_repository_ids"]
    unresolved = summary["unresolved_displayed_names"]
    nodes = [
        ("Input occurrence rows", str(occ)),
        ("Distinct displayed names", str(names)),
        ("Resolved stable GitHub IDs", str(ids)),
        ("Unresolved names, ID unavailable", str(unresolved)),
        ("Eligible cohort and follow-up", "NOT MEASURED"),
    ]
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 585" role="img" aria-labelledby="title desc">',
        '<title id="title">F01 observed-input sampling audit</title>',
        '<desc id="desc">Observed counts are from supplied JSONL only. Eligibility and follow-up are not measured.</desc>',
        '<rect width="760" height="585" fill="white"/>',
        '<text x="32" y="35" font-family="sans-serif" font-weight="bold" font-size="21" fill="#17324D">F01 · Observed sampling audit</text>',
        '<text x="32" y="61" font-family="sans-serif" font-size="14" fill="#874D18">OBSERVED INPUT ONLY — NOT VALIDATED COHORT</text>',
    ]
    for i, (label, value) in enumerate(nodes):
        y = 86 + i * 91
        out += [
            f'<rect x="65" y="{y}" width="630" height="70" rx="7" fill="#F0F4F7" stroke="#567D9C"/>',
            f'<text x="88" y="{y+28}" font-family="sans-serif" font-size="17" fill="#16324A">{escape(label)}</text>',
            f'<text x="675" y="{y+50}" text-anchor="end" font-family="sans-serif" font-size="18" font-weight="bold" fill="#17324D">{escape(value)}</text>',
        ]
        if i < len(nodes) - 1:
            out.append(f'<path d="M380 {y+70} v20" stroke="#59798D" stroke-width="2"/>')
    out += ['<text x="32" y="563" font-family="sans-serif" font-size="12" fill="#555">Unresolved IDs, unobserved captures and eligibility require independent reconciliation.</text>', '</svg>']
    return "\n".join(out) + "\n"


def run(argv=None):
    parser = argparse.ArgumentParser(description="Offline F01/T02 observed-only audit")
    parser.add_argument("--input", required=True, help="JSONL observation records (fixture or actual capture)")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--synthetic", action="store_true", help="Explicit synthetic-demo flag; outputs prominently labeled")
    args = parser.parse_args(argv)
    rows = load_observations(args.input)
    summary = summarize(rows)
    summary["input_sha256"] = hashlib.sha256(Path(args.input).read_bytes()).hexdigest()
    summary["input_type"] = "SYNTHETIC_FIXTURE" if args.synthetic else "USER_SUPPLIED_UNVERIFIED"
    # Never upgrade status to confirmed observations based solely on caller's assertion.
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    prefix = "SYNTHETIC DEMONSTRATION — " if args.synthetic else "UNVERIFIED INPUT — "
    (out / "F01_observed_sampling.svg").write_text(
        figure_svg(summary).replace("OBSERVED INPUT ONLY", prefix + "OBSERVED INPUT ONLY"), encoding="utf-8")
    (out / "T02_observed_counts.md").write_text(prefix + "\n\n" + table_markdown(summary), encoding="utf-8")
    (out / "sampling_audit.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": summary["evidence_status"], "files": ["F01_observed_sampling.svg", "T02_observed_counts.md", "sampling_audit.json"]}))


if __name__ == "__main__":
    run()
