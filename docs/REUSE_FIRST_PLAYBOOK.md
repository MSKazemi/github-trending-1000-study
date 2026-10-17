# Reuse before generation — practical protocol for Claude Code, Codex and humans

**Not an empirical finding:** a low-regret workflow to test; additional search can be wasteful, so cap the search budget and validate alternatives.

## Decision procedure
**Goal:** maximize independently verified user value per complete life-cycle cost, not the quantity of code written.

```
User problem + task acceptance tests
   |
   v
Existing code / package / prior work search (time-boxed)
   |
   +-- viable maintained, compatible, safe candidate? --> verify task --> reuse
   |                              |
   |                              +-- small unmet gap? --> propose upstream patch
   |
   +-- ambiguous candidates? --> test top feasible options, capture failure reasons
   |
   +-- none passes / license conflict / unacceptable risk?
                                  --> smallest custom implementation
   |
   v
Review + tests + docs + reuse instructions + independent user proof
   |
   v
30/90-day cost, security and repeat-use assessment
```

## Before a coding agent writes new code
- Record exactly what a real user must achieve, in what environment, and how an independent reviewer checks success.
- Ask: 'Which existing repo/library/package already does this?' Search official dependencies/packages, existing code in this repo, plugins, documentation and public GitHub. Record search date/terms and credible links.
- For each top candidate: exact version, license compatibility, security disclosures, support/maintenance, API stability, installation, transitive dependencies, tests, data/privacy requirements, integration cost. **Unknown != pass**.
- Evaluate **reusing an existing tool**, **submitting upstream improvements**, **composing two compatible components**, **forking with obligations**, or **writing fresh code**. Prefer the lowest-risk outcome satisfying a frozen acceptance suite; avoid a universal stars or dependency-count ranking.
- Define stop rules for searching; unlimited search itself can waste human and agent tokens.
- Do not copy from a public repo unless the license permits it and attribution requirements are met. A visible source file is not automatically open-source-licensed.
- For high-risk applications, require threat modeling and human approval. Consider using stable audited code instead of an unreviewed dependency.
- After shipping, make your own component reusable: clear problem and task example, install/compatibility/version matrix, test command, machine-readable license, API docs, minimal example, upstream contribution/feedback path, SECURITY and maintenance expectation.

## Bounded agent prompt
> You are implementing one precisely defined user task. Read AGENTS.md, the task acceptance tests, existing local code and reusable packages BEFORE generating new source files. In a short evidence table list up to five candidate libraries/repos with version, verified license, security/maintenance status, task fit and links. First propose reuse, configuration or an upstream contribution; only recommend new code if a testable gap remains. Time-box discovery to the task's declared budget. Do not install untrusted dependencies, copy restricted code or execute third-party scripts without authorization. Produce the smallest tested patch; update docs so another developer can reuse it. Report human time, agent calls/tokens when available, failed attempts and remaining risks. Do not invent energy or CO2 figures.

## After implementation: what counts as useful?
Independent clean install + relevant task pass, security controls appropriate to risk, documented reuse/compatibility and a credible maintainer plan. Genuine external reuse (verified dependent integration, success reports or a reproducible research artifact) adds evidence. **Stars, forks, commits and agent PR counts do not prove this.**

## Failure patterns
- 'It's on Trending' → treat as discovery lead, never eligibility/quality guarantee.
- 'This other repo has many stars' → inspect functionality, maintenance, license and dependency risks.
- 'The AI already wrote it' → sunk tokens don't justify keeping redundant code. Compare replacement cost and maintainability.
- 'Copying = reuse' → may propagate license/security/maintenance debt; dependency or upstream collaboration may be better.
- 'The new implementation is smaller' → smaller code is not necessarily lower lifecycle energy or better user task outcome.
- 'This avoids 1M tokens so it saves X CO2' → not without provider/measurement model, location, workload and boundary.

**Documentation:** [experiment](REUSE_FIRST_EXPERIMENT.md) · [metrics](REUSE_SUSTAINABILITY_METRICS.md) · [green science standard](../references/green_reuse_sources_2026.json) · [project decision guide](DEVELOPER_DECISION_PLAYBOOK.md).

## 2026-10-18 offline reuse-assessment input-integrity fix (#458)

The CLI `python -m trending_study.reuse_gate --input examples/reuse_check.example.json` now uses the repository's canonical **strict, descriptor-checked and 16 MiB-bounded** research JSON reader. Repeated JSON keys, including duplicate `functional_test` or `license_compatibility` labels, must never silently replace an earlier failed/unknown result. Nonstandard and overflowing/underflowing numeric literals, symlinks, directories and oversized input are rejected; input/OS failures use path-neutral diagnostics. The existing fictional example's decision is unchanged. Tests run the **actual CLI**, not just the in-memory evaluator.

**Limit:** This verifies input structure and error safety only; the evaluator still describes *self-reported* evidence rather than independently authenticated licenses, security advisories, candidate provenance or task success. No package was downloaded, installed or tested against third-party systems. The parent [package review tracker #22](https://github.com/MSKazemi/github-trending-1000-study/issues/22) remains open.

**Practical lesson:** guard untrusted assessment bytes before generating any reuse recommendation. A convenient JSON parser that silently takes the last duplicate key can turn a declared failed gate into a claimed passing gate.
