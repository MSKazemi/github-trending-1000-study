"""Offline regression checks; all names/reviewer evidence are synthetic."""
import copy
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import tempfile
import traceback
import unittest
from unittest import mock

from trending_study import quiet_reuse_registry as registry
from trending_study.data_integrity import MAX_FILE_BYTES


def tree_sha(entries):
    """Test-local Git tree-object SHA-1 for an all-blob directory listing."""
    body = b"".join(
        b"100644 " + e["package_name"].encode() + b"\0" + bytes.fromhex(e["blob_sha"])
        for e in sorted(entries, key=lambda e: e["package_name"].encode()))
    return hashlib.sha1(b"tree %d\0" % len(body) + body).hexdigest()


class RegistryPairIntegrityTests(unittest.TestCase):
    def manifest_and_plan(self):
        commit = "e" * 40
        segments = []
        for sid, path, name in (("length2", "2", "ab"), ("length3_a", "3/a", "abc")):
            entries = [{"package_name": name, "blob_sha": "1" * 40}]
            segments.append({"segment_id": sid, "index_path": path,
                             "directory_tree_sha": tree_sha(entries),
                             "source_url": f"https://api.github.com/repos/rust-lang/crates.io-index/contents/{path}?ref={commit}",
                             "declared_count": 1,
                             "entries": entries})
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
                    entries = manifest["segments"][0]["entries"]
                    entries[0]["blob_sha"] = "2" * 40
                    manifest["segments"][0]["directory_tree_sha"] = tree_sha(entries)
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
            registry.audit_pair_reviews(packet, *self.reports(packet), *self.manifest_and_plan())

    def test_floating_or_malformed_cargo_version_not_nominated(self):
        manifest, plan = self.manifest_and_plan()
        selection = registry.select_registry(manifest, plan)
        original = self.packet()
        invalid = ("latest", "main", "1", "1.0", "1.*", "^1.0.0",
                   ">=1.0.0", "1.0.0 || 2.0.0", "1.0.0/evil",
                   "1.0.0\\n2.0.0", "1.0.0-", "1.0.0+", "a"*129,
                   "01.2.3", "1.02.3", "1.2.03",
                   "1.2.3-alpha.01", "1.2.3-001", "1.2.3-rc.00+build.01")
        for version in invalid:
            nominations = copy.deepcopy(original["pairs"])
            nominations[0]["version"] = version
            with self.subTest(version=version), self.assertRaisesRegex(
                    registry.RegistryFrameError, "concrete pinned Cargo"):
                registry.prepare_pair_packet(selection, original["tasks"],
                                             nominations, manifest, plan)
        for version in ("1.0.0", "0.2.0-alpha.3", "2.1.4+build.5",
                        "2.1.4-rc.1+meta.7"):
            nominations = copy.deepcopy(original["pairs"])
            nominations[0]["version"] = version
            with self.subTest(valid_version=version):
                packet = registry.prepare_pair_packet(
                    selection, original["tasks"], nominations, manifest, plan)
                self.assertEqual(packet["pairs"][0]["version"], version)

    def test_forged_packet_hash_cannot_promote_floating_version(self):
        manifest, plan = self.manifest_and_plan()
        for version in ("latest", "^1.0.0", "1.*"):
            packet = self.packet()
            packet["pairs"][0]["version"] = version
            self.fingerprint(packet)  # attacker can recompute a plain hash
            a, b = self.reports(packet)
            with self.subTest(version=version), self.assertRaisesRegex(
                    registry.RegistryFrameError, "concrete pinned Cargo"):
                registry.audit_pair_reviews(packet, a, b, manifest, plan)

    def test_valid_pair_is_counted_once_but_never_authenticates_humans(self):
        packet = self.packet()
        audit = registry.audit_pair_reviews(packet, *self.reports(packet), *self.manifest_and_plan())
        self.assertEqual(audit["nominated_pairs"], 1)
        self.assertEqual(audit["concordant_provisional_fit"], 1)
        self.assertEqual(audit["two_reports_present"], 1)
        self.assertEqual(audit["externally_authenticated_human_pairs"], 0)
        self.assertEqual(audit["still_needed_for_50_authenticated_human_pairs"], 50)
        self.assertEqual(audit["still_needed_for_50_provisional"], 49)
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
        audit = registry.audit_pair_reviews(packet, a, b, *self.manifest_and_plan())
        self.assertEqual(audit["nominated_pairs"], 1)
        self.assertEqual(audit["two_reports_present"], 0)
        self.assertEqual(audit["concordant_provisional_fit"], 0)
        self.assertEqual(audit["pair_statuses"], [{"pair_id": "P1", "status": "single_review_only"}])

    def test_reviews_cannot_predate_independent_frozen_task_frame(self):
        packet = self.packet()
        a, b = self.reports(packet)
        a["reviewed_at_utc"] = "2025-12-31T23:59:59Z"
        with self.assertRaisesRegex(registry.RegistryFrameError, "predates"):
            registry.audit_pair_reviews(packet, a, b, *self.manifest_and_plan())
        # A modified packet with its hash recomputed still cannot accept a
        # coder's favorable pre-task vote as prospective task assessment.
        packet["tasks"][0]["baseline_utc"] = "2026-01-03T00:00:00Z"
        self.fingerprint(packet)
        a, b = self.reports(packet)
        with self.assertRaisesRegex(registry.RegistryFrameError, "predates"):
            registry.audit_pair_reviews(packet, a, b, *self.manifest_and_plan())
        # A report at the task baseline is chronologically possible but never
        # authenticates real human raters or independently frozen tasks.
        a["reviewed_at_utc"] = b["reviewed_at_utc"] = "2026-01-03T00:00:00Z"
        result = registry.audit_pair_reviews(packet, a, b, *self.manifest_and_plan())
        self.assertFalse(result["reviewers_authenticated_as_real_independent_humans"])
        self.assertFalse(result["meets_issue_15_scientific_acceptance"])

    def test_malformed_registry_timestamp_never_leaks_in_exception_chain(self):
        marker = "PRIVATE_REGISTRY_TIME_20261017"
        manifest, plan = self.manifest_and_plan()
        manifest["observed_at_utc"] = marker
        try:
            registry.select_registry(manifest, plan)
        except registry.RegistryFrameError as error:
            self.assertIn("invalid UTC", str(error))
            self.assertIsNone(error.__cause__)
            self.assertIsNone(error.__context__)
            self.assertNotIn(marker, "".join(traceback.format_exception(error)))
        else:
            self.fail("malformed registry timestamp must be refused")

    def test_private_duplicate_json_key_not_retained_in_registry_error_or_cli(self):
        marker = "PRIVATE_REGISTRY_JSON_KEY_20261017"
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "private-name.json"
            path.write_text(
                json.dumps({marker: 1})[:-1] + "," + json.dumps(marker) + ":2}",
                encoding="utf-8",
            )
            try:
                registry._read(path)
            except registry.RegistryFrameError as error:
                self.assertIsNone(error.__cause__)
                self.assertIsNone(error.__context__)
                self.assertNotIn(marker, "".join(traceback.format_exception(error)))
            else:
                self.fail("duplicate JSON must be refused")
            output = Path(folder) / "output.json"
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                try:
                    registry.main([
                        "select", "--manifest", str(path), "--plan", str(path),
                        "--output", str(output)])
                except SystemExit as error:
                    self.assertEqual(error.code, 2)
                    self.assertIsNone(error.__cause__)
                    self.assertIsNone(error.__context__)
                    self.assertNotIn(marker, stderr.getvalue())
                    self.assertNotIn(marker, "".join(traceback.format_exception(error)))
                else:
                    self.fail("ambiguous registry JSON must fail")
            self.assertFalse(output.exists())

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

    def test_direct_reader_rejects_large_special_and_linked_inputs(self):
        import os
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ordinary = root / "ordinary.json"
            ordinary.write_text('{"value": 1}', encoding="utf-8")
            self.assertEqual(registry._read(ordinary), {"value": 1})
            huge = root / "oversize.json"
            with huge.open("wb") as stream:
                stream.truncate(MAX_FILE_BYTES + 1)
            with self.assertRaisesRegex(registry.RegistryFrameError, "byte limit"):
                registry._read(huge)
            with self.assertRaises(registry.RegistryFrameError):
                registry._read(root)
            link = root / "linked.json"
            try:
                link.symlink_to(ordinary)
            except (OSError, NotImplementedError):
                pass  # Symlink creation is not supported on this host.
            else:
                with self.assertRaises(registry.RegistryFrameError):
                    registry._read(link)
            if hasattr(os, "mkfifo"):
                pipe = root / "untrusted.json"
                os.mkfifo(pipe)
                with self.assertRaises(registry.RegistryFrameError):
                    registry._read(pipe)

    def test_reader_redacts_private_duplicate_keys_and_keeps_output_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "private-file-name.json"
            path.write_text('{"secret-unique-marker":1,"secret-unique-marker":2}', encoding="utf-8")
            with self.assertRaises(registry.RegistryFrameError) as caught:
                registry._read(path)
            self.assertNotIn("secret-unique-marker", str(caught.exception))
            self.assertNotIn("private-file-name", str(caught.exception))
            target = root / "should-not-appear.json"
            with redirect_stderr(io.StringIO()) as stderr, self.assertRaises(SystemExit) as exited:
                registry.main(["select", "--manifest", str(path), "--plan", str(path),
                               "--output", str(target)])
            self.assertEqual(exited.exception.code, 2)
            self.assertFalse(target.exists())
            self.assertNotIn("secret-unique-marker", stderr.getvalue())
            self.assertNotIn("private-file-name", stderr.getvalue())

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

    def test_audit_rejects_refingerprinted_off_frame_or_rebound_packet(self):
        # The packet fingerprint is self-computed, so audit must re-bind the
        # packet to the original frame instead of trusting its own hashes.
        for change in ("package", "plan_hash", "source_hash"):
            with self.subTest(change=change):
                packet = self.packet()
                if change == "package":
                    packet["pairs"][0]["package_id"] = "pkg:cargo/offframe"
                elif change == "plan_hash":
                    packet["selection_plan_sha256"] = "0" * 64
                else:
                    packet["selection_source_sha256"] = "0" * 64
                self.fingerprint(packet)
                with self.assertRaisesRegex(registry.RegistryFrameError, "manifest and plan"):
                    registry.audit_pair_reviews(packet, *self.reports(packet),
                                                *self.manifest_and_plan())
        # A different (otherwise valid) plan cannot re-bind the same packet.
        packet = self.packet()
        manifest, plan = self.manifest_and_plan()
        plan["seed"] = "different-synthetic-seed"
        with self.assertRaisesRegex(registry.RegistryFrameError, "manifest and plan"):
            registry.audit_pair_reviews(packet, *self.reports(packet), manifest, plan)

    def test_cli_audit_requires_original_manifest_and_plan(self):
        manifest, plan = self.manifest_and_plan()
        packet = self.packet()
        a, b = self.reports(packet)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = ["audit-pairs"]
            for name, value in (("packet", packet), ("review-a", a), ("review-b", b),
                                ("manifest", manifest), ("plan", plan)):
                path = root / f"{name}.json"
                path.write_text(json.dumps(value), encoding="utf-8")
                args.extend((f"--{name}", str(path)))
            output = root / "audit.json"
            with redirect_stdout(io.StringIO()):
                registry.main(args + ["--output", str(output)])
            result = registry._read(output)
            self.assertEqual(result["externally_authenticated_human_pairs"], 0)
            self.assertFalse(result["meets_issue_15_scientific_acceptance"])
            missing = root / "missing-frame.json"
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                registry.main(args[:7] + ["--output", str(missing)])
            self.assertEqual(exc.exception.code, 2)
            self.assertFalse(missing.exists())

    def test_unhashable_identifiers_fail_as_frame_errors(self):
        manifest, plan = self.manifest_and_plan()
        manifest["segments"][0]["segment_id"] = ["length2"]
        with self.assertRaises(registry.RegistryFrameError):
            registry.select_registry(manifest, plan)
        manifest, plan = self.manifest_and_plan()
        packet = self.packet()
        selection = registry.select_registry(manifest, plan)
        bad = dict(packet["pairs"][0], task_id=["T1"])
        with self.assertRaises(registry.RegistryFrameError):
            registry.prepare_pair_packet(selection, packet["tasks"], [bad], manifest, plan)
        bad = dict(packet["pairs"][0], package_id={"x": 1})
        with self.assertRaises(registry.RegistryFrameError):
            registry.prepare_pair_packet(selection, packet["tasks"], [bad], manifest, plan)
        for key, value in (("fit", ["direct"]), ("pair_id", {"P1": 1})):
            with self.subTest(key=key):
                a, b = self.reports(packet)
                a["decisions"][0][key] = value
                with self.assertRaises(registry.RegistryFrameError):
                    registry.audit_pair_reviews(packet, a, b, manifest, plan)

    def test_reader_delegates_to_shared_research_json_loader(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            path.write_text('{"value": 1}', encoding="utf-8")
            with mock.patch.object(registry, "load_research_json_file",
                                   wraps=registry.load_research_json_file) as shared:
                self.assertEqual(registry._read(path), {"value": 1})
            shared.assert_called_once()

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
