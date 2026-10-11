# Offline reuse-first gate

This standard-library Python CLI helps prevent jumping directly into generation before surveying reusable options. It is deliberately **not** a retrieval engine, verified software assessment, security scanner, or carbon calculator. It does not contact GitHub or install dependencies.

```bash
python -m trending_study.reuse_gate --input examples/reuse_check.example.json
python -m unittest discover -s tests -v
```

Example data is **synthetic**, including its search log and fake candidate URL. It should print `verify_existing_candidates`, because unverified components must not be silently classified as safe or suitable.

Input schema:
- `schema_version`: "1.0"
- `task`: non-empty user task name
- `acceptance_test`: independent observable task specification (nonempty to proceed)
- `search_log`: list of actual documented search records with source/date/terms
- `candidates[]`: `name`, `source_url`, `functional_test`, `license_compatibility`, `security_review`, `maintenance_review`. Each gate is `verified`, `failed`, or `unknown`. In a real assessment, verification requires dated links/tests, not simply checking a value.

Output: one next evidence gate, candidate counts and self-reported status. No weights, stars, popularity rank or greenwashing statistics. Review candidate provenance independently before consuming untrusted code.

Future research issue: build versioned query/search/retrieval integrations with logged index coverage, no malicious code execution, gold candidate sets and time/energy budgets. See [reuse experiment](REUSE_FIRST_EXPERIMENT.md) and [metrics](REUSE_SUSTAINABILITY_METRICS.md).
