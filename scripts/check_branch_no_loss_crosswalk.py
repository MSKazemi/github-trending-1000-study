#!/usr/bin/env python3
"""Validate a frozen read-only #279 branch provenance snapshot, never mutate Git."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

SHA = re.compile(r"[0-9a-f]{40}\Z")
REF = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}\Z")
PARTS = Path("ops/branch-retirement/review-only-2026-10-17")
MAIN = "62254996c69fc8c359650b801b6e4935048c4f21"
ROW_FIELDS = {"branch", "sha", "protected", "open_prs", "compare",
              "changed_files", "disposition", "deletion_authorized"}
FILE_FIELDS = {"path", "change_kind", "previous_path", "branch_blob_sha",
               "main_blob_sha", "same_path_blob", "alternate_main_paths"}
DECISIONS = {"hold-open-pr", "hold-ancestor-await-protected-recovery",
             "hold-diverged-file-and-source-review"}


def reject_duplicate_keys(pairs):
    out = {}
    for name, value in pairs:
        if name in out:
            raise ValueError("Duplicate JSON key: " + name)
        out[name] = value
    return out


def checked_sha(value, allow_null=False):
    if value is None and allow_null:
        return
    if not isinstance(value, str) or SHA.fullmatch(value) is None:
        raise ValueError("Missing or invalid full Git SHA")


def checked_path(value):
    if (not isinstance(value, str) or not value or value.startswith("/")
            or "\\" in value or "\0" in value or
            any(part in ("", ".", "..") for part in value.split("/"))):
        raise ValueError("Unsafe or ambiguous file path")


def checked_ref(value):
    if (not isinstance(value, str) or REF.fullmatch(value) is None or
            value.startswith("refs/") or value.endswith((".", "/")) or
            ".." in value or any(x in ("", ".", "..") for x in value.split("/"))):
        raise ValueError("Unsafe Git branch name")


def validate_batches(batches, expected_main=MAIN, expected_refs=52,
                     expected_parts=8):
    """Prove snapshot structural consistency, NOT real-world branch or source status."""
    checked_sha(expected_main)
    if not isinstance(batches, list) or len(batches) != expected_parts:
        raise ValueError("Missing or additional snapshot part")
    names, pr_numbers = set(), set()
    stats = Counter()
    for index, batch in enumerate(batches):
        if not isinstance(batch, dict) or set(batch) != {
                "batch_index", "base_commit_sha", "records"}:
            raise ValueError("Unexpected snapshot batch schema")
        if type(batch["batch_index"]) is not int or batch["batch_index"] != index:
            raise ValueError("Nonconsecutive batch index")
        if batch["base_commit_sha"] != expected_main:
            raise ValueError("Mixed or unexpected snapshot base SHA")
        records = batch["records"]
        if not isinstance(records, list) or not records:
            raise ValueError("Empty or malformed snapshot records")
        if index < expected_parts - 1 and len(records) != 7:
            raise ValueError("Nonfinal snapshot part must contain 7 records")
        for row in records:
            if not isinstance(row, dict) or set(row) != ROW_FIELDS:
                raise ValueError("Unexpected branch record schema")
            name = row["branch"]
            checked_ref(name)
            checked_sha(row["sha"])
            if name == "main" or name in names:
                raise ValueError("Main or duplicate branch inside non-main snapshot")
            names.add(name)
            if type(row["protected"]) is not bool:
                raise ValueError("Unknown ref protection state")
            if row["deletion_authorized"] is not False:
                raise ValueError("Review-only data cannot authorize deletion")
            comp = row["compare"]
            if not isinstance(comp, dict) or set(comp) != {
                    "status", "ahead_by", "behind_by", "changed_files"}:
                raise ValueError("Malformed compare record")
            ahead, behind = comp["ahead_by"], comp["behind_by"]
            if any(type(n) is not int or n < 0 for n in (
                    ahead, behind, comp["changed_files"])):
                raise ValueError("Invalid compare count")
            expected_status = ("identical" if not ahead and not behind else
                               "ahead" if ahead and not behind else
                               "behind" if behind and not ahead else "diverged")
            if comp["status"] != expected_status:
                raise ValueError("Inconsistent ahead/behind compare status")
            prs = row["open_prs"]
            if not isinstance(prs, list):
                raise ValueError("Malformed open-PR list")
            for pr in prs:
                if not isinstance(pr, dict) or set(pr) != {
                        "pr", "draft", "head_sha"}:
                    raise ValueError("Malformed open-PR identity")
                number = pr["pr"]
                if type(number) is not int or number <= 0 or number in pr_numbers:
                    raise ValueError("Invalid or duplicate PR number")
                pr_numbers.add(number)
                if type(pr["draft"]) is not bool:
                    raise ValueError("Unknown draft status")
                checked_sha(pr["head_sha"])
                if pr["head_sha"] != row["sha"]:
                    raise ValueError("PR head not at frozen branch tip")
            decision = ("hold-open-pr" if prs else
                        "hold-ancestor-await-protected-recovery" if ahead == 0 else
                        "hold-diverged-file-and-source-review")
            if row["disposition"] != decision or decision not in DECISIONS:
                raise ValueError("Branch classification is unsafe")
            files = row["changed_files"]
            if not isinstance(files, list) or len(files) != comp["changed_files"]:
                raise ValueError("Incomplete changed-file inventory")
            file_names = set()
            for file in files:
                if not isinstance(file, dict) or set(file) != FILE_FIELDS:
                    raise ValueError("Malformed file-level crosswalk")
                name_path = file["path"]
                checked_path(name_path)
                if name_path in file_names:
                    raise ValueError("Duplicate changed-file path")
                file_names.add(name_path)
                if file["previous_path"] is not None:
                    checked_path(file["previous_path"])
                if file["change_kind"] not in (
                        "added", "modified", "removed", "renamed", "copied",
                        "changed", "unchanged"):
                    raise ValueError("Unknown GitHub changed-file kind")
                branch_blob, main_blob = file["branch_blob_sha"], file["main_blob_sha"]
                checked_sha(branch_blob, allow_null=True)
                checked_sha(main_blob, allow_null=True)
                identical = branch_blob is not None and branch_blob == main_blob
                if type(file["same_path_blob"]) is not bool or (
                        file["same_path_blob"] != identical):
                    raise ValueError("Unfounded byte-identity claim")
                if not isinstance(file["alternate_main_paths"], list):
                    raise ValueError("Malformed alternate-path list")
                if len(file["alternate_main_paths"]) != len(set(
                        file["alternate_main_paths"])):
                    raise ValueError("Duplicate alternate paths")
                for alt in file["alternate_main_paths"]:
                    checked_path(alt)
                    if alt == name_path:
                        raise ValueError("Current path cannot be its own alternate")
                stats["file_entries"] += 1
                stats["same_path_blobs"] += int(identical)
            stats[expected_status] += 1
            stats["open_pr_heads"] += int(bool(prs))
    if len(names) != expected_refs:
        raise ValueError("Incomplete fixed branch-count denominator")
    stats["refs"] = len(names)
    return dict(stats)


def read_batches(root, parts=8):
    folder = root / PARTS
    out = []
    for index in range(parts):
        path = folder / ("part-%02d.json" % index)
        if path.is_symlink() or any(p.is_symlink() for p in path.parents
                                    if p != p.parent):
            raise ValueError("Snapshot symlink path refused")
        out.append(json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
            parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value))))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    stats = validate_batches(read_batches(args.root))
    if stats != {"refs": 52, "behind": 18, "ahead": 6, "diverged": 28,
                 "open_pr_heads": 6, "file_entries": 183, "same_path_blobs": 51}:
        raise SystemExit("Frozen crosswalk denominators changed unexpectedly")
    print(json.dumps({"read_only": True, "base_sha": MAIN, "counts": stats},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
