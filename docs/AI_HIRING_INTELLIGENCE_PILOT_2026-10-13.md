# AI engineering hiring signals — first primary-source pilot (2026-10-13)

**Status:** exploratory, purposive **source-screened lead sample**, not a hiring census or a publication-ready result. **Observation date:** 2026-10-13 UTC date; precise source request times, initial posting dates, revisions and vacancy closures **not measured**. **Data:** [18 rows, 5 company groups](../references/ai_hiring_job_leads_2026-10-13.csv). **Tracking issue:** [#220](https://github.com/MSKazemi/github-trending-1000-study/issues/220). This is intentionally **separate** from the GitHub Trending sample and the six-month news event corpus.

## Subsequent individual-source QA (2026-10-13)

**Correction to the first-pass seed:** [18-row row-by-row source audit](../references/ai_hiring_job_leads_source_audit_2026-10-13.csv) supplies individual employer/ATS posting URLs, unique requisition IDs where actually visible, a concise skills/responsibilities paraphrase and source-access classifications (not independent third-party authentication). The original [seed CSV](../references/ai_hiring_job_leads_2026-10-13.csv) is retained **unaltered** as the initial lead register; the audit supersedes its first-pass evidence classifications. **17/18** audit rows identify an individual employer/ATS URL and a paraphrase of responsibilities, sometimes obtained from search-indexed text only, with no *recorded* company-identity conflict; this does not independently authenticate the employer or live posting; the remaining **one** (Cursor RL Environments) has an official page whose body names SpaceXAI and is **excluded from company comparisons pending identity adjudication**. This is an audit of a hand-picked sample, not proof that vacancies are active or a statistical hiring distribution.

The 18 individual-source records have **mixed access evidence**: some descriptions were directly opened, while others were retrieved via search-index page text. Search indexing alone cannot authenticate what is live now. Individual posting/publication dates and application/closure status are **unknown** for all records. The sources do not establish exact historical job start dates. Do not count role/location variants as separate requisitions without a stable employer ID.

## Original first-pass source state (historical; superseded by source audit)

- Five groups covered in this **nonrepresentative seed**: OpenAI (4 listings), Anthropic (4), Cursor (4), AWS (3), Cohere (3). Counts are the researchers' **selected job leads**, not total vacancies or an estimate of strategic investment.
- 10 records point to individual job pages with descriptions, 8 to careers-index **titles only** (Anthropic 4, Cursor 4). Never promote title-only leads to job-description evidence. Rows 1–4 and 13–18 have concise original-word paraphrases; extracted page snippets do not authenticate uninterrupted availability or posting history.
- All rows have an official-domain URL (Cohere uses its linked official third-party ATS). Access on a later date or a web index's crawl date is not the ad's publication date. **Unobserved fields are blank, not zero.**
- Only a source URL and brief paraphrase are retained; no copied full copyrighted job descriptions or personal applicant data.

## Source evidence and examples

| Company | Illustrative individual-source lead (access varies) | Narrow observable priority | Limits |
|---|---|---|---|
| OpenAI | [AI Systems Engineer, Codex Agents](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/) | Agent execution harness, sandboxing, orchestration, evals, production latency/cost and diagnostics | Hiring text is intent to staff work; no proof of particular future release |
| OpenAI | [Agent Enablement Engineer](https://openai.com/careers/full-stack-software-engineer-agent-enablement-san-francisco/) | Agent identity and cross-platform user controls | Described direction, not measured successful deployment |
| Anthropic | [Engineering roles index](https://www.anthropic.com/careers/jobs?team=4002065008) | Open titles mention Claude Code performance, managed agents and product sandboxing | **Titles only in this pilot;** exact tasks/skills require individual pages |
| Cursor | [Careers index](https://cursor.com/careers) | Open titles mention harness, RL environments, agent quality and Bugbot | **Titles only in this pilot;** descriptions not captured for these four |
| AWS | [Agentic AI DevOps Engineer](https://www.amazon.jobs/en/jobs/10552775/software-development-engineer-agentic-ai-devops) | Incident investigation/remediation, system integrations, operational reliability | Source is team job advert, not proof of autonomous production remediation outcomes |
| AWS | [AgentCore Engineer](https://amazon.jobs/en/jobs/10544938/sr-software-development-engineer-agentcore-aws-agentic-ai) | Developer SDK/CLI, runtime, memory, identity, evaluations, deployment | Job describes a technology stack, not third-party adoption rates |
| Cohere | [Agent Infrastructure Engineer](https://jobs.ashbyhq.com/cohere/70664617-84f6-4ee8-a4f6-4037ebfda9db/) | Secure execution, identity, model routing, resource control and state | Firm-specific needs; not workforce survey evidence |
| Cohere | [Agents Modeling MTS](https://jobs.ashbyhq.com/cohere/24fe6a0b-6209-4ee0-b622-49c18636d99c/) | Reasoning/tool use/memory and post-training methods | Research direction only, not published benchmark gains |

## Preliminary qualitative thematic synthesis — **not statistical results**

A manually selected set of adverts contains recurring terms associated with: (1) agent harnesses/execution and safe sandboxing, (2) tool interaction and long-running durable workflows, (3) evaluation/diagnostics/quality and RL environments, (4) agent identity/permissions/security, (5) inference/model routing/latency/cost, (6) developer-product integration and agent operations, and (7) memory/context and codebase integration.

**Conditional 2027–2031 interpretation:** If sustained investment and deployment corroborate these signals, a share of software engineering may shift from generating individual code snippets to specifying bounded tasks, discovering reusable dependencies, granting minimal permissions, executing agents, evaluating independent outcomes and maintaining deployed systems. Competing explanation: teams may recruit to fix current reliability problems, replace attrition, hedge research bets or market aspirational projects that never ship. A role title does not verify a budget, headcount, filled vacancy or a future company decision.

## Practical experiments for the green, reuse-first GitHub study

1. **Existing-code discovery task:** Randomly assign otherwise matched predeclared coding tasks to agent workflows with versus without verified existing-code search; blind-check functional acceptance, license/security, full human/agent cost, retries, maintenance and verified upstream/downstream reuse. A search miss is not proof no code exists.
2. **Agent-harness test:** Hold the agent/model, task set and tool versions constant; test isolated execution, permission minimization, traceable actions and resume-after-failure against baseline. Measure passed independent tests, security incidents, repair load and latency, including no-completion outcomes.
3. **Evaluation-before-merge test:** Randomize an independent test/review gate against ordinary PR workflow for eligible opt-in task cohorts; predeclare primary acceptance and downstream 30/90-day regression/maintenance outcomes. Count human review cost and failures.
4. **Agent-memory portability test:** Compare minimal portable task/context manifests and reusable project instructions with unstructured agent sessions on a blinded cross-repository transfer task. Check correct code reuse rather than just generated-code volume.

**Repository-level low-regret engineering proposals, not validated growth effects:** provide a machine-readable install/test/usage contract, safe sandbox for code-executing agents, least-privilege contribution instructions, reproducible evaluation fixtures, clear license/provenance and straightforward discovery of reusable modules. Do not add experimental complexity unless independent user-task completion improves.

## Design for next wave and scientific safeguards

**Sampling:** Predefine a population of company career pages (draw from the established 100-company watchlist), company/product identity map and company-time panel. Log exact queries, UTC observation times, index version, source status, robots/terms review, capture hash where allowed and job IDs. Include negative/missing observations with source failure categories; do not equate missing site data with zero jobs. Deduplicate mirrored positions, office/location variants and repostings; report raw ads and unique requisitions separately. Avoid invasive scraping and unauthorized snapshots.

**Codebook:** `company_id`, `parent_entity`, `job_id`, `title`, `canonical_url`, `role_location`, `team`, `first_observed_utc`, `last_observed_utc`, `posting_date_if_explicit`, `source_kind` (`individual`/`index`), `availability_verified`, `responsibility_paraphrase`, `required_skills`, `themes[]`, `direct_source_span` (short internal note), `archival_permission`, `source_sha256_if_permitted`, `coder_id_pseudonym`, `confidence`, `counterinterpretation`, `linked_product_evidence`. Prefer short paraphrase and only necessary quotes with rights review.

**Biases and review:** Job listings are strategically curated, may remain open, repeat, be re-posted or fill existing seats; location, outsourcing and ATS indexing differ by firm; a role signals capability demand, not realized spend or roadmap. Two independent coders should label a subset against a frozen taxonomy, reconcile disagreements and report appropriate inter-rater agreement. Triangulate with changelogs, release artifacts, actual public code and independent task tests. Report negative/cancelled initiatives and source-selection bias; avoid comparing raw company job counts without workforce-size and exposure corrections.

**Evidence classification:** The jobs are descriptive, direct company statements (company-watch E1 at best for the *advertised responsibilities*); thematic futurism is a conditional analyst hypothesis, **not** study E2+ association. All newly proposed repo experiments are untested. No observed tokens, energy, CO2e or adoption improvements are claimed.

**Next gates:** Expand to Microsoft, Google DeepMind/Google, Meta, NVIDIA, Mistral, Cognition and other watchlist companies *only after checking individual active descriptions*; save source page timestamps and working links, code independently, and compare with dated releases. The 18-row CSV is a **seed** and its company counts are not suitable for graphs of recruitment trends.

## Links to other work
[OpenAI #67](https://github.com/MSKazemi/github-trending-1000-study/issues/67), [Anthropic #68](https://github.com/MSKazemi/github-trending-1000-study/issues/68), [100-company methodology](COMPANY_INTELLIGENCE_METHOD_2026_10.md), [News #56](https://github.com/MSKazemi/github-trending-1000-study/issues/56), [source watch #32](https://github.com/MSKazemi/github-trending-1000-study/issues/32), [mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md), [evidence-to-lesson](EVIDENCE_TO_LESSON_PROTOCOL.md).
## Verification limits and audit follow-up

- Employer-origin ATS links were followed from official careers boards when possible; Anthropic Greenhouse IDs are explicit in the corrected ledger. Cohere and AWS pages sometimes returned a search-indexed full description while direct open attempts could not be fetched; these are tagged `read_indexed_text`, **not** independently authenticated live HTTP views.
- The Cursor RL Environments description resolves on a Cursor-branded localized URL but mentions SpaceXAI as the employer/team; until the identity is resolved do not allocate this row to a corporate parent or use it in theme/company comparisons.
- The first-pass count of 10 individual pages/8 title-only leads describes **the initial collection**, not the reviewed source-audit state. No row is a completed hiring event.
- **No blinded independent human double coding, rights review, complete 100-company search frame or 30/90/180-day follow-up has yet been completed.** Study forecasts are hypotheses only.


## Row-level source-audit amendment (2026-10-13)

The first-pass 10-individual/8-index distinction is **superseded for source characterization only** by the [18-row supplemental source audit](../references/ai_hiring_job_leads_source_audit_2026-10-13.csv). The original seed remains immutable. The audit identifies individual employer/ATS URLs and requisition IDs where accessible, separates directly read descriptions from descriptions seen through a search index, and retains **unknown** vacancy status and original posting dates. **Do not report all 18 as independently verified live vacancies.**

One Cursor RL Environments source has an employer-identity inconsistency (page text refers to SpaceXAI); quarantine that lead from company-level inference until adjudicated. No panel census, inter-rater agreement, measured future releases, measured adoption, or energy effects are established by this amendment.

## 2026-10-15 bounded direct-source revisit

The [dated ten-source source-access recheck](reviews/2026-10-15-hiring-source-recheck-220-221.md) confirms three readable individual job descriptions (OpenAI, Anthropic, Cursor), explicitly logs failed AWS/Cohere individual URLs, and separately records Google/NVIDIA failures, Microsoft/Meta index-only evidence and a Mistral employer-branded page marked unavailable. **No additional verified historical publication date, actual hire, company-wide headcount or automatically authorized crawling is claimed.** This supplements rather than overwrites the 18-row historical seed. #220 stays open until the required 7-company direct-source corpus and independent reviewer/source-rights gates are met.
