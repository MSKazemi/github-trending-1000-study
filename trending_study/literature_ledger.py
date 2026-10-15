"""Validate an offline *user-supplied* literature-screening ledger.

No database is queried; possible duplicates are flagged, never deleted.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from .data_integrity import ResearchJSONError, load_research_json_file

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
    if d > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise LiteratureError("search cannot be dated in the future")
    return d


def _normalize_doi(raw):
    if raw is None:
        return None
    if not isinstance(raw, str):
        raise LiteratureError("doi must be string or null")
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", raw.strip(), flags=re.I)
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
    run_dates = {}
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
        run_dates[ident] = _utc(run.get("searched_at_utc"))
    seen, duplicate_keys, title_keys, counts = set(), defaultdict(list), defaultdict(list), Counter()
    for row in items:
        if not isinstance(row, dict):
            raise LiteratureError("record must be object")
        ident = row.get("record_id")
        if not isinstance(ident, str) or not ident.strip() or ident in seen:
            raise LiteratureError("unique nonempty record_id required")
        seen.add(ident)
        run_id = row.get("run_id")
        if not isinstance(run_id, str) or not run_id.strip() or run_id not in run_ids:
            # Keep malformed, unhashable JSON values within the documented
            # validation error contract instead of raising a raw TypeError.
            raise LiteratureError("record must reference an existing search run")
        title = row.get("title")
        year = row.get("publication_year")
        if not isinstance(title, str) or not title.strip() or type(year) is not int or year < 1900 or year > 2100:
            raise LiteratureError("record requires title and plausible publication_year")
        if year > run_dates[row["run_id"]].year:
            raise LiteratureError("publication_year cannot postdate its source search run")
        if not isinstance(row.get("source_type"), str) or row["source_type"] not in SOURCE_TYPES:
            raise LiteratureError("invalid source_type")
        decision = row.get("decision")
        if not isinstance(decision, str) or decision not in DECISIONS:
            raise LiteratureError("invalid screening decision")
        if decision == "exclude" and (not isinstance(row.get("reason"), str) or not row["reason"].strip()):
            raise LiteratureError("excluded items require reason")
        if decision == "include":
            # An included finding must be traceable to a specific public source.
            # A DOI *string* alone is only a self-reported identifier: require
            # a canonical, source-specific URL even for DOI-bearing studies.
            source_url = row.get("source_url")
            if (not isinstance(source_url, str) or not source_url.strip()
                    or source_url != source_url.strip()
                    or any(ord(ch) < 33 or ord(ch) == 127 for ch in source_url)):
                raise LiteratureError("included record requires clean source_url")
            try:
                parsed_source = urlsplit(source_url)
                # urlsplit defers malformed/out-of-range port checks until access.
                port = parsed_source.port
                clean_source = (parsed_source.scheme == "https"
                                and bool(parsed_source.hostname)
                                and port != 0
                                and not parsed_source.netloc.endswith(":")
                                and parsed_source.username is None
                                and parsed_source.password is None
                                and not parsed_source.fragment
                                and not parsed_source.query
                                and bool(parsed_source.path.strip("/"))
                                and "\\" not in source_url
                                and re.search(r"%(?![0-9A-Fa-f]{2})", source_url) is None)
            except ValueError as exc:
                raise LiteratureError("invalid included source_url") from exc
            if not clean_source:
                raise LiteratureError("included source_url must be canonical clean HTTPS")
            extract = row.get("study_extract")
            if not isinstance(extract, dict) or any(
                not isinstance(extract.get(k), str) or not extract[k].strip()
                for k in ("design", "population", "outcome", "limitations")
            ):
                raise LiteratureError("included records require descriptive study_extract")
        doi = _normalize_doi(row.get("doi"))
        title_key = "title:" + re.sub(r"\W+", "", title.casefold()) + ":" + str(year)
        title_keys[title_key].append(ident)
        duplicate_keys["doi:" + doi if doi else title_key].append(ident)
        counts[decision] += 1
    return {"search_runs": len(runs), "screened_records": len(items),
            "decisions": {x: counts[x] for x in sorted(DECISIONS)},
            "possible_duplicate_groups": {k: sorted(v) for k, v in sorted(duplicate_keys.items()) if len(v) > 1},
            "title_year_collision_groups": {k: sorted(v) for k, v in sorted(title_keys.items()) if len(v) > 1},
            "duplicate_detection_is_not_adjudication": True,
            "prisma_flow_authenticated": False,
            "screening_is_self_reported": True}


def audit_file(path):
    """Load one bounded regular artifact via the shared strict research reader.

    ``load_research_json_file`` refuses symlinks, special files, oversized or
    grown inputs and ambiguous JSON with fixed, non-path diagnostics.
    """
    try:
        data = load_research_json_file(path)
    except ResearchJSONError as exc:
        if str(exc) == "invalid or ambiguous JSON input":
            # The shared reader already hides duplicate keys and filenames;
            # keep this tool's established decoder diagnostic.
            raise LiteratureError("input must be strict UTF-8 JSON without duplicate "
                                  "keys or invalid numbers") from None
        raise LiteratureError(str(exc)) from exc
    return audit(data)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True, type=Path)
    args = ap.parse_args(argv)
    try:
        out = audit_file(args.input)
    except (OSError, ValueError, RecursionError) as exc:
        ap.error(str(exc))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
