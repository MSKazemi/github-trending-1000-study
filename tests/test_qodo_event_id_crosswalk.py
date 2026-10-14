"""Offline Qodo source-ID preservation regression, not a vendor fact check."""
import csv
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
QODO = ROOT / "research/company-intelligence/2026-04-12_2026-10-12"
SOURCE = QODO / "source-archives/018-qodo.2026-10-12-source-ledger.csv"
WORKING = QODO / "018-qodo.events.csv"
CROSSWALK = QODO / "source-archives/018-qodo.2026-10-14-event-id-crosswalk.json"


def by_event_id(path):
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    keyed = {row["event_id"]: row for row in rows}
    if len(keyed) != len(rows):
        raise ValueError("duplicate event_id in " + path.name)
    return keyed


class QodoCrosswalkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = by_event_id(SOURCE)
        cls.working = by_event_id(WORKING)
        cls.crosswalk = json.loads(CROSSWALK.read_text(encoding="utf-8"))

    def test_scope_is_provisional_not_independent_validation(self):
        info = self.crosswalk
        self.assertEqual(info["schema_version"], "1.0")
        self.assertEqual(info["company_id"], "018")
        self.assertEqual(info["independent_source_review"], "pending")
        self.assertIs(info["not_empirical_validation"], True)
        self.assertEqual(info["source_ledger"], SOURCE.name)
        self.assertEqual(info["canonical_events"], "../018-qodo.events.csv")
        self.assertIn("publisher-controlled statement",
                      info["meaning"]["archived_evidence_tier_E1"])
        self.assertTrue(info["review_gates"])

    def test_all_legacy_ids_preserved_with_explicit_url_mapping(self):
        mappings = self.crosswalk["mappings"]
        self.assertEqual(len(mappings), len(self.source))
        self.assertEqual({m["archived_event_id"] for m in mappings},
                         set(self.source))
        self.assertEqual(len({m["archived_event_id"] for m in mappings}),
                         len(mappings))
        self.assertEqual(len({m["working_event_id"] for m in mappings}),
                         len(mappings))
        for item in mappings:
            with self.subTest(archived=item["archived_event_id"]):
                original = self.source[item["archived_event_id"]]
                current = self.working[item["working_event_id"]]
                if item["relation"] != "publisher_url_correction_same_event_id":
                    self.assertEqual(original["source_url"], current["source_url"])
                else:
                    self.assertEqual(original["source_url"], item["original_url"])
                    self.assertEqual(current["source_url"], item["corrected_url"])
                    self.assertNotEqual(item["original_url"], item["corrected_url"])
                self.assertEqual(original["published_utc"],
                                 current["published_utc"])
                self.assertEqual(original["company_id"], current["company_id"])
                self.assertEqual(original["evidence_tier"], "E1")
                # Neither ledger can infer the actual deployment date.
                self.assertEqual(original["event_date_utc"], "")
                self.assertEqual(current["event_date_utc"], "")
                if item["relation"] == "identical_id_and_source_url":
                    self.assertEqual(item["archived_event_id"],
                                     item["working_event_id"])
                    self.assertEqual(current["confidence"],
                                     "E0_ARCHIVED_UNREVIEWED_VENDOR_LEAD")
                elif item["relation"] == "source_url_and_publication_date_alias":
                    self.assertNotEqual(item["archived_event_id"],
                                        item["working_event_id"])
                    self.assertEqual(current["confidence"],
                                     "E1_VENDOR_DOCUMENT_ONLY")
                elif item["relation"] == "publisher_url_correction_same_event_id":
                    self.assertEqual(item["archived_event_id"], "CI-018-06")
                    self.assertEqual(item["working_event_id"], "CI-018-06")
                    self.assertEqual(current["confidence"],
                                     "E0_ARCHIVED_UNREVIEWED_VENDOR_LEAD")
                    self.assertTrue(item.get("note"))
                else:
                    self.fail("unreviewed event identifier mapping type")

    def test_archived_agentic_toolbox_identifier_is_not_lost(self):
        aliases = [item for item in self.crosswalk["mappings"]
                   if item["relation"] == "source_url_and_publication_date_alias"]
        self.assertEqual(
            [(item["archived_event_id"], item["working_event_id"])
             for item in aliases],
            [("CI-018-04", "CI2026-018-003")],
        )
        self.assertTrue(aliases[0].get("note"))
        self.assertNotIn("CI-018-04", self.working)
        self.assertIn("CI-018-04", self.source)
        self.assertIn("CI2026-018-003", self.working)


if __name__ == "__main__":
    unittest.main()
