# GitHub Trending 1000 Study

**A reproducible, longitudinal observational study of open-source repository visibility, community practices, and growth.**

[![CI](https://github.com/MSKazemi/github-trending-1000-study/actions/workflows/ci.yml/badge.svg)](https://github.com/MSKazemi/github-trending-1000-study/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)

> **Research status: protocol and tooling (not findings).** No sample of 1,000 repositories has been collected or analyzed yet. This project does **not** claim causal effects or endorse manipulation of GitHub Trending.

## Questions
- **RQ1:** Which observable repository practices are associated with subsequent star growth *within* a trending sample?
- **RQ2:** Do documentation, governance, automation and contribution affordances predict subsequent engagement after controlling for age, language and baseline popularity?
- **RQ3:** How do trending repositories differ from an independently sampled non-trending comparison cohort?
- **RQ4:** Which observed associations persist across languages, observation windows and follow-up periods?

## Start here
- [Research protocol](docs/PROTOCOL.md) — operational definitions, sampling, confounding and analysis.
- [Data dictionary](docs/DATA_DICTIONARY.md) — schema, missingness and provenance.
- [Ethics and limitations](docs/ETHICS.md) — privacy, API etiquette and validity.
- [Contributing](CONTRIBUTING.md) — human and AI-agent contributions.
- [Roadmap](docs/ROADMAP.md) — staged milestones and acceptance criteria.

## Install & run

Requires Python 3.10+; no external Python dependencies.

```bash
python -m unittest discover -s tests -v
python -m trending_study --help
python -m trending_study parse-trending --input tests/fixtures/trending.html --date 2026-10-11 --window daily --output /tmp/trending.jsonl
python -m trending_study summarize --input /tmp/trending.jsonl
```

To capture a *live*, public Trending page (explicit opt-in, no automatic scraping):

```bash
python -m trending_study capture --date 2026-10-11 --window daily --output data/raw/2026-10-11-daily.html
python -m trending_study parse-trending --input data/raw/2026-10-11-daily.html --date 2026-10-11 --window daily --output data/processed/2026-10-11-daily.jsonl
```

`capture` makes **one** HTTPS request. It does not bypass access controls or retry aggressively. Collection date must reflect the date on which the page is actually observed; backdated Trending rankings cannot be recovered from today's page. Consider manual snapshots if automated access is disallowed.

Enrich observed repositories with current public metadata (optional `GITHUB_TOKEN`; do not commit tokens):

```bash
GITHUB_TOKEN=... python -m trending_study enrich --input data/processed/2026-10-11-daily.jsonl --output /tmp/enriched.jsonl
```

See the protocol before interpreting any collected counts. A Trending appearance is not a random sample of all GitHub projects, and GitHub's Trending ranking methodology is opaque.

## Reproducibility and citation
Each observation includes provenance, UTC collection time, selection window and source URL. Preserve frozen raw captures with checksums before analysis. Record a protocol version, fixed analysis scripts and a snapshot tag for published results. **Do not infer causal growth strategies from cross-sectional correlations.**

## License
MIT applies to original code and text here. Third-party repository metadata remains subject to applicable rights, platform terms and privacy obligations. Reuse of harvested data should be assessed separately.

## Contribute
Open an issue for reproducibility defects, language coverage, validity threats, sampling improvements, visualization or replication. See [CONTRIBUTING.md](CONTRIBUTING.md).
