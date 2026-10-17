"""Offline integrity check of issue #277's historical read-only recovery audit.

This checks only frozen bytes and self-consistency. It neither queries GitHub
nor authorizes branch retirement, approves security controls or confirms tags
are immutable today.
"""
import copy
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json"
CROSSWALK = ROOT / "docs/reviews/2026-10-17-issue-277-readonly-archive-crosswalk.json"
SHA = re.compile(r"[0-9a-f]{40}\Z")
FIELDS = {"branch", "merged_pr", "expected_sha", "observed_branch_sha",
          "observed_archive_sha", "observed_archive_object_type", "classification"}


def no_duplicate_keys(pairs):
    result = {}
    for k, v in pairs:
        if k in result:
            raise ValueError("duplicate JSON key")
        result[k] = v
    return result


def parse_json(raw):
    return json.loads(
        raw.decode("utf-8"), object_pairs_hook=no_duplicate_keys,
        parse_constant=lambda _value: (_ for _ in ()).throw(ValueError("non-finite")),
    )


def validate_historical_snapshot(plan, crosswalk, manifest_blob_sha):
    if (not isinstance(plan, dict) or not isinstance(crosswalk, dict)
            or set(crosswalk) != {
                "schema_version", "record_type", "observation_date_utc",
                "repository", "source_manifest", "observed_main",
                "observed_inventory", "summary", "open_pr_heads_at_readback",
                "manifest_rows", "provenance_limits"}):
        raise ValueError("unexpected historical audit format")
    if (crosswalk["schema_version"] != "1.0" or
            crosswalk["record_type"] !=
            "read_only_repo_ref_crosswalk_not_an_authorized_retirement_plan"):
        raise ValueError("historical audit cannot become a deletion allowlist")
    if (crosswalk["repository"] != "MSKazemi/github-trending-1000-study" or
            crosswalk["repository"] != plan.get("repository")):
        raise ValueError("repository identity changed")
    manifest = crosswalk["source_manifest"]
    if (not isinstance(manifest, dict)
            or manifest.get("path") !=
            "ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json"
            or manifest.get("blob_sha") != manifest_blob_sha
            or manifest.get("source_main_sha") != plan.get("source_main_sha")
            or manifest.get("candidate_count") != len(plan.get("branches", []))
            or plan.get("archive_prefix") != "branch-archive/2026-10-13"):
        raise ValueError("untrusted historical source manifest")
    before = crosswalk["observed_main"]
    if (not isinstance(before, dict) or
            before.get("stable_between_reads") is not True or
            before.get("before_sha") != before.get("after_sha") or
            before.get("before_sha") is None or
            not SHA.fullmatch(before["before_sha"])):
        raise ValueError("historical main observation inconsistent")
    inventory = crosswalk["observed_inventory"]
    if (not isinstance(inventory, dict)
            or inventory.get("repository_rulesets_count") != 0
            or type(inventory.get("archive_tag_refs_with_prefix")) is not int
            or inventory["archive_tag_refs_with_prefix"] < 59):
        raise ValueError("historical ruleset/ref denominator inconsistent")
    if not isinstance(inventory.get("branch_pages"), list):
        raise ValueError("missing historical branch pagination")
    page_rows = inventory["branch_pages"]
    if (len(page_rows) < 2 or
            [x.get("page") for x in page_rows] != list(range(1, len(page_rows) + 1))
            or any(type(x.get("count")) is not int or x["count"] < 0
                   for x in page_rows)
            or page_rows[-1]["count"] != 0):
        raise ValueError("incomplete historical pagination")
    if not isinstance(crosswalk["open_pr_heads_at_readback"], list):
        raise ValueError("missing historical PR list")
    counts = inventory.get("open_pr_page_counts")
    if (not isinstance(counts, list) or not counts or counts[-1] != 0
            or sum(counts) != len(crosswalk["open_pr_heads_at_readback"])):
        raise ValueError("historical open PR pages disagree")
    source = plan.get("branches")
    rows = crosswalk["manifest_rows"]
    if (not isinstance(source, list) or len(source) != 60 or
            not isinstance(rows, list) or len(rows) != len(source)):
        raise ValueError("incomplete old-manifest crosswalk")
    previous = {}
    for entry in source:
        if (not isinstance(entry, dict) or
                set(entry) != {"branch", "expected_sha", "merged_pr", "merge_commit_sha"}
                or entry["branch"] in previous):
            raise ValueError("duplicate or malformed historical plan row")
        if type(entry["merged_pr"]) is not int or entry["merged_pr"] <= 0:
            raise ValueError("invalid merged PR")
        if not isinstance(entry["expected_sha"], str) or not SHA.fullmatch(entry["expected_sha"]):
            raise ValueError("invalid historical expected commit SHA")
        previous[entry["branch"]] = entry
    seen = set()
    matched = held = 0
    for row in rows:
        if not isinstance(row, dict) or set(row) != FIELDS:
            raise ValueError("unrecognized crosswalk row fields")
        branch = row["branch"]
        if branch not in previous or branch in seen:
            raise ValueError("missing or duplicate historical source branch")
        seen.add(branch)
        old = previous[branch]
        if (row["merged_pr"] != old["merged_pr"] or
                row["expected_sha"] != old["expected_sha"]):
            raise ValueError("PR/commit provenance mismatch")
        if row["classification"] == "absent_exact_commit_tag_observed":
            if (row["observed_branch_sha"] is not None or
                    row["observed_archive_sha"] != row["expected_sha"] or
                    row["observed_archive_object_type"] != "commit"):
                raise ValueError("unverified recovery SHA or tag type")
            matched += 1
        elif row["classification"] == "present_moved_hold":
            live = row["observed_branch_sha"]
            if (not isinstance(live, str) or not SHA.fullmatch(live)
                    or live == row["expected_sha"] or
                    row["observed_archive_sha"] is not None or
                    row["observed_archive_object_type"] is not None):
                raise ValueError("changed branch must remain a held ref")
            held += 1
        else:
            raise ValueError("unexpected historical disposition")
    if ((matched, held) != (59, 1) or
            crosswalk["summary"] != {
                "absent_exact_commit_tag_observed": matched,
                "present_moved_hold": held}):
        raise ValueError("inconsistent historical recovery totals")
    return {"archived_ref_observations": matched, "changed_ref_holds": held}


class HistoricalBranchRetirementSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw_plan = PLAN.read_bytes()
        cls.blob_sha = hashlib.sha1(
            b"blob " + str(len(raw_plan)).encode("ascii") + b"\0" + raw_plan
        ).hexdigest()
        cls.plan = parse_json(raw_plan)
        cls.snapshot = parse_json(CROSSWALK.read_bytes())

    def test_frozen_snapshot_consistent_not_authorization(self):
        self.assertEqual(self.blob_sha, self.snapshot["source_manifest"]["blob_sha"])
        self.assertEqual(validate_historical_snapshot(
            self.plan, self.snapshot, self.blob_sha
        ), {"archived_ref_observations": 59, "changed_ref_holds": 1})

    def test_duplicate_json_key_and_invalid_constant_fail(self):
        with self.assertRaises(ValueError):
            parse_json(b'{"x":1,"x":2}')
        with self.assertRaises(ValueError):
            parse_json(b'{"x":NaN}')

    def test_missing_or_duplicate_branch_fails(self):
        for mutation in ("drop", "duplicate"):
            doc = copy.deepcopy(self.snapshot)
            if mutation == "drop":
                doc["manifest_rows"].pop()
            else:
                doc["manifest_rows"][-1] = copy.deepcopy(doc["manifest_rows"][0])
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_historical_snapshot(self.plan, doc, self.blob_sha)

    def test_wrong_tag_and_changed_tip_never_pass(self):
        for field, value in (
            ("observed_archive_sha", "f" * 40),
            ("observed_archive_object_type", "tag"),
            ("observed_branch_sha", "f" * 40),
            ("classification", "safe_to_delete"),
        ):
            doc = copy.deepcopy(self.snapshot)
            row = next(r for r in doc["manifest_rows"]
                       if r["classification"] == "absent_exact_commit_tag_observed")
            row[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_historical_snapshot(self.plan, doc, self.blob_sha)

    def test_existing_moved_branch_never_approved(self):
        doc = copy.deepcopy(self.snapshot)
        row = next(r for r in doc["manifest_rows"]
                   if r["classification"] == "present_moved_hold")
        row["observed_archive_sha"] = row["expected_sha"]
        with self.assertRaises(ValueError):
            validate_historical_snapshot(self.plan, doc, self.blob_sha)

    def test_retargeting_historical_manifest_or_main_blocks(self):
        for field, value in (("source_main_sha", "e" * 40),
                             ("blob_sha", "f" * 40)):
            doc = copy.deepcopy(self.snapshot)
            doc["source_manifest"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_historical_snapshot(self.plan, doc, self.blob_sha)
        doc = copy.deepcopy(self.snapshot)
        doc["observed_main"]["after_sha"] = "f" * 40
        with self.assertRaises(ValueError):
            validate_historical_snapshot(self.plan, doc, self.blob_sha)

    def test_no_hidden_permission_or_incomplete_pagination(self):
        doc = copy.deepcopy(self.snapshot)
        doc["deletion_authorized"] = True
        with self.assertRaises(ValueError):
            validate_historical_snapshot(self.plan, doc, self.blob_sha)
        doc = copy.deepcopy(self.snapshot)
        doc["observed_inventory"]["branch_pages"][-1]["count"] = 10
        with self.assertRaises(ValueError):
            validate_historical_snapshot(self.plan, doc, self.blob_sha)


if __name__ == "__main__":
    unittest.main()
