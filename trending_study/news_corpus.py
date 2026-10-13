"""Offline validation of provisional AI-era news evidence records.

Does not validate source claims or authenticate independent review.
"""
import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, urlsplit

# Reuse the canonical offline research decoder instead of interpreting
# duplicate keys, NaN/Infinity, or extreme numeric literals differently.
from trending_study.data_integrity import (
    MAX_FILES, MAX_FILE_BYTES, MAX_TOTAL_BYTES, _decode_document,
)


ID_RE = re.compile(r"NEWS-[0-9]{4}-[0-9]{4}$")
TRACKING_PARAMS = frozenset(("fbclid", "gclid", "msclkid", "mc_cid", "mc_eid", "igshid", "yclid", "twclid", "wbraid", "gbraid"))


def _canonical_url_key(parts):
    """Deduplicate tracking variants without merging distinct query-addressed pages.

    `ref` is deliberately kept: it may encode a branch or document selector,
    not merely marketing attribution. This is syntactic screening, not a claim
    that different URLs describe different underlying events.
    """
    query = tuple(sorted((key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True)
                         if not key.lower().startswith("utm_") and key.lower() not in TRACKING_PARAMS))
    return (parts.hostname.lower(), parts.port or 443, parts.path.rstrip("/") or "/", query)

REQUIRED = {
    "schema_version", "id", "title", "publisher", "author",
    "original_publication_date", "accessed_date_utc", "canonical_url",
    "source_type", "topics", "screening_status", "source_review_status",
    "attributed_claim_summary", "evidence_or_event",
    "confidence_in_article_reporting", "independent_corrob_status",
    "limitations", "research_relevance", "practical_experiment",
    "policy_conclusion", "independent_reviewer", "review_status",
    "related_existing_sources", "correction_status", "fulltext_stored",
}
TEXT = {"title", "publisher", "source_type", "screening_status",
        "source_review_status", "attributed_claim_summary",
        "evidence_or_event", "confidence_in_article_reporting",
        "independent_corrob_status", "limitations", "research_relevance",
        "practical_experiment", "policy_conclusion", "review_status",
        "correction_status"}


def validate_records(records):
    if not isinstance(records, list):
        raise ValueError("expected array of records")
    ids, urls = set(), set()
    for name, record in records:
        if not isinstance(record, dict) or set(record) != REQUIRED:
            raise ValueError(f"{name}: incorrect record fields")
        identifier = record["id"]
        if not isinstance(identifier, str) or not ID_RE.fullmatch(identifier):
            raise ValueError(f"{name}: invalid ID")
        if name != identifier + ".json":
            raise ValueError(f"{name}: filename and ID mismatch")
        if identifier in ids:
            raise ValueError(f"{name}: duplicate ID")
        ids.add(identifier)
        if record["schema_version"] != "1.0":
            raise ValueError(f"{name}: unsupported schema")
        for field in TEXT:
            value = record[field]
            if not isinstance(value, str) or not value.strip() or len(value) > 2500:
                raise ValueError(f"{name}: invalid {field}")
        if not isinstance(record["topics"], list) or not record["topics"] or not all(
            isinstance(x, str) and x.strip() and len(x) <= 80 for x in record["topics"]
        ):
            raise ValueError(f"{name}: invalid topics")
        if not isinstance(record["related_existing_sources"], list) or not all(
            isinstance(x, str) and x.strip() for x in record["related_existing_sources"]
        ):
            raise ValueError(f"{name}: invalid related source IDs")
        if record["author"] is not None and not isinstance(record["author"], str):
            raise ValueError(f"{name}: invalid author")
        if record["independent_reviewer"] is not None and not isinstance(record["independent_reviewer"], str):
            raise ValueError(f"{name}: invalid reviewer")
        if type(record["fulltext_stored"]) is not bool:
            raise ValueError(f"{name}: invalid fulltext flag")
        # fromisoformat also accepts compact and week dates; the corpus requires
        # an unambiguous YYYY-MM-DD calendar date for reproducible review.
        for field in ("original_publication_date", "accessed_date_utc"):
            value = record[field]
            if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
                raise ValueError(f"{name}: invalid dates ({field} must be YYYY-MM-DD)")
        try:
            publication = date.fromisoformat(record["original_publication_date"])
            accessed = date.fromisoformat(record["accessed_date_utc"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name}: invalid dates") from exc
        if publication > accessed or accessed > datetime.now(timezone.utc).date():
            raise ValueError(f"{name}: future publication/access date")
        url = record["canonical_url"]
        if not isinstance(url, str) or len(url) > 2048 or url != url.strip():
            raise ValueError(f"{name}: invalid canonical URL")
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.fragment:
            raise ValueError(f"{name}: canonical URL must be clean HTTPS")
        # Strip known marketing trackers, not meaningful ?id=... or ?ref=...
        # selectors; treating all queries as duplicates can erase real studies.
        canonical = _canonical_url_key(parsed)
        if canonical in urls:
            raise ValueError(f"{name}: duplicate canonical source URL")
        urls.add(canonical)
        # Schema 1.0 stores provisional, single-screened entries only.
        # An arbitrary string must never self-certify an independent audit.
        # Signed reviewer evidence and dates require a separately versioned
        # schema/procedure; this validator cannot authenticate those people.
        if (record["review_status"] != "pending"
                or record["independent_reviewer"] is not None):
            raise ValueError(f"{name}: pending independent review only in schema v1.0")
        if (record["screening_status"] != "included_provisional_single_reviewer"
                or record["source_review_status"] !=
                   "web_primary_page_inspected_not_independently_fact_checked"
                or record["independent_corrob_status"] != "not_assessed"):
            raise ValueError(f"{name}: unverified source cannot claim independent review")
        if record["fulltext_stored"]:
            raise ValueError(f"{name}: source fulltext storage not permitted in v1.0")
        if any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in url):
            raise ValueError(f"{name}: canonical URL cannot contain whitespace or controls")
    return {"records": len(ids), "distinct_urls": len(urls),
            "evidence_status": "provisional_structural_validation_only"}


def validate_directory(directory):
    """Read only bounded, ordinary files; reject linked/unreviewed evidence."""
    directory = Path(directory)
    if directory.is_symlink():
        raise ValueError("news records directory symlink is forbidden")
    if not directory.is_dir():
        raise ValueError("news records directory does not exist or is not a directory")
    paths = sorted(directory.glob("NEWS-*.json"))
    if not paths:
        raise ValueError("no news records found")
    if len(paths) > MAX_FILES:
        raise ValueError("news records exceed research artifact file-count limit")

    records = []
    total_bytes = 0
    for path in paths:
        # This CLI must be fail-closed even outside a full repository checkout:
        # the main CI integrity gate alone cannot protect standalone callers.
        if path.is_symlink():
            raise ValueError(f"{path.name}: symlinked news input is forbidden")
        if not path.is_file():
            raise ValueError(f"{path.name}: expected an ordinary JSON file")
        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            raise ValueError(f"{path.name}: news input exceeds file-size limit")
        total_bytes += size
        if total_bytes > MAX_TOTAL_BYTES:
            raise ValueError("news inputs exceed total research artifact byte limit")
        records.append((path.name, _decode_document(path.read_bytes(), path.name)))
    return validate_records(records)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate research-news JSON structure offline")
    parser.add_argument("--directory", default="references/ai-era-news/items")
    args = parser.parse_args(argv)
    try:
        result = validate_directory(args.directory)
    except (OSError, TypeError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
