"""Fail-closed, offline syntax/integrity checks for tracked research JSON.

Reject ambiguous duplicate keys and non-finite numbers before they become
silently reinterpreted by downstream readers. Does not authenticate sources,
validate a study schema, or verify that observations actually occurred.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import io
import json
import math
from pathlib import Path
import sys

SOURCE_DIRS = ("examples", "references", "research", "research-notes", "templates")
EXTENSIONS = frozenset((".json", ".jsonl", ".csv"))
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_TOTAL_BYTES = 128 * 1024 * 1024
MAX_FILES = 5000
MAX_INTEGER_DIGITS = 1024


class ResearchJSONError(ValueError):
    """A JSON research artifact failed a deterministic validation gate."""


def _unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ResearchJSONError(f"duplicate JSON object key {key!r}")
        obj[key] = value
    return obj


def _finite_float(literal):
    """Reject numeric values that silently change to infinity or to zero."""
    try:
        exact = Decimal(literal)
        value = float(exact)
    except (ValueError, InvalidOperation, OverflowError) as exc:
        raise ResearchJSONError("unrepresentable JSON number") from exc
    if not math.isfinite(value) or (exact != 0 and value == 0.0):
        raise ResearchJSONError("non-finite, overflowing or underflowing JSON number")
    return value


def _bounded_integer(literal):
    if len(literal.lstrip("-")) > MAX_INTEGER_DIGITS:
        raise ResearchJSONError("JSON integer exceeds 1024 digit safety limit")
    return int(literal)


def _invalid_constant(literal):
    raise ResearchJSONError(f"nonstandard JSON numeric constant {literal}")


def _decode_document(raw, label):
    try:
        text = raw.decode("utf-8")
        return json.loads(
            text, object_pairs_hook=_unique_pairs,
            parse_constant=_invalid_constant, parse_float=_finite_float,
            parse_int=_bounded_integer,
        )
    except UnicodeDecodeError as exc:
        raise ResearchJSONError(f"{label}: invalid UTF-8") from exc
    except (json.JSONDecodeError, ResearchJSONError, ValueError) as exc:
        raise ResearchJSONError(f"{label}: {exc}") from exc


def _check_csv(raw, label):
    """Validate UTF-8 CSV header and every record without inferring data truth."""
    if b"\x00" in raw:
        raise ResearchJSONError(f"{label}: embedded NUL byte")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ResearchJSONError(f"{label}: invalid UTF-8") from exc
    try:
        reader = csv.reader(io.StringIO(text, newline=""), strict=True)
        header = next(reader, None)
        if not header or any(not col.strip() for col in header):
            raise ResearchJSONError(f"{label}: CSV requires nonempty header cells")
        normalized = [col.strip().casefold() for col in header]
        if len(normalized) != len(set(normalized)):
            raise ResearchJSONError(f"{label}: duplicate CSV header names")
        count = 0
        for row in reader:
            if len(row) != len(header):
                raise ResearchJSONError(
                    f"{label}: CSV record ending at line {reader.line_num} "
                    f"has {len(row)} cells, expected {len(header)}"
                )
            count += 1
    except csv.Error as exc:
        raise ResearchJSONError(f"{label}: malformed CSV: {exc}") from exc
    if not count:
        raise ResearchJSONError(f"{label}: CSV contains no data records")
    return count


def _check_file(path, root):
    label = str(path.relative_to(root))
    if path.is_symlink():
        raise ResearchJSONError(f"{label}: symlinks cannot be validated as immutable evidence")
    if not path.is_file():
        raise ResearchJSONError(f"{label}: expected a regular file")
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ResearchJSONError(
            f"{label}: exceeds {MAX_FILE_BYTES} byte inspection limit; "
            "split it into independently named artifacts"
        )
    raw = path.read_bytes()
    if path.suffix == ".csv":
        return _check_csv(raw, label)
    if path.suffix == ".json":
        _decode_document(raw, label)
        return 1
    # Keep the line number in diagnostics; blank lines are permitted only
    # between real JSONL records, never in place of all evidence.
    lines = raw.splitlines()
    count = 0
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        _decode_document(line, f"{label}:line {number}")
        count += 1
    if not count:
        raise ResearchJSONError(f"{label}: empty JSONL file has no records")
    return count


def validate_repository(root):
    """Return reproducible counts or raise without modifying input files."""
    root = Path(root)
    if not root.is_dir():
        raise ResearchJSONError(f"repository root is not a directory: {root}")
    root = root.resolve()
    files = []
    for dirname in SOURCE_DIRS:
        folder = root / dirname
        if folder.is_symlink():
            raise ResearchJSONError(f"{dirname}: source directory cannot be a symlink")
        if not folder.exists():
            continue
        if not folder.is_dir():
            raise ResearchJSONError(f"{dirname}: source directory must be a directory")
        for candidate in folder.rglob("*"):
            if candidate.suffix in EXTENSIONS:
                files.append(candidate)
    if not files:
        raise ResearchJSONError("no .json/.jsonl/.csv research artifacts found")
    if len(files) > MAX_FILES:
        raise ResearchJSONError("research artifact file count exceeds safety limit")
    json_records = csv_rows = total_bytes = 0
    for path in sorted(files):
        total_bytes += path.stat().st_size
        if total_bytes > MAX_TOTAL_BYTES:
            raise ResearchJSONError("cumulative research artifact bytes exceed safety limit")
        count = _check_file(path, root)
        if path.suffix == ".csv":
            csv_rows += count
        else:
            json_records += count
    return {
        "validated_files": len(files),
        "json_documents_or_jsonl_records": json_records,
        "csv_data_rows": csv_rows,
        "total_research_records": json_records + csv_rows,
        "checked_bytes": total_bytes,
        "source_directories": list(SOURCE_DIRS),
        "modifies_artifacts": False,
        "authenticated_research_evidence": False,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."),
                        help="Git checkout root (default: current directory)")
    args = parser.parse_args(argv)
    try:
        result = validate_repository(args.root)
    except (ResearchJSONError, OSError) as exc:
        parser.exit(2, f"research JSON integrity gate failed: {exc}\n")
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
