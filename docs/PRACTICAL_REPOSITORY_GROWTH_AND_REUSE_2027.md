# Practical maintainer handbook: high-quality, reusable and discoverable GitHub repositories

**2026-10-12 | Status:** actionable engineering *hypotheses and baseline hygiene*, not experimentally established "growth tricks". See [mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md) and [evidence-to-lesson gate](EVIDENCE_TO_LESSON_PROTOCOL.md). Verify each project's outcomes before adopting advice broadly.

## Which success do we mean?

For each project independently specify: **persona, repeatable job/task, validated completion, cost/risk baseline, reuse unit, and intended adoption channel.** An academic dataset, an infrastructure library, a CLI and a training example have different valid endpoints. A project with few users can be valuable; a high-star repository can remain unusable.

## Practical repository audit — priority order

| Priority | What maintainer implements | Proof of function / outcome | Caution |
|---|---|---|---|
| P0 | Write a one-sentence target user and problem, link the nearest existing alternatives | External user can explain why this is needed and why the alternatives fall short | Not every original project needs broad appeal |
| P0 | Search registry/GitHub/prior art and compare integrate, extend, upstream patch, compose, build, or no-build | Timestamped candidate and task-fit/license/security decision | Search miss cannot prove nonexistence |
| P0 | Publish clear name, precise description, truthful capability/limit statement and accessible license | External visitor identifies scope and legal obligations; license reviewed | SEO keywords don't prove discoverability or rights |
| P0 | Provide clean environment quickstart, 5-minute runnable example, one meaningful end-to-end test/demo | Uncoached non-maintainer attempts task; report successes and failures over all attempts | "5 minutes" is an illustrative target, not observed universal threshold |
| P0 | Pin supported versions; test clean installation, core functions, failures and security-sensitive behavior | CI result and independent test against frozen requirements | Passing tests don't certify safety |
| P1 | Provide stable versioned interfaces, API/reference docs, migration/deprecation notes and reproducible releases | Second independent downstream consumer upgrades without undocumented work | Extra abstractions can make simple tools worse |
| P1 | Supply CONTRIBUTING, bounded good-first issues, triage policy, CODE_OF_CONDUCT and SECURITY route where applicable | Newcomer can complete bounded accepted contribution; measure review and rework minutes | More PRs alone are not better |
| P1 | Document citation, provenance, examples for research vs production and fair upstream credit | Independent researcher reproduces use; downstream use is linked | Require explicit permission for private deployment telemetry |
| P1 | Publish illustrative benchmarks and architecture tradeoffs with fixed environment and workload | Third party reproduces test and understands when NOT to use the code | Never fabricate cost/energy figures |
| P2 | Explain value through tutorials, relevant technical discussions, talks, release notes and appropriately scoped comparisons | Verifiable qualified inbound issue/task/user, actual downstream usage where observable | No purchased stars, engagement exchanges or spam |
| P2 | Record adoption, regressions, issue response and development/maintenance burden across 30/90/180 days | Dated consistent denominators and cohort-matched trends | Repo traffic cannot be fetched for arbitrary third-party projects |

**Priority indicates practical sequencing, not an empirically fitted ranking.** A safety-critical project may need considerably more testing and audit than shown.

## Minimum release gate

1. A fixed user task and accepted behavior exist; an independent tester actually tried it.
2. Another tool/package was evaluated first; its license, security and dependency risks were considered.
3. A fresh environment executes the documented first-run path; errors and unsupported platforms are disclosed.
4. Tests cover accepted behavior and failure cases; high-risk changes receive expert review.
5. Documentation, packaging and version history match the tested release.
6. A support/security path, contributor entry point and maintainership expectations are stated.
7. Attribution and use rights for reused code are verified.
8. Claims about users, energy, savings and growth link to evidence, otherwise say "not measured".

## Researcher and company reuse readiness

A **researcher** needs: pinned environment, dataset/model/code provenance, runnable reproduction, license/citation, known methodological limitations and a baseline. A **company** needs: supported interfaces, security/contact disclosure, version/release compatibility, dependency and license assessment, operational failure mode, maintenance policy and examples. Neither actor should need to contact the author to complete the first representative task.

## Portfolio-level rule

Maintain a portfolio decision table per repository with: intended user/task, overlapping alternatives (including maintainer's own), reproducible proof, actual independent integrations, cost of continued maintenance, security risk and candidate consolidation. Choose *merge modules / maintain separate / contribute upstream / archive / re-scope* by measured interoperability and value—not by repository-count vanity. Run a documented review at least each quarter when feasible.

## Ethical 2027 evidence gathering

- **Observation study:** show which baseline practices precede future attention, but avoid causal language.
- **Intervention study:** optional opt-in staged README/quickstart/API/contributor-guide changes, fixed outcome definition beforehand, comparison windows and independent test participants. Measure first-run success, qualified external adoption, time-to-first-accepted contribution, and human review burden, not just stars.
- **Agent study:** preassign tasks, freeze acceptance tests, compare conventional coding and reuse-first with precise tool versions; inspect negative outcomes and total cost.
- **Green:** report kWh/CO2 only with legitimate boundary and uncertainty. Provider-side inference opacity usually prevents an exact full-lifecycle result.

## Standard work contract for Codex / Claude Code

> Read AGENTS.md, README.md, CONTRIBUTING.md and the relevant design documents. Choose one bounded, user-validated task. Before implementing, inspect existing code and evaluate safe compatible public alternatives. State why reuse, configuration, upstream contribution, minimal patch or new code is preferable. Freeze acceptance criteria independent of generated solution. Implement the smallest traceable change with tests, compatibility/security checks, docs and honest provenance. Run the full available suite, report untested areas and exact human/token/CI costs if observed. Do not claim adoption, energy savings or popularity without independent evidence. Deliver one focused PR.

## How a scientific result becomes advice

Use the project's E0–E5 evidence-to-lesson protocol. For every claim specify evidence, population, eligible denominators, point/time estimate, uncertainty, confounders, cost, potential harm, applicability, reproducible experiment, and the observation that would refute it. Keep a **test-it-on-my-repository** step with a 30/90-day outcome and a rollback trigger. A null result means do not promote a generic tactic.

**Start small now:** the most immediately useful audit is *one true first-run user test, one pre-code search/compare, one pinned runnable demo, and one concrete external-reuse target per repository*. Those are testable actions, not quantified promises of growth or energy savings.
