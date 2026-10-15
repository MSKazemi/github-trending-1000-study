"""Offline integrity checks for the dated, purposive hiring evidence seed.

These checks authenticate neither employers nor live vacancies. They protect
the versioned source ledger from accidental schema drift or false certainty.
"""
import csv
from datetime import date
from pathlib import Path
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / "references"
SEED = ROOT / "ai_hiring_job_leads_2026-10-13.csv"
AUDIT = ROOT / "ai_hiring_job_leads_source_audit_2026-10-13.csv"
EXPANSION = ROOT / "ai_hiring_expansion_leads_2026-10-13.csv"

EXPECTED_AUDIT = {
    "seed_row", "company", "job_title", "individual_official_url",
    "requisition_id", "source_granularity", "content_verification",
    "theme_codes", "short_description_paraphrase", "skills_as_advertised",
    "source_observation_date_utc", "posting_date_utc", "first_posted_date_utc",
    "is_confirmed_active", "analyst_notes",
}
EXPECTED_EXPANSION = {
    "company", "requisition_id", "job_title", "official_url",
    "theme_hypotheses", "description_paraphrase", "source_evidence_class",
    "collection_date_utc", "job_first_published_utc",
    "live_status_verified", "restriction",
}
# These are expected URL host/path shapes for this historical pilot, NOT
# verification of employer identity, posting content, or a live vacancy.
# They are NOT a general allowlist for future company sampling.
ORIGINS = {
    "OpenAI": ("openai.com", "/careers/"),
    "Anthropic": ("job-boards.greenhouse.io", "/anthropic/jobs/"),
    "Cursor": ("cursor.com", "/careers/"),
    "Amazon AWS": ("amazon.jobs", "/"),
    "Cohere": ("jobs.ashbyhq.com", "/cohere/"),
    "NVIDIA": ("nvidia.wd5.myworkdayjobs.com", "/"),
    "Google": ("www.google.com", "/about/careers/"),
}


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        headings = reader.fieldnames
        if not headings or len(set(headings)) != len(headings):
            raise AssertionError("missing or duplicate CSV headings: " + str(path))
        rows = list(reader)
    if any(None in row for row in rows):
        raise AssertionError("extra CSV fields: " + str(path))
    if any(any(value is None for value in row.values()) for row in rows):
        raise AssertionError("missing CSV cells: " + str(path))
    return set(headings), rows


def check_url(company, url):
    if not isinstance(url, str) or not url:
        raise AssertionError("empty source URL")
    parsed = urlsplit(url)
    expected_host, expected_prefix = ORIGINS[company]
    actual_host = (parsed.hostname or "").removeprefix("www.")
    if (parsed.scheme != "https" or
            actual_host != expected_host.removeprefix("www.") or
            not (parsed.path.startswith(expected_prefix) or
                 (company == "Cursor" and parsed.path.startswith("/fr/careers/"))) or
            parsed.username is not None or parsed.password is not None or
            parsed.query or parsed.fragment or parsed.port is not None):
        raise AssertionError("unexpected employer/ATS origin: " + url)


class HiringDataIntegrityTests(unittest.TestCase):
    def test_seed_and_audit_are_traceable_one_to_one(self):
        fields, seed = read_csv(SEED)
        self.assertIn("job_title", fields)
        self.assertIn("official_url", fields)
        audit_fields, audit = read_csv(AUDIT)
        self.assertEqual(audit_fields, EXPECTED_AUDIT)
        self.assertEqual(len(seed), 18)
        self.assertEqual(len(audit), 18)
        self.assertEqual(
            [int(row["seed_row"]) for row in audit], list(range(1, 19))
        )
        for historical, checked in zip(seed, audit):
            self.assertEqual(historical["company"], checked["company"])
            self.assertEqual(historical["job_title"], checked["job_title"])
        # An audit must supplement the historical seed, never erase it.

    def test_source_audit_has_consistent_identity_and_missingness(self):
        _, rows = read_csv(AUDIT)
        urls = set()
        reqs = set()
        for row in rows:
            with self.subTest(row=row["seed_row"]):
                check_url(row["company"], row["individual_official_url"])
                u = row["individual_official_url"].rstrip("/")
                self.assertNotIn(u, urls)
                urls.add(u)
                self.assertIn(row["source_granularity"], {
                    "direct_individual", "direct_individual_indexed",
                })
                self.assertIn(row["content_verification"], {
                    "read", "read_indexed_text", "identity_hold",
                })
                self.assertEqual(row["is_confirmed_active"], "unknown")
                self.assertEqual(row["posting_date_utc"], "")
                self.assertEqual(row["first_posted_date_utc"], "")
                self.assertEqual(row["source_observation_date_utc"],
                                 "2026-10-13")
                self.assertTrue(row["theme_codes"].strip())
                self.assertTrue(row["short_description_paraphrase"].strip())
                self.assertLess(len(row["short_description_paraphrase"]), 350)
                if row["content_verification"] == "identity_hold":
                    self.assertIn("identity", row["analyst_notes"].lower())
                if row["content_verification"] == "read_indexed_text":
                    self.assertIn("index", row["analyst_notes"].lower())
                req_id = row["requisition_id"]
                if req_id:
                    self.assertIn(req_id.casefold(), u.casefold())
                    key = (row["company"], req_id.casefold())
                    self.assertNotIn(key, reqs)
                    reqs.add(key)
        self.assertTrue(any(
            row["content_verification"] == "identity_hold" for row in rows
        ), "identity-conflict evidence must remain documented")

    def test_expansion_is_not_misrepresented_as_live_census(self):
        fields, rows = read_csv(EXPANSION)
        self.assertEqual(fields, EXPECTED_EXPANSION)
        self.assertEqual(len(rows), 6)
        urls = set()
        reqs = set()
        for row in rows:
            with self.subTest(requisition=row["requisition_id"]):
                check_url(row["company"], row["official_url"])
                self.assertNotIn(row["official_url"], urls)
                urls.add(row["official_url"])
                key = (row["company"], row["requisition_id"].casefold())
                self.assertNotIn(key, reqs)
                reqs.add(key)
                self.assertIn(row["requisition_id"].casefold(),
                              row["official_url"].casefold())
                self.assertEqual(row["live_status_verified"], "no")
                self.assertEqual(row["job_first_published_utc"], "")
                self.assertEqual(row["collection_date_utc"], "2026-10-13")
                self.assertIn(row["source_evidence_class"], {
                    "official_individual_page", "official_individual_search_index",
                })
                self.assertTrue(row["description_paraphrase"].strip())
                self.assertTrue(row["restriction"].strip())
        self.assertEqual(set(row["company"] for row in rows),
                         {"Google", "NVIDIA"})

    def test_access_mode_and_identity_quarantine_are_preserved(self):
        _, rows = read_csv(AUDIT)
        held = [r for r in rows if r["content_verification"] == "identity_hold"]
        self.assertEqual(len(held), 1, "exactly one source has a known identity hold")
        self.assertEqual(held[0]["company"], "Cursor")
        for row in rows:
            with self.subTest(seed_row=row["seed_row"]):
                if row["content_verification"] == "read":
                    self.assertEqual(row["source_granularity"], "direct_individual")
                else:
                    self.assertEqual(row["source_granularity"],
                                     "direct_individual_indexed")
                if row["content_verification"] == "identity_hold":
                    note = (row["short_description_paraphrase"] + " " +
                            row["analyst_notes"]).casefold()
                    self.assertIn("spacexai", note)

    def test_seed_title_only_rows_and_unknown_dates_are_not_promoted(self):
        _, rows = read_csv(SEED)
        self.assertEqual(sum(r["source_granularity"] == "index_only"
                             for r in rows), 8)
        for row in rows:
            with self.subTest(title=row["job_title"]):
                self.assertEqual(row["publication_date_utc"], "")
                self.assertEqual(row["job_posting_date_utc"], "")
                if row["source_granularity"] == "index_only":
                    self.assertEqual(row["source_evidence_class"],
                                     "official_careers_index")
                    self.assertIn("title-only",
                                  row["paraphrased_evidence"].casefold())
                else:
                    self.assertEqual(row["source_granularity"], "individual")
                    self.assertEqual(row["source_evidence_class"],
                                     "official_individual_page")

    def test_original_and_expansion_have_no_overlapping_verified_ids(self):
        _, audited = read_csv(AUDIT)
        _, expansion = read_csv(EXPANSION)
        urls = {r["individual_official_url"].rstrip("/").casefold()
                for r in audited}
        ids = {(r["company"], r["requisition_id"].casefold())
               for r in audited if r["requisition_id"]}
        for row in expansion:
            with self.subTest(requisition=row["requisition_id"]):
                self.assertNotIn(row["official_url"].rstrip("/").casefold(),
                                 urls)
                self.assertNotIn((row["company"],
                                  row["requisition_id"].casefold()), ids)

    def test_observation_dates_are_calendar_dates_not_job_publication(self):
        for path, date_col in ((AUDIT, "source_observation_date_utc"),
                               (EXPANSION, "collection_date_utc")):
            _, rows = read_csv(path)
            for row in rows:
                with self.subTest(path=path.name):
                    self.assertEqual(date.fromisoformat(row[date_col]),
                                     date(2026, 10, 13))


if __name__ == "__main__":
    unittest.main()
