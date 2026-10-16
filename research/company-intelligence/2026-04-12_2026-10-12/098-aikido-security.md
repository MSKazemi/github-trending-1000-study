# Aikido Security — provisional six-month technology intelligence screen (098)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](098-aikido-security.events.csv) and [search log](098-aikido-security.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 098
- **Research issue:** [#166](https://github.com/MSKazemi/github-trending-1000-study/issues/166). Evidence corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` item was minted here; candidates are listed in §9.
- **Ownership and product boundaries (as of 2026-10-12):** Aikido Security NV, Belgium (entity name as reported by [SiliconANGLE, 2026-06-30](https://siliconangle.com/2026/06/30/aikido-acquires-root-patch-open-source-without-forced-upgrades/)). It is privately held and venture-funded, and no parent company was found. In-window it acquired **Root** (Root.io Inc., formerly Slim.AI), announced 2026-06-30. Earlier acquisitions are baseline (see §2). Filing-level corporate verification was **not** performed.
- **Product URL and company newsroom:** [aikido.dev](https://www.aikido.dev/), [blog](https://www.aikido.dev/blog) ([RSS](https://www.aikido.dev/blog/rss.xml)), [product changelog](https://help.aikido.dev/changelog), [status page](https://status.aikido.dev/), [AikidoSec on GitHub](https://github.com/AikidoSec), [Aikido Intel](https://intel.aikido.dev/), npm `@aikidosec/*`, PyPI `aikido_zen`, Hugging Face [`AikidoSec/altar-1`](https://huggingface.co/AikidoSec/altar-1).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). 37 ledger rows cover all seven calendar segments.
- **Source coverage:** about 150 in-window blog posts were dated from the RSS feed and page metadata. About 40 were read in full. The coverage also includes the official changelog (#48–#57), GitHub releases, the npm, PyPI and Hugging Face registries, GitHub malware advisories, NVD history, and independent or second-entity pages: SiliconANGLE, Infosecurity Magazine, OpenJS Foundation, Help Net Security, the Composer release notes, a competitor comparison (Audn.AI) and Hacker News threads. The New Stack is robots-disallowed for Claude agents and was not read. BleepingComputer returned HTTP 403. See the [search log](098-aikido-security.search-log.md).

## 1. Search and inclusion audit

This is a summary only. Exact requests, opened URLs and exclusions are in the [search log](098-aikido-security.search-log.md). Search-engine result totals were not exposed and are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | aikido.dev RSS + sitemap + raw HTML | all blog posts 2026-04-12..10-12 | ~150 in window | ~40 read in full | 20 rows | ~43 "top tools"/"alternatives" listicles; explainers; unchecked disclosures kept as context | sitemap may omit posts; pages edited after publication |
| 2026-10-16 | help.aikido.dev changelog (.md) | #48 (2 Jun) … #57 (07 Oct) + 4 feature posts | 14 | 14 | 6 rows | others folded into rows | no entries before 2 Jun are listed in the current index |
| 2026-10-16 | GitHub API, npm, PyPI, Hugging Face, GHSA, NVD | AikidoSec repos/releases; registry timestamps; advisories | 63 repos; 27 safe-chain, 25 firewall-node releases | — | 6 rows + 14 checks | — | registry removal times not exposed |
| 2026-10-16 | HN Algolia + 3 WebSearch queries | Aikido / aikido.dev stories; Root; JetBrains; TeamPCP; funding | 31 + 23 HN hits; unknown web | ~30 | 1 row + 5 checks | aggregators and rewrites graded E0 | The New Stack disallowed; BleepingComputer 403 |

## 2. Verified company/product identity and baseline

Aikido sells a developer-first application-security platform. It combines SCA and malware detection, SAST (including the community fork **Opengrep**, LGPL-2.1, co-founded with about nine other vendors), secrets scanning (it employs the author of Gitleaks and backs the MIT-licensed **Betterleaks**), IaC/container/cloud posture scanning, the in-app runtime protection agents **Zen** (`firewall-*` repositories), the install-time malware proxy **Safe Chain**, the developer-endpoint product **Device Protection**, AI pentesting and, in-window, LLM-based code review and audit. The public **Aikido Intel** feed underpins its malware disclosures.

**Licensing boundary.** Zen and Safe Chain use a custom licence: "offered under a commercial and under the AGPL license" (LICENSE files; npm says AGPL-3.0-or-later, and the GitHub API reports NOASSERTION). The `@aikidosec/mcp` npm package declares "AGPL". The [`aikido-claude-plugin`](https://github.com/AikidoSec/aikido-claude-plugin) and `aikido-cursor-plugin` repositories show **no detected licence** (GitHub API, 2026-10-16). The SaaS backend, Intel pipeline and AI agents are proprietary.

**Pre-window baseline (context only, not counted):** a $60M Series B at a $1B valuation in January 2026, as restated by SiliconANGLE on 2026-06-30. Earlier acquisitions per Aikido's own category page and SiliconANGLE: Trag (2025-08), Allseek and Haicker (2025-09). Earlier launches: Betterleaks (2026-03-12), Aikido Infinite (2026-02-26) and Package Health (2026-02-03). Safe Chain minimum package age arrived in 2025-11. **No in-window funding round was found** (one WebSearch only surfaced January coverage).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Axios CVE "not exploitable" analysis (Apr 14); Device Protection launch and Safe Chain 1.5.0 (Apr 20); Bitwarden CLI worm disclosure (Apr 23); Mini Shai-Hulud on SAP `@cap-js` (Apr 29); AWS Kiro hooks integration (Apr 30); firewall-node 1.8.23+ | [blog](https://www.aikido.dev/blog/endpoint-security-for-developer-devices), [blog](https://www.aikido.dev/blog/aikido-x-kiro), [release](https://github.com/AikidoSec/safe-chain/releases/tag/1.5.0) | NVD history for CVE-2026-40175; GHSA-g98r-qjhg-4fmr; npm registry | GPT-Proxy backdoor (Apr 22), fake "tanstack" packages and PyTorch Lightning compromise (Apr 29–30) read only as listing titles (context) |
| 2026-05 | Safe Chain 1.5.2 (checksums, loopback-only proxy) (May 4); Opengrep one-year report (May 12); further Mini Shai-Hulud waves (May 12, 19); Google API key revocation delay research (May 21); Laravel-Lang and Codex Remote UI disclosures (May 23, 27); `@aikidosec/mcp` 1.0.8 on npm (May 29) | [release](https://github.com/AikidoSec/safe-chain/releases/tag/1.5.2), [blog](https://www.aikido.dev/blog/opengrep-sast-one-year) | Opengrep repo/releases via GitHub API | The New Stack story "AI coding agents are installing packages no one owns" (May 27, from HN) **not read** (robots). No changelog entries listed for May |
| 2026-06 | Changelog #48 AI Code Audit + Aikido MCP (Jun 2); Docker Hardened Images VEX (Jun 11); #49 Device Protection Windows (Jun 15); AI Code Analysis launch and JetBrains plugin malware (Jun 16); Mastra scope compromise (Jun 17); OWASP 200-credit offer (Jun 18); Drydock (Jun 23); codfish GitHub Action tag hijack (Jun 24); Packagist/Composer (Jun 26); **Root acquisition**, Aikido Libraries/Images and #50 Registry Proxy (Jun 30) | [changelog](https://help.aikido.dev/changelog/q2-2026/48-ai-code-audit-aikido-mcp-and-servicenow-integration), [blog](https://www.aikido.dev/blog/introducing-code-audit-find-complex-vulnerabilities-hidden-in-your-codebase), [blog](https://www.aikido.dev/blog/aikido-acquires-root) | [SiliconANGLE Jun 30](https://siliconangle.com/2026/06/30/aikido-acquires-root-patch-open-source-without-forced-upgrades/); [Infosecurity Magazine Jun 17](https://www.infosecurity-magazine.com/news/fifteen-jetbrains-marketplace/); GHSA-pp62-grrw-hvfp; Composer 2.10.0 notes | Busiest product month. HN thread on Code Audit (Jun 19) contains critical comments (E0) |
| 2026-07 | Noise reduction for secrets/CVEs (Jul 8); AsyncAPI `pull_request_target` compromise and Intel explainer (Jul 14); 13-model CVE benchmark (Jul 16); SleeperGem RubyGems (Jul 19); Betterleaks suppression rules (Jul 23); #52 DSPM + Aikido Libraries (Jul 28) | [changelog](https://help.aikido.dev/changelog/q3-2026/52-dspm-aikido-libraries-and-repository-code-quality-scans), [blog](https://www.aikido.dev/blog/benchmarking-ai-models-known-cves) | npm registry (@asyncapi/specs); [betterleaks PR #207](https://github.com/betterleaks/betterleaks/pull/207) | Jul 31 post commenting on a third party's agent incident was not used as evidence about that third party |
| 2026-08 | **keyv worm** (Aug 4); Aikido Machine on-prem (Aug 5); #53 Deep Review + Android pentest (Aug 12); 11.7bn-token model benchmark (Aug 21); self-comparison against Claude Security/Codex Security (Aug 24); ISO 42001 claim (Aug 26); #54 Device Protection Linux beta (Aug 25) | [blog](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack), [blog](https://www.aikido.dev/blog/the-aikido-machine-on-prem-ai-pentesting-that-never-leaves-your-network), [changelog](https://help.aikido.dev/changelog/q3-2026/53-deep-review-android-pentests-custom-reports-and-free-credits) | GHSA-3p9h-f68w-m6fx; npm keyv; HN (keyv 251 points, 138 comments) | TeamPCP arrests reported by [Help Net Security](https://www.helpnetsecurity.com/2026/08/27/alleged-teampcp-hackers-arrested-australia/) (context; Aikido not named) |
| 2026-09 | Safe Chain 1.5.16 fixes a min-age bypass (Sep 3); Deep Review $1/PR (Sep 4); AWS Security Competency (Sep 17); competitor comparison (Sep 18); **Altar** open-weight model (Sep 21); #56 min-age bypass for critical CVE fixes (Sep 22); Deel partnership and supplychain.local Go worm (Sep 23); Safe Chain 1.5.21 (Sep 25); OpenJS SSP (Sep 25/28) | [blog](https://www.aikido.dev/blog/aikido-altar-open-weight-ai-sovereign-security), [release](https://github.com/AikidoSec/safe-chain/releases/tag/1.5.16), [blog](https://www.aikido.dev/blog/aikido-openjs-ssp-node-security) | [OpenJS Foundation Sep 25](https://openjsf.org/blog/openjs-foundation-launches-the-security-stewardshi); [Audn.AI Sep 18](https://blog.audn.ai/posts/audn-vs-codex-vs-aikido-juice-shop-comparison); Hugging Face model API | Status page lists only a planned maintenance (Sep 20) |
| 2026-10-01..12 | FedRAMP Moderate claim via Knox (Oct 6); #57 Terraform provider (Oct 7); tensorlake worm (Oct 8); CREST pentest accreditation claim (Oct 12) | [blog](https://www.aikido.dev/blog/aikido-fedramp-moderate-authorization), [changelog](https://help.aikido.dev/changelog/q4-2026/57-aikido-speaks-5-languages-and-adds-a-terraform-provider), [blog](https://www.aikido.dev/blog/tensorlake-npm-package-compromised) | GHSA-rqxj-g25x-4v9v; FedRAMP marketplace page (Knox) | No in-window incidents on the status page |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](098-aikido-security.events.csv) (37 rows, IDs `CI2026-098-001`…`037`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-098-001 | 2026-04-14 | Argues CVE-2026-40175 (Axios) is not exploitable in practice | CNA vector revised from critical-equivalent to 4.8 on 04-16; ADP 8.1 still conflicts | [blog](https://www.aikido.dev/blog/axios-cve-2026-40175-a-critical-bug-thats-not-exploitable) | NVD CVE history API | E2 (direction corroborated, causation unknown) |
| CI2026-098-003/004 | 2026-04-20 | Device Protection; Safe Chain 1.5.0 (uvx, PyPI min-age fix) | free tier stated; Safe Chain AGPL/commercial | [blog](https://www.aikido.dev/blog/endpoint-security-for-developer-devices), [release](https://github.com/AikidoSec/safe-chain/releases/tag/1.5.0) | npm publish 21:57Z | E1 / E2 |
| CI2026-098-010 | 2026-06-02 | AI Code Audit; Aikido MCP for AI coding assistants | MCP npm 1.0.8 published 2026-05-29 | [changelog #48](https://help.aikido.dev/changelog/q2-2026/48-ai-code-audit-aikido-mcp-and-servicenow-integration) | npm registry | E2 (documentary) |
| CI2026-098-012 | 2026-06-16 | AI Code Analysis covers "roughly 70-80%" of a pentest at "around 10x lower cost" | internal testing, no denominator | [blog](https://www.aikido.dev/blog/introducing-code-audit-find-complex-vulnerabilities-hidden-in-your-codebase) | HN critique (E0) | E1 |
| CI2026-098-014 | 2026-06-17 | 141 @mastra packages republished with a malicious dependency | GHSA preceded the post | [blog](https://www.aikido.dev/blog/over-140-popular-mastra-npm-packages-hit-by-supply-chain-attack) | GHSA-pp62-grrw-hvfp; npm | E2 |
| CI2026-098-017 | 2026-06-30 | Root acquisition → Aikido Libraries/Images (version-pinned backports) | price not disclosed in sources read | [blog](https://www.aikido.dev/blog/aikido-acquires-root) | SiliconANGLE | E1 + press |
| CI2026-098-025 | 2026-08-04 | keyv family worm published with valid GitHub Actions provenance | scope grew from about 11 listed packages to at least 444 in the post's own 2026-08-05 update | [blog](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) | GHSA-3p9h-f68w-m6fx; npm | E2 |
| CI2026-098-027 | 2026-08-12 | Deep Review agentic PR review ($1 per PR) | accuracy unmeasured | [changelog #53](https://help.aikido.dev/changelog/q3-2026/53-deep-review-android-pentests-custom-reports-and-free-credits) | — | E2 (documentary) |
| CI2026-098-029 / 031 | 2026-08-24 / 09-18 | Vendor self-comparison (68/89 vs 60 vs 58) vs competitor comparison (4 of 235 findings shared; Aikido "noisy" on test fixtures) | both are interested parties | [Aikido](https://www.aikido.dev/blog/aikido-finds-more-vulnerabilities-claude-security-mythos), [Audn.AI](https://blog.audn.ai/posts/audn-vs-codex-vs-aikido-juice-shop-comparison) | each other only | E1 / E1 |
| CI2026-098-030 / 033 | 2026-09-03 / 09-25 | Safe Chain fixes a minimum-age bypass, then adds a safe-patches exemption | guardrail churn | [1.5.16](https://github.com/AikidoSec/safe-chain/releases/tag/1.5.16), [1.5.21](https://github.com/AikidoSec/safe-chain/releases/tag/1.5.21) | npm; changelog #56 | E2 |
| CI2026-098-032 | 2026-09-21 | Altar: pruned GLM-5.3 derivative, open weights | licence "other", inherits GLM-5.3 terms | [blog](https://www.aikido.dev/blog/aikido-altar-open-weight-ai-sovereign-security) | [Hugging Face](https://huggingface.co/AikidoSec/altar-1) | E2 (artifact exists) |
| CI2026-098-034 | 2026-09-28 (launch 09-25) | Inaugural funder of OpenJS Security Stewardship Program | amount undisclosed | [blog](https://www.aikido.dev/blog/aikido-openjs-ssp-node-security) | [OpenJS](https://openjsf.org/blog/openjs-foundation-launches-the-security-stewardshi) | E2 (second entity) |
| CI2026-098-035 | 2026-10-06 | FedRAMP Moderate claim | marketplace link resolves to the Knox Systems package, whose embedded data lists "Aikido for Government" (dateAvailable 2026-09-28) | [blog](https://www.aikido.dev/blog/aikido-fedramp-moderate-authorization) | [FedRAMP marketplace](https://www.fedramp.gov/marketplace/products/F1206111371/) | E2 (government marketplace listing; corrected 2026-10-16) |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent-facing tooling | Aikido MCP server (25 npm versions in window), Kiro agent hooks, Claude/Cursor plugin repos (unlicensed), Custom Reports via "Aikido Agent" | shipped (vendor) |
| LLM review/audit | AI Code Audit / Code Analysis (credits), Deep Review agentic PR review ($1/PR), fix PRs from review comments, threat-model diagrams, AI noise reduction for secrets/CVEs | shipped (vendor) |
| Supply chain | Device Protection (Apr launch; then Windows, Ruby/Rust, Linux beta, Firefox/Homebrew), Registry Proxy, Safe Chain 1.5.x, Composer default malware blocking, Drydock pre-publish review | shipped / beta |
| Remediation | Agentic Dependency AutoFix; Aikido Libraries and Images (Root) with version-pinned backports | shipped (vendor) |
| On-prem / model | Aikido Machine appliance; Altar open-weight model | shipped (vendor) |
| Governance/compliance | FedRAMP Moderate (via Knox), ISO 42001, CREST, AWS Security Competency, approval inbox for ignores, Terraform provider | vendor-stated |
| OSS stewardship | Opengrep releases (LGPL-2.1), Betterleaks rules (MIT), OpenJS SSP funding, stated free upstream backports | mixed; see rows |
| Licensing | AGPL+commercial for Zen/Safe Chain; MCP "AGPL"; plugin repos without licence; Altar "other" | observed |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "Critical fixes for actively exploited vulnerabilities will continue to go back to the community, upstream across ecosystems, not locked behind a paywall." | [Root post, 2026-06-30](https://www.aikido.dev/blog/aikido-acquires-root) | none stated | planned, uncommitted in measurable terms | No count, list or SLA of upstreamed fixes found in window |
| Aikido Machine runs "AI pentesting and AI Code Analysis (+ many more to come)" on-prem | [2026-08-05](https://www.aikido.dev/blog/the-aikido-machine-on-prem-ai-pentesting-that-never-leaves-your-network) | none | tentative | Which products follow is unspecified |
| Opengrep post reflects on "what comes next for Opengrep" | [2026-05-12](https://www.aikido.dev/blog/opengrep-sast-one-year) | none | multi-vendor project roadmap, not an Aikido commitment | v2.0.0 "nopython" alphas (Sep) are "FOR TESTING ONLY" |
| OWASP credit benefit "runs for six months" from 18 June 2026 | [2026-06-18](https://www.aikido.dev/blog/aikido-x-owasp-200-free-credits-for-individual-members) | to ~Dec 2026 | planned, time-limited | Take-up unknown |
| Device Protection for Linux "now in beta" | [changelog #54, 2026-08-25](https://help.aikido.dev/changelog/q3-2026/54-device-protection-for-linux-and-vm-scanning-for-google-cloud) | GA undated | tentative | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Install-time controls on developer and agent machines (minimum package age, registry proxies, pre-publish review) become a default layer next to CI scanning | Device Protection expansions; Safe Chain; Registry Proxy; Composer 2.10 default malware policy; Drydock pre-publish review; repeated worm waves (Bitwarden, Mastra, keyv, tensorlake) | Vendor marketing during a cluster of incidents; registries may internalise the controls and remove the vendor layer | Registry-native controls (trusted publishing, freezes, staged publishing) cut malicious-version dwell time without third-party proxies | moderate that the layer grows; low on who owns it |
| H2: Exceptions erode cooling-off guardrails over time | Safe Chain fixed a min-age bypass (Sep 3) and then added a safe-patches exemption (Sep 25); changelog #56 auto-bypasses for critical CVEs | Exceptions may be tightly governed and net-positive for patch latency | Published exemption criteria and audit logs; no incident traced to an exempted package | low; n=2 changes |
| H3: Vendor-run LLM security benchmarks will not settle tool choice; neutral, task-level comparisons will be needed | Aikido's self-comparison (76% vs 67% vs 65%) vs a competitor's Juice Shop test (4 of 235 findings shared); contamination concerns on HN | Benchmarks may converge once public suites mature | An independent, pre-registered benchmark with hidden tasks shows stable rankings across vendors | moderate |
| H4: "Fix in place" backports (Aikido Libraries/Images) shift maintenance from upgrading to vendor-patched forks, creating provenance questions | Root acquisition; "no breaking changes" positioning; Docker hardened images/VEX | Backports may stay a narrow stop-gap for critical CVEs | Backported packages carry clear upstream lineage, licences and SBOM attestations; few customers stay on forks long-term | low; no usage data |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Agents install packages and skills autonomously, and vendors add MCP servers and agent hooks for security feedback | Count consented agent sessions that add dependencies, and whether a policy layer intercepted any | Agents rarely add dependencies in small repos | Only consented session logs; no vendor counts |
| M2 accepted task quality | LLM review (Deep Review, Code Audit) may find logic flaws but also raises noise | Hidden-test task set with and without an LLM reviewer; count true/false findings | No difference in accepted-task rate; reviewer noise costs time | All findings adjudicated by a human, with the denominator kept |
| M3 discoverability | Disclosure blogs drive HN traffic (keyv: 251 points) | Separate attention metrics from reuse | Attention is not reuse | Stars, HN points and downloads never used as outcomes |
| M4 verified third-party reuse | Opengrep, Betterleaks and Composer adopt shared components and feeds | Trace pinned downstream imports and executed tests | Code presence without execution | Pinned commits; executed tests only |
| M5 rights/security/provenance | Valid provenance did not stop the keyv worm; AGPL+commercial tools; unlicensed plugin repos; Altar "other" licence | Licence and provenance check before adopting any of these tools | A guardrail adds friction without catching anything | Licence files at a pinned commit; GHSA records |
| M6 review/maintenance and lifecycle cost | Credit-priced LLM audits ($1/PR), frequent Safe Chain releases (27 in window) | Measure setup and review minutes plus invoice lines | Agents absorb the cost cheaply | No kWh/CO2e inferred from tokens ("11.7 billion tokens" is not energy) |
| M7 actionable interventions | Minimum package age and pinned actions as cheap guardrails | See §8 | Guardrail blocks legitimate updates | Synthetic and offline tasks until approval |

Company adoption claims (for example "100k+ teams" in page footers and SiliconANGLE's "more than 100,000 teams") are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) CI and local development dependency installs (`pip` for the test suite, plus GitHub Actions references in `.github/workflows/`). The disabled Trending `capture` command stays disabled, and nothing here changes source-access rules.

**Candidate practice (not yet validated):** a reuse-first, install-time supply-chain guardrail. Compare two configurations. The **comparator (Arm A)** is the current workflow plus already-available native controls: Actions pinned to full commit SHAs and a hash-locked `requirements` file with `pip install --require-hashes`. **Arm B** is Arm A plus a minimum-package-age policy enforced by an existing tool: Aikido Safe Chain (AGPL/commercial, so check the licence before use) or an equivalent native setting where one exists. Do not build a new tool.

**Treatment/control and frozen comparable task:** freeze 10 dependency-maintenance tasks, each taken from a real upstream release of a dependency already used by the repository, for example "update X to the latest version that passes the full suite". Freeze 2 synthetic "poisoned version" fixtures served from a local index in an offline sandbox, with no network access to public registries during the trial. Run each task in both arms in randomised order with the same operator and time budget. **Accepted-task unit:** one dependency update merged by the maintainer that passes `python -m unittest discover -s tests -v` and both synthetic CLI smoke gates, with no rework.

**Success and guardrails:** Primary outcomes are accepted updates out of the 10 assigned (blocked, abandoned and failed tasks stay in the denominator) and whether each poisoned fixture was blocked. Guardrails:
- no real credential, token or personal data in either environment (planted fake secrets only);
- no new runtime dependency added to the repository;
- the licence of any tool is reviewed by a human before use;
- no paid service or API spend without the owner's explicit approval;
- full test suite green.

**Measured human work:** setup minutes, minutes per task, and false blocks (legitimate versions delayed) with time lost. No energy or CO2e estimate is made unless it is actually metered. Commit authorship stays with the maintainer.

**Stop/reversal rule:** keep Arm A only if Arm B blocks neither poisoned fixture that Arm A missed. Also keep Arm A if Arm B delays more than 2 of the 10 legitimate updates beyond the task time budget, adds more than 5 minutes per task on average, or its licence is incompatible with the repository's use. Stop immediately if any real secret appears in a log. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** Safe Chain 1.5.0–1.5.25 and firewall-node 1.8.23–1.8.45 (GitHub releases plus npm timestamps); `@aikidosec/mcp` releases; changelog-listed features #48–#57 (AI Code Audit, MCP, Registry Proxy, Agentic AutoFix, DSPM, Aikido Libraries, Deep Review, Android pentest, Device Protection for Windows and Linux beta, Terraform provider); Altar weights on Hugging Face; Betterleaks PR #207 and v1.7.0; Opengrep releases; OpenJS SSP partnership (second entity); Root acquisition (SiliconANGLE). Six malware disclosures match registry and GHSA records showing the named versions were published and withdrawn. Those records do not establish who detected them first.
- **Claims/announcements only:** AI Code Analysis "70-80%" of a pentest at "~10x lower cost"; Intel "under 8 minutes"; benchmark results (23/26, 28/32, 68/89); Altar recall loss; FedRAMP, ISO 42001, CREST and AWS competency; Kiro "first security ISV"; "100k+ teams"; free upstream backports.
- **Conjectures and unknowns:** H1–H4 in §6; real false-positive and false-negative rates of LLM review; energy cost of LLM audits; actual upstream-backport volume.
- **Important contradictory or null evidence:**
  - (a) A competitor's public comparison reports low cross-tool agreement and calls Aikido noisy on test-fixture secrets. Anonymous HN comments raise the same issue and plan caps hidden under "fair-usage" (E0).
  - (b) Safe Chain had a minimum-age bypass fixed on 2026-09-03.
  - (c) keyv scope grew from about 11 packages listed in the original post to "at least 444 packages (across 1381 versions)" in the post's own 2026-08-05 update, repeated as "444+" in changelog #53. This is an update, not a contradiction.
  - (d) CVE-2026-40175 still carries an 8.1 ADP score, while the CNA/NVD score is 4.8.
  - (e) The FedRAMP link resolves to the Knox Systems package. *Corrected 2026-10-16:* the page's embedded data lists "Aikido for Government" as a service under that package (dateAvailable 2026-09-28). The earlier note that the page does not name Aikido was wrong.
  - (f) GHSA records for Mastra (04:55Z), Bitwarden and tensorlake predate or coincide with Aikido's posts, so being "first" is not established.
  - (g) A search-tool summary claimed a ~$70M Root price, and no source read supports it.
  - (h) No status-page incidents were published in the window. That is absence of disclosure, not proof of zero incidents.
- **#56 candidates (not minted):** SiliconANGLE 2026-06-30 (Root); Infosecurity Magazine 2026-06-17 (JetBrains plugins; relays Aikido); OpenJS Foundation 2026-09-25 (SSP); Audn.AI 2026-09-18 (competitor comparison; interested party); Help Net Security 2026-08-27 (ecosystem context). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

A second agent re-fetched the cited sources on 2026-10-16 and compared each figure, date and quote with the raw text. Robots.txt was checked first for every host. No host fetched has Claude- or Anthropic-specific rules; The New Stack disallows `anthropic-ai`, `ClaudeBot` and `Claude-Web` and was correctly left unread. The original screen fetched `pypi.org/pypi/aikido_zen/json`, which PyPI's robots.txt disallows (`/pypi/*/json`). No ledger row depends on it: the in-window upload count was re-confirmed from the allowed PyPI RSS feed, and the licence value from that endpoint is unverifiable. No row was marked `E0_UNVERIFIABLE_ROBOTS_DISALLOWED_SOURCE`.

| Row | Outcome | Note |
|---|---|---|
| CI2026-098-001 | corrected (minor) | NVD history confirms the CNA change on 2026-04-16 (critical-equivalent vector to 4.8) and an 8.1 ADP score. The ADP first added a 9.0-equivalent scope-changed vector on 2026-06-30 and revised it to 8.1 on 2026-08-06; the limitation now says so. The quote about validating with the reporting researcher is confirmed |
| CI2026-098-004 / 008 / 030 / 033 | confirmed | Safe Chain release timestamps (1.5.0 2026-04-20T21:56Z, 1.5.2 2026-05-04T12:52Z, 1.5.16 2026-09-03T08:51Z, 1.5.21 2026-09-25T10:29Z) match. 27 in-window releases. 1.5.2 notes contain "Bind registry proxy to loopback only" and checksum validation |
| CI2026-098-005 | confirmed | npm `@bitwarden/cli` 2026.4.0 time 2026-04-22T21:22:59Z and no longer served; GHSA-g98r-qjhg-4fmr published 2026-04-23T17:07:51Z |
| CI2026-098-006 | confirmed | All four package versions, the preinstall hook and the "11.7 MB" payload are in the post. `@cap-js/sqlite` 2.2.2 published 2026-04-29T11:25Z and no longer served |
| CI2026-098-009 | confirmed | "25–74%", "Up to 2×", "1.74 million binary downloads from GitHub releases", "2,000+", "10 security companies" are verbatim. Ten named co-forking vendors, including Aikido. Repo LGPL-2.1 |
| CI2026-098-012 | confirmed | "roughly 70-80% of what a full pentest engagement surfaces, at around 10x lower cost", "Based on our internal testing and early users"; credits pricing confirmed |
| CI2026-098-013 | confirmed | "At least 15", "seven vendor accounts", "close to 70,000"; inflation caveat present. Infosecurity Magazine (2026-06-17) relays "around 70,000" |
| CI2026-098-014 | confirmed | 141 packages, 01:15–02:00 UTC, 918K, easy-day-js verbatim. npm 1.42.1 at 01:15:13Z; GHSA at 04:55:41Z; RSS pubDate 08:43Z |
| CI2026-098-016 | confirmed | Post says Intel powers default malware blocking for Composer 2.10+. Composer 2.10.0 published 2026-05-28 and its notes mention malware but not Aikido |
| CI2026-098-017 | confirmed | SiliconANGLE (2026-06-30) names "Aikido Security NV", "$37.6 million", "15 to 40 minutes", and states no price. The upstream/paywall wording is in Aikido's post |
| CI2026-098-021 | confirmed | "more than four million packages" and "under 8 minutes" are verbatim |
| CI2026-098-022 | confirmed | 23/26, 88.5%, Kimi K3 update of July 19 confirmed. The page also shows "Last updated on: Sep 1, 2026" |
| CI2026-098-023 | confirmed | "~2%" and default shipping confirmed. Betterleaks is MIT; PR #207 merged 2026-07-01; v1.7.0 2026-07-23 |
| CI2026-098-025 | corrected | Provenance claim and 565M vs 580M inconsistency confirmed. However, the post's own 2026-08-05 update already states "at least 444 packages (across 1381 versions)", so "11 vs 444+" is an update rather than a conflict. Row, report §4/§9(c) and search log corrected |
| CI2026-098-028 | confirmed | 11.7 billion tokens, 10 models, three attempts, 32 vulns, 28 of 32, about $295 verbatim |
| CI2026-098-029 | confirmed | 89 / 68 (76%) / $75; 60 (67%) / $157; 58 (65%) / $125 verbatim; "private benchmark app". The number of runs is not stated explicitly, so "single run" is an inference from "this run" |
| CI2026-098-031 | confirmed | Audn.AI (datePublished 2026-09-18): 235 findings, four shared by all four, Aikido 36 findings, ~52 seconds, only tool running SCA, "Static only. No diff awareness", "Noisy: many 'secrets' are test fixtures" |
| CI2026-098-032 | confirmed | W4A16, 488→328 GB, 32.8%, about one point lower recall, 4×H200 confirmed. HF API: created 2026-09-07, not gated, licence `other`, 2,422 downloads |
| CI2026-098-034 | confirmed | OpenJS "Posted On: September 25, 2026"; Socket and Aikido are inaugural partners; $100,000 minimum annually. Aikido RSS pubDate 2026-09-28 |
| CI2026-098-035 | **wrong → corrected** | The FedRAMP marketplace page (Knox Systems, F1206111371) **does** name Aikido: its embedded data lists "Aikido for Government" with dateAvailable 2026-09-28. The screen had stripped script content before searching. Row, report §4/§9(e) and search log corrected; confidence raised to `E2_GOV_MARKETPLACE_LISTING`. Agency ATO details remain unread |
| CI2026-098-036 | confirmed | Title says "6 languages", slug says "5"; Terraform provider and monthly credit top-ups confirmed |
| CI2026-098-037 | confirmed | npm 0.5.144 at 2026-10-08T01:12:07Z and no longer served; GHSA at 02:54:39Z; "over 100,000" lifetime installs is vendor-reported |

**Counts:** 25 rows checked (22 table lines). 22 confirmed (029 with a caveat noted), 2 corrected (001 minor, 025), 1 wrong and corrected (035); 0 unverifiable. The search log's statement that every ledger figure was regex-confirmed is now qualified, because it missed the 025 and 035 limitation errors. No personal identifier was sent in any request (generic `Mozilla/5.0` User-Agent only; no sec.gov access).

*This is an AI-assisted spot-check, not qualified human review.*
