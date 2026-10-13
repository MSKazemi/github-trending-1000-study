# Task-first OSS search comparison — pre-pilot design (#19)

**2026-10-13 status:** methodological pilot specification only; **no search engine, independent gold pool, real retrieval measurements, cohort, license/security certification, or empirical results** have been established.

## Research question and falsification

For prospectively sampled, time-stamped tasks, does a time/budget-limited reuse-first **hybrid** source search find *more independently verified usable, legally compatible, safe-enough components* than lexical-only source search at a given search cost? The null/negative outcomes (including no usable candidate, unknown pool coverage, longer search time and installation failure) must be preserved. This is a testable comparison, not a claim that semantic search is inherently better.

## Reuse-first decision

The repo already provides \`trending_study.goldset.evaluate\` and [its documented validator](GOLDSET_VALIDATION_CLI.md), as well as [independent gold-label requirements](REUSE_GOLD_STANDARD_2027.md). **Reuse the current tool for scored system rankings**; do not create a parallel search-accuracy metric or new parser. Actual retrieval is deferred to an access-policy-reviewed, resource-bounded pilot. [Synthetic example](../examples/goldset.synthetic.json) compares two named rank lists but is not empirical proof.

## Predeclare a valid comparison

1. **Freeze independent task frame**: tasks obtained without looking at candidate retrieval or feasibility results; include no-known-solution, educational, unpopular, historical and specialized tasks, with source frame, language/ecosystem, task cutoff UTC, task-spec SHA-256, and independently written acceptance-suite SHA-256. Keep all tasks and prespecified exclusions in the denominator.
2. **Freeze three alternatives**: (L) bounded lexical search across repository/package metadata and docs; (S) bounded embedding search using the same admissible corpus snapshot; (H) hybrid lexical+semantic fusion with an **explicitly fixed** fusion rule and any weights chosen on disjoint development tasks. Include (B) no-search/default build as a workflow comparator in a distinct randomized task trial, **not** a retrieval ranker.
3. **Comparable corpus**: identical access-date and licensing provenance window for L/S/H. List registries, GitHub public metadata, local code and archival coverage; report index construction/amortization, stale/deleted packages, paid/API limitations and exact retrieval version. Filter candidates published after the task's baseline. A system's failure to retrieve does not demonstrate absence of a solution.
4. **Budgets and blinding**: preregister candidate inspection K (for instance 5), wall/human-active search limits, tokens/tool-calls where actually observed, max source requests, and stopping logic. Randomize query/system presentation to independent human raters; redact system labels from candidate judgments where possible and keep a leakage/conflict log. A deterministic CLI's 'raw agreement' is **not** independent verification.
5. **Pool assembly**: union top-K from all searchers; add a separate deeper/rand-audit sample (with documented probability and ecosystem coverage) to address pool incompleteness. Independently verify **exact version and availability at task cutoff**, functional fit using frozen acceptance tests, license/obligations, package identity/security, maintenance burden; unresolved gates → **unknown**, not zero. Never install arbitrary packages during evaluation in a privileged environment.
6. **Outcome metric**: for each system/task, use current goldset's precision@K bounds, judged coverage, observed pooled-relative recall (not global recall), and raw agreement. Record functional integration success, failed/abandoned/refused/no-candidate tasks, search time, validation time, reviewer burden, and post-use maintenance separately. No trade-off score should hide a hard safety/license failure.
7. **Analysis**: paired within-task system comparisons with task-cluster bootstrap intervals or an explicitly stated paired permutation test. Estimate relative improvements in independently validated task success and cost, not code volume. Report effect estimates **with 95% uncertainty intervals**, paired missingness, N/tasks, archetype/language/time strata and sensitivity to unknown judgments. Registered primary and secondary metrics and multiple-comparison policy must be fixed before reading outcomes. An underpowered or contaminated pilot remains exploratory.
8. **Stop and interpretation**: halt a retrieval source if platform permissions, credential exposure, dangerous package execution, or uncontrolled cost become material. Negative results and nonviable retrievals remain visible. Code search or similarity cannot establish adoption or reduced electricity; environmental attribution belongs to [issue #23](FULL_LIFECYCLE_BREAK_EVEN_2027.md).

## Reproducible synthetic smoke check

    python -m trending_study.goldset --input examples/goldset.synthetic.json --k 2
    python -m unittest discover -s tests -v

Expected: the synthetic lexical rank list has one viable and one audited failing top-2 candidate; the synthetic semantic list has an unjudged item and therefore **no single precision@2 or pooled-recall point estimate**. Its known-good precision lower bound is 0.5 and upper bound is 1.0. This arithmetic does not compare actual retrievers: the rank lists and all labels are invented fixtures.

## Independent pilot acceptance / not-yet-done

- Obtain signed scientific owner approval and task/label blind reviewer independence before prospective enrollment.
- Capture reproducible full candidate source snapshots, exact date/version/license and predeclared retrieval configuration with controlled budgets.
- Test on genuinely held-out user tasks with independently authored acceptance and opt-in human review; include tasks with no solution or unresolved evidence.
- Publish paired all-task uncertainty, missingness, source-coverage limitations, acceptance, search/validation cost, and adverse outcomes; amend protocol prospectively if infeasible.

## Practical lesson for maintainers

For one real incoming issue, write the externally checkable acceptance test **before** asking an agent to generate code. Time-box a local-code and package search, verify one exact-version candidate against license/security/functionality, and document whether reusing or adapting it met the task. If no source meets the checks, build the smallest compatible implementation. Do not call the repository 'more reusable' until an independent new user actually integrates and succeeds.
