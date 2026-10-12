"""Synthetic only: checks that unverified lessons are not auto-promoted."""
import unittest
from trending_study.lesson_registry import LessonError, audit


def hypothesis():
    return {"lessons": [{"id": "SYN-001", "title": "Synthetic task",
        "status": "hypothesis", "evidence_grade": "E0",
        "question": "Could setup documentation help?", "population": "fictional users",
        "comparison": "two fictional READMEs", "primary_outcome": "first-use pass",
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
                 analysis_commit="a"*40, sample_n=10, effect_size=0, interval=[-1, 1])
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
                 analysis_commit="a"*40, sample_n=10, effect_size=float("nan"),
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


    def test_malformed_status_type_is_rejected(self):
        p = hypothesis()
        p["lessons"][0]["status"] = {}
        with self.assertRaises(LessonError):
            audit(p)


if __name__ == "__main__":
    unittest.main()
