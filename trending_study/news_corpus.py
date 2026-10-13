"""Offline validation of provisional AI-era news evidence records.

Does not validate source claims or authenticate independent review.
"""
import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


ID_RE = re.compile(r"NEWS-[0-9]{4}-[0-9]{4}$")
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
        # URL fragments and tracking query parameters should not make two
        # records appear independent; query strings are ignored for detection.
        # HTTP paths may be case-sensitive; hostnames are case-insensitive.
        # Keep the path case to avoid collapsing distinct source documents.
        canonical = (parsed.hostname.lower(), parsed.path.rstrip("/"))
        if canonical in urls:
            raise ValueError(f"{name}: duplicate canonical source URL")
        urls.add(canonical)
        if record["review_status"] == "pending" and record["independent_reviewer"] is not None:
            raise ValueError(f"{name}: pending independent review cannot name reviewer")
    return {"records": len(ids), "distinct_urls": len(urls),
            "evidence_status": "provisional_structural_validation_only"}


def validate_directory(directory):
    directory = Path(directory)
    paths = sorted(directory.glob("NEWS-*.json"))
    if not paths:
        raise ValueError("no news records found")
    records = [(p.name, json.loads(p.read_text(encoding="utf-8"))) for p in paths]
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
