"""Offline, synthetic adversarial tests of the historical archive evidence gate."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from scripts.check_archive_crosswalk_snapshot import (
    MANIFEST, REPO, SNAPSHOT, _git_blob_sha, _parse, check, validate_snapshot
)


def fixture():
    main = "a" * 40
    manifest = {
        "schema_version": "1.0", "repository": REPO,
        "source_main_sha": main,
        "archive_prefix": "branch-archive/2026-10-13",
        "branches": [],
    }
    rows = []
    for i in range(60):
        branch = "test/branch-%02d" % i
        sha = "%040x" % (i + 1)
        pr = i + 1
        manifest["branches"].append({
            "branch": branch, "expected_sha": sha,
            "merged_pr": pr, "merge_commit_sha": "%040x" % (pr + 200),
        })
        rows.append({
            "branch": branch, "merged_pr": pr,
            "expected_sha": sha, "observed_branch_sha": None,
            "observed_archive_sha": sha,
            "observed_archive_object_type": "commit",
            "classification": "absent_exact_commit_tag_observed",
        })
    rows[-1]["observed_branch_sha"] = "f" * 40
    rows[-1]["observed_archive_sha"] = None
    rows[-1]["observed_archive_object_type"] = None
    rows[-1]["classification"] = "present_moved_hold"
    raw = (json.dumps(manifest, indent=2) + "\n").encode()
    snapshot = {
        "schema_version": "1.0",
        "record_type": "read_only_repo_ref_crosswalk_not_an_authorized_retirement_plan",
        "observation_date_utc": "2026-10-17", "repository": REPO,
        "source_manifest": {
            "path": MANIFEST.as_posix(), "blob_sha": _git_blob_sha(raw),
            "source_main_sha": main, "candidate_count": 60,
        },
        "observed_main": {
            "before_sha": main, "after_sha": main,
            "stable_between_reads": True,
            "protected_before": False, "protected_after": False,
        },
        "observed_inventory": {
            "branch_pages": [{"page": 1, "count": 54}, {"page": 2, "count": 0}],
            "archive_tag_refs_with_prefix": 229,
            "repository_rulesets_count": 0,
            "open_pr_page_counts": [1, 0],
        },
        "summary": {"absent_exact_commit_tag_observed": 59,
                    "present_moved_hold": 1},
        "open_pr_heads_at_readback": [{
            "number": 440, "head_ref": "research/feasibility",
            "head_sha": "c" * 40, "head_repo": REPO,
        }],
        "manifest_rows": rows,
        "provenance_limits": ["Historical observations are not deletion approval."],
    }
    return snapshot, manifest, raw


class ArchiveCrosswalkSnapshotTests(unittest.TestCase):
    def test_valid_snapshot_always_denies_deletion(self):
        snapshot, manifest, raw = fixture()
        self.assertEqual(validate_snapshot(snapshot, manifest, raw), {
            "historical_snapshot_only": True, "deletion_authorized": False,
            "candidate_count": 60, "exact_archive_tags_observed": 59,
            "moved_branches_held": 1,
        })

    def test_duplicate_json_keys_and_nonfinite_rejected(self):
        for content in (b'{"a":1,"a":2}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.subTest(raw=content), self.assertRaises(ValueError):
                _parse(content)

    def test_mismatched_or_missing_archive_tag_blocks(self):
        for key, value in (("observed_archive_sha", "a" * 40),
                           ("observed_archive_sha", None),
                           ("observed_archive_object_type", "tag"),
                           ("observed_branch_sha", "a" * 40)):
            snapshot, manifest, raw = fixture()
            snapshot["manifest_rows"][0][key] = value
            with self.subTest(field=key), self.assertRaises(ValueError):
                validate_snapshot(snapshot, manifest, raw)

    def test_moved_head_cannot_be_relabelled_as_safe(self):
        snapshot, manifest, raw = fixture()
        snapshot["manifest_rows"][-1]["classification"] = "absent_exact_commit_tag_observed"
        with self.assertRaisesRegex(ValueError, "classification"):
            validate_snapshot(snapshot, manifest, raw)

    def test_changed_original_pr_sha_or_replaced_branch_fails(self):
        for field, value in (("expected_sha", "0" * 40),
                             ("merged_pr", 999),
                             ("branch", "test/another-branch")):
            snapshot, manifest, raw = fixture()
            snapshot["manifest_rows"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_snapshot(snapshot, manifest, raw)

    def test_duplicate_or_missing_manifest_row_fails(self):
        snapshot, manifest, raw = fixture()
        snapshot["manifest_rows"][5] = copy.deepcopy(snapshot["manifest_rows"][4])
        with self.assertRaises(ValueError):
            validate_snapshot(snapshot, manifest, raw)
        snapshot, manifest, raw = fixture()
        snapshot["manifest_rows"].pop()
        with self.assertRaises(ValueError):
            validate_snapshot(snapshot, manifest, raw)

    def test_modifying_manifest_bytes_breaks_blob_binding(self):
        snapshot, manifest, raw = fixture()
        with self.assertRaisesRegex(ValueError, "Git blob"):
            validate_snapshot(snapshot, manifest, raw + b" ")
        manifest["branches"][0]["expected_sha"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "Git blob"):
            validate_snapshot(snapshot, manifest, json.dumps(manifest).encode())

    def test_false_summary_counts_or_delete_flag_fails(self):
        snapshot, manifest, raw = fixture()
        snapshot["summary"]["present_moved_hold"] = 0
        with self.assertRaises(ValueError):
            validate_snapshot(snapshot, manifest, raw)
        snapshot, manifest, raw = fixture()
        snapshot["deletion_authorized"] = True
        with self.assertRaisesRegex(ValueError, "schema"):
            validate_snapshot(snapshot, manifest, raw)

    def test_open_pr_count_and_sha_are_anchored(self):
        snapshot, manifest, raw = fixture()
        snapshot["observed_inventory"]["open_pr_page_counts"] = [2, 0]
        with self.assertRaisesRegex(ValueError, "open-PR"):
            validate_snapshot(snapshot, manifest, raw)
        snapshot, manifest, raw = fixture()
        snapshot["open_pr_heads_at_readback"][0]["head_sha"] = "bad"
        with self.assertRaisesRegex(ValueError, "SHA"):
            validate_snapshot(snapshot, manifest, raw)

    def test_main_stability_must_match_shas(self):
        snapshot, manifest, raw = fixture()
        snapshot["observed_main"]["after_sha"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "main state"):
            validate_snapshot(snapshot, manifest, raw)
        snapshot, manifest, raw = fixture()
        snapshot["observed_main"]["stable_between_reads"] = 1
        with self.assertRaisesRegex(ValueError, "main state"):
            validate_snapshot(snapshot, manifest, raw)

    def test_reject_missing_final_page_and_boolean_count(self):
        for field, value in (("branch_pages", [{"page": 1, "count": 54}]),
                             ("branch_pages", [{"page": 1, "count": True},
                                               {"page": 2, "count": 0}]),
                             ("open_pr_page_counts", [1, 1])):
            snapshot, manifest, raw = fixture()
            snapshot["observed_inventory"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_snapshot(snapshot, manifest, raw)

    def test_symlink_and_oversize_files_are_rejected(self):
        snapshot, manifest, raw = fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / MANIFEST).parent.mkdir(parents=True)
            (root / SNAPSHOT).parent.mkdir(parents=True)
            (root / MANIFEST).write_bytes(raw)
            (root / SNAPSHOT).write_text(json.dumps(snapshot))
            self.assertFalse(check(root)["deletion_authorized"])
            (root / SNAPSHOT).unlink()
            target = root / "evidence-original.json"
            target.write_text(json.dumps(snapshot))
            (root / SNAPSHOT).symlink_to(target)
            with self.assertRaises(ValueError):
                check(root)
            (root / SNAPSHOT).unlink()
            (root / SNAPSHOT).write_bytes(b" " * (128 * 1024 + 1))
            with self.assertRaises(ValueError):
                check(root)


if __name__ == "__main__":
    unittest.main()
