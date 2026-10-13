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

    def test_unknown_artifact_digest_stays_unknown_and_never_approves(self):
        p = candidate()
        p["candidate"]["artifact_sha256"] = None
        self.assertEqual(evaluate(p)["decision"], "defer")
        p["checks"] = {
            k: {"status": "pass", "evidence_url": "https://example.org/evidence"}
            for k in FIELDS
        }
        result = evaluate(p)
        self.assertEqual(result["decision"], "defer")
        self.assertIn("artifact_sha256", result["unknown_checks"])
        self.assertFalse(result["automatic_install_approved"])

    def test_missing_digest_field_requires_explicit_unknown(self):
        p = candidate()
        del p["candidate"]["artifact_sha256"]
        with self.assertRaisesRegex(PackageReviewError, "explicitly known or null"):
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

    def test_versions_containing_letters_t_or_n_are_not_rejected(self):
        # Regression: an escaped '\\t\\n' character class accidentally
        # rejected ordinary letters in valid pinned release identifiers.
        for version in ("1.0.post1", "1.2.0-nightly.1"):
            with self.subTest(version=version):
                p = candidate()
                p["candidate"]["version"] = version
                p["candidate"]["registry_url"] = (
                    f"https://pypi.org/project/fictionalpkg/{version}/"
                )
                result = evaluate(p)
                self.assertEqual(result["decision"], "defer")
                self.assertFalse(result["automatic_install_approved"])

    def test_whitespace_and_selectors_are_not_pinned_versions(self):
        for version in ("1.0\\t2", "1.0\\n2", "1.0 2", "1.0/2", "1.0,2",
                        "1.0||2", "^1.0", "1.*", ">=1.0", "latest", "stable"):
            with self.subTest(version=repr(version)):
                p = candidate()
                p["candidate"]["version"] = version
                with self.assertRaisesRegex(PackageReviewError, "pinned"):
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

    def test_temporal_reject_never_bypasses_complete_evidence_validation(self):
        p = candidate()
        p["candidate"]["first_available_at_utc"] = "2027-01-01T00:00:00Z"
        del p["checks"]["functional_fit"]
        with self.assertRaisesRegex(PackageReviewError, "every evidence check"):
            evaluate(p)
        p["checks"]["functional_fit"] = {"status": "pass"}
        with self.assertRaisesRegex(PackageReviewError, "evidence_url"):
            evaluate(p)
        p["checks"]["functional_fit"] = {"status": "unknown"}
        result = evaluate(p)
        self.assertEqual(result["decision"], "reject")
        self.assertIn("temporal_availability", result["failed_checks"])
        self.assertIn("functional_fit", result["unknown_checks"])

    def test_unbound_registry_never_reports_review_ready(self):
        p = candidate()
        p["candidate"]["ecosystem"] = "npm"
        p["candidate"]["registry_url"] = "https://registry.npmjs.org/fictionalpkg"
        p["checks"] = {k: {"status": "pass", "evidence_url": "https://example.org/evidence"}
                       for k in FIELDS}
        result = evaluate(p)
        self.assertEqual(result["decision"], "defer")
        self.assertIn("official_registry_identity_binding", result["unknown_checks"])
        self.assertFalse(result["automatic_install_approved"])
        p["checks"]["known_advisories"]["status"] = "fail"
        self.assertEqual(evaluate(p)["decision"], "reject")

    def test_pypi_name_must_be_canonical_safe_registry_segment(self):
        for name in ("../fictionalpkg", "fictional/pkg", "fictional%2fpkg", "name?version"):
            p = candidate()
            p["candidate"]["package_name"] = name
            with self.subTest(name=name), self.assertRaisesRegex(
                    PackageReviewError, "PyPI package_name"):
                evaluate(p)

    def test_malformed_gate_type_is_rejected(self):
        p = candidate()
        p["checks"]["known_advisories"]["status"] = []
        with self.assertRaises(PackageReviewError):
            evaluate(p)


    def test_optional_exact_package_url_and_source_commit(self):
        p = candidate()
        p["candidate"]["purl"] = "pkg:pypi/fictionalpkg@1.0"
        p["candidate"]["source_commit"] = "a" * 40
        out = evaluate(p)
        self.assertEqual(out["decision"], "defer")
        self.assertFalse(out["automatic_install_approved"])

    def test_package_url_identity_mismatch_rejected(self):
        for purl in ("pkg:pypi/different@1.0", "pkg:pypi/fictionalpkg@2.0",
                     "pkg:npm/fictionalpkg@1.0", "pkg:pypi/fictionalpkg@latest",
                     "https://pypi.org/project/fictionalpkg/1.0/"):
            p = candidate()
            p["candidate"]["purl"] = purl
            with self.subTest(purl=purl), self.assertRaises(PackageReviewError):
                evaluate(p)

    def test_optional_source_commit_must_be_pinned_sha(self):
        for commit in ("main", "abc123", "", "A" * 40, 123):
            p = candidate()
            p["candidate"]["source_commit"] = commit
            with self.subTest(commit=commit), self.assertRaises(PackageReviewError):
                evaluate(p)


if __name__ == "__main__":
    unittest.main()
