# Enterprise PR quality, scientific review and no-loss merge policy

**Effective draft:** 2026-10-13. **Scope:** proposed engineering contribution for [issue #240](https://github.com/MSKazemi/github-trending-1000-study/issues/240). This explains how authorized maintainers should perform merges; a document alone cannot enforce branch protection, source permission or independent scientific approval.

## Purpose

Each merged change must improve useful, verifiable software without corrupting evidence, replacing research work prepared by another branch, or overstating empirical results. A GitHub Actions green check proves only what its particular automated checks ran. It **does not** prove scientific validity, privacy/consent, verified external reuse, license compliance or production safety.

The [2026-10-13 inventory](PR_AUDIT_2026-10-13.md) found many unfinished draft PRs and multiple different research contributions touching the same path. The policy prioritizes **no silent loss of source material** over merge volume.

## Preconditions — ordered, fail closed

| Gate | Minimum required evidence | Decision if not met |
|---|---|---|
| G0. Scope and human ownership | One bounded issue, reviewed spec/acceptance, affected methods and change risk; PR not Draft | Keep Draft |
| G1. Source/ethics authorization | Preserve GitHub Trending capture hard stop; no forbidden scrape/retry/bypass; verify opt-in consent, rights and privacy for human/enterprise traces | Block source collection or methodological change |
| G2. Research honesty | Verify observed source dates and IDs separately from authored/synthetic data, preserve unknown, failures, null results, intended sample denominator; cite original sources and label hypotheses | Block empirical claims and high-risk methods |
| G3. Code safety | Inspect whole diff, inputs/bounds, error paths, write-once behavior, secrets, licensing, dependency versions, reversible changes, cross-platform assumptions | Repair, extend tests and retest |
| G4. Compatibility and no-loss | Compare to **current** main and all overlapping PRs; check every touched file; retain original evidence and reconcile conflicting additions explicitly; no blind ours/theirs merges | Keep separate, produce merge-resolution PR, or request human adjudication |
| G5. CI with exact SHA | On the **merge candidate**: test matrix 3.10, 3.12, 3.13, Python compilation and research-artifact integrity; all named checks completed success | Do not merge if pending, skipped unexpectedly, outdated, cancelled or failing |
| G6. Independent human methods review | Qualified dated human review for new enrollment, statistical analysis, sampling/exclusion, real participant data, gold labels, privacy or changes to preregistered hypotheses; AI feedback does not impersonate that review | Do not call research approval complete |
| G7. Merge transaction | Reconfirm PR head SHA, base/current main, reviews, branch updates, conflicts and required checks immediately before merge. Use expected-head SHA; preserve source-level commit history with merge commits where it carries distinct evidence, and squash only when an independently reviewed mapping preserves every useful artifact | Retry only after resolving changed head/base; no force merge |
| G8. Verification after merge | Check main tree and CI, linked docs/source files, issue tracking, completed/deferred gates and rollback documentation | Revert safely or fix promptly; never destroy original captures |

These are **process requirements**, not a new research preregistration. Passing G5 is necessary but never sufficient.

## Enterprise engineering CI contract

The repository's read-only GitHub Actions workflow uses SHA-pinned official checkout/setup-python actions (v7.0.1 / v7.0.0; the official Git tag SHA was checked on 2026-10-13), with no repo write token, timeouts and isolated Python environments:

- `python -m compileall -q trending_study scripts tests`, then `python -m unittest discover -s tests -v` and CLI `--help` smoke checks on Python 3.10, 3.12, 3.13 and 3.14, using the Ubuntu 24.04 runner family.
- `python scripts/check_research_artifacts.py --root .` independently validates checked-out `examples/`, `references/`, `research-notes/` and, when present, `research/` and `templates/` JSON/JSONL/CSV files. It does not equate the filesystem with an authenticated Git source manifest. Reject malformed JSON, duplicate keys (including nested), NaN/Infinity, numeric literals that overflow/underflow representable finite values, gigantic integer fields, embedded NUL bytes, invalid UTF-8, missing directories, broken CSV field alignment, symlinks and oversized artifacts (16 MiB per file; 128 MiB cumulatively, at most 5,000 examined files), and deeply nested inputs that exceed the parser's safe recursion depth. This is **not a schema, source-authenticity, privacy or statistical validator**.
- The workflow avoids `pull_request_target` and injected credentials; untrusted PR tests run without secrets.

Version upgrades of tools or workflows require specific review and passing checks. The suite has not established fuzz resistance, real-source correctness, secure dependencies, nor enterprise deployment readiness. For security-sensitive changes, apply appropriate threat modeling and independent code review beyond this baseline.

### Reproduce locally

```bash
python -m compileall -q trending_study scripts tests
python -m unittest discover -s tests -v
python scripts/check_research_artifacts.py --root .
```

The artifact check is **read-only**, makes no external requests and reports artifact file counts, not source quality. It also does not parse Markdown citations or establish an original study finding.

## Handling conflicting pull requests: never silently choose a whole file

1. Capture current main SHA and each PR's exact head SHA. Inspect the complete file list, pairwise diff and semantic overlap; stale green checks must be rerun after integrating newer main.
2. Maintain both branches unchanged. If PRs modify the **same research note**, export or compare the original version, individual sources, dated event claims, search logs, counter-evidence and methodology from both.
3. Assign an appropriate independent reviewer to reconcile disputed factual claims and protocols. Do **not** concatenate contradictory findings and call them verified; preserve both original provenance records and status.
4. Create a separate clearly attributed synthesis/merge-resolution branch when warranted. Make individual source/event links and resolved/unresolved discrepancies explicit. Do not force push, delete, squash away original provenance, or overwrite immutable raw captures.
5. Run all updated tests and manual evidence checks on the integrated tree. Merge only after explicit human methods signoff where needed. Closing superseded PRs is allowed **only with a direct link to the merged replacement and verification that their valuable content survives**.
6. After the final merge, verify saved files in `main`, links, issue notes and source access restrictions. The existence of a branch is not proof its contribution reached `main`.

**Example collisions observed** in the snapshot: #191 vs #228 (Meta); #192 vs #229 (Amazon/AWS); #197 vs #231 (Amp Inc.); #212 vs #230 (Replit); #213 vs #232 (Qodo). These update the **same** Markdown path with visibly different report contents. Treat both versions as valuable unresolved evidence until reviewed. Proposed experimental tools for #22 (#186 vs #216), #12 (#185 vs #210) and #5 (#183 vs #187) have related scopes even when files do not collide; compare contracts before consolidating.

## Protected main branch — administrator steps still needed

**Observed access (2026-10-13):** GitHub's public repository rulesets endpoint returned `[]`, and `GET /branches/main` reported `protected: false`. The connected integration could not read the detailed branch protection endpoint (403). Thus no enforceable branch-protection gate was verified, and an administrator must confirm/update the configuration in Settings; endpoint restrictions do not imply protections are enabled. An authorized owner should check repository Settings → Rules → Rulesets / Branch protection and configure:

- No force pushes or branch deletion on `main`.
- Require an up-to-date, successful PR head/merge queue test matrix **and** `research-artifacts` job before merge; review actual rule evaluation and required status names, not just badge appearance.
- Require qualified non-author human approval of source/ethics/scientific or security-sensitive changes; dismiss stale approvals on new commits where the collaboration model permits it.
- Resolve blocking review comments, require conversation resolution and prevent admin bypass where appropriate; account for solo-maintainer constraints explicitly instead of fabricating approval.
- Prefer merge commits for independently sourced research-history preservation; squash/rebase only when review confirms that no unique source artifact, date or provenance chain would be lost. Record original PR and postmerge test status.

Because repository rulesets were not installed by this change and may be restricted by plan/policy, **no claim of technical enforcement by GitHub branch protection is made**.

## Risk-based review depth

| Change type | Additional checks |
|---|---|
| Offline code/tool | Negative and malformed-input tests, write-once semantics, no network default, API compatibility |
| Trending parser/capture | **Never** bypass robots/access stop; independent actual source review only after permission and approved protocol |
| Sampling, trial, metrics or causal inference | Independent study design, preregistration amendments and denominator leakage checks; separately authorize real humans |
| Agent execution / package supply chain | License/version/provenance/security gates, least privileges, isolation and no arbitrary remote code in CI |
| Energy, sustainability, financial costs | System boundary, calibrated sources, partial/missingness and currency/time units, no token-to-carbon multiplier |
| Corporate/news intelligence | First-party and independent source links, date-of-event vs date-of-publication, corroboration, contradictory evidence, duplicate overlapping PR comparison |
| Documentation-only methodology | Explicitly provisional vs reviewed methods, no invented signs/participants; human methods review before adoption as confirmatory protocol |

## Escalation and useful project lessons

- Stop merging immediately on unexpected overwritten evidence, unapproved source access, credentials in public files, incorrect research claims, failing CI, or loss of accepted task denominator.
- Preserve the smallest reliable implementation with tests and a runnable first-use example rather than multiplying parallel versions of the same logic.
- When agents submit patches, favor independently accepted tasks and real downstream reuse over line counts, stars, merge counts or volume of generated PRs.
- A PR quality policy is only valuable if it actually rejects or improves weak changes; track how many defects were caught **without incentivizing artificial failures or PR volumes**. Protect human maintainer time, and publish negative findings rather than inventing growth or carbon impact.
