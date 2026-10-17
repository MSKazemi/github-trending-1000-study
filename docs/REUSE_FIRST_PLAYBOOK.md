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


### 2026-10-18 full-traceback privacy regression

Input-parser and evaluator failures now produce `SystemExit` **after** the original exception handlers end, preserving the canonical strict bounded reader while keeping full tracebacks free of private source path/key and evaluator exception chains. New direct in-process tests verify `__cause__`, `__context__` and formatted exception stacks, not only subprocess stderr. Synthetic tests do not authenticate external licenses, source identity, safe dependency installation, or real research outcomes. Keep issue #22 open.

## 2026-10-18 reusable candidate identity and status hardening (#461)

The offline reuse gate now rejects multiple candidates with the same **trimmed, case-insensitive display name**. Before this change, `failed_gates` was a name-keyed mapping and a duplicate could overwrite or contradict another candidate's negative review result. If two versions of a package must be compared, give them **distinct explicit names including versions**, and record both results; name collisions do not establish which candidate is correct. The CLI rejects arbitrary candidate fields, unhashable state objects (list/dict), and more than 100 candidate entries. Candidate name and URL strings are bounded and cannot contain control characters. The original synthetic valid example retains its decision; status labels remain `verified/failed/unknown` but are still **self-reported**, not authenticated evidence.

No package resolution, third-party code execution, license verification, source rights or user-study data was introduced. Broader supply-chain approval remains blocked under [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22).

**Practical lesson:** a key used to summarize review results must be unique, and malformed nested fields must produce controlled refusal—not a traceback or silently overwritten failures.
