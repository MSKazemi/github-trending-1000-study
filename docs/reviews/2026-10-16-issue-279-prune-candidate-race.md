# #279 — Read-only prune-candidate race audit (2026-10-16)

**Status:** proposed engineering correction. This document does not authorize deletion, close #279, or establish research approval.

## Observed repository checkpoint

The GitHub REST branch-list endpoint returned **28** branch entries in one page; the open-PR endpoint returned **5** PRs. `main` was at `639054a0b98fe29c8bd0d6d72fb16b19fc26bff9` with all **five** main-commit test and research-artifact checks successful. The rulesets endpoint was `[]`; no server-enforced review/branch protections were proven. These counts are moving observations on 2026-10-16, not a census of preserved unique evidence or a scientific outcome.

## Failure mode, source, and narrow change

The existing `scripts/branch_lifecycle_audit.py` enumerates branches, captures full branch SHA, enumerates open PRs, compares exact commit IDs and verifies the base remains the same. However, an **unprotected branch can move after its page listing and before the report**, and a new PR can be opened after the PR listing. The prior tool could still label that stale head `manual-prune-candidate`. The original value was always advisory, but even advisory stale classifications are dangerous in a branch-retirement runbook.

**Reuse-first decision:** extend the existing standard-library auditor and its existing synthetic tests. Do not create a second inventory engine, add dependencies, or call GitHub with write permissions.

The proposed patch:

1. Re-reads each otherwise-eligible candidate from `GET /branches/<quoted-ref>`; checks exact full SHA, explicit protection boolean and requested branch name against the initial listing. A moved or newly protected branch becomes `hold-ref-or-protection-moved-rerun`, retaining the **original** reported SHA. Missing or malformed detail fails the audit.
2. Re-reads the paginated set of open PRs and compares the strictly validated (PR number, ref, head repository) tuples. If the set changes, still-eligible candidates become `hold-open-pr-inventory-moved-rerun`. A duplicate PR number or missing head repository fails closed.
3. Validates a branch ref before constructing its detail URL and URL-escapes accepted branch names, preventing candidate metadata from injecting a request query.
4. Preserves the earlier documented base-movement hold, conservative ahead/behind rules and **read-only** behavior.

Six new deterministic, offline unit tests cover unchanged ref, moved/protected ref, newly opened PR, missing/malformed detail, untrusted branch names, and duplicate PR numbers. An existing base-drift test is extended to mock candidate rechecks.

## Residual risk and next steps

HTTP listing, branch re-read and PR re-read are **not an atomic GitHub snapshot**. A last-millisecond push or newly created PR can still race the final read. Consequently, neither `manual-prune-candidate` nor a successful test may trigger deletion. The separately restricted workflow tracked by [#277](https://github.com/MSKazemi/github-trending-1000-study/issues/277) must still do live protected-ref/PR review, verify original archive tags and Git `--force-with-lease` compare-and-delete, after required human security/administrator review. [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248) owns actual main/archive GitHub ruleset enforcement. [#279](https://github.com/MSKazemi/github-trending-1000-study/issues/279) remains open for full branch-by-branch no-loss reconciliation.

**Acceptance before this PR merges:** inspect diff and all affected cases; run exact-head Python 3.10/3.12/3.13/3.14 + research-artifacts GitHub Actions, obtain independent maintainer review and perform SHA-locked merge/post-merge main CI. This document records *proposed* behavior; it is not a claim of qualified review or final deployment.

## Practical lessons for maintainers

- SHA-pin both the *observation* and the final mutation lease. A Git SHA recorded earlier is not a lock on a moving branch name.
- Treat changes in PR membership or branch protection as safety signals, not inconveniences to silently ignore.
- Count *retained evidence and independently accepted improvements*, not issue closure, branch reduction or green synthetic tests, as research success.

## 2026-10-16 exact-head branch ancestry crosswalk (new, read-only)

A new [JSON checkpoint](2026-10-16-branch-ancestry-33refs.json) freezes **33** exact branch names and 40-character SHA values against inspected `main` `639054a0b98fe29c8bd0d6d72fb16b19fc26bff9`, with directly observed `protected=false`, **11** open PR branches (all held) and **21** other branches without an open PR. Branch-list SHA values were unchanged in the second read, but REST inventory is not atomic. Every one of these **21** non-PR branches returned GitHub `compare/main...<exact-head>` status `diverged`, with **ahead_by between 1 and 24** and **behind_by between 1 and 496**. None was `behind` or `identical`; **zero branches were classified as immediately ancestry-safe for deletion**, and no delete/merge was performed by the audit.

This shows why an operator must **not** select retirement candidates by PR closure, branch age or naming alone. An old branch can have divergent commit history even if the canonical implementation was incorporated via a squash/semantic replacement. The converse also holds: divergent commits do not necessarily contain still-unique, valuable changes. Check exact file SHA, original tests, provenance citations and negative outcomes, preserve them on current main or write-once archive tags, then obtain the #277 and #248 security/admin approvals. The JSON's `compare_file_count` is a Git history/file-change statistic, not a count of validated unique research artifacts.

The contemporaneous published API results here did not include a verified UTC clock time, HTTP response hash, or complete GitHub data-export replay. Accordingly this is a **dated operational checkpoint**, not a cryptographically frozen global GitHub transaction or external scientific evidence. New PR #417 itself adds one working branch and is held for real review.

**Owner-facing result:** prioritize file-level preservation for the 21 ahead/diverged branches; schedule genuinely independent code/security review of PR #417 and the separately drafted ruleset PR #302, not deletion of any of these 21 from an ancestry-only table.

## Bounded file-level no-loss spot check (2026-10-16)

To avoid confusing Git divergence with actual missing content, the following **five** branch-versus-current-main file pairs were fetched by explicit refs and compared by full file contents plus Git blob SHA. This is a *selected diagnostic check*, not a complete preservation audit of the 21 held divergent branches:

| Branch and path | Historical blob SHA | Main blob SHA | Equality / action |
|---|---|---|---|
| `audit/branch-merge-readiness-20261016`: `docs/reviews/2026-10-16-branch-merge-readiness.md` | `93ad9de61d74b52677b9568fab1fa9c7cde33881` | same | Exact file already on main; **not** overall branch retirement approval |
| `audit/pr-merge-gate-log-20261013`: `docs/PR_REVIEW_2026_10_13.md` | `d90c7b906aa85b33c0c1f7bbf6216e60d5a2295e` | `a11802ff43535c705e6fb1a7db2fe047a63f2091` | Different versions; inspect unique review evidence before archival |
| `chore/enterprise-pr-merge-guardrails-20261013`: `.github/pull_request_template.md` | `299a94d1bb5cd79b213721cb7cd275f836791b45` | `60d8103709d6e59366a07878b0580831a815acb2` | Different versions; current main has expanded template, but semantic/source equality not established |
| `ci/enterprise-pr-qa-gates-issue-240`: `docs/BRANCH_RECONCILIATION_2026_10_14.md` | `1486cf06d1eded32c7c22e7a36347c6f51610295` | `d36a5422ce5f346a7b456927167b18b5a5019319` | Different versions; retain historical audit rather than rewriting the original |
| `ci/enterprise-pr-qa-gates-issue-240`: `ops/branch-retirement/review-only-2026-10-14.json` | `bec93d96de57e02431966c36e7950a0bb40631f4` | same | Historical snapshot byte-identical on main; still no branch-level no-loss certification |

**What this adds:** two exact preserved file artifacts and three explicit nonidentical files requiring content/claim review. It is not evidence of the correctness of either version, identity of human reviewers, source rights or full retention of all commits. Do not discard source branches until every material file, changed test and cited source is reconciled and approved.

## Historical review addendum rescued without replacing canonical main

An additional [archived original review addendum](2026-10-16-preserved-2026-10-13-pr-merge-gate-addendum.md) retains the **7,590-character original 2026-10-13 PR merge-review section** from the exact historical branch `audit/pr-merge-gate-log-20261013` commit `2b460c8e15819afd54e62bed1d7334d0e6a78a8e`, source file blob `d90c7b906aa85b33c0c1f7bbf6216e60d5a2295e`. Directly reading `docs/PR_REVIEW_2026_10_13.md` from historical head versus current main showed that this section was not fully on main: original length 25,823 characters versus main length 18,840. The archive preserves the complete section with an added source/limitations header, *without changing original or canonical files*. Historical accounts may be AI-assisted and require verification; no new human-authenticated review is implied.

## 2026-10-16 complete namespace re-list safeguard

The read-only `audit` now additionally re-fetches the **whole paginated branch list** after candidate SHA/protection and open PR rechecks. It validates shape, 40-character SHAs, distinct branch rows and protection booleans, then compares name/SHA/protection tuples with the first listing. The report exposes `branch_inventory_stable_at_second_read`; any intervening branch addition, deletion, ref move or protection change causes still-advisory prune candidates to become `hold-branch-inventory-moved-rerun`. Malformed/duplicated refresh data aborts the run. Two synthetic regressions demonstrate a newly created branch and a duplicated refresh entry.

The second REST read remains non-atomic. It **cannot** replace an independently approved last-moment Git server lease, protected recovery tags or live administrator policy. In particular, the 33-ref 2026-10-16 JSON checkpoint above is historical and should never be replayed as a deletion allowlist.

## 2026-10-16 API repository-route validation follow-up

The read-only audit now explicitly refuses `.` and `..` **owner/repo path components** and non-string repository arguments before composing any GitHub API path. The previous broad lexical owner/repo expression could accept `../name` or `owner/..`, despite the existing strict base-branch and candidate-ref checks. A deterministic offline test uses an aborting fetch function to verify invalid owner/repo values cause zero network requests. This hardening does not permit deleting branches or substitute for an atomic GitHub ref lease, repository rulesets, or human approval.
