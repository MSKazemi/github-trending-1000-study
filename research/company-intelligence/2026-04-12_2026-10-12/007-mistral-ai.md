# Mistral AI — provisional six-month technology intelligence screen (007)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](007-mistral-ai.events.csv), [search log](007-mistral-ai.search-log.md) and [source-QC note](007-mistral-ai.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. Merging is not scientific or security sign-off; issue #73 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 007; [issue #73](https://github.com/MSKazemi/github-trending-1000-study/issues/73). Sector: foundation models and major AI platforms. Study lens: open-weight and deployable model alternatives; models, Codestral/Devstral, Mistral Code/Vibe agents.
- **Window:** 2026-04-12 through 2026-10-12 inclusive (calendar publication dates); **source-screened on 2026-10-16** (earlier screen as-of 2026-10-12/13). Exact UTC search-run times, complete search-engine result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen (24 traceable source leads covering all seven calendar segments); not reviewed by a qualified human; factual/link, source-access/rights and methods review pending**. Not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion.
- **Official sources checked:** [Mistral news index](https://mistral.ai/news/), [docs changelog](https://docs.mistral.ai/getting-started/changelog/), [security advisories](https://docs.mistral.ai/resources/security-advisories), GitHub releases of [mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe), GitHub/Hugging Face licence metadata. **Methods:** [company-source protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md); [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). **Claim grading** is company-watch E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The rendered [news index](https://mistral.ai/news/) listed **24 distinct in-window posts** (Apr 12–30: 1; May: 8; Jun: 2; Jul: 3; Aug: 4; Sep: 5; Oct 1–12: 1); the [docs changelog](https://docs.mistral.ai/getting-started/changelog/) listed 9 in-window entries; the GitHub API listed **54 `mistral-vibe` releases** in window; and Mistral's advisory page listed **2** in-window advisories. The 24 ledger rows are a **purposive selection** for the coding-agent / open-weight / reuse lens plus security, retirements and corporate events. Robotics (Robostral Navigate), Physics-AI research posts, HUMAIN and Cloudera partnerships were screened by title and excluded from rows. Counts are from single fetches on 2026-10-16 and can change. Independent coverage was thin and mostly relayed vendor claims; two security items have genuine second-party sources (LiteLLM's May 12 post; HiddenLayer as CVE numbering authority). Absence of a row is **not** evidence that nothing else shipped. Full query table: [search log](007-mistral-ai.search-log.md).

## 2. Corporate/product identity and rights baseline

**Mistral AI** describes itself as a European technology company (Sep 8 funding post); legal form, headquarters and any parent were **not** verified from filings in this screen. On [Sep 8](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) it announced a **€3B Series D** at a post-money valuation above €21B led by Samsung Electronics (corroborated for amount and lead by [Techzine](https://techzine.eu/news/applications/144116/mistral-raises-3-billion-samsung-leads-round); the article itself shows no date). It signed a definitive agreement to acquire **Emmi AI** on [May 23](https://mistral.ai/news/accelerate-ai-native-industry/) (closing not stated on that page; a Sep 28 [Munich-hub post](https://mistral.ai/news/hallo-deutschland/) says the acquisition happened in May). Cap-table and filing-level ownership were **not** checked.

**Brands in scope:** *Vibe* (since [May 28](https://mistral.ai/news/vibe-agent/) the umbrella agent: Le Chat is "now Vibe", with Work Mode, Code Mode, VS Code extension and the Vibe CLI); *Mistral Studio* (API platform with Connectors, Workflows, prompt/skill registry); models (Medium 3.5, Large 4 preview, Leanstral 1.5, OCR 4/4.1, Shieldstral). **Codestral/Devstral:** the docs changelog shows **no in-window Codestral or Devstral entry** (latest Devstral entry reported as January 2026), and the Vibe and legacy-migration posts name no specific coding model; current status of those brands is therefore **unknown**, not "discontinued". "Mistral Code" was not searched separately (not executed; see log).

**Licences (as read 2026-10-16):** GitHub `license.spdx_id` — [mistral-vibe](https://github.com/mistralai/mistral-vibe) Apache-2.0; client-python, mistral-inference, mistral-common Apache-2.0; search-starter-app MIT. Model weights — [Leanstral 1.5](https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B) and [Shieldstral](https://huggingface.co/mistralai/Shieldstral-1.0-3B) Apache-2.0; [Medium 3.5](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) a "Modified MIT" licence (HF tag `other`; terms **not reviewed**); Large 4 weights **not released** in window and licence **unstated**. Open SDKs/CLI and some open weights do **not** make the hosted Studio, Workflows control plane, Vibe cloud sandboxes or OCR models open source.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (displayed dates; ledger IDs) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Vibe CLI v2.8.0, Apr 21](https://github.com/mistralai/mistral-vibe/releases/tag/v2.8.0) (-07); [Workflows public preview, Apr 27](https://mistral.ai/news/workflows/) (-01); [docs changelog: Medium 3.5 open weights, Apr 28](https://docs.mistral.ai/getting-started/changelog/) (-09) | Workflows is preview on a Mistral-hosted Temporal control plane; Medium 3.5 date conflicts with May 22 post |
| May | [Connectors in Studio, May 22](https://mistral.ai/news/connectors/) (-02, **corrected to preview**); [Remote agents + Medium 3.5, May 22](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5/) (-08); [MAI-2026-002 SDK supply-chain compromise, May 12](https://docs.mistral.ai/resources/security-advisories/MAI-2026-002) (-10); [Emmi agreement, May 23](https://mistral.ai/news/accelerate-ai-native-industry/) (-22); [Vibe unified agent, May 28](https://mistral.ai/news/vibe-agent/) (-03); [Search Toolkit preview, May 28](https://mistral.ai/news/search-toolkit/) (-21) | Malicious `mistralai` 2.4.6 (PyPI) and `@mistralai/*` npm versions were published by a third-party worm, removed within hours |
| June | [OCR 4, Jun 23](https://mistral.ai/news/ocr-4/) (-13); [connector admin controls and scoped keys GA, Jun 24](https://mistral.ai/news/more-control-over-connectors/) (-11) | OCR benchmarks vendor-run; connectors-in-Workflows still preview |
| July | [Leanstral 1.5 Apache-2.0 weights, Jul 2](https://mistral.ai/news/leanstral-1-5/) (-12); [prompt/skill system of record, Jul 9](https://mistral.ai/news/manage-prompts-and-skills-in-studio/) (-04) | Changelog dates Leanstral Jun 30; OCR 4.1 Jul 16 noted only |
| August | [Shieldstral, Aug 4](https://mistral.ai/news/shieldstral/) (-14); [regional endpoints GA + compute direction, Aug 11](https://mistral.ai/news/regional-inference-open-models-new-compute/) (-15, -05); [Agentic Search, Aug 20](https://mistral.ai/news/agentic-search/) (-16) | 1 GW by 2030 is a plan (announced_only) |
| September | [€3B Series D, Sep 8](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) (-17); [legacy Fortran→C++ case study, Sep 9](https://mistral.ai/news/legacy-code-modernization/) (-23); [MAI-2026-003 Vibe shell-permission CVEs, Sep 14](https://docs.mistral.ai/resources/security-advisories/MAI-2026-003) (-18); [Firefox Smart Window beta, Sep 16](https://mistral.ai/news/mistral-x-mozilla/) (-19); [changelog: Leanstral and OCR 4.0 API retirements, Sep 29](https://docs.mistral.ai/getting-started/changelog/) (-20) | CVEs published by HiddenLayer Sep 11; fix in Vibe 2.25.4 (Sep 12) |
| Oct 1–12 | [Large 4 public preview, Oct 6](https://mistral.ai/news/mistral-large-4/) (-06); [Vibe v2.26.0, Oct 6](https://github.com/mistralai/mistral-vibe/releases/tag/v2.26.0) (-24) | Weights promised "by the end of the month"; none on Hugging Face at access (Oct 16). Timestral (Oct 15) **excluded** |

`event_date_utc` is filled only where the source states a distinct date (release timestamps; advisory upload/CVE dates). Different first-party pages give different dates for Medium 3.5 and Leanstral 1.5; both are kept and **not resolved by guess**.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited document supports | Important non-equivalence or counterexample |
|---|---|---|
| Workflows (-01) → Connectors (-02) → connector governance (-11) → prompt/skill registry (-04) | Mistral rebuilt little of the orchestration core: Workflows is "built on Temporal's durable execution engine"; connectors use MCP; registry gives immutable versions, owners, audit logs | Mistral-hosted control plane + customer workers moves, not removes, operational burden; connectors were **preview** in May, controls GA only in June |
| Vibe CLI releases (-07, -24), remote agents (-08), unified Vibe (-03) | Apache-2.0 CLI with ~54 in-window releases; skills, MCP connectors, cloud sandboxes ending in PRs | Release cadence is not quality; remote agents need repository credentials in a vendor sandbox |
| [MAI-2026-003](https://docs.mistral.ai/resources/security-advisories/MAI-2026-003) (-18) + [CVE-2026-87984 record](https://app.opencve.io/cve/CVE-2026-87984) | Permission checks "did not account for all command syntax, options or file paths"; prompt-injected content could trigger unapproved shell commands; fixed 2.25.4 | Vendor rates High, CNA rates CVE-2026-87984 9.3 Critical (CVSS 4.0); one CVE was introduced in 2.15.0 and only partly fixed in 2.20.0/2.23.0 — **agent approval prompts are not a security boundary by themselves** |
| [MAI-2026-002](https://docs.mistral.ai/resources/security-advisories/MAI-2026-002) (-10) + [GHSA-wx9m-wx4f-4cmg](https://github.com/mistralai/client-python/security/advisories/GHSA-wx9m-wx4f-4cmg) + [LiteLLM](https://docs.litellm.ai/blog/mistral-supply-chain-attack-may-2026) | `mistralai` 2.4.6 was uploaded outside the repo's Trusted-Publishing pipeline and ran a credential-harvesting dropper on import (Linux); LiteLLM was unaffected because it calls the HTTP API without importing the SDK | Strong concrete case for **pinning, hash-locking and minimal dependencies**; no exposure counts available |
| Open weights: Medium 3.5 (-08/-09), Leanstral 1.5 (-12), Shieldstral (-14) | Real downloadable artifacts with stated licences | Leanstral's **hosted API was retired Sep 30** (-20) ~3 months after launch while weights remain — the open artifact, not the endpoint, is the durable reuse unit |
| Large 4 (-06) | Public-preview API; 1T total / 52B active (vendor) | Weights not released in window; secondary leads cite 49B active (unresolved); no independent benchmark found |
| Agentic Search (-16), Search Toolkit (-21) | Reuses an existing index with five generic tools; toolkit called "open source", public preview | Benchmarks vendor-run; no toolkit licence/repo linked; starter app created after the post date |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Company-stated intention | Current research classification |
|---|---|---|
| [Large 4, Oct 6](https://mistral.ai/news/mistral-large-4/) | "We will release the weights by the end of the month" | **announced, not delivered** in window |
| [Regional inference, Aug 11](https://mistral.ai/news/regional-inference-open-models-new-compute/) and [Munich hub, Sep 28](https://mistral.ai/news/hallo-deutschland/) | European Compute Units; "up to 1 GW of capacity by 2030"; third-party open models "will" be supported starting with GLM-5.2 | **plan**; GLM-5.2 later appears in the changelog (deprecated Sep 29 in favour of GLM 5.3), so third-party hosting did ship in some form |
| [€3B raise, Sep 8](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) | Scale research and compute; "open-weight models, the infrastructure and the compute capacity" as one stack | **financing**, no specific open-weight release commitment |
| [Mozilla, Sep 16](https://mistral.ai/news/mistral-x-mozilla/) | UK and Germany "expected to follow later this year" | **beta** in France/North America; expansion announced only |
| [Vibe, May 28](https://mistral.ai/news/vibe-agent/) | Slack triggering "coming in June"; Le Chat chat mode sunset "soon" | not verified as delivered |

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company commitments)

| Testable scenario | Rival explanation | Disconfirming observation |
|---|---|---|
| Deployable open weights (Apache-2.0 / modified-MIT) let maintainers pin a model and replay agent tasks reproducibly | Hosted-only previews, licence riders and short endpoint lifetimes erase the advantage | Pinned local replay of the same tasks diverges or costs more to maintain than a hosted API |
| Vendor-built orchestration on existing OSS (Temporal, MCP) reduces bespoke agent glue | Lock-in to a hosted control plane and preview APIs that change | Teams using plain Temporal/CI achieve the same acceptance rate with less setup |
| Agent CLIs with approval prompts become safe defaults | Shell-permission parsing is inherently incomplete (MAI-2026-003) | Sandboxed/OS-level isolation shows no fewer unapproved writes than prompt-based approval |

## 7. Mapping to the study's M1–M7 objectives

| Construct | Prospective measurement, not inferred conclusion |
|---|---|
| **M1** agent/workflow change | Consented, version-pinned task records with Vibe CLI/remote agents vs current practice; feature availability is **not adoption** |
| **M2** accepted quality and review load | Frozen external acceptance suite; count failures and review minutes for **all assigned tasks**; include permission-boundary tests (cf. MAI-2026-003) |
| **M3** discoverability | Not addressed by these sources beyond distribution channels (Firefox, Vibe); measure with matched repo controls |
| **M4** independent reuse | Audited outsider use of open weights/CLI; HF downloads and GitHub stars are insufficient |
| **M5** reuse vs rebuilding | Workflows-on-Temporal and Agentic-Search-on-existing-index are vendor examples of reuse; test against direct OSS use with licence/provenance/supply-chain checks (cf. MAI-2026-002) |
| **M6** lifecycle cost | Endpoint retirements (-20), preview churn, dependency incidents and human review minutes per functional unit; kWh only if metered |
| **M7** maintainer intervention | Ethics-reviewed, opt-in dependency-hygiene or agent-sandboxing intervention with independent first-use tasks |

These are **measurement targets**, not observed M1–M7 effects.

## 8. One falsifiable reuse-first maintainer experiment

**Repository:** [GitHub Trending 1000 Study](https://github.com/MSKazemi/github-trending-1000-study) (offline CLI and synthetic fixtures only; live Trending capture stays disabled under the source-access decision).

**Practice to test:** *Call a model provider through the smallest existing dependency surface* — a standard-library (`urllib.request`) HTTPS call, adding no new package — versus adding a vendor SDK. Motivated by MAI-2026-002 (LiteLLM unaffected because it did not import the SDK) and by Workflows' reuse of Temporal rather than custom orchestration.

**Comparator:** A = add the vendor SDK (`mistralai`, latest stable, version-pinned with hashes); B = no new dependency, a ≤40-line wrapper over an existing HTTP client. Same frozen synthetic prompt set, same model ID, same offline-mocked responses for tests.

**Freeze before treatment:** repository SHA, lockfile, 10 synthetic tasks with independently authored hidden acceptance tests (schema, error handling, timeout, retry, no secret in logs), task/time cap. No real API keys in Git; live calls only with an explicitly authorised throwaway key.

**Primary outcome:** tasks independently accepted / **all 10 assigned**, including failures. **Secondary:** new transitive dependencies (count), lockfile lines, `pip-audit`/advisory hits, human minutes to implement and review, 30-day maintenance events (version bumps, breaking changes, advisories).

**Stop rule:** stop B if it fails >1 acceptance test that A passes or needs >2× A's review minutes; stop A on any unpinned upgrade or advisory hit. Prefer the arm with equal acceptance and smaller dependency surface; a **null result is a valid outcome**. Prospective; **not run**; sample is small and illustrative, not powered.

## 9. Evidence quality, limitations and review state

- **Inventory:** 24 dated rows (E1 first-party announcements; E2 for GitHub releases, changelog entries, advisories and HF artifacts). No E3/E4 evidence: no independent benchmark, controlled replication or adoption measure was found.
- **Corrections in this upgrade:** CI-007-02 status `shipped` → `preview` (page says "Public Preview"); CI-007-05 limitation scoped to the compute direction, with GA regional endpoints as new row -15. See [source-QC note](007-mistral-ai.source-qc-2026-10-16.md).
- **Unresolved:** Medium 3.5 and Leanstral 1.5 release-day conflicts; Large 4 active-parameter conflict and weight licence; Medium 3.5 "Modified MIT" terms; Search Toolkit licence; Emmi closing; independent critical or regulatory reporting (queries not executed); Codestral/Devstral/"Mistral Code" status.
- **Not demonstrated:** feature efficacy, benchmark validity, customer/OSS adoption, cost savings, kWh/CO2e or causal environmental benefit. Funding and release counts are not usefulness evidence.
- **Pending:** independent human factual/link spot-check, source-access/rights review, methods review, licence-text reading, and the prospective experiment.
- **Cross-link:** distinct verified articles (e.g. the LiteLLM and Techzine pages) may enter the [#56 news corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) after its own verification; no `NEWS-` ID is minted here.

## Earlier screen (preserved)

The first screen was produced in commits 177c7e3, 10e3798, d3e4b56 and 30b684e and merged via **PR #193** ("research(007): evidence-graded Mistral AI company screen (#73)"); its full text is in git history. It was an "INITIAL source-screened draft" as of 2026-10-12 with a 2026-10-13 documentary recheck. Summary of what it claimed:

- **Six events:** [Workflows](https://mistral.ai/news/workflows/) (Apr 27, preview); [Studio connectors](https://mistral.ai/news/connectors/) (May 22, recorded as *shipped* — **corrected to preview** on 2026-10-16); [Vibe agent](https://mistral.ai/news/vibe-agent/) (May 28); [managed prompts and skills](https://mistral.ai/news/manage-prompts-and-skills-in-studio/) (Jul 9); [regional inference and compute direction](https://mistral.ai/news/regional-inference-open-models-new-compute/) (Aug 11, announced_only); [Large 4 public preview](https://mistral.ai/news/mistral-large-4/) (Oct 6). Official entry point: https://mistral.ai/news/.
- **June and September** were recorded as "no event documented in this bounded source subset"; this upgrade found dated official events in both (OCR 4 and connector controls in June; five September rows).
- It listed four **reproduction search suggestions** (not executed logs): `"Mistral AI" after:2026-04-11 before:2026-10-13 agent coding open weights`; `site:mistral.ai 2026 model launch agents`; `"Mistral AI" 2026 developer API security pricing`; `"Mistral AI" 2026 independent benchmark and criticism`.
- Its 2026-10-13 recheck highlighted Workflows "built on Temporal's durable execution engine" with a Mistral-hosted control plane and customer Kubernetes workers, and Large 4 "52B active parameters" with weights only promised; both are confirmed by the 2026-10-16 QC.
- Its pilot proposed comparing a bespoke orchestration wrapper with versioned declarative task specs, and evaluating an existing Temporal integration before any custom orchestration; that idea is retained as background to the experiment in §8.
