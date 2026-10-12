"""Strict synthetic self-declared supply-chain tests, no package execution."""
import unittest
from trending_study.package_review import FIELDS, PackageReviewError, evaluate


def candidate():
    return {"candidate": {
                "ecosystem": "pypi", "package_name": "fictionalpkg",
                "version": "1.0", "spdx_expression": "MIT",
                "registry_url": "https://pypi.org/project/fictionalpkg/1.0/",
                "artifact_sha256": "a"*64, "first_available_at_utc": "2026-01-01T00:00:00Z"},
            "task_frozen_at_utc": "2026-10-12T00:00:00Z",
            "checks": {k: {"status": "unknown"} for k in FIELDS}}


class PackageReviewTests(unittest.TestCase):
    def test_all_unknown_deferred_never_approved(self):
        r = evaluate(candidate())
        self.assertEqual(r["decision"], "defer")
        self.assertFalse(r["automatic_install_approved"])

    def test_temporally_impossible_release(self):
        p = candidate()
        p["candidate"]["first_available_at_utc"] = "2027-10-12T00:00:00Z"
        self.assertEqual(evaluate(p)["decision"], "reject")

    def test_failed_license_rejected(self):
        p = candidate()
        p["checks"]["license_compatibility"]["status"] = "fail"
        self.assertEqual(evaluate(p)["decision"], "reject")

    def test_all_pass_still_requires_independent_review(self):
        p = candidate()
        p["checks"] = {k: {"status": "pass", "evidence_url": "https://example.org/evidence"}
                       for k in FIELDS}
        r = evaluate(p)
        self.assertEqual(r["decision"], "review_ready")
        self.assertFalse(r["automatic_install_approved"])

    def test_invalid_digest_rejected(self):
        p = candidate()
        p["candidate"]["artifact_sha256"] = "not-a-digest"
        with self.assertRaises(PackageReviewError):
            evaluate(p)

    def test_unsubstantiated_pass_rejected(self):
        p = candidate()
        p["checks"]["known_advisories"] = {"status": "pass"}
        with self.assertRaises(PackageReviewError):
            evaluate(p)

    def test_missing_field_fails_closed(self):
        p = candidate()
        del p["checks"]["functional_fit"]
        with self.assertRaises(PackageReviewError):
            evaluate(p)


if __name__ == "__main__":
    unittest.main()
