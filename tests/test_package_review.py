"""Strict synthetic self-declared supply-chain tests, no package execution."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from trending_study.package_review import FIELDS, PackageReviewError, evaluate, evaluate_file, main


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

    def test_registry_url_rejects_hidden_parameters_and_malformed_authorities(self):
        # urllib.parse silently removes newlines and separates ;params from
        # path. Both behaviors can make a malformed URL appear to be official.
        for url in (
            "https://pypi.org/project/fictionalpkg/1.0/;unreviewed",
            "https://pypi.org:invalid/project/fictionalpkg/1.0/",
            "https://pypi.org:65536/project/fictionalpkg/1.0/",
            "https://[malformed/project/fictionalpkg/1.0/",
            "https://pypi.org/project/fictionalpkg/1.0/" + chr(10),
            " https://pypi.org/project/fictionalpkg/1.0/",
            "https://pypi.org:/project/fictionalpkg/1.0/",
        ):
            p = candidate()
            p["candidate"]["registry_url"] = url
            with self.subTest(url=repr(url)), self.assertRaises(PackageReviewError):
                evaluate(p)

    def test_passing_evidence_url_cannot_hide_tokens_or_invalid_port(self):
        p = candidate()
        p["checks"]["known_advisories"] = {
            "status": "pass", "evidence_url": "https://security.example.org/advisory"
        }
        self.assertEqual(evaluate(p)["decision"], "defer")
        for url in (
            "https://security.example.org/advisory?token=private",
            "https://security.example.org/advisory;hidden",
            "https://security.example.org:invalid/advisory",
            "https://security.example.org:65536/advisory",
            "https://[broken/issue",
            "https://security.example.org/one" + chr(10) + "two",
        ):
            p["checks"]["known_advisories"]["evidence_url"] = url
            with self.subTest(url=repr(url)), self.assertRaises(PackageReviewError):
                evaluate(p)

    def test_unexpected_root_candidate_and_gate_fields_fail_closed(self):
        for level in ("root", "candidate", "gate"):
            p = candidate()
            if level == "root":
                p["private_prompt_text"] = "should-not-be-accepted"
            elif level == "candidate":
                p["candidate"]["private_registry_token"] = "should-not-be-accepted"
            else:
                p["checks"]["known_advisories"]["private_key"] = "should-not-be-accepted"
            with self.subTest(level=level), self.assertRaises(PackageReviewError):
                evaluate(p)

    def test_failure_or_unknown_evidence_url_also_rejects_secrets(self):
        for status in ("fail", "unknown"):
            p = candidate()
            p["checks"]["known_advisories"] = {
                "status": status, "evidence_url": "https://vendor.example.test/notice?token=private"
            }
            with self.subTest(status=status), self.assertRaises(PackageReviewError):
                evaluate(p)
            p["checks"]["known_advisories"]["evidence_url"] = (
                "https://vendor.example.test/notice")
            result = evaluate(p)
            self.assertEqual(result["decision"], "reject" if status == "fail" else "defer")
            self.assertFalse(result["automatic_install_approved"])

    def test_null_evidence_url_means_unknown_on_nonpassing_gates(self):
        # Regression: on main, {"status": "unknown", "evidence_url": null}
        # deferred; null is this repository's explicit "unknown" value.
        for status, decision in (("unknown", "defer"), ("fail", "reject")):
            p = candidate()
            p["checks"]["known_advisories"] = {"status": status, "evidence_url": None}
            with self.subTest(status=status):
                result = evaluate(p)
                self.assertEqual(result["decision"], decision)
                self.assertFalse(result["automatic_install_approved"])
        p = candidate()
        p["checks"]["known_advisories"] = {"status": "pass", "evidence_url": None}
        with self.assertRaisesRegex(PackageReviewError, "evidence_url"):
            evaluate(p)
        for unsafe in ("", "http://vendor.example.test/notice", 0, False):
            p["checks"]["known_advisories"] = {"status": "unknown", "evidence_url": unsafe}
            with self.subTest(unsafe=repr(unsafe)), self.assertRaises(PackageReviewError):
                evaluate(p)

    def test_explicit_port_zero_rejected_for_every_https_url(self):
        for status in ("pass", "unknown"):
            p = candidate()
            p["checks"]["known_advisories"] = {
                "status": status, "evidence_url": "https://vendor.example.test:0/notice"}
            with self.subTest(status=status), self.assertRaisesRegex(
                    PackageReviewError, "evidence_url"):
                evaluate(p)
        p = candidate()
        p["candidate"].update(ecosystem="npm",
                              registry_url="https://registry.example.test:0/fictionalpkg/1.0")
        with self.assertRaisesRegex(PackageReviewError, "registry_url"):
            evaluate(p)
        # A valid nondefault port is still structurally acceptable.
        p["candidate"]["registry_url"] = "https://registry.example.test:8443/fictionalpkg/1.0"
        self.assertEqual(evaluate(p)["decision"], "defer")

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

    def test_pypi_url_rejects_escaped_or_unicode_name_aliases(self):
        # urllib.parse.unquote plus Unicode casefold can otherwise turn the
        # long-s character into ASCII 's', falsely binding another URL path.
        cases = (
            ("fictionalpkg", "%66ictionalpkg"),
            ("safety", "%C5%BFafety"),
            ("fictionalpkg", "fictional%2Fpkg"),
            ("fictionalpkg", "fictionalpkg%00"),
            ("fictionalpkg", "fictionalpkg\u200d"),
        )
        for declared, url_segment in cases:
            p = candidate()
            p["candidate"]["package_name"] = declared
            p["candidate"]["registry_url"] = (
                "https://pypi.org/project/" + url_segment + "/1.0/"
            )
            with self.subTest(segment=url_segment), self.assertRaisesRegex(
                    PackageReviewError, "literal ASCII"):
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

    def test_equivalent_pypi_name_normalization_binds_url_and_purl(self):
        for name in ("Fictional__Pkg", "fictional..pkg", "fictional-_.pkg"):
            p = candidate()
            p["candidate"]["package_name"] = name
            p["candidate"]["registry_url"] = "https://pypi.org/project/fictional-pkg/1.0/"
            p["candidate"]["purl"] = "pkg:pypi/fictional-pkg@1.0"
            with self.subTest(name=name):
                result = evaluate(p)
                self.assertEqual(result["decision"], "defer")
                self.assertFalse(result["automatic_install_approved"])


class PackageReviewInputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "review.json"

    def run_cli(self):
        return subprocess.run(
            [sys.executable, "-m", "trending_study.package_review",
             "--input", str(self.path)], capture_output=True, text=True, timeout=5)

    def test_duplicate_gate_cannot_silently_replace_failure_with_pass(self):
        p = candidate()
        p["checks"] = {k: {"status": "pass", "evidence_url": "https://example.org/evidence"}
                       for k in FIELDS}
        self.path.write_text(json.dumps(p).replace(
            '"status": "pass"', '"status": "fail", "status": "pass"', 1))
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("strict UTF-8 JSON", result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("Traceback", result.stderr)

    def test_cli_rejects_nonstandard_and_nonfinite_numbers(self):
        for number in ("NaN", "Infinity", "-Infinity", "1e999", "1e-999"):
            self.path.write_text(json.dumps(candidate())[:-1] + ', "extra": ' + number + '}')
            with self.subTest(number=number):
                result = self.run_cli()
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)

    def test_valid_file_retains_explicit_review_limits(self):
        self.path.write_text(json.dumps(candidate()))
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(output["decision"], "defer")
        self.assertTrue(output["source_checks_self_declared"])
        self.assertFalse(output["automatic_install_approved"])

    def test_cli_rejects_deep_json_without_traceback(self):
        self.path.write_text("[" * 20000 + "0" + "]" * 20000)
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("Traceback", result.stderr)

    def test_decoder_diagnostics_do_not_expose_private_keys_or_filename(self):
        self.path = self.path.with_name("PRIVATE-synthetic-personal-filename.json")
        self.path.write_text(
            '{"PRIVATE-synthetic-credential-field":1,"PRIVATE-synthetic-credential-field":2}')
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("strict UTF-8 JSON", result.stderr)
        self.assertNotIn("PRIVATE", result.stderr)
        self.assertNotIn(str(self.path), result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_decoder_recursion_failure_has_portable_private_error_contract(self):
        self.path.write_text(json.dumps(candidate()))
        with patch("trending_study.data_integrity.decode_research_json",
                   side_effect=RecursionError("PRIVATE-synthetic-decoder-context")):
            with self.assertRaises(PackageReviewError) as raised:
                evaluate_file(self.path)
            self.assertIn("strict UTF-8 JSON", str(raised.exception))
            self.assertNotIn("PRIVATE", str(raised.exception))
            self.assertTrue(raised.exception.__suppress_context__)

    def test_symlink_input_is_rejected(self):
        target = Path(self.temp.name) / "target.json"
        target.write_text(json.dumps(candidate()))
        self.path.symlink_to(target)
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("regular non-symlink file", result.stderr)

    def test_directory_input_is_rejected_without_traceback(self):
        self.path.mkdir()
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO input requires POSIX")
    def test_fifo_input_is_rejected_without_waiting_for_a_writer(self):
        os.mkfifo(self.path)
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn("regular non-symlink file", result.stderr)

    def test_file_byte_limit_rejects_before_evaluation(self):
        self.path.write_text(json.dumps(candidate()))
        with patch("trending_study.package_review.MAX_FILE_BYTES", 16), \
             patch("trending_study.package_review.evaluate") as evaluator:
            with self.assertRaises(SystemExit) as raised:
                main(["--input", str(self.path)])
            self.assertEqual(raised.exception.code, 2)
            evaluator.assert_not_called()


if __name__ == "__main__":
    unittest.main()
