# Pull-request merge and scientific evidence gate

**Recorded:** 2026-10-13. **Status:** engineering review policy and operational checklist, **not** an assertion that all existing PRs received human review, that GitHub branch protection is configured, or that CI tests prove empirical validity. Related issue: [#242](https://github.com/MSKazemi/github-trending-1000-study/issues/242).

## Mandatory merge decision — always check the *final commit*

1. **Scope and preservation.** Identify one bounded issue; list changed files and overlaps with all open PRs. Compare existing interfaces/data structures before adding a second engine. Preserve useful distinct tests, data, citations and docs in a single versioned implementation or explicitly retain both as distinct contracts, with migration plan. Never silently delete or overwrite write-once observations or previous references.
2. **Correctness and safety.** Read the actual diff and changed files; test malformed, unknown, negative and malicious-input cases. Never treat self-declared URLs, model-written assertions, passing tests or package metadata as authenticated license/security/reviewer evidence. Preserve no-auto-install and no-untrusted-code execution guarantees. Treat user/privacy/credential handling as separate security gates.
3. **Independent scientific review.** A generated checklist or automated reviewer is not an independent human. For a changed study protocol, primary hypothesis, sampling frame, source validation, blinded labels, observational results, or security deployment policy, obtain the actual qualified human methodological/security signoff required by the relevant issue/PR. Mark this gate **pending** if not obtained, even when synthetic CI is green. Do not report predicted, uncollected or self-attested study outcomes as observations.
4. **Fresh CI.** Confirm that the final expected PR head SHA has a completed, successful **pull_request** GitHub Actions run, including all matrix jobs (Python 3.10/3.12) and required checks. A prior branch SHA's green CI or an empty Commit Status API response is insufficient. Where main has advanced, reconcile the branch and rerun integrated checks. No merge on failures, cancelled jobs, incomplete runs or unresolved conflicts.
5. **Review and permissions.** Check open conversations, Change Requests, license, security, privacy, data rights, method/protocol change and human reviewers' actual state. A user delegating engineering maintenance is not evidence of independent blind source reviewers. Respect draft status and branch protection rather than force-merging.
6. **Safe merge.** Re-fetch the PR and its current head. Merge with `expected_head_sha` and appropriate squash/merge method only when green and human gates are satisfied. If the repo is concurrently changing, refresh preflight instead of applying stale CI evidence. For same-file/same-schema PRs, stage an integration PR rather than replacing useful work.
7. **Verify post-merge.** Confirm the resulting main commit and the **push-triggered** CI on the integrated tree. If it fails, immediately triage/revert with a traceable correction; do not describe a merge as verified before the integrated test succeeds. Record SHA, workflow run, test versions and risks in the review log.

### Limits of CI coverage

As of the dated baseline, `.github/workflows/ci.yml` ran standard-library unit tests on Python 3.10 and 3.12. This change also compiles every tracked Python module under `trending_study/` and `tests/` so syntax errors in unimported modules are detected. **Not automatically covered:** end-to-end GitHub access or permissions, credentialed package/security scans, actual two-rater scientific adjudication, downstream integrations, supply-chain authenticity, controlled task outcomes, energy metering, DOI fact checks, or independent reproducibility. Those need appropriately designed separate gates.

### Scientific correctness checklist for research PRs

- Exact source, dated version, source author, canonical URL, source type, disclosure/conflict and a record of what was actually inspected
- Descriptive/vendor statement versus independent causal effect clearly labeled; no invented effect sizes, adoption denominators, kWh or 2027–2031 observations
- Reviewers' identities and independence never inferred from fields, self-written records or matching generated text
- Data preservation: immutable original captures, stable repository IDs, missingness and attrition, chronology, null/negative cases, source-to-claim links
- For any recommended reuse: task/license/version/provenance/security compatibility, full human maintenance burden and environmental system boundary stated
- Protocol amendments versioned, approved and distinguished from preregistered hypotheses

## 2026-10-13 integration risk inventory (snapshot, not live status)

| PR | Boundary and overlap | Engineering/research gate at review time |
|---|---|---|
| [#59](https://github.com/MSKazemi/github-trending-1000-study/pull/59) | News source corpus, 20 provisional articles; source claims and dates unindependently reviewed | Draft; offline validator rejects forged verification and malformed URLs, but genuine second source/fact review + discovery ledger remain pending |
| [#170](https://github.com/MSKazemi/github-trending-1000-study/pull/170) | Frozen 16 public-issue leads, source recheck, structural A/B/C screening | CI passed; no actual independent task gold labels or qualified human methods review established by the technical logs. Prior written blocker must not be represented as satisfied by CI |
| [#182](https://github.com/MSKazemi/github-trending-1000-study/pull/182) | Trending overlap/list stability | Structural offline QA, **not** actual GitHub page auditing or secret algorithm recovery |
| [#190](https://github.com/MSKazemi/github-trending-1000-study/pull/190) | Canonical page-audit optional C reviewer | Synthetic reviewer records and real independent blinded human reviews are distinct |
| [#208](https://github.com/MSKazemi/github-trending-1000-study/pull/208) | E0–E5 lesson evidence registry | Structural source/provenance guard, **not** independent validation of real study effects |
| [#186](https://github.com/MSKazemi/github-trending-1000-study/pull/186) and [#216](https://github.com/MSKazemi/github-trending-1000-study/pull/216) | Duplicate package-security gate proposals | #216 implements stronger PyPI/version/date review and regression tests; preserve #186's multi-candidate/PURL/source-commit features, but do not treat two self-declarations as independent security approval |
| [#183](https://github.com/MSKazemi/github-trending-1000-study/pull/183) and [#187](https://github.com/MSKazemi/github-trending-1000-study/pull/187) | Documentation rubric and agreement instrument | Need one compatible archetype/labels contract before certified scoring |
| [#185](https://github.com/MSKazemi/github-trending-1000-study/pull/185) and [#210](https://github.com/MSKazemi/github-trending-1000-study/pull/210) | Independent adoption definitions and missingness instrumentation | Align observation denominators, explicit unknown/unobservable and evidence-level labels; do not equate stars to use |
| Company intelligence PR series | Same six-month research program, company-specific sources | Cross-check duplicated announcements, original date vs updated date, competing claims and no invented roadmap promises |

**Operational note:** several PRs were merged by concurrent workflows during the audit. GitHub state can move while this document is edited. Each merge needs a fresh per-commit gate; this snapshot is not an approval list or authority to rewrite previously preserved data.

## Practical lessons for maintainers

1. Adopt **one clear implementation per public interface**, with versioned extension points; preserve distinctive evidence/tests during consolidation.
2. Require a *runnable independent acceptance task* and a negative/failure example rather than celebrating CI checkmarks or generated LOC alone.
3. Document reviewer and source provenance as rigorously as code provenance; labels written by an AI agent are not independent assessment.
4. Prefer measured cost per verified reused task to stars, PR volume or speculative token-to-carbon conversions.
5. Protect long-lived datasets with immutable raw artifacts, timestamped changes, full null/missingness accounting and explicit superseding links.

## CI implementation integration — 2026-10-13

The concurrent PR quality-policy drafts were reconciled into **this canonical gate**, not duplicated as a second normative policy. The dated [PR review checkpoint](PR_REVIEW_CHECKPOINT_2026_10_13.md) is an operational audit, not a competing policy.

- The official release Git tags `actions/checkout@v7.0.1` and `actions/setup-python@v7.0.0` were verified through the GitHub release/tag-ref APIs; CI executes their **immutable commit SHAs** `3d3c42e5aac5ba805825da76410c181273ba90b1` and `5fda3b95a4ea91299a34e894583c3862153e4b97`.
- Read-only `contents: read` permissions, no persisted checkout credentials, no dependency installs, a 15-minute timeout, and Python **3.10/3.12/3.14** source compilation/full standard-library tests/CLI smoke constitute the documented technical baseline.
- CI runs for **pull requests and pushes to main**; cancel only superseded PR revisions, never fast-following post-merge main pushes. The main integration run is a separate gate; an earlier successful PR run cannot substitute for it.
- The GitHub workflows/policy alone do **not** configure server-enforced branch protection or required independent human reviewers. Repo administrators should set required status checks and approval rules in GitHub repository settings.

### Preservation decision for competing quality PRs
A concurrent PR introduced this useful canonical [template](../.github/pull_request_template.md), which is retained and updated to the three-version matrix. The other PR's more stringent immutable-action configuration and an independently dated integration-risk report were carried forward here. We deliberately avoid two PR templates or two normative merge policy files; unique, useful text is retained in this addendum and the [audit checkpoint](PR_REVIEW_CHECKPOINT_2026_10_13.md).

### Preserved newer validation from concurrent main
The final CI retains the separate stricter JSON syntax/duplicate-key/nonstandard-number guard from another integration PR, and smoke tests the existing `trending_study`, `reuse_gate`, and `goldset` entrypoints. Those checks must **not** be dropped when action versions or Python matrices change. Real research-source integrity still needs independent verification beyond JSON syntax.
