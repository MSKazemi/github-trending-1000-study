# Documentation quality rubric agreement instrument (issue #5)

**2026-10-12; status:** offline method/tooling, no observed repository labels, no consenting raters and no 100+ repository audit. This is a bounded contribution to [#5](https://github.com/MSKazemi/github-trending-1000-study/issues/5), **not issue completion**.

## Run and input

```bash
python -m trending_study.rubric_agreement --input YOUR_ANNOTATIONS.json
python -m unittest discover -s tests -p 'test_rubric_agreement.py' -v
```

Minimal **synthetic illustration** (not a real dataset):

```json
{
  "rater_a": "blind_A", "rater_b": "blind_B",
  "records": [
    {"item_id": "fictional-1", "project_type": "cli", "criterion": "first_run",
     "rating_a": "pass", "rating_b": "fail"},
    {"item_id": "fictional-2", "project_type": "library", "criterion": "import_example",
     "rating_a": "unknown", "rating_b": "pass"}
  ]
}
```

Ratings are `pass`, `fail`, `not_applicable` and `unknown`. Unknown labels are excluded from the Cohen kappa denominator **and separately counted**; `not_applicable` is an explicit rated category and asymmetric N/A is a disagreement. The instrument calculates chance-corrected Cohen kappa on paired labels (not weighted). A single-category panel has undefined kappa (JSON null), not kappa=1. Per-criterion and per-project-type analysis should be separately preregistered; pooling across heterogeneous criteria is at best a diagnostic.

## Real auditing prerequisites (not performed)

- Predefine type-specific items: CLI first run and help, Python library import/example, research artifact reproduction and deployed app access; record `not_applicable` rather than treating unavailable features as failures.
- Lock a transparent, independently sampled 100+ repository audit frame and time window; train two **actually independent** reviewers without access to one another's ratings or parser outputs.
- For each repository, freeze commit SHA, docs URL, exact criterion, reviewer/time, timed clean-room task, outcome and uncertainty; do not collect author-sensitive data.
- Publish per-stratum paired coverage, unknown/N/A counts, agreement, disagreement adjudication and uncertainty intervals. Compute kappa only where estimable; report prevalence/skew.
- Obtain signed human screening, use real source refs, and independently reproduce at least a subset of first-run tasks before drawing quality conclusions.

**Practical lesson for own repositories:** pilot a task-specific first-run rubric on two README versions; evaluate independently accepted setup before claiming longer docs or AI-generated docs improve usefulness. Neither stars nor raw kappa establishes downstream adoption.

**Validity:** this program verifies supplied label arithmetic only; IDs cannot prove real independent people or unbiased sampling. Any true study result needs ethics/consent, provenance and review specified in [study design](STUDY_DESIGN.md).

## 2026-10-13 scientific hardening: stratification, missingness, and interpretation

Change: `rubric_agreement.evaluate()` now reports marginal counts and complete-case nominal Cohen κ separately by **project archetype**, the number excluded because either reviewer marked `unknown`, and the unmodified overall calculation. A stratum with fewer than two jointly rated items reports `null` κ, never pseudo-precision. Case-only reviewer ID aliases are rejected; this remains a **structural** independence check only.

**Review design:** freeze an archetype-specific rubric, versioned criteria and at least 100 prospectively selected eligible repository/task units before observing agreement; recruit two real independently working and blinded human raters, using identical written instructions. Count failed/not-applicable labels explicitly; adjudicate disagreement separately rather than rewriting original A/B ratings. Randomize presentation and keep an auditable ordered assessment ledger. Do not use selected examples as a sampling prevalence estimate.

**Estimation:** report per-archetype N, complete-pair N, missing-pair fraction, confusion matrix/marginal class frequencies, observed agreement, unweighted κ and its uncertainty once a real prospective design exists. Kappa depends on class prevalence and reviewer bias; never compare κ in isolation or collapse N/A into failure. A code-generated κ does not authenticate reviewers, sampling or validity.

**Sources:** [Cohen (1960), A coefficient of agreement for nominal scales](https://doi.org/10.1177/001316446002000104); [Byrt, Bishop & Carlin (1993), Bias, prevalence and kappa](https://doi.org/10.1016/0895-4356(93)90018-V). These justify the agreement measure and interpreting marginal frequencies, **not** the validity of our uncollected study.

**Practical repository lesson to test:** on CLI and library docs, independently audit first-run and example-task completeness by project type. Improve a rubric criterion only if new users independently complete accepted tasks; do not optimize README length or a synthetic κ value.
