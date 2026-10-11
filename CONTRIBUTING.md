# Contributing

Contributions to methods, reproducibility, tests, docs and scientific critique are welcome.

1. Open or claim a **bounded issue**. Explain scientific validity effects, not only code changes.
2. Branch from `main`; keep PRs focused. Update docs alongside any changed schema, interface or sampling rule.
3. Run `python -m unittest discover -s tests -v`; attach fixture coverage for parser changes.
4. Include an exact reproducible example, assumptions, source URL, date, limitations and whether any data was actually collected.
5. Do not upload credentials, private personal information, undocumented scrapes, inflated growth claims or generated findings presented as observations.
6. Require human review before merging methodological changes or changing sampling/exclusion policy.

## Using AI coding agents (Claude Code, Codex, etc.)
Agents may implement isolated tasks, generate tests, or propose analyses. Ask the agent to first read `AGENTS.md`, `docs/PROTOCOL.md`, and this guide. An example prompt:

> Read AGENTS.md, CONTRIBUTING.md, the research protocol, and the relevant open issue. Implement **only** that issue on a branch. Preserve observational provenance and fail closed on uncertain parsing. Add offline fixture tests, update related documentation, run the full test suite, and open a PR with reproducible evidence. Do not fabricate sample data or research conclusions. Clearly describe any unavailable live validation.

All AI-assisted changes require maintainer review. Disclose substantial AI assistance in the PR.

## 2027 evidence track: contributor workflow
- Before coding, see [research discussion synthesis](docs/CONVERSATION_SYNTHESIS.md), [usefulness construct definitions](docs/USEFULNESS_FRAMEWORK.md), [AI study methods](docs/AI_CODING_STUDY_2027.md), and [claim ledger](docs/CLAIM_LEDGER.md).
- Suggest experiments using [experiment registration](templates/experiment_registration.md) and public recommendations using [lesson card](templates/lesson_card.md). Missing evidence stays explicitly missing.
- Agent contributors can use `python -m trending_study.value_gate --input examples/idea_card.example.json` for an offline synthetic example. The gate is a transparent heuristic and **is not** trained on repository data.
- No publication of private conversations, private prompt logs, user identities, API keys, or unconsented telemetry. Conversation synthesis is not a verbatim archive.
- Document null/negative results, alternative explanations, project-type boundaries and real cost (human time, review/rework, token consumption when observable).
- New idea → bounded issue → preregistered success criterion → minimal tested change → independent reviewer → measured result → documentation and provenance.


## Reuse-first / green engineering requirements
- Before adding new code, document the task, searched prior implementations and at least one realistic reuse/extension alternative when available. Make clear if the search was constrained; no ceremonial empty checkbox.
- Reuse candidates must have reviewed license compatibility, task fit, security and maintenance; independent acceptance tests matter more than GitHub stars. Do not commit unlicensed copied code or raw third-party repositories.
- For research claims, distinguish clone detection from true redundant functionality and independently accepted user benefit. Energy claims require [SCI-style boundary and uncertainty](docs/REUSE_SUSTAINABILITY_METRICS.md), not token multiplication.
- Align any proposed parser, sample or methodology change with [Trending validity](docs/TRENDING_VALIDITY_AUDIT.md), [selection](docs/SELECTION_PROTOCOL_2027.md), and [reuse experimental design](docs/REUSE_FIRST_EXPERIMENT.md). Maintain a dated design amendment before analyzing outcomes.
- Use `python -m trending_study.reuse_gate --input examples/reuse_check.example.json` to demonstrate the evidence gate (synthetic only), plus the full offline unit tests.


## Methodology protection: incomplete retrieval and lifecycle inference
- For every reproducible reuse discovery claim, document task baseline UTC, frozen spec and acceptance tests, all candidate sources including package registries, judged pool coverage, non-judged results and blinded independent verification. False negatives and rejected candidates are valuable outcomes.
- Rater consensus without functional/license/safety verification is not a golden answer. Never mark missing values as zero or use absolute recall without a complete candidate universe.
- Preserve original upstream credit and limit the burden on external maintainers; do not automate unapproved contributions or CI execution of downloaded code.
- Include real alternative choices (do nothing, integrate, upstream patch, compose or bounded build), and life-cycle sensitivity instead of token-only green claims.
- Proposed goldset tool and its synthetic data are methodological guards, not a benchmark of real repositories.
