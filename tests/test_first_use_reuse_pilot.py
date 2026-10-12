"""One synthetic, offline first-use task for an existing public repository.

This is an *engineering smoke test*, authored within the project. It is not
an independent human usability experiment or a randomized reuse/build trial.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.reuse_gate import evaluate


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "trending.html"
ASSESSMENT = ROOT / "examples" / "first_use_reuse_pilot.example.json"
EXPECTED = ["alpha-org/first-project", "example-user/another.repo"]


def run_cli(*args):
    """Use only this project's fixed CLI; never execute a discovered package."""
    return subprocess.run(
        [sys.executable, "-m", "trending_study", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )


class FirstUseReusePilotTests(unittest.TestCase):
    def test_existing_cli_solves_synthetic_task_without_fake_capture_provenance(self):
        original = FIXTURE.read_bytes()
        source_hash = hashlib.sha256(original).hexdigest()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "parsed.jsonl"
            parsed = run_cli(
                "parse-trending",
                "--input", str(FIXTURE),
                "--date", "2026-10-12",  # Metadata supplied by operator, NOT capture evidence
                "--window", "daily",
                "--output", str(output),
            )
            self.assertEqual(parsed.returncode, 0, parsed.stderr)
            rows = [json.loads(line) for line in output.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([r["repository"] for r in rows], EXPECTED)
            self.assertEqual([r["rank"] for r in rows], [1, 2])
            self.assertTrue(all(r["source_sha256"] == source_hash for r in rows))
            self.assertTrue(all(r["capture_time_status"] == "unverified_parse_only" for r in rows))
            self.assertTrue(all(r["eligible_for_confirmatory_cohort"] is False for r in rows))
            self.assertTrue(all(r["observation_date"] == "2026-10-12" for r in rows))
            self.assertTrue(all(r["window"] == "daily" for r in rows))
            self.assertTrue(all("parsed_at_utc" in r for r in rows))
            summary = run_cli("summarize", "--input", str(output))
            self.assertEqual(summary.returncode, 0, summary.stderr)
            counts = json.loads(summary.stdout)
            self.assertEqual(counts["occurrences"], 2)
            self.assertEqual(counts["distinct_repository_names"], 2)
        self.assertEqual(FIXTURE.read_bytes(), original)

    def test_existing_output_fails_closed_without_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "already-present.jsonl"
            protected_bytes = b"research record: must not overwrite\n"
            output.write_bytes(protected_bytes)
            result = run_cli(
                "parse-trending",
                "--input", str(FIXTURE),
                "--date", "2026-10-12",
                "--window", "daily",
                "--output", str(output),
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_bytes(), protected_bytes)

    def test_malformed_row_is_rejected_without_publishing_partial_data(self):
        with tempfile.TemporaryDirectory() as directory:
            broken = Path(directory) / "malformed.html"
            broken.write_text(
                "<html><article class='Box-row'><h2>Missing repository link</h2>"
                "</article></html>", encoding="utf-8",
            )
            output = Path(directory) / "should-not-exist.jsonl"
            result = run_cli(
                "parse-trending",
                "--input", str(broken),
                "--date", "2026-10-12",
                "--window", "daily",
                "--output", str(output),
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

    def test_reuse_gate_requires_review_instead_of_approving_self_assessment(self):
        assessment = json.loads(ASSESSMENT.read_text(encoding="utf-8"))
        self.assertEqual(assessment["schema_version"], "1.0")
        self.assertEqual(len(assessment["candidates"]), 1)
        result = evaluate(assessment)
        self.assertEqual(result["next_action"], "verify_existing_candidates")
        self.assertEqual(result["self_reported_qualified"], [])
        self.assertEqual(result["candidate_count"], 1)
        self.assertTrue(all(
            assessment["candidates"][0][key] == "unknown"
            for key in ("functional_test", "license_compatibility",
                        "security_review", "maintenance_review")
        ))


if __name__ == "__main__":
    unittest.main()
