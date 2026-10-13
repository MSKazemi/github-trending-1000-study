# Enterprise PR integration and CI integrity contract

**Reviewed:** 2026-10-13. **Issue:** [#244](https://github.com/MSKazemi/github-trending-1000-study/issues/244). **Scope:** tested engineering safeguards and process for this repo; **not a certified secure supply chain, completed empirical study or independent human review**.

## Why a green Python unittest run is necessary but insufficient

The previous [workflow](../.github/workflows/ci.yml) ran only `unittest discover` on Python 3.10 and 3.12. A new unused `.py` file with invalid syntax, unreferenced malformed `.json` research evidence, duplicate JSON keys or non-standard `NaN` could still be merged. The repo has many simultaneous PRs and **overlapping issue implementations**, so merges must preserve both code and research provenance rather than favor whichever branch is newest.

## CI changes in this PR

- **Pinned official actions**, checked via GitHub's official `/git/ref/tags/v4` / `v5` on 2026-10-13: `actions/checkout@11d5960a326750d5838078e36cf38b85af677262` and `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`. A full commit SHA prevents tag retargeting from silently changing the action used in a given run. **Periodically review versions and security advisories; pinning alone does not establish an action is safe**.
- Pinned GitHub-hosted Ubuntu image family to `ubuntu-24.04` (package/image content can still change; for complete reproducibility pin Docker image digest and toolchain too).
- Enforced read-only `GITHUB_TOKEN` with `permissions: contents: read`; no arbitrary external network calls or secret exposure are added by the gate.
- CI runs for PRs and for pushes to `main`, reducing duplicate push+PR jobs on the same feature branch. PR concurrency cancels superseded runs; two Python matrix versions have `fail-fast: false` so both failures remain visible, with a bounded 15-minute job timeout.
- `python scripts/check_artifact_integrity.py`: enumerates tracked `.py`, `.json` and `.jsonl` via `git ls-files -z` and **parses**, never executes, content. Python `ast.parse` finds syntax errors in even unimported modules; strict JSON check rejects invalid UTF-8, duplicate object keys at any depth, `NaN`/`Infinity`, non-finite numeric overflow and unreadable/escaped checkout paths; files over 8 MiB are explicitly rejected. JSONL lines are individually parsed, duplicate nested keys and nonfinite values fail closed with their original line numbers, and empty JSONL is rejected.
- The existing `python -m unittest discover -s tests -v` remains mandatory on **both Python 3.10 and 3.12**; twelve unit tests cover positive and negative artifact cases without external dependencies.
- Deterministic JSON errors include relative tracked paths, not personal content. The parser never fetches network URLs, installs third-party packages, validates licence terms, interprets human experiments or changes scientific data.

## How to reproduce locally

```bash
python scripts/check_artifact_integrity.py
python -m unittest discover -s tests -p 'test_artifact_integrity.py' -v
python -m unittest discover -s tests -v
```

**Green checks mean only syntactic/structural validity and execution of tested scenarios**. No machine-proof of reviewer identity, repository usefulness, package absence of vulnerability, authenticity of vendor reports, GitHub Trending capture authorization, accepted external task, AGENTS.md attribution or environmental savings is implied.

## Minimum evidence-gated pre-merge review (not automatically fulfilled by CI)

| Gate | Reviewer action and recorded evidence | Hard stop |
|---|---|---|
| Source/head identity | Review exact PR file list, immutable head SHA, base SHA, issue and test path; compare with current `main` | Unknown/inappropriate files, unrelated scope, hidden branch rewrite |
| Preservation | Review overlapping PRs, old/quiet candidate implementations and docs. Resolve conflicts **semantically**, preserving useful source data and negative findings. Use merge commits or bounded cherry-picks with explicit trace | Force-overwrite, silent deletion of evidence or duplication of competing engines |
| Correctness | Read new functions, error paths and tests; exercise negative/edge cases; update documentation/schema; verify Python 3.10+ support | Incorrect inputs accepted, unsafe file writes, missing regressions |
| Scientific validity | Confirm source URL/date/license rights, denominators, UTC provenance, audit trail and honest `unknown` state; distinguish experiment tools from actual experimental evidence | Invented users, timestamps, approval, full-page recall, environmental impact or causal result |
| Security | Assess secrets, network/process writes, untrusted input, dependency and GitHub permissions, package provenance and threat model | Known unsafe behavior, automated untrusted install, credential leakage |
| CI and integration | Required 3.10 and 3.12 `test` jobs green on exact reviewed integrated head; no cancelled/pending/failing checks; clean against latest `main`; recheck expected SHA at merge time | Tests fail, stale head, unresolved overlap or review outstanding |
| Post-merge | Verify merge commit contains exact intended files, `main` CI succeeded, docs and previous tests still present; link audit/issue | Regressions or missing evidence; revert or repair promptly |

**Do not automatically merge every draft**: a draft can document intentional blockers (missing human reviewers, data-access clearance, unpublished evidence, overlapping implementations). Even if CI is green, resolve the particular blocker or retain the PR as draft. Prefer actual independent code review for methodological changes.

## Concurrent-PR overlap audit (non-exhaustive, as observed on 2026-10-13)

GitHub's open-PR search returned **43 open PR references during this review**, with multiple branches updating/merging concurrently. That count is a momentary tool snapshot, **not a finalized PR outcome**. Notable conflicting scopes:

- **#5 documentation assessment** — [#183](https://github.com/MSKazemi/github-trending-1000-study/pull/183) rubric docs and [#187](https://github.com/MSKazemi/github-trending-1000-study/pull/187) rubric computation: distinct deliverables, but align vocabulary/denominators and retain originals.
- **#12 adoption/retention** — [#185](https://github.com/MSKazemi/github-trending-1000-study/pull/185) measurement plan vs [#210](https://github.com/MSKazemi/github-trending-1000-study/pull/210) evidence/missingness instrumentation: choose a canonical schema, keep dated complementary notes.
- **#22 supply-chain verification** — [#186](https://github.com/MSKazemi/github-trending-1000-study/pull/186) self-reported `package_trust` vs [#216](https://github.com/MSKazemi/github-trending-1000-study/pull/216) strict `package_review`: avoid shipping two unaligned decision engines merely because both are green. Preserve useful test scenarios and source notes when consolidating; distinguish official registry binding from claimed evidence.
- **Trending page audit** — canonical [#190](https://github.com/MSKazemi/github-trending-1000-study/pull/190) was found merged during review; any competing closed PR #52/#54 should be cross-checked for uniquely useful tests/docs rather than bulk-imported.
- **Company intelligence screens** — multiple recent provisional PRs contain public-vendor citations and six-month windows. A green test cannot confirm the company's claims, full source coverage, real-world adoption or predicted roadmap. Require exact source publication dates and explicit claim vs conjecture before promotion.
- **Core independent task work** — real issue metadata and synthetic audit tooling are permissible distinct outputs; human-independent task acceptance and consent **still require real evidence**. Issue #65 and prospective trial gates remain separate.

These are triage findings, not claims that every one of the 43 PR diffs was fully inspected. Decisions for each PR must be recorded on the individual PR with an exact commit and CI result.

## Repository protection still requiring an authorized maintainer setting

As checked during review, the `main` GitHub branch was **not marked protected**. This means tests may pass without being technically enforced at merge time. The GitHub Rulesets/Branch protection settings should require both CI matrix checks, disallow force pushes and deletions, and require qualified human/code-owner review for protected work. The connected GitHub action set here does **not** expose a branch-protection mutation; this document does not claim a ruleset was configured.

Recommended review settings for `main`: require PRs, require latest-commit required statuses (actual job names as shown in Actions), require at least one independent reviewer, dismiss stale reviews after code changes, require conversation resolution, disallow bypass except controlled emergencies, and enable secret scanning/CodeQL if available. Test the rule with a harmless failing PR before treating enforcement as active.

## Practical maintainer lesson

The smallest valuable improvement is **not another bulk-merge script**. It is evidence-backed merging: one reviewed task, one canonical implementation, comprehensive negative tests, immutable inputs, licensed reuse, honest unknowns and verified post-merge state. A green suite is one gate in that process—not proof that thousands of observations, verified adoption or green-computing savings exist.
