"""Synthetic maintainer-burden accounting, never private participant data."""
import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import traceback
import unittest
from unittest.mock import patch

from trending_study.data_integrity import MAX_FILE_BYTES
from trending_study.maintainer_burden import BurdenError, summarize, FIELDS, main

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "maintainer_externality.synthetic.json"

def card():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))

class BurdenTests(unittest.TestCase):
    def test_absent_logs_cannot_be_zero_cost(self):
        r = summarize([card()])
        self.assertEqual(r["case_count"], 1)
        self.assertEqual(r["missing_component_entries"], 6)
        self.assertEqual(r["observed_component_entries"], 0)
        self.assertEqual(r["observed_upstream_component_entries"], 0)
        self.assertEqual(r["observed_downstream_component_entries"], 0)
        self.assertIsNone(r["known_partial_minutes_not_a_total"])
        self.assertIsNone(r["upstream_known_partial_minutes_not_a_total"])
        self.assertIsNone(r["downstream_known_partial_minutes_not_a_total"])
        self.assertIsNone(r["overall_human_minutes"])
        self.assertIsNone(r["per_accepted_task_minutes"])
        self.assertFalse(r["independent_review_authenticated"])

    def test_unconsented_work_may_not_be_recorded(self):
        c = card()
        c["human_time_minutes"]["upstream_review"] = 0
        with self.assertRaisesRegex(BurdenError, "unconsented"):
            summarize([c])

    def test_consent_declared_partial_is_not_complete_total(self):
        c = card()
        c["consent_state"] = "consented"
        c["human_time_minutes"]["upstream_review"] = 11.5
        r = summarize([c])
        self.assertEqual(r["known_partial_minutes_not_a_total"], 11.5)
        self.assertIsNone(r["overall_human_minutes"])
        self.assertEqual(r["missing_component_entries"], 5)

    def test_observed_zero_differs_from_missing_in_each_direction(self):
        # All-null reports are null, while truly measured zeros remain 0.0.
        for field, direction in (
            ("upstream_review", "upstream"),
            ("downstream_implementation", "downstream"),
        ):
            c = card()
            c["consent_state"] = "consented"
            c["human_time_minutes"][field] = 0.0
            with self.subTest(field=field):
                r = summarize([c])
                self.assertEqual(r["known_partial_minutes_not_a_total"], 0.0)
                self.assertEqual(r["observed_component_entries"], 1)
                self.assertEqual(r[f"{direction}_known_partial_minutes_not_a_total"], 0.0)
                opposite = "downstream" if direction == "upstream" else "upstream"
                self.assertIsNone(r[f"{opposite}_known_partial_minutes_not_a_total"])
                self.assertEqual(r[f"observed_{direction}_component_entries"], 1)
                self.assertEqual(r[f"observed_{opposite}_component_entries"], 0)
                self.assertIsNone(r["overall_human_minutes"])
                self.assertFalse(r["independent_review_authenticated"])

    def test_partial_group_sums_preserve_missingness_across_cases(self):
        first = card()
        first["consent_state"] = "consented"
        first["human_time_minutes"]["upstream_support"] = 9
        second = card()
        second["case_id"] = "FICTIONAL-SECOND-CASE"
        second["consent_state"] = "consented"
        summary = summarize([first, second])
        self.assertEqual(summary["known_partial_minutes_not_a_total"], 9)
        self.assertEqual(summary["upstream_known_partial_minutes_not_a_total"], 9)
        self.assertIsNone(summary["downstream_known_partial_minutes_not_a_total"])
        self.assertEqual(summary["observed_component_entries"], 1)
        self.assertEqual(summary["observed_upstream_component_entries"], 1)
        self.assertEqual(summary["observed_downstream_component_entries"], 0)
        self.assertEqual(summary["missing_component_entries"], 11)
        self.assertIsNone(summary["overall_human_minutes"])

    def test_duplicate_case_does_not_inflate_independent_count(self):
        with self.assertRaisesRegex(BurdenError, "unique"):
            summarize([card(), copy.deepcopy(card())])

    def test_complete_synthetic_stays_unauthenticated(self):
        c = card()
        c["consent_state"] = "consented"
        c["task_accepted_by_independent_reviewer"] = "pass"
        c["human_time_minutes"] = {k: 1 for k in FIELDS}
        r = summarize([c])
        self.assertIsNone(r["overall_human_minutes"])
        self.assertEqual(r["synthetic_scenario_minutes"], 6)
        self.assertEqual(r["cases_with_complete_time_boundary"], 1)
        self.assertIsNone(r["per_accepted_task_minutes"])
        self.assertEqual(r["synthetic_case_count"], 1)

    def test_negative_nan_or_future_time_fail(self):
        for value in (-1, float("nan"), float("inf")):
            c = card()
            c["consent_state"] = "consented"
            c["human_time_minutes"]["upstream_review"] = value
            with self.subTest(value=str(value)), self.assertRaises(BurdenError):
                summarize([c])
        c = card()
        c["consent_state"] = "consented"
        c["observed_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(BurdenError, "future"):
            summarize([c])

    def test_mixed_synthetic_and_real_cases_cannot_be_pooled(self):
        a = card()
        b = copy.deepcopy(a)
        b["case_id"] = "CONSENTED-CASE-2"
        b["not_empirical_data"] = False
        b["synthetic"] = False
        b["frame_commit"] = "a" * 40
        b["consent_state"] = "consented"
        with self.assertRaisesRegex(BurdenError, "never share one aggregate"):
            summarize([a, b])

    def test_real_case_requires_frozen_frame_commit(self):
        p = card()
        p["not_empirical_data"] = False
        p["synthetic"] = False
        p["consent_state"] = "consented"
        with self.assertRaisesRegex(BurdenError, "frame_commit"):
            summarize([p])
        p["frame_commit"] = "a" * 40
        result = summarize([p])
        self.assertEqual(result["dataset_kind"], "self_reported_pilot")
        self.assertFalse(result["approved_for_public_release"])

    def test_withdrawn_case_never_keeps_time_observation(self):
        p = card()
        p["consent_state"] = "withdrawn"
        p["observed_at_utc"] = "2026-10-12T12:00:00Z"
        with self.assertRaisesRegex(BurdenError, "cannot retain"):
            summarize([p])

    def test_extra_private_case_and_outcome_fields_fail_closed(self):
        for change in ("raw_prompt", "private_email", "participant_name"):
            c = card()
            c[change] = "NEVER_PUBLISH_PRIVATE_PARTICIPANT_DATA"
            with self.subTest(extra=change), self.assertRaisesRegex(
                    BurdenError, "case schema or fields"):
                summarize([c])
        c = card()
        c["outcomes"]["person_name"] = "NEVER_PUBLISH"
        with self.assertRaisesRegex(BurdenError, "outcome schema"):
            summarize([c])
        c = card()
        del c["opt_in_project_id"]
        with self.assertRaisesRegex(BurdenError, "case schema or fields"):
            summarize([c])

    def test_synthetic_provenance_flags_must_agree(self):
        for synthetic, declared in ((False, True), (True, False)):
            c = card()
            c["synthetic"] = synthetic
            c["not_empirical_data"] = declared
            with self.subTest(synthetic=synthetic, declared=declared):
                with self.assertRaisesRegex(BurdenError, "conflicting synthetic"):
                    summarize([c])
        c = card()
        c["synthetic"] = "false"
        with self.assertRaisesRegex(BurdenError, "conflicting synthetic"):
            summarize([c])

    def test_v01_cannot_self_certify_human_review_or_release(self):
        for field in ("human_review_state", "data_release_approval"):
            c = card()
            c[field] = "approved"
            with self.subTest(field=field), self.assertRaisesRegex(
                    BurdenError, "cannot self-certify"):
                summarize([c])

    def test_identifiers_and_outcome_states_not_free_text(self):
        for field in ("case_id", "opt_in_project_id", "task_type",
                      "declared_workflow", "frame_commit"):
            c = card()
            c[field] = "PRIVATE\\nPARTICIPANT\\tNAME"
            with self.subTest(field=field), self.assertRaises(BurdenError):
                summarize([c])
        c = card()
        c["outcomes"]["actionability"] = "contains private interview text"
        with self.assertRaisesRegex(BurdenError, "outcome schema"):
            summarize([c])

    def test_unhashable_status_values_are_controlled_domain_errors(self):
        for field in ("consent_state", "task_accepted_by_independent_reviewer"):
            c = card()
            c[field] = []
            with self.subTest(field=field), self.assertRaises(BurdenError):
                summarize([c])

    def test_bounded_case_count_prevents_unbounded_direct_processing(self):
        with self.assertRaisesRegex(BurdenError, "bounded nonempty"):
            summarize([card()] * 10001)

    def test_batch_envelope_accepts_only_declared_cases_key(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "cases.json"
            batch = {"cases": [card()]}
            path.write_text(json.dumps(batch), encoding="utf-8")
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                main(["--input", str(path)])
            self.assertEqual(json.loads(stdout.getvalue())["case_count"], 1)
            for unwanted in ("raw_interview", "participant_email", "extra_sources"):
                with self.subTest(unwanted=unwanted):
                    bad = dict(batch)
                    bad[unwanted] = "PRIVATE_BATCH_FIELD_MARKER"
                    path.write_text(json.dumps(bad), encoding="utf-8")
                    stderr = io.StringIO()
                    with redirect_stderr(stderr), self.assertRaises(SystemExit) as result:
                        main(["--input", str(path)])
                    self.assertEqual(result.exception.code, 2)
                    self.assertIn("invalid maintainer cases envelope", stderr.getvalue())
                    self.assertNotIn("PRIVATE_BATCH_FIELD_MARKER", stderr.getvalue())
                    self.assertNotIn(unwanted, stderr.getvalue())
            for raw in ({"cases": {}}, {"cases": []}, {"cases": "private"}):
                with self.subTest(invalid_shape=type(raw["cases"]).__name__):
                    path.write_text(json.dumps(raw), encoding="utf-8")
                    with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                        main(["--input", str(path)])

    def test_cli_privacy_errors_never_echo_private_input_data(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "PRIVATE_PARTICIPANT_MARKER.json"
            c = card()
            c["raw_private_interview"] = "PRIVATE_INTERVIEW_CONTENT"
            path.write_text(json.dumps(c), encoding="utf-8")
            stderr = io.StringIO()
            with redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
                main(["--input", str(path)])
            self.assertEqual(caught.exception.code, 2)
            self.assertIn("invalid maintainer case schema", stderr.getvalue())
            self.assertNotIn("PRIVATE_PARTICIPANT_MARKER", stderr.getvalue())
            self.assertNotIn("PRIVATE_INTERVIEW_CONTENT", stderr.getvalue())
            self.assertNotIn("raw_private_interview", stderr.getvalue())

    def test_malformed_private_time_avoids_full_exception_chain_disclosure(self):
        from trending_study.maintainer_burden import _utc
        marker = "PRIVATE_HUMAN_TIMESTAMP_20261017"
        try:
            _utc(marker)
        except BurdenError as exc:
            self.assertEqual(str(exc), "invalid timestamp")
            self.assertIsNone(exc.__cause__)
            self.assertIsNone(exc.__context__)
            self.assertNotIn(marker, "".join(traceback.format_exception(exc)))
        else:
            self.fail("invalid timestamp should not be accepted")

    def test_cli_systemexit_does_not_chain_raw_json_private_identifiers(self):
        with tempfile.TemporaryDirectory() as folder:
            marker = "PRIVATE_RESEARCH_JSON_KEY_20261017"
            path = Path(folder) / "private-data.json"
            # Even if stderr itself was already sanitized, argparse.error
            # inside an except block chained the underlying decoder error.
            payload = json.dumps({marker: 1})[:-1] + "," + json.dumps(marker) + ": 2}"
            path.write_text(payload, encoding="utf-8")
            errors = io.StringIO()
            with redirect_stderr(errors):
                try:
                    main(["--input", str(path)])
                except SystemExit as exc:
                    self.assertEqual(exc.code, 2)
                    self.assertIsNone(exc.__cause__)
                    self.assertIsNone(exc.__context__)
                    self.assertNotIn(marker, errors.getvalue())
                    self.assertNotIn(marker, "".join(traceback.format_exception(exc)))
                else:
                    self.fail("ambiguous research input must not be accepted")

    def test_row_and_multi_case_float_sums_never_overflow_to_infinity(self):
        a = card()
        a["consent_state"] = "consented"
        a["human_time_minutes"] = {category: 1e308 for category in FIELDS}
        with self.assertRaisesRegex(BurdenError, "finite numeric range"):
            summarize([a])
        # Each individual case's partial sum is finite, but the population
        # sum would silently overflow if not independently bounded.
        a = card()
        a["consent_state"] = "consented"
        a["human_time_minutes"]["upstream_review"] = 1e308
        b = copy.deepcopy(a)
        b["case_id"] = "FICTIONAL-CASE-002"
        with self.assertRaisesRegex(BurdenError, "finite numeric range"):
            summarize([a, b])

    def test_nonconsented_or_withdrawn_rows_cannot_retain_task_outcomes(self):
        for consent in ("not_consented", "withdrawn"):
            for target in ("accepted", "outcome"):
                case = card()
                case["consent_state"] = consent
                if target == "accepted":
                    case["task_accepted_by_independent_reviewer"] = "pass"
                else:
                    case["outcomes"]["actionability"] = "pass"
                with self.subTest(consent=consent, target=target):
                    with self.assertRaisesRegex(
                            BurdenError, "nonconsented case must not retain"):
                        summarize([case])
        # Explicitly unknown and not_started preserve denominator-only rows.
        self.assertEqual(summarize([card()])["case_count"], 1)

    def test_huge_private_numeric_input_never_survives_exception_chain(self):
        # Construct the large synthetic value outside the failing call so
        # Python's formatted source traceback cannot quote its contents.
        value = 10 ** 400
        case = card()
        case["consent_state"] = "consented"
        case["human_time_minutes"]["upstream_review"] = value
        try:
            summarize([case])
        except BurdenError as error:
            self.assertIn("finite, nonnegative", str(error))
            self.assertIsNone(error.__cause__)
            self.assertIsNone(error.__context__)
            self.assertNotIn(str(value), "".join(traceback.format_exception(error)))
        else:
            self.fail("unrepresentable human minutes must be rejected")

    def test_unbounded_python_integer_is_rejected_as_domain_error(self):
        a = card()
        a["consent_state"] = "consented"
        a["human_time_minutes"]["upstream_review"] = 10 ** 400
        with self.assertRaisesRegex(BurdenError, "finite, nonnegative"):
            summarize([a])

    def test_cli_uses_shared_strict_descriptor_checked_reader(self):
        with patch("trending_study.maintainer_burden.load_research_json_file",
                   return_value=card()) as loader:
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                main(["--input", "fake-local-file.json"])
            loader.assert_called_once_with(Path("fake-local-file.json"),
                                           max_bytes=MAX_FILE_BYTES)
            self.assertIn('"dataset_kind": "synthetic"', stdout.getvalue())

    def test_cli_rejects_unsafe_json_without_leaking_private_key_or_filename(self):
        with tempfile.TemporaryDirectory() as folder:
            private = "PRIVATE_FILE_OR_EMAIL_MARKER"
            path = Path(folder) / (private + ".json")
            for raw in ('{"PRIVATE_SECRET_KEY":1,"PRIVATE_SECRET_KEY":2}',
                        '{"x":NaN}', '{"x":Infinity}',
                        '{"x":1e999}', '{"x":1e-999}'):
                with self.subTest(raw=raw):
                    path.write_text(raw, encoding="utf-8")
                    errors = io.StringIO()
                    with redirect_stderr(errors), self.assertRaises(SystemExit) as caught:
                        main(["--input", str(path)])
                    self.assertEqual(caught.exception.code, 2)
                    self.assertIn("invalid or unsafe research JSON input", errors.getvalue())
                    self.assertNotIn(private, errors.getvalue())
                    self.assertNotIn("PRIVATE_SECRET_KEY", errors.getvalue())

    def test_cli_rejects_symlinked_and_nonregular_input(self):
        with tempfile.TemporaryDirectory() as folder:
            parent = Path(folder)
            target = parent / "valid.json"
            target.write_text(json.dumps(card()), encoding="utf-8")
            symlink = parent / "PRIVATE_SYMLINK_MARKER.json"
            symlink.symlink_to(target)
            for path in (symlink, parent):
                with self.subTest(path=str(path)):
                    err = io.StringIO()
                    with redirect_stderr(err), self.assertRaises(SystemExit) as caught:
                        main(["--input", str(path)])
                    self.assertEqual(caught.exception.code, 2)
                    self.assertIn("invalid or unsafe research JSON input", err.getvalue())
                    self.assertNotIn("PRIVATE_SYMLINK_MARKER", err.getvalue())


    def test_coded_outcomes_and_separate_effort_missingness_are_descriptive_only(self):
        first = card()
        first["consent_state"] = "consented"
        first["human_time_minutes"] = {
            "upstream_review": 2, "upstream_support": 3,
            "downstream_search": 4, "downstream_implementation": 5,
            "downstream_review_repair": 6, "downstream_followup": 7,
        }
        first["task_accepted_by_independent_reviewer"] = "pass"
        first["outcomes"].update({
            "actionability": "pass",
            "newcomer_comprehension_pass": "fail",
            "followup_30_day": "completed",
            "followup_90_day": "not_started",
            "security_or_privacy_incident": "no",
        })
        second = copy.deepcopy(first)
        second["case_id"] = "FICTIONAL-CASE-002"
        second["human_time_minutes"] = {field: None for field in FIELDS}
        second["human_time_minutes"]["downstream_search"] = 8
        second["task_accepted_by_independent_reviewer"] = "fail"
        second["outcomes"].update({
            "actionability": "fail",
            "newcomer_comprehension_pass": "unknown",
            "followup_30_day": "missing",
            "followup_90_day": "unknown",
            "security_or_privacy_incident": "yes",
        })
        withdrawn = card()
        withdrawn["case_id"] = "FICTIONAL-CASE-003"
        withdrawn["consent_state"] = "withdrawn"
        result = summarize([first, second, withdrawn])
        self.assertEqual(result["case_count"], 3)
        self.assertEqual(result["consent_state_counts"], {
            "consented": 2, "not_consented": 0, "withdrawn": 1})
        self.assertEqual(
            result["task_acceptance_counts_self_reported_not_authenticated"],
            {"fail": 1, "pass": 1, "unknown": 1})
        self.assertEqual(result["upstream_known_partial_minutes_not_a_total"], 5)
        self.assertEqual(result["downstream_known_partial_minutes_not_a_total"], 30)
        self.assertEqual(result["known_partial_minutes_not_a_total"], 35)
        self.assertEqual(result["missing_upstream_component_entries"], 4)
        self.assertEqual(result["missing_downstream_component_entries"], 7)
        self.assertEqual(result["missing_component_entries"], 11)
        self.assertEqual(result["missing_or_not_due_outcome_entries"], 9)
        counts = result["outcome_counts_self_reported_not_authenticated"]
        self.assertEqual(counts["actionability"],
                         {"fail": 1, "pass": 1, "unknown": 1})
        self.assertEqual(counts["newcomer_comprehension_pass"],
                         {"fail": 1, "pass": 0, "unknown": 2})
        self.assertEqual(counts["followup_30_day"],
                         {"completed": 1, "missing": 1,
                          "not_started": 1, "unknown": 0})
        self.assertEqual(counts["followup_90_day"],
                         {"completed": 0, "missing": 0,
                          "not_started": 2, "unknown": 1})
        self.assertEqual(counts["security_or_privacy_incident"],
                         {"no": 1, "unknown": 1, "yes": 1})
        self.assertFalse(result["independent_review_authenticated"])
        self.assertFalse(result["approved_for_public_release"])
        self.assertIsNone(result["overall_human_minutes"])
        self.assertIsNone(result["per_accepted_task_minutes"])
        self.assertNotIn("FICTIONAL-CASE", json.dumps(result))

    def test_unknown_coded_outcome_values_are_rejected_without_echo(self):
        for name, value in (
                ("actionability", "wins"),
                ("newcomer_comprehension_pass", "completed"),
                ("followup_30_day", "yes"),
                ("followup_90_day", "approved"),
                ("security_or_privacy_incident", "pass"),
                ("actionability", []),
                ("followup_30_day", {"private": "content"})):
            record = card()
            record["consent_state"] = "consented"
            record["outcomes"][name] = value
            with self.subTest(name=name, value=type(value).__name__):
                with self.assertRaisesRegex(BurdenError, "outcome schema"):
                    summarize([record])

    def test_real_pending_pilot_coded_outcomes_are_not_authenticated(self):
        record = card()
        record["synthetic"] = False
        record["not_empirical_data"] = False
        record["frame_commit"] = "a" * 40
        record["consent_state"] = "consented"
        record["task_accepted_by_independent_reviewer"] = "fail"
        record["outcomes"]["actionability"] = "fail"
        record["outcomes"]["newcomer_comprehension_pass"] = "unknown"
        result = summarize([record])
        self.assertEqual(result["dataset_kind"], "self_reported_pilot")
        self.assertEqual(
            result["task_acceptance_counts_self_reported_not_authenticated"]["fail"], 1)
        self.assertFalse(result["approved_for_public_release"])
        self.assertFalse(result["independent_review_authenticated"])
        self.assertIsNone(result["overall_human_minutes"])



    def test_fictional_three_case_batch_fixture_has_null_and_negative_outcomes(self):
        fixture = Path(__file__).resolve().parents[1] / (
            "examples/maintainer_feasibility_batch.synthetic.json")
        data = json.loads(fixture.read_text(encoding="utf-8"))
        result = summarize(data["cases"])
        self.assertEqual(result["case_count"], 3)
        self.assertEqual(result["dataset_kind"], "synthetic")
        self.assertEqual(result["consent_state_counts"]["withdrawn"], 1)
        self.assertEqual(
            result["outcome_counts_self_reported_not_authenticated"]
                  ["actionability"]["fail"], 1)
        self.assertEqual(result["missing_component_entries"], 11)
        self.assertEqual(result["missing_or_not_due_outcome_entries"], 9)
        self.assertIsNone(result["overall_human_minutes"])
        self.assertIsNone(result["per_accepted_task_minutes"])
        self.assertFalse(result["approved_for_public_release"])
        self.assertNotIn("FICTIONAL-CASE-", json.dumps(result))



if __name__ == "__main__":
    unittest.main()
