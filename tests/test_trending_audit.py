"""Offline synthetic/adversarial cases for issue #6 (no live GitHub data)."""
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trending_study import trending_audit
from trending_study.trending_audit import (
    TrendingAuditError, evaluate_coverage, evaluate_proxy,
    load_offline_json, main,
)

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def coverage():
    return json.loads(
        (EXAMPLES / "trending_language_coverage.synthetic.json").read_text(encoding="utf-8")
    )


def proxy():
    return json.loads(
        (EXAMPLES / "trending_rank_proxy.synthetic.json").read_text(encoding="utf-8")
    )


class CoverageAuditTests(unittest.TestCase):
    def test_independently_declared_per_frame_denominator(self):
        out = evaluate_coverage(coverage())
        self.assertEqual(out["dataset_kind"], "synthetic")
        self.assertFalse(out["independent_verification"])
        self.assertFalse(out["eligible_for_confirmatory_cohort"])
        self.assertIsNone(out["cross_language_population_coverage"])
        by_id = {row["frame_id"]: row for row in out["surfaces"]}
        py = by_id["SYN-PYTHON"]
        self.assertEqual(py["denominator_predeclared_frame_ids"], 4)
        self.assertEqual(py["numerator_observed_frame_ids"], 2)
        self.assertEqual(py["frame_ids_not_on_page"], 2)
        self.assertEqual(py["page_ids_outside_frame"], 1)
        self.assertEqual(py["observed_page_ids"], 3)
        self.assertEqual(py["frame_observed_fraction"], 0.5)
        rust = by_id["SYN-RUST"]
        self.assertEqual(rust["denominator_predeclared_frame_ids"], 2)
        self.assertEqual(rust["numerator_observed_frame_ids"], 1)
        self.assertEqual(rust["frame_observed_fraction"], 0.5)

    def test_denominator_not_derived_from_trending_page_size(self):
        data = coverage()
        data["surfaces"][0]["eligible_repository_ids"].append(99)
        report = evaluate_coverage(data)
        py = next(x for x in report["surfaces"] if x["frame_id"] == "SYN-PYTHON")
        self.assertEqual(py["numerator_observed_frame_ids"], 2)
        self.assertEqual(py["denominator_predeclared_frame_ids"], 5)
        self.assertAlmostEqual(py["frame_observed_fraction"], 0.4)

    def test_frame_frozen_before_capture_and_explicit_provenance(self):
        original = coverage()
        for value in ("2026-10-12T12:00:00Z", "2099-01-01T00:00:00Z"):
            with self.subTest(value=value):
                data = copy.deepcopy(original)
                data["surfaces"][0]["frame_as_of_utc"] = value
                with self.assertRaises(TrendingAuditError):
                    evaluate_coverage(data)
        for field in ("frame_definition", "frame_sampling", "frame_source_sha256"):
            with self.subTest(field=field):
                data = copy.deepcopy(original)
                data["surfaces"][0].pop(field)
                with self.assertRaises(TrendingAuditError):
                    evaluate_coverage(data)

    def test_duplicate_and_invalid_frame_ids(self):
        for bad in ([10, 10], [10, 0], [10, True], [], ["10"], list(range(10001))):
            with self.subTest(variant=str(bad[:3])):
                data = coverage()
                data["surfaces"][0]["eligible_repository_ids"] = bad
                with self.assertRaises(TrendingAuditError):
                    evaluate_coverage(data)

    def test_duplicate_named_frame_and_bad_input_shapes(self):
        data = coverage()
        data["surfaces"][1]["frame_id"] = "SYN-PYTHON"
        with self.assertRaisesRegex(TrendingAuditError, "duplicate frame_id"):
            evaluate_coverage(data)
        for value in ({}, None, [], True):
            with self.subTest(value=str(value)):
                with self.assertRaises(TrendingAuditError):
                    evaluate_coverage(value)

    def test_untrusted_capture_is_rejected_using_existing_validator(self):
        modifications = (
            ("page_url", "https://github.com@hostile.invalid/trending/python?since=daily"),
            ("page_url", "https://github.com/trending/python?since=weekly"),
            ("source_sha256", "BAD"),
            ("repository_ids", [10, 10]),
            ("captured_at_utc", "2026-10-11T12:00:00+02:00"),
            ("window", "monthly"),
        )
        for key, bad in modifications:
            with self.subTest(key=key, value=str(bad)):
                data = coverage()
                data["surfaces"][0]["capture"][key] = bad
                with self.assertRaises(TrendingAuditError):
                    evaluate_coverage(data)

    def test_extra_fields_cannot_bypass_privacy_and_schema_checks(self):
        data = coverage()
        for obj, key in ((data, "raw_html"), (data["surfaces"][0], "private_email"),
                         (data["surfaces"][0]["capture"], "raw_user_profile")):
            with self.subTest(key=key):
                obj[key] = "sensitive"
                with self.assertRaisesRegex(TrendingAuditError, "unsupported"):
                    evaluate_coverage(data)
                obj.pop(key)

    def test_frame_fraction_is_not_called_population_recall(self):
        report = evaluate_coverage(coverage())
        self.assertEqual(report["denominator_scope"], "per_predeclared_frame_only")
        self.assertIn("unverified", report["interpretation"])
        self.assertTrue(all("frame_observed_fraction" in s for s in report["surfaces"]))


class ChronologicalProxyTests(unittest.TestCase):
    def test_train_only_selector_and_macro_heldout_pairwise_score(self):
        report = evaluate_proxy(proxy())
        self.assertEqual(report["schema_version"], "trending-rank-proxy-1.0")
        self.assertEqual(report["selected_predictor_train_only"], "prior_7d_star_delta")
        self.assertEqual(report["train_pages"], 2)
        self.assertEqual(report["heldout_pages"], 2)
        self.assertEqual(report["train_unique_repository_ids"], 6)
        self.assertEqual(report["heldout_unique_repository_ids"], 6)
        self.assertAlmostEqual(report["train_selected_macro_accuracy"], 1.0)
        self.assertAlmostEqual(report["heldout_macro_pairwise_accuracy"], 5 / 6)
        self.assertEqual([x["pairs"] for x in report["heldout_page_scores"]], [3, 3])
        self.assertFalse(report["selection_universe_known"])
        self.assertFalse(report["independent_verification"])
        self.assertFalse(report["eligible_for_confirmatory_cohort"])

    def test_holdout_cannot_change_training_selected_feature(self):
        original = proxy()
        control = evaluate_proxy(original)
        for page in original["pages"][2:]:
            for i, row in enumerate(page["features"]):
                row["prior_forks"] = 900 - i * 100
                row["prior_stars"] = 800 - i * 100
                row["prior_7d_star_delta"] = i
        outcome = evaluate_proxy(original)
        self.assertEqual(outcome["selected_predictor_train_only"],
                         control["selected_predictor_train_only"])
        self.assertEqual(outcome["train_macro_accuracy_by_predictor"],
                         control["train_macro_accuracy_by_predictor"])
        self.assertNotEqual(outcome["heldout_macro_pairwise_accuracy"],
                            control["heldout_macro_pairwise_accuracy"])

    def test_prediction_ties_award_half_credit(self):
        data = proxy()
        for page in data["pages"][:2]:
            for row in page["features"]:
                row["prior_7d_star_delta"] = 1
                row["prior_forks"] = 1
                row["prior_stars"] = 1
        outcome = evaluate_proxy(data)
        self.assertEqual(outcome["selected_predictor_train_only"], "prior_7d_star_delta")
        self.assertEqual(outcome["train_selected_macro_accuracy"], 0.5)
        self.assertEqual(outcome["heldout_page_scores"][0]["feature_ties"], 0)

    def test_temporal_split_requires_at_least_two_pages_each(self):
        data = proxy()
        data["protocol_locked_at_utc"] = "2026-10-08T13:00:00Z"
        with self.assertRaisesRegex(TrendingAuditError, "two pre-lock"):
            evaluate_proxy(data)
        data = proxy()
        data["protocol_locked_at_utc"] = "2026-10-14T13:00:00Z"
        with self.assertRaisesRegex(TrendingAuditError, "two pre-lock"):
            evaluate_proxy(data)

    def test_same_instant_as_protocol_lock_is_invalid(self):
        data = proxy()
        data["protocol_locked_at_utc"] = "2026-10-09T12:00:00Z"
        with self.assertRaisesRegex(TrendingAuditError, "equal"):
            evaluate_proxy(data)

    def test_out_of_order_captures_and_duplicate_capture_id(self):
        data = proxy()
        data["pages"][1], data["pages"][2] = data["pages"][2], data["pages"][1]
        with self.assertRaisesRegex(TrendingAuditError, "chronological"):
            evaluate_proxy(data)
        data = proxy()
        data["pages"][3]["capture"]["capture_id"] = data["pages"][2]["capture"]["capture_id"]
        with self.assertRaisesRegex(TrendingAuditError, "duplicate capture_id"):
            evaluate_proxy(data)

    def test_leakage_from_cross_split_identity_is_refused(self):
        data = proxy()
        data["pages"][2]["capture"]["repository_ids"][0] = 101
        data["pages"][2]["features"][0]["repository_id"] = 101
        with self.assertRaisesRegex(TrendingAuditError, "cross-split"):
            evaluate_proxy(data)

    def test_future_features_and_missing_metadata_rejected(self):
        for bad in ("2026-10-13T12:00:00Z", "2099-01-01T00:00:00Z"):
            with self.subTest(bad=bad):
                data = proxy()
                data["pages"][2]["features"][0]["recorded_at_utc"] = bad
                with self.assertRaises(TrendingAuditError):
                    evaluate_proxy(data)
        for field in ("recorded_at_utc", "feature_source_sha256", "prior_stars",
                      "prior_forks", "prior_7d_star_delta"):
            with self.subTest(field=field):
                data = proxy()
                data["pages"][0]["features"][0].pop(field)
                with self.assertRaises(TrendingAuditError):
                    evaluate_proxy(data)

    def test_unknown_is_not_treated_as_zero_and_bool_is_invalid(self):
        for key, value in (("prior_stars", None), ("prior_stars", True),
                           ("prior_forks", -1), ("prior_7d_star_delta", 3.5)):
            with self.subTest(key=key, value=str(value)):
                data = proxy()
                data["pages"][0]["features"][0][key] = value
                with self.assertRaises(TrendingAuditError):
                    evaluate_proxy(data)
        data = proxy()
        data["pages"][0]["features"][0]["prior_7d_star_delta"] = -10
        self.assertEqual(evaluate_proxy(data)["train_pages"], 2)

    def test_missing_extra_and_duplicate_feature_rows_rejected(self):
        data = proxy()
        data["pages"][0]["features"].pop()
        with self.assertRaises(TrendingAuditError):
            evaluate_proxy(data)
        data = proxy()
        data["pages"][0]["features"][0]["repository_id"] = 9000
        with self.assertRaisesRegex(TrendingAuditError, "do not match"):
            evaluate_proxy(data)
        data = proxy()
        data["pages"][0]["features"][1]["repository_id"] = 101
        with self.assertRaisesRegex(TrendingAuditError, "duplicate"):
            evaluate_proxy(data)
        data = proxy()
        data["pages"][0]["features"][0]["rank_label"] = 1
        with self.assertRaisesRegex(TrendingAuditError, "unsupported"):
            evaluate_proxy(data)

    def test_mixed_surface_comparison_is_blocked(self):
        data = proxy()
        page = data["pages"][3]["capture"]
        page.update(page_url="https://github.com/trending?since=weekly", window="weekly")
        with self.assertRaisesRegex(TrendingAuditError, "one matched surface"):
            evaluate_proxy(data)

    def test_invalid_protocol_lock_reference_and_dataset_kind(self):
        for field, value in (("protocol_reference", ""), ("protocol_locked_at_utc", "wrong"),
                             ("dataset_kind", "empirical_verified"),
                             ("dataset_kind", []), ("schema_version", "other")):
            with self.subTest(field=field):
                data = proxy()
                data[field] = value
                with self.assertRaises(TrendingAuditError):
                    evaluate_proxy(data)

    def test_fixture_is_structure_only_not_real_2026_analysis(self):
        report = evaluate_proxy(proxy())
        self.assertIn("ALREADY DISPLAYED", report["interpretation"])
        self.assertFalse(report["holdout_frozen_by_external_review"])


class OfflineCLITests(unittest.TestCase):
    def test_both_synthetic_cli_modes(self):
        for mode, file in (
            ("coverage", "trending_language_coverage.synthetic.json"),
            ("proxy", "trending_rank_proxy.synthetic.json"),
        ):
            with self.subTest(mode=mode):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    main([mode, "--input", str(EXAMPLES / file)])
                value = json.loads(output.getvalue())
                self.assertEqual(value["dataset_kind"], "synthetic")
                self.assertFalse(value["independent_verification"])

    def test_duplicate_json_keys_and_nonstandard_numbers_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bad.json"
            for content in (
                '{"schema_version":"x","schema_version":"y"}',
                '{"schema_version":"x","field":NaN}',
                '{"schema_version":"x","field":Infinity}',
            ):
                with self.subTest(content=content):
                    source.write_text(content, encoding="utf-8")
                    with contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as caught:
                            main(["coverage", "--input", str(source)])
                    self.assertEqual(caught.exception.code, 2)

    def test_reject_symlink_and_oversized_input(self):
        with tempfile.TemporaryDirectory() as directory:
            d = Path(directory)
            file = d / "regular.json"
            file.write_text(json.dumps(coverage()), encoding="utf-8")
            with patch.object(trending_audit, "MAX_FILE_BYTES", 30):
                with self.assertRaisesRegex(TrendingAuditError, "byte limit"):
                    load_offline_json(file)
            link = d / "link.json"
            try:
                link.symlink_to(file)
            except (NotImplementedError, OSError):
                self.skipTest("symlink unavailable on this filesystem")
            with self.assertRaisesRegex(TrendingAuditError, "non-symlink"):
                load_offline_json(link)


if __name__ == "__main__":
    unittest.main()
