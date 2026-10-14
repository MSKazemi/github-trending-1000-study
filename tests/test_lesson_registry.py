"""Synthetic only: checks that unverified lessons are not auto-promoted."""
import copy
import json
from pathlib import Path
import contextlib
import io
import tempfile
import unittest
from trending_study.lesson_registry import LessonError, audit, audit_file, main


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
        p["dataset_kind"] = "self_reported"
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
        p["dataset_kind"] = "self_reported"
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
        p["dataset_kind"] = "self_reported"
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
        p["dataset_kind"] = "self_reported"
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



def v11_hypothesis():
    p = hypothesis()
    p["schema_version"] = "1.1"
    p["lessons"][0].update(research_question_id="GRQ1", result_kind="not_estimated")
    return p


def v11_observation():
    p = v11_hypothesis()
    x = p["lessons"][0]
    x.update(status="exploratory", evidence_grade="E1",
             observed_at_utc="2026-10-12T12:00:00Z",
             observed_data_ref="synthetic:fixture-only",
             sources=[{"url": "https://example.org/synthetic-paper",
                       "published_at_utc": "2026-10-11T12:00:00Z"}],
             analysis_commit="a" * 40, data_sha256="b" * 64)
    return p


def v11_estimate():
    p = v11_observation()
    p["lessons"][0].update(evidence_grade="E2", result_kind="null_compatible",
        sample_n=12, effect_size=0.1, interval=[-0.3, 0.4],
        interval_level=0.95, effect_unit="task-success difference",
        analysis_method="synthetic demonstration only")
    return p


class LessonRegistryV11Tests(unittest.TestCase):
    def test_versioned_sample_is_nonempirical(self):
        p = v11_hypothesis()
        self.assertEqual(audit(p)["schema_version"], "1.1")
        self.assertEqual(audit(p)["independently_verified_lesson_count"], 0)
        self.assertFalse(audit(p)["v1_0_legacy_input"])
        self.assertTrue(audit(hypothesis())["v1_0_legacy_input"])

    def test_schema_disallows_unrecognized_private_fields_at_every_level(self):
        p = v11_observation()
        for scope, key in [(p, "raw_log"), (p["lessons"][0], "prompt"),
                           (p["lessons"][0]["sources"][0], "private_user_email")]:
            with self.subTest(key=key):
                scope[key] = "sensitive-content-not-for-public-git"
                with self.assertRaisesRegex(LessonError, "unsupported field"):
                    audit(p)
                del scope[key]

    def test_synthetic_validated_declaration_is_rejected_even_with_review(self):
        p = v11_estimate()
        x = p["lessons"][0]
        x.update(evidence_grade="E4", status="validated_for_context",
                 analyst="reviewer-a", independent_reviewer="reviewer-b",
                 reviewed_at_utc="2026-10-13T12:00:00Z",
                 review_record_ref="synthetic:review",
                 observed_data_ref="synthetic:data")
        with self.assertRaisesRegex(LessonError, "synthetic records"):
            audit(p)
        p["dataset_kind"] = "self_reported"
        r = audit(p)
        self.assertEqual(r["declared_validated_ids_needing_external_review"], ["SYN-001"])
        self.assertEqual(r["independently_verified_lesson_count"], 0)
        p["schema_version"] = "1.0"
        p["dataset_kind"] = "synthetic"
        with self.assertRaisesRegex(LessonError, "synthetic records"):
            audit(p)

    def test_e1_requires_explicit_rq_and_dated_observation(self):
        p = v11_observation()
        x = p["lessons"][0]
        for key in ("research_question_id", "observed_data_ref", "observed_at_utc"):
            with self.subTest(key=key):
                value = x.pop(key)
                with self.assertRaises(LessonError):
                    audit(p)
                x[key] = value
        self.assertEqual(audit(p)["by_grade"]["E1"], 1)

    def test_e2_metadata_and_missingness_are_not_zero(self):
        p = v11_estimate()
        x = p["lessons"][0]
        for key in ("interval_level", "effect_unit", "analysis_method", "result_kind"):
            with self.subTest(key=key):
                value = x.pop(key)
                with self.assertRaises(LessonError):
                    audit(p)
                x[key] = value
        x["interval_level"] = True
        with self.assertRaisesRegex(LessonError, "interval_level"):
            audit(p)
        x["interval_level"] = 0.95
        x["effect_size"] = None
        with self.assertRaisesRegex(LessonError, "finite"):
            audit(p)

    def test_null_compatible_is_not_proof_of_no_effect(self):
        p = v11_estimate()
        self.assertEqual(audit(p)["by_status"]["exploratory"], 1)
        x = p["lessons"][0]
        x["interval"] = [0.2, 0.5]
        x["effect_size"] = 0.3
        with self.assertRaisesRegex(LessonError, "containing 0"):
            audit(p)
        x["result_kind"] = "estimated"
        self.assertEqual(audit(p)["by_grade"]["E2"], 1)

    def test_e0_does_not_turn_absence_into_zero(self):
        p = v11_hypothesis()
        x = p["lessons"][0]
        x["sample_n"] = 0
        with self.assertRaisesRegex(LessonError, "unknown sample_n"):
            audit(p)
        x["sample_n"] = None
        x["effect_size"] = 0
        with self.assertRaisesRegex(LessonError, "cannot present"):
            audit(p)

    def test_supersession_requires_present_noncyclic_target(self):
        p = v11_hypothesis()
        x = p["lessons"][0]
        x.update(status="superseded", superseded_by="SYN-002")
        with self.assertRaisesRegex(LessonError, "reference"):
            audit(p)
        y = copy.deepcopy(x)
        y.update(id="SYN-002", status="hypothesis", superseded_by=None)
        p["lessons"].append(y)
        self.assertEqual(audit(p)["by_status"]["superseded"], 1)
        y.update(status="superseded", superseded_by="SYN-001")
        with self.assertRaisesRegex(LessonError, "cycle"):
            audit(p)

    def test_direct_cli_rejects_duplicate_and_nonstandard_json(self):
        with tempfile.TemporaryDirectory() as directory:
            f = Path(directory) / "evidence.json"
            for content in ('{"schema_version":"1.0","schema_version":"1.1"}',
                            '{"schema_version":"1.1","lessons":[NaN]}'):
                with self.subTest(content=content):
                    f.write_text(content, encoding="utf-8")
                    with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
                        main(["--input", str(f)])
                    self.assertEqual(cm.exception.code, 2)

    def test_cli_refuses_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            d = Path(directory)
            target = d / "real.json"
            target.write_text(json.dumps(v11_hypothesis()), encoding="utf-8")
            link = d / "alias.json"
            try:
                link.symlink_to(target)
            except (NotImplementedError, OSError):
                self.skipTest("filesystem does not support symlinks")
            with self.assertRaisesRegex(LessonError, "non-symlink"):
                audit_file(link)

    def test_v11_accepted_fixture_is_synthetic_and_versioned(self):
        example = Path(__file__).resolve().parents[1] / "examples" / "lesson_registry.synthetic.json"
        r = audit_file(example)
        self.assertEqual(r["schema_version"], "1.1")
        self.assertEqual(r["independently_verified_lesson_count"], 0)

    def test_source_rejects_malformed_authority_and_whitespace(self):
        p = v11_observation()
        x = p["lessons"][0]["sources"][0]
        for url in ("https://[bad-host/example", "https://example.org:bad/path",
                    "https://example.org/path\nInjected"):
            with self.subTest(url=url):
                x["url"] = url
                with self.assertRaises(LessonError):
                    audit(p)


if __name__ == "__main__":
    unittest.main()
