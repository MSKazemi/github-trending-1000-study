"""Issue #19: strict local gold-pool JSON and malformed ranking guards.

All labels are synthetic. Passing these tests does not authenticate actual
retrieval, source availability, human reviewers, or software reuse.
"""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tests.test_goldset import DATA
from trending_study.goldset import GoldsetError, evaluate


class GoldsetMalformedMetadataTests(unittest.TestCase):
    def test_rank_ids_must_be_scalar_strings_before_duplicate_check(self):
        for item in ([1], [True], [None], [[]], [{}], [""]):
            with self.subTest(item=item):
                d = copy.deepcopy(DATA)
                d["tasks"][0]["systems"][0]["ranked_candidate_ids"] = item
                with self.assertRaisesRegex(GoldsetError, "nonempty strings"):
                    evaluate(d)

    def test_final_label_and_gate_status_reject_unhashable_json(self):
        for bad in ([], {}, ["viable"]):
            with self.subTest(bad=bad):
                d = copy.deepcopy(DATA)
                d["tasks"][0]["candidates"][0]["final_label"] = bad
                with self.assertRaisesRegex(GoldsetError, "final_label"):
                    evaluate(d)
                d = copy.deepcopy(DATA)
                d["tasks"][0]["candidates"][0]["gates"]["security"] = bad
                with self.assertRaisesRegex(GoldsetError, "gate security"):
                    evaluate(d)
                d = copy.deepcopy(DATA)
                d["tasks"][0]["candidates"][0]["gates"]["availability"] = bad
                with self.assertRaisesRegex(GoldsetError, "availability"):
                    evaluate(d)

    def test_existing_synthetic_scores_unchanged(self):
        a = evaluate(DATA, k=2)["results"][0]
        self.assertEqual(a["systems"][0]["precision_at_k"], 0.5)
        self.assertIsNone(a["systems"][1]["precision_at_k"])
        self.assertEqual(a["systems"][1]["unjudged_at_k"], 1)
        self.assertEqual(a["observed_opportunity"], "viable_found_in_audited_pool")


class GoldsetStrictCLIInputs(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.source = Path(self.tmp.name) / "evidence.json"

    def run_cli(self):
        return subprocess.run(
            [sys.executable, "-m", "trending_study.goldset",
             "--input", str(self.source), "--k", "2"],
            capture_output=True, text=True, timeout=8,
        )

    def test_duplicate_json_keys_fail_closed_instead_of_last_value_wins(self):
        self.source.write_text('{"PRIVATE-BAD-KEY":false,"PRIVATE-BAD-KEY":true}')
        proc = self.run_cli()
        self.assertEqual(proc.returncode, 2)
        self.assertIn("invalid or unsafe", proc.stderr)
        self.assertNotIn("PRIVATE-BAD-KEY", proc.stderr)
        self.assertNotIn(str(self.source), proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)
        self.assertEqual(proc.stdout, "")

    def test_nonstandard_and_overflowing_number_rejected(self):
        for literal in ("NaN", "Infinity", "-Infinity", "1e999", "1e-999"):
            self.source.write_text('{"unverified":'+literal+'}')
            with self.subTest(literal=literal):
                proc = self.run_cli()
                self.assertEqual(proc.returncode, 2)
                self.assertIn("invalid or unsafe", proc.stderr)
                self.assertEqual(proc.stdout, "")

    def test_file_above_limit_refused_without_reading_payload(self):
        self.source.write_bytes(b" " * 1_000_001)
        proc = self.run_cli()
        self.assertEqual(proc.returncode, 2)
        self.assertIn("invalid or unsafe", proc.stderr)
        self.assertEqual(proc.stdout, "")

    def test_symlink_and_directory_refused(self):
        original = Path(self.tmp.name) / "private-original.json"
        original.write_text(json.dumps(DATA))
        self.source.symlink_to(original)
        proc = self.run_cli()
        self.assertEqual(proc.returncode, 2)
        self.assertIn("invalid or unsafe", proc.stderr)
        self.assertEqual(proc.stdout, "")
        self.source.unlink()
        self.source.mkdir()
        proc = self.run_cli()
        self.assertEqual(proc.returncode, 2)
        self.assertIn("invalid or unsafe", proc.stderr)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "POSIX FIFO only")
    def test_fifo_refused_without_hanging(self):
        os.mkfifo(self.source)
        proc = self.run_cli()
        self.assertEqual(proc.returncode, 2)
        self.assertIn("invalid or unsafe", proc.stderr)

    def test_existing_offline_fixture_still_scored(self):
        self.source.write_text(json.dumps(DATA))
        proc = self.run_cli()
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["task_count"], 1)
        self.assertEqual(out["results"][0]["systems"][0]["precision_at_k"], 0.5)


if __name__ == "__main__":
    unittest.main()
