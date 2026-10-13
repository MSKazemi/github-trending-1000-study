"""Validate tracked Python and JSON artifacts before a pull request can pass CI.

This is a standard-library-only *syntax and artifact-integrity* gate, not a
security scanner, schema validator, source authenticity test or human review.
No project Python module is imported and no JSON payload is executed.
"""
from __future__ import annotations

import argparse
import ast
import json
import math
from pathlib import Path
import subprocess
import sys
from typing import Iterable

SUFFIXES = frozenset({".py", ".json", ".jsonl"})
MAX_ARTIFACT_BYTES = 8 * 1024 * 1024


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """Reject duplicate keys at every nesting level (JSON default: last wins)."""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("non-finite JSON number")
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON number: {value}")


def inspect(root: Path, relative_path: str) -> str | None:
    """Return a diagnostic, or None for a syntactically valid tracked artifact.

    Paths are relative to an existing repository root and may only be Python or
    JSON files. Resolve symlinks to ensure CI cannot read outside the checkout.
    """
    rel = Path(relative_path)
    if rel.is_absolute() or ".." in rel.parts or not rel.parts:
        return f"{relative_path}: unsafe path"
    if rel.suffix not in SUFFIXES:
        return None
    target = root / rel
    try:
        if not target.resolve().is_relative_to(root.resolve()):
            return f"{relative_path}: symlink escapes repository root"
        if not target.is_file():
            return f"{relative_path}: missing or non-file artifact"
        if target.stat().st_size > MAX_ARTIFACT_BYTES:
            return f"{relative_path}: artifact exceeds {MAX_ARTIFACT_BYTES} bytes"
        source = target.read_bytes().decode("utf-8")
        if rel.suffix == ".py":
            # Syntax only: compile/import/execution of untrusted PR code is not
            # required to validate a newly added but otherwise unimported file.
            ast.parse(source, filename=relative_path)
        else:
            def check_json(document: str) -> None:
                json.loads(
                    document, object_pairs_hook=_unique_object,
                    parse_constant=_reject_constant, parse_float=_finite_float,
                )

            if rel.suffix == ".json":
                check_json(source)
            else:
                records = 0
                for line_number, line in enumerate(source.splitlines(), 1):
                    if not line.strip():
                        continue
                    try:
                        check_json(line)
                    except ValueError as exc:
                        raise ValueError(f"JSONL line {line_number}: {exc}") from exc
                    records += 1
                if records == 0:
                    raise ValueError("JSONL file contains no records")
    except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
        return f"{relative_path}: {type(exc).__name__}: {exc}"
    return None


def audit(root: Path, paths: Iterable[str]) -> dict[str, object]:
    """Check all supplied paths once; preserve explicit diagnostics."""
    checked = {"python": 0, "json": 0, "jsonl": 0}
    errors: list[str] = []
    seen: set[str] = set()
    for path in paths:
        if path in seen:
            errors.append(f"{path}: duplicate tracked file path")
            continue
        seen.add(path)
        suffix = Path(path).suffix
        if suffix not in SUFFIXES:
            continue
        checked[{".py": "python", ".json": "json", ".jsonl": "jsonl"}[suffix]] += 1
        diagnostic = inspect(root, path)
        if diagnostic is not None:
            errors.append(diagnostic)
    return {"checked": checked, "errors": errors, "ok": not errors}


def tracked_files(root: Path) -> list[str]:
    """Ask Git for committed artifacts, not generated/untracked build outputs."""
    process = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--", "*.py", "*.json", "*.jsonl"],
        capture_output=True,
        check=True,
        timeout=30,
    )
    return [
        item.decode("utf-8")
        for item in process.stdout.split(b"\0")
        if item
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to checked-out Git repository (defaults to this project)",
    )
    args = parser.parse_args(argv)
    try:
        report = audit(args.root, tracked_files(args.root))
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired,
            UnicodeError) as exc:
        print(f"artifact-integrity: cannot obtain tracked file list: {exc}",
              file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
