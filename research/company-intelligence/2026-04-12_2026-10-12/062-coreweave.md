# CoreWeave: provisional six-month technology intelligence screen (062)

> **PROVISIONAL, AI-assisted, not reviewed by a human (2026-10-16).** This report, its [event ledger](062-coreweave.events.csv) and its [search log](062-coreweave.search-log.md) are an AI-assisted first pass at documentary source leads. It is a provisional screen. The issue may be closed with this status recorded. The human factual/link, rights and methods review gates remain open. It is not a scientific, financial or security sign-off.

- **Company watchlist ID:** 062. **Research issue:** [#130](https://github.com/MSKazemi/github-trending-1000-study/issues/130). **Evidence corpus link:** [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). Verified, non-duplicate leads from the ledger may be proposed for #56 only after a human has read them.
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. **Sources accessed:** 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / *pending* / *pending*.
- **Status:** screened (provisional). The ledger holds **31 dated source records** covering all seven calendar segments (Apr 4, May 6, Jun 5, Jul 3, Aug 3, Sep 8, Oct 2). It is a purposive selection, not a census of CoreWeave activity.
- **Source coverage:** newsroom (40 newest articles read), blog, docs release-notes index, GitHub API, investor-relations releases (through WebFetch), and selected independent trade, finance and benchmark sources. **SEC EDGAR is not cited** because it could not be accessed in a compliant way (see the [search log](062-coreweave.search-log.md) section 4). Search result counts and UTC run times are unavailable. **Grades** are the company-watch E0–E4 tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Query / channel | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16, time not captured | coreweave.com/news | listing plus the 40 newest articles | 40 | 40 | 14 rows (+3 used as checks) | 16 in-window customer, marketing or minor items; 7 pre-window | Listing-page date strings unreliable, so article datelines were used |
| same | docs.coreweave.com llms.txt | dated release-note index | 21 in window | 21 | 6 rows (+2 used as checks) | 13 minor | Docs pages can be edited after publication; no archived snapshots |
| same | coreweave.com/blog | listing plus 8 posts | n/a | 8 | 5 rows from 4 posts | 3 used only as checks or narrative | Not every blog post was opened |
| same | GitHub API | 6 repositories | 6 | 6 | 1 row (+1 check) | release counts used as context only | Stars and releases are not adoption |
| same | web search (one engine) | 17 run + 1 not run (budget exhausted) | unknown | ~45 result links | 6 independent or secondary pages used | see search log | No result counts exposed; US-centric results |

## 2. Verified company/product identity and baseline

**CoreWeave, Inc.** is listed on **Nasdaq as CRWV**, per every 2026 release dateline. Releases are datelined Livingston, N.J. It describes itself as "The Essential Cloud for AI". The 2026-06-12 release says it joined the Nasdaq-100 just over a year after its IPO. As of 2026-10-12, no in-window source names a parent company or a change of control. Beneficial ownership was **not** checked at filing level because EDGAR was not accessible.

The offering covers four layers:

- **GPU/CPU infrastructure:** CoreWeave Kubernetes Service (CKS), SUNK (Slurm on Kubernetes), AI Object Storage with LOTA caching, and Mission Control.
- **Development and serving layer:** marketed since 2026-09-30 as **CoreWeave Forge**. It includes Weights & Biases (W&B) Models and Weave, ARIA, Sandboxes, serverless RL/SFT, Serverless and Dedicated Inference, Registry, and Notebooks built on the open-source marimo project.
- **Coding-agent integrations:** a Mission Control MCP server and the CoreWeave Skills package.
- **Services:** Physical AI Field Engineering.

**Acquired brands (baseline, before the window):** the newsroom index lists acquisition releases for **Weights & Biases**, **OpenPipe**, **marimo** and **Monolith**, plus a proposed acquisition of **Core Scientific**. The Sep 30 Forge release confirms that W&B, OpenPipe post-training expertise and marimo are now part of Forge. The Sep 10 Physical AI release confirms the "team and methods CoreWeave acquired with Monolith AI". Acquisition dates and the outcome of the Core Scientific deal were **not re-verified** here. The open-source repositories `marimo-team/marimo` (Apache-2.0), `wandb/weave` (Apache-2.0), `wandb/wandb` (MIT) and `OpenPipe/ART` (Apache-2.0) remain public, with 19, 14, 10 and 1 in-window releases respectively per the GitHub API. Those counts are maintenance activity, not adoption.

**Baseline excluded from window counts:** the Meta $21B expansion (2026-04-09), the Anthropic multi-year agreement (2026-04-10), and a securities class action filed in January 2026 over 2025 data-center delays. The class action's allegations are unproven, and its in-window procedural status could not be verified without EDGAR.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Jane Street ~$6B commitment plus $1B equity (001). Cross-cloud LOTA/SUNK Anywhere (002, preview). Interconnect (003, announced only). CEO letter: 8+ GW by 2030 (004, intention) | [news](https://www.coreweave.com/news/jane-street-signs-6-billion-ai-cloud-agreement-with-coreweave), [blog](https://www.coreweave.com/blog/coreweave-announces-new-capabilities-to-simplify-cross-cloud-ai), [letter](https://www.coreweave.com/blog/coreweave-2025-annual-report-shareholder-letter) | [Reuters via Yahoo](https://finance.yahoo.com/sectors/technology/articles/jane-street-signs-6-billion-125224786.html) (7% discount) | April high-yield notes dropped (no compliant source) |
| 2026-05 | Q1 results (005). Kimi K2.6 benchmark claim (006). Sandboxes (007). $3.1B DDTL 5.0 at SOFR+4.50% (008). Critical capital-intensity commentary (009). Training-to-inference loop: Serverless RL, Weave, W&B Skills/MCP (010) | [IR Q1](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/default.aspx), [Sandboxes](https://www.coreweave.com/news/coreweave-sandboxes-launches-to-accelerate-reinforcement-learning-agent-tool-use-and-model-evaluation) | [24/7 Wall St. via Yahoo](https://finance.yahoo.com/markets/stocks/articles/coreweave-raised-20-billion-capital-144406639.html) | Kimi dateline reads "2025" (conflict) |
| 2026-06 | Vera Rubin bring-up (011). MLPerf Training v6.0 (012). Kimi K2.7 Code serving (013). Sweden/Conapto "renewable" capacity (014). ARIA plus Weave agent GA (015) | [VR](https://www.coreweave.com/news/coreweave-completes-industry-first-bring-up-of-nvidia-vera-rubin-nvl72), [MLPerf](https://www.coreweave.com/news/coreweave-sets-new-ai-training-records-in-mlperf-r-training-v6-0-training-deepseek-v3-in-approximately-two-minutes) | [MLCommons results repo](https://github.com/mlcommons/training_results_v6.0/tree/main/CoreWeave) | Energy-efficiency figures are NVIDIA claims |
| 2026-07 | SUNK v8.0.0 breaking re-architecture (016). Ratepayer Protection Pledge (017). Leidos sovereign-cloud intent (018) | [SUNK 8.0](https://docs.coreweave.com/release-notes/sunk-8-0.md) | none found | Gartner Visionary is vendor-only. Two incidents reported by status aggregators were inaccessible (E0) |
| 2026-08 | Indonesia 360 MW for 2028 (019). Login methods GA (020). Q2 results (021) | [IR Q2](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx) | [MarketBeat call summary](https://www.marketbeat.com/instant-alerts/coreweave-q2-earnings-call-highlights-2026-08-11/) | Q2 capex figures conflict between secondary sources |
| 2026-09 | coreweave/skills v0.2.0 (022). FOCUS usage export (023). Multi-rack Vera Rubin and storage tiers (024). $3.7B 2.875% convertible (025). ClusterMAX 3.0 (026). Mission Control Agent preview and MCP GA (027). **Forge** (028). Vera Rubin limited availability (029) | [Forge](https://www.coreweave.com/news/coreweave-forge-launches-turning-the-ai-loop-production-run-into-a-better-model-and-agent), [MC Agent](https://docs.coreweave.com/release-notes/mission-control-agent.md) | [SemiAnalysis](https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard), [Data Center Knowledge](https://www.datacenterknowledge.com/ai-data-centers/coreweave-targets-enterprises-with-forge-platform) | Fully Connected conference (vendor event) |
| 2026-10-01..12 | India 240 MW for mid-2028 (030). **CoreWeave Skills public preview** for coding agents (031) | [India](https://www.coreweave.com/news/coreweave-enters-india-expanding-ai-cloud-platform-with-adaniconnex), [Skills](https://docs.coreweave.com/release-notes/coreweave-skills.md) | [CRN Asia](https://www.crnasia.com/india/news/2026/coreweave-brings-240-mw-ai-cloud-capacity-to-india-with-adaniconnex) | Q3 results fall after the window |

## 4. Dated event evidence and capabilities (feature inventory)

All rows are listed in the [CSV](062-coreweave.events.csv). The clusters below separate what a vendor asserted from what someone else could check.

| Capability cluster | What the cited document supports | Availability and limits | Independent check | Grade |
|---|---|---|---|---|
| **Coding-agent integrations:** W&B Skills/MCP (010), Mission Control MCP (027), CoreWeave Skills (022, 031) | Agent Skills for Claude Code and similar agents: create a CKS cluster, add node pools, deploy self-managed vLLM, load models, verify GPU workloads. The MCP server is GA. The Mission Control Agent runs with the signed-in user's permissions, and its write tools are not self-serve | Skills: public preview (2026-10-09), v0.2.0 tags (2026-09-02). **Licence is proprietary** ("CoreWeave Skills License", all rights reserved): no redistribution, no derivative works for third parties, no outside contributions. The GitHub API reports `NOASSERTION` | Repo metadata, LICENSE and releases read through the GitHub API. **No task-success evaluation exists**. The repo contains vendor-authored `evals/` | E2 documentary |
| **Agent and RL execution:** Sandboxes (007), Serverless RL (010), ARIA (015), Agent Lens and RL Rollouts (028) | Isolated per-run environments with a Python SDK, either on CKS or serverless through W&B. Serverless RL is claimed to be "up to 40%" cheaper and "~1.4x" faster. Agent Lens is claimed to detect "20 percent more critical failures" | Sandboxes and ARIA were relabelled "now generally available" on Sep 30. RL Rollouts and Model Distillation are in preview | None: every efficiency figure is a footnoted vendor benchmark against unnamed baselines | E1 |
| **Model serving:** Kimi K2.6 (006), K2.7 Code (013), Dedicated Inference (005, Q1 mention) | Serverless per-token open-weight endpoints and dedicated deployments with bring-your-own weights. The Kimi K2.6 chart shows 205 output tokens/s at 10k input tokens, "accurate as of 5/11/2026" | Point-in-time third-party leaderboard positions, quoted by the vendor | The Artificial Analysis pages themselves were not retrieved | E1 |
| **Training scale:** MLPerf v6.0 (012), Vera Rubin (011, 024, 029) | Claimed DeepSeek-V3 671B training in 2.02 min on 8,192 GB300 GPUs. Vera Rubin NVL72 in limited availability in US-CENTRAL-09A | The MLCommons repo **confirms** a CoreWeave closed-division "Available cloud" system of 2,048 nodes × 4 GB300 with a `deepseekv3_671b` result. The time was **not recomputed** | [MLCommons](https://github.com/mlcommons/training_results_v6.0/tree/main/CoreWeave) | E2 (partial) |
| **Operations, identity and metering:** SUNK v8 (016), login methods (020), FOCUS export (023), ClusterMAX (026) | SUNK 8.0 warns that a plain `helm upgrade` from 7.x can delete accounting data. FOCUS exports hourly **usage quantities only**, with no cost or energy fields | ClusterMAX 3.0 rates CoreWeave Platinum, but **Nebius now shares that tier**. SemiAnalysis also reports CoreWeave saying head nodes ran out of memory while a remote-controlled Claude agent orchestrated a cluster | [SemiAnalysis](https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard) (partly paywalled) | E2 |
| **Cross-cloud:** LOTA Cross-Cloud, SUNK Anywhere, Interconnect (002, 003) | Caching and scheduler portability across clouds, plus a private Google Cloud link | LOTA is in limited availability. Interconnect was "private preview soon" in April and is listed as launched in Q2, with no dated preview start | none | E1 |
| **Capacity, energy and finance:** 001, 004, 005, 008, 009, 014, 017, 019, 021, 025, 030 | Q2 2026 revenue $2,575M, net loss $(626)M, interest expense $(640)M, backlog ~$104B, 1.5 GW active power. Debt financing includes SOFR+4.50% and 2.875% convertible notes. New capacity is announced for 2028 (Indonesia 360 MW, India 240 MW). A "renewable" Swedish capacity claim | Contracted power and backlog are not delivered capacity or usage. **No metered energy, PUE or emissions figures were found in any in-window source** | Reuters (Jane Street), MarketBeat (call), 24/7 Wall St. (critical) | E1 (E0 commentary) |

**Contrary and critical evidence:**

- Capital intensity and leverage are the dominant critical theme. See the 24/7 Wall St. commentary of May 19 and the high interest expense in both quarterly releases.
- Customer concentration and pending shareholder litigation are known risk themes. Their in-window filing details were **not** cited because EDGAR was inaccessible.
- SemiAnalysis's agentic-operations anecdote is a concrete failure mode for coding agents operating clusters.
- No first-party incident history was obtainable, and two status-aggregator incident pages returned 403.

**Security:** this screen found no in-window CoreWeave security advisory. That is unknown, **not zero**, because no public advisory index was located.

## 5. What the company says it intends to do

| Public direction (paraphrase or ≤25-word quote) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| "adding more than 5 gigawatts of additional data center capacity ... a total of 8 plus gigawatts of active power by 2030" | [CEO letter, 2026-04-22](https://www.coreweave.com/blog/coreweave-2025-annual-report-shareholder-letter) | 2030 | objective (tentative) | Depends on financing, power and supply. Q2 shows 1.5 GW active and ~3.7 GW contracted |
| Inference and agentic workloads "are expected to drive new capabilities up and down the CoreWeave stack", including developer tooling and multi-cloud operation | same | unspecified | planned | Partly delivered later (Forge, Skills, MCP) |
| CoreWeave Interconnect "available in private preview soon" | [blog, 2026-04-22](https://www.coreweave.com/blog/coreweave-announces-new-capabilities-to-simplify-cross-cloud-ai) | "soon" | planned at the time | Listed as launched in Q2 with no tier |
| Remote Key Encryption "will be available later this year" | [blog, 2026-09-22](https://www.coreweave.com/blog/bringing-enterprise-identity-and-key-control-to-ai-on-coreweave) | 2026 | planned | No release note found by 2026-10-12 |
| Indonesia 360 MW "expected to come online in 2028". India first phase "expected to be available in mid-2028" | [Aug 4](https://www.coreweave.com/news/coreweave-expands-cloud-ai-platform-to-indonesia-marking-first-move-into-asia-pacific-region), [Oct 6](https://www.coreweave.com/news/coreweave-enters-india-expanding-ai-cloud-platform-with-adaniconnex) | 2028 | planned | Contracted, not built |
| CoreWeave "will expand its compute portfolio with the NVIDIA Vera CPU" for agent workloads | [2026-09-30](https://www.coreweave.com/news/coreweave-to-offer-nvidia-vera-the-first-cpu-built-for-ai-agents) | unspecified | announced only | No instance documentation found |

These are commercial statements, not independent forecasts.

## 6. Independent interpretation: conditional 2027–2031 scenarios (researcher's, not CoreWeave's)

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: GPU-cloud vendors will increasingly ship **agent-facing interfaces** (skills, MCP servers, ops agents) as the main way users drive infrastructure | Skills (Oct 9), Mission Control MCP GA and Agent preview (Sep 24), W&B Skills/MCP (May 28) | Developer-relations marketing that follows the current coding-agent trend, with little real use | Skills stay in preview, are archived, or show no external task evidence by 2028. Agent-induced incidents (like the head-node OOM anecdote) lead to restrictions | Low to moderate. No usage data |
| H2: Vendor-authored agent skills will stay **proprietary and non-redistributable**, which limits community reuse compared with OSS runbooks | CoreWeave Skills License forbids redistribution and derivative works | Licence may be relaxed later. Usefulness may not need redistribution rights | Relicensing to an OSI licence, or accepted outside contributions | Moderate for 2026. Unknown afterwards |
| H3: AI clouds will turn into **closed-loop development platforms** (trace → RL → redeploy) instead of selling bare GPUs | Forge, Sandboxes, ARIA, RL Rollouts; trade press framing "beyond GPU infrastructure" | Bundling to raise margins and switching costs; demand may stay with bare-metal labs (SemiAnalysis notes the largest labs buy bare metal) | Revenue mix stays dominated by committed bare-capacity contracts. Forge editions are withdrawn | Moderate. No revenue split by product verified |
| H4: **Lifecycle energy transparency will lag** capacity growth | GW roadmaps and "renewable" claims without PUE/MWh. FOCUS exports quantities only | Disclosures may exist outside the sources screened (e.g. a sustainability report not searched) | CoreWeave publishes metered per-region energy or emissions per workload unit | Moderate. Search for sustainability reports was incomplete |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** coding practice | Coding agents act through vendor skills/MCP rather than manual CLI | Compare agent transcripts with and without a skill on frozen tasks (opt-in, synthetic) | Agents succeed equally from READMEs | Agent and model version pinned. No real credentials |
| **M2** accepted task quality | Fewer failed infra tasks | Hidden, human-authored acceptance checks. All attempts count in the denominator | Skills encode vendor-happy paths only | Vendor `evals/` are not independent |
| **M3** discovery | Skills distributed through plugin marketplaces | Not testable from public data | n/a | No download data |
| **M4** verified third-party reuse | Restricted by licence | Count only consented downstream use. Licence check first | Proprietary terms block reuse | Stars ≠ reuse |
| **M5** reuse-first | Prefer vLLM, Slurm and OSS runbooks over vendor-locked skills | Compare the vendor skill against an OSS equivalent for the same task | The vendor path is easier for vendor customers | Licence and lock-in |
| **M6** lifecycle cost | Upgrade burden (SUNK 8.0), metering gaps | Log review and upgrade minutes. Use metered energy only if instrumented | Costs shift to the vendor and become invisible | **No token→kWh or CO2e conversion** |
| **M7** actionable intervention | Repo-local "agent skill" runbooks | See section 8 | Null effect is plausible | Synthetic pilot only |

Vendor adoption claims (backlog, customer names, testimonials) are **not** evidence of independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline tooling only. The live Trending `capture` command stays **disabled**, and nothing here touches the network or GitHub Trending.

**Candidate practice (not yet validated):** a repository-local, permissively licensed **agent runbook** (prerequisites → exact commands → verification check). It borrows the *structure* of CoreWeave Skills, not their content, because CoreWeave's licence forbids derivative works for distribution. It would sit next to the existing README/CONTRIBUTING.

**Treatment/control and frozen task:**

- **Control A:** the existing `README.md`, `CONTRIBUTING.md` and `AGENTS.md`.
- **Treatment B:** A plus one runbook file.
- **Frozen task set:** 10 offline tasks fixed before any trial. Examples: "from a clean checkout, run `python -m unittest discover -s tests -v`, `python -m trending_study.value_gate --input examples/idea_card.example.json` and `python -m trending_study.reuse_gate --input examples/reuse_check.example.json`, then report each exit code correctly"; "explain why `capture` refuses to run". Include at least 2 tasks with **no valid solution** (e.g. "enable live capture"), where the correct outcome is refusal.
- **Pinning:** pin the agent and model versions and the repo commit. Use the same prompts across arms.
- **Functional unit:** one task whose result is **accepted by hidden checks**. The maintainer, or a second human, writes those checks before the trial and keeps them out of the agent's context.

**Success and guardrails:**

- **Primary outcome:** accepted tasks divided by all assigned tasks, counting refused, failed and timed-out runs.
- **Guardrails, each of which must be zero:** network calls, credential or `.env` reads, edits outside a scratch worktree, invoking `capture`, and any attempt to bypass the source-access decision.
- **Authorship:** all commits keep the maintainer as the sole author, with no AI contributor or co-author attribution.
- **Measured human work:** minutes to write the runbook, review minutes per task, and runbook maintenance minutes over 30 days after any CLI change.
- **Energy:** wall-clock and CI minutes only. Energy is reported only if actually metered. No carbon figures.

**Stop/reversal rule:** stop and keep only A if any of the following holds:

- B does not exceed A by at least 2 accepted tasks out of 10.
- Any guardrail is breached.
- Any no-solution task is "completed" instead of refused.
- Runbook maintenance exceeds 30 minutes in the 30-day window.

A null or negative result is a valid outcome and must be kept. **No trial has been run and no effect is estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, E2):** SUNK v8.0.0 (breaking); login methods GA; FOCUS usage export (preview); Mission Control MCP GA; CoreWeave Skills public preview with a proprietary licence and v0.2.0 tags; Vera Rubin limited availability in one zone; an MLCommons artifact matching the claimed 8,192-GPU system.
- **Claims/announcements only (E1):** Forge, Sandboxes, ARIA, Agent Lens and Serverless RL efficiency numbers; inference leaderboard positions; NVIDIA-sourced perf/watt figures; the "renewable" Swedish capacity; 2028 capacity in Indonesia and India; Interconnect, RKE and Vera CPU; the 8+ GW by 2030 objective.
- **Conjectures and unknowns:** real usage of the agent-facing features; independent security of Sandboxes; energy per workload; in-window filing-level details (customer concentration, litigation, the April notes), which were inaccessible without a declared EDGAR identity; incident history.
- **Important contradictory or null evidence:** capital-intensity criticism; ClusterMAX no longer shows a sole Platinum provider; the Kimi release dateline year error; GA relabelling in September of features launched in May and June; Q2 capex figures that disagree between secondary sources; no in-window security advisory index found (unknown, not zero).
- **Reviewer links and audit date:** pending human factual/link, rights and methods review. **Machine checks run on 2026-10-16:** `scripts/check_research_artifacts.py`, `trending_study.data_integrity`, and the unit suite. These are structural checks only.

**Figures confirmed against raw page text (`curl` + grep) or the GitHub API:** all newsroom, blog and docs figures in the CSV; the MLCommons system size; the Skills repo creation date, licence and release tags. **Confirmed only through WebFetch verbatim extraction (curl 403):** the Q1 and Q2 results, DDTL 5.0 and the convertible-notes figures. **Unverified (E0):** the 24/7 Wall St. capital and price figures, status-aggregator incidents, and the India date discrepancy.
