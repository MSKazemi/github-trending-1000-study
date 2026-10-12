import copy
import json
from pathlib import Path
import unittest

from trending_study.lesson_registry import LessonError, evaluate

EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "lesson_registry.synthetic.json"


class LessonRegistryTests(unittest.TestCase):
    def test_hypothesis_only(self):
        out = evaluate(json.loads(EXAMPLE.read_text()))
        self.assertEqual(out["grades"]["E0"], 1)
        self.assertIsNone(out["validated_scientific_findings"])
        self.assertFalse(out["independent_verification"])

    def test_claim_grade_requires_provenance(self):
        doc = json.loads(EXAMPLE.read_text())
        doc["lessons"][0]["grade"] = "E2"
        with self.assertRaises(LessonError):
            evaluate(doc)

    def test_no_unreviewed_validation(self):
        doc = json.loads(EXAMPLE.read_text())
        doc["lessons"][0]["status"] = "validated_for_context"
        with self.assertRaises(LessonError):
            evaluate(doc)

    def test_duplicate_ids_rejected(self):
        doc = json.loads(EXAMPLE.read_text())
        doc["lessons"].append(copy.deepcopy(doc["lessons"][0]))
        with self.assertRaises(LessonError):
            evaluate(doc)

    def test_reject_untrusted_source_http(self):
        doc = json.loads(EXAMPLE.read_text())
        doc["lessons"][0]["sources"] = [{"url": "http://example.com", "published_date": "2026-10-12"}]
        with self.assertRaises(LessonError):
            evaluate(doc)


if __name__ == "__main__":
    unittest.main()
