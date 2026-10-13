# Pull request — evidence and merge readiness

> [Enterprise merge policy](../docs/PR_QUALITY_AND_MERGE_POLICY.md). Keep **Draft** until the author has met its acceptance criteria. Green CI alone is not approval to merge.

## Why this change is needed

Related issue: #
User-relevant task and expected behavior:
Best existing implementation/configuration/upstream alternative considered:
Why the proposed change is preferable:

## Scope, compatibility and rollback

Files/interfaces/schemas affected:
Migration or backwards-compatibility considerations:
Potentially overlapping PRs or data artifacts:
Rollback plan if the change fails after merging:

## Independent verification

- [ ] I read the current `AGENTS.md`, scientific methods, ethics and contributing rules.
- [ ] I reviewed the actual diff against the **latest** `main`; unrelated useful source material and research observations are preserved.
- [ ] New behavior has bounded acceptance/failure tests, including malformed/unknown inputs when relevant.
- [ ] `python -m unittest discover -s tests -v` passes on the exact PR head.
- [ ] CI Python versions, compilation and research-artifact checks passed on the **current head SHA**, with no pending/failed required checks.
- [ ] Documentation, instructions, data dictionary and reproducible examples reflect the change.
- [ ] No unapproved credential access, network capture, third-party code execution, or unsafe dependency installation was introduced.

## Research integrity and data rights

- Evidence type: [ ] synthetic only [ ] observed public metadata [ ] registered/consented experiment [ ] documentation/method hypothesis.
- Source URLs, publication *and event* dates, attribution, licensing, data rights and uncertainties verified or labeled pending.
- [ ] Synthetic fixtures are never presented as real participants, adoption, measured savings or model benchmarks.
- [ ] Unknown/missing observations remain unknown; primary denominator, original data, failures and negative findings are preserved.
- [ ] Private participant/agent traces, prompts, credentials and identifiable information are excluded from public artifacts.
- [ ] Any affected data-access, protocol, preregistration, sampling or experimental decisions have qualified **human** methods/ethics approval with a verifiable reference; otherwise the work is expressly provisional and cannot advance the study gate.
- [ ] Existing GitHub Trending capture **access stop** remains in effect; no bypass or backfill.
- [ ] Reused dependencies/solutions have exact-version provenance, compatible license, security and independent functional review.

## Merge decision (completed by authorized reviewer, not the PR author)

- [ ] Not a draft; no unresolved blocking reviews or conflicts.
- [ ] Evidence, tests and CI were checked against the immutable expected head SHA.
- [ ] All overlapping PRs inspected and useful sources/data reconciled without force-pushing or silent replacement.
- [ ] Human scientific signoff recorded where applicable; **automation or AI-only review cannot satisfy an independent reviewer requirement**.
- [ ] Merge is safe, scoped, reversible and does not misstate research readiness.

**What remains unvalidated:**  
**Exact CI run and head SHA:**  
**Reviewer and approval evidence (if required):**
