"""Offline destructive-overwrite regressions for immutable research captures."""
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from trending_study.__main__ import capture, enrich, parse_trending, pilot_parse
from trending_study.pilot import build_capture_manifest
from trending_study.safe_io import (
    ProvenanceWriteError, disjoint, publish_once, publish_json, publish_jsonl,
)

FIXTURE = Path(__file__).parent / "fixtures" / "trending.html"


def args(**kwargs):
    return type("Args", (), kwargs)()


class SourceImmutabilityTests(unittest.TestCase):
    def test_existing_artifact_never_replaced(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "observations.jsonl"
            target.write_bytes(b"PROTECTED")
            with self.assertRaisesRegex(ProvenanceWriteError, "overwrite"):
                publish_jsonl(target, [{"value": "new"}])
            self.assertEqual(target.read_bytes(), b"PROTECTED")

    def test_staged_artifact_publishes_valid_complete_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "nested" / "record.json"
            publish_json(target, {"key": "value"})
            self.assertEqual(json.loads(target.read_text()), {"key": "value"})
            self.assertEqual(list(target.parent.glob(".capture-pending-*")), [])

    def test_symlink_alias_detected(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / "raw.html"
            alias = Path(d) / "alias.html"
            source.write_bytes(b"PROTECTED")
            alias.symlink_to(source)
            with self.assertRaisesRegex(ProvenanceWriteError, "overlap"):
                disjoint(source, alias)

    def test_stage_publish_failure_never_creates_partial_single_file(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / "new.jsonl"
            with patch("trending_study.safe_io.os.link", side_effect=OSError("synthetic failure")):
                with self.assertRaisesRegex(ProvenanceWriteError, "no output published"):
                    publish_once([(target, b"123")])
            self.assertFalse(target.exists())
            self.assertEqual(list(Path(d).glob(".capture-pending-*")), [])

    def test_partial_bundle_preserved_and_explicitly_invalid(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.html"
            manifest = Path(d) / "manifest.json"
            actual_link = os.link
            calls = []

            def fail_second(src, dest):
                calls.append(str(dest))
                if len(calls) == 2:
                    raise OSError("simulated disk interruption")
                return actual_link(src, dest)

            with patch("trending_study.safe_io.os.link", side_effect=fail_second):
                with self.assertRaisesRegex(ProvenanceWriteError, "partial bundle"):
                    publish_once([(raw, b"SOURCE"), (manifest, b'{"sha":"x"}')])
            self.assertEqual(raw.read_bytes(), b"SOURCE")
            self.assertFalse(manifest.exists())
            self.assertEqual(list(Path(d).glob(".capture-pending-*")), [])
            with self.assertRaisesRegex(ProvenanceWriteError, "overwrite"):
                publish_once([(raw, b"NEW")])
            self.assertEqual(raw.read_bytes(), b"SOURCE")

    def test_legacy_parse_same_path_cannot_destroy_html(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.html"
            original = FIXTURE.read_bytes()
            raw.write_bytes(original)
            with self.assertRaisesRegex(ProvenanceWriteError, "overlap"):
                parse_trending(args(input=str(raw), output=str(raw),
                                    date="2026-10-12", window="daily"))
            self.assertEqual(raw.read_bytes(), original)

    def test_legacy_parse_refuses_existing_derived_file(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.html"
            out = Path(d) / "out.jsonl"
            raw.write_bytes(FIXTURE.read_bytes())
            out.write_bytes(b"OLD")
            with self.assertRaisesRegex(ProvenanceWriteError, "overwrite"):
                parse_trending(args(input=str(raw), output=str(out),
                                    date="2026-10-12", window="daily"))
            self.assertEqual(out.read_bytes(), b"OLD")

    def test_enrich_same_path_rejected_before_request(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / "rows.jsonl"
            source.write_text('{"repository":"sample/demo"}\n')
            with patch("trending_study.__main__.urlopen") as network:
                with self.assertRaisesRegex(ProvenanceWriteError, "overlap"):
                    enrich(args(input=str(source), output=str(source)))
                network.assert_not_called()
            self.assertEqual(source.read_text(), '{"repository":"sample/demo"}\n')

    def test_capture_existing_output_rejected_before_network(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.html"
            raw.write_bytes(b"PREVIOUS CAPTURE")
            manifest = Path(d) / "manifest.json"
            with patch("trending_study.__main__.urlopen") as network:
                with self.assertRaisesRegex(ProvenanceWriteError, "overwrite"):
                    capture(args(date=datetime.now(timezone.utc).date().isoformat(),
                                 window="daily", output=str(raw),
                                 manifest_output=str(manifest)))
                network.assert_not_called()
            self.assertEqual(raw.read_bytes(), b"PREVIOUS CAPTURE")
            self.assertFalse(manifest.exists())

    def test_capture_existing_manifest_rejected_before_network(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "new.html"
            manifest = Path(d) / "manifest.json"
            manifest.write_text("OLD MANIFEST")
            with patch("trending_study.__main__.urlopen") as network:
                with self.assertRaisesRegex(ProvenanceWriteError, "overwrite"):
                    capture(args(date=datetime.now(timezone.utc).date().isoformat(),
                                 window="daily", output=str(raw),
                                 manifest_output=str(manifest)))
                network.assert_not_called()
            self.assertFalse(raw.exists())
            self.assertEqual(manifest.read_text(), "OLD MANIFEST")

    def test_capture_raw_manifest_same_path_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            dest = str(Path(d) / "same-path")
            with patch("trending_study.__main__.urlopen") as network:
                with self.assertRaisesRegex(ProvenanceWriteError, "overlap"):
                    capture(args(date=datetime.now(timezone.utc).date().isoformat(),
                                 window="daily", output=dest,
                                 manifest_output=dest))
                network.assert_not_called()

    def test_capture_manifest_roundtrip_and_no_second_capture(self):
        class FakeResponse:
            status = 200
            headers = {"Content-Type": "text/html", "Date": "Mon, 12 Oct 2026 12:00:00 GMT"}
            def __enter__(self):
                return self
            def __exit__(self, *_):
                return False
            def read(self, maximum):
                return FIXTURE.read_bytes()

        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.html"
            manifest = Path(d) / "manifest.json"
            a = args(date=datetime.now(timezone.utc).date().isoformat(),
                     window="daily", output=str(raw), manifest_output=str(manifest))
            with patch("trending_study.__main__.urlopen", return_value=FakeResponse()) as network:
                with redirect_stdout(io.StringIO()):
                    capture(a)
                self.assertEqual(network.call_count, 1)
                self.assertEqual(raw.read_bytes(), FIXTURE.read_bytes())
                self.assertEqual(json.loads(manifest.read_text())["source_sha256"],
                                 hashlib.sha256(raw.read_bytes()).hexdigest())
                with self.assertRaises(ProvenanceWriteError):
                    capture(a)
                self.assertEqual(network.call_count, 1)

    def test_pilot_parse_derived_artifacts_never_replace_capture(self):
        with tempfile.TemporaryDirectory() as d:
            raw = Path(d) / "raw.html"
            manifest = Path(d) / "manifest.json"
            audit = Path(d) / "audit.json"
            rows = Path(d) / "rows.jsonl"
            raw.write_bytes(FIXTURE.read_bytes())
            manifest_data = build_capture_manifest(
                raw=raw.read_bytes(), output=str(raw), window="daily",
                captured_at_utc="2026-10-12T12:00:00+00:00",
                content_type="text/html", http_status=200,
            )
            manifest.write_text(json.dumps(manifest_data))
            original = raw.read_bytes()
            audit.write_bytes(b"EXISTING AUDIT")
            with self.assertRaisesRegex(ProvenanceWriteError, "overwrite"):
                pilot_parse(args(input=str(raw), manifest=str(manifest),
                                 output=str(rows), audit_output=str(audit)))
            self.assertFalse(rows.exists())
            self.assertEqual(raw.read_bytes(), original)
            self.assertEqual(audit.read_bytes(), b"EXISTING AUDIT")


if __name__ == "__main__":
    unittest.main()
