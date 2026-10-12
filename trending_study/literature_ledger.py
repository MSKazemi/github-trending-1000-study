"""Validate an offline *user-supplied* literature-screening ledger.

No database is queried; possible duplicates are flagged, never deleted.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime
import json
from pathlib import Path
import re

DECISIONS = {"include", "exclude", "pending"}
SOURCE_TYPES = {"peer_reviewed", "preprint", "standard", "news", "vendor", "other"}
DOI = re.compile(r"^10\.\d{4,9}/\S+$", re.I)


class LiteratureError(ValueError):
    pass


def _utc(s):
    if not isinstance(s, str):
        raise LiteratureError("searched_at_utc must be string")
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError as exc:
        raise LiteratureError("invalid searched_at_utc") from exc
    if d.tzinfo is None or d.utcoffset().total_seconds() != 0:
        raise LiteratureError("search timestamp must be UTC")


def _normalize_doi(raw):
    if raw is None:
        return None
    if not isinstance(raw, str):
        raise LiteratureError("doi must be string or null")
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", raw.strip(), flags=re.I)
    if not DOI.fullmatch(value):
        raise LiteratureError("DOI must be a valid DOI identifier (not arbitrary URL)")
    return value.lower()


def audit(data):
    if not isinstance(data, dict):
        raise LiteratureError("expected object")
    runs, items = data.get("search_runs"), data.get("records")
    if not isinstance(runs, list) or not runs or not isinstance(items, list):
        raise LiteratureError("nonempty search_runs and records list required")
    run_ids = set()
    for run in runs:
        if not isinstance(run, dict):
            raise LiteratureError("run must be object")
        ident = run.get("run_id")
        if not isinstance(ident, str) or not ident.strip() or ident in run_ids:
            raise LiteratureError("unique nonempty run_id required")
        run_ids.add(ident)
        for key in ("database", "query"):
            if not isinstance(run.get(key), str) or not run[key].strip():
                raise LiteratureError("database and exact query required")
        _utc(run.get("searched_at_utc"))
    seen, duplicate_keys, counts = set(), defaultdict(list), Counter()
    for row in items:
        if not isinstance(row, dict):
            raise LiteratureError("record must be object")
        ident = row.get("record_id")
        if not isinstance(ident, str) or not ident.strip() or ident in seen:
            raise LiteratureError("unique nonempty record_id required")
        seen.add(ident)
        if row.get("run_id") not in run_ids:
            raise LiteratureError("record must reference an existing search run")
        title = row.get("title")
        year = row.get("publication_year")
        if not isinstance(title, str) or not title.strip() or type(year) is not int or year < 1900 or year > 2100:
            raise LiteratureError("record requires title and plausible publication_year")
        if row.get("source_type") not in SOURCE_TYPES:
            raise LiteratureError("invalid source_type")
        decision = row.get("decision")
        if decision not in DECISIONS:
            raise LiteratureError("invalid screening decision")
        if decision == "exclude" and (not isinstance(row.get("reason"), str) or not row["reason"].strip()):
            raise LiteratureError("excluded items require reason")
        if decision == "include":
            extract = row.get("study_extract")
            if not isinstance(extract, dict) or any(
                not isinstance(extract.get(k), str) or not extract[k].strip()
                for k in ("design", "population", "outcome", "limitations")
            ):
                raise LiteratureError("included records require descriptive study_extract")
        doi = _normalize_doi(row.get("doi"))
        duplicate_keys["doi:" + doi if doi else "title:" + re.sub(r"\W+", "", title.casefold()) + ":" + str(year)].append(ident)
        counts[decision] += 1
    return {"search_runs": len(runs), "screened_records": len(items),
            "decisions": {x: counts[x] for x in sorted(DECISIONS)},
            "possible_duplicate_groups": {k: sorted(v) for k, v in sorted(duplicate_keys.items()) if len(v) > 1},
            "duplicate_detection_is_not_adjudication": True,
            "screening_is_self_reported": True}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = audit(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
