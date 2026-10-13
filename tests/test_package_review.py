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

    def test_unknown_license_can_be_deferred(self):
        p = candidate()
        p["candidate"]["spdx_expression"] = None
        self.assertEqual(evaluate(p)["decision"], "defer")

    def test_license_pass_requires_spdx(self):
        p = candidate()
        p["candidate"]["spdx_expression"] = None
        p["checks"]["license_compatibility"] = {
            "status": "pass", "evidence_url": "https://example.org/evidence"}
        with self.assertRaises(PackageReviewError):
            evaluate(p)

    def test_bad_evidence_url_rejected(self):
        p = candidate()
        p["checks"]["known_advisories"] = {"status": "pass", "evidence_url": "https://"}
        with self.assertRaises(PackageReviewError):
            evaluate(p)

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


    def test_registry_url_must_match_exact_official_pypi_identity(self):
        for url in (
            "https://pypi.org.evil.test/project/fictionalpkg/1.0/",
            "https://pypi.org/project/anotherpkg/1.0/",
            "https://pypi.org/project/fictionalpkg/latest/",
            "https://pypi.org/project/fictionalpkg/2.0/",
            "https://pypi.org/project/fictionalpkg/1.0/#fragment",
        ):
            p = candidate()
            p["candidate"]["registry_url"] = url
            with self.subTest(url=url), self.assertRaises(PackageReviewError):
                evaluate(p)

    def test_moving_aliases_not_pinned_release(self):
        for version in ("latest", "main", "HEAD", ">=1.0", "1.*", "*"):
            p = candidate()
            p["candidate"]["version"] = version
            with self.subTest(version=version), self.assertRaisesRegex(PackageReviewError, "pinned"):
                evaluate(p)

    def test_spdx_sentinel_does_not_equal_approved_license(self):
        for value in ("NONE", "NOASSERTION"):
            p = candidate()
            p["candidate"]["spdx_expression"] = value
            p["checks"]["license_compatibility"] = {
                "status": "pass", "evidence_url": "https://spdx.org/licenses/"
            }
            with self.subTest(value=value), self.assertRaisesRegex(PackageReviewError, "actual SPDX"):
                evaluate(p)

    def test_future_freeze_cannot_make_future_package_available(self):
        p = candidate()
        p["task_frozen_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(PackageReviewError, "future"):
            evaluate(p)

    def test_malformed_gate_type_is_rejected(self):
        p = candidate()
        p["checks"]["known_advisories"]["status"] = []
        with self.assertRaises(PackageReviewError):
            evaluate(p)


if __name__ == "__main__":
    unittest.main()
