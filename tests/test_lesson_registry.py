"""Synthetic only: checks that unverified lessons are not auto-promoted."""
import copy
import json
from pathlib import Path
import unittest
from trending_study.lesson_registry import LessonError, audit


def hypothesis():
    return {"schema_version": "1.0", "dataset_kind": "synthetic",
            "lessons": [{"id": "SYN-001", "title": "Synthetic task",
        "status": "hypothesis", "evidence_grade": "E0",
        "question": "Could setup documentation help?", "population": "fictional users",
        "comparison": "two fictional READMEs", "primary_outcome": "first-use pass",
        "intervention_or_feature": "fictional onboarding tutorial",
        "negative_findings": "none observed; no experiment conducted",
        "practical_cost": "not measured",
        "suggested_experiment": "a preregistered first-use task trial",
        "measurement_window": "prospective, not observed",
        "applicability": "CLI repositories", "risks": "confounding",
        "stop_rule": "stop if unsafe", "validity_threats": "no observations",
        "sources": []}]}


class LessonRegistryTests(unittest.TestCase):
    def test_hypothesis_is_valid_not_empirical(self):
        r = audit(hypothesis())
        self.assertFalse(r["empirical_result_generated"])
        self.assertEqual(r["by_status"]["hypothesis"], 1)

    def test_no_promotion_from_e0(self):
        p = hypothesis()
        p["lessons"][0]["status"] = "validated_for_context"
        with self.assertRaises(LessonError):
            audit(p)

    def test_higher_grade_requires_dated_source(self):
        p = hypothesis()
        p["lessons"][0]["evidence_grade"] = "E3"
        with self.assertRaises(LessonError):
            audit(p)

    def test_validated_requires_independent_reviewer_and_commit(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="validated_for_context", evidence_grade="E4",
                 sources=[{"url": "https://example.org/paper",
                           "published_at_utc": "2026-10-11T12:00:00Z"}],
                 observed_data_ref="registry:snapshot-1", analyst="alice",
                 independent_reviewer="bob", reviewed_at_utc="2026-10-12T12:00:00Z",
                 analysis_commit="a"*40, data_sha256="b"*64,
                 sample_n=10, effect_size=0, interval=[-1, 1])
        r = audit(p)
        self.assertEqual(r["declared_validated_ids_needing_external_review"], ["SYN-001"])
        x["independent_reviewer"] = "alice"
        with self.assertRaises(LessonError):
            audit(p)

    def test_nonfinite_estimate_rejected(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="validated_for_context", evidence_grade="E4",
                 sources=[{"url": "https://example.org/paper",
                           "published_at_utc": "2026-10-11T12:00:00Z"}],
                 observed_data_ref="registry:snapshot-1", analyst="alice",
                 independent_reviewer="bob", reviewed_at_utc="2026-10-12T12:00:00Z",
                 analysis_commit="a"*40, data_sha256="b"*64,
                 sample_n=10, effect_size=float("nan"),
                 interval=[-1, 1])
        with self.assertRaises(LessonError):
            audit(p)

    def test_duplicate_id(self):
        p = hypothesis()
        p["lessons"].append(dict(p["lessons"][0]))
        with self.assertRaises(LessonError):
            audit(p)

    def test_untrusted_non_https_source(self):
        p = hypothesis()
        p["lessons"][0].update(evidence_grade="E1",
            sources=[{"url": "file:///tmp/fake", "published_at_utc": "2026-10-12T10:00:00Z"}])
        with self.assertRaises(LessonError):
            audit(p)


    def test_migrated_e0_fixture_from_competing_pr_is_not_empirical(self):
        sample = Path(__file__).resolve().parents[1] / "examples" / "lesson_registry.synthetic.json"
        report = audit(json.loads(sample.read_text(encoding="utf-8")))
        self.assertEqual(report["dataset_kind"], "synthetic")
        self.assertEqual(report["by_grade"]["E0"], 1)
        self.assertFalse(report["independent_verification"])
        self.assertFalse(report["empirical_result_generated"])

    def test_requires_explicit_schema_and_evidence_kind(self):
        for key in ("schema_version", "dataset_kind"):
            p = hypothesis()
            p.pop(key)
            with self.subTest(key=key), self.assertRaises(LessonError):
                audit(p)
        p = hypothesis()
        p["dataset_kind"] = "empirically_validated"
        with self.assertRaises(LessonError):
            audit(p)
        for invalid in ({}, [], None, True):
            p["dataset_kind"] = invalid
            with self.subTest(kind=str(invalid)), self.assertRaises(LessonError):
                audit(p)

    def test_e1_needs_frozen_source_and_analysis_provenance(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="exploratory", evidence_grade="E1",
                 sources=[{"url":"https://example.org/observational-report",
                           "published_at_utc":"2026-10-11T12:00:00Z"}])
        with self.assertRaisesRegex(LessonError, "analysis_commit"):
            audit(p)
        x["analysis_commit"] = "a" * 40
        with self.assertRaisesRegex(LessonError, "data_sha256"):
            audit(p)
        x["data_sha256"] = "b" * 64
        result = audit(p)
        self.assertEqual(result["by_grade"]["E1"], 1)
        self.assertFalse(result["independent_verification"])

    def test_hypothesis_cannot_claim_nonzero_grade(self):
        p = hypothesis()
        p["lessons"][0].update(evidence_grade="E1",
                               analysis_commit="a" * 40, data_sha256="b" * 64,
                               sources=[{"url":"https://example.org/study",
                                         "published_at_utc":"2026-10-11T12:00:00Z"}])
        with self.assertRaisesRegex(LessonError, "hypothesis status"):
            audit(p)

    def test_e2_requires_effect_interval_sample_and_provenance(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="exploratory", evidence_grade="E2",
                 sources=[{"url":"https://example.org/study",
                           "published_at_utc":"2026-10-11T12:00:00Z"}],
                 analysis_commit="a" * 40, data_sha256="b" * 64)
        with self.assertRaisesRegex(LessonError, "sample_n"):
            audit(p)
        x.update(sample_n=5, effect_size=4.0, interval=[0.0, 2.0])
        with self.assertRaisesRegex(LessonError, "enclosing"):
            audit(p)
        x["interval"] = [1.0, 6.0]
        self.assertEqual(audit(p)["by_grade"]["E2"], 1)
        for effect in (float("nan"), float("inf"), True):
            with self.subTest(effect=str(effect)):
                y = copy.deepcopy(p)
                y["lessons"][0]["effect_size"] = effect
                with self.assertRaisesRegex(LessonError, "finite"):
                    audit(y)

    def test_reviewers_cannot_differ_only_by_case(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="validated_for_context", evidence_grade="E4",
                 sources=[{"url":"https://example.org/study",
                           "published_at_utc":"2026-10-11T12:00:00Z"}],
                 observed_data_ref="private:synthetic-example",
                 analyst="ALICE", independent_reviewer="alice",
                 reviewed_at_utc="2026-10-12T12:00:00Z",
                 analysis_commit="a" * 40, data_sha256="b" * 64,
                 sample_n=5, effect_size=0.0, interval=[-1.0, 1.0])
        with self.assertRaisesRegex(LessonError, "distinct"):
            audit(p)

    def test_future_source_or_review_timestamp_rejected(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="exploratory", evidence_grade="E1",
                 analysis_commit="a" * 40, data_sha256="b" * 64,
                 sources=[{"url":"https://example.org/study",
                           "published_at_utc":"2099-01-01T00:00:00Z"}])
        with self.assertRaisesRegex(LessonError, "future"):
            audit(p)
        x["sources"][0]["published_at_utc"] = "2026-10-11T12:00:00Z"
        x.update(status="validated_for_context", evidence_grade="E4",
                 observed_data_ref="private:synthetic-example",
                 analyst="alpha", independent_reviewer="beta",
                 reviewed_at_utc="2099-01-01T00:00:00Z", sample_n=5,
                 effect_size=0.0, interval=[-1.0, 1.0])
        with self.assertRaisesRegex(LessonError, "future"):
            audit(p)

    def test_source_url_cannot_contain_credentials_or_fragment(self):
        p = hypothesis()
        x = p["lessons"][0]
        x.update(status="exploratory", evidence_grade="E1",
                 analysis_commit="a" * 40, data_sha256="b" * 64)
        for url in ("https://user:secret@example.org/report",
                    "https://example.org/report#tracking",
                    "https://example.org@evil.example/report"):
            with self.subTest(url=url):
                x["sources"] = [{"url":url,
                                  "published_at_utc":"2026-10-11T12:00:00Z"}]
                with self.assertRaisesRegex(LessonError, "clean HTTPS"):
                    audit(p)
        # Only basic URL hygiene is validated; trusted source identity
        # must still be established by a real independent evidence review.
        x["sources"] = [{"url":"https://evil.example/report",
                         "published_at_utc":"2026-10-11T12:00:00Z"}]
        self.assertEqual(audit(p)["by_grade"]["E1"], 1)

    def test_malformed_status_type_is_rejected(self):
        p = hypothesis()
        p["lessons"][0]["status"] = {}
        with self.assertRaises(LessonError):
            audit(p)


if __name__ == "__main__":
    unittest.main()
