# Repository instructions for AI coding agents

**Mission:** Build reproducible research infrastructure; never invent results or imply 1,000 repositories have already been collected.

- Before changes, read `README.md`, `docs/PROTOCOL.md`, `docs/DATA_DICTIONARY.md`, `docs/ETHICS.md`, and `CONTRIBUTING.md`.
- Work on one bounded issue per PR. Update documentation for interface, schema and methods changes.
- Respect GitHub access rules, API limits and credentials. No scheduled scraping, bypass, invasive personal-data harvesting or unverified claims.
- Distinguish an *appearance* (same repo may recur) from a *unique repository* (ID-based when available).
- Keep timestamps in UTC and include provenance; do not substitute today's metadata for historical measurement.
- Test offline with committed synthetic fixtures; no integration-test dependency on live GitHub.
- Run `python -m unittest discover -s tests -v`. State what was tested and what remains unvalidated.
- Before proposing any PR merge, inspect the **entire current diff**, confirm an exact-head Python 3.10/3.12 CI result, review security/provenance/docs, reconcile overlapping branches **without losing unique tests or source references**, and use the expected head SHA for any merge. Do not treat unprotected `main`, draft PRs or green synthetic tests as human methods approval. See [merge gates](docs/PR_MERGE_QUALITY_GATES_2026_10_13.md).
- Research protocol changes need explicit justification, versioning and human approval.

## 2027 value research and lessons
- Read `docs/CONVERSATION_SYNTHESIS.md`, `docs/USEFULNESS_FRAMEWORK.md`, `docs/AI_CODING_STUDY_2027.md`, `docs/EVIDENCE_TO_LESSON_PROTOCOL.md`, `docs/REFERENCES_AI_2027.md`, and `docs/CLAIM_LEDGER.md` before making evidence claims.
- Never conflate GitHub stars/commits/PR counts with user benefit, adoption, correctness or total developer productivity.
- Use the prospective templates for experiments and lesson cards; unknown measures must remain unknown, not become 0 or fabricated observations.
- Coding agents must favor reuse, minimal patches, user-task acceptance tests, review/security and budget-aware iterations. Be transparent that example project assessments are synthetic.
- Neither AGENTS.md nor stylistic fingerprints establish undisclosed AI authorship. Do not identify individual developers from detector guesses.


## Mandatory reuse-first checks for agent contributions
- Before generating source, read `docs/GREEN_REUSE_MISSION_2027.md`, `docs/REUSE_FIRST_PLAYBOOK.md`, `docs/REUSE_SUSTAINABILITY_METRICS.md`, and `docs/TRENDING_VALIDITY_AUDIT.md`.
- Search repository code and appropriate public packages/peer implementations first. Log time-boxed candidates and compare functional fit, valid licenses, security and maintenance; a GitHub star or Trending rank does NOT verify suitability.
- Prefer a tiny tested upstream patch or a compatible reused library over rebuilding functionality, **where independent acceptance tests support the choice**. Reuse is never mandatory when safety/maintainability makes it inferior.
- Every new feature should have a practical external task, fixed acceptance criteria, bounded human/token budget, existing-code comparison and transparent limitations.
- Run both `python -m trending_study.value_gate --input examples/idea_card.example.json` and `python -m trending_study.reuse_gate --input examples/reuse_check.example.json` as synthetic CLI smoke tests, plus the full unit suite.
- Never invent kWh or gCO2e from token count. Only report reproducible measured or clearly modeled environmental impacts with uncertainty and system boundary.


## Critical gap checks before recommending new software or scientific conclusions
- Consult docs/CRITICAL_RESEARCH_GAPS_2027.md and docs/REUSE_GOLD_STANDARD_2027.md. Do not claim a reusable implementation doesn't exist solely because search failed.
- Do not let a coding agent evaluate its own correctness with self-authored acceptance tests. Freeze task requirements and arrange independent review, and keep no-solution tasks in the primary treatment denominator.
- Inspect exact package+version, first availability date, license, provenance, security and maintenance evidence; no arbitrary unreviewed scripts or untrusted dependency installation.
- Assess human and maintainer effort plus development and runtime energy; no exact CO2/tokens multiplier, no false global-recall claim from an incomplete pool.
- Run python -m trending_study.goldset --input examples/goldset.synthetic.json --k 2 for the declared synthetic demonstration only and python -m unittest discover -s tests -v for offline regression tests.
- Do not assert the 2027 study has been preregistered, collected or externally validated until it actually has been.


## Five-year research and trust rules
- Read docs/ADVISORY_BOARD_STRATEGY_2027_2031.md, docs/FIVE_YEAR_ROADMAP_2027_2031.md and docs/LEADERSHIP_SCORECARD_2027_2031.md when changes affect strategic goals or research claims.
- Never claim real professorial/CEO/CTO oversight or partner-company endorsement. The 'board' is a hypothetical role-based framework until named experts actually consent.
- Prefer portable task specifications, independent acceptance, valid provenance and benchmark repeatability across changing agent models.
- Do not optimize 2027–2031 'success' by increasing project N, stars, merged PRs, token generation or unlabeled reused code. Quantify independently verified user/task value, safety/rights, lifecycle cost and full/partial environmental boundaries.
- Do not build a commercial ranking marketplace or change gold labels for sponsors; maintain independent open research data, registered hypotheses and null findings.
- Follow docs/INCEPTION_CHECKLIST_2026_2027.md; if October pilot or permissions are incomplete, amend enrollment dates rather than backdate samples.


## 2026–2027 pilot preflight and capture integrity
- The October 2026 pilot is **proposed and not yet executed**; do not describe a synthetic fixture or self-declared manifest as authenticated GitHub collection.
- **Access hard stop (2026-10-13):** `trending_study capture` is intentionally disabled before network I/O because `/trending?since=...` falls under the published robots disallow pattern and access for this project remains unapproved. Never bypass it with a flag, monkeypatch, manual snapshot or alternate HTTP client. Only a reviewed code/protocol amendment following documented human source-access approval can re-enable it. Offline synthetic test mocks are not real capture permission. Read [source-access decision](docs/SOURCE_ACCESS_DECISION_2026-10-13.md).
- After an approved future re-enablement, any new capture must use `capture --manifest-output` and `pilot-parse --manifest`; never backfill `captured_at_utc` from parsing or a supplied date.
- The strict parser only implements unfiltered daily/weekly/monthly surfaces, **not** six language views or 9-page daily capture. Expand the source manifest protocol and human audit before changing enrollment eligibility.
- Maintain human access-policy review, manual page QA, immutable numeric repo IDs, task-based independent acceptance, statistical power, consent and preregistration checks. These gates cannot be fulfilled by checking in a JSON file.
- Run `python -m trending_study pilot-preflight --input examples/pilot-preflight.example.json --stage confirmatory` and `python -m unittest discover -s tests -v` after a protocol/CLI change. The documented example should remain not_ready.
- See docs/PILOT_CAPTURE_AND_PREFLIGHT.md, docs/PREREGISTRATION_DRAFT_2027.md and docs/PROTOCOL_FREEZE_STATUS_2026_10_12.md. Update versions and date decisions without rewriting original hypotheses after results.

## Central research objective and practical lesson delivery (2026-10-12)
- Before describing the research's goals or delivering generic GitHub-growth advice, read [AI-era coding and reuse research mission](docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md) and [practical maintainer handbook](docs/PRACTICAL_REPOSITORY_GROWTH_AND_REUSE_2027.md).
- The purpose is to understand *changes in coding methods* (traditional, AI-assisted, vibe/prompt-led, delegated-agent), functional quality, independently verified downstream reuse, organic discoverability, contribution, and whole-lifecycle sustainability. Trending ranks are not the mission's success criterion.
- Give maintainers specific task-tested, project-type-appropriate actions and use [the blank action/evidence card](templates/repository_action_evidence_card.md); do not invent adoption, effect sizes or energy outcomes. Preserve negative/null findings and confounders.
- Keep old reusable projects eligible as alternatives and controls. Do not optimize for having few repositories rather than high-value interoperable components.


## Never overwrite original observation evidence (issue #4)
- The original raw HTML, SHA manifest, pilot audit, parsed JSONL and enrichment are write-once records. Use new attempt filenames; never replace, truncate, or silently backdate an artifact.
- If publishing an artifact bundle is interrupted, preserve partial evidence with explicit error and do not count it toward a valid cohort. The pair is not an atomic database transaction.
- Read [capture safety and operator instructions](docs/CAPTURE_IMMUTABILITY_2026_10_12.md) and update regression tests whenever collector semantics change.

## Longitudinal follow-up data-integrity gate (issue #4)

- Read [longitudinal follow-up instrumentation](docs/LONGITUDINAL_FOLLOWUPS_2026_10_12.md) before editing any follow-up code, schedule or event schema.
- Never set `eligible_for_confirmatory_cohort=true` or a protocol/approval reference without independently verified human signoff. Fake fixture approval is a synthetic test flag, not research authorization.
- Baseline t0 is the **actual UTC metadata measurement timestamp**; scheduled observations must preserve matched repository ID, true observed timestamp, plan checksum, missingness, response/rate-limit metadata and scope. No historical backfill from a later API count.
- Opt-in network calls only, bounded and permission-safe. Test with mocked HTTP; do not claim completed pilot or validated outcome data from offline tests.

## Structural parser validity is NOT real-page recall (#2)

- Treat each supported Trending Box-row as one immutable displayed rank. Never drop malformed/duplicate rows and then call the remaining ranks complete.
- A structural selector-row count cannot detect off-selector rows or changed GitHub markup. Check [real human QA criteria](docs/PARSER_STRUCTURE_QA_2026_10_12.md); real capture dates, supported surfaces and at least 30 independently adjudicated rows are outstanding.
- Do not mark `parser_audit` verified or close #2 based only on synthetic unit tests.


## Planned task-trial instrumentation guard (#25)
- Use [trial pilot instrument](docs/TRIAL_PILOT_INSTRUMENT.md) only to validate prospective **synthetic or independently authorized opt-in pilot** records. Verify frame SHA binding, write-once assignment, all randomized task outcomes including refused/abandoned/pending and actual consent; no pilot data is authenticated by the script.
- A public deterministic assignment seed is not allocation concealment or a real preregistration; do not convert public issue intake leads to trial participants automatically. Keep hidden acceptance tests independently authored and out of agent context.


## New independent page-QA guardrails (#2)
- Read docs/INDEPENDENT_PAGE_AUDIT_2026_10_12.md before claiming any real GitHub Trending parser validity.
- Use two actually independent reviewers who inspect the original preserved source **before** looking at parser output. The QA scorer cannot independently establish the people exist or were blind; a matching pair of generated annotations is **not** independent verification.
- Include *every* displayed row, not only valid `article.Box-row` hits. Compare identity and exact rank, and count parser-rejected pages as missing emissions rather than silently excluding them.
- Use `audit-pages` over the captured raw SHA/manifest and reviewer labels; retain a write-once canonical JSON QA report, with optional derived `--markdown-output` and no overwrite. Dual outputs are **not atomic**; preserve partial publications for human incident review. A documentary pass never changes `eligible_for_confirmatory_cohort=false` and is not a signed protocol or ethical approval.
- Reviewer A/B/C references must be bounded ASCII pseudonyms rather than email, contact details, path text or the placeholder `unknown`. Matching pseudonyms do **not** authenticate different real people.
- Optional reviewer-C adjudication is **only** for actually disputed A/B ranks; preserve original A/B labels and reviewer chronology. A third self-declared ID or passing synthetic regression does **not** authenticate human independence, source access or scientific approval. Do not introduce a competing page-QA CLI.
- Never call the 36-row synthetic regression test a real 30-entry live audit, or infer current robots/Terms permission when source access is unavailable.


## Task-cost ledger and privacy requirement (issue #10; 2026-10-12)

- Read [task cost ledger contract](docs/TASK_COST_LEDGER_2026-10-12.md) before changing per-task economics or agent telemetry; do **not** collect real provider, Copilot/Codex/Claude or human traces without participant consent and explicit human scientific approval.
- Use `trending_study.task_costs` **offline** with frozen trial frame/assignment/outcome inputs, one record per randomized task, explicit missingness, fail-closed field checks and write-once output. A log validator cannot authenticate instrumented data.
- Treat currency as provenance-tagged **event scope only**; tokens are not kWh, parallel agent duration is not extra human hours, and a missing record is never a zero-cost result.
- Use `python -m unittest discover -s tests -v`; disclose that all committed task-cost fixtures and performance values are synthetic, without generating or publishing human identities or prompt content.
