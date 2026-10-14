# Documentation-quality evaluation: bounded pilot rubric (issue #5)

**2026-10-12. Status: proposed instrument; ZERO independently scored repositories.**
This is not a 100-repository validation, a tested psychometric scale or a claim that documentation causes popularity.

## Stratified applicability
| Archetype | Mandatory first-use evaluation | Inapplicable example |
|---|---|---|
| Library/SDK | install, import, run an API example, identify version | web deployment |
| CLI | install or portable binary, help, real input/output, exit codes | notebook rendering |
| Service/API | local safe startup, sample request, data and auth prerequisites | reusable Python import |
| Research software/model | reproducible environment, input dataset rights, rerunnable example, expected tolerances | production SLA |
| Template/agent skill | scaffold or invoke a bounded task, inspect emitted code and license | download metrics |
| Documentation-only | find a specific answer, follow a maintained canonical reference | executable setup |

## Rater worksheet and anchors (proposed)
Two independent human raters, **blinded to stars, Trending rank and each other's labels**, use a clean environment and frozen end-user task.
Record `repo_id`, commit SHA, UTC, archetype, predefined task, environment, reviewer pseudonym, evidence path, minutes, failure reason and each dimension. Do not publish names, prompts, login credentials or private user files.

For every **applicable** dimension rate 0 = task cannot be completed / requirement absent; 1 = possible with nontrivial undocumented correction or outside assistance; 2 = completed unaided using repository instructions. Use `NA` only with a documented inapplicability reason, and `unknown` when untested. Dimensions:
1. Clean installation and dependency/version reproducibility.
2. A task-relevant, runnable quickstart with expected results.
3. Clear public API/CLI contract and error recovery instructions.
4. Required input/test data and legal access conditions.
5. Contributor setup, tests and meaningful issue/PR workflow.
6. Security, supported versions and disclosure/update instructions.
7. Accessibility for target user, troubleshooting, and maintenance of links.

Primary outcome **is not sum of arbitrary scores**: independently accepted first-use task success / all consented attempts, stratified by archetype. Secondary: per-dimension 0/1/2 distribution with NA/unknown denominators, time, help requests and critical failures. Do not assign scores when the reviewer never attempted the task.

## Agreement, adjudication and selection
Freeze sampling stratum and random seed *before* viewing docs; include old, low-star, non-Trending components. To meet the issue's requested 100+ sample, predeclare sampling frame, exclusion log, archetype quotas and distinct stable repository IDs. Sample remains **uncollected**.
Before discussion, report raw exact agreement and pairwise Cohen kappa for each ordinal dimension using mutually applicable paired ratings. Explicitly report n, marginal distributions and prevalence sensitivity; quadratic weighted kappa may supplement but not replace exact agreement. Compute task-pass agreement separately. Never calculate kappa from NA/unknown treated as 0. If both raters always choose one category, kappa denominator can be zero: report undefined rather than perfect agreement. An independent adjudicator receives discordant evidence and records a decision plus rationale and review date, preserving both raw labels.

## Practical repository experiment
For a current maintainer repo, freeze a 10-minute clean-install task, recruit consenting unaffiliated first-time users and record attempts/failures. Fix only independently observed onboarding blockers, rerun under the same task standard, and preserve negative results. A higher star count is not an acceptance criterion.

**Next gates:** implement machine-readable rater entry/validator, collect consent, pilot agreement on heterogeneous projects, calibrate anchors, then evaluate 100+ actual repositories. Human methods signoff is required; no evidence claim is allowed from this template alone.

## Integration boundary: task-success versus nominal agreement

The proposed **ordinal 0/1/2 dimension ratings** require an explicit, separately reviewed agreement method (including any weighted kappa and treatment of true `NA`). The companion [nominal rubric-agreement instrument](RUBRIC_AGREEMENT_INSTRUMENT_2026_10.md) accepts only `pass`, `fail`, `not_applicable`, and `unknown`; its unweighted Cohen kappa **must not** be presented as agreement on this ordinal scale. Use the nominal tool only for a separately prespecified binary task-pass or nominal checklist judgment. Neither instrument provides independent human labels or the issue's requested 100+ repository evaluation. Keep review and registration gates open after documentation integration.
