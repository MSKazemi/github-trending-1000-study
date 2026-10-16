"""Offline structural screening of *provisional* news source leads.

Derived from draft PR #59 without importing unreviewed source records.
Syntax, provenance fields, and duplicate URL detection never authenticate a
source, rights, publication date, claim, actual human review, or research value.
"""
import argparse
from datetime import date, datetime, timezone
import ipaddress
import json
import os
from pathlib import Path
import re
import stat
from urllib.parse import unquote_plus, urlsplit

# Reuse the canonical offline research decoder instead of interpreting
# duplicate keys, NaN/Infinity, or extreme numeric literals differently.
from trending_study.data_integrity import (
    MAX_FILES, MAX_FILE_BYTES, MAX_TOTAL_BYTES, decode_research_json,
)


ID_RE = re.compile(r"NEWS-[0-9]{4}-[0-9]{4}$")
TRACKING_PARAMS = frozenset(("fbclid", "gclid", "msclkid", "mc_cid", "mc_eid", "igshid", "yclid", "twclid", "wbraid", "gbraid"))
_DNS_LABEL = re.compile(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\\Z")
_NUMERIC_IPV4_PART = r"(?:0[xX][0-9A-Fa-f]+|0[0-7]+|[0-9]+)"


def _public_source_host(host):
    """Conservative lexical URL evidence screening, NOT DNS/SSRF protection."""
    if not isinstance(host, str) or not host or len(host) > 253:
        return False
    if host == "localhost" or host.endswith((".localhost", ".local", ".internal")):
        return False
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    if address is not None:
        return address.is_global
    # Legacy network stacks may resolve numeric spellings rejected by
    # ipaddress (127.1, 2130706433, 0x7f000001) to special IPv4 addresses.
    if re.fullmatch(_NUMERIC_IPV4_PART + r"(?:\\." + _NUMERIC_IPV4_PART + r"){0,3}",
                    host, flags=re.IGNORECASE):
        return False
    labels = host.split(".")
    return len(labels) >= 2 and all(
        len(label) <= 63 and _DNS_LABEL.fullmatch(label) is not None
        for label in labels
    )


def _canonical_url_key(parts):
    """Deduplicate tracking variants without merging distinct query-addressed pages.

    `ref` is deliberately kept: it may encode a branch or document selector,
    not merely marketing attribution. This is syntactic screening, not a claim
    that different URLs describe different underlying events.
    """
    # Keep the RAW spelling of meaningful selectors. parse_qsl() decodes
    # %2F to "/" and "+" to a space; some origin servers inspect raw query
    # bytes, so collapsing either form could silently discard a source lead.
    # Only remove literal, known marketing keys; an encoded key is ambiguous.
    query_items = []
    for item in parts.query.split("&") if parts.query else []:
        key = item.partition("=")[0]
        if key.lower().startswith("utm_") or key.lower() in TRACKING_PARAMS:
            continue
        query_items.append((key, item))
    # Detect keys that become equal only after decoding, but preserve their
    # original spelling and sequence. Encoded keys are not safely sortable.
    decoded_names = [unquote_plus(key) for key, _ in query_items]
    order_sensitive = (len(decoded_names) != len(set(decoded_names))
                       or any("%" in key or "+" in key for key, _ in query_items))
    query = tuple(item for _, item in (
        query_items if order_sensitive else sorted(query_items)
    ))
    # A trailing slash can identify a different resource on the same host:
    # /report and /report/ must not be silently conflated as source evidence.
    # Empty path and explicit root slash share the HTTP root request path.
    return (parts.hostname.lower(), parts.port if parts.port is not None else 443,
            parts.path or "/", query)

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
        # urlsplit may silently strip certain ASCII control characters.
        # Reject the raw submitted spelling before any parsing or filtering.
        if any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in url):
            raise ValueError(f"{name}: canonical URL cannot contain whitespace or controls")
        try:
            parsed = urlsplit(url)
            # Force malformed/overflowing ports and broken IPv6 authority to
            # fail with the same documented input-validation exception.
            port = parsed.port
        except ValueError as exc:
            raise ValueError(f"{name}: malformed canonical HTTPS authority") from exc
        if (parsed.scheme != "https" or not parsed.hostname
                or parsed.username is not None or parsed.password is not None
                or parsed.netloc.endswith(":") or port == 0 or parsed.fragment):
            raise ValueError(f"{name}: canonical URL must be clean HTTPS")
        if not _public_source_host(parsed.hostname):
            raise ValueError(f"{name}: canonical URL requires a public source host")
        if "\\" in url or re.search(r"%(?![0-9A-Fa-f]{2})", url):
            raise ValueError(f"{name}: malformed or ambiguous canonical URL")
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
        allowed_provisional = (
            record["screening_status"] == "included_provisional_single_reviewer"
            and record["source_review_status"] ==
                "web_primary_page_inspected_not_independently_fact_checked"
        )
        allowed_synthetic = (
            record["screening_status"] == "synthetic_test_only"
            and record["source_review_status"] == "not_inspected_synthetic_fixture"
        )
        if (not (allowed_provisional or allowed_synthetic)
                or record["independent_corrob_status"] != "not_assessed"):
            raise ValueError(f"{name}: unverified source cannot claim independent review")
        if record["fulltext_stored"]:
            raise ValueError(f"{name}: source fulltext storage not permitted in v1.0")
        if any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in url):
            raise ValueError(f"{name}: canonical URL cannot contain whitespace or controls")
    return {"records": len(ids), "distinct_urls": len(urls),
            "evidence_status": "provisional_structural_validation_only"}


def _read_record(path):
    """Bound actual bytes from one opened regular file, not an earlier stat."""
    # A local reader (not data_integrity.load_research_json_file) is kept
    # because the directory-wide total cap needs the actual bytes read.
    # OSError text embeds the full input path, so it is replaced by a fixed
    # diagnostic (e.g. a leaf symlink swapped in after the is_symlink check).
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    descriptor = None
    try:
        descriptor = os.open(path, flags)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise ValueError(f"{path.name}: expected an ordinary JSON file")
        if metadata.st_size > MAX_FILE_BYTES:
            raise ValueError(f"{path.name}: news input exceeds file-size limit")
        stream = os.fdopen(descriptor, "rb")
        descriptor = None
        with stream:
            raw = stream.read(MAX_FILE_BYTES + 1)
        if len(raw) > MAX_FILE_BYTES:
            raise ValueError(f"{path.name}: news input exceeds file-size limit")
        return raw
    except OSError:
        raise ValueError("news input must be a readable ordinary non-symlink file") from None
    finally:
        if descriptor is not None:
            os.close(descriptor)


def validate_directory(directory):
    """Read only bounded, ordinary files; reject linked/unreviewed evidence."""
    directory = Path(directory)
    if directory.is_symlink():
        raise ValueError("news records directory symlink is forbidden")
    if not directory.is_dir():
        raise ValueError("news records directory does not exist or is not a directory")
    # Inspect every directory entry, not only matching globs: a misspelled
    # JSON record or symlink must not silently disappear from the denominator.
    paths = []
    count = 0
    for path in directory.iterdir():
        count += 1
        if count > MAX_FILES + 1:
            raise ValueError("news source directory exceeds file-count limit")
        if path.is_symlink():
            raise ValueError("symlinked news input is forbidden")
        if path.is_dir():
            raise ValueError("nested news directories are not inspected")
        if path.suffix == ".json":
            if not ID_RE.fullmatch(path.stem):
                raise ValueError("unexpected JSON record filename")
            paths.append(path)
        elif path.name != "README.md":
            raise ValueError("unexpected non-record file")
    if not paths:
        raise ValueError("no news records found")
    paths.sort()

    records = []
    total_bytes = 0
    for path in paths:
        # This CLI must be fail-closed even outside a full repository checkout:
        # the main CI integrity gate alone cannot protect standalone callers.
        if path.is_symlink():
            raise ValueError("symlinked news input is forbidden")
        if not path.is_file():
            raise ValueError(f"{path.name}: expected an ordinary JSON file")
        raw = _read_record(path)
        total_bytes += len(raw)
        if total_bytes > MAX_TOTAL_BYTES:
            raise ValueError("news inputs exceed total research artifact byte limit")
        try:
            record = decode_research_json(raw, path.name)
        except (ValueError, RecursionError):
            # Decoder diagnostics can contain untrusted, private object keys.
            raise ValueError(f"{path.name}: invalid or ambiguous research JSON") from None
        records.append((path.name, record))
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
