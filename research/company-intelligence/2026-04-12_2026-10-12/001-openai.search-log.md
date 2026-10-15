# OpenAI company-watch #001: source discovery, exclusions and reproducibility log

**Ran on:** 2026-10-12 (search interface; no persistent engine hit-count or ranked-result export available). **Interval:** 2026-04-12 through 2026-10-12 inclusive, publication date. **Protocol:** [company method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md). **Issue:** [#67](https://github.com/MSKazemi/github-trending-1000-study/issues/67).

## Exact search terms entered

Queries below were submitted as web search terms on 2026-10-12. Engine ranking, full result-list snapshot, individual hit counts and actual scanned-result denominators were **not saved**. **Found / screened / excluded numeric totals are unknown**, *not zero*. Each month has primary URL examples in the [report](001-openai.md), and each included event has one canonical URL in [the event table](001-openai.events.csv). Repeated official/press narratives of the same event were deduplicated editorially, not mechanically.

| Segment | Reproducible search terms | Search coverage and remaining blind spots |
|---|---|---|
| Apr 12–30 | `site:openai.com/index/ Codex after:2026-04-11 before:2026-05-01`; `site:openai.com/index/ Codex April 2026 OpenAI announcement 2026-04` | Official/product and partner release; deep technical changelog changes may be missing |
| May | `site:openai.com/index/ Codex after:2026-04-30 before:2026-06-01`; `site:openai.com/index/ Codex May 2026 announcement` | Official safety and mobile preview; independent product tests not identified in included set |
| Jun | `site:openai.com/index/ Codex after:2026-05-31 before:2026-07-01`; `site:openai.com/index/ Codex June 2026 announcement` | Official product, AWS and proposed transaction; roadmap confirmation required |
| Jul | `site:openai.com/index/ Codex after:2026-06-30 before:2026-08-01`; `OpenAI Codex July 2026 security Hugging Face incident` | Captured important **adverse** event; incomplete accounting for routine releases |
| Aug | `site:openai.com/index/ Codex after:2026-07-31 before:2026-09-01`; `METR report OpenAI Hugging Face incident August 2026 independent findings` | Official docs and independently scoped METR analysis, not complete incident transcript |
| Sep | `site:openai.com/index/ Codex after:2026-08-31 before:2026-10-01`; `OpenAI Agents API September 2026 pricing capabilities docs openai` | API and DevDay recaps; release-specific platform/geo eligibility incomplete |
| Oct 1–12 | `site:openai.com/index/ Codex after:2026-09-30 before:2026-10-13`; `OpenAI Codex October 2026 site:openai.com/index` | API changelog and GitHub public release metadata; no claims for later dates |
| Cross-month docs | `site:developers.openai.com/codex/changelog/ 2026 July August September October`; `site:platform.openai.com/docs/changelog 2026 July Agents API`; `site:developers.openai.com/api/docs/changelog 2026 July August September October` | Search engines index mutable documentation inconsistently; used live canonical changelog for dated entries |
| Cross-month independent | `Reuters OpenAI Codex 2026 April September coding agent work AWS enterprise`; `TechCrunch OpenAI Codex June September 2026 agent cloud`; `The Register OpenAI Codex security 2026 compromise evaluation August`; `METR report OpenAI Hugging Face incident August 2026 independent findings` | News articles repeating product announcements do not become independent task-validation evidence |
| Product/identity | `OpenAI organization company structure nonprofit OpenAI Foundation public benefit corporation 2026 official`; `OpenAI Codex CLI releases 2026 GitHub openai codex Apache 2 license` | Corporate ownership supported by provider statement; no third-party cap-table review |

**Additional exploratory search groups:** Specific date phrases such as `site:openai.com/index "Codex for almost everything" April 16 2026`, `site:openai.com/index "Agents API" September 10 2026`, `site:metr.org "OpenAI" "Hugging Face" "August 26" 2026`, and direct URL reads of official announcements, safety notices, release tags, and partner/victim records. Some exploratory searches were repeated under different domains; they are not systematically logged at per-hit resolution and cannot support recall estimates.

## Canonical source locations inspected (not a comprehensive crawl)

- Corporate: https://openai.com/our-structure/ ; https://openai.com/codex/
- Product release / news: https://openai.com/index/codex-for-almost-everything/ ; https://openai.com/index/introducing-workspace-agents-in-chatgpt/ ; https://openai.com/index/work-with-codex-from-anywhere/ ; https://openai.com/index/codex-for-every-role-tool-workflow/ ; https://openai.com/index/introducing-the-agents-api/ ; https://openai.com/index/devday-2026-recap/
- Docs/release: https://developers.openai.com/api/docs/changelog ; https://developers.openai.com/api/docs/assistants/migration ; https://github.com/openai/codex/releases/tag/rust-v0.162.1 ; https://github.com/openai/codex/blob/main/LICENSE
- Safeguards/adverse event: https://openai.com/index/running-codex-safely/ ; https://huggingface.co/blog/security-incident-july-2026 ; https://openai.com/index/hugging-face-model-evaluation-security-incident/ ; https://openai.com/index/hugging-face-incident-and-the-road-ahead/ ; https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- Independent industry report: https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/

**Exclusions:**
1. All 2025 restructuring announcements from the **within-window release counts** (they remain baseline identity evidence).
2. Uncorroborated snippets, forecast essays, anonymous speculation, customer testimonials and social reposts from **performance/adoption evidence**.
3. Syndicated or journalistic summaries of the same corporate release as new independent product success or independent event counts.
4. Pages without a verified in-window publication date from the **dated 23-event ledger**; a mutable undated docs page may still support current technical context.
5. Material after **2026-10-12**, regardless of when a page was queried.
6. Published agent capabilities unrelated to observed downstream OSS reuse from the **verified reuse outcome** count.
7. An announced acquisition from the category **completed acquisition** unless a dated independent closing statement is verified.

**Known disputed wording:** [Apr 22 workspace-agent announcement](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) uses both GA and research-preview phrasing; unresolved product-specific availability is recorded as **reported_undetermined**.

## Independent-check and verification requirements before merging

- [x] Check major event dates against at least their listed primary landing pages/changelog; keep dated PDF/HTML revisions if redistributable and permitted.
- [x] Check openai/codex LICENSE and public release-tag metadata via GitHub repository API (2026-10-12): Apache-2.0; rust-v0.162.1 public release metadata dated 2026-10-09.
- [x] Compare July/August provider, affected-party and METR statements, preserving changes in attribution and scope.
- [ ] **Second person** verify direct links, source publication/event dates, every critical characterization and disputed GA/preview claim. This was NOT achieved in this drafting pass.
- [ ] Validate the full CSV schema against the project's canonical method and independently sample the ledger for duplicate event groups, corrected sources, and fact boundaries.
- [ ] Run any suitable automated CSV validation and the repo unit suite in a checked-out branch (not run during this connector-only source-authoring session).
- [ ] Seek a security-domain reviewer to validate the incident summary and prevent scope overgeneralization.
- [ ] Frozen preregistration and independently accepted reuse trials remain a separate 2027 study gate; this document does not substitute for them.

**Immutable evidence caveat:** This is a linked **bibliographic record**, not a full-text archived evidence snapshot. No copyrighted pages were copied in full and no inaccessible source was treated as verified.

**Scientifically safe practical interpretation:** test an offline reuse-first first-use task with independent acceptance, safe sandbox, explicit approval boundary and compatibility regression. Evaluate total reviewer/maintainer cost, not just generated tokens or stars; avoid claims that Codex releases proved climate benefit.
