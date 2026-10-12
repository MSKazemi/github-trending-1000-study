# AI-era engineering news evidence corpus (2024–2031)

**Started:** 2026-10-12. **Stage:** provisional editorial/source review, NOT systematic literature review, not preregistered and not independently fact-checked. **Target:** up to 1,000 individually cited distinct entries; **currently committed:** 14 (NEWS-2026-0001 through 0014). **Important:** 14/1,000 = 1.4%; this does not imply coverage or representativeness.

**Scope:** major research updates, official vendor launches, standards/governance announcements, independently sourced technology journalism and contradictory investigations relevant to agentic software engineering, coding methods, quality, reuse, OSS adoption, interoperability, supply-chain security, human/energy cost, and bounded 2027–2031 futures. Source publication may precede 2026; future events must never be represented as observed.

## Files and conventions
- Each individually committed item: [references/ai-era-news/items/](../references/ai-era-news/items/); immutable stable ID `NEWS-2026-NNNN`. The `2026` portion means **ingestion vintage**, NOT publication year.
- Source-of-truth is one UTF-8 JSON record per item; do not silently overwrite originals or regenerate unreviewed source facts. Corrections via review-linked revision.
- Existing scholarship: [2026 research register](../references/study_sources_2026.json), [references](REFERENCES_AI_2027.md), [scientific claim ledger](CLAIM_LEDGER.md). The same study may be discussed in a news item and in a scholarly item; cross-link but **do not count as independent confirmation**.
- This launch provides **no original study observations**, adoption denominators, lifecycle measurements, or causal effects.

## Screen and save each article before moving on
1. Record discovery query, search date, candidate URL, inclusion/exclusion reason. Favor accountable original sources and empirical/corrective reports, while inviting independent critiques and null findings; do not select solely by vendor prestige, circulation, popularity or a desired narrative.
2. Read the full accessible source (or mark only abstract/snippet, exclude unsupported claims); verify exact headline, source identity, original publication date versus update date, canonical URL, and whether actual data is supplied.
3. Identify the **type of evidence**: primary product release, organizational forecast, standard, research report, independently reported journalism, peer-reviewed paper, survey, or expert commentary. A launch is **availability**, not **adoption**; a survey is not an experiment; a prediction is not an observed future.
4. Paraphrase key falsifiable attributed claims and methods/denominators (or write `not supplied`); state version, conflicts/incentives, counterevidence, and conditional applicability. No bulk copying of copyrighted reports.
5. Commit ONE item as `references/ai-era-news/items/NEWS-2026-NNNN.json` before starting another. Use stable canonical URLs and check duplicates; mark follow-on stories as related, not independent corroboration.
6. Suggest ONE cheap, safe independent maintainer experiment with pre-specified task, baseline and human review; label as **proposed**, never proven. Do not fabricate outcomes.
7. On independent fact-check/reviewer completion, update status with reviewer and date on a separate traceable commit. Superseded/incorrect items remain auditable, not deleted.
8. Refresh a **derived** index/counter after adding entries. Do not claim a 1,000-source achievement before the count is verified.

## Minimum record v1.0
Required: `schema_version`, `id`, `title`, `publisher`, `original_publication_date`, `accessed_date_utc`, `canonical_url`, `source_type`, `topics`, `screening_status`, `source_review_status`, `attributed_claim_summary`, `limitations`, `practical_experiment`, `independent_corrob_status`, `review_status`. Additional review fields and data fields remain explicit `null` / `not_assessed` until checked. Reject non-HTTP URLs, future publication dates relative to verified access and duplicate canonical URLs. No source is upgraded to E4/E5 from a vendor announcement.

## Priority topic allocation for further *screening*, not quotas on conclusions

| Area | Exploratory target | Primary research question |
|---|---:|---|
| Agentic coding and delegation | 170 | What tasks safely shift from humans to agents? |
| Model capability, benchmarks, validity and evaluation | 140 | Do benchmarks predict independently accepted work? |
| Reuse, discovery, libraries, maintainability | 140 | Does reuse-first beat generate-first for net value? |
| Security, supply chain, provenance, privacy | 125 | What safety costs and controls follow agents? |
| OSS communities, contributor economics, adoption | 110 | What is sustained independent use, not mere stars? |
| Standards, MCP, A2A, interoperability, workflow | 95 | Can tools and evidence outlast one model provider? |
| Energy, hardware, costs, lifecycle sustainability | 95 | Is there a measured or bounded net environmental benefit? |
| Human factors, policy, research methods, futures | 125 | What changes in review, work allocation and 2027–31 scenarios? |
| **Total** | **1,000** | Planned balanced evidence frame, not observed distribution |

Screen across 2024 historical baseline; 2025–26 agent launches and actual studies; 2027–31 **prospective checks only**. Curate diverse independent reporting, open critique, published negative findings and OSS maintainer voices, not only executives. Rank source reliability based on methods, primary evidence, provenance, correction practices and disclosed conflicts—not importance of a CEO.

## Initial synthesis — explicitly provisional
1. **Agent delegation expanded in 2025:** Anthropic Claude Code (NEWS-2026-0003), OpenAI Codex (0005), GitHub Copilot coding agent (0006) and later management panels (0008, 0014). This is a documented product timeline, **not** a quantitative agent-use cohort or a validated task improvement.
2. **Interoperability is becoming an explicit design objective:** MCP (0001), A2A (0004) and the Agentic AI Foundation (0013) support attention to portable task/tool contracts; claims of complete portability await tests.
3. **Attention is not reuse:** GitHub Octoverse (0009) reports sizable platform activity and language trends, but platform descriptives do not prove independent utility, safety, or AI-caused growth.
4. **Productivity remains context-dependent:** METR's 2025 RCT (0012) found slower completion under one early-2025 condition. Its 2026 methodological update (0011) describes later selection and time-tracking problems. Neither supports a universal current speed multiplier.
5. **Bottleneck hypothesis:** as agents create more changes, human review, secure acceptance tests, task routing and dependency reuse may become stronger constraints. Treat this as a **forecast hypothesis** (see GitHub vision 0007), not an established 2031 prediction.

## Immediate practical maintainer lessons (proposed validation)
- Codex/Claude contributions: requirement → search existing implementations → version/license/security check → bounded agent work → independent acceptance tests → human-approved PR → 30/90-day recheck.
- Track real first-user task success and working downstream integration; do not optimize solely for GitHub Trending, stars, LOC, merged PRs or automation count.
- Give each agent run a traceable task ID, source versions, attempted reuse, cost, tests, reviewer outcome and failure record.
- Measure *entire* task time and maintenance/review burden before claiming acceleration; run an opt-in controlled comparison for reuse-first vs generate-first.
- Treat estimated tokens saved as an economic input, not an energy measurement; environmental assertions require measured or explicitly bounded whole-lifecycle analysis.

## Required to qualify for a scientific systematic evidence synthesis
Publish preregistered questions, search strings, databases and UTC search timestamps, screening exclusions and PRISMA-style counts, two independent reviewers with agreement/adjudication, field-level verification for all items, duplicate cluster resolution, bias appraisal, source versions and corrections, denominators by class/date and publicly reproducible synthesis scripts. Until then this is a useful **curated, provisional research intelligence corpus**, not a systematic review.

**Cross-links:** [Evidence-to-lesson protocol](EVIDENCE_TO_LESSON_PROTOCOL.md), [AI-era research mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md), [source-watch issue #32](https://github.com/MSKazemi/github-trending-1000-study/issues/32), [news expansion issue #56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).

## Offline structural validation (not a factual review)

Run `python -m trending_study.news_corpus --directory references/ai-era-news/items` and `python -m unittest discover -s tests -v` before adding records or requesting review. This checks file/ID consistency, duplicate canonical pages (ignoring query strings), mandatory fields, chronology, URL hygiene and explicit pending-review status. It **does not** fetch live sources, authenticate review, check event/claim accuracy or make this a systematic sample. Missing/excluded candidates and multiple articles covering one event require a separate discovery/screening ledger, not fictional entries in the included-item collection. Keep this PR draft until independent checks and latest-head CI succeed.
