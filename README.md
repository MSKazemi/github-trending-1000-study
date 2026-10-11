# GitHub Trending 1000 Study

**2027 mission:** Discover, verify and reuse existing open-source code before reinventing it, so developers can deliver **genuinely useful software** with less unnecessary human effort, AI-token expenditure, technical debt and environmental impact. GitHub Trending measures *observed attention*, not proven utility or sustainability.

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


## 2027 research track: Useful software in the AI-agent era

**Our goal extends beyond trending:** learn what makes a public project *useful, independently verifiable, economical to maintain, and worth building* as AI-assisted coding expands. This is a proposed sub-study, not a completed set of results.

- [Discussion synthesis / decision history](docs/CONVERSATION_SYNTHESIS.md)
- [Usefulness constructs and metrics](docs/USEFULNESS_FRAMEWORK.md)
- [AI-assisted and vibe-coding sub-study](docs/AI_CODING_STUDY_2027.md)
- [Evidence-to-lesson protocol (E0–E5)](docs/EVIDENCE_TO_LESSON_PROTOCOL.md)
- [Developer build/reuse/pivot playbook](docs/DEVELOPER_DECISION_PLAYBOOK.md)
- [Total token, human and maintenance economics](docs/TOKEN_TIME_ECONOMICS.md)
- [2027 conditional scenarios and monitoring](docs/FUTURES_2027.md)
- [Reference register](docs/REFERENCES_AI_2027.md) and [claim ledger](docs/CLAIM_LEDGER.md)
- [Project idea validation template](templates/idea_validation_card.md), [evidence-graded lesson template](templates/lesson_card.md) and [experiment registration](templates/experiment_registration.md)

### Assess a proposed idea offline

```bash
python -m trending_study.value_gate --input examples/idea_card.example.json
```

This deterministic **heuristic** shows the next evidence gate and budget warnings. It does **not** claim to predict the popularity or usefulness of a project, classify trained-on-1,000 data, or validate a product. The example is synthetic. See [its specification](docs/USEFULNESS_EVALUATION_TOOL.md).

### Research commitments
No generated 'findings' without observed data; no fabricated users, installations or savings; no claim that AI attribution is perfectly detectable; no manipulation of stars/traffic; and no paid growth services. A verified small niche tool may be more useful than a large popular repo.


## New central research track: Green, reusable software by 2027

We now explicitly study **reuse before generation**, not only repository popularity. The scientific question is whether finding, evaluating, integrating and maintaining existing code can improve independently verified user outcomes and reduce total human/energy cost relative to a matched new-build alternative. No energy/CO2 savings have yet been demonstrated.

- **[Green reuse research mission](docs/GREEN_REUSE_MISSION_2027.md)** — updated overarching goal and additional independent reuse cohort
- **[Trending validity and weakness audit](docs/TRENDING_VALIDITY_AUDIT.md)** — what rank/stars do and do not validate
- **[Selection period and eligibility](docs/SELECTION_PROTOCOL_2027.md)** — 2026 Oct pilot; Nov 2026–Apr 2027 candidate enrollment; 180-day follow-ups
- **[Coding agent chronology](docs/AGENT_RELEASE_ADOPTION_TIMELINE.md)** — why 2024+ baseline and verified agent-use events
- **[Reuse/green measurement dictionary](docs/REUSE_SUSTAINABILITY_METRICS.md)** — functional proof, time, token, kWh and SCI-style CO2 bounds
- **[Reuse-first randomized study](docs/REUSE_FIRST_EXPERIMENT.md)** — human vs agent × normal vs reuse-first workflows
- **[Agent development reuse guide](docs/REUSE_FIRST_PLAYBOOK.md)** — practical search, license, security, validation, stop rules
- **[Reusable evidence gate](docs/REUSE_GATE_TOOL.md)** — offline deterministic heuristic; unknown is not pass
- **[Scientific source list](docs/READING_LIST_2027.md)**; [35 AI/GitHub/tech news sources](references/study_sources_2026.json); [16 green/reuse/energy sources](references/green_reuse_sources_2026.json)
- **[Conversation checkpoint](research-notes/conversation-checkpoint-2026-10-11.md)** — all study-related user prompts in this chat, dated assistant findings and decision history

To use the **offline reuse-first evidence check**:

```bash
python -m trending_study.reuse_gate --input examples/reuse_check.example.json
python -m unittest discover -s tests -v
```

The example is synthetic and should request verification, not install code or claim carbon savings. New code may be desirable when no safe, compatible or suitable prior implementation exists. A 1,000-repository Trending sample cannot by itself represent the global universe of useful reusable software.
