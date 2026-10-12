"""Offline tests: synthetic baselines, mock GitHub API, no live collection."""
from datetime import datetime, timedelta, timezone
import hashlib
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock

from urllib.error import HTTPError

from trending_study.longitudinal import (
    FollowupError, _event, _record, classification, collect, jsonl_data,
    load_events, load_plan, make_plan, summary, utc,
)
from trending_study.safe_io import ProvenanceWriteError, publish_jsonl


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0)


def baseline(rid, when, *, approved=True, name=None):
    return {
        "schema_version": "SYNTHETIC-baseline-v1",
        "study_id": "SYNTHETIC-no-real-enrollment",
        "repository_id": rid,
        "full_name_at_enrichment": name or f"fictional-owner/repo-{rid}",
        "metadata_status": "ok",
        "eligible_for_confirmatory_cohort": approved,
        "enriched_at_utc": when.isoformat(),
        "stars": 17,
        "source_sha256": "a" * 64,
        "protocol_commit": "b" * 40,
        "cohort_approval_ref": "SYNTHETIC-approval-not-verified",
    }


def as_jsonl(rows):
    return ("\n".join(json.dumps(x) for x in rows) + "\n").encode("utf-8")


def prepared(root, rows, grace=(3, 7, 14)):
    baseline_path = Path(root) / "baseline.jsonl"
    baseline_path.write_bytes(as_jsonl(rows))
    plan = make_plan(baseline_path.read_bytes(), grace)
    path = Path(root) / "plan.jsonl"
    publish_jsonl(path, plan)
    return path, plan


class Response:
    status = 200
    headers = {
        "Date": "Mon, 12 Oct 2026 12:00:00 GMT",
        "X-RateLimit-Remaining": "13",
        "X-RateLimit-Reset": "1791810000",
    }

    def __init__(self, rid, name, stars=22, private=False):
        self.data = json.dumps({
            "id": rid,
            "full_name": name,
            "private": private,
            "stargazers_count": stars,
            "forks_count": 4,
            "open_issues_count": 2,
        }).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self, maximum):
        return self.data[:maximum]


class PlanValidityTests(unittest.TestCase):
    def test_schedule_is_id_stable_deterministic_and_calendar_based(self):
        stamp = datetime(2026, 10, 12, 9, 10, tzinfo=timezone.utc)
        raw = as_jsonl([baseline(200, stamp), baseline(100, stamp)])
        first = make_plan(raw, (3, 7, 14))
        second = make_plan(raw, (3, 7, 14))
        self.assertEqual(first, second)
        self.assertEqual([(x["repository_id"], x["followup_days"]) for x in first],
                         [(100, 30), (100, 90), (100, 180),
                          (200, 30), (200, 90), (200, 180)])
        self.assertEqual(first[0]["scheduled_at_utc"],
                         (stamp + timedelta(days=30)).isoformat())
        self.assertEqual(first[0]["expires_at_utc"],
                         (stamp + timedelta(days=33)).isoformat())
        self.assertEqual(first[0]["cohort_input_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(first[0]["approval_verification"],
                         "self_reported_not_authenticated_by_software")

    def test_rejects_unapproved_pilot_and_unverified_metadata(self):
        stamp = utc_now() - timedelta(days=1)
        with self.assertRaisesRegex(FollowupError, "not declared cohort eligible"):
            make_plan(as_jsonl([baseline(1, stamp, approved=False)]), (3, 7, 14))
        row = baseline(1, stamp)
        row["metadata_status"] = "http_403"
        with self.assertRaisesRegex(FollowupError, "no successful"):
            make_plan(as_jsonl([row]), (3, 7, 14))

    def test_refuses_duplicates_invalid_ids_or_missing_provenance(self):
        stamp = utc_now() - timedelta(days=1)
        row = baseline(1, stamp)
        with self.assertRaisesRegex(FollowupError, "duplicate"):
            make_plan(as_jsonl([row, row]), (3, 7, 14))
        row["repository_id"] = True
        with self.assertRaisesRegex(FollowupError, "invalid stable"):
            make_plan(as_jsonl([row]), (3, 7, 14))
        row["repository_id"] = 3
        row["source_sha256"] = None
        with self.assertRaisesRegex(FollowupError, "source SHA-256"):
            make_plan(as_jsonl([row]), (3, 7, 14))

    def test_rejects_naive_dates_future_dates_and_bad_grace(self):
        stamp = utc_now()
        row = baseline(1, stamp)
        row["enriched_at_utc"] = stamp.replace(tzinfo=None).isoformat()
        with self.assertRaisesRegex(FollowupError, "UTC offset"):
            make_plan(as_jsonl([row]), (3, 7, 14))
        row = baseline(1, utc_now() + timedelta(days=7))
        with self.assertRaisesRegex(FollowupError, "future"):
            make_plan(as_jsonl([row]), (3, 7, 14))
        row = baseline(1, utc_now() - timedelta(days=1))
        for grace in [(3, 7), (3, 7, -1), (3, True, 14)]:
            with self.subTest(grace=grace):
                with self.assertRaises(FollowupError):
                    make_plan(as_jsonl([row]), grace)

    def test_plan_tampering_or_duplicate_task_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path, rows = prepared(d, [baseline(1, utc_now() - timedelta(days=30))])
            rows[0]["scheduled_at_utc"] = "2020-01-01T00:00:00+00:00"
            path.write_bytes(as_jsonl(rows))  # disposable synthetic fixture only
            with self.assertRaisesRegex(FollowupError, "inconsistent dates"):
                load_plan(path)
            rows = make_plan(as_jsonl([baseline(1, utc_now() - timedelta(days=30))]), (3, 7, 14))
            path.write_bytes(as_jsonl([rows[0], rows[0]]))
            with self.assertRaisesRegex(FollowupError, "repeats a repository/horizon"):
                load_plan(path)

    def test_plan_command_never_overwrites_existing_output(self):
        with tempfile.TemporaryDirectory() as d:
            source = Path(d) / "baseline.jsonl"
            source.write_bytes(as_jsonl([baseline(1, utc_now() - timedelta(days=1))]))
            target = Path(d) / "plan.jsonl"
            cmd = [
                sys.executable, "-m", "trending_study.longitudinal", "plan",
                "--input", str(source), "--output", str(target),
                "--grace-days", "3", "7", "14",
            ]
            first = subprocess.run(cmd, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(json.loads(first.stdout)["planned_followups"], 3)
            original = target.read_bytes()
            second = subprocess.run(cmd, text=True, capture_output=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(target.read_bytes(), original)

    def test_blank_event_ledger_does_not_claim_completed_work(self):
        with tempfile.TemporaryDirectory() as d:
            file, plan = prepared(d, [baseline(1, utc_now() - timedelta(days=1))])
            _, by_id, hashval = load_plan(file)
            s = summary(plan, load_events(Path(d) / "no-events", by_id, hashval), utc_now())
            self.assertEqual(s["counts"]["upcoming"], 3)
            self.assertEqual(s["counts"]["completed"], 0)


class FollowupCollectionTests(unittest.TestCase):
    def test_explicit_opt_in_required_and_future_tasks_do_not_fetch(self):
        with tempfile.TemporaryDirectory() as d:
            file, _ = prepared(d, [baseline(1, utc_now() - timedelta(days=1))])
            opener = Mock(side_effect=AssertionError("no network permitted"))
            with self.assertRaisesRegex(FollowupError, "confirm-network"):
                collect(file, Path(d) / "events", opener=opener)
            result = collect(file, Path(d) / "events", allow_network=True,
                             opener=opener, clock=utc_now)
            self.assertEqual(result["requests"], 0)
            self.assertEqual(result["new_events"], 0)
            opener.assert_not_called()

    def test_successful_snapshot_records_provenance_then_idempotently_resumes(self):
        when = utc_now() - timedelta(days=30, hours=1)
        now = utc_now()
        with tempfile.TemporaryDirectory() as d:
            file, _ = prepared(d, [baseline(11, when)])
            events = Path(d) / "events"
            seen = []

            def fake(request, timeout):
                seen.append((request.full_url, timeout))
                return Response(11, "new-owner/renamed-repo")
            first = collect(file, events, allow_network=True, opener=fake,
                            clock=lambda: now)
            self.assertEqual(first["requests"], 1)
            self.assertEqual(first["summary"]["counts"]["completed"], 1)
            self.assertEqual(seen[0][0], "https://api.github.com/repos/fictional-owner/repo-11")
            record = json.loads(next(events.glob("*.json")).read_text())
            self.assertEqual(record["status"], "ok")
            self.assertEqual(record["repository_id"], 11)
            self.assertEqual(record["full_name_at_followup"], "new-owner/renamed-repo")
            self.assertEqual(record["rate_limit_remaining"], 13)
            self.assertEqual(record["stars"], 22)
            self.assertGreater(record["lag_seconds"], 0)
            second = collect(file, events, allow_network=True,
                             opener=Mock(side_effect=AssertionError("would refetch")),
                             clock=lambda: now)
            self.assertEqual(second["requests"], 0)
            self.assertEqual(len(list(events.glob("*.json"))), 1)

    def test_missed_window_cannot_be_backfilled_by_late_api_count(self):
        with tempfile.TemporaryDirectory() as d:
            file, _ = prepared(d, [baseline(10, utc_now() - timedelta(days=210))])
            events = Path(d) / "events"
            opener = Mock(side_effect=AssertionError("expired tasks cannot fetch"))
            result = collect(file, events, allow_network=True,
                             opener=opener, clock=utc_now)
            opener.assert_not_called()
            self.assertEqual(result["summary"]["counts"]["missed"], 3)
            self.assertEqual(len(list(events.glob("*.json"))), 3)
            for event_path in events.glob("*.json"):
                event = json.loads(event_path.read_text())
                self.assertEqual(event["status"], "missed_window")
                self.assertIsNone(event["stars"])

    def test_rate_limit_halts_without_silent_retry(self):
        now = utc_now()
        data = [baseline(10, now - timedelta(days=30)),
                baseline(20, now - timedelta(days=30))]
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, data)

            def exhausted(_request, timeout):
                raise HTTPError("https://api.github.com/", 403, "limited",
                                {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1791810000"},
                                None)
            opener = Mock(side_effect=exhausted)
            result = collect(path, Path(d) / "events", allow_network=True,
                             opener=opener, clock=lambda: now)
            self.assertEqual(result["requests"], 1)
            self.assertTrue(result["stopped_early"])
            event = json.loads(next((Path(d) / "events").glob("*.json")).read_text())
            self.assertEqual(event["status"], "rate_limited")
            self.assertEqual(event["rate_limit_remaining"], 0)
            self.assertIsNone(event["stars"])
            self.assertEqual(result["summary"]["counts"]["attempted_today"], 1)
            self.assertEqual(result["summary"]["counts"]["due"], 1)

    def test_not_found_may_mean_private_or_renamed_and_no_same_day_retry(self):
        now = utc_now()
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, [baseline(10, now - timedelta(days=30))])
            opener = Mock(side_effect=HTTPError(
                "https://api.github.com/", 404, "not found", {}, None))
            first = collect(path, Path(d) / "events", allow_network=True,
                            opener=opener, clock=lambda: now)
            self.assertEqual(first["requests"], 1)
            self.assertEqual(first["summary"]["counts"]["attempted_today"], 1)
            record = json.loads(next((Path(d) / "events").glob("*.json")).read_text())
            self.assertEqual(record["status"], "not_found_or_private_or_renamed")
            self.assertIsNone(record["stars"])
            second = collect(path, Path(d) / "events", allow_network=True,
                             opener=opener, clock=lambda: now)
            self.assertEqual(second["requests"], 0)
            self.assertEqual(opener.call_count, 1)

    def test_identity_mismatch_never_becomes_star_measurement(self):
        now = utc_now()
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, [baseline(10, now - timedelta(days=30))])
            result = collect(path, Path(d) / "events", allow_network=True,
                             opener=lambda request, timeout: Response(999, "other/repo", 99),
                             clock=lambda: now)
            self.assertTrue(result["stopped_early"])
            record = json.loads(next((Path(d) / "events").glob("*.json")).read_text())
            self.assertEqual(record["status"], "identity_mismatch")
            self.assertEqual(record["observed_repository_id"], 999)
            self.assertIsNone(record["stars"])

    def test_observed_response_just_after_expiry_is_not_success(self):
        base = utc_now() - timedelta(days=30)
        due = base + timedelta(days=30)
        # First check says due; response finished after an allowed zero-day window.
        ticks = [due] + [due + timedelta(minutes=1)] * 4  # three tasks, one response, final summary
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, [baseline(10, base)], grace=(0, 0, 0))
            result = collect(path, Path(d) / "events", allow_network=True,
                             opener=lambda request, timeout: Response(10, "owner/repo"),
                             clock=lambda: ticks.pop(0))
            self.assertEqual(result["summary"]["counts"]["missed"], 1)
            record = json.loads(next((Path(d) / "events").glob("*.json")).read_text())
            self.assertEqual(record["status"], "late_observation")
            self.assertEqual(record["stars"], 22)

    def test_corrupt_or_unlinked_event_blocks_resume(self):
        now = utc_now()
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, [baseline(10, now - timedelta(days=30))])
            events = Path(d) / "events"
            events.mkdir()
            (events / "corrupt.json").write_text("{")
            opener = Mock(side_effect=AssertionError("no calls on corrupt ledger"))
            with self.assertRaisesRegex(FollowupError, "invalid event file"):
                collect(path, events, allow_network=True,
                        opener=opener, clock=lambda: now)
            opener.assert_not_called()

    def test_existing_concurrent_lock_blocks_network(self):
        now = utc_now()
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, [baseline(10, now - timedelta(days=30))])
            events = Path(d) / "events"
            events.mkdir()
            (events / ".followup.lock").write_text("stale or active")
            opener = Mock(side_effect=AssertionError("no calls under lock"))
            with self.assertRaisesRegex(FollowupError, "collector lock"):
                collect(path, events, allow_network=True,
                        opener=opener, clock=lambda: now)
            opener.assert_not_called()

    def test_cli_status_is_offline_and_counts_unknown(self):
        with tempfile.TemporaryDirectory() as d:
            path, _ = prepared(d, [baseline(1, utc_now() - timedelta(days=1))])
            cp = subprocess.run([
                sys.executable, "-m", "trending_study.longitudinal", "status",
                "--plan", str(path), "--events-dir", str(Path(d) / "events"),
            ], text=True, capture_output=True)
            self.assertEqual(cp.returncode, 0, cp.stderr)
            self.assertEqual(json.loads(cp.stdout)["counts"]["completed"], 0)


class EventLedgerIntegrityTests(unittest.TestCase):
    """Synthetic incident cases; never manipulate or delete a real event."""

    def setup_record(self, directory):
        now = utc_now()
        plan_path, records = prepared(directory, [baseline(410, now - timedelta(days=30))])
        plan, by_id, digest = load_plan(plan_path)
        task = next(r for r in plan if r["followup_days"] == 30)
        event = _event(
            task, digest, now, status="ok",
            api_url="https://api.github.com/repos/fictional-owner/repo-410",
            http_status=200, full_name_at_followup="fictional-owner/repo-410",
            stars=29, forks=3, open_issues_including_prs=1,
            observed_repository_id=410, response_date_header=None,
            rate_limit_remaining=20, rate_limit_reset_epoch=None,
            lag_seconds=round((now - utc(task["scheduled_at_utc"], "due")).total_seconds(), 3),
        )
        events_dir = Path(directory) / "events"
        events_dir.mkdir()
        return plan_path, task, by_id, digest, event, events_dir, now

    def assert_bad_event(self, modify, message):
        with tempfile.TemporaryDirectory() as directory:
            plan_path, task, lookup, digest, event, events_dir, now = self.setup_record(directory)
            modify(event, task)
            (events_dir / "synthetic-event.json").write_text(json.dumps(event), encoding="utf-8")
            opener = Mock(side_effect=AssertionError("network must not run on invalid ledger"))
            with self.assertRaisesRegex(FollowupError, message):
                collect(plan_path, events_dir, allow_network=True,
                        opener=opener, clock=lambda: now)
            opener.assert_not_called()

    def test_well_formed_success_is_still_completed(self):
        with tempfile.TemporaryDirectory() as directory:
            _, task, lookup, digest, event, events_dir, now = self.setup_record(directory)
            _record(events_dir, event)
            loaded = load_events(events_dir, lookup, digest)
            self.assertEqual(classification(task, loaded[task["task_id"]], now), "completed")
            self.assertEqual(loaded[task["task_id"]][0]["stars"], 29)

    def test_never_accept_fictitious_success_counters(self):
        for key, value in (("stars", None), ("stars", -7), ("forks", True),
                           ("open_issues_including_prs", "2")):
            with self.subTest(key=key, value=value):
                self.assert_bad_event(
                    lambda event, task: event.__setitem__(key, value),
                    "success has missing/invalid",
                )

    def test_success_requires_real_response_fields(self):
        self.assert_bad_event(lambda event, task: event.update(http_status=None),
                              "HTTP 200")
        self.assert_bad_event(lambda event, task: event.update(observed_repository_id=999),
                              "stable repository ID")
        self.assert_bad_event(lambda event, task: event.update(api_url="https://evil.invalid/repos/x/y"),
                              "official repository path")

    def test_success_timestamp_cannot_precede_due_or_exceed_expiry(self):
        self.assert_bad_event(
            lambda event, task: event.update(observed_at_utc=(
                utc(task["scheduled_at_utc"], "due") - timedelta(seconds=1)).isoformat()),
            "observation precedes",
        )
        self.assert_bad_event(
            lambda event, task: event.update(observed_at_utc=(
                utc(task["expires_at_utc"], "end") + timedelta(seconds=1)).isoformat()),
            "outside its prespecified observation window",
        )

    def test_missed_and_late_statuses_require_correct_window(self):
        self.assert_bad_event(
            lambda event, task: event.update(status="late_observation"),
            "missed/late status contradicts",
        )
        self.assert_bad_event(
            lambda event, task: event.update(
                status="missed_window", http_status=None, stars=None,
                reason="synthetic no observation"),
            "event fields mismatch",
        )
        # Use a genuine missed-event schema but put it *before* expiration.
        def early_missed(event, task):
            event.clear()
            event.update(_event(
                task, "a" * 64, utc(task["scheduled_at_utc"], "due"),
                status="missed_window", http_status=None, stars=None,
                reason="synthetic premature missingness"))
        self.assert_bad_event(early_missed, "event does not belong")

    def test_failing_fetch_cannot_report_success_counters(self):
        def forged(event, task):
            event.update(status="network_error", http_status=None,
                         observed_repository_id=None)
        self.assert_bad_event(forged, "failed or uncertain event")

    def test_frozen_plan_fields_cannot_be_changed_in_event(self):
        self.assert_bad_event(
            lambda event, task: event.update(study_id="another-study"),
            "study ID conflicts",
        )
        self.assert_bad_event(
            lambda event, task: event.update(
                scheduled_at_utc=(utc(task["scheduled_at_utc"], "due")
                                  + timedelta(hours=1)).isoformat()),
            "scheduled_at_utc conflicts",
        )
        self.assert_bad_event(
            lambda event, task: event.update(
                expires_at_utc=(utc(task["expires_at_utc"], "end")
                                + timedelta(days=1)).isoformat()),
            "expires_at_utc conflicts",
        )

    def test_reject_unexpected_fields_lag_or_invalid_header(self):
        self.assert_bad_event(lambda event, task: event.update(access_token="SECRET"),
                              "event fields mismatch")
        self.assert_bad_event(lambda event, task: event.update(lag_seconds=999),
                              "lag does not match")
        self.assert_bad_event(lambda event, task: event.update(rate_limit_remaining=-1),
                              "rate_limit_remaining")

    def test_symlink_event_cannot_count_as_immutable(self):
        with tempfile.TemporaryDirectory() as directory:
            _, task, lookup, digest, event, events_dir, _ = self.setup_record(directory)
            target = Path(directory) / "external-event.json"
            target.write_text(json.dumps(event), encoding="utf-8")
            (events_dir / "linked.json").symlink_to(target)
            with self.assertRaisesRegex(FollowupError, "symlinked event"):
                load_events(events_dir, lookup, digest)

    def test_noncanonical_repo_segments_are_rejected(self):
        raw = as_jsonl([baseline(11, utc_now() - timedelta(days=1), name="../repo")])
        with self.assertRaisesRegex(FollowupError, "invalid repository full name"):
            make_plan(raw, (3, 7, 14))
        with tempfile.TemporaryDirectory() as directory:
            plan_path, rows = prepared(directory, [baseline(11, utc_now() - timedelta(days=1))])
            rows[0]["full_name_at_baseline"] = "../repo"
            Path(plan_path).write_bytes(as_jsonl(rows))  # temporary synthetic file
            with self.assertRaisesRegex(FollowupError, "plan repository name"):
                load_plan(plan_path)


if __name__ == "__main__":
    unittest.main()
