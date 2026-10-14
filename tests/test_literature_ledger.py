"""Artificial source screening; no review databases were searched."""
import unittest
from trending_study.literature_ledger import LiteratureError, audit


def source():
    return {"search_runs": [{"run_id": "r1", "database": "OpenAlex",
                             "query": "reuse software AND agents",
                             "searched_at_utc": "2026-10-12T12:00:00Z"}],
            "records": [{"record_id": "s1", "run_id": "r1",
                         "title": "Synthetic Evidence Example", "publication_year": 2026,
                         "doi": "https://doi.org/10.1000/XYZ",
                         "source_url": "https://doi.org/10.1000/XYZ",
                         "source_type": "peer_reviewed",
                         "decision": "include", "study_extract": {
                             "design": "illustrative only", "population": "fictional",
                             "outcome": "not measured", "limitations": "synthetic"}}]}


class LiteratureLedgerTests(unittest.TestCase):
    def test_valid_input(self):
        r = audit(source())
        self.assertEqual(r["decisions"]["include"], 1)
        self.assertEqual(r["possible_duplicate_groups"], {})

    def test_duplicate_normalized_doi_flag(self):
        p = source()
        duplicate = dict(p["records"][0])
        duplicate.update(record_id="s2", doi="DOI:10.1000/xyz", decision="pending")
        p["records"].append(duplicate)
        r = audit(p)
        self.assertEqual(r["possible_duplicate_groups"]["doi:10.1000/xyz"], ["s1", "s2"])

    def test_common_doi_prefix_variants_normalize_to_same_identity(self):
        p = source()
        first = p["records"][0]
        second = dict(first, record_id="s2", doi="DOI: 10.1000/xyz",
                      decision="pending")
        third = dict(first, record_id="s3", doi="https://dx.doi.org/10.1000/XYZ",
                     decision="pending")
        p["records"].extend([second, third])
        report = audit(p)
        self.assertEqual(report["possible_duplicate_groups"]["doi:10.1000/xyz"],
                         ["s1", "s2", "s3"])
        self.assertEqual(report["screened_records"], 3)

    def test_exclusion_requires_reason(self):
        p = source()
        p["records"][0]["decision"] = "exclude"
        with self.assertRaises(LiteratureError):
            audit(p)

    def test_include_requires_extraction(self):
        p = source()
        del p["records"][0]["study_extract"]
        with self.assertRaises(LiteratureError):
            audit(p)

    def test_included_without_source_url_must_not_enter_evidence(self):
        payload = source()
        del payload["records"][0]["source_url"]
        with self.assertRaisesRegex(LiteratureError, "source_url"):
            audit(payload)
        # Unverified retrieved leads remain pending rather than being
        # invented as independently sourced included studies.
        payload["records"][0]["decision"] = "pending"
        self.assertEqual(audit(payload)["decisions"]["pending"], 1)

    def test_included_source_url_rejects_credentials_fragments_and_bad_authorities(self):
        for link in (
            "", "http://doi.org/10.1000/XYZ",
            "https:///missing-host", "https://me:secret@doi.org/10.1000/XYZ",
            "https://doi.org/10.1000/XYZ#note",
            "https://doi.org/10.1000/XYZ?token=private",
            "https://doi.org/10.1000/XYZ" + chr(10),
            "https://[malformed/10.1000/XYZ",
        ):
            payload = source()
            payload["records"][0]["source_url"] = link
            with self.subTest(url=link), self.assertRaises(LiteratureError):
                audit(payload)

    def test_canonical_doi_source_url_is_structural_only(self):
        self.assertEqual(audit(source())["decisions"]["include"], 1)
        # An HTTPS string is *not* independent content verification.
        payload = source()
        payload["records"][0]["source_url"] = "https://example.org/unchecked"
        self.assertEqual(audit(payload)["decisions"]["include"], 1)

    def test_run_identity_required(self):
        p = source()
        p["records"][0]["run_id"] = "missing"
        with self.assertRaises(LiteratureError):
            audit(p)

    def test_rejects_naive_timestamp(self):
        p = source()
        p["search_runs"][0]["searched_at_utc"] = "2026-10-12"
        with self.assertRaises(LiteratureError):
            audit(p)

    def test_preprint_not_peer_reviewed_by_default(self):
        p = source()
        p["records"][0]["source_type"] = "preprint"
        self.assertEqual(audit(p)["decisions"]["include"], 1)


    def test_title_year_cross_doi_collision_is_review_only(self):
        p = source()
        q = dict(p["records"][0])
        q.update(record_id="s2", doi="10.1000/another", decision="pending")
        p["records"].append(q)
        report = audit(p)
        self.assertEqual(report["possible_duplicate_groups"], {})
        self.assertEqual(list(report["title_year_collision_groups"].values()), [["s1", "s2"]])
        self.assertEqual(report["screened_records"], 2)
        self.assertFalse(report["prisma_flow_authenticated"])

    def test_future_search_timestamp_is_not_historical_evidence(self):
        p = source()
        p["search_runs"][0]["searched_at_utc"] = "2099-01-01T00:00:00Z"
        with self.assertRaisesRegex(LiteratureError, "future"):
            audit(p)

    def test_source_publication_cannot_postdate_search(self):
        p = source()
        p["records"][0]["publication_year"] = 2027
        with self.assertRaisesRegex(LiteratureError, "postdate"):
            audit(p)

    def test_malformed_source_type_is_rejected(self):
        p = source()
        p["records"][0]["source_type"] = {}
        with self.assertRaises(LiteratureError):
            audit(p)

    def test_unhashable_run_id_is_controlled_validation_error(self):
        for invalid in (None, [], {}, 123, " "):
            with self.subTest(run_id=invalid):
                p = source()
                p["records"][0]["run_id"] = invalid
                with self.assertRaisesRegex(LiteratureError, "existing search run"):
                    audit(p)



if __name__ == "__main__":
    unittest.main()
