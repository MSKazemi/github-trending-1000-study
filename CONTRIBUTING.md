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
