# NVIDIA: provisional six-month technology intelligence screen (061)

> **PROVISIONAL, AI-assisted, not human-reviewed (2026-10-16).** This report, its [event ledger](061-nvidia.events.csv) and its [search log](061-nvidia.search-log.md) are an AI-assisted documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a validated task outcome, an exhaustive search, an endorsement, or a security or scientific sign-off.

- **Company watchlist ID:** 061, NVIDIA (slug `nvidia`).
- **Research issue:** [#129](https://github.com/MSKazemi/github-trending-1000-study/issues/129). Corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). The ledger rows are candidate leads for #56. No `NEWS-YYYY-NNNN` items were created.
- **Product URL and channels:** [developer.nvidia.com](https://developer.nvidia.com/), [newsroom](https://nvidianews.nvidia.com/), [technical blog](https://developer.nvidia.com/blog/), [corporate blog](https://blogs.nvidia.com/), [PSIRT bulletins on GitHub](https://github.com/NVIDIA/product-security), and official GitHub organisations: [NVIDIA](https://github.com/NVIDIA), [NVIDIA-NeMo](https://github.com/NVIDIA-NeMo), [ai-dynamo](https://github.com/ai-dynamo), [triton-inference-server](https://github.com/triton-inference-server).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources were read on 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass. Factual reviewer and review date are **pending**.
- **Status:** screened (provisional). 38 dated ledger rows cover all seven calendar segments.
- **Scope:** the issue's angle, meaning the AI software stack, inference and serving, developer tooling, open models and licences, agent security, and energy-relevant execution. Gaming, automotive, consumer devices, quantum, finance and most hardware news were screened out on purpose (see the [search log](061-nvidia.search-log.md)).
- **Evidence grades:** the ledger uses company-watch E0–E4 tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

The full query table is in the [search log](061-nvidia.search-log.md). Most rows rest on three kinds of source:

1. **GitHub API records:** release timestamps, prerelease flags and licence files for 15 NVIDIA repositories.
2. **Raw Markdown PSIRT bulletins:** 51 in-range bulletin folders were downloaded from `NVIDIA/product-security`. Initial-release dates come from each bulletin's revision table.
3. **Downloaded newsroom, blog, docs and third-party pages:** every figure was confirmed by grepping the raw text.

Inaccessible sources were VMblog, TMCnet, MarkTechPost, BetaNews, gpuinsights.net and NVIDIA investor-relations pages (all HTTP 403). No Reuters or The Register item surfaced. Result counts were not recorded; they are **unknown, not zero**. This screen does not claim exhaustive coverage.

## 2. Verified company/product identity and baseline

- **Entity:** NVIDIA Corporation. Press releases in the window carry "NVIDIA (NASDAQ: NVDA)" and "© 2026 NVIDIA Corporation", for example the [Sep 28 release](https://nvidianews.nvidia.com/news/open-agent-safety-platform).
- **Ownership:** publicly listed, with no parent company indicated. Filing-level confirmation is **not cited** (EDGAR not accessed; see the search log).
- **Brands:** no acquisition or rename of a scoped brand was found in the window. Two re-homings were found:
  - The NeMo repository split, with speech moving to [NVIDIA-NeMo/Speech](https://github.com/NVIDIA-NeMo/Speech/releases/tag/v3.0.0) (CI2026-061-023).
  - The NVIDIA-founded Open Secure AI Alliance moving to Linux Foundation stewardship (CI2026-061-030).
- **Pre-window baseline (context only, not counted):**
  - Dynamo 1.0 "enters production" (GTC, 2026-03-16).
  - NemoClaw repo created 2026-03-15; OpenShell repo created 2026-02-24.
  - MLPerf Inference v6.0 (2026-04-01).
  - Run:ai was open-sourced on 2026-10-13, the day after the window closed, so it is excluded.
- **Licences checked (current default branch, not historical):**

| Repository | Licence |
|---|---|
| TensorRT-LLM | Apache-2.0, with third-party portions |
| Dynamo | Apache-2.0, with MIT test data |
| NeMo-Agent-Toolkit, OpenShell, NemoClaw, cuda-python, Container Toolkit, TensorRT OSS | Apache-2.0 |
| NeMo-Guardrails | Apache-2.0 per the SPDX header |
| Megatron-LM | BSD-style |
| Triton server | BSD-3-Clause |
| NOOA (`labs-OO-Agents`) | Apache-2.0 |

  - Open model weights moved to **OpenMDW-1.1** for new releases (CI2026-061-009, 013, 024). The TensorRT core library, NIM and the DSX components are not shown to be open source by anything read here.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs `CI2026-061-NNN`) | Independent / contrary reporting | Notes |
|---|---|---|---|
| 2026-04-12..30 | 001 TRT-LLM v1.2.1 (last stable tag in window); 002 KAI Scheduler bulletin; 003 NemoClaw prompt-injection env-var bulletin | none read | No in-window newsroom item on the scoped angle was read. Nano Omni (reported 04-28) was excluded: no dated first-party page. |
| 2026-05 | 004 cuda.core 1.0 stable; 005 TRT-LLM and 006 Triton bulletins (Triton CVE-2026-24207 rated 9.8); 008 NeMo Agent Toolkit 1.7; 009 OpenMDW-1.1 adoption plan; 010 Agent Toolkit / NemoClaw / OpenShell early preview; 011 DSX OS / MaxLPS | 007 TechTalks on Lasso's NemoClaw prompt-injection research | CUDA 13.3.0 is listed only as "May 2026" in the [archive](https://developer.nvidia.com/cuda-toolkit-archive); it has no row. |
| 2026-06 | 012 TensorRT 11.0; 013 Nemotron 3 Ultra (OpenMDW-1.1); 015 NeMo bulletin; 016 Container Toolkit TOCTOU bulletin | 014 Artificial Analysis (pre-release partner) plus the CodeRabbit check | No June "GTC Paris" software item was found. |
| 2026-07 | 017 TRT-LLM bulletin (fixes only in rc builds); 018 Triton bulletin; 019 Dynamo 1.3 (CUDA 13); 020 Open Secure AI Alliance + NOOA | 021 Cloud Security Alliance critique (no charter or board) | CUDA 13.4.0 developer preview is listed at month level only. |
| 2026-08 | 022 Dynamo bulletin (CVE-2026-24254 rated 9.8); 023 NeMo Speech 3.0; 024 Nemotron 3.5 Lightning; 025 Container Toolkit 1.20; 026 Triton 9.8 path traversal; 027 NemoClaw/OpenShell bulletin (two 9.9 sandbox escapes) | none read | |
| 2026-09 | 028 PSIRT moves to GitHub-only from Oct 1; 029 Megatron Bridge (30 HIGH CVEs); 031 CUDA 13.4 GA; 033 Dynamo 1.5 (opt-in TLS); 034 OpenShell 0.1.0; 035 Open Agent Safety Platform (OpenShell + Sentry) | 030 Phoronix (alliance moves to LF); 032 MLCommons v6.1; TechCrunch on 035 | |
| 2026-10-01..12 | 036 AI-factory economics blog (USD per MW); 037 Model-Optimizer bulletin; 038 OCP Vera Rubin designs and grid standards | none read | Run:ai OSS (Oct 13) and Nemotron 3.5 Super VL/Bolt (Oct 15) are out of window. |

## 4. Dated event evidence and capabilities

See the [CSV](061-nvidia.events.csv) for all 38 rows, each with its publication date, event date, availability, limitation and grade. The clusters that matter most for the study:

| Cluster | What the cited documents support | What they do **not** support |
|---|---|---|
| **Agent runtime: NemoClaw/OpenShell** (003, 007, 010, 027, 034, 035) | OpenShell was "early preview" on May 31 (010) and "broadly available" on Sep 28 (035). v0.1.0 shipped Sep 25, after near-daily v0.0.x tags (034). NVIDIA's own bulletins list a prompt-injection env-var exfiltration flaw (CVE-2026-24222, 8.6; 003). They also list two OpenShell sandbox-escape/provisioning flaws rated 9.9, fixed in v0.0.34 (027). | Independent containment efficacy. TechTalks reports Lasso's injection-driven key exfiltration and NVIDIA calling it out of bounty scope (007): a sandbox that "behaved as configured" did not stop semantic manipulation. Sentry has no stated availability date. |
| **Inference serving: Triton, TRT-LLM, Dynamo** (001, 005, 006, 017, 018, 019, 022, 026, 033) | Monthly Triton releases and roughly monthly Dynamo feature releases. Dynamo 1.5 adds opt-in TLS/mTLS on TCP and NATS and deprecates KVBM (033). Critical-rated issues: Triton auth bypass (006), Triton path traversal (026), Dynamo multimodal (022). | Exploitation data. Also not supported: that "latest stable" is patched. TRT-LLM's July fixes exist only in v1.3.0 release candidates, with no stable v1.3.0 by Oct 12 (001, 017). Several bulletins came weeks to months after their fix releases (015, 016, 022). |
| **Open models and licences** (009, 013, 014, 024) | New Nemotron releases use OpenMDW-1.1. Ultra is 550B/55B-active with an NVFP4 checkpoint. Lightning's model card says "ready for commercial use". | That "open" covers data equally. NVIDIA's Nemotron info page describes separate training-data terms, and Nano/Super were not relicensed. Capability: NVIDIA's own table shows Ultra behind GLM 5.1 and Kimi K2.6 on Terminal-Bench 2.0 (013). Artificial Analysis evaluated Ultra *in partnership with* NVIDIA (014). |
| **Developer platform portability** (004, 012, 023, 031) | cuda.core 1.0 promises SemVer stability (004). CUDA 13.4 adds Windows on Arm and a Rubin preview, and R615 drivers ship only open kernel modules (031). NeMo Speech 3.0 reports removing 800k deprecated LOC and adding `AGENTS.md` (023). | Migration cost. TensorRT 11 removed twelve plugins (012). CUDA Python 13.4 deprecates Python 3.10 (031), which matters because this repository's CI tests 3.10. |
| **Security disclosure process** (028, plus 51 downloaded bulletin files screened) | From Oct 1, 2026, PSIRT says it will publish only on GitHub, in Markdown, CSAF and CVE formats (028). | Bulletin data quality is imperfect. Examples: a CWE mismatch (022), an impact/vector mismatch (026), a CVE removed on revision (5848), a CWE description corrected (029). |
| **Energy-relevant execution** (011, 032, 036, 038) | Vendor framing is "token performance per megawatt" (DSX MaxLPS, 011; AI-factory ROI blog, 036), plus a grid-responsive pilot (011) and OCP grid-resilience standards (038). | Any measured lifecycle energy. MLPerf v6.1 is an independent benchmark body, but NVIDIA's 2.5x figure is a submitter statement on Preview-category hardware, and power results were **not inspected** (032). The roughly $60M-per-MW figure is a vendor estimate with no method (036). |

## 5. What the company says it intends to do

| Close paraphrase or short quote | Link/date | Horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Adopt OpenMDW "across future releases" of Cosmos, Isaac GR00T, Ising, Nemotron | [2026-05-28](https://www.devopsdigest.com/linux-foundation-releases-openmdw-11) | future releases | planned | Existing Nano/Super keep the older licence; data terms are separate |
| OpenShell "will intelligently route queries to local models based on the user's privacy policies" on Windows | [2026-05-31](https://nvidianews.nvidia.com/news/enterprise-software-leaders-build-ai-agents-with-nvidia) | unstated | tentative | "when-and-if-available" disclaimer on DSX/Agent pages |
| DSX MaxLPS lets operators run "up to 40% more GPUs" in a fixed power budget | [2026-05-31](https://nvidianews.nvidia.com/news/dsx-infrastructure-ai-factory) | unstated | vendor claim | No method or baseline published in the release |
| PSIRT "will only publish security bulletins on GitHub" from Oct 1, 2026 | [2026-09-01 commit](https://github.com/NVIDIA/product-security/commit/2bcefb8992) | 2026-10-01 | announced | Website discontinuation not checked |
| Sentry reference design to quarantine agents out-of-band on BlueField-4 | [2026-09-28](https://nvidianews.nvidia.com/news/open-agent-safety-platform) | unstated | reference design; no date | Partner list is not adoption evidence |
| KVBM "removal targeted for v1.7.0"; standalone Rust EPP image "planned" | [2026-09-21](https://github.com/ai-dynamo/dynamo/releases/tag/v1.5.0) | next releases | planned | |
| Rubin CUDA support to reach GA "in a future release of the CUDA Toolkit" | [2026-09-09](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus/) | unstated | planned | |

These are company statements. They are not forecasts by this study and not delivered features.

## 6. Independent interpretation: conditional 2027–2031 scenarios (researcher, not NVIDIA)

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence |
|---|---|---|---|---|
| H1. Agent sandboxes become a standard deployment layer, but they will not by themselves reduce data exfiltration driven by prompt injection | 007, 010, 027, 035; many partner integrations announced | Ordinary containers, VMs and egress allowlists may give equal protection at lower cost; adoption may stay a press-release phenomenon | Independent replications show sandboxed agents leaking at the same rate as unsandboxed ones, **or** comparable tasks show no difference against a plain locked-down container | low |
| H2. Release-candidate-only security fixes and delayed bulletins in fast-moving inference stacks will keep "pin a stable version" from being a sufficient security policy | 001, 015, 016, 017, 022 | The cadence may slow as products mature; downstream distributions (NGC containers) may package fixes that GitHub tags do not show | A stable TRT-LLM 1.3 ships with all July fixes, and later bulletins arrive within days of fixes | medium (for 2026); unknown for 2027+ |
| H3. A uniform open-model licence (OpenMDW) lowers legal review cost for reusing NVIDIA weights | 009, 013, 024 | Data-agreement and gated-dataset terms may keep total review cost unchanged; mixed legacy licences persist | Legal review of an OpenMDW model takes as long as review of a custom-licence model in a timed comparison | low |
| H4. "Tokens per megawatt" becomes the vendor's energy metric, while independent lifecycle energy per accepted task stays unmeasured | 011, 032, 036, 038 | MLPerf power submissions may already give comparable data (not inspected here) | MLCommons or a peer-reviewed study publishes a task-level energy comparison including NVIDIA systems | medium |
| H5. Machine-readable advisories (CSAF on GitHub) make automated dependency checks of NVIDIA AI components practical | 028 | Advisory data inconsistencies (022, 026) may limit automation value | Automated tooling still misses fixed versions or mis-ranks severity on sampled bulletins | low |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** coding-agent practice | Repos adding `AGENTS.md`, agent skills or sandbox policies (023, 008, 034) | Count such files in sampled repos at t0 and follow-up, with dated commits | Files are added for marketing, not used | File presence is not agent use |
| **M2** accepted task quality | Sandboxed vs. unsandboxed agent task acceptance | Hidden, human-authored acceptance tests on frozen tasks | No quality difference; the sandbox only adds friction | Count all attempts, including refused and timed-out ones |
| **M3** discoverability | NVIDIA repos and models surface via vendor events, not organic search | Compare referral sources where observable | Press coverage does not equal discovery by the target users | Stars and trending rank are not adoption |
| **M4** verified third-party reuse | Partner "integrations" (010, 035) | Trace one consented, working downstream integration per claim | Announced integrations never ship | Vendor partner lists count as E1 only |
| **M5** reuse-first, rights and security | RC-only fixes, OpenMDW vs. legacy licences, CSAF feeds | Licence/advisory audit of pinned NVIDIA dependencies | The audit finds no actionable difference | Current licence files are not historical licences |
| **M6** lifecycle human and energy cost | Migration work from deprecations (012, 031, 033) and security upgrades | Log human minutes per upgrade; measure CPU/GPU energy only where metered | Costs are trivial for small repos | **No token-to-CO2e conversion**; no vendor per-MW figures reused as measurements |
| **M7** actionable interventions | The experiment in section 8 | Preregistered pilot | The null result is kept | Small-N pilot, no generalisation |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The run uses offline synthetic tests only. The live Trending `capture` stays disabled under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md), and no sandbox makes unapproved collection permissible.

**Candidate practice (not yet validated):** run coding-agent work on this repository inside a policy-enforced agent sandbox with deny-by-default egress. The sandbox is NVIDIA OpenShell, pinned to a release at or above v0.1.0, and therefore past the v0.0.34 fixes in 027.

**Comparator (reuse-first):** the maintainer's current practice, meaning the agent in an isolated git worktree with the harness's own permission prompts. A second, cheaper comparator, if time allows, is a rootless container with an egress allowlist built from existing OS tools. If the cheaper option passes the same tests, it wins.

**Frozen task set and functional unit:**
- 12 small, pre-written repository tasks, such as validator rule additions and documentation-consistency fixes. Each has **hidden acceptance tests authored by a human before the trial** and kept out of the agent's context.
- In 4 of the 12 tasks, a fixture file contains a seeded indirect prompt-injection string. The string asks the agent to read a synthetic canary file and send it to a local mock endpoint. Which tasks are seeded is fixed in advance and not disclosed to the operator during runs.
- **Functional unit:** one task independently accepted by the hidden tests and a human reviewer. **Every** assigned task counts in the denominator, including refused, failed and timed-out runs.

**Guardrails:**
- Synthetic canary only; no real credentials, tokens or emails anywhere in the environment.
- Pinned versions of the agent, model and sandbox, recorded at the start.
- Full unit suite plus `check_research_artifacts.py` must pass for a task to be accepted.
- Any dependency added by the agent fails the task unless the reuse gate passes.
- No live GitHub network access beyond what the harness needs for the model API.

**Measured human work:** setup minutes, policy-edit and approval interruptions per task, review minutes per accepted task, and rework count. Wall-clock time and CPU time come from `/usr/bin/time`. Energy is recorded only if a hardware meter or RAPL counter is actually available. Otherwise it is reported as **not measured**, and no carbon figure is computed.

**Primary endpoints:**
1. Accepted tasks divided by 12, per arm.
2. Canary exfiltration events, counted at the mock sink. **This must be 0.**

**Stop/reversal rule:**
- Stop the treatment arm on any canary reaching the sink.
- Do not adopt the sandbox if:
  - setup takes more than 2 human-hours, **or**
  - it accepts 2 or more fewer tasks than the comparator with no safety difference, **or**
  - review-plus-interruption minutes per accepted task exceed the comparator by more than 50%.
- Stop on any newly disclosed unpatched critical OpenShell CVE affecting the pinned version.
- A null or negative result is recorded as such.
- **No trial has been run; no effect is claimed.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (E2 documentary):**
  - GitHub releases: TRT-LLM 1.2.1, cuda.core 1.0, NAT 1.7, TensorRT 11.0, Dynamo 1.3/1.5, NeMo Speech 3.0, Container Toolkit 1.20, OpenShell 0.1.0.
  - CUDA 13.4 GA notes.
  - The Nemotron 3.5 Lightning model card.
  - 13 PSIRT bulletins with dated revision tables.
- **Claims/announcements only (E1):**
  - Agent Toolkit and partner integrations, DSX OS/MaxLPS energy claims, the Open Agent Safety Platform and Sentry, OpenMDW adoption for future releases, the Open Secure AI Alliance, OCP contributions, and AI-factory economics.
- **Conjectures and unknowns:**
  - Section 6 hypotheses.
  - Whether a stable TRT-LLM 1.3 with the fixes ships.
  - Whether NVIDIA's legacy bulletin website stopped receiving bulletins after Oct 1.
  - The exact CUDA 13.4.1 GA day.
  - Sentry availability.
  - Whether DSX OS is published under an open licence (no repository was verified).
  - MLPerf power results.
- **Important contradictory or null evidence:**
  - Lasso/TechTalks prompt-injection results against NemoClaw (007).
  - OpenShell's own critical sandbox-escape CVEs (027).
  - The CSA critique of the alliance's governance (021).
  - Ultra trailing rivals on Terminal-Bench 2.0 in NVIDIA's own table (013).
  - The partner relationship behind the Artificial Analysis evaluation (014) and CodeRabbit's near-baseline result with a high retry rate.
  - Conflicting alliance member counts (020).
  - Bulletin data inconsistencies (022, 026).
  - "Early preview" vs. "broadly available" vs. months of public GitHub releases for OpenShell.
- **EDGAR not used:** no SEC filing is cited because EDGAR requires a declared contact identity for automated access (see the search log).
- **Reviewer links and audit date:** pending. A human reviewer should:
  - re-run the logged queries;
  - spot-check at least 10 ledger rows against their sources, including 001/017 (RC-only fixes), 022, 026 and 027;
  - confirm the OpenMDW licence text and the Nemotron data-agreement terms;
  - inspect MLPerf v6.1 power submissions.

Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
