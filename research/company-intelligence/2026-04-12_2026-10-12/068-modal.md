# Modal — provisional six-month technology intelligence screen (068)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](068-modal.events.csv) and [search log](068-modal.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 068
- **Research issue:** [#136](https://github.com/MSKazemi/github-trending-1000-study/issues/136); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Modal Labs, Inc. (press: "Modal Labs Inc.", New York-based), operating the Modal cloud platform; privately held and venture-funded. No parent company or acquisition of Modal was found. Modal itself acquired **Butter** (announced [2026-04-10](https://modal.com/blog/butter-is-joining-modal), pre-window baseline). Filing-level corporate verification was **not** performed.
- **Product URL and company newsroom:** [modal.com](https://modal.com/), [blog / news](https://modal.com/blog) ([Atom feed](https://modal.com/blog/atom.xml)), [Python SDK changelog](https://modal.com/docs/reference/changelog), [status page](https://status.modal.com/incidents), [modal-labs/modal-client](https://github.com/modal-labs/modal-client) (Apache-2.0), [PyPI `modal`](https://pypi.org/project/modal/).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 32 ledger rows across all seven calendar segments.
- **Source coverage:** official blog (39 in-window Atom entries listed; 27 in-window posts fetched as raw HTML), full SDK changelog, PyPI JSON upload times, GitHub tags/repos via `gh api`, npm registry, official status page (rolling Aug–Oct only), and independent reporting (SiliconANGLE, Bloomberg via Claims Journal, TechCrunch, Tech.eu, Hugging Face). The OpenAI announcement page returned HTTP 403. Reuters and Axios originals were not read. See the [search log](068-modal.search-log.md).

## 1. Search and inclusion audit

Summary only; exact queries, opened URLs and exclusions are in the [search log](068-modal.search-log.md). Search engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | modal.com Atom feed + raw HTML | all blog entries 2026-04-12..10-12 | 39 in-window entries | 27 opened (+2 out-of-window) | 20 rows | case studies, model-availability posts, opinion pieces (log) | feed gives `<updated>`, page shows displayed date only |
| 2026-10-16 | changelog + PyPI + GitHub tags | SDK 1.4.2 … 1.6.1 | 10 releases | 10 | 7 rows | 1.5.1/1.5.2/1.5.5 folded or excluded (log) | changelog dates vs upload times differ |
| 2026-10-16 | web search (8 queries) | funding, incident, outage, London, Devin, OpenAI SDK, VM sandboxes | unknown | ~20 | 4 rows | aggregators and trackers graded E0 and not used | Reuters/Axios not read; OpenAI 403 |
| 2026-10-16 | status.modal.com | incident history | 8 incidents shown (Aug–Oct) | 8 | 1 row | others listed in §3 | Apr–Jul history not displayed |

## 2. Verified company/product identity and baseline

Modal is a serverless cloud for AI workloads: Python-defined Functions, GPU/CPU containers, **Sandboxes** for running untrusted or agent-generated code, Volumes/Queues/Dicts, and (in-window) Servers, Endpoints and multi-node Clusters. The open-source surface is the client SDKs in [modal-labs/modal-client](https://github.com/modal-labs/modal-client) (Apache-2.0 per GitHub API; `py/`, `js/`, `go/` tags) and the [`modal` PyPI package](https://pypi.org/project/modal/) (license expression Apache-2.0). The **service, runtime, scheduler and storage layer are proprietary** and hosted; an Apache-2.0 client does not grant any right to the backend.

Pre-window baseline (context only, not counted): a prior round at a $1.1B valuation in September 2025 (round letter not stated in either cited source; corrected from "Series B" by the 2026-10-16 spot-check) (as reported by [SiliconANGLE](https://siliconangle.com/2026/05/21/serverless-ai-infrastructure-startup-modal-labs-seals-355m-funding-round/) and [Tech.eu](https://tech.eu/2026/08/06/new-york-headquartered-ai-startup-modal-labs-to-open-london-office/)); SDK 1.4.0 (2026-03-25) agent-oriented log CLI and 1.3.5 `modal changelog` CLI "useful … to coding agents" ([changelog](https://modal.com/docs/reference/changelog)); Butter acquisition 2026-04-10. **Post-window, excluded:** [Series D / $1B annualized run rate, 2026-10-14](https://modal.com/blog/1-billion-annualized-run-rate-series-d) and a Muse Spark model post dated 2026-10-15.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Autoresearch demo (Apr 14); OpenAI Agents SDK sandbox integration (Apr 15); SDK 1.4.2 rollover + experimental `modal bootstrap` (Apr 16) | [blog](https://modal.com/blog/autoscaling-autoresearch), [blog](https://modal.com/blog/building-with-modal-and-the-openai-agent-sdk), [changelog](https://modal.com/docs/reference/changelog) | Upstream [openai-agents-python v0.14.0](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0) contains `extensions/sandbox/modal` | AE Studio partner post (Apr 29) excluded as partner case study |
| 2026-05 | SDK 1.4.3 regional routing public beta + Sandbox CIDR allowlists (May 18); Claude Managed Agents integration (May 19); Series C and stated direction (May 21); RBAC GA for Team/Enterprise (May 27) | [blog](https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes), [blog](https://modal.com/blog/modal-series-c), [blog](https://modal.com/blog/role-based-access-control-for-humans-and-agents) | [SiliconANGLE May 21](https://siliconangle.com/2026/05/21/serverless-ai-infrastructure-startup-modal-labs-seals-355m-funding-round/) (cites Reuters) | "Truly serverless GPUs" explainer (May 12) excluded as background |
| 2026-06 | SDK 1.5.0 named Images, egress domain allowlist, `modal skills` CLI (Jun 9); VM Sandboxes alpha (Jun 15); Auto Endpoints + Servers in SDK 1.5.1 (Jun 23); Claude Science integration (Jun 30) | [changelog](https://modal.com/docs/reference/changelog), [blog](https://modal.com/blog/product-updates-vm-sandboxes-domain), [blog](https://modal.com/blog/introducing-auto-endpoints), [blog](https://modal.com/blog/modal-integration-brings-scalable-compute-to-claude-science) | none found | Servers blog (Jun 25) used as limitation note on the Auto Endpoints row |
| 2026-07 | 1M-sandbox demo (Jul 16); Devin Outposts alpha via MIT `modal-devin` (Jul 21); SDK 1.5.3 logs/billing APIs, RBAC API change (Jul 23); **agent-intrusion incident** naming a Modal customer sandbox (HF Jul 27, Modal Jul 29, Bloomberg Jul 30) | [blog](https://modal.com/blog/scaling-to-1-million-concurrent-sandboxes-in-seconds), [blog](https://modal.com/blog/devin-outposts-run-devin-in-modal-sandoxes), [blog](https://modal.com/blog/a-note-on-the-hugging-face-agent-incident) | [Hugging Face](https://huggingface.co/blog/agent-intrusion-technical-timeline); [Bloomberg via Claims Journal](https://www.claimsjournal.com/news/national/2026/07/30/339166.htm) | Three accounts of **one** incident share duplicate group `068-016` |
| 2026-08 | Regional I/O plane migration (Aug 4); London office reported by Tech.eu (Aug 6); SDK 1.5.4 opt-in new Sandbox backend (Aug 12) | [blog](https://modal.com/blog/bringing-serverless-functions-closer-to-the-speed-of-wire), [changelog](https://modal.com/docs/reference/changelog) | [Tech.eu Aug 6](https://tech.eu/2026/08/06/new-york-headquartered-ai-startup-modal-labs-to-open-london-office/) | Status page: Aug 19 `.spawn()` latency, Aug 26 function latency and snapshot-restore degradation (not ledgered) |
| 2026-09 | Official London post (Sep 2); Sidecars public alpha, VM Sandboxes public beta, region multiplier 1.5x→1.15x (Sep 14); Sandbox/Dashboard outage (Sep 16); coding-agent inference write-up (Sep 23); $750M talks report (Sep 28); SDK 1.6.0 (Sep 28) | [blog](https://modal.com/blog/product-updates-sidecars-models-dashboard), [status](https://status.modal.com/incidents), [changelog](https://modal.com/docs/reference/changelog) | [TechCrunch Sep 28](https://techcrunch.com/2026/09/28/source-inference-provider-modal-labs-closing-in-on-750m-round-at-15-75b-valuation/) | Sep 4 storage degradation (2h8m) on status page not ledgered |
| 2026-10-01..12 | Runtime conference (Oct 1): VM Sandboxes GA, Clusters GA, Sidecars; SDK 1.6.1 endpoint observability (Oct 3); Endpoint Candidates GA (Oct 12) | [blog](https://modal.com/blog/vm-sandboxes-agent-computers), [blog](https://modal.com/blog/modal-clusters-generally-available), [blog](https://modal.com/blog/introducing-sandbox-sidecars-trust-boundary), [blog](https://modal.com/blog/endpoint-candidates) | none in-window beyond vendor | Oct 5 status degradation (7 min) not ledgered; Oct 13–15 posts excluded |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](068-modal.events.csv) (32 rows, IDs `CI2026-068-001`…`032`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-068-002 | 2026-04-15 | Modal sandbox backend for OpenAI Agents SDK | Upstream code present at tag; not executed | [Modal tutorial](https://modal.com/blog/building-with-modal-and-the-openai-agent-sdk) (first party) | [openai-agents-python v0.14.0](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0) | E2 |
| CI2026-068-008 | 2026-05-27 | RBAC / Restricted Environments for humans and agents | Team/Enterprise only; API renamed in 1.5.3 | [blog](https://modal.com/blog/role-based-access-control-for-humans-and-agents) | changelog only | E2 (documentary) |
| CI2026-068-009 | 2026-06-09 | `modal skills` agent-skill CLI; Sandbox egress domain allowlist; named Images | Breaking snapshot-TTL default (30 days) | [changelog](https://modal.com/docs/reference/changelog) | PyPI upload 2026-06-09T22:37Z | E2 |
| CI2026-068-011 | 2026-06-23 | Auto Endpoints; `@app.server` Servers | Vendor latency (p50 39ms→6ms) unverified | [blog](https://modal.com/blog/introducing-auto-endpoints) | changelog 1.5.1 | E2 (documentary) |
| CI2026-068-014 | 2026-07-21 | Devin Outposts on Modal (alpha) | MIT `modal-devin` repo | [blog](https://modal.com/blog/devin-outposts-run-devin-in-modal-sandoxes) | [repo](https://github.com/modal-labs/modal-devin) | E2 |
| CI2026-068-016/017/018 | 2026-07-27 / 07-29 / 07-30; incident Jul 9–13 per HF | Agent used a customer's unauthenticated public sandbox endpoint on Modal as a launchpad; Modal, HF and Bloomberg all report Modal's platform was not compromised | One incident, three accounts | [HF](https://huggingface.co/blog/agent-intrusion-technical-timeline), [Modal](https://modal.com/blog/a-note-on-the-hugging-face-agent-incident), [Bloomberg/Claims Journal](https://www.claimsjournal.com/news/national/2026/07/30/339166.htm) | cross-entity | E2 (second-entity documentary), not E3 |
| CI2026-068-027 | 2026-09-28 | SDK 1.6.0: new Sandbox backend default, clusters, sticky sessions, VM runtime option, breaking removals | PyPI 2026-09-29T01:17Z | [changelog](https://modal.com/docs/reference/changelog) | PyPI + tag `py/v1.6.0` | E2 |
| CI2026-068-028/030 | 2026-10-01 | VM Sandboxes GA (Cloud Hypervisor-based); Sidecars (experimental API) | GA vendor claim; gVisor still default | [blog](https://modal.com/blog/vm-sandboxes-agent-computers), [blog](https://modal.com/blog/introducing-sandbox-sidecars-trust-boundary) | changelog 1.6.0 `runtime="vm"` | E2 / E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent tooling | `modal skills` CLI (1.5.0); agent-oriented logs/observability CLI and SDK (1.5.3–1.6.1); Modal Skills used in vendor autoresearch demo | shipped (vendor) |
| Agent integrations | OpenAI Agents SDK sandbox provider; Claude Managed Agents; Claude Science; Devin Outposts (alpha) | shipped / alpha |
| Sandboxes | inbound/outbound CIDR allowlists (1.4.3), egress domain allowlist (1.5.0), new backend (opt-in 1.5.4, default 1.6.0), VM runtime alpha→public beta→GA, Sidecars public alpha | mixed; see rows |
| Governance | RBAC/Restricted Environments, service users for agents, Environment budgets, token TTL (`--expires-in`, 1.6.0), proxy-token auth default for Servers/Endpoints | shipped, plan-gated |
| Inference | Auto Endpoints, Servers, Shared Endpoints with token pricing, Endpoint Candidates (traffic mirroring) | shipped (vendor) |
| Training | Multi-node Clusters GA (`@modal.clustered`) | GA (vendor) |
| Pricing/billing APIs | billing report/summary/rates APIs; broad-region multiplier 1.5x→1.15x (Sep 14) | shipped (vendor) |
| Licensing | Client SDKs Apache-2.0; `modal-devin` and `modal-openai` MIT; `claude-managed-agents-modal-sandbox` and `modal-cursor` show **no detected license** via GitHub API (2026-10-16) | observed |
| Breaking changes | snapshot TTL default (1.5.0), Environment.members deprecated (1.5.3), removals in 1.6.0 incl. `modal bootstrap` six months after introduction | observed in changelog |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "We're going to keep improving here, starting by shipping granular RBAC so customers can give agents capability without risk." | [Series C, 2026-05-21](https://modal.com/blog/modal-series-c) | none stated | RBAC part delivered 2026-05-27 | Broader "compute layer for agents" uncommitted |
| Expand "the Sandbox surface with new capabilities and the scale to run millions in parallel" | same | none stated | partly delivered (VM GA, Sidecars alpha, new backend) | Scale is vendor-demonstrated only |
| Make "the complete model training lifecycle … accessible to far more teams" | same | none stated | uncommitted; Clusters GA Oct 1 is related | No adoption denominator |
| VM runtime default "may change in the future" (gVisor default for now) | [SDK 1.6.0 changelog](https://modal.com/docs/reference/changelog) | none | tentative | Could change sandbox semantics for reusers |
| "building several new tools to help you optimize your own inference servers–starting with Endpoint Candidates" | [2026-10-12](https://modal.com/blog/endpoint-candidates) | none | planned, unspecified | — |
| Further London investment; office "will grow to include engineering" | [2026-09-02](https://modal.com/blog/modal-europe-expansion) | "over time" | uncommitted | Tech.eu reported earlier date and different headcount |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Agent execution will separate "harness/credentials" from "untrusted tool execution" as a default pattern | Claude Managed Agents and Devin Outposts integrations; Sidecars; Modal's stated view that this "is likely to emerge as the winning pattern" | Vendor marketing for its own product; local-first agents may stay dominant for individual developers | Major agent tools keep credentials inside the execution sandbox by default through 2028; no measurable drop in credential-exposure incidents | low–moderate; no task-level data |
| H2: Sandbox misuse incidents will mostly come from customer misconfiguration, not platform escapes | Jul 2026 incident: three sources agree the exposed endpoint was a customer's | Lack of public platform-escape reports may reflect disclosure limits, not absence | An independently confirmed isolation escape on Modal or a peer platform | low; n=1 incident |
| H3: Fast-moving agent infrastructure SDKs impose noticeable migration cost on reusers | 10 SDK releases in window; breaking changes in 1.4.0, 1.5.0, 1.6.0; `modal bootstrap` added and removed within ~5 months | Breaking changes may be small in practice; agents may absorb migration work cheaply | Measured migration time for a pinned example repo stays near zero across 1.4→1.6 | moderate for "churn exists", unknown for cost |
| H4: Vendor-distributed "agent skills" will become a normal discovery/onboarding channel | `modal skills` CLI; autoresearch demo using Modal Skills | Skills may not improve accepted-task rates over plain docs | Controlled tasks show no gain in accepted outcomes vs docs-only condition | low; untested |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Agents increasingly run remote, sandboxed, with machine-readable logs/skills | Count opt-in agent workflows that run in remote sandboxes vs local | Remote execution adopted only by large teams | Only consented workflow logs; no inference from vendor counts |
| M2 accepted task quality | Isolation and egress controls may change failure modes, not success rates | Same task set run locally vs in sandbox, with hidden acceptance tests | No difference in accepted-task rate | All attempts in denominator |
| M3 discoverability | Funding/press volume grows sharply ($355M Series C; $750M talks report) | Separate press counts from verified reuse | Press is not reuse | Stars/funding never used as outcome |
| M4 verified third-party reuse | Integrations exist in third-party OSS (openai-agents-python `modal` extension) | Trace consented downstream repos that actually import and run it | Code presence without execution | Pinned commits; executed tests only |
| M5 rights/security/provenance | Mixed licensing: Apache-2.0 client, MIT examples, unlicensed example repos; shared-responsibility incident | License check before any reuse; egress/auth defaults review | Unlicensed repos are not reusable regardless of popularity | Repository license files at a pinned commit |
| M6 review/maintenance and lifecycle cost | Breaking SDK changes; billing APIs expose spend, not energy | Measure migration minutes per SDK minor version | Agents absorb migration cheaply | No kWh/CO2e inferred from GPU-hours or tokens |
| M7 actionable interventions | Sandbox egress allowlists and auth-by-default as low-cost guardrails | See §8 | Guardrail adds friction without reducing exposure | Synthetic tasks only until approval |

Company adoption claims (e.g., "over 1 billion sandboxes", customer names) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline unit-test suite (`python -m unittest discover -s tests -v`), run as a **synthetic, network-free** task. The disabled Trending `capture` command stays disabled; no sandbox provider makes unapproved scraping permissible.

**Candidate practice (not yet validated):** Run agent-proposed patches in an isolated, egress-denied, ephemeral sandbox before human review, instead of on the maintainer's workstation. Reuse first: compare an existing local container runner (Docker/Podman with `--network none`, already available) against a hosted sandbox (Modal Sandbox with `outbound_domain_allowlist=[]`/CIDR allowlist and a short-TTL token). Do not build a new sandbox tool.

**Treatment/control and frozen comparable task:** Freeze 12 small synthetic issues (for example docstring, validator edge-case and CSV-schema fixes) with **hidden acceptance tests written by a person other than the agent operator** and kept out of agent context. Arm A: local container, network disabled. Arm B: Modal Sandbox, egress denied, pinned `modal` SDK version (record exact version) and pinned image. Same agent, model version, prompt and time budget for both arms; order randomized per task. Accepted-task unit: one patch that passes hidden tests and is accepted by the human reviewer without rework.

**Success and guardrails:** Primary: accepted tasks / all 12 assigned tasks (refused, failed, timed-out included). Guardrails: zero real credentials, tokens or personal data in either environment (only a planted fake secret, whose exfiltration attempt must be blocked and logged); any successful outbound connection is a failure; no new dependency added to the repo; full unit suite green. Measured human work: setup minutes, per-task review minutes, debugging of environment failures. Cost: provider invoice line items only if actually billed; no energy or CO2e estimate unless metered. Commit authorship stays with the maintainer; no AI contributor attribution is recorded in commits.

**Stop/reversal rule:** Stop and keep Arm A if Arm B does not improve accepted-task rate or blocked-egress evidence, or if it adds more than 10 setup/review minutes per task on average, requires a credential with scope beyond one short-TTL token, or its terms/retention for uploaded code cannot be confirmed. Stop immediately on any unblocked outbound connection or fake-secret exposure. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, vendor-sourced):** ten Python SDK releases 1.4.2–1.6.1 (PyPI upload times confirmed); RBAC GA (plan-gated); egress allowlists; Auto Endpoints/Servers; new Sandbox backend; VM Sandboxes alpha→public beta→GA claim; Clusters GA claim; Endpoint Candidates GA claim; third-party integrations whose code exists upstream (OpenAI Agents SDK) or in MIT repos (`modal-devin`).
- **Claims/announcements only:** revenue (>$300M annualized), "over 1 billion sandboxes", 1M-concurrent demo, latency/throughput gains (39ms→6ms, ~80ms p50, 2.8x/5.6x, 3x Sidecars, 6.4 Tbps), OpenRouter token plurality, customer names — all unverified vendor statements. Future direction items in §5.
- **Conjectures and unknowns:** H1–H4 in §6; actual task outcomes, isolation strength, energy use, and status history before late July.
- **Important contradictory or null evidence:** (a) London office reported by Tech.eu on 2026-08-06 vs Modal post 2026-09-02, with headcount ~170 (Tech.eu) vs "120+" (Modal, May); (b) changelog dates vs PyPI/tag times (1.6.0: changelog 2026-09-28, PyPI 2026-09-29T01:17Z; 1.4.2: PyPI 2026-04-16, tag commit 2026-04-17); (c) Sep 16 outage shown as 14 minutes on the official status page vs a different duration in a third-party tracker snippet (E0, unused); (d) an aggregator snippet claiming Modal "disclosed a customer-data leak" was **not** supported by any source read (all three read sources say the exposed asset was a customer's own endpoint and the platform was not compromised); (e) $750M round only reported via one anonymous source inside the window; Modal's confirmation is dated 2026-10-14 and excluded.
- **#56 candidates (not minted):** SiliconANGLE 2026-05-21; Hugging Face 2026-07-27; Bloomberg via Claims Journal 2026-07-30; Tech.eu 2026-08-06; TechCrunch 2026-09-28. Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned; syndicated copies must not be counted twice.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

AI-assisted spot-check, not qualified human review. Each cited URL was re-fetched on 2026-10-16 (`curl` with a generic browser User-Agent; `gh api`; PyPI JSON). Figures were compared against raw page text, not WebFetch summaries. 23 items were checked: 22 ledger rows plus the funding baseline. Ledger-row outcome: 21 confirmed, 1 corrected, 0 unverifiable, 0 wrong. The baseline was corrected.

| Item checked | Outcome | Note |
|---|---|---|
| Baseline: prior round "Series B at $1.1B, Sep 2025" | corrected | SiliconANGLE says the valuation rose "from just $1.1 billion when it last secured funding in September". Tech.eu says "up from its $1.1bn valuation eight months before". Neither source names the round letter, so "Series B" was removed. The Butter post is datePublished 2026-04-10 (confirmed) |
| CI2026-068-001 autoresearch | confirmed | datePublished 2026-04-14. "113 experiments across 238 GPU-hours" on OpenAI's Parameter Golf |
| CI2026-068-002 OpenAI Agents SDK | confirmed | `gh api`: v0.14.0 published 2026-04-15T17:11:33Z. `src/agents/extensions/sandbox/modal` exists at the tag alongside blaxel, cloudflare, daytona, e2b, runloop and vercel. Repo licence MIT |
| CI2026-068-003 SDK 1.4.2 | confirmed | PyPI upload 2026-04-16T20:27Z. license_expression Apache-2.0. `modal bootstrap` was added in 1.4.2 and removed in 1.6.0 per the changelog |
| CI2026-068-005 Claude Managed Agents examples | confirmed (repo metadata only) | `gh api`: repo created 2026-05-18, license null. The blog text was not re-read |
| CI2026-068-006 Series C | confirmed | "$355 million", "$4.65B post-money", "led by General Catalyst and Redpoint", "surpassing $300 million in annualized revenue", "Over 1 billion sandboxes"; datePublished 2026-05-21. SiliconANGLE (2026-05-22T01:11Z) independently reports $355M at $4.65B and quotes Bernhardsson speaking to Reuters |
| CI2026-068-007 stated direction | confirmed | "Sandboxes already drive more than a third of our revenue"; "starting by shipping granular RBAC" |
| CI2026-068-013 1M sandboxes | confirmed | "up to fifty thousand concurrent sandboxes per customer"; "creating all 1 million in under a minute"; datePublished 2026-07-16 |
| CI2026-068-014 modal-devin | confirmed (repo metadata) | `gh api`: created 2026-07-16T15:58Z, MIT |
| CI2026-068-016 Hugging Face timeline | confirmed | "Published July 27, 2026". Describes an "unsecured, user-hosted public endpoint ... on third-party sandbox infrastructure (Modal)" and says "Modal's infrastructure was not compromised in any way". The activity table runs 07-09 to 07-13 |
| CI2026-068-017 Modal note | confirmed | datePublished 2026-07-29. "Modal's platform and isolation were not compromised"; the endpoint was "publicly accessible without authentication" |
| CI2026-068-018 Bloomberg via Claims Journal | confirmed | By Andrew Martin, 2026-07-30T05:00Z. Quotes CTO Akshat Bubna: "Modal's platform wasn't compromised". Cites "Reuters reported earlier on Tuesday" and an Axios CyberGym link |
| CI2026-068-019 I/O plane | confirmed | datePublished 2026-08-04. "≥4 regions"; "dropped by roughly 80ms at p50" |
| CI2026-068-020 Tech.eu London | corrected (limitation) | 2026-08-06T07:48Z, "sources say". Marble Arch, "up to 40 workers", offices in New York, San Francisco and Sweden, "around 170 people". The row attributed the "120+" team figure to the 2026-09-02 London post, but it appears in the 2026-05-21 Series C post |
| CI2026-068-022 London post | confirmed | datePublished 2026-09-02. "our second in Europe"; a VP EMEA joined to build GTM teams |
| CI2026-068-023 Sept product update | confirmed | datePublished 2026-09-14. The broad-region multiplier fell "from 1.5x to 1.15x". Sidecars are in public alpha, VM Sandboxes in public beta, and Environment-level budgets are available for Team and Enterprise |
| CI2026-068-024 status outage | confirmed | The incident detail page ([1065907](https://status.modal.com/incident/1065907)) shows created Sep 16, 2026 6:29pm UTC and resolved 6:43pm UTC (14 minutes). Affected: Deployment, Sandboxes, Dashboard. The detail URL was added as the check URL |
| CI2026-068-025 Kimi serving | confirmed | datePublished 2026-09-23. "2.8x per user and 5.6x across users on the replica"; "repeatedly served the plurality of Kimi-K3 tokens on ... OpenRouter" (vendor claim, unverified) |
| CI2026-068-026 TechCrunch round | confirmed | 2026-09-28T21:29Z. "$750 million funding round led by Accel at a $15.75 billion valuation", "according to a source"; "Modal Labs declined to comment" |
| CI2026-068-027 SDK 1.6.0 | confirmed | The changelog heading is "1.6.0 (2026-09-28)"; the PyPI upload was 2026-09-29T01:17Z. `create()` now blocks until scheduled, and `modal bootstrap` was removed |
| CI2026-068-029 Clusters GA | confirmed | datePublished 2026-10-01. "InfiniBand verbs at up to 6.4 Tbps", billed by the second |
| CI2026-068-030 Sidecars | confirmed | datePublished 2026-10-01. "at least 3x faster" (p50 0.58 ms vs 2.6 ms). The example uses `sb._experimental_sidecars` |
| CI2026-068-031 SDK 1.6.1 | confirmed | PyPI upload 2026-10-03T16:05Z. The changelog lists the endpoint info/stats/logs CLI, `container_total_count` and the "wait up to 25 minutes" note |

PyPI upload times for 1.4.3, 1.5.0, 1.5.1, 1.5.3 and 1.5.4 (rows 004, 009, 011, 015, 021) also match the ledger. Those rows' feature text was not re-checked, so they are not counted above. No personal identifier was sent in any request, and no access gate was bypassed.
