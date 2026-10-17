"""Synthetic regression tests for Study A proposed controls; no field cohort."""
import copy
from contextlib import redirect_stderr
import io
import json
from pathlib import Path
import tempfile
import traceback
import unittest

from trending_study.control_sampling import ControlFrameError, main, sample


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "control_frame.synthetic.json"


def frame():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


class ControlSamplingTests(unittest.TestCase):
    def test_select_preserves_trending_and_unknown_exclusions(self):
        r = sample(frame())
        self.assertEqual(r["quota_requested"], 3)
        self.assertEqual(r["selected_count"], 2)
        self.assertFalse(r["quota_fulfilled_in_supplied_frame"])
        self.assertEqual(len([x for x in r["selected"]
                              if x["stratum_id"] == "py_mature_low_w42"]), 1)
        self.assertIn(2001, [x["repository_id"] for x in r["selected"]])
        self.assertTrue({x["repository_id"] for x in r["selected"]} <= {1001, 1002, 2001})
        self.assertNotIn(2003, [x["repository_id"] for x in r["selected"]])
        self.assertNotIn(1003, [x["repository_id"] for x in r["selected"]])
        self.assertEqual(r["strata"][1]["observed_trending_held"], 1)
        self.assertEqual(r["strata"][1]["shortfall"], 1)
        self.assertTrue(r["inclusion_probabilities_not_estimated"])
        self.assertTrue(r["not_seen_in_supplied_trending_ids_is_not_never_trending"])
        self.assertFalse(r["causal_or_population_inference_authorized"])

    def test_hash_and_selected_rows_ignore_input_order(self):
        p = frame()
        baseline = sample(p)
        p["source_frames"].reverse()
        p["strata"].reverse()
        p["candidates"].reverse()
        p["observed_trending_repository_ids"].reverse()
        got = sample(p)
        self.assertEqual(baseline["selection_plan_sha256"], got["selection_plan_sha256"])
        self.assertEqual(baseline["selected"], got["selected"])
        self.assertEqual(baseline["strata"], got["strata"])

    def test_plan_hash_changes_on_seed_quota_status_or_trending_set(self):
        base = sample(frame())["selection_plan_sha256"]
        for mutation in ("seed", "quota", "status", "observed", "source"):
            p = frame()
            if mutation == "seed":
                p["seed"] += "-new"
            elif mutation == "quota":
                p["strata"][0]["quota"] += 1
            elif mutation == "status":
                p["candidates"][0]["eligibility_state"] = "unknown"
            elif mutation == "observed":
                p["observed_trending_repository_ids"].append(1001)
            else:
                p["source_frames"][0]["source_sha256"] = "c" * 64
            with self.subTest(mutation=mutation):
                self.assertNotEqual(sample(p)["selection_plan_sha256"], base)

    def test_fail_closed_future_snapshot_and_source(self):
        for target in ("source", "candidate", "freeze"):
            p = frame()
            if target == "source":
                p["source_frames"][0]["captured_at_utc"] = "2026-10-19T00:00:00Z"
            elif target == "candidate":
                p["candidates"][0]["snapshot_at_utc"] = "2026-10-16T00:00:00Z"
            else:
                p["frozen_at_utc"] = "2099-01-01T00:00:00Z"
            with self.subTest(target=target), self.assertRaises(ControlFrameError):
                sample(p)

    def test_source_and_candidate_calendar_week_alignment_is_required(self):
        for target in ("source_week", "candidate_week"):
            p = frame()
            if target == "source_week":
                p["strata"][0]["calendar_week"] = "2026-W41"
            else:
                p["candidates"][0]["snapshot_at_utc"] = "2026-10-11T14:00:00Z"
            with self.subTest(target=target), self.assertRaisesRegex(
                    ControlFrameError, "week"):
                sample(p)

    def test_malformed_scalar_fields_fail_with_domain_error(self):
        for target in ("kind", "source_kind", "coverage", "eligibility"):
            p = frame()
            if target == "kind":
                p["evidence_kind"] = []
            elif target == "source_kind":
                p["source_frames"][0]["source_kind"] = []
            elif target == "coverage":
                p["source_frames"][0]["coverage"] = {}
            else:
                p["candidates"][0]["eligibility_state"] = []
            with self.subTest(target=target), self.assertRaises(ControlFrameError):
                sample(p)

    def test_field_kind_cannot_represent_synthetic_only_source(self):
        p = frame()
        p["evidence_kind"] = "field_self_reported"
        for r in p["source_frames"]:
            r["source_kind"] = "github_rest_search_metadata"
        with self.assertRaisesRegex(ControlFrameError, "synthetic"):
            sample(p)

    def test_duplicate_ids_and_profiles_rejected(self):
        for target in ("candidate", "trending", "source", "stratum", "profile"):
            p = frame()
            if target == "candidate":
                p["candidates"].append(copy.deepcopy(p["candidates"][0]))
            elif target == "trending":
                p["observed_trending_repository_ids"].append(2003)
            elif target == "source":
                p["source_frames"].append(copy.deepcopy(p["source_frames"][0]))
            elif target == "stratum":
                p["strata"].append(copy.deepcopy(p["strata"][0]))
            else:
                p["strata"].append(dict(p["strata"][0], stratum_id="second_identical_profile"))
            with self.subTest(target=target), self.assertRaises(ControlFrameError):
                sample(p)

    def test_leakage_private_columns_invalid(self):
        for key in ("future_stars", "downstream_reuse", "private_user_notes"):
            p = frame()
            p["candidates"][0][key] = "PRIVATE_SOURCE_SECRET"
            with self.subTest(key=key), self.assertRaises(ControlFrameError):
                sample(p)
        p = frame()
        p["bad_output"] = True
        with self.assertRaises(ControlFrameError):
            sample(p)

    def test_boolean_id_bad_week_invalid_label_and_frame_cross_link(self):
        for target in ("id", "week", "language", "frame"):
            p = frame()
            if target == "id":
                p["candidates"][0]["repository_id"] = True
            elif target == "week":
                p["strata"][0]["calendar_week"] = "2026-W54"
            elif target == "language":
                p["strata"][0]["language"] = "python secret"
            else:
                p["candidates"][0]["frame_id"] = "mock_search_b"
            with self.subTest(target=target), self.assertRaises(ControlFrameError):
                sample(p)

    def test_all_unknown_produces_incomplete_selection_not_fake_zero_results(self):
        p = frame()
        for r in p["candidates"]:
            r["eligibility_state"] = "unknown"
        got = sample(p)
        self.assertEqual(got["selected_count"], 0)
        self.assertFalse(got["quota_fulfilled_in_supplied_frame"])
        self.assertEqual(got["source_rows"], 6)
        self.assertEqual(sum(s["unknown_held"] for s in got["strata"]), 5)
        self.assertEqual(sum(s["observed_trending_held"] for s in got["strata"]), 1)

    def test_real_claim_is_not_authenticated_by_kind(self):
        p = frame()
        p["evidence_kind"] = "field_self_reported"
        for source in p["source_frames"]:
            source["source_kind"] = "github_rest_search_metadata"
            source["coverage"] = "bounded_page"
        got = sample(p)
        self.assertTrue(got["source_frame_authenticity_unverified"])
        self.assertTrue(got["preliminary_eligibility_not_independently_verified"])
        self.assertFalse(got["causal_or_population_inference_authorized"])

    def test_cli_strict_valid_and_private_duplicate_key_redaction(self):
        with tempfile.TemporaryDirectory() as temp:
            valid = Path(temp) / "valid.json"
            valid.write_text(json.dumps(frame()), encoding="utf-8")
            out = io.StringIO()
            from contextlib import redirect_stdout
            with redirect_stdout(out):
                main(["--input", str(valid)])
            self.assertEqual(json.loads(out.getvalue())["selected_count"], 2)
            bad = Path(temp) / "PRIVATE_FILENAME_CONTROL.json"
            bad.write_text('{"PRIVATE_SECRET":1,"PRIVATE_SECRET":2}', encoding="utf-8")
            errors = io.StringIO()
            with redirect_stderr(errors):
                try:
                    main(["--input", str(bad)])
                except SystemExit as exc:
                    self.assertEqual(exc.code, 2)
                    self.assertIsNone(exc.__context__)
                    self.assertIsNone(exc.__cause__)
                    self.assertNotIn("PRIVATE", "".join(traceback.format_exception(exc)))
                else:
                    self.fail("malformed duplicated JSON must fail")
            self.assertNotIn("PRIVATE", errors.getvalue())
            self.assertIn("strict UTF-8 JSON", errors.getvalue())

    def test_cli_symlink_rejected_without_private_file_path(self):
        with tempfile.TemporaryDirectory() as temp:
            raw = Path(temp) / "real.json"
            raw.write_text(json.dumps(frame()), encoding="utf-8")
            link = Path(temp) / "PRIVATE_LINK.json"
            link.symlink_to(raw)
            errors = io.StringIO()
            with redirect_stderr(errors), self.assertRaises(SystemExit):
                main(["--input", str(link)])
            self.assertIn("non-symlink", errors.getvalue())
            self.assertNotIn("PRIVATE_LINK", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
