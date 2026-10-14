"""Issue #15 registry pilot: synthetic contract checks; no real human adjudication."""
import copy
import hashlib
import unittest

from trending_study.quiet_reuse_registry import (
    POLICY, RegistryFrameError, audit_pair_reviews, prepare_pair_packet,
    select_registry,
)


def fake():
    sha = "a" * 40
    segments = []
    for sid, path, names in (("length2", "2", ["aa", "ab", "ac"]),
                             ("length3_a", "3/a", ["aaa", "aab", "aac"])):
        segments.append({
            "segment_id": sid, "index_path": path, "directory_tree_sha": sha,
            "source_url": ("https://api.github.com/repos/rust-lang/crates.io-index/"
                           "contents/" + path + "?ref=" + sha),
            "declared_count": len(names),
            "entries": [{"package_name": n, "blob_sha": "b"*40} for n in names],
        })
    return ({
        "schema_version": "1.0", "dataset_kind": "bounded_public_registry_index_listing",
        "registry": "crates.io", "index_commit_sha": sha,
        "observed_at_utc": "2026-10-12T00:00:00Z", "segments": segments,
    }, {
        "schema_version": "1.0", "dataset_kind": "registry_slice_sampling_plan",
        "index_commit_sha": sha, "declared_at_utc": "2026-10-12T00:00:00Z",
        "seed": "transparent-example", "policy": POLICY,
        "quotas": {"length2": 2, "length3_a": 2},
    })


def packet():
    m, p = fake()
    selection = select_registry(m, p)
    task = {"task_id": "task1", "baseline_utc": "2026-10-12T00:00:00Z",
            "spec_sha256": "c" * 64, "acceptance_sha256": "d" * 64,
            "source_ref": "synthetic://task"}
    nomination = {"pair_id": "pair1", "task_id": "task1",
                  "package_id": selection["selected"][0]["package_id"],
                  "version": None, "release_evidence_ref": None,
                  "repository_id": None, "identity_evidence_ref": None}
    return prepare_pair_packet(selection, [task], [nomination], m, p)


def report(pkt, ref):
    return {"schema_version": "1.0", "packet_sha256": pkt["packet_sha256"],
            "reviewer_ref": ref, "reviewed_at_utc": "2026-10-12T10:00:00Z",
            "decisions": [{"pair_id": "pair1", "fit": "unknown",
                           "functional": "not_run", "license": "unknown",
                           "security": "unknown", "availability": "unknown",
                           "evidence_ref": None, "test_evidence_ref": None}]}


class RegistrySliceTests(unittest.TestCase):
    def test_deterministic_selection_and_denominators(self):
        m, p = fake()
        a = select_registry(m, p)
        m["segments"][0]["entries"].reverse()
        self.assertEqual(a["selected"], select_registry(m, p)["selected"])
        self.assertEqual(a["registry_directory_denominator"], 6)
        self.assertEqual(a["selected_package_leads"], 4)
        self.assertEqual(a["external_repo_crosswalk_count"], 0)
        self.assertEqual(a["verified_task_component_pairs"], 0)
        self.assertFalse(a["population_prevalence_eligible"])

    def test_rejects_source_mismatch_duplicate_and_non_slice(self):
        m, p = fake()
        m["segments"][0]["source_url"] = m["segments"][0]["source_url"].replace(
            "ref=" + "a"*40, "ref=master")
        with self.assertRaises(RegistryFrameError):
            select_registry(m, p)
        m, p = fake()
        m["segments"][0]["entries"][1] = copy.deepcopy(m["segments"][0]["entries"][0])
        with self.assertRaises(RegistryFrameError):
            select_registry(m, p)
        m, p = fake()
        m["segments"][1]["entries"][0]["package_name"] = "bee"
        with self.assertRaises(RegistryFrameError):
            select_registry(m, p)

    def test_rejects_selection_after_outcome_and_quota_errors(self):
        m, p = fake()
        m["segments"][0]["entries"][0]["future_adoptions"] = 100
        with self.assertRaises(RegistryFrameError):
            select_registry(m, p)
        m, p = fake()
        p["quotas"]["length2"] = 4
        with self.assertRaises(RegistryFrameError):
            select_registry(m, p)
        m, p = fake()
        p["seed"] = "different"
        self.assertNotEqual(select_registry(m, p)["selection_plan_sha256"],
                            select_registry(m, fake()[1])["selection_plan_sha256"])

    def test_packet_rejects_out_of_frame_pair(self):
        m, p = fake()
        selection = select_registry(m, p)
        task = {"task_id": "task1", "baseline_utc": "2026-10-12T00:00:00Z",
                "spec_sha256": "c"*64, "acceptance_sha256": "d"*64,
                "source_ref": "synthetic://source"}
        with self.assertRaises(RegistryFrameError):
            prepare_pair_packet(selection, [task], [{
                "pair_id": "pair1", "task_id": "task1", "package_id": "pkg:cargo/outside",
                "version": None, "release_evidence_ref": None,
                "repository_id": None, "identity_evidence_ref": None}], m, p)

    def test_two_placeholder_reviews_never_satisfy_scientific_gate(self):
        pkt = packet()
        audit = audit_pair_reviews(pkt, report(pkt, "raterA"), report(pkt, "raterB"))
        self.assertEqual(audit["two_reports_present"], 1)
        self.assertEqual(audit["concordant_provisional_fit"], 0)
        self.assertEqual(audit["still_needed_for_50_provisional"], 50)
        self.assertFalse(audit["meets_issue_15_scientific_acceptance"])

    def test_same_reviewer_and_fabricated_pass_without_evidence(self):
        pkt = packet()
        a = report(pkt, "raterA")
        with self.assertRaises(RegistryFrameError):
            audit_pair_reviews(pkt, a, report(pkt, "raterA"))
        b = report(pkt, "raterB")
        b["decisions"][0]["functional"] = "pass"
        with self.assertRaises(RegistryFrameError):
            audit_pair_reviews(pkt, a, b)

    def test_packet_hash_cannot_be_modified_silently(self):
        pkt = packet()
        pkt["pairs"][0]["repository_id"] = 100
        with self.assertRaises(RegistryFrameError):
            audit_pair_reviews(pkt, report(pkt, "raterA"), report(pkt, "raterB"))

    def test_no_human_claim_from_two_favorable_report_cards(self):
        pkt = packet()
        pkt["pairs"][0].update({"version": "1.0.0", "release_evidence_ref": "synthetic",
                                "repository_id": 42, "identity_evidence_ref": "synthetic"})
        from trending_study.quiet_reuse_registry import _digest
        pkt["packet_sha256"] = _digest({k:v for k,v in pkt.items() if k!="packet_sha256"})
        a = report(pkt, "raterA")
        b = report(pkt, "raterB")
        for review in (a, b):
            review["decisions"][0].update({
                "fit": "direct", "functional": "pass",
                "license": "compatible", "security": "acceptable",
                "availability": "before_baseline", "evidence_ref": "synthetic",
                "test_evidence_ref": "synthetic"})
        result = audit_pair_reviews(pkt, a, b)
        self.assertEqual(result["concordant_provisional_fit"], 1)
        self.assertFalse(result["reviewers_authenticated_as_real_independent_humans"])
        self.assertFalse(result["meets_issue_15_scientific_acceptance"])


if __name__ == "__main__":
    unittest.main()
