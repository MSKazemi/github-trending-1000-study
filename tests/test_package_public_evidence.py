"""Issue #22: all synthetic, offline fail-closed checks for public evidence links.

No source is fetched. This does not authenticate any package, license, human
reviewer, advisory database, host DNS, or installation approval.
"""
import unittest

from trending_study.package_review import PackageReviewError, FIELDS, evaluate
from tests.test_package_review import candidate


def all_pass():
    p = candidate()
    p["checks"] = {
        key: {"status": "pass", "evidence_url": "https://example.org/evidence"}
        for key in FIELDS
    }
    return p


class SafeEvidenceHostTests(unittest.TestCase):
    def test_private_or_local_evidence_links_refused_for_every_status(self):
        blocked = (
            "https://localhost/notice", "https://run.localhost/notice",
            "https://registry.local/notice", "https://security.internal/report",
            "https://metadata.google.internal/latest/meta-data/",
            "https://127.0.0.1/internal", "https://127.4.5.6/internal",
            "https://10.20.30.40/internal", "https://172.16.8.1/internal",
            "https://192.168.1.2/internal", "https://169.254.169.254/latest/",
            "https://100.64.0.1/notice", "https://0.0.0.0/internal",
            "https://[::1]/secret", "https://[fe80::1]/hidden",
            "https://[fc00::1]/report", "https://[::ffff:127.0.0.1]/",
            "https://domain.example.org./notice",
        )
        for status in ("pass", "unknown", "fail"):
            for url in blocked:
                with self.subTest(status=status, url=url):
                    p = candidate()
                    p["checks"]["known_advisories"] = {
                        "status": status, "evidence_url": url,
                    }
                    with self.assertRaisesRegex(PackageReviewError, "public evidence host"):
                        evaluate(p)

    def test_public_https_well_formed_source_still_possible(self):
        p = all_pass()
        self.assertEqual(evaluate(p)["decision"], "review_ready")
        self.assertFalse(evaluate(p)["automatic_install_approved"])
        p["checks"]["known_advisories"]["evidence_url"] = (
            "https://[2001:4860:4860::8888]/resource"
        )
        self.assertEqual(evaluate(p)["decision"], "review_ready")

    def test_non_pypi_registry_private_is_rejected_before_defer(self):
        p = candidate()
        p["candidate"].update(
            ecosystem="npm", registry_url="https://127.0.0.1/package",
        )
        with self.assertRaisesRegex(PackageReviewError, "public evidence host"):
            evaluate(p)


class SentinelLicenseTests(unittest.TestCase):
    def test_none_or_noassertion_anywhere_forbids_license_pass(self):
        for value in (
            "NONE", "NOASSERTION", "(MIT OR NOASSERTION)",
            "MIT AND NONE", "(MIT AND NOASSERTION)",
            "None OR Apache-2.0",
        ):
            with self.subTest(value=value):
                p = all_pass()
                p["candidate"]["spdx_expression"] = value
                with self.assertRaisesRegex(PackageReviewError, "actual SPDX"):
                    evaluate(p)

    def test_license_reference_containing_none_is_not_automatically_rejected(self):
        p = all_pass()
        p["candidate"]["spdx_expression"] = "LicenseRef-NONE"
        # LicenseRef is structurally accepted, but NOT a verified license grant.
        self.assertEqual(evaluate(p)["decision"], "review_ready")
        self.assertFalse(evaluate(p)["automatic_install_approved"])

    def test_multiline_and_unbounded_license_field_fails_closed(self):
        for value in ("MIT\nAND Apache-2.0", "MIT\rNOASSERTION", "X" * 513):
            p = candidate()
            p["candidate"]["spdx_expression"] = value
            with self.subTest(value=repr(value[:40])):
                with self.assertRaisesRegex(PackageReviewError, "single-line"):
                    evaluate(p)

    def test_unknown_license_still_deferred_instead_of_zero(self):
        p = all_pass()
        p["candidate"]["spdx_expression"] = None
        p["checks"]["license_compatibility"] = {"status": "unknown"}
        self.assertEqual(evaluate(p)["decision"], "defer")


if __name__ == "__main__":
    unittest.main()
