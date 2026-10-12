# Machine-readable evidence/lesson audit: issue #11

**Status:** bounded offline validator (2026-10-12); neither a real evidence registry nor a replication result. Addresses [#11](https://github.com/MSKazemi/github-trending-1000-study/issues/11) partly.

```bash
python -m trending_study.lesson_registry --input MY_LESSONS.json
python -m unittest tests.test_lesson_registry -v
```

JSON input has a `lessons` array. Each record requires unique `id`, `title`, `status`, `evidence_grade` (E0–E5), `question`, `population`, `comparison`, `primary_outcome`, `measurement_window`, `applicability`, `risks`, `stop_rule`, `validity_threats` and `sources` (empty allowed for hypothesis/E0 only). Sources require HTTPS URL and explicit UTC publication timestamp. Superseded lessons need a successor ID.

A record labeled `validated_for_context` **must** declare E4/E5 controlled or replicated evidence, data reference, distinct analyst/reviewer identities, reviewed timestamp, analysis commit, sample size, numerical effect and interval. The validator still emits `declared_validated_ids_needing_external_review`: a syntactically valid reviewer label, URL or SHA **cannot prove** independence, valid study design or actual observations. This tool never upgrades E0 to another grade.

**Reproducible research workflow:** keep immutable snapshots and versioned code, predeclare the target project type and accepted task, quantify missing data and negative results, independently inspect source/data references, then publish the evidence card. Superseded or contradicted results stay visible. See [E0–E5 protocol](EVIDENCE_TO_LESSON_PROTOCOL.md) and [claim ledger](CLAIM_LEDGER.md).

**Practical maintainer action:** attach one prospectively written lesson card to a first-run onboarding change or reuse-first repair. Only call it an evidence-backed growth practice if independent user acceptance, follow-up and cost corroborate it. Stars, downloads and token totals are not independent reuse evidence.

**Not yet satisfied for issue closure:** citation dereferencing/DOI checks, real data immutability, observer identities/consent, confidence-interval analysis, registered lessons from real cohorts, independent review and integration with the study's full claim register.
