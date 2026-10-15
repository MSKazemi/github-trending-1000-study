"""Adversarial synthetic input tests for issue #4; never fetch real GitHub."""
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

from trending_study.longitudinal import (
    FollowupError, _event, _record, collect, jsonl_data, load_events,
    load_plan, make_plan,
)


def baseline():
    return {
        "schema_version": "SYNTHETIC-baseline-v1",
        "study_id": "SYNTHETIC-no-enrollment",
        "repository_id": 817,
        "full_name_at_enrichment": "fictional/example",
        "metadata_status": "ok",
        "eligible_for_confirmatory_cohort": True,
        "enriched_at_utc": (
            datetime.now(timezone.utc).replace(microsecond=0)
            - timedelta(days=30, hours=1)
        ).isoformat(),
        "stars": 10,
        "source_sha256": "a" * 64,
        "protocol_commit": "b" * 40,
        "cohort_approval_ref": "SYNTHETIC-not-an-approval",
    }


def jsonl(rows):
    return ("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)).encode()


def plan_file(root):
    path = Path(root) / "plan.jsonl"
    path.write_bytes(jsonl(make_plan(jsonl([baseline()]), (3, 7, 14))))
    return path


class MockResponse:
    status = 200
    headers = {
        "Date": "Thu, 15 Oct 2026 14:00:00 GMT",
        "X-RateLimit-Remaining": "15",
        "X-RateLimit-Reset": "1792072800",
    }

    def __init__(self, raw):
        self.raw = raw

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, limit):
        return self.raw[:limit]


class LongitudinalInputIntegrityTests(unittest.TestCase):
    def test_duplicate_json_keys_and_nonfinite_literals_fail_closed(self):
        raw = jsonl([baseline()]).decode()
        duplicate = raw.replace('"stars": 10', '"stars": 0, "stars": 10')
        self.assertNotEqual(raw, duplicate)
        for candidate in (
            duplicate,
            raw.replace('"stars": 10', '"stars": NaN'),
            raw.replace('"stars": 10', '"stars": Infinity'),
            raw.replace('"stars": 10', '"stars": 1e999'),
            raw.replace('"stars": 10', '"stars": 1e-999'),
            raw + "\n",  # blank record
        ):
            with self.subTest(candidate=candidate[-30:]):
                with self.assertRaises(FollowupError):
                    make_plan(candidate.encode(), (3, 7, 14))

    def test_decoder_does_not_echo_private_duplicate_key(self):
        private = "PRIVATE-synthetic-password-label"
        payload = ('{"' + private + '":1,"' + private + '":2}\n').encode()
        with self.assertRaises(FollowupError) as exc:
            jsonl_data(payload, "baseline")
        self.assertNotIn(private, str(exc.exception))

    def test_plan_must_preserve_all_horizons(self):
        with tempfile.TemporaryDirectory() as directory:
            path = plan_file(directory)
            rows = [json.loads(line) for line in path.read_text().splitlines()]
            path.write_bytes(jsonl(rows[:2]))
            with self.assertRaisesRegex(FollowupError, "all 30/90/180"):
                load_plan(path)

    def test_plan_baseline_fields_cannot_change_across_horizons(self):
        with tempfile.TemporaryDirectory() as directory:
            path = plan_file(directory)
            rows = [json.loads(line) for line in path.read_text().splitlines()]
            rows[1]["baseline_stars"] = 999
            path.write_bytes(jsonl(rows))
            with self.assertRaisesRegex(FollowupError, "inconsistent per-repository"):
                load_plan(path)

    def test_plan_schema_rejects_secret_fields_and_fake_review_flags(self):
        with tempfile.TemporaryDirectory() as directory:
            path = plan_file(directory)
            original = [json.loads(line) for line in path.read_text().splitlines()]
            injected = [dict(row) for row in original]
            for row in injected:
                row["PRIVATE-synthetic-access-token"] = "not-a-real-token"
            path.write_bytes(jsonl(injected))
            with self.assertRaisesRegex(FollowupError, "missing or unexpected"):
                load_plan(path)
            path.write_bytes(jsonl(original))
            original[0]["approval_verification"] = "verified_human"
            path.write_bytes(jsonl(original))
            with self.assertRaisesRegex(FollowupError, "approval cannot be certified"):
                load_plan(path)

    def test_plan_source_digest_is_not_optional(self):
        with tempfile.TemporaryDirectory() as directory:
            path = plan_file(directory)
            rows = [json.loads(line) for line in path.read_text().splitlines()]
            rows[1]["baseline_capture_sha256"] = "not-a-digest"
            path.write_bytes(jsonl(rows))
            with self.assertRaisesRegex(FollowupError, "valid baseline_capture_sha256"):
                load_plan(path)

    def test_plan_duplicate_key_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = plan_file(directory)
            original = path.read_text()
            changed = original.replace('"baseline_stars": 10',
                                       '"baseline_stars": 0, "baseline_stars": 10', 1)
            self.assertNotEqual(original, changed)
            path.write_text(changed)
            with self.assertRaisesRegex(FollowupError, "ambiguous"):
                load_plan(path)

    def test_plan_leaf_symlink_and_directory_are_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            real = plan_file(directory)
            link = Path(directory) / "plan-link.jsonl"
            link.symlink_to(real)
            with self.assertRaisesRegex(FollowupError, "non-symlink"):
                load_plan(link)
            with self.assertRaisesRegex(FollowupError, "regular non-symlink"):
                load_plan(Path(directory))

    @unittest.skipUnless(hasattr(os, "mkfifo"), "POSIX FIFO fixture")
    def test_fifo_plan_is_rejected_without_waiting_for_writer(self):
        with tempfile.TemporaryDirectory() as directory:
            fifo = Path(directory) / "frozen.jsonl"
            os.mkfifo(fifo)
            with self.assertRaisesRegex(FollowupError, "regular non-symlink"):
                load_plan(fifo)

    def test_plan_byte_cap_applies_to_actual_reads(self):
        from unittest.mock import patch
        import trending_study.longitudinal as instrument
        with tempfile.TemporaryDirectory() as directory:
            path = plan_file(directory)
            with patch.object(instrument, "MAX_PLAN_BYTES", 60):
                with self.assertRaisesRegex(FollowupError, "byte limit"):
                    load_plan(path)

    def test_event_duplicate_key_is_rejected_before_resumption(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = plan_file(directory)
            tasks, by_id, digest = load_plan(plan)
            task = tasks[0]
            due = datetime.fromisoformat(task["scheduled_at_utc"])
            raw = _event(
                task, digest, due + timedelta(minutes=10), status="ok",
                api_url="https://api.github.com/repos/fictional/example",
                http_status=200, full_name_at_followup="fictional/example",
                stars=12, forks=3, open_issues_including_prs=2,
                observed_repository_id=817, response_date_header=None,
                rate_limit_remaining=11, rate_limit_reset_epoch=None,
                lag_seconds=600.0,
            )
            folder = Path(directory) / "events"
            folder.mkdir()
            payload = json.dumps(raw).replace(
                '"status": "ok"', '"status": "network_error", "status": "ok"'
            )
            (folder / "event.json").write_text(payload)
            opener = Mock(side_effect=AssertionError("no API on ambiguous replay"))
            with self.assertRaisesRegex(FollowupError, "invalid event file"):
                collect(plan, folder, allow_network=True, opener=opener)
            opener.assert_not_called()

    def test_event_ledger_does_not_ignore_stray_or_partial_files(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = plan_file(directory)
            _, by_id, digest = load_plan(plan)
            events = Path(directory) / "events"
            events.mkdir()
            for name in ("unexpected.jsonl", ".capture-pending-crash"):
                path = events / name
                path.write_text("incomplete synthetic observation")
                with self.subTest(name=name):
                    with self.assertRaisesRegex(FollowupError, "unexpected file"):
                        load_events(events, by_id, digest)
                path.unlink()

    def test_event_directory_symlink_is_not_an_empty_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = plan_file(directory)
            _, by_id, digest = load_plan(plan)
            real = Path(directory) / "real"
            real.mkdir()
            (Path(directory) / "events").symlink_to(real, target_is_directory=True)
            with self.assertRaisesRegex(FollowupError, "events-dir must not be a symlink"):
                load_events(Path(directory) / "events", by_id, digest)

    def test_missing_task_id_type_is_controlled_error(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = plan_file(directory)
            rows, by_id, digest = load_plan(plan)
            task = rows[0]
            now = datetime.fromisoformat(task["scheduled_at_utc"]) + timedelta(minutes=1)
            record = _event(task, digest, now, status="network_error",
                            api_url="https://api.github.com/repos/fictional/example",
                            http_status=None, full_name_at_followup=None,
                            stars=None, forks=None, open_issues_including_prs=None,
                            observed_repository_id=None, response_date_header=None,
                            rate_limit_remaining=None, rate_limit_reset_epoch=None,
                            lag_seconds=60.0)
            record["task_id"] = ["unhashable", "not-an-id"]
            events = Path(directory) / "events"
            events.mkdir()
            (events / "bad.json").write_text(json.dumps(record))
            with self.assertRaisesRegex(FollowupError, "immutable plan"):
                load_events(events, by_id, digest)

    def test_api_duplicate_identity_or_nan_never_counts_as_observed(self):
        now = datetime.now(timezone.utc).replace(microsecond=0)
        with tempfile.TemporaryDirectory() as directory:
            plan = plan_file(directory)
            valid = json.dumps({
                "id": 817, "full_name": "fictional/example", "private": False,
                "stargazers_count": 22, "forks_count": 4,
                "open_issues_count": 2,
            })
            for body in (
                valid.replace('"id": 817', '"id": 999, "id": 817'),
                valid.replace('"stargazers_count": 22', '"stargazers_count": NaN'),
            ):
                # Fresh ledger per request avoids the same-day-attempt gate.
                folder = Path(directory) / ("events-" + str(len(list(Path(directory).glob("events-*")))))
                opener = Mock(return_value=MockResponse(body.encode()))
                result = collect(plan, folder, allow_network=True, opener=opener,
                                 clock=lambda: now)
                self.assertEqual(result["requests"], 1)
                self.assertEqual(result["summary"]["counts"]["completed"], 0)
                events = list(folder.glob("*.json"))
                self.assertEqual(len(events), 1)
                observed = json.loads(events[0].read_text())
                self.assertEqual(observed["status"], "invalid_response")
                self.assertIsNone(observed["stars"])

    def test_clean_plan_and_locked_event_ledger_remain_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            plan = plan_file(directory)
            _, by_id, digest = load_plan(plan)
            events = Path(directory) / "events"
            events.mkdir()
            (events / ".followup.lock").write_text("pid=0 (synthetic)")
            self.assertEqual(
                sum(len(v) for v in load_events(events, by_id, digest).values()), 0
            )


if __name__ == "__main__":
    unittest.main()
