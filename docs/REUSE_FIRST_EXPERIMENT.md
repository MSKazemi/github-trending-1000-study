# Falsifiable 2027 experiment: reuse-first versus generate-first development

**Status:** protocol candidate; not running, no participants, no results. Designed to test whether searching for verified existing code *before* generating new code reduces net effort, environmental burden and technical debt without sacrificing verified user utility.

## Units and enrollment
Recruit opt-in developers, with consented task/time logs; freeze developer experience, codebase familiarity, new-vs-mature task status and task-specific acceptance tests **before assignment**. Sample real bounded tasks from community requests, issue backlogs, developer workflows; include tasks with independently adjudicated reuse opportunities and tasks without them. Predeclare privacy boundaries and avoid sensitive domains in pilot. Pilot determines N and statistical power; no fixed N claims.

## Randomized 2×2 design (proposed)
| | Baseline search/workflow | Mandatory documented reuse-first |
|---|---|---|
| No coding agent allowed | A: manual normal development | B: human reuse-first |
| Coding agent allowed | C: agent normal workflow | D: agent reuse-first |

**All four arms may use standard package registries and must obey the same safety/ethics requirements**; the intervention changes the *sequence and evidence requirement*, not whether security checks exist. Baseline arms are not forbidden from natural reuse. Keep software/agents, model versions, prompts, budgets and permitted search affordances as similar as practical and document changes.

Block randomization by developer experience, language, task type (CLI, library, application, research) and estimated difficulty; plan independent task-reviewers blinded to workflow where feasible. Prevent cross-task answer leakage with unique but functionally comparable tasks or cluster/counterbalanced assignment. Consider developer fatigue, learning and hidden prior exposure.

## Reuse-first treatment
1. Requirements and fixed acceptance suite, scope/risk constraints, baseline expected outcome.
2. Before any generation, search local dependency graph + public package registries + repository/source docs + function/task-level candidate search where legally allowed.
3. Record top N candidates with date, exact version, evidence link and why applicable/not applicable.
4. Review real install/run behavior, license, dependencies, security advisories, active support and maintainers.
5. Choose from **reuse as-is**, **configure/compose**, **contribute extension upstream**, **fork with attribution and update plan**, **new bounded implementation**; no automatic dependence on high stars.
6. Run same acceptance tests, independent safety review, clean reproduction, and follow-up at +30/+90.
7. Log all attempt outcomes, human effort, agent calls/tokens, CI and device energy where measured, maintenance.

## Outcomes
**Primary feasibility endpoint:** independently accepted useful tasks per all human-active hours (intention-to-treat, including failed/abandoned attempts). **Co-primary/secondary safety guardrail:** accepted-task failure and severity. Environmental endpoint only **confirmatory** when measurement boundaries/calibrations are sufficient, otherwise exploratory with ranges. Additional metrics: search precision@5, true reusable candidate found, dependency risks, duplicated work avoided after independent counterfactual, total tokens, device kWh and 30/90-day repair hours.

## Algorithms to evaluate
- **Lexical search:** BM25 and structured GitHub/package-ecosystem queries over task description/README/API symbols.
- **Semantic retrieval:** embeddings and nearest-neighbor task/code search; report top-K and model/version and indexing costs.
- **Hybrid ranking:** lexicographic feasibility filters first (license/safety), then relevance/functional evidence, maintenance and integration effort. Avoid an opaque single score when criteria are uncertain.
- **Functional verification:** run candidate in a controlled, clean sandbox against fixed acceptance/negative tests; report false positives (similar words, wrong API) and false negatives.
- **Clone checks:** token-based SourcererCC or modern comparable tools on bounded legal/public data; benchmark Type-1/2/3 detection and **separate** functional-equivalence annotation. Do not claim a clone is an unnecessary project.
- **Study models:** preregister mixed effects/cluster-robust comparisons, intention-to-treat, selected factorial interaction and adjustment for task/user effects. Report medians, uncertainty, attrition and negative outcomes.

## Confounders and pitfalls
- "Agent" is a bundle of model and tooling; commercial versions change monthly. Pin tested versions, date and environment.
- No-agent vs agent may involve volunteer refusal: analyze intention-to-treat, deviations and volunteer generalizability.
- A strict reuse gate might increase up-front searching while *reducing* maintenance or vice versa; whole-life measurement is essential.
- More dependencies can degrade security, installability, offline support and environmental runtime; never mandate reuse when unfit.
- Generating a completely new helpful API may be superior to stitching incompatible packages; study must allow such results.
- Search and embedding index construction have their own energy and ongoing infrastructure costs. Attribute amortization explicitly.
- Energy measurement for external model services can be inaccessible; report separately measured developer-device kWh and estimated server energy, with honest intervals.
- AI benchmark-like public tasks may already occur in model training context; use previously unpublished task variants and report contamination risk.

## Decisions and deliverables
Freeze registered tasks/metrics and definitions. Include code and raw measurement provenance where privacy/platform permission permits; independent evaluator adjudication, clean reproduction, qualitative interviews on *why* reuse failed/succeeded, and an evidence-graded lesson card. Publish valuable failures and null findings.

Resources: [metrics](REUSE_SUSTAINABILITY_METRICS.md), [green mission](GREEN_REUSE_MISSION_2027.md), [reuse-first playbook](REUSE_FIRST_PLAYBOOK.md), [source registry](../references/green_reuse_sources_2026.json).


## Scientific correction: avoid an outcome-selected reuse-positive cohort (2026-10-11 amendment)

The main analysis must include **all prospectively sampled and randomized tasks**, whether a viable existing component was found or not. Otherwise the study would be biased in favor of reuse by choosing only tasks on which it was possible. Eligibility for a secondary reuse-opportunity subgroup must be judged by independent assessors **before intervention outcome**.

The gold set must be created independently of the agent under study and include old, small and non-GitHub components where legally available. Pair a time-stamped task with components available at that time, assess independent functional tests, license, security and maintenance, and label unresolved opportunities unknown (not 'none exist'). Use a [pooled judged candidate protocol](REUSE_GOLD_STANDARD_2027.md) and [supply-chain validation](SUPPLY_CHAIN_PROVENANCE_2027.md).

Prevent hidden leakage from historical public PR patches and agent-accessible answer pages; include new held-out tasks, identical functional requirements across workflows, and independent tests for correctness/security. The intervention itself consumes retrieval/index compute and can shift support work to upstream maintainers; capture these in the lifecycle [break-even and externalities](FULL_LIFECYCLE_BREAK_EVEN_2027.md).
