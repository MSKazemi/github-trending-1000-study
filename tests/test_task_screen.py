"""Synthetic screen audit tests + real public metadata recheck structural regression.

Tests do NOT simulate actual human-independent judgments or accepted tasks.
"""
import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.task_screen import TaskScreenError, audit, prepare, validate_recheck


ROOT = Path(__file__).resolve().parents[1]
FRAME = ROOT / "examples" / "task_intake.cross_ecosystem_2026-10-12.json"
RECHECK = ROOT / "research-notes" / "issue-recheck-2026-10-12.json"


class ScreenTests(unittest.TestCase):
    def setUp(self):
        self.frame = json.loads(FRAME.read_text(encoding="utf-8"))
        self.recheck = json.loads(RECHECK.read_text(encoding="utf-8"))

    def make_review(self, role, label="screenable_for_spec_drafting", reviewer=None):
        packet = prepare(self.frame, self.recheck)
        rows = []
        for item in packet["candidates"]:
            rows.append({
                "task_id": item["task_id"], "label": label,
                "reason_code": "none" if label == "screenable_for_spec_drafting" else
                               "scope" if label == "exclude_candidate" else "unknown",
                "leakage_signal": "unknown",
                "issue_status_check": "open",
                "evidence_ref": item["source_url"] if label != "defer_unknown" else None,
            })
        return {"schema_version": "1.0", "packet_sha256": packet["packet_sha256"],
                "reviewer_slot": role, "reviewer_ref": reviewer or ("synthetic-" + role),
                "reviewed_at_utc": self.recheck["rechecked_at_utc"],
                "decisions": rows}

    def test_actual_recheck_only_verifies_public_metadata_not_tasks(self):
        sampled, selected, originals, seen = validate_recheck(self.frame, self.recheck)
        self.assertEqual(len(selected), 16)
        self.assertEqual(len(seen), 16)
        self.assertEqual(len(originals), 16)
        self.assertEqual(self.recheck["source_frame_sha256"], sampled["reduced_frame_sha256"])
        self.assertTrue(all(rec["fetch_status"] == "observed" and rec["state"] == "open"
                            for rec in seen.values()))
        packet = prepare(self.frame, self.recheck)
        self.assertEqual(packet["selected_count"], 16)
        self.assertEqual(packet["source_frame_sha256"], self.recheck["source_frame_sha256"])
        self.assertEqual(len({x["task_id"] for x in packet["candidates"]}), 16)
        self.assertTrue(all(x["review_state"] == "unreviewed"
                            and x["reuse_opportunity"] == "unknown"
                            and x["task_acceptance"] == "not_frozen"
                            and x["metadata_updated_since_intake"] is False
                            for x in packet["candidates"]))
        self.assertFalse(packet["human_independence_verified"])
        self.assertEqual(packet["experiment_enrollment"], "blocked")

    def test_reject_missing_or_forged_source_row(self):
        for change in ("missing", "duplicate", "foreign"):
            val = copy.deepcopy(self.recheck)
            if change == "missing":
                val["records"].pop()
            elif change == "duplicate":
                val["records"].append(copy.deepcopy(val["records"][0]))
            else:
                val["records"][0]["issue_id"] = 999999
            with self.subTest(change=change), self.assertRaises(TaskScreenError):
                prepare(self.frame, val)

    def test_reject_incorrect_intake_checksum(self):
        val = copy.deepcopy(self.recheck)
        val["source_frame_sha256"] = "0" * 64
        with self.assertRaisesRegex(TaskScreenError, "checksum"):
            prepare(self.frame, val)

    def test_reject_after_recheck_updates_or_backward_update(self):
        for changed in ("2040-01-01T00:00:00Z", "2000-01-01T00:00:00Z"):
            val = copy.deepcopy(self.recheck)
            val["records"][0]["updated_at_utc"] = changed
            with self.subTest(time=changed), self.assertRaises(TaskScreenError):
                prepare(self.frame, val)

    def test_unavailable_source_is_unknown_not_absence_of_solution(self):
        val = copy.deepcopy(self.recheck)
        record = val["records"][0]
        record.update({"fetch_status": "unavailable", "state": "unknown",
                       "updated_at_utc": None, "closed_at_utc": None,
                       "source_error": "rate_limited"})
        candidate = prepare(self.frame, val)["candidates"]
        match = [x for x in candidate if x["task_id"] == record["task_id"]][0]
        self.assertIsNone(match["metadata_updated_since_intake"])
        self.assertEqual(match["recheck_issue_state"], "unknown")
        self.assertEqual(match["reuse_opportunity"], "unknown")
        bad = copy.deepcopy(val)
        bad["records"][0]["source_error"] = None
        with self.assertRaises(TaskScreenError):
            prepare(self.frame, bad)

    def test_closed_issue_requires_real_closure_timestamp(self):
        val = copy.deepcopy(self.recheck)
        val["records"][0]["state"] = "closed"
        with self.assertRaises(TaskScreenError):
            prepare(self.frame, val)
        val["records"][0]["closed_at_utc"] = self.recheck["rechecked_at_utc"]
        self.assertEqual(prepare(self.frame, val)["selected_count"], 16)

    def test_observed_recheck_forbids_raw_issue_body_or_user_profile(self):
        val = copy.deepcopy(self.recheck)
        val["records"][0]["body"] = "should not be stored"
        with self.assertRaises(TaskScreenError):
            prepare(self.frame, val)

    def test_two_synthetic_concordant_reports_never_accept_task(self):
        a, b = self.make_review("A"), self.make_review("B")
        result = audit(self.frame, self.recheck, a, b)
        self.assertEqual(result["double_reviewed"], 16)
        self.assertEqual(result["raw_agreement"], 1.0)
        self.assertEqual(result["status_counts"], {"concordant_provisional": 16})
        self.assertEqual(result["accepted_tasks"], 0)
        self.assertFalse(result["human_independence_verified"])
        self.assertFalse(result["task_specs_frozen"])
        self.assertEqual(result["experimental_enrollment"], "blocked")
        self.assertTrue(all(not row["accepted_task"] for row in result["records"]))

    def test_partial_review_stays_missing_instead_of_faking_labels(self):
        a, b = self.make_review("A"), self.make_review("B")
        a["decisions"].pop()
        result = audit(self.frame, self.recheck, a, b)
        self.assertEqual(result["double_reviewed"], 15)
        self.assertEqual(result["status_counts"].get("missing_independent_review"), 1)
        self.assertEqual(result["accepted_tasks"], 0)

    def test_screenable_reports_defer_when_source_unavailable(self):
        data = copy.deepcopy(self.recheck)
        data["records"][0].update({"fetch_status": "unavailable", "state": "unknown",
                                   "updated_at_utc": None, "closed_at_utc": None,
                                   "source_error": "rate_limited"})
        # Review packet hashes are bound to the modified observation.
        original = self.recheck
        self.recheck = data
        try:
            a, b = self.make_review("A"), self.make_review("B")
            result = audit(self.frame, data, a, b)
            self.assertEqual(result["status_counts"]["deferred_source_status"], 1)
            self.assertFalse(next(x for x in result["records"] if x["task_id"] == data["records"][0]["task_id"])["accepted_task"])
            self.assertEqual(sum(x["provisional_label"] == "screenable_for_spec_drafting"
                                 for x in result["records"]), 15)
        finally:
            self.recheck = original

    def test_screenable_reports_defer_on_conflicting_status(self):
        a, b = self.make_review("A"), self.make_review("B")
        b["decisions"][0]["issue_status_check"] = "closed"
        result = audit(self.frame, self.recheck, a, b)
        self.assertEqual(result["status_counts"]["deferred_source_status"], 1)
        self.assertEqual(next(x for x in result["records"] if x["task_id"] == a["decisions"][0]["task_id"])["provisional_label"], "defer_unknown")

    def test_disagreement_requires_distinct_third_and_after_time(self):
        a, b = self.make_review("A"), self.make_review("B")
        b["decisions"][0]["label"] = "exclude_candidate"
        b["decisions"][0]["reason_code"] = "scope"
        result = audit(self.frame, self.recheck, a, b)
        self.assertEqual(result["status_counts"].get("unresolved_disagreement"), 1)
        c = self.make_review("C", "defer_unknown")
        c["decisions"] = [c["decisions"][0]]
        result = audit(self.frame, self.recheck, a, b, c)
        self.assertEqual(result["status_counts"].get("adjudicated_provisional"), 1)
        self.assertEqual(result["accepted_tasks"], 0)
        bad = copy.deepcopy(c)
        bad["reviewer_ref"] = a["reviewer_ref"]
        with self.assertRaisesRegex(TaskScreenError, "adjudicator"):
            audit(self.frame, self.recheck, a, b, bad)

    def test_adjudication_on_agreement_is_rejected(self):
        a, b, c = (self.make_review("A"), self.make_review("B"),
                   self.make_review("C", "defer_unknown"))
        c["decisions"] = [c["decisions"][0]]
        with self.assertRaisesRegex(TaskScreenError, "adjudication allowed only"):
            audit(self.frame, self.recheck, a, b, c)

    def test_wrong_packet_or_reviewer_is_rejected(self):
        a, b = self.make_review("A"), self.make_review("B")
        a["packet_sha256"] = "0" * 64
        with self.assertRaisesRegex(TaskScreenError, "packet/version/slot"):
            audit(self.frame, self.recheck, a, b)
        a = self.make_review("A")
        b["reviewer_ref"] = a["reviewer_ref"]
        with self.assertRaisesRegex(TaskScreenError, "distinct"):
            audit(self.frame, self.recheck, a, b)

    def test_duplicate_or_undeclared_review_item_is_rejected(self):
        a, b = self.make_review("A"), self.make_review("B")
        a["decisions"].append(copy.deepcopy(a["decisions"][0]))
        with self.assertRaisesRegex(TaskScreenError, "duplicate"):
            audit(self.frame, self.recheck, a, b)
        a = self.make_review("A")
        a["decisions"][0]["task_id"] = "GH-not-selected"
        with self.assertRaisesRegex(TaskScreenError, "unexpected"):
            audit(self.frame, self.recheck, a, b)

    def test_bad_exclusion_reason_and_missing_evidence_rejected(self):
        a, b = self.make_review("A"), self.make_review("B")
        a["decisions"][0]["label"] = "exclude_candidate"
        with self.assertRaisesRegex(TaskScreenError, "exclusion"):
            audit(self.frame, self.recheck, a, b)
        a = self.make_review("A")
        a["decisions"][0]["evidence_ref"] = None
        with self.assertRaisesRegex(TaskScreenError, "evidence"):
            audit(self.frame, self.recheck, a, b)

    def test_cli_packet_is_write_once_and_cannot_overwrite_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "screening-packet.json"
            cmd = [sys.executable, "-m", "trending_study.task_screen", "prepare",
                   "--frame", str(FRAME), "--recheck", str(RECHECK), "--output", str(output)]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(json.loads(output.read_text())["selected_count"], 16)
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)
            self.assertIn("overwrite", second.stderr)
            alias = cmd[:-1] + [str(RECHECK)]
            third = subprocess.run(alias, capture_output=True, text=True)
            self.assertEqual(third.returncode, 2)
            self.assertIn("overlap", third.stderr)


if __name__ == "__main__":
    unittest.main()
