# Dated research milestone: blinded task-to-component judgment tooling

**Date:** 2026-10-12. **Status:** proposed, synthetic-only, pending independent review.

## Motivation and scope
The research objective remains reducing unnecessary regeneration of code by humans and AI agents when good reusable implementations are available, without assuming reuse is always cheaper, safer or greener. Observed Trending appearances are an attention measure; they cannot establish verified code reuse or causal environmental benefit. User requested continuation of the task-first real-world assessment, building on existing issue #21 and the earlier unmerged issue-intake PR #38.

## What is now implemented in the proposed branch
- New standalone, stdlib-only blinded packet preparation and reviewer-submission audit (`trending_study/blind_review.py`) for frozen task hashes and candidate provenance.
- Strict reviewer A/B source separation at the *data-file* level, with optional C adjudication only on disagreements; blind packets omit run names, channels and ranks.
- Conservative unknown handling for missing second reviews and unresolved disagreements, evidence-reference requirement per passing/failing gate, time-indexed availability and pool fingerprint guard.
- CSV-free structured JSON export conforming to the existing gold-set validator (`goldset_input`), with raw agreement and nominal Cohen's kappa computed for paired synthetic labels.
- Synthetic-only task, evidence and review fixtures; offline regression tests. No real individuals supplied ratings or task success evidence.

## Reuse-first code decision
Instead of introducing external database, agent platform, code-search crawler, model API or IR metric library, this change **reuses the existing goldset evaluator** and Python standard library. Implementation writes no automatic GitHub comments or PRs to third-party maintainers. The review system measures no electrical consumption; do not infer energy savings from code size or reduced dependency count.

## Scientific blockers not solved here
1. The real 6-issue intake frame in PR #38 is *unreviewed*, not six independently frozen tasks; PR #38 also awaits methodological review.
2. Two independent humans, adjudication and hidden acceptance tests are not provided by a code validator.
3. External source metadata and license/security/maintenance claims are self-reported; trust requires independently archived evidence and isolated functional testing.
4. Sample representativeness, source coverage, preregistration, human consent/ethics, power and environmental measurement are not addressed by these synthetic fixtures.
5. Empirical findings, percentages of reusable tasks, time savings, verified contributors, carbon savings and any implications for 2027 are **not available**.

## Next human research gate
After approval of the instrument and task-intake frame, choose a small prospective task subset independent of reuse opportunity, freeze acceptance suites/versions with SHA-256, commission two appropriately blinded reviewers and a third when required, create an evidence registry, and perform authorized isolated functional checks. Pilot-review coverage, disagreements and failures must be reported before scaling to hundreds or thousands of cases.
