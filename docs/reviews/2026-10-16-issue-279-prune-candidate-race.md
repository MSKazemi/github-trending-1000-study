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
