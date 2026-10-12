"""Synthetic-only scientific gate tests; no GitHub requests or package execution."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study.blind_review import ReviewError, audit, fingerprint, prepare

try:
    from trending_study.goldset import evaluate as goldset_evaluate
except ImportError:
    goldset_evaluate = None  # Full repository CI checks the integration.

ROOT = Path(__file__).resolve().parents[1]
EX = ROOT / "examples"

def fixture(name):
    return json.loads((EX / name).read_text(encoding="utf-8"))

class BlindReviewTests(unittest.TestCase):
    def setUp(self):
        self.pool = fixture("review_pool.synthetic.json")
        self.a = fixture("review_rater_a.synthetic.json")
        self.b = fixture("review_rater_b.synthetic.json")
        self.c = fixture("review_adjudication.synthetic.json")

    def test_blinded_packet_masks_rank_sources_and_prior_labels(self):
        packet = prepare(self.pool)
        self.assertEqual(packet["dataset_kind"], "synthetic")
        self.assertEqual(packet["pool_sha256"], fingerprint(self.pool))
        as_text = json.dumps(packet)
        for sensitive in ("registry-example", "lexical-example", "deep-audit-example",
                          "retrieval_runs", "ranked_candidate_ids", "channel", "final_label", "reviewer_labels"):
            self.assertNotIn(sensitive, as_text)
        self.assertEqual(len(packet["tasks"]), 2)
        self.assertEqual(len(packet["tasks"][0]["candidates"]), 4)

    def test_deterministic_and_order_independent_hash(self):
        self.assertEqual(prepare(self.pool), prepare(self.pool))
        shuffled = json.loads(json.dumps(self.pool, sort_keys=True))
        self.assertEqual(fingerprint(self.pool), fingerprint(shuffled))

    def test_audit_counts_and_keeps_unknown(self):
        result = audit(self.pool, self.a, self.b, self.c)
        self.assertEqual(result["pairs"], 4)
        self.assertEqual(result["double_reviewed"], 3)
        self.assertAlmostEqual(result["raw_agreement"], 2 / 3)
        self.assertAlmostEqual(result["cohen_kappa"], 0.5)
        self.assertEqual(result["provisional_labels"], {"not_viable": 1, "unknown": 2, "viable": 1})
        self.assertEqual(result["tasks_with_fewer_than_two_distinct_channels"], [])
        entries = {x["candidate_id"]: x for x in result["records"]}
        self.assertEqual(entries["C-B"]["status"], "missing_independent_review")
        self.assertEqual(entries["C-B"]["provisional_label"], "unknown")
        self.assertEqual(entries["C-C"]["status"], "adjudicated_disagreement")
        self.assertEqual(entries["C-C"]["provisional_label"], "not_viable")
        self.assertEqual(result["goldset_input"]["dataset_kind"], "synthetic")
        self.assertEqual(len(result["goldset_input"]["tasks"]), 2)

    def test_absent_adjudicator_stays_unknown(self):
        result = audit(self.pool, self.a, self.b)
        status = {x["candidate_id"]: x for x in result["records"]}
        self.assertEqual(status["C-C"]["provisional_label"], "unknown")
        self.assertEqual(status["C-C"]["status"], "unresolved_disagreement")
        self.assertEqual(result["provisional_labels"], {"unknown": 3, "viable": 1})

    def test_pool_candidate_needs_recorded_retrieval_or_deep_audit(self):
        pool=copy.deepcopy(self.pool)
        pool["tasks"][0]["retrieval_runs"] = pool["tasks"][0]["retrieval_runs"][:2]
        with self.assertRaisesRegex(ReviewError, "recorded retrieval"):
            prepare(pool)

    def test_review_timestamps_are_utc_after_task(self):
        a=copy.deepcopy(self.a)
        a["reviewed_at_utc"]="2026-10-11T11:00:00Z"
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)
        c=copy.deepcopy(self.c)
        c["adjudicated_at_utc"]="2026-10-11T13:03:00Z"
        with self.assertRaisesRegex(ReviewError, "precedes individual reviews"):
            audit(self.pool,self.a,self.b,c)

    def test_only_one_rater_does_not_validate(self):
        b=copy.deepcopy(self.b)
        b["judgments"] = []
        result=audit(self.pool,self.a,b)
        self.assertEqual(result["double_reviewed"], 0)
        self.assertIsNone(result["raw_agreement"])
        self.assertIsNone(result["cohen_kappa"])
        self.assertEqual(result["provisional_labels"], {"unknown": 4})

    def test_pool_hash_mismatch_rejected(self):
        b=copy.deepcopy(self.b)
        b["pool_sha256"]="f"*64
        with self.assertRaises(ReviewError): audit(self.pool,self.a,b)

    def test_extra_personal_metadata_is_rejected(self):
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["candidates"][0]["maintainer_email"]="private@example.com"
        with self.assertRaises(ReviewError): prepare(p)
        a=copy.deepcopy(self.a)
        a["reviewer_name"]="Alice"
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)

    def test_duplicate_candidate_or_task_rejected(self):
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["candidates"].append(copy.deepcopy(p["tasks"][0]["candidates"][0]))
        with self.assertRaises(ReviewError): prepare(p)
        p=copy.deepcopy(self.pool)
        p["tasks"].append(copy.deepcopy(p["tasks"][0]))
        with self.assertRaises(ReviewError): prepare(p)

    def test_unpooled_rank_candidate_rejected(self):
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["retrieval_runs"][0]["ranked_candidate_ids"].append("C-UNSEEN")
        with self.assertRaises(ReviewError): prepare(p)

    def test_wrong_reviewer_slot_rejected(self):
        b=copy.deepcopy(self.b)
        b["reviewer_slot"]="A"
        with self.assertRaises(ReviewError): audit(self.pool,self.a,b)

    def test_unknown_candidate_ref_rejected(self):
        a=copy.deepcopy(self.a)
        a["judgments"][0]["candidate_id"]="UNPOOL"
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)

    def test_duplicate_review_rejected(self):
        a=copy.deepcopy(self.a)
        a["judgments"].append(copy.deepcopy(a["judgments"][0]))
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)

    def test_viable_requires_real_availability_metadata(self):
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["candidates"][0]["available_since_utc"] = "2027-01-01T00:00:00Z"
        a=copy.deepcopy(self.a); b=copy.deepcopy(self.b)
        h=fingerprint(p)
        a["pool_sha256"]=b["pool_sha256"]=h
        with self.assertRaisesRegex(ReviewError, "released after"):
            audit(p,a,b)

    def test_viable_rejects_missing_license_evidence(self):
        a=copy.deepcopy(self.a)
        a["judgments"][0]["evidence_refs"]["license"] = None
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)

    def test_viable_rejects_unknown_security(self):
        a=copy.deepcopy(self.a)
        a["judgments"][0]["gates"]["security"] = "unknown"
        a["judgments"][0]["evidence_refs"]["security"] = None
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)

    def test_not_viable_requires_documented_failure(self):
        a=copy.deepcopy(self.a)
        a["judgments"][2]["gates"]["functional"] = "unknown"
        a["judgments"][2]["evidence_refs"]["functional"] = None
        with self.assertRaises(ReviewError): audit(self.pool,a,self.b)

    def test_adjudicator_only_for_disagreement(self):
        c=copy.deepcopy(self.c)
        c["decisions"].append(copy.deepcopy(self.a["judgments"][0]))
        with self.assertRaises(ReviewError): audit(self.pool,self.a,self.b,c)

    def test_missing_acceptance_sha_rejected(self):
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["acceptance_sha256"]="not-a-hash"
        with self.assertRaises(ReviewError): prepare(p)

    def test_bad_timestamp_or_url_rejected(self):
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["baseline_utc"]="2026-10-11T14:00:00+02:00"
        with self.assertRaises(ReviewError): prepare(p)
        p=copy.deepcopy(self.pool)
        p["tasks"][0]["candidates"][0]["artifact_ref"]="http://not-secure.invalid"
        with self.assertRaises(ReviewError): prepare(p)

    def test_cli_round_trip_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            packet=Path(folder)/"packet.json"
            output=Path(folder)/"audit.json"
            prep=[sys.executable,"-m","trending_study.blind_review","prepare","--pool",
                  str(EX/"review_pool.synthetic.json"),"--output",str(packet)]
            a=subprocess.run(prep,capture_output=True,text=True,cwd=ROOT)
            self.assertEqual(a.returncode,0,a.stderr)
            b=subprocess.run(prep,capture_output=True,text=True,cwd=ROOT)
            self.assertNotEqual(b.returncode,0)
            self.assertIn("File exists",b.stderr)
            cmd=[sys.executable,"-m","trending_study.blind_review","audit","--pool",
                 str(EX/"review_pool.synthetic.json"),"--review-a",str(EX/"review_rater_a.synthetic.json"),
                 "--review-b",str(EX/"review_rater_b.synthetic.json"),"--adjudication",
                 str(EX/"review_adjudication.synthetic.json"),"--output",str(output)]
            c=subprocess.run(cmd,capture_output=True,text=True,cwd=ROOT)
            self.assertEqual(c.returncode,0,c.stderr)
            self.assertEqual(json.loads(output.read_text())["pairs"],4)

    @unittest.skipIf(goldset_evaluate is None, "Gold-set integration test runs in full GitHub repository")
    def test_export_consumed_by_existing_goldset(self):
        result = audit(self.pool,self.a,self.b,self.c)
        gold=goldset_evaluate(result["goldset_input"],k=2)
        self.assertEqual(gold["task_count"],2)
        self.assertEqual(gold["results"][0]["pool_verified_viable"],1)
        self.assertEqual(gold["results"][0]["pool_unknown"],2)
    @unittest.skipIf(goldset_evaluate is None, "Full repo integration required")
    def test_availability_only_failure_survives_goldset_export(self):
        """Post-task-baseline release cannot be a historical viable alternative."""
        pool = copy.deepcopy(self.pool)
        a, b = copy.deepcopy(self.a), copy.deepcopy(self.b)
        candidate = pool["tasks"][0]["candidates"][0]
        # Task at 12:00, code first released 12:30, both reviews at 13:00+.
        candidate["available_since_utc"] = "2026-10-11T12:30:00Z"
        for review in (a, b):
            choice = next(j for j in review["judgments"]
                          if j["task_id"] == "SYNTH-TASK-1" and j["candidate_id"] == "C-A")
            choice["label"] = "not_viable"
            choice["gates"]["availability"] = "fail"
            choice["decision_ref"] = "SYNTHETIC-NOT-REAL:post-baseline-availability-failure"
            review["pool_sha256"] = fingerprint(pool)
        result = audit(pool, a, b)  # no real reviewers, synthetic only
        exported = result["goldset_input"]["tasks"][0]["candidates"][0]
        self.assertEqual(exported["gates"]["availability"], "fail")
        self.assertTrue(all(exported["gates"][key] == "pass"
                            for key in ("functional", "license", "security", "maintenance")))
        gold = goldset_evaluate(result["goldset_input"], k=2)
        self.assertEqual(gold["results"][0]["pool_verified_not_viable"], 1)

    def test_cannot_claim_availability_pass_when_release_is_after_baseline(self):
        pool = copy.deepcopy(self.pool)
        a = copy.deepcopy(self.a)
        b = copy.deepcopy(self.b)
        pool["tasks"][0]["candidates"][0]["available_since_utc"] = "2026-10-11T12:30:00Z"
        new_hash = fingerprint(pool)
        a["pool_sha256"] = new_hash
        b["pool_sha256"] = new_hash
        with self.assertRaisesRegex(ReviewError, "availability cannot pass"):
            audit(pool, a, b)



if __name__ == "__main__":
    unittest.main()
