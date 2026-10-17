"""Exact original byte identities for two noncanonical research branch drafts.

Git blob hashes prove a repository-content crosswalk, not research truth,
publisher authenticity, source permissions or reviewed method equivalence.
"""
from hashlib import sha1
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "research-notes/branch-draft-archive/2026-10-18-two-research-prototypes"

SOURCES = {
    "rank-drift/docs/TRENDING_DRIFT_OFFLINE_2026_10.md":
        "4208dc955a111b81e2995e1407b56c74a7e8a637",
    "rank-drift/tests/test_trending_drift.py.txt":
        "787a4975c5501c37db3c8270f5ee63d975c7e119",
    "rank-drift/code/trending_drift.py.txt":
        "837195677d4be06742a53a4ddd9519bd15db2c23",
    "package-trust/docs/PACKAGE_TRUST_INSTRUMENT_2026_10_12.md":
        "8ee9fa3b9082c8d58243a0b9c28b59296b71d7a7",
    "package-trust/examples/package_trust.synthetic.json.txt":
        "ca7518a044003865b2782bb18062c63355b78007",
    "package-trust/tests/test_package_trust.py.txt":
        "b66147fb8906b0a328bfa6b75689e4bbbec700bc",
    "package-trust/code/package_trust.py.txt":
        "b91060841ee6d80016d438174701040527c6428f",
}


def original_git_blob_hash(raw):
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


class HistoricalResearchDraftArchiveTests(unittest.TestCase):
    def test_all_seven_original_git_blobs_preserved_exactly(self):
        for relative, digest in SOURCES.items():
            with self.subTest(path=relative):
                path = ARCHIVE / relative
                self.assertTrue(path.is_file())
                self.assertEqual(original_git_blob_hash(path.read_bytes()), digest)

    def test_legacy_scripts_and_json_are_not_active_files(self):
        self.assertEqual(len(SOURCES), 7)
        self.assertEqual(
            {path.suffix for path in map(Path, SOURCES)
             if "code/" in str(path) or "tests/" in str(path)
             or "examples/" in str(path)},
            {".txt"},
        )
        archive_docs = (ARCHIVE / "README.md").read_text(encoding="utf-8")
        self.assertIn("NONCANONICAL", archive_docs)
        self.assertIn("branch-deletion authorization", archive_docs.lower())
        self.assertIn("real Trending capture", archive_docs)
        self.assertIn("source-rights", archive_docs)


if __name__ == "__main__":
    unittest.main()
