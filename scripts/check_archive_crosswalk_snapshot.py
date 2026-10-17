#!/usr/bin/env python3
"""Fail-closed OFFLINE checks for a historical archive crosswalk; never mutate refs.

This checks internal provenance and the original manifest's Git blob bytes.
It cannot confirm live GitHub ref state, tag protection, consent, or approval.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat

REPO = "MSKazemi/github-trending-1000-study"
MANIFEST = Path("ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json")
SNAPSHOT = Path("docs/reviews/2026-10-17-issue-277-readonly-archive-crosswalk.json")
SHA = re.compile(r"[0-9a-f]{40}\Z")
BRANCH = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,199}\Z")
MAX_BYTES = 128 * 1024


def _error(message):
    raise ValueError(message)


def _object_pairs(pairs):
    record = {}
    for key, val in pairs:
        if key in record:
            _error("duplicate JSON key")
        record[key] = val
    return record


def _reject_nonfinite(value):
    _error("non-finite JSON number")


def _read(path):
    """Read bounded regular files, disallowing symlinks in their relative path."""
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            _error("symlink in evidence file path")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags)
    try:
        mode = os.fstat(fd).st_mode
        if not stat.S_ISREG(mode):
            _error("evidence input must be a regular file")
        if os.fstat(fd).st_size > MAX_BYTES:
            _error("evidence input exceeds byte limit")
        content = os.read(fd, MAX_BYTES + 1)
        if len(content) > MAX_BYTES:
            _error("evidence input exceeds byte limit")
    finally:
        os.close(fd)
    return content


def _parse(content):
    return json.loads(content.decode("utf-8"), object_pairs_hook=_object_pairs,
                      parse_constant=_reject_nonfinite)


def _dict(value, keys, description):
    if type(value) is not dict or set(value) != set(keys):
        _error("invalid " + description + " schema")


def _sha(value):
    if type(value) is not str or SHA.fullmatch(value) is None:
        _error("invalid 40-digit Git SHA")


def _branch(value):
    if (type(value) is not str or BRANCH.fullmatch(value) is None or
            value.startswith("refs/") or value.endswith((".", "/")) or
            ".." in value or any(part in ("", ".", "..") for part in value.split("/"))):
        _error("invalid or ambiguous Git branch name")


def _integer(value, *, positive=False):
    if type(value) is not int or value < (1 if positive else 0):
        _error("invalid integer or boolean substituted for integer")


def _count_pages(pages, *, named):
    if type(pages) is not list or not 2 <= len(pages) <= 20:
        _error("incomplete paginated " + named + " inventory")
    counts = []
    for ix, item in enumerate(pages, 1):
        if named == "branch":
            _dict(item, ("page", "count"), "branch page")
            if type(item["page"]) is not int or item["page"] != ix:
                _error("missing or reordered branch page")
            count = item["count"]
        else:
            count = item
        _integer(count)
        if count > 1000 or (ix < len(pages) and count == 0):
            _error("incomplete or excessive paginated inventory")
        counts.append(count)
    if counts[-1] != 0:
        _error("missing terminal empty page")
    return sum(counts)


def _git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def validate_snapshot(snapshot, manifest, manifest_bytes):
    """Validate reported historical evidence, not live refs or deletion eligibility."""
    _dict(manifest, ("schema_version", "repository", "source_main_sha", "archive_prefix",
                     "branches"), "original manifest")
    if (manifest["schema_version"] != "1.0" or manifest["repository"] != REPO or
            manifest["archive_prefix"] != "branch-archive/2026-10-13"):
        _error("unexpected original manifest identity")
    _sha(manifest["source_main_sha"])
    if type(manifest["branches"]) is not list or not manifest["branches"]:
        _error("missing original manifest branches")
    originals = {}
    for original in manifest["branches"]:
        _dict(original, ("branch", "expected_sha", "merged_pr", "merge_commit_sha"),
              "original branch row")
        name = original["branch"]
        _branch(name)
        _sha(original["expected_sha"])
        _sha(original["merge_commit_sha"])
        _integer(original["merged_pr"], positive=True)
        if name == "main" or name in originals:
            _error("duplicate original branch or main")
        originals[name] = original

    _dict(snapshot, ("schema_version", "record_type", "observation_date_utc",
                     "repository", "source_manifest", "observed_main",
                     "observed_inventory", "summary", "open_pr_heads_at_readback",
                     "manifest_rows", "provenance_limits"), "snapshot")
    if (snapshot["schema_version"] != "1.0" or
            snapshot["record_type"] !=
            "read_only_repo_ref_crosswalk_not_an_authorized_retirement_plan" or
            snapshot["observation_date_utc"] != "2026-10-17" or
            snapshot["repository"] != REPO):
        _error("unexpected historical snapshot identity")
    source = snapshot["source_manifest"]
    _dict(source, ("path", "blob_sha", "source_main_sha", "candidate_count"),
          "source provenance")
    _sha(source["blob_sha"])
    if (source["path"] != MANIFEST.as_posix() or
            source["blob_sha"] != _git_blob_sha(manifest_bytes) or
            source["source_main_sha"] != manifest["source_main_sha"] or
            type(source["candidate_count"]) is not int or
            source["candidate_count"] != len(originals) or len(originals) != 60):
        _error("source Git blob or historical candidate set mismatch")

    main = snapshot["observed_main"]
    _dict(main, ("before_sha", "after_sha", "stable_between_reads",
                 "protected_before", "protected_after"), "main observation")
    _sha(main["before_sha"])
    _sha(main["after_sha"])
    if (type(main["stable_between_reads"]) is not bool or
            main["stable_between_reads"] != (main["before_sha"] == main["after_sha"]) or
            type(main["protected_before"]) is not bool or
            type(main["protected_after"]) is not bool):
        _error("inconsistent observed main state")

    inventory = snapshot["observed_inventory"]
    _dict(inventory, ("branch_pages", "archive_tag_refs_with_prefix",
                      "repository_rulesets_count", "open_pr_page_counts"),
          "observed inventory")
    if _count_pages(inventory["branch_pages"], named="branch") != 54:
        _error("unexpected historical branch-page total")
    _integer(inventory["archive_tag_refs_with_prefix"])
    _integer(inventory["repository_rulesets_count"])
    open_pr_count = _count_pages(inventory["open_pr_page_counts"], named="open PR")

    prs = snapshot["open_pr_heads_at_readback"]
    if type(prs) is not list or len(prs) != open_pr_count:
        _error("inconsistent open-PR inventory")
    pr_numbers = set()
    for row in prs:
        _dict(row, ("number", "head_ref", "head_sha", "head_repo"), "open PR head")
        _integer(row["number"], positive=True)
        _branch(row["head_ref"])
        _sha(row["head_sha"])
        if row["head_repo"] != REPO or row["number"] in pr_numbers:
            _error("duplicate or foreign open PR head")
        pr_numbers.add(row["number"])

    records = snapshot["manifest_rows"]
    if type(records) is not list or len(records) != len(originals):
        _error("missing or extra archived-manifest row")
    counted = {"absent_exact_commit_tag_observed": 0, "present_moved_hold": 0}
    seen = set()
    for row in records:
        _dict(row, ("branch", "merged_pr", "expected_sha",
                    "observed_branch_sha", "observed_archive_sha",
                    "observed_archive_object_type", "classification"),
              "archive observation")
        name = row["branch"]
        _branch(name)
        if name not in originals or name in seen:
            _error("missing original branch or duplicate observation")
        seen.add(name)
        original = originals[name]
        if (type(row["merged_pr"]) is not int or
                row["merged_pr"] != original["merged_pr"] or
                row["expected_sha"] != original["expected_sha"]):
            _error("archive observation changed original PR or head SHA")
        live = row["observed_branch_sha"]
        archive = row["observed_archive_sha"]
        if live is not None:
            _sha(live)
        if archive is not None:
            _sha(archive)
        exact_tag = (live is None and archive == original["expected_sha"] and
                     row["observed_archive_object_type"] == "commit")
        moved_hold = (live is not None and live != original["expected_sha"] and
                      archive is None and row["observed_archive_object_type"] is None)
        label = row["classification"]
        if exact_tag:
            if label != "absent_exact_commit_tag_observed":
                _error("false exact-archive classification")
        elif moved_hold:
            if label != "present_moved_hold":
                _error("unsafe moved-branch classification")
        else:
            _error("unknown or unsafe branch/archive state")
        counted[label] += 1

    _dict(snapshot["summary"], tuple(counted), "summary")
    if any(type(snapshot["summary"][key]) is not int or
           snapshot["summary"][key] != count for key, count in counted.items()):
        _error("claimed summary disagrees with row-level observations")
    limitations = snapshot["provenance_limits"]
    if (type(limitations) is not list or not limitations or len(limitations) > 30 or
            any(type(x) is not str or not (1 <= len(x) <= 1024) for x in limitations)):
        _error("missing or malformed source limitations")
    return {"historical_snapshot_only": True, "deletion_authorized": False,
            "candidate_count": len(originals),
            "exact_archive_tags_observed": counted["absent_exact_commit_tag_observed"],
            "moved_branches_held": counted["present_moved_hold"]}


def check(root):
    manifest_bytes = _read(root / MANIFEST)
    snapshot_bytes = _read(root / SNAPSHOT)
    return validate_snapshot(_parse(snapshot_bytes), _parse(manifest_bytes),
                             manifest_bytes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        outcome = check(args.root)
    except (OSError, ValueError, UnicodeError) as exc:
        parser.exit(1, "Archive crosswalk BLOCKED: " + str(exc) + "\n")
    print(json.dumps(outcome, sort_keys=True))


if __name__ == "__main__":
    main()
