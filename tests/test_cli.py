import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.__main__ import extract_repos

FIXTURE = Path(__file__).parent / "fixtures" / "trending.html"


class TrendingTests(unittest.TestCase):
    def test_extract_and_deduplicate(self):
        self.assertEqual(extract_repos(FIXTURE.read_text()), ["alpha-org/first-project", "example-user/another.repo"])

    def test_no_rows_fails_closed(self):
        with self.assertRaises(ValueError):
            extract_repos('<html><a href="/owner/repo">unrelated</a></html>')

    def test_parse_command_and_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "observations.jsonl"
            cmd = [sys.executable, "-m", "trending_study", "parse-trending", "--input", str(FIXTURE), "--date", "2026-10-11", "--window", "daily", "--output", str(out)]
            result = subprocess.run(cmd, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = [json.loads(line) for line in out.read_text().splitlines()]
            self.assertEqual(len(rows), 2)
            self.assertEqual([row["rank"] for row in rows], [1, 2])
            self.assertTrue(all(len(row["source_sha256"]) == 64 for row in rows))
            summary = subprocess.run([sys.executable, "-m", "trending_study", "summarize", "--input", str(out)], text=True, capture_output=True)
            self.assertEqual(json.loads(summary.stdout)["occurrences"], 2)


if __name__ == "__main__":
    unittest.main()
