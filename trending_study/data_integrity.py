"""Fail-closed, offline syntax/integrity checks for tracked research JSON.

Reject ambiguous duplicate keys and non-finite numbers before they become
silently reinterpreted by downstream readers. Does not authenticate sources,
validate a study schema, or verify that observations actually occurred.
"""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import math
import os
import stat
from pathlib import Path
import sys

SOURCE_DIRS = ("examples", "references", "research", "research-notes", "templates")
EXTENSIONS = frozenset((".json", ".jsonl", ".csv"))
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_TOTAL_BYTES = 128 * 1024 * 1024
MAX_FILES = 5000


class ResearchJSONError(ValueError):
    """A JSON research artifact failed a deterministic validation gate."""


def _unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ResearchJSONError("duplicate JSON object key")
        obj[key] = value
    return obj


def _finite_float(literal):
    # A tiny nonzero value must not silently become float zero. Preserve a
    # strict, finite downstream float contract while checking its exact
    # decimal lexical value first (no conversion to Decimal in outputs).
    try:
        exact = Decimal(literal)
        approximate = float(exact)
    except (InvalidOperation, OverflowError, ValueError) as exc:
        raise ResearchJSONError("invalid JSON numeric literal") from exc
    if not math.isfinite(approximate):
        raise ResearchJSONError("non-finite or overflowing JSON number")
    if exact != 0 and approximate == 0:
        raise ResearchJSONError("underflowing nonzero JSON number")
    return approximate


def _bounded_int(literal):
    # Avoid interpreter-dependent 3.10/3.12 digit limits and memory spikes
    # from an enormous integer in a nominally valid research ledger.
    if len(literal.lstrip("-")) > 1024:
        raise ResearchJSONError("JSON integer exceeds 1024 decimal digits")
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

def decode_research_json(raw, label):
    """Strictly decode an offline JSON document (duplicates/non-finite rejected).

    This public helper is shared by schema validators so a direct CLI run has
    the same parse integrity guarantees as the repository-wide artifact gate.
    """
    return _decode_document(raw, label)



def read_research_input_bytes(path, max_bytes=MAX_FILE_BYTES):
    """Read the bytes of one bounded offline input (JSON, CSV, ...).

    Rejects nonregular files (including FIFOs), refuses leaf symlinks where
    supported, checks the *opened* descriptor and actual bytes read. It is
    not a hostile ancestor-directory sandbox or source-authenticity proof.
    CLI diagnostics must never include user-supplied keys or paths.
    """
    if type(max_bytes) is not int or not 0 < max_bytes <= MAX_FILE_BYTES:
        raise ResearchJSONError("invalid bounded JSON input byte limit")
    path = Path(path)
    if path.is_symlink():
        raise ResearchJSONError("input must be a regular non-symlink file")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    flags |= getattr(os, "O_NONBLOCK", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise ResearchJSONError("input must be a readable regular non-symlink file") from exc
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise ResearchJSONError("input must be a regular non-symlink file")
        if metadata.st_size > max_bytes:
            raise ResearchJSONError("input exceeds configured JSON byte limit")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = None
            raw = stream.read(max_bytes + 1)
        if len(raw) > max_bytes:
            raise ResearchJSONError("input exceeds configured JSON byte limit")
    except OSError as exc:
        raise ResearchJSONError("cannot safely read input file") from exc
    finally:
        if descriptor is not None:
            os.close(descriptor)
    return raw


def load_research_json_file(path, max_bytes=MAX_FILE_BYTES, *, with_sha256=False):
    """Read one bounded offline JSON input and decode with canonical strict rules.

    Uses :func:`read_research_input_bytes`. With ``with_sha256=True`` returns
    ``(value, sha256_hex)`` of the exact bytes that were decoded, so callers
    can record raw-input provenance without a second (racy) read.
    """
    raw = read_research_input_bytes(path, max_bytes)
    try:
        value = decode_research_json(raw, "input")
    except (ResearchJSONError, RecursionError, OverflowError) as exc:
        # Full decoder diagnostics can contain sensitive duplicate-key text.
        raise ResearchJSONError("invalid or ambiguous JSON input") from exc
    return (value, hashlib.sha256(raw).hexdigest()) if with_sha256 else value

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
    if path.suffix == ".json":
        _decode_document(raw, label)
        return 1
    if path.suffix == ".csv":
        # Standard CSV parsing preserves quoted multiline values and commas.
        # Inspect headers/row widths only; never execute spreadsheet formulas.
        try:
            decoded = raw.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise ResearchJSONError(f"{label}: invalid UTF-8") from exc
        if "\x00" in decoded:
            raise ResearchJSONError(f"{label}: embedded NUL byte")
        try:
            reader = csv.reader(io.StringIO(decoded, newline=""), strict=True)
            try:
                header = next(reader)
            except StopIteration as exc:
                raise ResearchJSONError(f"{label}: CSV has no header") from exc
            if not header or any(not field.strip() for field in header):
                raise ResearchJSONError(f"{label}: CSV header contains blank names")
            canonical = [field.strip().casefold() for field in header]
            if len(set(canonical)) != len(canonical):
                raise ResearchJSONError(f"{label}: duplicate CSV header names")
            rows = 0
            for row in reader:
                if len(row) != len(header):
                    raise ResearchJSONError(
                        f"{label}: CSV record {rows+2} has {len(row)} cells; "
                        f"expected {len(header)}"
                    )
                rows += 1
            if rows == 0:
                raise ResearchJSONError(f"{label}: CSV contains no data records")
            return rows
        except csv.Error as exc:
            raise ResearchJSONError(f"{label}: invalid CSV ({exc})") from exc
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
            # A nested source-directory symlink is an uninspected evidence
            # subtree. Reject it before suffix filtering, rather than silently
            # returning an incomplete completeness/denominator claim.
            if candidate.is_symlink():
                raise ResearchJSONError(
                    f"{candidate.relative_to(root)}: symlinked research content; symlinks are not allowed"
                )
            if candidate.suffix in EXTENSIONS:
                if len(files) >= MAX_FILES:
                    raise ResearchJSONError("research artifact file count exceeds safety limit")
                files.append(candidate)
    if not files:
        raise ResearchJSONError("no .json/.jsonl/.csv research artifacts found")
    records = 0
    csv_files = csv_records = total_bytes = 0
    for path in sorted(files):
        total_bytes += path.stat().st_size
        if total_bytes > MAX_TOTAL_BYTES:
            raise ResearchJSONError("cumulative research artifact bytes exceed safety limit")
        count = _check_file(path, root)
        if path.suffix == ".csv":
            csv_files += 1
            csv_records += count
        else:
            records += count
    return {
        "validated_files": len(files),
        "json_documents_or_jsonl_records": records,
        "validated_csv_files": csv_files,
        "csv_data_rows": csv_records,
        "total_research_records": records + csv_records,
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
