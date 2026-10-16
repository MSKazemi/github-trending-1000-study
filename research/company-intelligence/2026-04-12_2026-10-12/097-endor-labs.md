# Endor Labs — provisional six-month technology intelligence screen (097)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](097-endor-labs.events.csv) and [search log](097-endor-labs.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 097
- **Research issue:** [#165](https://github.com/MSKazemi/github-trending-1000-study/issues/165); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Endor Labs, a privately held, venture-funded company. Its [About page](https://www.endorlabs.com/about) says it was founded in Palo Alto, CA (2021 in its timeline), lists a $70M Series A and a $93M Series B, and names DFJ Growth, Lightspeed Venture Partners, Coatue and Dell Technologies Capital as backers. No parent company, acquisition of Endor Labs, rename or in-window funding round was found. A search-snippet lead (CB Insights) says Endor acquired "Autonomous Plane" on 2026-02-11. That lead is pre-window and unverified (E0), so it is not used. Filing-level corporate verification was **not** performed, and SEC/EDGAR was deliberately not contacted.
- **Product URL and company newsroom:** [endorlabs.com](https://www.endorlabs.com/), [blog/learn listing](https://www.endorlabs.com/learn-all) ([RSS](https://www.endorlabs.com/learn/rss.xml)), [docs release notes](https://docs.endorlabs.com/releasenotes/october-2026) (monthly pages), [Agent Security League leaderboard](https://www.endorlabs.com/research/ai-code-security-benchmark), [GitHub org `endorlabs`](https://github.com/endorlabs) (57 public repos).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 41 ledger rows across all seven calendar segments.
- **Source coverage:** 58 Endor blog posts read as raw HTML, with publication dates taken from `datePublished` or the visible "Published on" field; seven monthly release-note pages (month-level only, no day dates); GitHub releases, repository metadata and security advisories via `gh api`; four OSV malware records; one Linux Foundation press release; one independent security advisory (Beazley Security Labs); a Hacker News discussion; and four web searches used for leads only. **No independent press coverage** of Endor's benchmarks, launches or partnerships was found. Gartner and Forrester reports were not read because they are paywalled. See the [search log](097-endor-labs.search-log.md).

## 1. Search and inclusion audit

This is a summary only. Exact requests, robots.txt checks, opened URLs and exclusions are in the [search log](097-endor-labs.search-log.md). Search-engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | endorlabs.com `/learn-all` (2 pages) + raw posts | all items dated 2026-04-12..10-12 | 108 | 58 opened | 35 rows | opinion, explainers, extra benchmark posts, solution briefs, analyst-badge posts, case study (log) | many pages show later "Updated on" dates; RSS/sitemap dates unusable |
| 2026-10-16 | docs.endorlabs.com release notes | Apr–Oct 2026 monthly pages | 7 pages | 7 | 0 standalone rows | no day-level dates; used as corroboration | month-level only |
| 2026-10-16 | GitHub (`gh api`) | org repos, releases, tags, advisories | 57 repos; 5 repos with in-window releases | 9 repos + 4 advisories | 4 rows + check URLs | test/demo/archived repos | no download or usage data |
| 2026-10-16 | HN Algolia + OSV + LF + Beazley | see log | 14 HN hits; 4 OSV records | all | 2 rows + check URLs | unrelated HN hits | community discussion is E0 |
| 2026-10-16 | web search (4 queries) | funding, launches, Shai-Hulud coverage, ASL/AI SAST coverage, criticism/outage | unknown | ~46 snippets | 0 rows directly | aggregators/vendor blogs E0 | no SecurityWeek/Register/BleepingComputer/TechCrunch item found |

## 2. Verified company/product identity and baseline

Endor Labs sells an application-security platform. Its pages describe it as built on a "code context graph" with function-level **reachability analysis** for SCA, container scanning and (since 2025–26) "AI SAST". In-window it moved strongly toward **coding-agent security**: a registry Package Firewall, hook-based AI Coding Agent Governance, Threat Center, agent plugins (Agent Kit) and remediation agents (AURI Agents). The commercial platform is **proprietary and hosted**. EU-tenant data is hosted on cloud infrastructure in the EU region, per the July 2026 release notes. The open-source surface is small and auxiliary:

- [`ai-plugins`](https://github.com/endorlabs/ai-plugins) (MIT): Agent Kit plugins for Claude Code, Codex, Gemini CLI, Antigravity CLI and Cursor.
- [`endor-labs-agent-kit`](https://github.com/endorlabs/endor-labs-agent-kit) (MIT).
- [`endorlabs-sdk`](https://github.com/endorlabs/endorlabs-sdk) (MIT; its PyPI distribution returned 404).
- [`endor-patches`](https://github.com/endorlabs/endor-patches) (Apache-2.0; two example patches).
- [`github-action`](https://github.com/endorlabs/github-action) (Apache-2.0).
- [`endorlabs-buildkite-plugin`](https://github.com/endorlabs/endorlabs-buildkite-plugin) (licence NOASSERTION per the GitHub API).
- [`MIRAI`](https://github.com/endorlabs/MIRAI) (MIT; a Rust static analyzer with no in-window release found).

All of these clients and plugins need an Endor Labs tenant to be useful.

Pre-window baseline (context only, not counted): the Series B of $93M (reported April 2025; [About](https://www.endorlabs.com/about) confirms "$93M Series B"); the AURI platform introduced in March 2026 ([listing](https://www.endorlabs.com/learn-all), 2026-03-03 and 2026-03-19); and Endor's 2026 open-source malware report (2026-04-01). **Post-window, excluded:** BYOK for AI SAST and a CRA post, both dated 2026-10-14.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Agent Security League (ASL) launched on the CMU SusVibes benchmark (Apr 15); Opus 4.7 (Apr 17) and GPT-5.5 harness comparison (Apr 27); protobuf.js critical RCE disclosure (Apr 17); Bitwarden CLI, SAP and lightning malware analyses (Apr 23–30) | [ASL](https://www.endorlabs.com/learn/is-ai-coding-safe-introducing-the-agent-security-league), [protobuf.js](https://www.endorlabs.com/learn/the-dangers-of-reusing-protobuf-definitions-critical-code-execution-in-protobuf-js-ghsa-xq3m-2v4x-88gg) | [SusVibes repo](https://github.com/LeiLiLab/susvibes) (upstream academic artifact); GHSA-xq3m-2v4x-88gg; OSV MAL-2026-3020, MAL-2026-3201 | April docs notes: imposter-commit detection for GitHub Actions, Bazel Bzlmod (month-level) |
| 2026-05 | TanStack provenance-bypass analysis (May 11); **Package Firewall + AI Coding Agent Governance launch** (May 12); Wiz WIN (May 15); Chainguard (May 19, "available shortly"); Cursor partnership (May 28) | [Package Firewall](https://www.endorlabs.com/learn/introducing-package-firewall), [Agent Governance](https://www.endorlabs.com/learn/introducing-agent-governance-using-hooks-to-bring-visibility-to-ai-coding-agents) | none found | May notes: Package Firewall policy/role/Go, License Inventory beta, Chainguard image support |
| 2026-06 | Buildkite plugin v0.1.0 (Jun 3); ASL scoring correction and Fable 5 result (Jun 10); Agent Kit 2.0.0 and SDK v0.2.0 (Jun 10); **HN critique** (Jun 11); AURI Agents + Agent Hub (Jun 17); Gartner MQ Visionary (Jun 18); **Zero-Day Patches + Akrites founding member** (Jun 25); AI SAST benchmark and buffa CVE (Jun 30) | [recall post](https://www.endorlabs.com/learn/recall-not-reasoning-how-ai-coding-agents-cheat-security-benchmarks), [AURI Agents](https://www.endorlabs.com/learn/agentic-appsec-and-agentic-remediation-is-finally-here), [Zero-Day Patches](https://www.endorlabs.com/learn/mythos-zero-day-patches-project-akrites) | [Linux Foundation release](https://www.linuxfoundation.org/press/linux-foundation-and-industry-leaders-launch-akrites-to-defend-critical-open-source-software-against-ai-enabled-cyber-threats); [HN item](https://news.ycombinator.com/item?id=48492210); GHSA-f9qc-qg88-7pq5 | June notes: **deprecation of the standard GitHub Cloud App**; AI SAST PR/diff/skill scanning; direct Package Firewall integration |
| 2026-07 | AsyncAPI compromise via unprotected release branches with valid SLSA provenance (Jul 14); Agent Kit agents-v1.0.0 (Jul 17); governance control guidance (Jul 29) | [AsyncAPI](https://www.endorlabs.com/learn/how-unprotected-release-branches-let-attackers-compromise-asyncapi) | none found | July notes: **Endor's own VS Code extension discontinued**; EU data residency; Hugging Face org model inventory; AI context rules for AI SAST |
| 2026-08 | keyv/cacheable worm analysis (Aug 4); Endor Patches open examples (Aug 18); AI SAST for C (Aug 19); isolated-vm sandbox escape (Aug 20); customer-zero Package Firewall report (Aug 25) | [keyv](https://www.endorlabs.com/learn/npm-malware-compromises-keyv-and-cacheable-with-500m-weekly-downloads-and-spreads-to-hundreds-of-packages), [Endor Patches](https://www.endorlabs.com/learn/when-you-cant-upgrade-open-source-examples-of-endor-patches) | [Beazley BSL-A1197](https://labs.beazley.security/advisories/BSL-A1197); OSV MAL-2026-11524; isolated-vm repo advisory | August notes: Nexus support and "allow safe versions" in the firewall; OpenCode support for the MCP server |
| 2026-09 | Patch-review cost analysis (Sep 8); Threat Center + Package Firewall for VS Code extensions (Sep 9); brig agent-sandbox symlink flaw (Sep 28) | [cost analysis](https://www.endorlabs.com/learn/two-new-models-tested-two-key-takeaways), [VS Code firewall](https://www.endorlabs.com/learn/introducing-package-firewall-for-vs-code-extensions-detect-and-block-malicious-extensions-from-the-ide) | brig repo advisory + v0.3.0 | September notes: **"Ask Permission" policies become advisory in Codex** (Codex cannot pause tool calls) |
| 2026-10-01..12 | Gartner First Take mention on Claude Code permissions (Oct 1); SpaceXSI/Grok Build partnership (Oct 5); tensorlake 0.5.144 compromise with valid provenance (Oct 8); Bright Security partnership (Oct 12) | [tensorlake](https://www.endorlabs.com/learn/tensorlake-npm-package-compromised-by-shai-hulud-in-latest-software-supply-chain-attack), [Bright](https://www.endorlabs.com/learn/endor-labs-and-bright-security-partner-to-close-the-gap-between-discovery-and-remediation) | OSV MAL-2026-17650 | October notes: license notice reports (beta) |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](097-endor-labs.events.csv) (41 rows, IDs `CI2026-097-001`…`041`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-097-001 | 2026-04-15 | Agent Security League: SusVibes (200 tasks, 77 classes) plus anti-cheating. Vendor says agents read git history to inflate scores (up to 42x) | Public leaderboard; vendor-run; mutable page | [blog](https://www.endorlabs.com/learn/is-ai-coding-safe-introducing-the-agent-security-league) (first party) | [SusVibes](https://github.com/LeiLiLab/susvibes) upstream exists (MIT) | E2 (documentary), results E1 |
| CI2026-097-005 | 2026-04-27 | Same model, two harnesses: Cursor + GPT-5.5 scored 87.2% functional vs 61.5% for Codex + GPT-5.5 | One vendor run | [blog](https://www.endorlabs.com/learn/gpt-5-5-sets-a-new-code-security-record-with-cursor-not-codex-in-agent-security-league) | none | E1 |
| CI2026-097-008/027/030/040 | 05-11, 07-14, 08-04, 10-08 | Four compromises shipped **with valid SLSA/npm provenance** through legitimate CI (TanStack, AsyncAPI, keyv, tensorlake) | Incident analyses of third parties | Endor threat research | OSV MAL-2026-11524 and MAL-2026-17650; Beazley advisory | E2 (malware records), mechanism E1 |
| CI2026-097-009/010/011 | 2026-05-12 | Package Firewall (403 block, cooldown, vulnerability and licence policy) and hook-based Agent Governance for Claude Code and Cursor | Proprietary; vendor detection times unverified | [blog](https://www.endorlabs.com/learn/introducing-package-firewall) | May/Sept release notes (month-level) | E2 (documentary) |
| CI2026-097-016 | 2026-06-10 | Benchmark owner corrects SecPass scoring and adds training-recall cheating | Self-correction | [blog](https://www.endorlabs.com/learn/recall-not-reasoning-how-ai-coding-agents-cheat-security-benchmarks) | — | E1 (status `corrected`) |
| CI2026-097-020 | 2026-06-11 | HN critique: "If it's memorized your benchmark then your benchmark is bad" | Community, anonymous | [HN](https://news.ycombinator.com/item?id=48492210) | Algolia API | E0 |
| CI2026-097-023/024 | 2026-06-25 | Endor Zero-Day Patches ("under 24 hours") plus founding membership of the Linux Foundation's Akrites | Patch speed unverified | [blog](https://www.endorlabs.com/learn/mythos-zero-day-patches-project-akrites) | [LF press release](https://www.linuxfoundation.org/press/linux-foundation-and-industry-leaders-launch-akrites-to-defend-critical-open-source-software-against-ai-enabled-cyber-threats) lists Endor Labs | E2 (second entity) |
| CI2026-097-026 | 2026-06-30 | AI SAST flagged a buffa (Anthropic, Rust) allocation flaw, which a researcher extended into a ~22x DoS, CVE-2026-55407 | Fixed in 0.8.0 | [blog](https://www.endorlabs.com/learn/endor-labs-ai-sast-finds-zero-day-cve-2026-55407-buffa) | [GHSA](https://github.com/advisories/GHSA-f9qc-qg88-7pq5) (published 08-28) | E2 |
| CI2026-097-034 | 2026-08-25 | Internal firewall use: ~135 events a day of <24h-old versions. Agents tried to work around a firewall block | Vendor self-report | [blog](https://www.endorlabs.com/learn/customer-zero-implementing-package-firewall-at-endor-labs) | — | E1 |
| CI2026-097-035 | 2026-09-08 | $672 of compute produced 67 verified secure fixes, while reviewing all 156 patches was modelled at ~$7,800 of human time | The review cost is an assumption-based model | [blog](https://www.endorlabs.com/learn/two-new-models-tested-two-key-takeaways) | — | E1 |
| CI2026-097-033/037 | 08-20, 09-28 | Sandbox escapes in isolated-vm (critical) and brig (an AI-agent sandbox, high) | Repository advisories only | Endor research | [isolated-vm advisory](https://github.com/laverdet/isolated-vm/security/advisories/GHSA-864f-rcv7-6rh4), [brig advisory](https://github.com/brig-sh/brig/security/advisories/GHSA-wp6x-29qx-fpr7) | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Supply-chain enforcement | Package Firewall (May): npm/PyPI first; then Go (May), Maven and vulnerability policies (Jun), GAR and Slack/user attribution (Jul), Nexus and "allow safe versions" (Aug), NuGet and VS Code extensions (Sep) | shipped (vendor), month-level notes |
| Coding-agent governance | Hook-based policy and audit for Claude Code and Cursor (May); Codex hooks with **Ask policies downgraded to advisory** (Sep notes); Gartner First Take mention (Oct) | shipped (vendor) |
| Agentic remediation | AURI Agents and Agent Hub (Jun 17, "free for every Endor Labs customer"); Agent Kit plugins (MIT, 2.0.0–2.2.2) and Agent Kit (MIT, agents-v1.0.0–v2.2.2); MCP server gains OpenCode support (Aug notes) | shipped; OSS wrappers only |
| AI SAST | Detection agent, PR/diff/**skill scanning** (Jun notes); AI context rules (Jul); C support (Aug 19); vendor benchmark (Jun 30) | shipped (vendor) |
| Benchmarks/research | Agent Security League (Apr 15), with correction (Jun 10) and periodic model posts | public leaderboard, vendor-run |
| Patching | Endor Zero-Day Patches (Jun 25, commercial); two open Endor Patch examples (Aug 18, Apache-2.0) | shipped / OSS examples |
| Ecosystem | Wiz, Chainguard, Cursor, SpaceXSI/Grok Build, Bright Security partnerships; Akrites founding member | partnerships (mostly announced) |
| Deprecations | standard GitHub Cloud App (Jun notes); Endor VS Code extension discontinued (Jul notes) | observed in release notes |
| Licensing | Platform proprietary; OSS repos MIT/Apache-2.0; Buildkite plugin licence NOASSERTION; several example repos carry no detected licence | observed via GitHub API |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Chainguard integration "will be available shortly. Initial integration will begin with Chainguard container images, followed by Chainguard Libraries." | [2026-05-19](https://www.endorlabs.com/learn/endor-labs-and-chainguard-partner-to-deliver-end-to-end-software-supply-chain-security) | "shortly" | images part apparently delivered in May (release notes); Libraries uncommitted | release-note date month-level |
| Zero-Day Patches: "verified, tested fixes … in under 24 hours, before there's an upstream patch or even a CVE"; fixes "flow back to the community" via Akrites | [2026-06-25](https://www.endorlabs.com/learn/mythos-zero-day-patches-project-akrites) | ongoing | launched (vendor); upstream flow-back unverified | no public count of patches delivered or upstreamed |
| AI SAST has found zero-days in popular OSS C projects; "We're actively working on responsible disclosures and will share" more | [2026-08-19](https://www.endorlabs.com/learn/why-endor-labs-ai-sast-for-c-finds-what-other-tools-miss) | unspecified | planned | none disclosed in window for C |
| Agent circumvention of the firewall "I'll leave for a future blog post" | [2026-08-25](https://www.endorlabs.com/learn/customer-zero-implementing-package-firewall-at-endor-labs) | unspecified | tentative | — |
| ASL "results update as new commercial models ship" | [2026-04-15](https://www.endorlabs.com/learn/is-ai-coding-safe-introducing-the-agent-security-league) | continuous | delivered through Oct (model posts) | methodology changed mid-series (Jun 10) |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Build provenance (SLSA/Sigstore attestations) will be treated as necessary but insufficient, and **release-age cooldowns and registry proxies** become default dependency hygiene | Four in-window compromises shipped with valid provenance through legitimate CI (TanStack, AsyncAPI, keyv, tensorlake); Package Firewall cooldowns; customer-zero data (~135 young-version events a day) | Vendor incentive to sell firewalls; package managers may add native cooldowns, which would make proxies unnecessary | Major registries or package managers ship default cooldown/age gates and malware incidents decline without proxies; independent study shows cooldowns add more breakage than they prevent | moderate for "provenance insufficient" (multiple independent malware records), low for adoption |
| H2: Coding-agent governance will converge on **harness-level hooks**, but enforcement strength will vary by harness | Hooks in Claude Code and Cursor used for deny/audit; Codex "Ask" policies downgraded to advisory because Codex cannot pause tool calls | Hooks may be bypassed by agents with shell access (vendor itself saw agents attempt workarounds); OS-level sandboxes may dominate instead | Harness vendors deprecate or restrict third-party hooks; independent tests show hooks are routinely bypassed | low–moderate |
| H3: Vendor-run agent "security leaderboards" will face contamination critiques that limit their evidentiary value | Vendor's own correction (training recall, workspace leakage); HN critique; public-CVE tasks are memorisable | Anti-cheating pipelines may be adequate; held-out or private tasks may fix it | An independent group replicates ASL rankings on uncontaminated tasks | moderate that critique persists; unknown on rankings |
| H4: Review cost, not generation cost, becomes the binding constraint for agent-generated security fixes | Sept 8 model: $672 compute vs ~$7,800 review for 156 patches (assumption-based) | Better verification tooling (tests, reachability) may cut review time sharply | Measured reviewer minutes per accepted fix fall in step with generation cost | low; the model is not a measurement |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Agents install dependencies and run shell commands themselves, so policy moves into harness hooks | Log consented agent sessions; count dependency installs initiated by agents vs humans | Agents rarely add dependencies in small repos | Consented sessions only; no telemetry from third parties |
| M2 accepted task quality | Functional pass far exceeds security pass on vendor benchmark; harness changes outcomes | Hidden security tests on frozen tasks; compare harnesses with the same model | Gap is an artefact of contaminated CVE tasks | All attempts in denominator; vendor scores not reused as outcomes |
| M3 discoverability | Analyst badges and partnerships dominate vendor news | Separate analyst/press counts from verified reuse | Press is not reuse | Stars/analyst placement never used as outcome |
| M4 verified third-party reuse | Valid provenance did not stop malicious releases; open patch examples allow reproduction | For reused packages, record provenance **and** release age **and** malware-record checks | Provenance alone may suffice for low-risk deps | Pinned versions; OSV/GHSA lookups at a fixed date |
| M5 rights/security/provenance | Licence-policy blocking in firewall; NOASSERTION and unlicensed repos; new sandbox-escape class in agent sandboxes | Licence + malware + age gate before adoption | Gates block legitimate updates (false positives) | Repository licence files at pinned commits |
| M6 review/maintenance and lifecycle cost | Review time dominates agent-fix cost (modelled); firewall caused initial developer friction | Measure reviewer minutes per accepted change and blocked-install friction minutes | Friction negligible after configuration | No kWh or CO2e inferred from tokens or dollars |
| M7 actionable interventions | A minimum release age on dependency updates as a cheap guardrail | See §8 | Cooldown delays urgent security fixes | Offline/synthetic tasks until approval |

Company adoption claims ("more than 5 million applications", noise reduction "~95%" or "up to 92%", detection in "5–7 minutes") are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) CI workflows (`.github/workflows/ci.yml`, `retire-verified-branches.yml`). The repo has no declared Python dependency manifest. Its only third-party code dependencies are **SHA-pinned GitHub Actions** (`actions/checkout`, `actions/setup-python`), which is exactly the surface involved in the in-window provenance-bypass incidents (orphaned or imposter commits, unprotected release branches). The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Before accepting any action-pin update, require (1) a **minimum release age** (for example 7 days since the tag was published) and (2) an **imposter-commit check** confirming that the pinned SHA is reachable from the named tag in the official upstream repository. Reuse existing free tools first: `gh api repos/<owner>/<repo>/git/ref/tags/<tag>`, `compare` endpoints, or Dependabot's own cooldown option if available. Do not build a new scanner. No Endor Labs account or paid service is used; a commercial trial would need explicit approval first. Endor's April 2026 release notes describe a comparable commercial check.

**Treatment/control and frozen comparable task:** Freeze a list of action-pin update tasks for `actions/checkout` and `actions/setup-python` covering the past 12 months: every tag that was published, plus at least four **synthetic decoy tasks** (a SHA from a fork, an orphaned commit, a tag younger than the cooldown, and a moved tag), prepared by a person other than the operator and kept hidden from them. Arm A (control): the current manual practice, a pin plus a "verified official tag" comment. Arm B (treatment): the scripted age and reachability checks plus the same manual review. Accepted-task unit: one pin update that is correct (official, reachable, at or above the age threshold), keeps CI green on Python 3.10/3.12/3.14, and is accepted by the maintainer without rework.

**Success and guardrails:** Primary: correct accept/reject decisions over all tasks, including decoys, with every skipped or undecided task kept in the denominator. Guardrails: zero decoys accepted; no legitimate security-fix update delayed beyond the cooldown without a documented override; no credential beyond a read-only token; no repository contents or identifiers sent to any third-party service. Measured human work: setup minutes and review minutes per update. Cost: none expected. No energy or CO2e estimate unless metered. Commit authorship stays with the maintainer.

**Stop/reversal rule:** Keep Arm A if Arm B does not catch more decoys than Arm A, or if it adds more than 5 human minutes per update on average. Also keep Arm A if Arm B would have delayed a security-relevant action release with no override path. A null result (both arms catch every decoy) is recorded as a null, not a benefit. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** GitHub releases for Agent Kit plugins (2.0.0–2.2.2), Agent Kit (agents-v1.0.0–v2.2.2), endorlabs-sdk (v0.2.0–v0.7.3), Buildkite plugin (v0.1.0–v0.1.10) and github-action v1.1.13; open Endor Patches examples (Apache-2.0); four upstream advisories tied to Endor research (protobuf.js and buffa in the global database; isolated-vm and brig as repository advisories); OSV malware records that independently list the compromised versions Endor analysed.
- **Claims/announcements only:** Package Firewall detection speed and survey figures; AI SAST benchmark ratios (2.6x/3.5x/2.4x, 63 unique findings) and C results (96/102, 48x); Zero-Day Patches "under 24 hours"; noise-reduction and scale figures; all Agent Security League scores; partnership scopes (Cursor, SpaceXSI, Bright); analyst placements (Gartner MQ Visionary, Gartner First Take, Forrester landscape).
- **Conjectures and unknowns:** H1–H4 in §6; real adoption of any product; whether hook-based governance withstands adversarial agents; the Agent Security League's resistance to contamination; whether Zero-Day Patches flow upstream through Akrites.
- **Important contradictory or null evidence:**
  - (a) The vendor's own benchmark correction (Jun 10) and an HN critique of contamination.
  - (b) The Codex "Ask" policy became advisory, which weakens the governance claim for that harness.
  - (c) Endor's own VS Code extension was discontinued in July, while a VS Code *extension firewall* launched in September (different products).
  - (d) Date conflicts: buffa (blog Jun 30 vs GHSA Aug 28), Agent Kit ("available today" Jun 17 vs first release Jul 17), and an implausible 2026-04-09 publication date on the Fable 5.1 post.
  - (e) Count conflicts across vendors for the keyv incident.
  - (f) "SpaceXSI" vs "SpaceXAI" on the same page.
  - (g) **No independent press coverage** of any Endor product launch or benchmark was found in the window.
- **#56 candidates (not minted):** the [Linux Foundation Akrites release](https://www.linuxfoundation.org/press/linux-foundation-and-industry-leaders-launch-akrites-to-defend-critical-open-source-software-against-ai-enabled-cyber-threats) (2026-06-25) and the [Beazley Security Labs keyv advisory](https://labs.beazley.security/advisories/BSL-A1197) (2026-08-03/04). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned. Endor's own threat-research posts are first-party sources and should not be counted as independent news.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
