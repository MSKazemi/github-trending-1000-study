"""Validate committed research JSON/JSONL/CSV inputs without network dependencies.

This guards file *syntax and information preservation* (not scientific truth,
third-party licensing, evidence provenance, or participant consent). In
particular, duplicate JSON keys must not silently replace earlier values.
"""
import argparse
import os
import stat
import subprocess
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
MAX_TOTAL_BYTES = 128 * 1024 * 1024
MAX_FILES = 5000
MAX_JSON_DEPTH = 128


class IntegrityError(ValueError):
    """A checked research artifact would lose information or cannot be read."""


def _unique_fields(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            # JSON keys are caller-controlled and may contain secrets or PII.
            # Show only a stable error class in CI diagnostics.
            raise IntegrityError("duplicate JSON object key")
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



def _read_git_index_blob(root, oid, max_file_bytes):
    """Read a bounded Git-index blob without running clean/smudge filters.

    A locally staged blob may differ from the checked-out file. A checkout-only
    scan must not report success while an invalid blob is staged for commit.
    """
    if len(oid) not in (40, 64) or any(b not in b"0123456789abcdef" for b in oid):
        raise IntegrityError("invalid Git index blob identifier")
    try:
        header = subprocess.run(
            ["git", "-C", str(root), "cat-file",
             "--batch-check=%(objecttype) %(objectsize)"],
            input=oid + b"\n", check=True, capture_output=True, timeout=20,
        ).stdout.strip().split()
        if len(header) != 2 or header[0] != b"blob" or not header[1].isdigit():
            raise IntegrityError("Git index entry is missing or not a blob")
        size = int(header[1])
        if size > max_file_bytes:
            raise IntegrityError(f"Git index blob exceeds {max_file_bytes} byte limit")
        payload = subprocess.run(
            ["git", "-C", str(root), "cat-file", "blob", oid.decode("ascii")],
            check=True, capture_output=True, timeout=20,
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise IntegrityError("cannot read Git index blob") from exc
    if len(payload) != size:
        raise IntegrityError("Git index blob size changed during inspection")
    return payload



def _open_tracked_file(root, parts, flags):
    """Open indexed path without following ancestor symlinks on POSIX.

    Resolving each directory relative to an already-open directory descriptor
    closes the check-then-open ancestor swap window. Platforms without
    O_NOFOLLOW/O_DIRECTORY/dir_fd use the existing best-effort path checks.
    This is not a comprehensive hostile-filesystem sandbox.
    """
    if (hasattr(os, "O_NOFOLLOW") and hasattr(os, "O_DIRECTORY")
            and os.open in os.supports_dir_fd):
        directory_flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_DIRECTORY
        parent_fd = os.open(root, directory_flags)
        try:
            for part in parts[:-1]:
                next_fd = os.open(part, directory_flags, dir_fd=parent_fd)
                os.close(parent_fd)
                parent_fd = next_fd
            return os.open(parts[-1], flags, dir_fd=parent_fd)
        finally:
            os.close(parent_fd)
    return os.open(root.joinpath(*parts), flags)


def audit_tracked_code_json(
    root, max_file_bytes=MAX_BYTES_PER_FILE, max_total_bytes=MAX_TOTAL_BYTES
):
    """Validate every Git-indexed .py/.json file in a checkout, without imports.

    Unlike the research-directory scan, Git index enumeration reaches files in
    any directory, including hidden paths. It checks checked-out and Git-index blob bytes; it does
    not authenticate sources or inspect Git submodule internals.
    """
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise IntegrityError("tracked-file root must be a real directory")
    root = root.resolve()
    try:
        origin = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            check=True, capture_output=True, timeout=20,
        ).stdout.decode("utf-8").rstrip("\n")
        if Path(origin).resolve() != root:
            raise IntegrityError("tracked-file root must be the Git top-level directory")
        listing = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--stage", "--cached",
             "--full-name", "-z"],
            check=True, capture_output=True, timeout=20,
        ).stdout
    except (OSError, UnicodeError, subprocess.SubprocessError) as exc:
        raise IntegrityError("cannot inspect local Git index") from exc

    if len(listing) > 8 * 1024 * 1024:
        raise IntegrityError("Git index listing exceeds 8 MiB inspection limit")
    if not listing:
        raise IntegrityError("no Git-tracked Python/JSON files were found")
    if not listing.endswith(b"\0"):
        raise IntegrityError("Git index listing is incomplete")

    counts = {"python": 0, "json": 0, "files": 0, "checked_bytes": 0,
              "index_checked_bytes": 0}
    failures = []
    seen = set()

    for entry in listing[:-1].split(b"\0"):
        metadata, separator, filename = entry.partition(b"\t")
        fields = metadata.split()
        if not separator or len(fields) != 3:
            raise IntegrityError("malformed Git index entry")
        try:
            relative = filename.decode("utf-8")
        except UnicodeError as exc:
            raise IntegrityError("Git index has a non-UTF-8 filename") from exc
        suffix = Path(relative).suffix.lower()
        if suffix not in (".py", ".json"):
            continue
        counts["files"] += 1
        if counts["files"] > MAX_FILES:
            raise IntegrityError("tracked Python/JSON count exceeds inspection limit")

        label = repr(relative)  # Escape newlines/control chars in CI diagnostics.
        if relative in seen:
            failures.append(f"{label}: duplicate Git index path")
            continue
        seen.add(relative)
        parts = relative.split("/")
        if relative.startswith("/") or any(part in ("", ".", "..") for part in parts):
            failures.append(f"{label}: unsafe Git index path")
            continue
        mode, _sha, stage = fields
        if stage != b"0" or mode not in (b"100644", b"100755"):
            failures.append(f"{label}: nonregular or unmerged Git index entry")
            continue

        try:
            parent = root
            for part in parts[:-1]:
                parent /= part
                if parent.is_symlink():
                    raise IntegrityError("symlinked parent directory")
            path = root.joinpath(*parts)
            if path.is_symlink():
                raise IntegrityError("tracked file is a symlink")
            # Open the checked path once and inspect the *opened descriptor*.
            # O_NONBLOCK avoids hanging on a swapped-in FIFO; O_NOFOLLOW
            # rejects a swapped-in leaf symlink where the OS supports it.
            flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0)
            flags |= getattr(os, "O_NOFOLLOW", 0)
            with os.fdopen(_open_tracked_file(root, parts, flags), "rb") as handle:
                file_stat = os.fstat(handle.fileno())
                if not stat.S_ISREG(file_stat.st_mode):
                    raise IntegrityError("tracked path is missing or not a regular file")
                if file_stat.st_size > max_file_bytes:
                    raise IntegrityError(f"file exceeds {max_file_bytes} byte limit")
                if counts["checked_bytes"] + file_stat.st_size > max_total_bytes:
                    raise IntegrityError(
                        f"tracked artifact total exceeds {max_total_bytes} byte limit"
                    )
                # A size precheck alone is not a memory limit if the file
                # grows between fstat and read. Bound the actual read too.
                raw = handle.read(max_file_bytes + 1)
            if len(raw) > max_file_bytes:
                raise IntegrityError(f"file exceeds {max_file_bytes} byte limit")
            if len(raw) != file_stat.st_size:
                raise IntegrityError("file changed size during inspection")
            if counts["checked_bytes"] + len(raw) > max_total_bytes:
                raise IntegrityError(
                    f"tracked artifact total exceeds {max_total_bytes} byte limit"
                )
            counts["checked_bytes"] += len(raw)
            indexed = _read_git_index_blob(root, _sha, max_file_bytes)
            if counts["index_checked_bytes"] + len(indexed) > max_total_bytes:
                raise IntegrityError(
                    f"Git index blobs exceed {max_total_bytes} byte total limit"
                )
            counts["index_checked_bytes"] += len(indexed)
            if suffix == ".json":
                _strict_json(raw.decode("utf-8"))
                if indexed != raw:
                    try:
                        _strict_json(indexed.decode("utf-8"))
                    except (IntegrityError, UnicodeError, ValueError,
                            RecursionError) as exc:
                        raise IntegrityError(f"Git index blob: {exc}") from exc
                counts["json"] += 1
            else:
                # Compiling creates a code object but does not execute it;
                # unlike AST-only parsing this checks contextual syntax too,
                # e.g. 'return' outside a function. Respect PEP 263 cookies.
                compile(raw, relative, "exec", dont_inherit=True)
                if indexed != raw:
                    try:
                        compile(indexed, relative, "exec", dont_inherit=True)
                    except (SyntaxError, UnicodeError, ValueError,
                            OverflowError, RecursionError) as exc:
                        raise IntegrityError(f"Git index blob: {exc}") from exc
                counts["python"] += 1
        except (IntegrityError, OSError, UnicodeError, SyntaxError,
                ValueError, OverflowError, RecursionError) as exc:
            failures.append(f"{label}: {exc}")

    if counts["files"] == 0:
        failures.append("no Git-tracked Python/JSON files were found")
    if failures:
        raise IntegrityError(
            f"{len(failures)} tracked Python/JSON problem(s):\n"
            + "\n".join(failures[:25])
            + ("\n[additional failures omitted]" if len(failures) > 25 else "")
        )
    return counts


def main(argv=None):
    cli = argparse.ArgumentParser(description="Offline research artifact syntax and integrity gate")
    cli.add_argument("--root", type=Path, default=Path("."))
    cli.add_argument(
        "--tracked-code-json", action="store_true",
        help="also validate every Git-tracked Python and JSON file, in any directory",
    )
    args = cli.parse_args(argv)
    try:
        result = audit_repository(args.root)
        if args.tracked_code_json:
            result["tracked_code_json"] = audit_tracked_code_json(args.root)
    except IntegrityError as exc:
        cli.exit(2, f"artifact integrity gate failed: {exc}\n")
    print(json.dumps({
        "status": "syntax_checked_not_scientifically_validated",
        **result,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
