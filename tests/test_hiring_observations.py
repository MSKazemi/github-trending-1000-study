"""Prospective contract regression checks; all observations and evidence are synthetic."""
import copy
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from trending_study import hiring_observations as instrument

EXAMPLE = Path(__file__).resolve().parents[1] / "examples/hiring_observations.synthetic.json"


def fixture():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))


class ObservationLedgerTests(unittest.TestCase):
    def test_locations_share_identity_all_revisions_and_attempts_preserved(self):
        data = fixture()
        before = copy.deepcopy(data)
        report = instrument.audit(data)
        self.assertEqual(data, before)
        self.assertEqual(report["observation_attempts"], 9)
        self.assertEqual(report["unique_requisition_keys"], 3)
        self.assertEqual(report["missing_attempts"], 4)
        self.assertEqual(report["by_source"][0]["missing_attempts"], 4)
        a, b, c = report["requisitions"]
        self.assertEqual(a["location_variant_ids"], ["REMOTE", "SF"])
        self.assertEqual(a["observation_attempts"], 6)
        self.assertEqual(a["status_or_content_revision_count"], 4)
        self.assertEqual(a["first_observed_at_utc"], data["observations"][0]["observed_at_utc"])
        self.assertEqual(a["last_observed_at_utc"], data["observations"][5]["observed_at_utc"])
        self.assertEqual(a["observations"], data["observations"][:6])
        self.assertTrue(a["right_censored"])
        self.assertEqual(a["censoring_at_utc"], a["last_listed_observation_at_utc"])
        self.assertEqual(b["observations"][0]["linkage_status"], "unconfirmed")
        self.assertEqual(b["observations"][1]["linkage_status"], "known")
        self.assertIsNone(c["right_censored"])
        self.assertIsNone(c["first_listed_observation_at_utc"])
        for row in report["requisitions"]:
            self.assertIsNone(row["filled_positions"])
            self.assertIsNone(row["actual_closure_at_utc"])
        for field in ("source_access_approved", "human_methods_approved",
                      "eligible_for_confirmatory_cohort", "independent_verification"):
            self.assertFalse(report[field])

    def test_explicit_close_is_observed_not_a_filled_job_or_precise_close_time(self):
        data = fixture()
        data["observations"] = data["observations"][:5]
        report = instrument.audit(data)["requisitions"][0]
        self.assertFalse(report["right_censored"])
        self.assertEqual(report["last_observed_source_status"], "inaccessible")
        self.assertIsNone(report["actual_closure_at_utc"])
        self.assertIsNone(report["filled_positions"])

    def test_disappearance_is_missing_and_censored_at_last_live_not_study_end(self):
        for status, reason, http in (("inaccessible", "content_unavailable", 403),
                                     ("removed_or_redirected", "redirect", 302),
                                     ("not_listed_in_bounded_search", "search_miss", 200)):
            with self.subTest(status=status):
                data = fixture()
                data["observations"] = data["observations"][:3]
                data["observations"][-1].update(source_status=status, missing_reason=reason, http_status=http)
                report = instrument.audit(data)["requisitions"][0]
                self.assertTrue(report["right_censored"])
                self.assertNotEqual(report["censoring_at_utc"], report["observation_window_end_utc"])
                self.assertEqual(report["missing_attempts"], 1)

    def test_posted_date_is_explicit_separate_never_first_observation(self):
        data = fixture()
        data["observations"][0].update(posted_at_utc="2025-12-01T00:00:00Z", posting_date_basis="explicit_employer")
        report = instrument.audit(data)["requisitions"][0]
        self.assertEqual(report["first_observed_at_utc"], "2026-01-02T12:00:00Z")
        self.assertEqual(report["observations"][0]["posted_at_utc"], "2025-12-01T00:00:00Z")

    def test_no_future_backdating_or_delayed_historical_reconstruction(self):
        for fields in (
            {"observed_at_utc": "2100-01-01T00:00:00Z", "accessed_at_utc": "2100-01-01T00:00:00Z"},
            {"observed_at_utc": "2025-12-01T00:00:00Z"},
            {"accessed_at_utc": "2026-01-03T00:00:00Z"},
            {"recorded_at_utc": "2026-01-02T12:05:01Z"},
            {"recorded_at_utc": "2026-01-02T11:59:59Z"},
            {"observed_at_utc": "2026-01-02T13:00:00+01:00"},
        ):
            data = fixture()
            data["observations"][0].update(fields)
            with self.subTest(fields=fields), self.assertRaises(instrument.HiringObservationError):
                instrument.audit(data)

    def test_window_range_and_prospective_declaration(self):
        for key, value in (("declared_at_utc", "2026-01-03T00:00:00Z"),
                           ("study_end_utc", "2025-01-01T00:00:00Z"),
                           ("study_end_utc", "2028-01-01T00:00:00Z"),
                           ("analysis_as_of_utc", "2100-01-01T00:00:00Z"),
                           ("analysis_as_of_utc", "2026-01-02T11:00:00Z")):
            data = fixture(); data[key] = value
            with self.subTest(key=key), self.assertRaises(instrument.HiringObservationError):
                instrument.audit(data)

    def test_duplicate_observation_and_source_alias_and_requisition_alias(self):
        data = fixture(); data["observations"][1]["observation_id"] = data["observations"][0]["observation_id"]
        with self.assertRaises(instrument.HiringObservationError): instrument.audit(data)
        data = fixture(); data["sources"].append(dict(data["sources"][0], source_id="ALIAS"))
        with self.assertRaises(instrument.HiringObservationError): instrument.audit(data)
        data = fixture(); data["observations"][1]["requisition_id"] = "OTHER"
        data["observations"][1]["canonical_url"] = data["observations"][0]["canonical_url"]
        with self.assertRaises(instrument.HiringObservationError): instrument.audit(data)
        data = fixture(); data["observations"][1]["location_variant_id"] = "SF"
        with self.assertRaises(instrument.HiringObservationError): instrument.audit(data)

    def test_unknown_identity_invalid_source_employer_and_http_range(self):
        for key, value in (("source_id", "OTHER"), ("employer_id", "OTHER"),
                           ("requisition_id", None), ("http_status", True),
                           ("http_status", 0), ("http_status", 600),
                           ("source_status", "filled"), ("missing_reason", "unknown")):
            data = fixture(); data["observations"][0][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(instrument.HiringObservationError):
                instrument.audit(data)

    def test_reopening_required_even_after_intervening_inaccessibility(self):
        data = fixture(); data["observations"][5].update(relation_kind="none", linkage_status="none",
                                                      linked_requisition_id=None, link_evidence_ref=None)
        with self.assertRaisesRegex(instrument.HiringObservationError, "reopening"):
            instrument.audit(data)

    def test_linkage_known_requires_evidence_uncertainty_is_not_known(self):
        for index, fields in ((5, {"link_evidence_ref": None}),
                              (6, {"link_evidence_ref": "FALSE_EVIDENCE"}),
                              (6, {"linked_requisition_id": "MISSING"}),
                              (6, {"linked_requisition_id": "REQ_B"}),
                              (5, {"linked_requisition_id": "REQ_B"})):
            data = fixture(); data["observations"][index].update(fields)
            with self.subTest(index=index, fields=fields), self.assertRaises(instrument.HiringObservationError):
                instrument.audit(data)

    def test_past_closure_cannot_support_repeated_reopening_while_already_live(self):
        data = fixture()
        repeated = dict(data["observations"][5], observation_id="REPEAT_REOPEN",
                        observed_at_utc="2026-01-10T12:00:00Z",
                        accessed_at_utc="2026-01-10T12:00:00Z",
                        recorded_at_utc="2026-01-10T12:00:00Z")
        data["observations"].append(repeated)
        with self.assertRaisesRegex(instrument.HiringObservationError, "reopening"):
            instrument.audit(data)

    def test_unconfirmed_reopening_stays_explicitly_unconfirmed(self):
        data = fixture(); data["observations"][5].update(linkage_status="unconfirmed", link_evidence_ref=None)
        row = instrument.audit(data)["requisitions"][0]["observations"][-1]
        self.assertEqual(row["linkage_status"], "unconfirmed")

    def test_closure_requires_employer_evidence_and_conflicting_variants_rejected(self):
        data = fixture(); data["observations"][3]["closure_evidence_ref"] = None
        with self.assertRaises(instrument.HiringObservationError): instrument.audit(data)
        data = fixture(); data["observations"][1].update(source_status="explicitly_closed", closure_evidence_ref="SYN_CLOSE")
        with self.assertRaisesRegex(instrument.HiringObservationError, "simultaneous"):
            instrument.audit(data)

    def test_missing_variant_does_not_negate_explicit_requisition_closure(self):
        data = fixture(); data["observations"] = data["observations"][:2]
        data["observations"][0].update(source_status="explicitly_closed", closure_evidence_ref="SYN_CLOSE")
        data["observations"][1].update(source_status="inaccessible", http_status=403,
                                       content_sha256=None, missing_reason="content_unavailable")
        history = instrument.audit(data)["requisitions"][0]
        self.assertEqual(history["observation_attempts"], 2)
        self.assertEqual(history["missing_attempts"], 1)
        self.assertFalse(history["right_censored"])

    def test_no_private_keys_or_asserted_approvals(self):
        private = "private.person@example.invalid"
        for target in ("root", "source", "observation"):
            data = fixture(); obj = data if target == "root" else data["sources"][0] if target == "source" else data["observations"][0]
            obj[private] = "sensitive"
            with self.assertRaises(instrument.HiringObservationError) as error: instrument.audit(data)
            self.assertNotIn(private, str(error.exception))
        data = fixture(); data["sources"][0]["access_review_status"] = "approved"
        with self.assertRaises(instrument.HiringObservationError): instrument.audit(data)

    def test_query_free_url_never_parses_empty_query_python310_contract(self):
        # Emulate the 3.10 strict parser's error on an empty string even when
        # running on newer interpreters that changed this behavior.
        with patch.object(instrument, "parse_qsl", side_effect=ValueError("empty query")) as parse:
            self.assertEqual(instrument._url("https://careers.example.invalid/jobs").query, "")
            parse.assert_not_called()
        self.assertEqual(instrument._url("https://careers.example.invalid/jobs?gh_jid=J1").query, "gh_jid=J1")
        for query in ("?", "?gh_jid=", "?&gh_jid=J1", "?gh_jid=J1&", "?gh_jid=J1&&job_id=J2"):
            with self.subTest(query=query), self.assertRaises(instrument.HiringObservationError):
                instrument._url("https://careers.example.invalid/jobs" + query)

    def test_clean_urls_deny_credentials_tracking_percent_alias_and_traversal(self):
        for url in ("http://careers.example.invalid/jobs/A", "https://user:token@careers.example.invalid/jobs/A",
                    "https://careers.example.invalid/jobs/%41", "https://careers.example.invalid/jobs/../A",
                    "https://careers.example.invalid/jobs/A?token=secret", "https://careers.example.invalid/jobs/A?",
                    "https://careers.example.invalid/jobs/A?gh_jid=%41",
                    "https://CAREERS.example.invalid/jobs/A", "https://careers.example.invalid/jobs/A#secret",
                    "https://hostile.invalid/jobs/A"):
            data = fixture(); data["observations"][0]["canonical_url"] = url
            with self.subTest(url=url), self.assertRaises(instrument.HiringObservationError): instrument.audit(data)

    def test_row_order_cannot_rewrite_prior_history(self):
        data = fixture(); data["observations"][2], data["observations"][3] = data["observations"][3], data["observations"][2]
        with self.assertRaisesRegex(instrument.HiringObservationError, "chronologically"):
            instrument.audit(data)


class SecurePublicationTests(unittest.TestCase):
    def test_strict_json_keys_numbers_and_private_error_redaction(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            for raw in ('{"private_email":1,"private_email":2}', '{"x":NaN}', '{"x":Infinity}',
                        '{"x":1e999}', '{"x":1e-999}'):
                path.write_text(raw)
                with self.assertRaises(instrument.HiringObservationError) as error: instrument.load(path)
                self.assertNotIn("private_email", str(error.exception))
            path.write_bytes(b'\xff')
            with self.assertRaises(instrument.HiringObservationError): instrument.load(path)

    def test_input_symlink_fifo_directory_and_actual_byte_growth_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); path = root / "input.json"; path.write_text(EXAMPLE.read_text())
            link = root / "link.json"; link.symlink_to(path)
            with self.assertRaises(OSError): instrument.load(link)
            with self.assertRaises(instrument.HiringObservationError): instrument.load(root)
            fifo = root / "fifo"; os.mkfifo(fifo)
            with self.assertRaises(instrument.HiringObservationError): instrument.load(fifo)
            with patch.object(instrument, "MAX_FILE_BYTES", 10), self.assertRaises(instrument.HiringObservationError):
                instrument.load(path)
            fake = SimpleNamespace(st_mode=path.stat().st_mode, st_size=1)
            with patch.object(instrument, "MAX_FILE_BYTES", 10), patch.object(instrument.os, "fstat", return_value=fake):
                with self.assertRaises(instrument.HiringObservationError): instrument.load(path)

    def test_cli_write_once_and_input_output_alias(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.json"
            args = ["--input", str(EXAMPLE), "--output", str(output)]
            with contextlib.redirect_stdout(io.StringIO()): instrument.main(args)
            before = output.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit): instrument.main(args)
            self.assertEqual(output.read_bytes(), before)
            source = Path(tmp) / "input.json"; source.write_bytes(EXAMPLE.read_bytes())
            before = source.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                instrument.main(["--input", str(source), "--output", str(source)])
            self.assertEqual(source.read_bytes(), before)

    def test_no_output_from_invalid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "bad.json"; source.write_text('{"private_email":1,"private_email":2}')
            output = Path(tmp) / "result.json"; stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit):
                instrument.main(["--input", str(source), "--output", str(output)])
            self.assertFalse(output.exists())
            self.assertNotIn("private_email", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
