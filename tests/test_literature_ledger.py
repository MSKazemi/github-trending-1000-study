"""Artificial source screening; no review databases were searched."""
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from trending_study.literature_ledger import LiteratureError, audit, audit_file, main
from trending_study.data_integrity import MAX_FILE_BYTES


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

    def test_zero_or_empty_explicit_https_port_is_invalid(self):
        for link in ("https://doi.org:0/10.1000/XYZ",
                     "https://doi.org:/10.1000/XYZ"):
            payload = source()
            payload["records"][0]["source_url"] = link
            with self.subTest(link=link), self.assertRaises(LiteratureError):
                audit(payload)
        # A valid nondefault HTTPS port remains acceptable as documented.
        payload = source()
        payload["records"][0]["source_url"] = "https://example.org:8443/article"
        self.assertEqual(audit(payload)["decisions"]["include"], 1)

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

    def test_malformed_ports_rejected_without_changing_legitimate_sources(self):
        for url in ("https://example.org:not-a-port/paper",
                    "https://example.org:99999/paper", "https://example.org:-1/paper"):
            p = source()
            p["records"][0]["source_url"] = url
            with self.subTest(url=url), self.assertRaisesRegex(LiteratureError, "source_url"):
                audit(p)
        p = source()
        p["records"][0]["source_url"] = "https://example.org:443/paper"
        self.assertEqual(audit(p)["decisions"]["include"], 1)


class LiteratureFileIntegrityTests(unittest.TestCase):
    def test_regular_file_preserves_audit_output_and_exact_search_query(self):
        payload = source()
        payload["search_runs"][0]["query"] = 'title:("reuse code") AND year:[2020 TO 2026]'
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            self.assertEqual(audit_file(path), audit(payload))
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                main(["--input", str(path)])
            self.assertEqual(json.loads(stdout.getvalue()), audit(payload))

    def test_strict_decoding_rejects_ambiguous_or_extreme_values_before_audit(self):
        documents = ('{"search_runs":[],"search_runs":[]}',
                     '{"private":NaN}', '{"private":Infinity}',
                     '{"private":-Infinity}', '{"private":1e9999}',
                     '{"private":1e-9999}', '{"private":' + '1' * 1025 + '}')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.json"
            for raw in documents:
                path.write_text(raw, encoding="utf-8")
                with self.subTest(raw_prefix=raw[:30]), patch(
                    "trending_study.literature_ledger.audit") as called:
                    with self.assertRaisesRegex(LiteratureError, "strict UTF-8 JSON"):
                        audit_file(path)
                    called.assert_not_called()
            path.write_bytes(b'\xff')
            with self.assertRaisesRegex(LiteratureError, "strict UTF-8 JSON"):
                audit_file(path)

    def test_decoder_diagnostics_do_not_echo_private_keys_or_filename(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "private-personal-filename.json"
            path.write_text('{"private_credential_key":1,"private_credential_key":2}', encoding="utf-8")
            stderr = io.StringIO()
            with redirect_stderr(stderr), self.assertRaises(SystemExit) as exc:
                main(["--input", str(path)])
            self.assertEqual(exc.exception.code, 2)
            self.assertIn("strict UTF-8 JSON", stderr.getvalue())
            self.assertNotIn("private_credential_key", stderr.getvalue())
            self.assertNotIn(path.name, stderr.getvalue())
            self.assertNotIn("Traceback", stderr.getvalue())

    def test_oversized_regular_file_rejected_before_decoding(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "oversized.json"
            with path.open("wb") as stream:
                stream.truncate(MAX_FILE_BYTES + 1)
            with patch("trending_study.literature_ledger.decode_research_json") as decode:
                with self.assertRaisesRegex(LiteratureError, "byte limit"):
                    audit_file(path)
                decode.assert_not_called()

    def test_bounded_read_rejects_file_grown_after_size_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "grown.json"
            with path.open("wb") as stream:
                stream.truncate(MAX_FILE_BYTES + 1)
            stale_metadata = list(path.stat())
            stale_metadata[6] = 0  # fstat's stale size before concurrent growth.
            with patch("trending_study.literature_ledger.os.fstat",
                       return_value=os.stat_result(stale_metadata)):
                with patch("trending_study.literature_ledger.decode_research_json") as decode:
                    with self.assertRaisesRegex(LiteratureError, "byte limit"):
                        audit_file(path)
                    decode.assert_not_called()

    def test_directory_and_input_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaisesRegex(LiteratureError, "regular non-symlink"):
                audit_file(root)
            original = root / "ledger.json"
            original.write_text(json.dumps(source()), encoding="utf-8")
            alias = root / "alias.json"
            alias.symlink_to(original)
            with self.assertRaisesRegex(LiteratureError, "regular non-symlink"):
                audit_file(alias)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO unavailable")
    def test_fifo_cli_fails_promptly_without_writer_or_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.fifo"
            os.mkfifo(path)
            result = subprocess.run([sys.executable, "-m", "trending_study.literature_ledger",
                                     "--input", str(path)], capture_output=True, text=True, timeout=3)
            self.assertEqual(result.returncode, 2)
            self.assertIn("regular non-symlink", result.stderr)
            self.assertEqual(result.stdout, "")

    @unittest.skipUnless(hasattr(os, "O_NOFOLLOW"), "No-follow open unavailable")
    def test_open_refuses_symlink_even_if_initial_path_check_is_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = root / "ledger.json"
            original.write_text(json.dumps(source()), encoding="utf-8")
            alias = root / "alias.json"
            alias.symlink_to(original)
            with patch.object(Path, "is_symlink", return_value=False):
                with self.assertRaisesRegex(LiteratureError, "readable regular non-symlink"):
                    audit_file(alias)



if __name__ == "__main__":
    unittest.main()
