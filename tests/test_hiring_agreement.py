"""Offline synthetic structural regressions; not human source observations."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from trending_study import hiring_agreement as h
from trending_study.blind_review import fingerprint
from trending_study.rubric_agreement import _agreement

ROOT = Path(__file__).resolve().parents[1]
FRAME = ROOT / "references/hiring_agreement/pilot_frame_v1.json"
FIXTURES = ROOT / "tests/fixtures/hiring_agreement"


class HiringAgreementTests(unittest.TestCase):
    def setUp(self):
        self.frame = h.load_json(FRAME)
        self.a = h.load_json(FIXTURES / "coder_a.synthetic.json")
        self.b = h.load_json(FIXTURES / "coder_b.synthetic.json")
        self.c = h.load_json(FIXTURES / "adjudication.synthetic.json")

    def analyze(self, a=None, b=None, c=None):
        return h.analyze(self.frame, a or self.a, b or self.b, c, ROOT)

    def test_provenance_projection_keeps_every_lead(self):
        result = h.verify_frame(self.frame, ROOT)
        self.assertEqual(result["source_frame_n"], 24)
        self.assertEqual(result["selected_n"], 9)
        self.assertEqual(result["status_counts"], {"selected_pending_recheck":9,"index_text_only":13,
                                                 "identity_hold":1,"direct_access_unconfirmed":1})
        self.assertNotIn("theme_codes", json.dumps(self.frame))
        self.assertNotIn("theme_hypotheses", json.dumps(self.frame))

    def test_rejects_frame_forgery_and_extra_private_field(self):
        for key,value in (("items",self.frame["items"][:-1]),("participant_email","secret@example.com")):
            bad=copy.deepcopy(self.frame);bad[key]=value
            with self.assertRaises(ValueError):h.verify_frame(bad,ROOT)
        bad=copy.deepcopy(self.frame);bad["sources"][0]["sha256"]="0"*64
        with self.assertRaises(ValueError):h.verify_frame(bad,ROOT)

    def test_blank_packet_never_fabricates_coding(self):
        packet=h.prepare(self.frame, "coder_A", ROOT)
        self.assertFalse(packet["human_attested"])
        self.assertIsNone(packet["reviewed_at_utc"])
        self.assertEqual(len(packet["ratings"]),9)
        self.assertTrue(all(r["primary_task"]=="not_reviewable" for r in packet["ratings"]))
        with self.assertRaises(ValueError):self.analyze(a=packet)

    def test_binary_math_and_missingness_denominators(self):
        result=self.analyze()
        self.assertEqual(len(result["records"]),24)
        stats=result["per_theme"]["agent_runtime"]
        self.assertEqual(stats["confusion"],{"PP":2,"PA":1,"AP":1,"AA":2})
        self.assertEqual(stats["n"],6)
        self.assertEqual(stats["selected_n"],9)
        self.assertEqual(stats["excluded_n"],3)
        self.assertAlmostEqual(stats["observed_agreement"],2/3)
        self.assertAlmostEqual(stats["cohens_kappa"],1/3)
        self.assertAlmostEqual(stats["positive_agreement"],2/3)
        self.assertAlmostEqual(stats["negative_agreement"],2/3)
        self.assertEqual(stats["rater_a_exclusions"],{"missing":1,"uncertain":1,"not_reviewable":1})
        self.assertFalse(result["human_independence_verified"])
        self.assertFalse(result["source_rights_verified"])
        self.assertEqual(result["research_enrollment"],"blocked")
        self.assertEqual(result["review_a_sha256"],fingerprint(self.a))

    def test_primary_nominal_not_multilabel_pooled(self):
        stats=self.analyze()["primary_task"]
        self.assertEqual(stats["n"],6)
        self.assertAlmostEqual(stats["cohens_kappa"],1/3)
        self.assertNotIn("positive_agreement",stats)
        self.assertEqual(_agreement([("pass","pass"),("fail","fail")])["cohens_kappa"],1)
        self.assertEqual(_agreement([("platform","platform"),("operations","operations")],labels=("platform","operations"))["cohens_kappa"],1)

    def test_sparse_degenerate_and_no_pair_null(self):
        for pairs,reason in (([],"no jointly rated items"),([("present","absent")],"fewer than two jointly rated items"),([("absent","absent")]*3,"chance agreement is one")):
            stats=h._statistics(pairs,("present","absent"))
            self.assertIsNone(stats["cohens_kappa"])
            self.assertEqual(stats["reason"],reason)
        stats=h._statistics([("absent","absent")]*3,("present","absent"))
        self.assertIsNone(stats["positive_agreement"])
        self.assertEqual(stats["negative_agreement"],1)

    def test_missing_records_retained_and_not_negative(self):
        a=copy.deepcopy(self.a);a["ratings"]=[]
        result=self.analyze(a=a)
        self.assertEqual(result["selected_n"],9)
        for stats in result["per_theme"].values():
            self.assertEqual(stats["n"],0)
            self.assertEqual(stats["rater_a_exclusions"]["missing"],9)

    def test_rejects_duplicate_unknown_ids_missing_decisions(self):
        variants=[]
        x=copy.deepcopy(self.a);x["ratings"].append(copy.deepcopy(x["ratings"][0]));variants.append(x)
        x=copy.deepcopy(self.a);x["ratings"][0]["item_id"]="E01";variants.append(x)
        x=copy.deepcopy(self.a);del x["ratings"][0]["themes"]["agent_runtime"];variants.append(x)
        x=copy.deepcopy(self.a);x["ratings"][0]["themes"]["novel_theme"]="present";variants.append(x)
        x=copy.deepcopy(self.a);x["ratings"][0]["themes"]["agent_runtime"]=[];variants.append(x)
        for x in variants:
            with self.assertRaises(ValueError):self.analyze(a=x)

    def test_inaccessible_sources_never_negative_or_positive(self):
        for vote in ("present","absent","uncertain"):
            a=copy.deepcopy(self.a);a["ratings"][5]["themes"]["agent_runtime"]=vote
            with self.assertRaises(ValueError):self.analyze(a=a)

    def test_primary_requires_matching_present_theme(self):
        a=copy.deepcopy(self.a);a["ratings"][0]["themes"]["agent_runtime"]="absent"
        with self.assertRaises(ValueError):self.analyze(a=a)
        a=copy.deepcopy(self.a);a["ratings"][0]["themes"]["other"]="not_reviewable"
        with self.assertRaises(ValueError):self.analyze(a=a)

    def test_pseudonym_and_dataset_attestations_fail_closed(self):
        for key,value in (("reviewer_id","FICTIONAL_b"),("reviewer_id","person@example.com"),("reviewer_id","unknown"),("human_attested",True),("human_attested",1),("dataset_kind","human_verified"),("contact_email","person@example.com")):
            a=copy.deepcopy(self.a);a[key]=value
            with self.assertRaises(ValueError):self.analyze(a=a)
        a=copy.deepcopy(self.a);a["dataset_kind"]="self_reported"
        with self.assertRaises(ValueError):self.analyze(a=a)

    def test_hash_and_time_bindings(self):
        for key,value in (("frame_sha256","0"*64),("reviewed_at_utc","2026-10-12T00:00:00Z"),("reviewed_at_utc","2026-10-14T01:00:00"),("reviewed_at_utc","2099-10-14T01:00:00Z")):
            a=copy.deepcopy(self.a);a[key]=value
            with self.assertRaises(ValueError):self.analyze(a=a)
        a=copy.deepcopy(self.a);a["ratings"][0]["source_checked_at_utc"]="2026-10-14T01:01:00Z"
        with self.assertRaises(ValueError):self.analyze(a=a)

    def test_adjudication_preserves_raw_stats_original_votes(self):
        before=self.analyze();after=self.analyze(c=self.c)
        self.assertEqual(before["per_theme"],after["per_theme"])
        self.assertEqual(before["primary_task"],after["primary_task"])
        self.assertEqual(before["disagreements"],after["disagreements"])
        self.assertEqual(before["records"],after["records"])
        self.assertEqual(after["adjudication"]["status"],"partial")
        self.assertEqual(len(after["adjudication"]["decisions"]),2)

    def test_adjudication_only_actual_disputes_and_bound_inputs(self):
        for key,value in (("review_a_sha256","0"*64),("adjudicator_id","fictional_A"),("predictions_unseen_attested",False),("adjudicated_at_utc",self.a["reviewed_at_utc"])):
            c=copy.deepcopy(self.c);c[key]=value
            with self.assertRaises(ValueError):self.analyze(c=c)
        c=copy.deepcopy(self.c);c["decisions"][0]["item_id"]="S01"
        with self.assertRaises(ValueError):self.analyze(c=c)
        c=copy.deepcopy(self.c);c["decisions"].append(c["decisions"][0])
        with self.assertRaises(ValueError):self.analyze(c=c)
        c=copy.deepcopy(self.c);c["decisions"][0]["decision"]="absent"
        with self.assertRaises(ValueError):self.analyze(c=c)

    def test_json_rejects_duplicate_nonfinite_nested_large_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"input.json"
            for payload in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":1e999}', '['*25+'0'+']'*25, ' '* (h.MAX_BYTES+1)):
                path.write_text(payload)
                with self.assertRaises(ValueError):h.load_json(path)
            path.write_text('{}')
            alias=Path(tmp)/"alias.json";alias.symlink_to(path)
            with self.assertRaises(ValueError):h.load_json(alias)

    def test_cli_write_once_and_collisions(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/"report.json"
            command=[sys.executable,"-m","trending_study.hiring_agreement","analyze","--frame",str(FRAME),"--root",str(ROOT),"--coder-a",str(FIXTURES/"coder_a.synthetic.json"),"--coder-b",str(FIXTURES/"coder_b.synthetic.json"),"--output",str(out)]
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            saved=out.read_bytes()
            report=json.loads(saved)
            self.assertEqual(report["raw_input_sha256"], {
                "frame":hashlib.sha256(FRAME.read_bytes()).hexdigest(),
                "coder_a":hashlib.sha256((FIXTURES/"coder_a.synthetic.json").read_bytes()).hexdigest(),
                "coder_b":hashlib.sha256((FIXTURES/"coder_b.synthetic.json").read_bytes()).hexdigest(),
                "adjudication":None})
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)
            self.assertEqual(out.read_bytes(),saved)
            command[-1]=str(FRAME)
            result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
            self.assertNotEqual(result.returncode,0)


if __name__ == '__main__':
    unittest.main()
