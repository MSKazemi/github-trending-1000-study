"""Regression compatibility checks for #277's frozen recovery evidence.

One canonical validator lives in scripts/check_archive_crosswalk_snapshot.py.
These tests preserve #443's original adversarial scenarios without copying the
validation logic or making any live GitHub request or deletion authorization.
"""
import copy
from pathlib import Path
import unittest

from scripts.check_archive_crosswalk_snapshot import (
    MANIFEST, SNAPSHOT, _git_blob_sha, _parse, _read, validate_snapshot
)

ROOT = Path(__file__).resolve().parents[1]


class HistoricalBranchRetirementSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw_plan = _read(ROOT / MANIFEST)
        cls.blob_sha = _git_blob_sha(cls.raw_plan)
        cls.plan = _parse(cls.raw_plan)
        cls.snapshot = _parse(_read(ROOT / SNAPSHOT))

    def validate(self, record):
        return validate_snapshot(record, self.plan, self.raw_plan)

    def test_frozen_snapshot_consistent_not_authorization(self):
        self.assertEqual(self.blob_sha, self.snapshot["source_manifest"]["blob_sha"])
        result = self.validate(self.snapshot)
        self.assertEqual(result["exact_archive_tags_observed"], 59)
        self.assertEqual(result["moved_branches_held"], 1)
        self.assertIs(result["deletion_authorized"], False)
        self.assertIs(result["historical_snapshot_only"], True)

    def test_duplicate_json_key_and_invalid_constant_fail(self):
        with self.assertRaises(ValueError):
            _parse(b'{"x":1,"x":2}')
        with self.assertRaises(ValueError):
            _parse(b'{"x":NaN}')

    def test_missing_or_duplicate_branch_fails(self):
        for mutation in ("drop", "duplicate"):
            doc = copy.deepcopy(self.snapshot)
            if mutation == "drop":
                doc["manifest_rows"].pop()
            else:
                doc["manifest_rows"][-1] = copy.deepcopy(doc["manifest_rows"][0])
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                self.validate(doc)

    def test_wrong_tag_and_changed_tip_never_pass(self):
        for field, value in (
            ("observed_archive_sha", "f" * 40),
            ("observed_archive_object_type", "tag"),
            ("observed_branch_sha", "f" * 40),
            ("classification", "safe_to_delete"),
        ):
            doc = copy.deepcopy(self.snapshot)
            row = next(x for x in doc["manifest_rows"]
                       if x["classification"] == "absent_exact_commit_tag_observed")
            row[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.validate(doc)

    def test_existing_moved_branch_never_approved(self):
        doc = copy.deepcopy(self.snapshot)
        row = next(x for x in doc["manifest_rows"]
                   if x["classification"] == "present_moved_hold")
        row["observed_archive_sha"] = row["expected_sha"]
        with self.assertRaises(ValueError):
            self.validate(doc)

    def test_retargeting_historical_manifest_or_main_blocks(self):
        for field, value in (("source_main_sha", "e" * 40),
                             ("blob_sha", "f" * 40)):
            doc = copy.deepcopy(self.snapshot)
            doc["source_manifest"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.validate(doc)
        doc = copy.deepcopy(self.snapshot)
        doc["observed_main"]["after_sha"] = "f" * 40
        with self.assertRaises(ValueError):
            self.validate(doc)

    def test_no_hidden_permission_or_incomplete_pagination(self):
        doc = copy.deepcopy(self.snapshot)
        doc["deletion_authorized"] = True
        with self.assertRaises(ValueError):
            self.validate(doc)
        doc = copy.deepcopy(self.snapshot)
        doc["observed_inventory"]["branch_pages"][-1]["count"] = 10
        with self.assertRaises(ValueError):
            self.validate(doc)


if __name__ == "__main__":
    unittest.main()
