"""Validate committed research JSON/JSONL/CSV inputs without network dependencies.

This guards file *syntax and information preservation* (not scientific truth,
third-party licensing, evidence provenance, or participant consent). In
particular, duplicate JSON keys must not silently replace earlier values.
"""
import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
import io
import json
import math
import re
from pathlib import Path
import sys
from urllib.parse import urlsplit


DATA_DIRS = ("examples", "references", "research-notes", "research", "templates")
REQUIRED_DATA_DIRS = frozenset(("examples", "references", "research-notes"))
SUFFIXES = {".json", ".jsonl", ".csv"}
MAX_BYTES_PER_FILE = 16 * 1024 * 1024
MAX_TOTAL_BYTES = 128 * 1024 * 1024
MAX_FILES = 5000
MAX_JSON_DEPTH = 128


class IntegrityError(ValueError):
    """A checked research artifact would lose information or cannot be read."""


def _unique_fields(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise IntegrityError(f"duplicate JSON object key {key!r}")
        out[key] = value
    return out


def _invalid_constant(value):
    raise IntegrityError(f"nonstandard JSON constant {value!r}")


def _finite_decimal(value):
    """Retain decimal digits while rejecting floats that would overflow or vanish."""
    try:
        exact = Decimal(value)
        approximate = float(exact)
    except (InvalidOperation, OverflowError, ValueError) as exc:
        raise IntegrityError("unrepresentable JSON numeric literal") from exc
    if not math.isfinite(approximate) or (exact != 0 and approximate == 0):
        raise IntegrityError("JSON numeric literal overflows or underflows finite float")
    return exact


def _bounded_integer(value):
    # Avoid Python 3.11+ integer digit conversion limits turning CI into a
    # version-dependent traceback instead of a fail-closed integrity error.
    if len(value.lstrip("-")) > 1024:
        raise IntegrityError("JSON integer has more than 1024 digits")
    return int(value)


def _check_json_depth(text):
    """Count structural brackets outside quoted strings before JSON decoding.

    Python JSON decoders accept different maximum depths across interpreter
    versions. Bound nesting explicitly to avoid version-dependent corruption,
    recursion failure, or unexpectedly expensive inputs.
    """
    depth = 0
    in_string = False
    escaped = False
    for char in text:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                raise IntegrityError(f"JSON nesting exceeds {MAX_JSON_DEPTH} levels")
        elif char in "]}":
            depth -= 1
            if depth < 0:
                raise IntegrityError("unbalanced JSON container closing bracket")


def _strict_json(text):
    _check_json_depth(text)
    return json.loads(
        text,
        object_pairs_hook=_unique_fields,
        parse_constant=_invalid_constant,
        parse_float=_finite_decimal,
        parse_int=_bounded_integer,
    )



# These are structural contracts for the versioned *candidate-source* indices,
# not an evaluation of source authenticity, license, availability or outcomes.
_COMPANY_EVENT_COLUMNS = (
    "event_id", "company_id", "company_label", "product", "source_url",
    "source_title", "source_publisher", "source_type", "published_utc",
    "event_date_utc", "accessed_utc", "kind", "claim_summary", "feature",
    "availability", "status", "study_construct", "limitation", "confidence",
    "duplicate_event_group", "independent_check_url",
)
_COMPANY_ALLOWED_STATUSES = frozenset((
    "shipped", "preview", "announced_only", "reported_undetermined",
    "reversed/cancelled", "corrected", "unavailable/unknown",
))
_COMPANY_FILE = re.compile(r"^([0-9]{3})-[a-z0-9]+(?:-[a-z0-9]+)*\.events\.csv$")
_DATE_PART = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
_WINDOW_PART = re.compile(
    r"^([0-9]{4}-[0-9]{2}-[0-9]{2})_([0-9]{4}-[0-9]{2}-[0-9]{2})$"
)


def _event_date(value, field, row_number):
    if not _DATE_PART.fullmatch(value):
        raise IntegrityError(f"company event row {row_number}: {field} must be YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise IntegrityError(
            f"company event row {row_number}: {field} is not a calendar date"
        ) from exc


def _company_event_context(path, header):
    """Return (company ID, inclusive date bounds, column positions) or None.

    Apply only to a canonical NNN-name.events.csv beneath company-intelligence.
    Historical archives and arbitrary CSV fixtures retain the existing generic
    CSV syntax gate. Both 21-column and 22-column source indices are supported.
    """
    if "company-intelligence" not in path.parts or not path.name.endswith(".events.csv"):
        return None
    match = _COMPANY_FILE.fullmatch(path.name)
    if not match:
        raise IntegrityError("company event file must be NNN-slug.events.csv")
    windows = [_WINDOW_PART.fullmatch(part) for part in path.parts]
    windows = [window for window in windows if window is not None]
    if len(windows) != 1:
        raise IntegrityError("company event file requires one dated window directory")
    start = _event_date(windows[0].group(1), "window start", 1)
    end = _event_date(windows[0].group(2), "window end", 1)
    if start > end:
        raise IntegrityError("company event window ends before it begins")
    required = set(_COMPANY_EVENT_COLUMNS)
    actual = set(header)
    if not required.issubset(actual) or actual - required - {"evidence_tier"}:
        raise IntegrityError("company event CSV has missing or unsupported columns")
    return (match.group(1), start, end, {name: header.index(name) for name in required})


def _validate_company_event_row(row, context, record_no, seen_ids, last_date):
    company_id, start, end, columns = context
    value = lambda name: row[columns[name]]
    event_id = value("event_id")
    if not event_id or event_id != event_id.strip():
        raise IntegrityError(f"company event row {record_no}: missing/unclean event_id")
    if event_id in seen_ids:
        raise IntegrityError(f"company event row {record_no}: repeated event_id")
    seen_ids.add(event_id)
    if value("company_id") != company_id:
        raise IntegrityError(f"company event row {record_no}: company_id differs from filename")
    for column in ("company_label", "source_title", "source_publisher", "confidence"):
        if not value(column).strip():
            raise IntegrityError(f"company event row {record_no}: empty {column}")
    published = _event_date(value("published_utc"), "published_utc", record_no)
    if not start <= published <= end:
        raise IntegrityError(f"company event row {record_no}: publication outside study window")
    if last_date is not None and published < last_date:
        raise IntegrityError(f"company event row {record_no}: nonchronological publication dates")
    for optional_date in ("event_date_utc", "accessed_utc"):
        if value(optional_date):
            _event_date(value(optional_date), optional_date, record_no)
    if value("status") not in _COMPANY_ALLOWED_STATUSES:
        raise IntegrityError(f"company event row {record_no}: unrecognized source status")
    url = value("source_url")
    if not url or url != url.strip() or any(char.isspace() for char in url):
        raise IntegrityError(f"company event row {record_no}: malformed source_url")
    try:
        parsed = urlsplit(url)
        if (parsed.scheme != "https" or not parsed.hostname
                or parsed.username is not None or parsed.password is not None):
            raise IntegrityError(f"company event row {record_no}: source_url must be public HTTPS")
        # Accessing .port also rejects invalid/overflowing port syntax.
        parsed.port
    except ValueError as exc:
        raise IntegrityError(f"company event row {record_no}: malformed source_url") from exc
    # Multiple real changes may legitimately cite the same *dated changelog*
    # URL. Their event IDs and publication dates must remain distinct instead
    # of claiming distinct URLs or independent corroboration.
    return published

def validate_text(path, content):
    """Validate one UTF-8 document; return number of logical data records."""
    if "\x00" in content:
        raise IntegrityError("embedded NUL byte is not a valid research artifact")
    if path.suffix == ".json":
        obj = _strict_json(content)
        if not isinstance(obj, (dict, list)):
            raise IntegrityError("JSON top level must be an object or array")
        return 1
    if path.suffix == ".jsonl":
        records = 0
        for line_no, line in enumerate(content.splitlines(), 1):
            if not line.strip():
                raise IntegrityError(f"JSONL line {line_no} is blank")
            obj = _strict_json(line)
            if not isinstance(obj, dict):
                raise IntegrityError(f"JSONL line {line_no} must be an object")
            records += 1
        if records == 0:
            raise IntegrityError("JSONL contains no records")
        return records
    if path.suffix == ".csv":
        reader = csv.reader(io.StringIO(content, newline=""), strict=True)
        try:
            header = next(reader)
        except StopIteration as exc:
            raise IntegrityError("CSV has no header") from exc
        if not header or not all(column.strip() for column in header):
            raise IntegrityError("CSV header contains blank names")
        canonical = [column.strip().casefold() for column in header]
        if len(canonical) != len(set(canonical)):
            raise IntegrityError("CSV header has repeated names")
        context = _company_event_context(path, header)
        seen_event_ids = set()
        last_published = None
        count = 0
        for number, row in enumerate(reader, 2):
            if len(row) != len(header):
                raise IntegrityError(
                    f"CSV record {number} has {len(row)} cells, expected {len(header)}"
                )
            if context is not None:
                last_published = _validate_company_event_row(
                    row, context, number, seen_event_ids, last_published
                )
            count += 1
        if count == 0:
            raise IntegrityError("CSV contains no data records")
        return count
    raise IntegrityError(f"unsupported file suffix {path.suffix}")


def audit_repository(root, max_file_bytes=MAX_BYTES_PER_FILE, max_total_bytes=MAX_TOTAL_BYTES):
    """Return deterministic counts; reject symlinks/aliases and malformed data."""
    root = Path(root)
    if not root.is_dir():
        raise IntegrityError("repository root is not a directory")
    counts = {"json": 0, "jsonl": 0, "csv": 0, "logical_records": 0}
    failures = []
    examined = 0
    total_bytes = 0

    for dirname in DATA_DIRS:
        folder = root / dirname
        if not folder.exists() and dirname not in REQUIRED_DATA_DIRS:
            continue  # Optional research or templates directory absent in fixtures.
        if not folder.is_dir() or folder.is_symlink():
            failures.append(f"{dirname}: missing data directory or directory symlink")
            continue
        # Symlinks to non-data files are also rejected under these directories:
        # they could be used by a malicious PR to read CI runner content.
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                failures.append(f"{path.relative_to(root)}: symlink forbidden")
                continue
            if not path.is_file() or path.suffix not in SUFFIXES:
                continue
            examined += 1
            if examined > MAX_FILES:
                raise IntegrityError("research artifact count exceeds conservative safety limit")
            relative = str(path.relative_to(root))
            try:
                size = path.stat().st_size
                if size > max_file_bytes:
                    raise IntegrityError(f"file exceeds {max_file_bytes} byte limit")
                total_bytes += size
                if total_bytes > max_total_bytes:
                    raise IntegrityError(f"cumulative research artifacts exceed {max_total_bytes} bytes")
                content = path.read_text(encoding="utf-8")
                count = validate_text(path, content)
                counts[path.suffix.lstrip(".")] += 1
                counts["logical_records"] += count
            except (IntegrityError, csv.Error, UnicodeError, OSError, json.JSONDecodeError, RecursionError) as exc:
                failures.append(f"{relative}: {exc}")
    if examined == 0:
        failures.append("no research JSON/JSONL/CSV artifacts were found")
    if failures:
        raise IntegrityError(
            f"{len(failures)} research artifact problem(s):\n"
            + "\n".join(failures[:25])
            + ("\n[additional failures omitted]" if len(failures) > 25 else "")
        )
    return {"files": examined, "checked_bytes": total_bytes, **counts}


def main(argv=None):
    cli = argparse.ArgumentParser(description="Offline research artifact syntax and integrity gate")
    cli.add_argument("--root", type=Path, default=Path("."))
    args = cli.parse_args(argv)
    try:
        result = audit_repository(args.root)
    except IntegrityError as exc:
        cli.exit(2, f"artifact integrity gate failed: {exc}\n")
    print(json.dumps({
        "status": "syntax_checked_not_scientifically_validated",
        **result,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
