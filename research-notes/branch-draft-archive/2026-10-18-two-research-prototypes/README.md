# Historical offline research prototypes — no-loss preservation, 2026-10-18

**Status: frozen, deliberately NONCANONICAL sources.** This folder preserves **seven exact Git blobs** from two historical divergent branch tips that are not active implementations on `main`. Their `.py.txt` and `.json.txt` extensions deliberately avoid automatic Python test discovery, CLI exposure and canonical research-data ingestion. The original branches and histories remain intact. This is **not** a branch-deletion authorization, scientific approval, safe-to-install package decision, real Trending capture, independent QA or externally observed result.

- `research/issue-6-rank-drift-oct2026` at `38728426909558fda5fcab618ea044eef48c7b8f`: a distinct early offline *synthetic* ranking-drift/overlap instrument for issue #6. Do not blindly import `trending_drift.py` as a second supported CLI alongside the newer canonical overlap/proxy tooling; compare mathematical contracts, real-source provenance, privacy and negative cases before any functional port.
- `research/issue22-package-trust-gate-20261012` at `d4619a9a1903ff53efc5fc89d14e54b43b9ea88d`: early static package-trust prototype, its synthetic fixture and tests for issue #22. This does **not** authenticate package registry origin, licensing, advisories or source rights, and must not shadow the newer `trending_study.package_review` evidence gate.

## Byte-level crosswalk

Each original Git blob is copied to a read-only-intent archival path **without any byte changes**. SHA-1 is Git's blob-object hash, *not* an external publisher attestation; the offline tests verify these exact content identities.

| Historical branch / original relative path | Preserved relative path in this folder | Original blob SHA-1 |
| --- | --- | --- |
| `research/issue-6-rank-drift-oct2026: docs/TRENDING_DRIFT_OFFLINE_2026_10.md` | `rank-drift/docs/TRENDING_DRIFT_OFFLINE_2026_10.md` | `4208dc955a111b81e2995e1407b56c74a7e8a637` |
| `research/issue-6-rank-drift-oct2026: tests/test_trending_drift.py` | `rank-drift/tests/test_trending_drift.py.txt` | `787a4975c5501c37db3c8270f5ee63d975c7e119` |
| `research/issue-6-rank-drift-oct2026: trending_study/trending_drift.py` | `rank-drift/code/trending_drift.py.txt` | `837195677d4be06742a53a4ddd9519bd15db2c23` |
| `research/issue22-package-trust-gate-20261012: docs/PACKAGE_TRUST_INSTRUMENT_2026_10_12.md` | `package-trust/docs/PACKAGE_TRUST_INSTRUMENT_2026_10_12.md` | `8ee9fa3b9082c8d58243a0b9c28b59296b71d7a7` |
| `research/issue22-package-trust-gate-20261012: examples/package_trust.synthetic.json` | `package-trust/examples/package_trust.synthetic.json.txt` | `ca7518a044003865b2782bb18062c63355b78007` |
| `research/issue22-package-trust-gate-20261012: tests/test_package_trust.py` | `package-trust/tests/test_package_trust.py.txt` | `b66147fb8906b0a328bfa6b75689e4bbbec700bc` |
| `research/issue22-package-trust-gate-20261012: trending_study/package_trust.py` | `package-trust/code/package_trust.py.txt` | `b91060841ee6d80016d438174701040527c6428f` |

## Why not merge executable legacy modules?

These are older, **divergent** tool prototypes with overlapping capabilities, unrelated historical changes and no claimed independent external/source-rights validation. Directly merging old branch file trees risks reintroducing weaker tests, duplicate public CLIs and stale research methodology. Instead, the integration commit uses current `main` as first parent and the **two original source tip commits as additional Git parents**, but includes only these passive archive copies, this README, a dated review checkpoint and archive-integrity tests as new working-tree files. The main active implementation, issue #6/#22 requirements and source data are unchanged.

## Follow-up acceptance still pending

1. Evaluate whether the legacy rank-drift metrics and RBO behavior differ materially from current canonical tools under independent, frozen tests; preserve null/negative results and record the semantic disposition.
2. Determine whether any unique safe supply-chain behavior is absent from canonical package-review. Do not automatically approve packages from self-declared fixtures or unreviewed security claims.
3. Obtain actual qualified human methods/security/rights review, protect recovery refs and `main` under #248, and meet the exact-SHA tag/lease restoration requirements under #277 before **any** branch is retired. Even history-backed archives do not prove server-side immutability while `main` is unprotected.

**Practical maintainer lesson:** archival integration can preserve conflicting earlier experiments and their exact source bytes without accidentally making them canonical. A branch-count reduction is not evidence of correct science, successful reuse, or lifecycle benefit. See [#279](https://github.com/MSKazemi/github-trending-1000-study/issues/279).
