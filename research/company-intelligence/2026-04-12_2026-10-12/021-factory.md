# Factory — provisional six-month technology intelligence screen (021)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](021-factory.events.csv), [search log](021-factory.search-log.md) and [source-QC note](021-factory.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #88 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 021; [issue #88](https://github.com/MSKazemi/github-trending-1000-study/issues/88).
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened 2026-10-16** (earlier passes 2026-10-12/13/14, see [Earlier screen (preserved)](#earlier-screen-preserved)).
- **Status:** provisional dated documentary screen — **30 ledger rows covering all seven calendar segments** (6 earlier rows, all re-checked and unchanged; 24 new). Not exhaustive retrieval, not independently verified task outcomes, not human-approved. [Study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [factory.com](https://factory.com/) (formerly factory.ai; `factory.ai` paths redirect to `factory.com`), [news index](https://factory.com/news), [CLI/Desktop changelog](https://docs.factory.com/changelog/cli-updates), [GitHub org Factory-AI](https://github.com/Factory-AI) via read-only `gh api`. Grades are company-watch E0–E4, not the [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](021-factory.search-log.md) records every fetch, `gh api` call and the 4 web searches run, per segment, with include/exclude decisions. The earlier screen's statement that April, May, July and early October had no verified event reflected a narrow search, **not** absence: all four segments now hold dated official records. Search result totals are **unknown**, not zero. "Factory" is a generic word; only the Droid maker (factory.com / GitHub `Factory-AI`) was kept, and generic "software/AI factory" hits were excluded. Out of window and excluded: OpenCompute (Oct 14) and the Blackstone case study (Oct 15).

## 2. Identity, ownership and rights baseline

- **Entity:** Factory, a San Francisco company building the **Droid** autonomous software-development agents (CLI, Desktop app, IDE extensions, GitHub/GitLab actions). Search-result-level reporting (S1 in the log) gives founding in 2023; corporate registry and beneficial ownership were **not** checked to filing level. Funding: [$150M Series C at $1.5B, Apr 16](https://factory.com/news/series-c) (Khosla lead, concurred by [counsel's client note](https://www.gunder.com/en/news-insights/client-news/factory-announces-dollar150-million-series-c-at-dollar15-billion-valuation)); [$200M at $5B, Sep 15](https://factory.com/news/5-billion-valuation). Acquisition announced: [Mentlio, Oct 9](https://factory.com/news/mentlio) (closing not stated). No parent company or rename beyond the factory.ai → factory.com domain change was found.
- **Product surface is proprietary SaaS** with a Factory-hosted control plane; [Factory Private](https://factory.com/news/factory-private) (customer VPC/on-prem/air-gapped) is private preview.
- **OSS / licences (GitHub API, 2026-10-16):**

| Repository | Licence detected by GitHub | Note |
|---|---|---|
| [Factory-AI/droid-action](https://github.com/Factory-AI/droid-action) | **none detected** | releases v5–v10 in window |
| [Factory-AI/vfs](https://github.com/Factory-AI/vfs) | **none detected** (licence endpoint 404) | fork of agentfs; v1.0.0 Aug 8 |
| [Factory-AI/factory](https://github.com/Factory-AI/factory) | none detected | created 2026-07-29, no releases |
| [Factory-AI/factory-plugins](https://github.com/Factory-AI/factory-plugins) | none detected | plugin marketplace |
| [Factory-AI/legacy-bench](https://github.com/Factory-AI/legacy-bench) | Apache-2.0 | 10 public tasks |
| [Factory-AI/droid-sdk-python](https://github.com/Factory-AI/droid-sdk-python) / droid-sdk-typescript | Apache-2.0 / NOASSERTION | no tagged releases |
| [Factory-AI/droid-code-review](https://github.com/Factory-AI/droid-code-review), tui-test, pb-gdal-fable | MIT | |
| [Hugging Face factoryai models](https://huggingface.co/api/models?author=factoryai) (Droid Shield 2.0 adapters) | **no licence tag** | open weights, rights unclear |

"No licence detected" means GitHub's API found no recognisable licence file — it is a rights **gap to resolve before reuse**, not a legal conclusion.

## 3. Seven-segment dated chronology

| Segment | In-window evidence (displayed publication date) | Availability / attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 16 Series C](https://factory.com/news/series-c); [Apr 16 droid-action v5 review-depth presets](https://github.com/Factory-AI/droid-action/releases/tag/v5); Apr 21 changelog v0.106.0 full-project security audit mode; [Apr 23 Automated QA](https://factory.ai/news/automated-qa) | Funding is context only; QA "available today in all plans" (vendor) |
| May | [May 8 GHSA-fq7h-9x26-6j22 / CVE-2026-42876 in external-secrets](https://github.com/advisories/GHSA-fq7h-9x26-6j22); May 14 changelog v0.126.0 EU data residency | Factory later (Jun 11) claims its reviews surfaced the CVE — vendor attribution unverified |
| June | [Jun 1 Factory Router](https://factory.ai/news/factory-router) (also at [factory.com](https://factory.com/news/factory-router)); [Jun 11 Automated Security Review](https://factory.com/news/automated-security-review); Jun 12 changelog command blocklist; [Jun 15 Factory 2.0 vision](https://factory.com/news/software-factory); [Jun 17 AutoWiki](https://factory.ai/news/wiki) | Router = private research preview; Factory 2.0 = vision (`announced_only`) |
| July | [Jul 1 Droid Shield 2.0](https://factory.com/news/droid-shield-2-0); Jul 9 changelog macOS whole-process sandbox (+ Jul 23 hardening); [Jul 28 Open Secure AI Alliance](https://factory.ai/news/open-secure-ai-alliance) | Shield 2.0 = research preview; alliance = commitments only |
| August | [Aug 4 City AM unconfirmed >$3.5bn report](https://www.cityam.com/?p=2447558); [Aug 8 vfs v1.0.0](https://github.com/Factory-AI/vfs/releases/tag/v1.0.0); [Aug 18 droid-action v7 CI triage/auto-fix](https://github.com/Factory-AI/droid-action/releases/tag/v7); [Aug 24 model-routing essay](https://factory.com/news/model-routing-belongs-in-the-harness); [Aug 25 Connectors/Personas](https://factory.com/news/personas-and-connectors); [Aug 27 multi-role research](https://factory.com/news/what-it-takes-for-coding-agents-to-complete-large-software-tasks) | City AM figure superseded by Sep 15 ($5B); research n=24, one run per cell |
| September | [Sep 9 Claude Marketplace](https://factory.com/news/claude-marketplace) (+ [Sep 29 OpenAI marketplace](https://factory.com/news/openai-b2b-marketplace)); [Sep 15 $200M/$5B](https://factory.com/news/5-billion-valuation) (restated by [TNW Sep 17](https://thenextweb.com/news/factory-200m-5bn-valuation-ai-coding-agents)); [Sep 18 Factory Private](https://factory.com/news/factory-private); [Sep 23 Router savings 63%](https://factory.com/news/factory-router-inference-savings); [Sep 24 Legacy-Bench](https://factory.com/news/legacy-bench-specialized-intelligence-index); [Sep 30 Automations GA](https://factory.com/news/automations) | Private = private preview; savings are vendor-computed |
| Oct 1–12 | [Oct 2 Analytics](https://factory.com/news/factory-analytics-transparency); [Oct 6 droid-action v10 token-redaction fix](https://github.com/Factory-AI/droid-action/releases/tag/v10); [Oct 9 Mentlio](https://factory.com/news/mentlio); [Oct 12 Environments](https://factory.com/news/droids-now-have-a-fleet-of-sandboxes) | Analytics: Business/Enterprise only; Mentlio closing not stated |

Per-segment row counts: Apr 4 · May 2 · Jun 5 · Jul 3 · Aug 6 · Sep 6 · Oct 4 (= 30). Multiple rows citing the one [changelog page](https://docs.factory.com/changelog/cli-updates) are distinct dated entries, not corroboration.

## 4. Feature map — vendor assertion vs what we could observe

| Cluster | Vendor-documented capability | What we observed ourselves | Non-equivalence |
|---|---|---|---|
| Review & security | Automated QA (Apr), security-review audit modes (Apr–May), STRIDE Automated Security Review (Jun), Droid Shield 2.0 learned secret detection (Jul), Git scanning (Sep changelog) | GHSA for CVE-2026-42876 exists (May 8); droid-action v10 release fixes its **own** token-redaction gap | No detection-rate evidence; one CVE is an anecdote. The v10 fix shows a secret-handling defect in Factory's own CI action |
| Model routing & cost | Router private preview (Jun 1, 20–25%), harness routing essay (Aug 24, 58%), Router savings (Sep 23, 63%), Analytics "Router savings" view (Oct 2), Mentlio acquisition (Oct 9) | None — all figures vendor-computed against vendor-chosen baselines | Three different percentages on three different baselines; not a CO2e or lifetime-cost result |
| Delegation & autonomy | Missions/Droid Computers (changelog), Connectors/Personas (Aug 25), Automations GA (Sep 30), Environments GA (Oct 12), CI triage/auto-fix in droid-action v7 | Releases exist on GitHub with dated notes | Wider tool and data access per agent; unattended runs increase review load |
| Safety controls | Command blocklist (Jun 12), macOS process sandbox (Jul 9/23), org MCP/hooks governance (Jun changelog) | Changelog entries only | Blocklists/sandboxes not tested for bypass |
| Deployment / data | EU data residency (May 14), Factory Private preview (Sep 18) | — | Contracts/DPAs not reviewed |
| Open artifacts | vfs (agent filesystem fork), legacy-bench 10 tasks, Shield adapters on HF, SDKs | Repos/licences via API (§2) | Several have no detected licence |

## 5. Publicly stated direction vs shipped

| Dated source | Stated direction | Classification |
|---|---|---|
| [Jun 15 Factory 2.0](https://factory.com/news/software-factory) | Move "from coding agents to software factories" coordinating Droids, Automations, Droid Computers, Missions, Router | Vision; components shipped piecemeal (Automations GA Sep 30, Environments GA Oct 12) |
| [Aug 24](https://factory.com/news/model-routing-belongs-in-the-harness) / [Oct 9 Mentlio](https://factory.com/news/mentlio) | Routing and token allocation belong in the harness | Router still preview (Jun 1; in Private preview Sep 23); acquisition announced |
| [Jul 28 alliance](https://factory.ai/news/open-secure-ai-alliance) | Open-weight secret detection, responsible disclosure, share research | Weights published; no licence tag on Hugging Face, so reuse terms are unstated |
| [Sep 15 raise](https://factory.com/news/5-billion-valuation) | Invest in research, product, global go-to-market (Japan office Aug 31) | Intent, not delivery |

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company promises)

| Hypothesis | Rival explanation | Disconfirming observation |
|---|---|---|
| Harness-level routing lowers billed cost per **accepted** task | Savings come from task mix/cheaper models that fail more and push cost into review | Matched tasks show equal cost per accepted task or more reviewer minutes |
| Built-in security review reduces shipped vulnerabilities | Existing SAST/secret scanners already catch the same issues | Paired PR fixtures show no extra true positives over CodeQL/gitleaks |
| Reusable sandboxes (Environments) cut setup time | Devcontainers/CI images already provide this | Same-repo setup time and failures equal with plain devcontainers |

## 7. M1–M7 mapping

| Construct | Relevance here (prospective measurement, not a conclusion) |
|---|---|
| **M1** coding-practice change | Delegated, scheduled and multi-role agent workflows (Automations, Missions, Aug 27 research) |
| **M2** accepted task quality | Vendor benchmarks (Aug 27, Sep 24) are not independent acceptance; count all attempts |
| **M3** discoverability | Marketplace listings (Sep 9/29) are procurement channels, not organic discovery |
| **M4** verified third-party reuse | None observed; third-party repos with Droid bot PRs were seen in search but not analysed |
| **M5** reuse-first | Compare droid-action / Automated Security Review against existing CodeQL/gitleaks; licence gaps block reuse of vfs/droid-action |
| **M6** lifecycle human/energy cost | Routing "savings" are price-based; no kWh/CO2e can be derived from tokens |
| **M7** ethical/safe adoption | Token-redaction fix (Oct 6), sandbox/blocklist controls, unlicensed weights |

## 8. One falsifiable reuse-first maintainer experiment (proposal, not executed)

**Question:** does an agent-based PR security review add independently accepted findings over existing free tooling in this repository?

- **Repository:** `MSKazemi/github-trending-1000-study`, offline fixtures only; live Trending capture remains disabled and no Factory feature changes that.
- **Functional unit:** one *seeded-defect PR* — a person other than the implementer freezes 12 synthetic PRs (6 with a planted secret or injection defect, 6 clean) and hidden expected labels before any run.
- **Comparator A (reuse baseline):** existing GitHub CodeQL + gitleaks in CI. **B:** A + Factory Automated Security Review / droid-action at a pinned release (v10 or later), only under purchased/approved terms and with a repo-scoped token.
- **Primary endpoint:** true-positive defects found / 6 and false alarms / 6, per arm, with every timeout or refusal counted.
- **Secondary:** reviewer minutes to triage, billed cost actually invoiced, CI minutes, 30-day maintenance; kWh only if instrumented.
- **Guardrails:** no production secrets; synthetic tokens only; confirm no token text appears in action logs (cf. the v10 fix); licence of droid-action resolved first.
- **Stop rule:** stop and keep A if B finds no additional true positive across the 6 seeded PRs, raises false alarms above A, or any token appears in logs.
- **Expected null:** B adds nothing over A — publish that result as-is.

## 9. Limitations

- Mostly vendor sources (E1) plus vendor-controlled GitHub releases/changelog (E2); second-party items are one GitHub advisory, a law-firm client note and two press articles. No E3 functional replication.
- Displayed publication dates are not archived snapshots; the Series C page was edited after publication.
- The changelog was summarised through a fetch model over a ≈214k-character page; version/date pairs need human re-reading.
- No installation, benchmark run, cost measurement or user study was performed. An AI assistant drafting its own report is not an independent reviewer.

## Earlier screen (preserved)

The previous versions of this report came from [PR #201](https://github.com/MSKazemi/github-trending-1000-study/pull/201) (initial report, with [JSON source observations](021-factory.events.json) left untouched) and [PR #236](https://github.com/MSKazemi/github-trending-1000-study/pull/236) (alternate draft, archived verbatim at [source-archives/021-factory.2026-10-13-first-screen.md](source-archives/021-factory.2026-10-13-first-screen.md)), followed by a 2026-10-14 desk check. Full texts are in git history (commits d1d8e83 … 67443a2) and the archive.

What the earlier screen claimed:
- Search expression `site:factory.com/news 2026 "software factories" "routing" "cost" product; 2026 August September 2026 droid`; result counts not available; April, May, July and Oct 1–12 had "no verified event in this bounded source screen" (now superseded by §3).
- Three E0/E1 leads: [Factory 2.0](https://factory.com/news/software-factory) (2026-06-15, `announced_only`), [model routing in the harness](https://factory.com/news/model-routing-belongs-in-the-harness) (2026-08-24, 58%, `reported_undetermined`), [Router inference savings](https://factory.com/news/factory-router-inference-savings) (2026-09-23, 63%, `preview`); plus three from the alternate draft: [Automated QA](https://factory.ai/news/automated-qa) (2026-04-23, `shipped`), [Factory Router](https://factory.ai/news/factory-router) (2026-06-01, `preview`), [AutoWiki](https://factory.ai/news/wiki) (2026-06-17, `shipped`).
- 2026-10-14 desk check of [Factory Router at factory.com](https://factory.com/news/factory-router): private research preview, vendor 20–25% lower token spend; `factory.ai` paths resolve to `factory.com`.
- Proposed experiment: 6 offline tasks, fixed-model vs cheap-first/escalation routing, independent tests, receipts, reviewer hours; stop if failures/privacy/repair time undermine savings.
- Study anchors cited: [company method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) · [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) · [2027 central mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md) · [reusable-component study](../../../docs/REUSE_FIRST_EXPERIMENT.md).

All six earlier ledger rows passed the 2026-10-16 [source QC](021-factory.source-qc-2026-10-16.md) unchanged.
