"""Fail-closed, offline syntax/integrity checks for tracked research JSON/JSONL/CSV.

Reject ambiguous duplicate keys and non-finite numbers before they become
silently reinterpreted by downstream readers. Does not authenticate sources,
validate a study schema, or verify that observations actually occurred.
"""
import argparse
import csv
import io
import json
import math
from pathlib import Path
import sys

SOURCE_DIRS = ("examples", "references", "research", "research-notes", "templates")
EXTENSIONS = frozenset((".json", ".jsonl", ".csv"))
MAX_FILE_BYTES = 16 * 1024 * 1024


class ResearchJSONError(ValueError):
    """An evidence artifact failed deterministic validation (legacy public name)."""


def _unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ResearchJSONError(f"duplicate JSON object key {key!r}")
        obj[key] = value
    return obj


def _finite_float(literal):
    value = float(literal)
    if not math.isfinite(value):
        raise ResearchJSONError("non-finite or overflowing JSON number")
    return value


def _invalid_constant(literal):
    raise ResearchJSONError(f"nonstandard JSON numeric constant {literal}")


def _decode_document(raw, label):
    try:
        text = raw.decode("utf-8")
        return json.loads(
            text, object_pairs_hook=_unique_pairs,
            parse_constant=_invalid_constant, parse_float=_finite_float,
        )
    except UnicodeDecodeError as exc:
        raise ResearchJSONError(f"{label}: invalid UTF-8") from exc
    except (json.JSONDecodeError, ResearchJSONError, ValueError) as exc:
        raise ResearchJSONError(f"{label}: {exc}") from exc


def _check_csv(raw, label):
    """Validate UTF-8 CSV records, including multiline quoted fields.

    CSV has no native schema or evidence-authenticity guarantee. Blank cells
    remain legitimate unknowns; inconsistent row widths and duplicate
    normalized header names are structural ambiguities and fail closed.
    """
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ResearchJSONError(f"{label}: invalid UTF-8") from exc
    if "\x00" in text:
        raise ResearchJSONError(f"{label}: embedded NUL in CSV artifact")
    try:
        reader = csv.reader(io.StringIO(text, newline=""), strict=True)
        header = next(reader, None)
        if not header or any(not col.strip() for col in header):
            raise ResearchJSONError(f"{label}: missing or blank CSV header")
        canon = [col.strip().casefold() for col in header]
        if len(canon) != len(set(canon)):
            raise ResearchJSONError(f"{label}: repeated CSV header names")
        records = 0
        for row in reader:
            if len(row) != len(header):
                raise ResearchJSONError(
                    f"{label}: CSV record {records + 2} contains {len(row)} columns, "
                    f"expected {len(header)}"
                )
            records += 1
    except csv.Error as exc:
        raise ResearchJSONError(f"{label}: malformed CSV ({exc})") from exc
    return records


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
        raise ResearchJSONError("no JSON/JSONL/CSV research artifacts found")
    json_records = 0
    csv_records = 0
    for path in sorted(files):
        count = _check_file(path, root)
        if path.suffix == ".csv":
            csv_records += count
        else:
            json_records += count
    return {
        "validated_files": len(files),
        "json_documents_or_jsonl_records": json_records,
        "csv_data_records": csv_records,
        "total_logical_records": json_records + csv_records,
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
