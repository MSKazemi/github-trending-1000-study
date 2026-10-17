"""Adversarial offline validation for #279 frozen non-executable branch crosswalk."""
import copy
from pathlib import Path
import unittest
from scripts.check_branch_no_loss_crosswalk import (
    MAIN, read_batches, reject_duplicate_keys, validate_batches
)


def sample_row():
    a, b = "a" * 40, "b" * 40
    return {
        "branch": "research/sample", "sha": a, "protected": False,
        "open_prs": [],
        "compare": {"status": "ahead", "ahead_by": 1,
                    "behind_by": 0, "changed_files": 1},
        "changed_files": [{
            "path": "docs/source.md", "change_kind": "modified",
            "previous_path": None, "branch_blob_sha": b,
            "main_blob_sha": a, "same_path_blob": False,
            "alternate_main_paths": []}],
        "disposition": "hold-diverged-file-and-source-review",
        "deletion_authorized": False,
    }


def sample_batch():
    return [{"batch_index": 0, "base_commit_sha": MAIN,
             "records": [sample_row()]}]


def validate_fixture(value):
    return validate_batches(value, expected_refs=1, expected_parts=1)


class BranchNoLossCrosswalkTests(unittest.TestCase):
    def test_frozen_provenance_and_denominators(self):
        records = read_batches(Path(__file__).resolve().parents[1])
        results = validate_batches(records)
        self.assertEqual(results["refs"], 52)
        self.assertEqual(results["file_entries"], 183)
        self.assertEqual(results["same_path_blobs"], 51)
        self.assertEqual(results["open_pr_heads"], 6)
        self.assertEqual(results["ahead"], 6)
        self.assertEqual(results["behind"], 18)
        self.assertEqual(results["diverged"], 28)

    def test_valid_synthetic(self):
        self.assertEqual(validate_fixture(sample_batch())["refs"], 1)

    def test_duplicate_keys_rejected_before_validation(self):
        with self.assertRaises(ValueError):
            reject_duplicate_keys([("branch", "a"), ("branch", "b")])

    def test_deletion_permission_can_never_be_inferred(self):
        row = sample_batch()
        row[0]["records"][0]["deletion_authorized"] = True
        with self.assertRaises(ValueError):
            validate_fixture(row)

    def test_bad_sha_or_ref_rejected(self):
        for field, value in (("sha", "abc"), ("branch", "refs/heads/evil"),
                             ("branch", "x/../y")):
            data = sample_batch()
            data[0]["records"][0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                validate_fixture(data)

    def test_unsafe_changed_file_paths_rejected(self):
        for path in ("../secret", "/tmp/file", "foo//bar", "a/./b"):
            data = sample_batch()
            data[0]["records"][0]["changed_files"][0]["path"] = path
            with self.subTest(path=path), self.assertRaises(ValueError):
                validate_fixture(data)

    def test_no_false_byte_equality(self):
        data = sample_batch()
        data[0]["records"][0]["changed_files"][0]["same_path_blob"] = True
        with self.assertRaisesRegex(ValueError, "byte-identity"):
            validate_fixture(data)

    def test_compare_counts_and_status_fail_closed(self):
        for key, value in (("status", "behind"), ("ahead_by", 0),
                           ("behind_by", -1), ("changed_files", 0)):
            data = sample_batch()
            data[0]["records"][0]["compare"][key] = value
            with self.subTest(field=key), self.assertRaises(ValueError):
                validate_fixture(data)

    def test_no_unheld_open_pr_or_moving_pr_head(self):
        for wrong_head in (False, True):
            data = sample_batch()
            row = data[0]["records"][0]
            row["open_prs"] = [{"pr": 17, "draft": False,
                               "head_sha": "b" * 40 if wrong_head else row["sha"]}]
            if not wrong_head:
                with self.assertRaisesRegex(ValueError, "classification"):
                    validate_fixture(data)
            else:
                with self.assertRaisesRegex(ValueError, "PR head"):
                    validate_fixture(data)

    def test_duplicate_branch_or_pr_rejected(self):
        data = sample_batch()
        data[0]["records"].append(copy.deepcopy(data[0]["records"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate branch"):
            validate_batches(data, expected_refs=2, expected_parts=1)
        data = sample_batch()
        row = data[0]["records"][0]
        row["open_prs"] = [{"pr": 17, "draft": True, "head_sha": row["sha"]}] * 2
        row["disposition"] = "hold-open-pr"
        with self.assertRaisesRegex(ValueError, "duplicate PR"):
            validate_fixture(data)

    def test_missing_batch_or_changed_base_rejected(self):
        data = sample_batch()
        with self.assertRaisesRegex(ValueError, "Missing or additional"):
            validate_batches(data, expected_refs=1, expected_parts=2)
        data[0]["base_commit_sha"] = "c" * 40
        with self.assertRaisesRegex(ValueError, "base SHA"):
            validate_fixture(data)


if __name__ == "__main__":
    unittest.main()
