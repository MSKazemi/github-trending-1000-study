"""Synthetic maintainer-burden accounting, never private participant data."""
import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
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
        b["frame_commit"] = "a" * 40
        b["consent_state"] = "consented"
        with self.assertRaisesRegex(BurdenError, "never share one aggregate"):
            summarize([a, b])

    def test_real_case_requires_frozen_frame_commit(self):
        p = card()
        p["not_empirical_data"] = False
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


if __name__ == "__main__":
    unittest.main()
