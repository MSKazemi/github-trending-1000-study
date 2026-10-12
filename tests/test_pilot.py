"""No live GitHub calls. Pilot checks use synthetic/local HTML only."""
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from trending_study.__main__ import capture, extract_repos
from trending_study.pilot import (
    PilotValidationError, PILOT_GATES, CONFIRMATORY_EXTRA_GATES,
    build_capture_manifest, evaluate_preflight, validate_capture, write_json,
)

FIXTURE = Path(__file__).parent / "fixtures" / "trending.html"
CAPTURE_TIME = "2026-10-12T08:00:00+00:00"


def make_manifest(raw=None):
    raw = FIXTURE.read_bytes() if raw is None else raw
    return build_capture_manifest(
        raw=raw, output="data/raw/example.html", window="daily",
        captured_at_utc=CAPTURE_TIME, content_type="text/html; charset=UTF-8",
        http_status=200, response_date_header="Mon, 12 Oct 2026 08:00:00 GMT",
    )


def make_preflight(status="pending"):
    names = PILOT_GATES + CONFIRMATORY_EXTRA_GATES
    if status == "verified":
        gates = {
            key: {
                "status": "verified",
                "evidence_ref": "https://example.invalid/synthetic-review",
                "reviewer": "SYNTHETIC reviewer; not real approval",
                "reviewed_at_utc": CAPTURE_TIME,
            }
            for key in names
        }
    else:
        gates = {
            key: {
                "status": status,
                "evidence_ref": None,
                "reviewer": None,
                "reviewed_at_utc": None,
            }
            for key in names
        }
    return {"schema_version": "1.0", "study_id": "SYNTHETIC-2027-REUSE", "gates": gates}


class CaptureProvenanceTests(unittest.TestCase):
    def test_round_trip_preserves_original_capture_time(self):
        raw = FIXTURE.read_bytes()
        manifest = make_manifest(raw)
        rows, audit = validate_capture(raw, manifest, extract_repos=extract_repos)
        self.assertEqual(len(rows), 2)
        self.assertEqual([x["rank"] for x in rows], [1, 2])
        self.assertEqual(rows[0]["captured_at_utc"], CAPTURE_TIME)
        self.assertEqual(rows[0]["collected_at_utc"], CAPTURE_TIME)
        self.assertNotEqual(rows[0]["parsed_at_utc"], CAPTURE_TIME)
        self.assertFalse(rows[0]["eligible_for_confirmatory_cohort"])
        self.assertEqual(audit["page_rows"], 2)
        self.assertEqual(audit["cohort_enrollment_status"], "not_enrolled")

    def test_changed_capture_detected(self):
        manifest = make_manifest()
        with self.assertRaisesRegex(PilotValidationError, "SHA-256"):
            validate_capture(FIXTURE.read_bytes() + b"!", manifest, extract_repos=extract_repos)

    def test_wrong_date_detected(self):
        manifest = make_manifest()
        manifest["capture_date_utc"] = "2026-10-11"
        with self.assertRaisesRegex(PilotValidationError, "capture date"):
            validate_capture(FIXTURE.read_bytes(), manifest, extract_repos=extract_repos)

    def test_unverifiable_language_filter_rejected(self):
        manifest = make_manifest()
        manifest["language_filter"] = "Python"
        with self.assertRaisesRegex(PilotValidationError, "language"):
            validate_capture(FIXTURE.read_bytes(), manifest, extract_repos=extract_repos)

    def test_source_url_spoofing_rejected(self):
        manifest = make_manifest()
        manifest["source_url"] = "https://github.com.evil.test/trending?since=daily"
        with self.assertRaisesRegex(PilotValidationError, "exact GitHub"):
            validate_capture(FIXTURE.read_bytes(), manifest, extract_repos=extract_repos)
        manifest = make_manifest()
        manifest["source_url"] = "https://github.com/trending?since=daily&lang=python"
        with self.assertRaisesRegex(PilotValidationError, "unsupported source URL"):
            validate_capture(FIXTURE.read_bytes(), manifest, extract_repos=extract_repos)

    def test_forged_manifest_method_rejected(self):
        manifest = make_manifest()
        manifest["capture_method"] = "unverified_manual"
        with self.assertRaisesRegex(PilotValidationError, "capture_method"):
            validate_capture(FIXTURE.read_bytes(), manifest, extract_repos=extract_repos)

    def test_empty_or_nonhtml_cannot_be_a_valid_capture(self):
        with self.assertRaises(PilotValidationError):
            make_manifest(b"")
        with self.assertRaises(PilotValidationError):
            build_capture_manifest(
                raw=FIXTURE.read_bytes(), output="fixture",
                window="daily", captured_at_utc=CAPTURE_TIME,
                content_type="application/json",
            )

    def test_fake_page_cannot_produce_trending_rows(self):
        raw = b"<html><body><p>bot challenge</p></body></html>"
        manifest = make_manifest(raw)
        with self.assertRaises(ValueError):
            validate_capture(raw, manifest, extract_repos=extract_repos)

    def test_cli_pilot_parse_audits_manifest_without_network(self):
        with tempfile.TemporaryDirectory() as d:
            raw = FIXTURE.read_bytes()
            html = Path(d) / "raw.html"
            manifest = Path(d) / "capture.json"
            out = Path(d) / "observations.jsonl"
            audit = Path(d) / "audit.json"
            html.write_bytes(raw)
            write_json(manifest, make_manifest(raw))
            command = [
                sys.executable, "-m", "trending_study", "pilot-parse",
                "--input", str(html), "--manifest", str(manifest),
                "--output", str(out), "--audit-output", str(audit),
            ]
            p = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            rows = [json.loads(x) for x in out.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["source_manifest_sha256"],
                             hashlib.sha256(manifest.read_bytes()).hexdigest())
            self.assertEqual(json.loads(audit.read_text())["page_rows"], 2)

    def test_legacy_parser_is_explicitly_unverified(self):
        with tempfile.TemporaryDirectory() as d:
            output = Path(d) / "legacy.jsonl"
            p = subprocess.run([
                sys.executable, "-m", "trending_study", "parse-trending",
                "--input", str(FIXTURE), "--date", "2026-10-11",
                "--window", "daily", "--output", str(output),
            ], capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            row = json.loads(output.read_text().splitlines()[0])
            self.assertEqual(row["capture_time_status"], "unverified_parse_only")
            self.assertFalse(row["eligible_for_confirmatory_cohort"])

    def test_capture_cli_writes_real_time_manifest_with_mocked_http(self):
        class FakeResponse:
            status = 200
            headers = {
                "Content-Type": "text/html; charset=UTF-8",
                "Date": "Mon, 12 Oct 2026 10:00:00 GMT",
            }

            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self, limit):
                return FIXTURE.read_bytes()

        with tempfile.TemporaryDirectory() as d:
            html = Path(d) / "raw.html"
            mf = Path(d) / "manifest.json"
            args = type("A", (), {
                "date": datetime.now(timezone.utc).date().isoformat(),
                "window": "daily", "output": str(html), "manifest_output": str(mf),
            })()
            with patch("trending_study.__main__.urlopen", return_value=FakeResponse()) as url_mock:
                with redirect_stdout(io.StringIO()):
                    capture(args)
            self.assertEqual(url_mock.call_count, 1)
            self.assertEqual(html.read_bytes(), FIXTURE.read_bytes())
            manifest = json.loads(mf.read_text(encoding="utf-8"))
            self.assertEqual(manifest["source_sha256"], hashlib.sha256(FIXTURE.read_bytes()).hexdigest())
            self.assertEqual(manifest["capture_method"], "explicit_cli")
            self.assertEqual(manifest["capture_date_utc"], args.date)


class PreflightTests(unittest.TestCase):
    def test_default_configuration_blocks_pilot_and_confirmatory(self):
        p = make_preflight()
        a = evaluate_preflight(p, stage="pilot")
        b = evaluate_preflight(p, stage="confirmatory")
        self.assertEqual(a["decision"], "not_ready")
        self.assertEqual(len(a["pending"]), len(PILOT_GATES))
        self.assertEqual(len(b["pending"]), len(PILOT_GATES) + len(CONFIRMATORY_EXTRA_GATES))

    def test_verified_documentary_gates_need_independent_human_approval(self):
        p = make_preflight("verified")
        a = evaluate_preflight(p)
        self.assertEqual(a["decision"], "ready_for_human_review")
        self.assertIn("NOT formal ethics approval", a["disclaimer"])

    def test_fake_verified_gate_without_source_ref_rejected(self):
        p = make_preflight("verified")
        p["gates"]["source_access_review"]["evidence_ref"] = None
        with self.assertRaisesRegex(PilotValidationError, "evidence_ref"):
            evaluate_preflight(p, stage="pilot")

    def test_incomplete_preflight_never_treated_as_verified(self):
        p = make_preflight("verified")
        del p["gates"]["preregistration"]
        summary = evaluate_preflight(p)
        self.assertEqual(summary["decision"], "not_ready")
        self.assertIn("preregistration", summary["pending"])

    def test_cli_refuses_premature_confirmatory_enrollment(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "preflight.json"
            write_json(path, make_preflight("pending"))
            cmd = [
                sys.executable, "-m", "trending_study", "pilot-preflight",
                "--input", str(path), "--stage", "confirmatory",
            ]
            p = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(json.loads(p.stdout)["decision"], "not_ready")
            blocked = subprocess.run(cmd + ["--require-ready"], capture_output=True, text=True)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("not complete", blocked.stderr)


if __name__ == "__main__":
    unittest.main()
