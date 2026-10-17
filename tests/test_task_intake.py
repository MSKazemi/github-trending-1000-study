import copy
from contextlib import redirect_stderr
import io
import traceback
import json
from pathlib import Path
import subprocess
import sys
import re
import tempfile
import unittest
from trending_study.task_intake import sample, IntakeError, main

FRAME = Path(__file__).resolve().parents[1] / "examples" / "task_intake.public_2026-10-12.json"
CROSS_ECOSYSTEM_FRAME = Path(__file__).resolve().parents[1] / "examples" / "task_intake.cross_ecosystem_2026-10-12.json"

class IntakeTests(unittest.TestCase):
    def frame(self):
        return json.loads(FRAME.read_text(encoding="utf-8"))

    def test_ledger_keeps_all_rows_and_pull_requests(self):
        r = sample(self.frame())
        self.assertEqual(r["total_rows"], 15)
        self.assertEqual(r["selected_issue_candidates"], 6)
        self.assertEqual(len(r["per_repo"]), 3)
        self.assertEqual(sum(x["selection_status"]=="excluded_pr_not_issue" for x in r["ledger"]), 3)
        self.assertTrue(all(x["reuse_opportunity"]=="unknown" for x in r["ledger"]))
        self.assertTrue(all(x["experiment_enrollment_status"]=="not_eligible_unreviewed" for x in r["ledger"]))

    def test_determinism(self):
        self.assertEqual(sample(self.frame()), sample(self.frame()))

    def test_reject_personal_data(self):
        x=self.frame()
        x["sources"][0]["issues"][0]["user"]={"login":"name"}
        with self.assertRaises(IntakeError): sample(x)

    def test_reject_future_update(self):
        x=self.frame()
        x["sources"][0]["issues"][0]["updated_at_utc"]="2027-01-01T00:00:00Z"
        with self.assertRaises(IntakeError): sample(x)

    def test_reject_wrong_url(self):
        x=self.frame()
        x["sources"][1]["issues"][0]["html_url"]="https://github.com/not/the-repo/issues/2"
        with self.assertRaises(IntakeError): sample(x)

    def test_reject_duplicate_ids(self):
        x=self.frame()
        x["sources"][1]["issues"][0]["id"]=x["sources"][0]["issues"][0]["id"]
        with self.assertRaises(IntakeError): sample(x)

    def test_reject_unsorted_frame(self):
        x=self.frame()
        x["sources"][1]["issues"][0],x["sources"][1]["issues"][1]=x["sources"][1]["issues"][1],x["sources"][1]["issues"][0]
        with self.assertRaises(IntakeError): sample(x)

    def test_reject_non_utc(self):
        x=self.frame()
        x["captured_at_utc"]="2026-10-12T10:28:55+02:00"
        with self.assertRaises(IntakeError): sample(x)

    def test_cli_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"out.json"
            cmd=[sys.executable,"-m","trending_study.task_intake","--input",str(FRAME),"--output",str(out)]
            a=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(a.returncode,0,a.stderr)
            self.assertEqual(json.loads(out.read_text())["selected_issue_candidates"],6)
            b=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(b.returncode,2)
            self.assertIn("File exists",b.stderr)

    def test_cli_rejects_duplicate_pr_flag_and_nonfinite_json_before_classification(self):
        # The duplicate PR flag could silently reclassify a GitHub pull
        # request if a permissive json.loads reader kept the second value.
        duplicate = FRAME.read_text(encoding="utf-8").replace(
            '"is_pull_request": true',
            '"is_pull_request": true, "is_pull_request": false', 1)
        self.assertIn('"is_pull_request": false', duplicate)
        for raw in (duplicate, '{"x":NaN}', '{"x":Infinity}',
                    '{"x":1e999}', '{"x":1e-999}'):
            with self.subTest(raw=raw[:60]), tempfile.TemporaryDirectory() as folder:
                parent = Path(folder)
                source = parent / "PRIVATE_SOURCE_FRAME.json"
                output = parent / "result.json"
                source.write_text(raw, encoding="utf-8")
                proc = subprocess.run(
                    [sys.executable, "-m", "trending_study.task_intake",
                     "--input", str(source), "--output", str(output)],
                    capture_output=True, text=True,
                )
                self.assertEqual(proc.returncode, 2)
                self.assertIn("invalid or unsafe task-intake JSON input", proc.stderr)
                self.assertNotIn("PRIVATE_SOURCE_FRAME", proc.stderr)
                self.assertNotIn("is_pull_request", proc.stderr)
                self.assertFalse(output.exists())

    def test_cli_rejects_unsafe_and_oversized_task_frame(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            link = root / "PRIVATE_SYMLINK_INPUT.json"
            link.symlink_to(FRAME)
            oversize = root / "PRIVATE_TOO_BIG.json"
            oversize.write_bytes(b" " * (16 * 1024 * 1024 + 1))
            for source in (link, root, oversize):
                with self.subTest(source=source.name):
                    output = root / "new-result.json"
                    proc = subprocess.run(
                        [sys.executable, "-m", "trending_study.task_intake",
                         "--input", str(source), "--output", str(output)],
                        capture_output=True, text=True,
                    )
                    self.assertEqual(proc.returncode, 2)
                    self.assertIn("invalid or unsafe task-intake JSON input", proc.stderr)
                    self.assertNotIn("PRIVATE_", proc.stderr)
                    self.assertFalse(output.exists())

    def test_cli_preserves_frozen_90_row_16_issue_intake(self):
        # Exercise the genuine CLI, not just the deterministic sample() helper.
        with tempfile.TemporaryDirectory() as d:
            output = Path(d) / "source_selection.json"
            run = subprocess.run(
                [sys.executable, "-m", "trending_study.task_intake",
                 "--input", str(CROSS_ECOSYSTEM_FRAME), "--output", str(output)],
                capture_output=True, text=True,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout), {
                "total_rows": 90, "selected_issue_candidates": 16
            })
            stored = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual((stored["total_rows"], stored["selected_issue_candidates"]),
                             (90, 16))
            self.assertEqual(sum(row["selection_status"] == "excluded_pr_not_issue"
                                 for row in stored["ledger"]), 46)
            frame = json.loads(CROSS_ECOSYSTEM_FRAME.read_text(encoding="utf-8"))
            self.assertEqual(stored["reduced_frame_sha256"],
                             sample(frame)["reduced_frame_sha256"])
            self.assertTrue(all(row["independent_acceptance_status"] == "not_frozen"
                                for row in stored["ledger"]))

    def test_cli_output_errors_do_not_expose_private_paths_or_clobber(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            missing = root / "PRIVATE_TASK_SOURCE.json"
            private_dest = root / "PRIVATE_UNREVIEWED_PARTICIPANT.json"
            private_dest.write_text("PRESERVE_THIS", encoding="utf-8")
            cases = (
                (missing, root / "not_written.json", "invalid or unsafe task-intake"),
                (FRAME, private_dest, "File exists"),
            )
            for source, destination, error in cases:
                with self.subTest(source=source.name, destination=destination.name):
                    run = subprocess.run(
                        [sys.executable, "-m", "trending_study.task_intake",
                         "--input", str(source), "--output", str(destination)],
                        capture_output=True, text=True,
                    )
                    self.assertEqual(run.returncode, 2)
                    self.assertIn(error, run.stderr)
                    self.assertNotIn("PRIVATE_", run.stderr)
                    self.assertFalse((root / "not_written.json").exists())
            self.assertEqual(private_dest.read_text(encoding="utf-8"),
                             "PRESERVE_THIS")

    def test_direct_cli_exit_has_no_private_exception_context(self):
        # stderr-only subprocess checks miss the chained FileExistsError/JSON
        # decoder exception attached to an in-process SystemExit.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            missing = root / "PRIVATE_SOURCE_MISSING.json"
            private_out = root / "PRIVATE_OUTPUT_ALREADY_EXISTS.json"
            private_out.write_text("PRESERVE_EXISTING", encoding="utf-8")
            malformed = root / "PRIVATE_INPUT_DUPLICATE_KEY.json"
            malformed.write_text('{"PRIVATE_RAW_FIELD":1,"PRIVATE_RAW_FIELD":2}',encoding="utf-8")
            for input_path, output_path in (
                (missing, root / "new.json"),
                (malformed, root / "fresh.json"),
                (FRAME, private_out),
            ):
                with self.subTest(case=input_path.name):
                    stderr = io.StringIO()
                    with redirect_stderr(stderr):
                        with self.assertRaises(SystemExit) as raised:
                            main(["--input", str(input_path), "--output", str(output_path)])
                    error = raised.exception
                    self.assertEqual(error.code, 2)
                    self.assertIsNone(error.__cause__)
                    self.assertIsNone(error.__context__)
                    trace = "".join(traceback.format_exception(error))
                    self.assertNotIn("PRIVATE_", trace + stderr.getvalue())
            self.assertEqual(private_out.read_text(encoding="utf-8"), "PRESERVE_EXISTING")

    def test_reject_future_labeled_capture(self):
        x = self.frame()
        x["captured_at_utc"] = "2030-01-01T00:00:00Z"
        with self.assertRaisesRegex(IntakeError, "future capture"):
            sample(x)

    def test_reject_noncanonical_repo_path_components(self):
        x = self.frame()
        for name in ("../click", "owner/..", "./repo", "owner/."):
            candidate = copy.deepcopy(x)
            candidate["sources"][0]["repository"] = name
            with self.subTest(repository=name):
                with self.assertRaisesRegex(IntakeError, "unsafe repository"):
                    sample(candidate)

    def test_reject_missing_source_frame_and_blank_seed(self):
        x = self.frame()
        x["source_panel"] = ""
        with self.assertRaisesRegex(IntakeError, "source_panel"):
            sample(x)
        x = self.frame()
        x["selection_seed"] = " "
        with self.assertRaisesRegex(IntakeError, "seed"):
            sample(x)


    def test_cross_ecosystem_public_metadata_frame_is_bounded_and_unreviewed(self):
        frame = json.loads(CROSS_ECOSYSTEM_FRAME.read_text(encoding="utf-8"))
        self.assertEqual(frame["dataset_kind"], "public_issue_intake_unreviewed")
        self.assertEqual(frame["per_repo_target"], 3)
        self.assertEqual(len(frame["sources"]), 6)
        self.assertEqual(sum(len(src["issues"]) for src in frame["sources"]), 90)
        self.assertTrue(all(len(src["issues"]) == src["per_page"] == 15 for src in frame["sources"]))
        result = sample(frame)
        self.assertEqual(result["total_rows"], 90)
        self.assertEqual(result["selected_issue_candidates"], 16)
        self.assertEqual(sum(row["selection_status"] == "excluded_pr_not_issue" for row in result["ledger"]), 46)
        self.assertEqual(sum(row["selection_status"] == "eligible_issue_not_sampled" for row in result["ledger"]), 28)
        self.assertEqual(len({row["issue_id"] for row in result["ledger"]}), 90)
        self.assertEqual(
            [r["selected"] for r in result["per_repo"]],
            [3, 3, 3, 3, 2, 2],
        )
        for row in result["ledger"]:
            self.assertEqual(row["reuse_opportunity"], "unknown")
            self.assertEqual(row["task_spec_status"], "not_frozen")
            self.assertEqual(row["independent_acceptance_status"], "not_frozen")
            self.assertEqual(row["experiment_enrollment_status"], "not_eligible_unreviewed")
            if row["selection_status"] == "selected_for_independent_task_screen":
                self.assertIn("/issues/", row["source_url"])

    def test_cross_ecosystem_source_frame_rejects_privacy_leak(self):
        frame = json.loads(CROSS_ECOSYSTEM_FRAME.read_text(encoding="utf-8"))
        frame["sources"][0]["issues"][0]["body"] = "should never be copied into the public reduced frame"
        with self.assertRaisesRegex(IntakeError, "unexpected issue fields"):
            sample(frame)


    def test_human_screen_queue_matches_deterministic_frame_selection(self):
        frame = json.loads(CROSS_ECOSYSTEM_FRAME.read_text(encoding="utf-8"))
        expected = {
            item["source_url"]
            for item in sample(frame)["ledger"]
            if item["selection_status"] == "selected_for_independent_task_screen"
        }
        queue = (
            Path(__file__).resolve().parents[1]
            / "research-notes" / "task-screen-queue-2026-10-12.md"
        ).read_text(encoding="utf-8")
        actual = re.findall(r"\]\((https://github\.com/[^)]+/issues/\d+)\)", queue)
        self.assertEqual(len(actual), 16)
        self.assertEqual(set(actual), expected)
        self.assertIn("unreviewed", queue.lower())
        self.assertIn("not_frozen", queue)


if __name__=="__main__":
    unittest.main()
