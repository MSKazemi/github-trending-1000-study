"""Synthetic guard tests; not a verification of live Trending pages."""
import copy
import unittest

from trending_study.trending_overlap import OverlapError, evaluate


def fixture():
    return {
        "schema_version": "1.0",
        "dataset_kind": "synthetic",
        "captures": [
            {"capture_id": "a", "captured_at_utc": "2026-10-10T12:00:00Z",
             "page_url": "https://github.com/trending?since=daily", "window": "daily",
             "language_filter": None, "source_sha256": "a" * 64,
             "repository_ids": [10, 20, 30]},
            {"capture_id": "b", "captured_at_utc": "2026-10-11T12:00:00Z",
             "page_url": "https://github.com/trending?since=daily", "window": "daily",
             "language_filter": None, "source_sha256": "b" * 64,
             "repository_ids": [20, 10, 40]},
        ],
    }


class TrendingOverlapTests(unittest.TestCase):
    def test_set_overlap_and_common_rank_reversal(self):
        result = evaluate(fixture())
        self.assertAlmostEqual(result["jaccard"], 0.5)
        self.assertEqual(result["common_unique_ids"], 2)
        self.assertEqual(result["kendall_comparable_pairs"], 1)
        self.assertEqual(result["kendall_tau_on_common"], -1.0)
        self.assertFalse(result["eligible_for_confirmatory_cohort"])
        self.assertGreater(result["discounted_prefix_overlap_lower_bound"], 0)
        self.assertLess(result["discounted_prefix_overlap_lower_bound"], 1)

    def test_equal_lists(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [10, 20, 30]
        out = evaluate(data)
        self.assertEqual(out["jaccard"], 1)
        self.assertEqual(out["kendall_tau_on_common"], 1)

    def test_equal_depth_rbo_reuses_competing_implementation(self):
        data = fixture()
        for p in (0.1, 0.5, 0.9):
            with self.subTest(p=p):
                result = evaluate(data, p)
                self.assertIsNotNone(result["rbo_extrapolated_equal_depth"])
                self.assertGreaterEqual(result["rbo_extrapolated_equal_depth"],
                                        result["discounted_prefix_overlap_lower_bound"])
                self.assertLessEqual(result["rbo_extrapolated_equal_depth"], 1.0)
                self.assertIsNone(result["rbo_extrapolation_reason"])
                self.assertEqual(result["prefix_persistence"], p)

    def test_identical_equal_depth_rbo_is_one(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [10, 20, 30]
        for p in (0.1, 0.5, 0.9):
            with self.subTest(p=p):
                self.assertAlmostEqual(evaluate(data, p)["rbo_extrapolated_equal_depth"], 1.0)

    def test_unequal_depth_does_not_invent_tail(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [20, 10]
        report = evaluate(data)
        self.assertIsNone(report["rbo_extrapolated_equal_depth"])
        self.assertEqual(report["rbo_extrapolation_reason"], "unequal observed page lengths")
        self.assertIsNotNone(report["discounted_prefix_overlap_lower_bound"])

    def test_equal_depth_disjoint_lists_rbo_is_zero(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [40, 50, 60]
        report = evaluate(data)
        self.assertEqual(report["discounted_prefix_overlap_lower_bound"], 0.0)
        self.assertEqual(report["rbo_extrapolated_equal_depth"], 0.0)

    def test_disjoint_rank_tau_not_zero(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [50, 60]
        out = evaluate(data)
        self.assertEqual(out["jaccard"], 0)
        self.assertIsNone(out["kendall_tau_on_common"])

    def test_one_common_rank_tau_unknown(self):
        data = fixture()
        data["captures"][1]["repository_ids"] = [10, 40]
        self.assertIsNone(evaluate(data)["kendall_tau_on_common"])

    def test_duplicate_ids_fail(self):
        data = fixture()
        data["captures"][0]["repository_ids"] = [10, 10]
        with self.assertRaises(OverlapError):
            evaluate(data)

    def test_wrong_surface_fails(self):
        for key, value in (("window", "weekly"),
                           ("language_filter", "Python"),
                           ("page_url", "https://github.com/trending/python?since=daily")):
            with self.subTest(key=key):
                data = fixture()
                data["captures"][1][key] = value
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_url_is_bound_to_real_trending_surface_and_declared_window(self):
        invalid_urls = (
            "https://github.com/trending-evil?since=daily",
            "https://github.com@evil.test/trending?since=daily",
            "https://github.com/trending?since=weekly",
            "https://github.com/trending?since=daily&since=weekly",
            "https://github.com/trending?since=daily#fragment",
            "http://github.com/trending?since=daily",
            "https://github.com/trending/python?since=daily",
        )
        for url in invalid_urls:
            with self.subTest(url=url):
                data = fixture()
                for entry in data["captures"]:
                    entry["page_url"] = url
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_unregistered_url_parameters_are_not_comparable_surfaces(self):
        for extra in ("&spoken_language_code=en", "&foo=bar", "&since=", "&q=language"):
            with self.subTest(extra=extra):
                data = fixture()
                for entry in data["captures"]:
                    entry["page_url"] += extra
                with self.assertRaisesRegex(OverlapError, "exactly one since"):
                    evaluate(data)

    def test_page_rank_volume_is_bounded(self):
        data = fixture()
        data["captures"][0]["repository_ids"] = list(range(1, 1002))
        with self.assertRaisesRegex(OverlapError, "1000 ranks"):
            evaluate(data)

    def test_valid_language_slug_and_label_match(self):
        data = fixture()
        for entry in data["captures"]:
            entry["language_filter"] = "Jupyter Notebook"
            entry["page_url"] = "https://github.com/trending/jupyter-notebook?since=daily"
        result = evaluate(data)
        self.assertEqual(result["language_filter"], "Jupyter Notebook")
        for entry in data["captures"]:
            entry["language_filter"] = "Python"
        with self.assertRaisesRegex(OverlapError, "language"):
            evaluate(data)

    def test_url_query_key_whitelist_and_trusted_origin(self):
        for url in (
            "https://github.com/trending?since=daily&foo=bar",
            "https://github.com/trending?foo=bar&since=daily",
            "https://github.com:443/trending?since=daily",
            "https://github.com:garbage/trending?since=daily",
            "https://github.com%2Eevil.test/trending?since=daily",
        ):
            with self.subTest(url=url):
                data = fixture()
                for entry in data["captures"]:
                    entry["page_url"] = url
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_nested_or_encoded_language_paths_fail_closed(self):
        for language, url in (
            ("Python/other", "https://github.com/trending/python/other?since=daily"),
            ("Python", "https://github.com/trending/python%2Fother?since=daily"),
            ("Python", "https://github.com/trending/python/other?since=daily"),
            ("a#b", "https://github.com/trending/a%23b/other?since=daily"),
        ):
            with self.subTest(language=language, url=url):
                data = fixture()
                for entry in data["captures"]:
                    entry["language_filter"] = language
                    entry["page_url"] = url
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_malformed_container_fields_return_contract_error(self):
        malformed = (
            ("window", []), ("window", {}),
            ("dataset_kind", []), ("dataset_kind", {}),
        )
        for field, value in malformed:
            with self.subTest(field=field, value=value):
                data = fixture()
                if field == "dataset_kind":
                    data[field] = value
                else:
                    data["captures"][0][field] = value
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_future_capture_time_is_invalid(self):
        data = fixture()
        data["captures"][1]["captured_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(OverlapError, "future"):
            evaluate(data)

    def test_unverified_or_incomplete_input_fails(self):
        for key, value in (("source_sha256", None), ("repository_ids", []),
                           ("captured_at_utc", "2026-10-11T13:00:00+02:00")):
            with self.subTest(key=key):
                data = fixture()
                data["captures"][1][key] = value
                with self.assertRaises(OverlapError):
                    evaluate(data)

    def test_not_positive_stable_ids(self):
        for value in (True, 0, -1, "10"):
            data = fixture()
            data["captures"][0]["repository_ids"] = [value]
            with self.assertRaises(OverlapError):
                evaluate(data)

    def test_no_forward_time_travel(self):
        data = fixture()
        data["captures"].reverse()
        with self.assertRaises(OverlapError):
            evaluate(data)

    def test_schema_and_persistence(self):
        data = fixture()
        data["dataset_kind"] = "observed_verified"
        with self.assertRaises(OverlapError):
            evaluate(data)
        for bad in (0, 1, True, -0.5):
            with self.assertRaises(OverlapError):
                evaluate(fixture(), bad)


if __name__ == "__main__":
    unittest.main()
