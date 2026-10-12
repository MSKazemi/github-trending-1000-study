"""Offline tests for observed-only visualization audit; deliberately synthetic."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from trending_study.visualize_sampling import load_observations, summarize, table_markdown

def example(name="lab/one", repo_id=None):
    row = dict(repository=name, observation_date="2026-10-11", window="daily",
               rank=1, source_sha256="a"*64, source_file="fixture.html",
               collected_at_utc="2026-10-11T09:00:00+00:00",
               trending_url="https://github.com/trending?since=daily")
    if repo_id is not None:
        row["repository_id"] = repo_id
    return row

class SamplingAuditTests(unittest.TestCase):
    def test_counts_are_observed_only(self):
        result = summarize([example(), example(), example("lab/second", 12)])
        self.assertEqual(result["observed_occurrences"], 3)
        self.assertEqual(result["distinct_displayed_names"], 2)
        self.assertEqual(result["unique_resolved_repository_ids"], 1)
        self.assertEqual(result["unresolved_displayed_names"], 1)
        self.assertIsNone(result["eligible_repository_count"])
        self.assertIn("NOT MEASURED", table_markdown(result))

    def test_renamed_repo_same_id_is_one(self):
        self.assertEqual(summarize([example("lab/old", 10), example("lab/new", 10)])["unique_resolved_repository_ids"], 1)

    def test_conflicting_ids_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "reconciliation"):
            summarize([example("lab/one", 10), example("lab/one", 11)])

    def test_malformed_provenance_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "bad.jsonl"
            for mutate in ({"source_sha256": "invalid"}, {"collected_at_utc": "2026-10-11T10:00:00"},
                           {"repository_id": "123"}, {"observation_date": "not-a-date"}):
                row = example()
                row.update(mutate)
                p.write_text(json.dumps(row) + "\n")
                with self.assertRaises(ValueError):
                    load_observations(p)

    def test_cli_writes_labeled_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source = base / "observations.jsonl"
            source.write_text(json.dumps(example()) + "\n")
            out = base / "out"
            command = [sys.executable, "-m", "trending_study.visualize_sampling", "--input",
                       str(source), "--output-dir", str(out), "--synthetic"]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("SYNTHETIC", (out / "F01_observed_sampling.svg").read_text())
            self.assertIn("NOT MEASURED", (out / "T02_observed_counts.md").read_text())
            manifest = json.loads((out / "sampling_audit.json").read_text())
            self.assertEqual(manifest["input_type"], "SYNTHETIC_FIXTURE")
            self.assertEqual(manifest["unique_resolved_repository_ids"], 0)
