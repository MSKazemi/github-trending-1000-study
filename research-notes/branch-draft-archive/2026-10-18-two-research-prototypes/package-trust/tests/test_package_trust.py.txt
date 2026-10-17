import copy
import json
from pathlib import Path
import unittest

from trending_study.package_trust import PackageTrustError, evaluate

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "package_trust.synthetic.json"


class PackageTrustTests(unittest.TestCase):
    def load(self):
        return json.loads(EXAMPLE.read_text())

    def test_unknown_never_install(self):
        out = evaluate(self.load())
        self.assertEqual(out["candidates"][0]["decision"], "review_required")
        self.assertFalse(out["auto_install_allowed"])
        self.assertFalse(out["independently_verified"])

    def test_failed_gate_blocks(self):
        doc = self.load()
        doc["candidates"][0]["gates"]["license"] = "fail"
        self.assertEqual(evaluate(doc)["candidates"][0]["decision"], "block_candidate")

    def test_unsubstantiated_pass_rejected(self):
        doc = self.load()
        doc["candidates"][0]["gates"]["identity"] = "pass"
        with self.assertRaises(PackageTrustError):
            evaluate(doc)

    def test_all_pass_still_needs_independent_review(self):
        doc = self.load()
        for gate in doc["candidates"][0]["gates"]:
            doc["candidates"][0]["gates"][gate] = "pass"
            doc["candidates"][0]["evidence"][gate] = "https://example.invalid/evidence"
        out = evaluate(doc)
        self.assertEqual(out["candidates"][0]["decision"], "ready_for_independent_review")
        self.assertFalse(out["auto_install_allowed"])

    def test_malformed_version_and_sha(self):
        for key, value in (("purl", "pkg:pypi/synthetic-example"),
                           ("source_commit", "deadbeef"),
                           ("captured_at_utc", "2026-10-12T22:00:00+02:00")):
            doc = self.load()
            doc["candidates"][0][key] = value
            with self.assertRaises(PackageTrustError):
                evaluate(doc)

    def test_duplicate_package(self):
        doc = self.load()
        doc["candidates"].append(copy.deepcopy(doc["candidates"][0]))
        with self.assertRaises(PackageTrustError):
            evaluate(doc)


if __name__ == "__main__":
    unittest.main()
