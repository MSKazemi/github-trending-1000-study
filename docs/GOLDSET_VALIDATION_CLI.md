# Reuse gold-set validator (offline, standard library)

This is an **input-validation and descriptive summary** tool. It does **not** prove that input judgments are accurate, test third-party code, evaluate security, audit licenses, or estimate true recall over all available open-source software.

## Run with SYNTHETIC data only
```bash
python -m trending_study.goldset --input examples/goldset.synthetic.json --k 2
python -m unittest discover -s tests -v
```

The synthetic example has exactly one reviewed viable pair, one unknown pair and one reviewed failing pair. The demo should return **no point estimate** for precision@2 when the top two includes an unjudged candidate. It reports a lower and upper bound and explicit judged-pool coverage; pooled relative recall is not absolute recall.

## Input rules
- A task records baseline UTC, frozen task/spec and acceptance suite hashes.
- Candidate has exact ID, recorded earliest availability, required gate statuses (functional, license, security, maintenance), two reviewer labels, final label and evidence reference.
- A candidate cannot be labeled viable if any mandatory gate is unknown or failed or if its first available version postdates the task.
- Reviewer disagreement needs a documented adjudicator.
- Ranked system results must correspond to candidates in the declared pool; do **not** silently treat an unknown search result as irrelevant.
- Study/pilot dataset kinds are declared and never made genuine by the software: empirical provenance requires actual auditors, dated tests and publication review.

## Scientific limitations
- Fixed top-K denominator counts non-returned slots as empty.
- Precision@K is undefined when an actual returned candidate has unknown judgment; pessimistic/optimistic bounds are shown.
- Pooled relative recall is reported only against **known viable candidates in the shared judged pool** and is usually biased upward relative to true global recall; never call it true recall.
- Raw percentage agreement is not Cohen's kappa and does not certify reviewer independence.
- No real collection or human study is performed by this module.

See [gold-standard protocol](REUSE_GOLD_STANDARD_2027.md), [critical gap register](CRITICAL_RESEARCH_GAPS_2027.md), and [science governance](SCIENTIFIC_GOVERNANCE_2027.md).
