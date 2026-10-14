"""Offline regression checks; all names/reviewer evidence are synthetic."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from trending_study import quiet_reuse_registry as registry


class RegistryPairIntegrityTests(unittest.TestCase):
    def packet(self):
        # A fictional package selection, independently authored task fixture,
        # and reviewer IDs do not establish any real scientific acceptance.
        selection = {
            "dataset_kind": "unreviewed_registry_leads",
            "selected": [{"package_id": "pkg:cargo/ab"}],
            "selection_plan_sha256": "a" * 64,
            "source_manifest_sha256": "b" * 64,
        }
        tasks = [{"task_id": "T1", "baseline_utc": "2026-01-01T00:00:00Z",
                  "spec_sha256": "c" * 64, "acceptance_sha256": "d" * 64,
                  "source_ref": "synthetic:task"}]
        pairs = [{"pair_id": "P1", "task_id": "T1", "package_id": "pkg:cargo/ab",
                  "version": "1.0.0", "release_evidence_ref": "synthetic:release",
                  "repository_id": 123, "identity_evidence_ref": "synthetic:identity"}]
        return registry.prepare_pair_packet(selection, tasks, pairs)

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


if __name__ == "__main__":
    unittest.main()
