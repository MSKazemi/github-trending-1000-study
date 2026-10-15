"""Offline structural regression tests for candidate company source ledgers.

Passing these tests DOES NOT verify URLs, company claims, release dates, source
rights, independent human review, outcomes, adoption or environmental benefits.
"""
import csv
import io
from pathlib import Path
import unittest

from scripts.check_research_artifacts import (
    IntegrityError,
    _COMPANY_EVENT_COLUMNS,
    validate_text,
)

LEDGER = Path(
    "research/company-intelligence/2026-04-12_2026-10-12/005-meta.events.csv"
)


def sample(event_id="CI-005-01", date="2026-05-01", **updates):
    base = {field: "" for field in _COMPANY_EVENT_COLUMNS}
    base.update({
        "event_id": event_id,
        "company_id": "005",
        "company_label": "Synthetic Company",
        "product": "Synthetic Product",
        "source_url": "https://example.invalid/lead/" + event_id,
        "source_title": "Synthetic first-party claim",
        "source_publisher": "Synthetic Publisher",
        "source_type": "first_party",
        "published_utc": date,
        "event_date_utc": "",
        "accessed_utc": "2026-10-14",
        "kind": "company_announcement",
        "claim_summary": "This invented input is not real evidence",
        "feature": "none",
        "availability": "unverified",
        "status": "reported_undetermined",
        "study_construct": "M1",
        "limitation": "No independent research review",
        "confidence": "E0_UNVERIFIED",
        "duplicate_event_group": "",
        "independent_check_url": "",
    })
    base.update(updates)
    return base


def render(rows, extra_column=False):
    columns = list(_COMPANY_EVENT_COLUMNS)
    if extra_column:
        columns.append("evidence_tier")
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        if extra_column:
            row = {**row, "evidence_tier": "E1"}
        writer.writerow(row)
    return stream.getvalue()


class CompanyEventSemanticIntegrityTests(unittest.TestCase):
    def assert_invalid(self, rows, match, path=LEDGER):
        with self.assertRaisesRegex(IntegrityError, match):
            validate_text(path, render(rows))

    def test_both_existing_21_and_22_column_variants(self):
        self.assertEqual(validate_text(LEDGER, render([sample()])), 1)
        self.assertEqual(validate_text(LEDGER, render([sample()], True)), 1)

    def test_two_dated_events_may_share_a_changelog_url(self):
        source = "https://docs.example.org/changelog"
        rows = [
            sample(event_id="CI-005-01", date="2026-05-01", source_url=source),
            sample(event_id="CI-005-02", date="2026-06-01", source_url=source),
        ]
        self.assertEqual(validate_text(LEDGER, render(rows)), 2)

    def test_duplicate_event_ids_rejected_even_if_urls_differ(self):
        rows = [sample(), sample(source_url="https://example.invalid/other")]
        self.assert_invalid(rows, "repeated event_id")

    def test_wrong_company_id_rejected(self):
        self.assert_invalid([sample(company_id="006")], "company_id")

    def test_invalid_or_out_of_window_publication_dates(self):
        for value in ("2026-02-01", "2026-10-13", "2026-02-30", "2026-5-1", ""):
            with self.subTest(value=value):
                self.assert_invalid([sample(published_utc=value)],
                                    "published_utc|publication outside study window")

    def test_invalid_optional_event_and_access_dates(self):
        for field in ("event_date_utc", "accessed_utc"):
            with self.subTest(field=field):
                self.assert_invalid([sample(**{field: "2026-13-50"})], field)

    def test_nonchronological_source_rows_rejected(self):
        self.assert_invalid([
            sample(event_id="CI-005-01", date="2026-06-02"),
            sample(event_id="CI-005-02", date="2026-06-01"),
        ], "nonchronological")

    def test_invalid_status_and_undisclosed_reporter(self):
        self.assert_invalid([sample(status="definitely_shipped")], "source status")
        self.assert_invalid([sample(source_publisher="  ")], "source_publisher")

    def test_missing_source_title_or_confidence_rejected(self):
        self.assert_invalid([sample(source_title="")], "source_title")
        self.assert_invalid([sample(confidence="")], "confidence")

    def test_url_scheme_credentials_and_malformed_ports_rejected(self):
        bad = [
            "http://example.org/test",
            "https://user:secret@example.org/test",
            "https://example.org:99999/test",
            "https://example.org:banana/test",
            "https://example.org/has a space",
            "https://",
            "javascript:alert(1)",
            "https://example.org/ \n",
        ]
        for url in bad:
            with self.subTest(url=url):
                self.assert_invalid([sample(source_url=url)], "source_url")

    def test_future_vendor_promises_not_reclassified(self):
        row = sample(
            status="announced_only",
            event_date_utc="2027-04-30",
            claim_summary="Hypothetical future policy, not shipped",
        )
        self.assertEqual(validate_text(LEDGER, render([row])), 1)

    def test_unverified_but_well_formed_source_is_not_auto_approved(self):
        # Syntax cannot establish that a domain exists or a claim is true.
        self.assertEqual(validate_text(LEDGER, render([sample()])), 1)

    def test_archives_not_forced_to_new_event_schema(self):
        path = Path(
            "research/company-intelligence/2026-04-12_2026-10-12/"
            "source-archives/005-meta.2026-10-12-source-ledger.csv"
        )
        self.assertEqual(validate_text(path, "legacy_id,claim\nold,unverified\n"), 1)

    def test_unexpected_company_schema_and_bad_filename_rejected(self):
        raw = render([sample()])
        raw = raw.replace("source_publisher", "unapproved_field", 1)
        with self.assertRaisesRegex(IntegrityError, "missing or unsupported"):
            validate_text(LEDGER, raw)
        invalid_name = Path(
            "research/company-intelligence/2026-04-12_2026-10-12/"
            "meta.events.csv"
        )
        self.assert_invalid([sample()], "NNN-slug", path=invalid_name)

    def test_bad_company_window_rejected(self):
        path = Path("research/company-intelligence/2026-10-12_2026-04-12/005-meta.events.csv")
        self.assert_invalid([sample()], "window ends before it begins", path=path)

    def test_all_checked_in_canonical_company_ledgers(self):
        root = Path(__file__).resolve().parents[1]
        folder = root / "research/company-intelligence/2026-04-12_2026-10-12"
        files = sorted(folder.glob("*.events.csv"))
        self.assertTrue(files, "at least one checked-in company ledger is required")
        for path in files:
            with self.subTest(path=path.name):
                self.assertGreater(validate_text(path, path.read_text(encoding="utf-8")), 0)


if __name__ == "__main__":
    unittest.main()
