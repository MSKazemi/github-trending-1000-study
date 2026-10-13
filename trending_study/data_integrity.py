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

SOURCE_DIRS = ("examples", "references", "research", "research-notes", "templates")
EXTENSIONS = frozenset((".json", ".jsonl", ".csv"))
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_FILES = 5000


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
    """Never silently round a very small nonzero measurement to zero."""
    try:
        exact = Decimal(literal)
        approximated = float(exact)
    except (InvalidOperation, OverflowError, ValueError) as exc:
        raise ResearchJSONError("unrepresentable JSON decimal literal") from exc
    if not math.isfinite(approximated) or (exact != 0 and approximated == 0):
        raise ResearchJSONError("non-finite, overflowing or underflowing JSON number")
    return exact


def _bounded_int(literal):
    if len(literal.lstrip("-")) > 1024:
        raise ResearchJSONError("JSON integer exceeds conservative 1024-digit limit")
    return int(literal)


def _invalid_constant(literal):
    raise ResearchJSONError(f"nonstandard JSON numeric constant {literal}")


def _decode_document(raw, label):
    try:
        text = raw.decode("utf-8")
        return json.loads(
            text, object_pairs_hook=_unique_pairs,
            parse_constant=_invalid_constant, parse_float=_finite_float,
            parse_int=_bounded_int,
        )
    except UnicodeDecodeError as exc:
        raise ResearchJSONError(f"{label}: invalid UTF-8") from exc
    except (json.JSONDecodeError, ResearchJSONError, ValueError) as exc:
        raise ResearchJSONError(f"{label}: {exc}") from exc


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
    if b"\x00" in raw:
        raise ResearchJSONError(f"{label}: embedded NUL byte")
    if path.suffix == ".csv":
        try:
            contents = raw.decode("utf-8")
            reader = csv.reader(io.StringIO(contents, newline=""), strict=True)
            header = next(reader, None)
            if header is None or not header or not all(col.strip() for col in header):
                raise ResearchJSONError(f"{label}: CSV header missing or contains blank field")
            canonical = [col.strip().casefold() for col in header]
            if len(canonical) != len(set(canonical)):
                raise ResearchJSONError(f"{label}: duplicate CSV column names")
            count = 0
            for record_number, row in enumerate(reader, 2):
                if len(row) != len(header):
                    raise ResearchJSONError(
                        f"{label}: CSV record {record_number}: "
                        f"{len(row)} cells, expected {len(header)}"
                    )
                count += 1
            return count
        except (UnicodeDecodeError, csv.Error) as exc:
            raise ResearchJSONError(f"{label}: invalid UTF-8 or CSV quoting: {exc}") from exc
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
            if candidate.is_symlink():
                raise ResearchJSONError(
                    f"{candidate.relative_to(root)}: symlinked research entry is not trusted"
                )
            if candidate.suffix in EXTENSIONS:
                files.append(candidate)
    if not files:
        raise ResearchJSONError("no .json/.jsonl/.csv research artifacts found")
    if len(files) > MAX_FILES:
        raise ResearchJSONError("too many research artifacts for bounded audit")
    records = 0
    for path in sorted(files):
        records += _check_file(path, root)
    return {
        "validated_files": len(files),
        "json_documents_jsonl_records_or_csv_rows": records,
        "json_documents_or_jsonl_records": records,  # retained for backwards compatibility
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
