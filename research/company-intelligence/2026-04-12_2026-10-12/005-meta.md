# Meta — provisional six-month technology intelligence screen (005)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](005-meta.events.csv), [search log](005-meta.search-log.md) and [source-QC note](005-meta.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review are **pending**. Merging is not scientific or security sign-off; issue [#71](https://github.com/MSKazemi/github-trending-1000-study/issues/71) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 005; [issue #71](https://github.com/MSKazemi/github-trending-1000-study/issues/71). Sector: foundation models and major AI platforms. Study lens: open model distribution and developer ecosystem.
- **Window:** 2026-04-12 through 2026-10-12 inclusive (publication dates); **source-screened 2026-10-12…16**. Exact UTC search times, full search-result counts, immutable page captures and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen — 23 traceable source leads covering all seven calendar segments**; not reviewed by a qualified human. Not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion. [Event ledger](005-meta.events.csv), [segment queries and inclusion/exclusion log](005-meta.search-log.md), [source QC](005-meta.source-qc-2026-10-16.md), [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).
- **Official sources checked:** [Meta newsroom](https://about.fb.com/news/), [Meta AI Research blog](https://research.meta.ai/blog/), [ai.meta.com](https://ai.meta.com/), [Meta developer site](https://dev.meta.ai/), [investor relations releases](https://investor.atmeta.com/), Hugging Face model API, and public GitHub release metadata (`gh api`, read-only). **Claim grading** is company-watch E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The 2026-10-16 pass started from the [Meta AI Research blog index](https://research.meta.ai/blog/) (16 dated posts, Apr 8 – Oct 15), the 2026-10-14 segment queries in [the QA log](source-audits/005-meta.2026-10-14-qa.md), four new web searches, and read-only GitHub release listings for Meta-originated repositories. Every ledger row was opened on a live public page; secondary reports are linked to the vendor event by `duplicate_event_group`, not counted as independent confirmations. **Unopened leads are not counted** (see search log §2/§4: Meta Connect 2026, three September research posts, Bloomberg/TechRadar items, the Reuters original). Out-of-window items excluded: Muse Spark launch (Apr 8, plus its May 12 page revision) and the **Muse Spark Open** open-weight release ([Oct 15](https://research.meta.ai/blog/muse-spark-open)), which belongs to a later window. Missing months would be *unknown*, not zero; here every segment has at least one dated source.

## 2. Corporate/product identity and rights baseline

**Meta Platforms, Inc.** is the reporting entity (quarterly results on [investor.atmeta.com](https://investor.atmeta.com/)). In this window its AI products appear under the **Muse** brand from Meta Superintelligence Labs: Muse Spark 1.1 → 1.2 → 1.3, Muse Wonder / Wonder Full, Muse Image / Video, the Muse personal agent, the **Muse Code** terminal coding agent, the **Meta Model API**, and the Meta Enterprise Platform. Corporate cap-table or filing-level ownership was not checked.

**Open-source/licence boundary (checked items only):**

| Artifact | Licence / access as observed 2026-10-16 | Boundary |
|---|---|---|
| [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) | `apache-2.0`, not gated, revision `a4e59da52a7bc87ae7251dd5545c0dd437c44b68` | Only checked open-weight Muse model in window; drafter/encoder licence not separately stated |
| Muse Spark 1.x, Muse Wonder / Wonder Full | No open-weights statement in the announcements; API / subscription access | Hosted, proprietary terms not inspected |
| Muse Code (CLI) and Muse Code SDK | Licence not stated on the Aug 5 or Aug 31 posts; no public source repo identified | Treat as proprietary until terms read |
| [OGX (formerly Llama Stack)](https://github.com/ogx-ai/ogx) | MIT; `meta-llama/llama-stack` now redirects to `ogx-ai/ogx` after the [Apr 28 rename](https://ogx-ai.github.io/blog/from-llama-stack-to-ogx) | Meta's governance role after transfer **undetermined** |
| [PyTorch](https://github.com/pytorch/pytorch) | BSD-style; governed by the PyTorch Foundation (Linux Foundation) | Meta-originated, not Meta-controlled |
| [FAISS](https://github.com/facebookresearch/faiss), [ExecuTorch](https://github.com/pytorch/executorch) | in-window releases exist (FAISS v1.14.2–v1.15.1; ExecuTorch v1.3.1–v1.5.1) | Noted, not ledgered; licences not re-checked this pass |

## 3. Seven-segment dated chronology

| Segment | In-window dated sources (ledger IDs) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 28 Llama Stack → OGX rename](https://ogx-ai.github.io/blog/from-llama-stack-to-ogx) (006); [Apr 29 Q1 results, capex $125–145B](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx) (007) | Rename is a project-team post; capex is guidance. Apr 8 Muse Spark launch **excluded** (pre-window) |
| May | [May 12 OGX v1.0.0](https://github.com/ogx-ai/ogx/releases/tag/v1.0.0) (008); [May 13 PyTorch 2.12.0](https://github.com/pytorch/pytorch/releases/tag/v2.12.0) (009) | No about.fb.com May post surfaced by search; both rows are OSS releases outside direct Meta control |
| June | [Jun 3 Meta Business Agent](https://about.fb.com/news/2026/06/meta-business-agent) (010); [Jun 15 Facebook AI tools](https://about.fb.com/news/2026/06/new-ai-tools-to-help-you-make-things-happen-on-facebook/) (CI-005-01) | Business Agent mixes now/waitlist/"soon"; Facebook tools are consumer features |
| July | [Jul 7 Muse Image / Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) (011); [Jul 9 Muse Spark 1.1 + Meta Model API public preview](https://research.meta.ai/blog/introducing-muse-spark-meta-model-api) (012); [Jul 24 Meta AI acts](https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/) (CI-005-02); [Jul 29 Q2 results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx) (013) | API is **preview**; Muse Video **announced only**; Jul 24 actions in select markets |
| August | [Aug 5 Muse Code beta + Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) (004); [Aug 6 The Stack report](https://www.thestack.technology/meta-releases-first-coding-agent-reports-first-agentic-hack/) (014); [Aug 10 Muse Glimmer open weights](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) (CI-005-03); [Aug 14 evaluation misconfiguration](https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1) (005); [Aug 31 Muse Code out of beta](https://dev.meta.ai/resources/blog/muse-code-new-plans-and-features) (015) | Beta → out of beta in 26 days; SDK only **developer preview**; Aug 14 is a vendor retrospective of a real third-party-site exploitation during testing |
| September | [Sep 2 Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) (016); [Sep 8 Muse agent](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) (001, status corrected to `shipped`, US); [Sep 9 The Week](https://www.theweek.in/news/sci-tech/2026/09/09/meta-says-its-muse-personal-ai-assistant-which-can-spend-your-money-is-safe-and-secure-is-it.html) (017); [Sep 28 Enterprise Platform](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/) (002); [Sep 29 Global News](https://globalnews.ca/news/12077192/metas-ai-agent-muse-privacy/) (018); [Sep 30 Tailscale connector](https://tailscale.com/blog/meta-muse-ai-agent-tailscale) (019) | Muse page shows a Sep 30 revision; Enterprise Platform is an organisational launch without dated product GA; two critical reports, one partner account |
| Oct 1–12 | [Oct 2 Scaling Framework update](https://research.meta.ai/blog/developing-capable-models-responsibly) (020); [Oct 12 Muse Wonder / Wonder Full](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) (003) | Framework = commitments; Wonder via API/Muse Code only, Muse integration "soon"; **Oct 15 Muse Spark Open excluded** |

Ledger IDs above abbreviate `CI2026-005-NNN`; `CI-005-0N` are the original IDs. `event_date_utc` is blank throughout because no source separately dates the underlying event.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited documents support | Non-equivalence / counter-evidence |
|---|---|---|
| **Muse Code** (Aug 5 beta → Aug 31 out of beta; Sep 2 Spark 1.3; Oct 12 Wonder in Muse Code) | Vendor describes a macOS/Linux terminal coding agent with background subagents, inter-session messaging over a local Unix socket, reusable workflows, event-log rewind, monthly plans and a TypeScript SDK (developer preview) | Benchmarks are vendor-run; [The Stack](https://www.thestack.technology/meta-releases-first-coding-agent-reports-first-agentic-hack/) notes an accusation of obscured comparisons. Price "$5/month" only in [RuntimeWire](https://runtimewire.com/article/meta-muse-code-out-of-beta-monthly-plans), not confirmed in Meta's text. No licence or source repo found |
| **Meta Model API** (Jul 9 public preview) | Developer access to Muse Spark 1.1+, later 1.2/1.3/Wonder | Preview status; pricing, rate limits, data-use terms not inspected |
| **Muse Glimmer** (Aug 10) | Only verified open-weight model in window: 30B, Apache-2.0, ungated on Hugging Face | One model's licence says nothing about Spark/Wonder; runtime behaviour untested |
| **Muse agent** (Sep 8) | Dedicated Secure VM, separate "Sentinel" agent gating internet access, credential isolation, approvals and audit trail; Confidential VM promised "later this year" | [The Week](https://www.theweek.in/news/sci-tech/2026/09/09/meta-says-its-muse-personal-ai-assistant-which-can-spend-your-money-is-safe-and-secure-is-it.html) (via Reuters) reports internal testers found guardrails routed around; [Global News](https://globalnews.ca/news/12077192/metas-ai-agent-muse-privacy/) reports a Marketplace address disclosure and Amazon blocking Muse purchases. Earlier leads: [The Verge, Oct 10](https://www.theverge.com/ai-artificial-intelligence/1009051/privacy-ai-agent-promises-openai-meta-muse-dots) (not re-fetchable 2026-10-16) |
| **Evaluation incident** (Aug 14) | Pre-release Muse Spark 1.1 reached the open internet in a contractor's misconfigured cyber evaluation, exploited a real site and modified its database; Meta reports new isolation checks | Vendor account; contractor and affected party not independently heard; a concrete example that agent sandboxes fail by configuration |
| **Tailscale connector** (Sep 30) | Muse joins the user's tailnet as a node, outbound-only, per-device confirmation | Partner promotional post; cross-reference [099-tailscale](099-tailscale.md) |
| **OSS ecosystem** | OGX 1.0–1.5 (MIT), PyTorch 2.12–2.14.1, FAISS 1.15, ExecuTorch 1.5 released in window | Llama Stack's move to `ogx-ai` with a "neutral" name and PyTorch's foundation governance mean Meta-originated OSS is increasingly **not** Meta-branded; no `meta-llama/llama-models` release in window |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Stated intention | Classification |
|---|---|---|
| [Q1 results, Apr 29](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx) | "on track to deliver personal superintelligence to billions of people"; capex raised to $125–145B | Aspiration + guidance |
| [Q2 results, Jul 29](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx) | capex narrowed to $130–145B | Guidance |
| [Business Agent, Jun 3](https://about.fb.com/news/2026/06/meta-business-agent) | paid subscriptions "in the coming months"; WhatsApp discovery "soon" | Planned, undated |
| [Muse agent, Sep 8](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) | Confidential VM "later this year"; AI-glasses support "coming soon" | Planned; agent itself shipped (US) |
| [Enterprise Platform, Sep 28](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/) | bring the full AI stack to businesses and developers | **Announced only** — no product GA dates |
| [Scaling Framework, Oct 2](https://research.meta.ai/blog/developing-capable-models-responsibly) | sandboxed high-risk RL runs, open-weight release guidance, Board AI committee; more changes "over the coming months" | Commitment, unaudited |
| [Muse Wonder, Oct 12](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) | Wonder "will soon power experiences in Muse"; safety report "available soon" | Planned |

**Direction (attributable):** Meta moved from consumer assistant features (Jun–Jul) to a developer stack — hosted Model API (preview), a paid terminal coding agent with SDK, one Apache-2.0 on-device model — and an enterprise pillar, while its most capable models stayed hosted. Shipped ≠ adopted; all of this is vendor-described.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company forecasts)

| Hypothesis | Rival explanation | Disconfirming observation |
|---|---|---|
| Meta will run a two-tier model: hosted frontier (Wonder) plus selected open weights (Glimmer, Oct 15 Spark Open) for ecosystem reach | Open releases may be one-off competitive responses | No further Apache/permissive Meta model release through 2027, or licence terms tighten |
| Muse Code will compete on price/data-sharing tiers rather than accepted-task quality | Quality may converge with rivals and price becomes irrelevant | Independent frozen-task evaluation shows Muse Code acceptance ≥ peers at equal cost |
| Meta-originated OSS keeps moving to neutral governance (PyTorch Foundation, OGX) | Moves reflect project maturity, not Meta strategy | Meta re-brands or re-acquires control of such projects |

## 7. M1–M7 study relevance

| Construct | Prospective measurement (not an inferred conclusion) |
|---|---|
| **M1** agent workflow | Opt-in logs of Muse Code subagent/workflow use vs a baseline agent on identical tasks |
| **M2** accepted quality and review load | Frozen external acceptance tests; count all attempts; vendor benchmarks excluded |
| **M3** discoverability | Whether OGX's rename changes discoverability vs `llama-stack` references (redirects, package names) |
| **M4** verified third-party reuse | Audited downstream imports of Glimmer weights or OGX, not downloads/likes (HF counters are popularity, not reuse) |
| **M5** reuse vs rebuild | Compare an OpenAI-compatible reusable server (OGX, MIT) against custom glue for a provider-switch task |
| **M6** lifecycle cost | Metered human/CI/runtime time; vendor "25% fewer tokens" is not kWh or CO2e |
| **M7** maintainer intervention | Least-privilege agent configuration as a repository policy, tested with synthetic denial cases |

## 8. One falsifiable reuse-first maintainer experiment

**Repository:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) (offline CLI and synthetic fixtures only; live Trending `capture` remains disabled).

**Practice:** reuse an existing OpenAI-compatible abstraction (pinned [OGX](https://github.com/ogx-ai/ogx) release, MIT) instead of writing a bespoke provider adapter, for an *optional* local model-assisted summary of synthetic fixture output — and keep the model swappable (e.g. a pinned open-weight model such as Muse Glimmer revision `a4e59da5…`).

**Comparator:** A = no new code (existing CLI output read by a human); B = OGX-based adapter; C = hand-written minimal adapter. Same synthetic inputs, same frozen expected JSON, same time cap.

**Acceptance (frozen in advance by a second person):** output equals the frozen expected rows; zero network calls beyond localhost; zero writes outside a temp dir; licence and dependency audit clean; all assigned attempts counted, including failures.

**Verified external-use signal:** an independent outsider reproduces B or C from the README in ≤30 minutes with the same acceptance result.

**Cost:** human minutes, reviewer minutes, dependency count added, CI minutes; no CO2e estimate.

**Stop rule:** drop B if it adds more than 10 transitive dependencies or a failed licence/security check, or if A or C passes acceptance with less review time. **Not run; no effect estimated.**

## 9. Evidence quality, limitations and review checklist

- **Inventory:** 23 rows (8 earlier + 15 added 2026-10-16), all seven segments covered: Apr 2, May 2, Jun 2, Jul 4, Aug 5, Sep 6, Oct 2. A purposive screen, not a census.
- **Evidence classes:** 16 first-party (13 `E1_VENDOR_DOCUMENT_ONLY` + 3 retaining the earlier `E0_ARCHIVED_UNREVIEWED_VENDOR_LEAD` label), 2 GitHub releases plus 1 repo-metadata row (E2), 3 independent news reports (E1-level: reporting, not audits), 1 partner blog. **No E3/E4** — no independent replication of any Meta claim.
- **QC correction:** CI2026-005-001 (Muse agent) status `announced_only` → `shipped` (US rollout stated on page). Details in the [QC note](005-meta.source-qc-2026-10-16.md).
- **Gaps:** Meta Connect 2026 (Sep 23–24) not screened; Muse Code/Model API pricing and terms unread; Reuters, TechRadar and Verge items not read; Axios URLs returned 403; no archived captures; displayed dates are publisher dates (Muse and Wonder pages show later revision dates).
- **Pending:** qualified human factual/link, rights and methods review; independent task trial. No adoption, accepted-code, cost or environmental outcome is claimed.

## Earlier screen (preserved)

The previous version of this report (PR #191 first screen, reconciled with draft PR [#228](https://github.com/MSKazemi/github-trending-1000-study/pull/228), merged 2026-10-15) claimed **5 directly linked dated first-party events** (IDs `CI-005-01`…`CI-005-05` in the [archived 2026-10-12 ledger](source-archives/005-meta.2026-10-12-source-ledger.csv)), later an 8-row canonical CSV. Its exact text is in git history and in [source-archives/005-meta.2026-10-13-first-screen.md](source-archives/005-meta.2026-10-13-first-screen.md); the 2026-10-14/15 query log and secondary-source supplement are in [source-audits/005-meta.2026-10-14-qa.md](source-audits/005-meta.2026-10-14-qa.md). Key earlier statements:

- Months Apr 12–30 and May had "No event documented in this bounded source subset" — now filled (§3).
- The archived ledger labelled the [Enterprise Platform](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/) `shipped` (`CI-005-04`); the canonical CSV (`CI2026-005-002`) uses `announced_only`, re-confirmed on 2026-10-16. Archived `CI-005-05` ↔ canonical `CI2026-005-003` (Muse Wonder).
- "[Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) is directly dated 2026-08-10, and the [published Hugging Face model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) displays Apache-2.0" — re-confirmed; revision SHA now recorded.
- "[Muse Wonder](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) … [Axios on October 12](https://www.axios.com/2026/10/12/meta-new-ai-models-anthropic-openai) provides an independent news account" — Axios returned HTTP 403 on 2026-10-16 (unverified, not refuted); a further lead was [Axios on Sep 8](https://www.axios.com/2026/09/08/meta-debuts-muse-personal-ai-agent).
- "[June 15 Facebook tools](https://about.fb.com/news/2026/06/new-ai-tools-to-help-you-make-things-happen-on-facebook/) primarily concerns consumer social-platform experiences" — re-confirmed.
- [Muse Spark acts across tasks](https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/) — re-confirmed (select markets).
- The earlier [Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent) row was `announced_only`; corrected to `shipped` on 2026-10-16.
- 2026-10-14 additions: [Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) (`preview`) and [Aug 14 evaluation response](https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1) (`reported_undetermined`) — both re-confirmed.
- QA-log leads not promoted: [Muse Spark Apr 8 page](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/) (pre-window), [Verge, Oct 12 Wonder Full](https://www.theverge.com/ai-artificial-intelligence/1009479/meta-muse-wonder-full-ai-model) and [Verge, Oct 10 privacy](https://www.theverge.com/ai-artificial-intelligence/1009051/privacy-ai-agent-promises-openai-meta-muse-dots) (not fetchable 2026-10-16).
- The earlier experiment compared the existing CLI with a reusable model-assisted task-plan template under frozen acceptance tests; §8 keeps that frozen-acceptance design and makes the reuse comparator concrete.
- Cross-link: distinct validated articles may enter the [#56 news corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) only after its own verification; no `NEWS-` ID is minted here.
