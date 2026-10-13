"""Validate committed research JSON/JSONL/CSV inputs without network dependencies.

This guards file *syntax and information preservation* (not scientific truth,
third-party licensing, evidence provenance, or participant consent). In
particular, duplicate JSON keys must not silently replace earlier values.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import io
import json
import math
from pathlib import Path
import sys


DATA_DIRS = ("examples", "references", "research-notes", "research", "templates")
REQUIRED_DATA_DIRS = frozenset(("examples", "references", "research-notes"))
SUFFIXES = {".json", ".jsonl", ".csv"}
MAX_BYTES_PER_FILE = 16 * 1024 * 1024
MAX_FILES = 5000


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


def _strict_json(text):
    return json.loads(
        text,
        object_pairs_hook=_unique_fields,
        parse_constant=_invalid_constant,
        parse_float=_finite_decimal,
        parse_int=_bounded_integer,
    )


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
        count = 0
        for number, row in enumerate(reader, 2):
            if len(row) != len(header):
                raise IntegrityError(
                    f"CSV record {number} has {len(row)} cells, expected {len(header)}"
                )
            count += 1
        return count
    raise IntegrityError(f"unsupported file suffix {path.suffix}")


def audit_repository(root, max_file_bytes=MAX_BYTES_PER_FILE):
    """Return deterministic counts; reject symlinks/aliases and malformed data."""
    root = Path(root)
    if not root.is_dir():
        raise IntegrityError("repository root is not a directory")
    counts = {"json": 0, "jsonl": 0, "csv": 0, "logical_records": 0}
    failures = []
    examined = 0

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
                if path.stat().st_size > max_file_bytes:
                    raise IntegrityError(f"file exceeds {max_file_bytes} byte limit")
                content = path.read_text(encoding="utf-8")
                count = validate_text(path, content)
                counts[path.suffix.lstrip(".")] += 1
                counts["logical_records"] += count
            except (IntegrityError, csv.Error, UnicodeError, OSError, json.JSONDecodeError) as exc:
                failures.append(f"{relative}: {exc}")
    if examined == 0:
        failures.append("no research JSON/JSONL/CSV artifacts were found")
    if failures:
        raise IntegrityError(
            f"{len(failures)} research artifact problem(s):\n"
            + "\n".join(failures[:25])
            + ("\n[additional failures omitted]" if len(failures) > 25 else "")
        )
    return {"files": examined, **counts}


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
