"""Offline regression checks; all names/reviewer evidence are synthetic."""
import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest

from trending_study import quiet_reuse_registry as registry


class RegistryPairIntegrityTests(unittest.TestCase):
    def manifest_and_plan(self):
        commit = "e" * 40
        segments = []
        for sid, path, name in (("length2", "2", "ab"), ("length3_a", "3/a", "abc")):
            segments.append({"segment_id": sid, "index_path": path,
                             "directory_tree_sha": "f" * 40,
                             "source_url": f"https://api.github.com/repos/rust-lang/crates.io-index/contents/{path}?ref={commit}",
                             "declared_count": 1,
                             "entries": [{"package_name": name, "blob_sha": "1" * 40}]})
        manifest = {"schema_version": "1.0", "dataset_kind": registry.SOURCE_KIND,
                    "registry": "crates.io", "index_commit_sha": commit,
                    "observed_at_utc": "2026-01-01T00:00:00Z", "segments": segments}
        plan = {"schema_version": "1.0", "dataset_kind": "registry_slice_sampling_plan",
                "index_commit_sha": commit, "declared_at_utc": "2026-01-01T00:00:00Z",
                "seed": "synthetic-fixed-seed", "policy": registry.POLICY,
                "quotas": {"length2": 1, "length3_a": 1}}
        return manifest, plan

    def packet(self):
        # A fictional package selection, independently authored task fixture,
        # and reviewer IDs do not establish any real scientific acceptance.
        manifest, plan = self.manifest_and_plan()
        selection = registry.select_registry(manifest, plan)
        tasks = [{"task_id": "T1", "baseline_utc": "2026-01-01T00:00:00Z",
                  "spec_sha256": "c" * 64, "acceptance_sha256": "d" * 64,
                  "source_ref": "synthetic:task"}]
        pairs = [{"pair_id": "P1", "task_id": "T1", "package_id": "pkg:cargo/ab",
                  "version": "1.0.0", "release_evidence_ref": "synthetic:release",
                  "repository_id": 123, "identity_evidence_ref": "synthetic:identity"}]
        return registry.prepare_pair_packet(selection, tasks, pairs, manifest, plan)

    def test_edited_off_frame_selection_cannot_nominate_forged_package(self):
        manifest, plan = self.manifest_and_plan()
        packet = self.packet()
        selection = registry.select_registry(manifest, plan)
        selection["selected"][0]["package_id"] = "pkg:cargo/forged-off-frame"
        nomination = dict(packet["pairs"][0], package_id="pkg:cargo/forged-off-frame")
        with self.assertRaisesRegex(registry.RegistryFrameError, "original manifest and plan"):
            registry.prepare_pair_packet(selection, packet["tasks"], [nomination], manifest, plan)

    def test_source_or_plan_changes_require_new_selection(self):
        for changed in ("source", "plan", "count"):
            with self.subTest(changed=changed):
                manifest, plan = self.manifest_and_plan()
                selection = registry.select_registry(manifest, plan)
                packet = self.packet()
                if changed == "source":
                    manifest["segments"][0]["entries"][0]["blob_sha"] = "2" * 40
                elif changed == "plan":
                    plan["seed"] = "different-synthetic-seed"
                else:
                    selection["selected_package_leads"] = True
                with self.assertRaisesRegex(registry.RegistryFrameError, "original manifest and plan"):
                    registry.prepare_pair_packet(selection, packet["tasks"], packet["pairs"], manifest, plan)

    def reports(self, packet):
        def one(ref):
            return {"schema_version": "1.0", "packet_sha256": packet["packet_sha256"],
                    "reviewer_ref": ref, "reviewed_at_utc": "2026-01-02T00:00:00Z",
                    "decisions": [{"pair_id": "P1", "fit": "direct", "functional": "pass",
                                   "license": "compatible", "security": "acceptable",
                                   "availability": "before_baseline",
                                   "evidence_ref": "synthetic:review",
                                   "test_evidence_ref": "synthetic:tests"}]}
        return one("synthetic_A"), one("synthetic_B")

    def fingerprint(self, packet):
        packet["packet_sha256"] = registry._digest({
            k: v for k, v in packet.items() if k != "packet_sha256"})

    def assert_invalid(self, packet):
        # Recompute the caller-supplied hash to prove fingerprint validation
        # alone does not protect the packet's denominator/schema contract.
        self.fingerprint(packet)
        with self.assertRaises(registry.RegistryFrameError):
            registry.audit_pair_reviews(packet, *self.reports(packet))

    def test_valid_pair_is_counted_once_but_never_authenticates_humans(self):
        packet = self.packet()
        audit = registry.audit_pair_reviews(packet, *self.reports(packet))
        self.assertEqual(audit["nominated_pairs"], 1)
        self.assertEqual(audit["concordant_provisional_fit"], 1)
        self.assertEqual(audit["two_reports_present"], 1)
        self.assertFalse(audit["meets_issue_15_scientific_acceptance"])
        self.assertFalse(audit["reviewers_authenticated_as_real_independent_humans"])

    def test_duplicate_pair_id_cannot_multiply_one_review(self):
        packet = self.packet()
        packet["pairs"].append(copy.deepcopy(packet["pairs"][0]))
        packet["nominated_pair_count"] = 2
        self.assert_invalid(packet)

    def test_duplicate_task_component_with_distinct_pair_id_rejected(self):
        packet = self.packet()
        duplicate = dict(packet["pairs"][0], pair_id="P2")
        packet["pairs"].append(duplicate)
        packet["nominated_pair_count"] = 2
        self.assert_invalid(packet)

    def test_pair_count_is_exact_nonboolean_integer(self):
        for count in (0, 2, True, 1.0, "1"):
            with self.subTest(count=count):
                packet = self.packet()
                packet["nominated_pair_count"] = count
                self.assert_invalid(packet)

    def test_duplicate_task_or_unknown_task_rejected(self):
        packet = self.packet()
        packet["tasks"].append(copy.deepcopy(packet["tasks"][0]))
        self.assert_invalid(packet)
        packet = self.packet()
        packet["pairs"][0]["task_id"] = "unframed"
        self.assert_invalid(packet)

    def test_invalid_version_or_unknown_schema_field_rejected(self):
        for key, value in (("schema_version", "2.0"),
                           ("independent_task_claims_unverified", False),
                           ("extra", "unchecked")):
            packet = self.packet()
            packet[key] = value
            self.assert_invalid(packet)

    def test_malformed_pair_identity_rejected(self):
        for key, value in (("pair_id", "../P1"), ("package_id", "pkg:pypi/ab"),
                           ("repository_id", True), ("repository_id", -1),
                           ("version", ""), ("identity_evidence_ref", "")):
            with self.subTest(key=key, value=value):
                packet = self.packet()
                packet["pairs"][0][key] = value
                self.assert_invalid(packet)

    def test_invalid_task_provenance_or_shape_rejected(self):
        for key, value in (("baseline_utc", "2026-01-01T00:00:00"),
                           ("spec_sha256", "not-a-sha"), ("source_ref", "")):
            packet = self.packet()
            packet["tasks"][0][key] = value
            self.assert_invalid(packet)
        packet = self.packet()
        packet["tasks"] = []
        self.assert_invalid(packet)
        packet = self.packet()
        packet["pairs"] = None
        self.assert_invalid(packet)

    def test_missing_or_single_review_preserves_denominator(self):
        packet = self.packet()
        a, b = self.reports(packet)
        b["decisions"] = []
        audit = registry.audit_pair_reviews(packet, a, b)
        self.assertEqual(audit["nominated_pairs"], 1)
        self.assertEqual(audit["two_reports_present"], 0)
        self.assertEqual(audit["concordant_provisional_fit"], 0)
        self.assertEqual(audit["pair_statuses"], [{"pair_id": "P1", "status": "single_review_only"}])

    def test_direct_reader_reuses_strict_json_guard(self):
        documents = ('{"version": "wrong", "version": "1.0"}',
                     '{"value": NaN}', '{"value": Infinity}',
                     '{"value": 1e999}', '{"value": 1e-999}')
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            for raw in documents:
                with self.subTest(raw=raw):
                    path.write_text(raw, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        registry._read(path)
            path.write_text(json.dumps({"value": None}), encoding="utf-8")
            self.assertEqual(registry._read(path), {"value": None})

    def test_cli_prepare_rederives_selection_from_original_inputs(self):
        manifest, plan = self.manifest_and_plan()
        packet = self.packet()
        selection = registry.select_registry(manifest, plan)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            payloads = {"manifest": manifest, "plan": plan, "selection": selection,
                        "tasks": packet["tasks"], "nominations": packet["pairs"]}
            args = ["prepare-pairs"]
            for name, value in payloads.items():
                path = root / f"{name}.json"
                path.write_text(json.dumps(value), encoding="utf-8")
                args.extend((f"--{name}", str(path)))
            output = root / "packet.json"
            args.extend(("--output", str(output)))
            with redirect_stdout(io.StringIO()):
                registry.main(args)
            self.assertEqual(registry._read(output), packet)
            # Keep the original output intact on the failed second attempt.
            saved = output.read_bytes()
            selection["selected"][0]["package_id"] = "pkg:cargo/forged"
            (root / "selection.json").write_text(json.dumps(selection), encoding="utf-8")
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                registry.main(args)
            self.assertEqual(exc.exception.code, 2)
            self.assertEqual(output.read_bytes(), saved)

    def test_cli_ambiguous_json_fails_before_output_publication(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text('{"schema_version":"wrong","schema_version":"1.0"}', encoding="utf-8")
            output = Path(tmp) / "result.json"
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                registry.main(["select", "--manifest", str(path), "--plan", str(path),
                               "--output", str(output)])
            self.assertEqual(exc.exception.code, 2)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
