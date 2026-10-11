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
