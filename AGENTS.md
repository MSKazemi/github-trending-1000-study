# Repository instructions for AI coding agents

**Mission:** Build reproducible research infrastructure; never invent results or imply 1,000 repositories have already been collected.

- Before changes, read `README.md`, `docs/PROTOCOL.md`, `docs/DATA_DICTIONARY.md`, `docs/ETHICS.md`, and `CONTRIBUTING.md`.
- Work on one bounded issue per PR. Update documentation for interface, schema and methods changes.
- Respect GitHub access rules, API limits and credentials. No scheduled scraping, bypass, invasive personal-data harvesting or unverified claims.
- Distinguish an *appearance* (same repo may recur) from a *unique repository* (ID-based when available).
- Keep timestamps in UTC and include provenance; do not substitute today's metadata for historical measurement.
- Test offline with committed synthetic fixtures; no integration-test dependency on live GitHub.
- Run `python -m unittest discover -s tests -v`. State what was tested and what remains unvalidated.
- Research protocol changes need explicit justification, versioning and human approval.

## 2027 value research and lessons
- Read \`docs/CONVERSATION_SYNTHESIS.md\`, \`docs/USEFULNESS_FRAMEWORK.md\`, \`docs/AI_CODING_STUDY_2027.md\`, \`docs/EVIDENCE_TO_LESSON_PROTOCOL.md\`, \`docs/REFERENCES_AI_2027.md\`, and \`docs/CLAIM_LEDGER.md\` before making evidence claims.
- Never conflate GitHub stars/commits/PR counts with user benefit, adoption, correctness or total developer productivity.
- Use the prospective templates for experiments and lesson cards; unknown measures must remain unknown, not become 0 or fabricated observations.
- Coding agents must favor reuse, minimal patches, user-task acceptance tests, review/security and budget-aware iterations. Be transparent that example project assessments are synthetic.
- Neither AGENTS.md nor stylistic fingerprints establish undisclosed AI authorship. Do not identify individual developers from detector guesses.
