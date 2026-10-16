# OX Security: provisional six-month technology intelligence screen (100)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](100-ox-security.events.csv) and its [search log](100-ox-security.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 100
- **Research issue:** [#168](https://github.com/MSKazemi/github-trending-1000-study/issues/168). Evidence corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` item was minted here; candidates are listed in §9.
- **Ownership and product boundaries (as of 2026-10-12):**
  - **Entity:** OX Security, an Israeli application-security company with a New York press dateline. A [Globes report (2025-05-07)](https://en.globes.co.il/en/article-israeli-cybersecurity-co-ox-security-raises-60m-1001509728) describes a $60M Series B led by DTCP that brought total funding to $94M. It says the company was founded about three and a half years earlier by two Check Point veterans. This is pre-window baseline.
  - **In-window funding:** the 2026-07-28 release still states "$94 million in total funding, including a $60 million Series B led by DTCP". No in-window funding round, acquisition of OX, or layoff story was found.
  - **Brands:** OX owns the open-source **MegaLinter** project. The GitHub org `megalinter` is described as "MegaLinter is now part of OX Security", and the code lives at [oxsecurity/megalinter](https://github.com/oxsecurity/megalinter) (AGPL-3.0). The acquisition date was not verified.
  - **Corporate filings:** not checked. OX is private, and SEC EDGAR was deliberately not contacted.
- **Product URL and company newsroom:**
  - [ox.security](https://www.ox.security/) — **not readable**: every page returned a Cloudflare 403 challenge; only the sitemaps could be read.
  - [docs.ox.security](https://docs.ox.security/) (GitBook, readable, no release notes)
  - OX releases on [PR Newswire](https://www.prnewswire.com/search/news/?keyword=OX%20Security)
  - GitHub orgs [oxsecurity](https://github.com/oxsecurity) and [megalinter](https://github.com/megalinter)
  - npm packages `@oxappsec/ox-cli` and `ox-vibesec-demo-package`
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). The ledger has 23 rows across all seven calendar segments; October has one row.
- **Source coverage:**
  - **Primary sources:** 8 PR Newswire releases (4 in window); 4 MegaLinter GitHub releases with npm timestamps; the GitHub org repo list; npm registry JSON; 6 OX docs pages.
  - **Independent and third-party sources:** NVD API (4 CVEs); OSV API for 119 OpenSSF malicious-package records; The Register; CSA Labs; the LiteLLM security blog; Decrypt; WorkOS; HN Algolia (no relevant stories); 10 web searches.
  - **Not obtained:** the OX blog and research posts, which are known only as sitemap URLs (E0). VentureBeat (429) and BleepingComputer (403) were inaccessible.

## 1. Search and inclusion audit

This is a summary only. Exact requests and exclusions are in the [search log](100-ox-security.search-log.md). Web-search totals were not shown, so they are recorded as unknown, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | ox.security sitemaps | post/newsroom/resources/page sitemaps, lastmod in window | 253 post URLs | 253 (titles only) | 0 | all (pages unreadable; lastmod ≠ publication) | Cloudflare 403 on every page |
| 2026-10-16 | PR Newswire search | keyword `OX Security` (2 variants, 2 pages) | 8 | 8 | 4 | 4 pre-window | wire coverage only |
| 2026-10-16 | GitHub API + npm registry | oxsecurity/megalinter org repos, releases, advisories; npm packages | 4 releases, 14 repos, 2 packages | all | 7 rows | routine repos | no changelog for ox-cli |
| 2026-10-16 | NVD API, GHSA, OSV API | 4 CVEs; GHSA-c9gw-hvqq-f33r; 119 OpenSSF records matching "OX Security" | 4 + 1 + 119 | all | 7 rows | CVE-2026-63764 (no OX link) | code-search index may be incomplete |
| 2026-10-16 | HN Algolia + 10 web searches | OX Security, MCP STDIO, Shai-Hulud, MCP governance, funding, October | 1 HN (unrelated) + unknown | ~95 | 5 rows | aggregators, inaccessible outlets | VentureBeat 429, BleepingComputer 403 |

## 2. Verified company/product identity and baseline

The products and statuses below are vendor-described ([AINAPP release, 2026-07-28](https://www.prnewswire.com/news-releases/ox-security-becomes-first-prompt-to-runtime-security-platform-leading-the-evolving-ainapp-category-302835427.html); [docs](https://docs.ox.security/vibesec/vibesec)).

| Product | Licence | Status / notes |
|---|---|---|
| **VibeSec**: guidance for AI coding agents, Agent AI-BOM, malicious-dependency blocking, secret protection | proprietary | docs list Claude Code, Cursor, Kiro and VS Code with Copilot; launched 2025-09-30 per search results only (pre-window, not re-read) |
| **OX Code**: SAST/SCA/supply chain, the earlier ASPM product | proprietary | — |
| **OX Cloud**: CNAPP plus runtime sensor | proprietary | launched in window (Sep 16); the runtime sensor ships GPL eBPF components |
| **Agentic Pentester** | proprietary | launched 2026-03-12 (pre-window); the docs page says "**Early Access** … not generally available" |
| **MegaLinter** | AGPL-3.0 repo; npm runner MIT | — |
| **MaskerLogger** | MIT | no in-window release |
| **ox-cli** | npm, "SEE LICENSE IN LICENSE" | — |

**Pre-window baseline (context only, not counted):**
- PR Newswire releases: Agentic Pentester (2026-03-12), a 2026 AppSec benchmark report (2026-03-17), a Tenable integration (2026-03-19) and an AI-code report (2025-10-23).
- Funding: Series B (2025-05-07).

**MCP STDIO research timeline:** OX's research began in November 2025 according to The Register. LiteLLM states that OX published the advisory on April 15, 2026. OX's own pages for that disclosure could not be read.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | MCP STDIO "by design" disclosure (Apr 15), with downstream CVEs for Flowise (critical) and Windsurf; LiteLLM fix statement (Apr 21); empty `ox-vibesec` "Claude Code plugin marketplace" repo (Apr 23) | [GHSA](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-c9gw-hvqq-f33r), [LiteLLM](https://docs.litellm.ai/blog/mcp-stdio-command-injection-april-2026) | [The Register](https://www.theregister.com/security/2026/04/16/mcp-design-flaw-puts-200k-servers-at-risk-researcher/5222022), [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-by-design-rce-ox-security-20260420/) | OX advisory unreadable; scale figures are OX estimates |
| 2026-05 | ox-cli 0.47.0 (May 4); MegaLinter v9.5.0 freezes Docker Hub at v9.4.0 (May 16); first OX-credited OpenSSF records (May 20, May 25 PhantomSub); Shai-Hulud clone attribution (May 17) | [v9.5.0](https://github.com/oxsecurity/megalinter/releases/tag/v9.5.0), [OSV](https://osv.dev/vulnerability/MAL-2026-4519) | [Decrypt](https://decrypt.co/368477/shai-hulud-what-know-malware-spreading-software-pipelines) | BleepingComputer inaccessible |
| 2026-06 | Gartner MQ "Leader" claim (Jun 18); MegaLinter v9.6.0 (Jun 28) | [PRN](https://www.prnewswire.com/news-releases/ox-security-named-a-leader-in-the-inaugural-gartner-magic-quadrant-for-software-supply-chain-security-302804633.html), [v9.6.0](https://github.com/oxsecurity/megalinter/releases/tag/v9.6.0) | none | no OX-credited OpenSSF records in June |
| 2026-07 | NVD CVE-2026-30623 for LiteLLM at CVSS 9.8 (Jul 15); AINAPP "prompt-to-runtime" repositioning with a 70–90% claim (Jul 28) | [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-30623), [PRN](https://www.prnewswire.com/news-releases/ox-security-becomes-first-prompt-to-runtime-security-platform-leading-the-evolving-ainapp-category-302835427.html) | none | no MegaLinter release; no OX-credited OpenSSF records |
| 2026-08 | MegaLinter v10.0.0 with coding-agent skills and Gitleaks→betterleaks (Aug 8); demo npm package (Aug 11); ClickFix npm phishing records (Aug 26) | [v10.0.0](https://github.com/oxsecurity/megalinter/releases/tag/v10.0.0), [OSV](https://osv.dev/vulnerability/MAL-2026-15607) | none found | 19 OX-credited OpenSSF records |
| 2026-09 | MegaLinter v10.1.0 agent plugin and LLM Advisor provider (Sep 5); **OX Cloud launch** (Sep 16); **15,465-MCP-server report** (Sep 24) | [v10.1.0](https://github.com/oxsecurity/megalinter/releases/tag/v10.1.0), [PRN](https://www.prnewswire.com/news-releases/ox-security-launches-ox-cloud-redefining-cloud-security-for-the-agentic-era-302879668.html), [PRN](https://www.prnewswire.com/news-releases/new-research-mcp-servers-connect-ai-agents-to-china-russia-home-networks-and-abandoned-domains-302888066.html) | [WorkOS](https://workos.com/blog/mcp-governance-gap) (vendor commentary) | 35 OX-credited OpenSSF records |
| 2026-10-01..12 | PhantomSub OpenSSF records continue (45 OX-credited, through Oct 12); ox-cli 0.70.0 (Oct 5) | [OSV](https://osv.dev/vulnerability/MAL-2026-17381) | none found | no press release, no MegaLinter release (76 maintenance commits) |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](100-ox-security.events.csv): 23 rows, IDs `CI2026-100-001`…`023`. Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-100-003 | 2026-04-16 / research since Nov 2025 | MCP STDIO: OX says Anthropic declined to change the protocol ("expected"); 10 high/critical CVEs; OX estimates >150M downloads and up to 200,000 servers | Disclosure only; Anthropic did not respond to the outlet | [The Register](https://www.theregister.com/security/2026/04/16/mcp-design-flaw-puts-200k-servers-at-risk-researcher/5222022) (news) | [CSA note](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-by-design-rce-ox-security-20260420/) | E1 (secondary) |
| CI2026-100-001 | 2026-04-15 | Flowise CVE-2026-40933 (CVSS 9.9), fixed in 3.1.0; NVD cites OX posts | Authenticated attacker required | [GHSA](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-c9gw-hvqq-f33r) | [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-40933) | E2 |
| CI2026-100-005 / -014 | 2026-04-21 / 07-15 | LiteLLM says the issue was authenticated-only and fixed in v1.83.6-nightly; NVD later records CVSS 9.8 | **Conflict** on severity, unresolved | [LiteLLM](https://docs.litellm.ai/blog/mcp-stdio-command-injection-april-2026), [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-30623) | each other | E2 |
| CI2026-100-008 | 2026-05-16 | MegaLinter publishes only to ghcr.io "until OIDC-based publishing to Docker Hub is implemented"; Docker Hub frozen at v9.4.0 | Users on Docker Hub tags silently stay on v9.4.0 | [release](https://github.com/oxsecurity/megalinter/releases/tag/v9.5.0) | npm 9.5.0 upload | E2 |
| CI2026-100-016 | 2026-08-08 | MegaLinter v10: agent skills (`npx skills add oxsecurity/megalinter`), Gitleaks removed for betterleaks, 5-min linter timeout, main image 4.55→4.13 GB | Breaking; image sizes maintainer-reported | [release](https://github.com/oxsecurity/megalinter/releases/tag/v10.0.0) | npm 10.0.0 upload | E2 |
| CI2026-100-015 | 2026-07-28 | AINAPP platform; VibeSec customers saw a "70–90% reduction in newly introduced vulnerabilities" | No method, denominator or comparator | [PRN](https://www.prnewswire.com/news-releases/ox-security-becomes-first-prompt-to-runtime-security-platform-leading-the-evolving-ainapp-category-302835427.html) | none | E1 |
| CI2026-100-020 | 2026-09-16 | OX Cloud: AIDR and Agentic Attack Surface Management plus CNAPP | "Available now" (vendor); runtime sensor docs predate the launch | [PRN](https://www.prnewswire.com/news-releases/ox-security-launches-ox-cloud-redefining-cloud-security-for-the-agentic-era-302879668.html) | [docs](https://docs.ox.security/ox-cloud/ox-runtime-sensor/gpl-licensed-components-and-source-availability) | E1 |
| CI2026-100-021 | 2026-09-24 | 15,465 MCP servers; 15.6% of 5,095 hostnames outside the US; six $4–$12 unregistered domains; Always-Allow escalation with Haiku 3.5, blocked by Opus 4.6/4.7 | Vendor report; location ≠ risk; no exploitation shown | [PRN](https://www.prnewswire.com/news-releases/new-research-mcp-servers-connect-ai-agents-to-china-russia-home-networks-and-abandoned-domains-302888066.html) | [WorkOS](https://workos.com/blog/mcp-governance-gap) restatement | E1 |
| CI2026-100-011 / -023 | 2026-05-25 → 10-12 | 76 OX-credited OpenSSF records for the PhantomSub WhatsApp-library fork family; 104 OX-credited records in total | Third-party database; finder-stated family size | [OSV](https://osv.dev/vulnerability/MAL-2026-4519), [OSV](https://osv.dev/vulnerability/MAL-2026-17381) | [ossf/malicious-packages](https://github.com/ossf/malicious-packages) | E2 |
| CI2026-100-006 | 2026-04-23 | `ox-vibesec` "Claude Code plugin marketplace" repo created | **Empty** (size 0, no licence) at access | [GitHub](https://github.com/oxsecurity/ox-vibesec) | GitHub API | E2 (null artifact) |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change or documented capability | Class |
|---|---|---|
| Agent-time governance (VibeSec) | Prompt analysis, with security guidance sent to the agent before code generation. Agent AI-BOM of MCP servers, SaaS and models, including per-developer usage. Malicious-dependency blocking for npm and pip: a whole install is blocked if one dependency is malicious. Agent Activity Log keeps 7 days. Unsupported Copilot models (Gemini 2.5, GPT-4) must be disabled | documented; release dates unknown |
| Cloud/runtime | OX Cloud AIDR, AASM and CNAPP; runtime sensor with GPL eBPF (source on request for three years; earliest request date 2025-10-15) | shipped (vendor) |
| Pentesting | Agentic Pentester (white-box, code-aware) | vendor says available; docs say Early Access |
| Research output | MCP STDIO disclosure (Apr); MCP governance report (Sep); 104 OpenSSF malicious-package records (May–Oct) | observed (third-party records) |
| Open source (MegaLinter) | 4 releases; agent skills and plugin; betterleaks; Docker Hub freeze; per-linter timeout; prerun mode; LLM Advisor provider; Biome, OpenTofu and ApexGuru linters | shipped (E2) |
| Packages | ox-cli: 13 npm versions in window, proprietary bundle, no changelog; a do-nothing demo package published to public npm | observed |
| Licensing | MegaLinter AGPL-3.0 (npm runner MIT); MaskerLogger MIT; `ox-vibesec`, `ox-ide` no licence; runtime sensor GPL eBPF components | observed via GitHub/npm/docs |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "every decision our team has made has been about one thing: securing autonomous systems" | [2026-07-28](https://www.prnewswire.com/news-releases/ox-security-becomes-first-prompt-to-runtime-security-platform-leading-the-evolving-ainapp-category-302835427.html) | none | strategic statement | "First" and AINAPP are self-declared categories |
| Platform "governs AI users and agents at the point of the prompt … enforces policy at runtime" | same | none | uncommitted beyond "available now" | Agentic Pentester docs still say Early Access |
| MegaLinter images on ghcr.io only "until OIDC-based publishing to Docker Hub is implemented" | [v9.5.0, 2026-05-16](https://github.com/oxsecurity/megalinter/releases/tag/v9.5.0) | none | tentative (OSS project) | No date; v10.0.0 notes (2026-08-08) still say images are "only published on GitHub Container Registry since v9.5.0"; Docker Hub tags not checked directly |
| Security teams "need to know what it's doing" (agents in cloud) | [2026-09-16](https://www.prnewswire.com/news-releases/ox-security-launches-ox-cloud-redefining-cloud-security-for-the-agentic-era-302879668.html) | none | product positioning | — |
| MCP "does not establish where a server should run, who should operate it…" | [2026-09-24](https://www.prnewswire.com/news-releases/new-research-mcp-servers-connect-ai-agents-to-china-russia-home-networks-and-abandoned-domains-302888066.html) | none | advocacy, not a product commitment | Protocol owner's view not obtained |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: AppSec vendors shift the control point from CI scans to the **agent loop** (prompt guidance, MCP inventory, install-time dependency blocking) | VibeSec docs; AINAPP repositioning; MegaLinter agent skills; empty plugin-marketplace repo shows intent ahead of artifact | Category marketing; buyers may keep CI scanning as the enforcement point | Controlled tasks show no fewer accepted vulnerabilities with prompt-time guidance than with CI-only scanning; vendors return to CI-centric messaging | low; the only outcome figure (70–90%) has no method |
| H2: **Protocol-level "by design" risks** in agent tooling are settled downstream, one CVE per consumer, rather than at the protocol root | MCP STDIO: Anthropic declined the change; multiple downstream CVEs (Flowise, Windsurf, LiteLLM); CSA recommends allowlisting | The behaviour is a reasonable trust boundary (the configuring user is trusted); severity disputed (LiteLLM: authenticated only) | MCP SDKs ship a default-deny or allowlist for STDIO commands; downstream CVE flow stops | moderate that the pattern held in 2026; unknown later |
| H3: **Malicious-package detection becomes a shared commons**, with vendor findings flowing into OpenSSF/OSV and co-credited across competitors | 104 OX-credited records, 38 co-credited with Amazon Inspector, others with Aikido, Socket, Wiz and SafeDep | Credit is marketing; record counts reflect campaign structure (76 forks of one family), not detection breadth | Vendors stop contributing or move findings behind paywalls; OSV records stay single-vendor | moderate on sharing; low on the value of counts |
| H4: OSS tools owned by security vendors keep shipping **breaking supply-chain changes** that shift work onto users | Docker Hub freeze; Gitleaks removal; 14 linters removed; Docker-socket runtime removed | Normal major-version hygiene; the changes reduce attack surface | Few user-reported breakages; smooth automated migration | low; user impact not measured |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Security guidance injected into agent context; agent skills for linters | Compare frozen agent tasks with and without a pre-generation guidance or skill step | Guidance ignored, or it adds tokens without fewer defects | Consented, offline tasks only |
| M2 accepted task quality | 70–90% vendor claim vs independent results | Hidden security acceptance tests; all attempts in the denominator | No difference in accepted-and-secure rate | Vendor figures never used as outcomes |
| M3 discoverability | Wire releases and "first"/"Leader" claims; no HN traction found for OX stories | Separate attention from adoption | Attention is not reuse | Press counts are not an outcome |
| M4 verified third-party reuse | MegaLinter (2,615 stars at access) and OpenSSF records reused by OSV consumers | Trace consented repos that actually run MegaLinter at a pinned version | Stars without execution | Pinned version plus executed CI logs only |
| M5 rights/security/provenance | AGPL tool, MIT runner, unlicensed repos, GPL eBPF on request; downstream CVEs; malicious-package records | Licence and provenance check before reuse; OSV lookup on every dependency added | Licence or CVE presence says nothing about efficacy | Licence files at a pinned commit |
| M6 review/maintenance and lifecycle cost | 4 MegaLinter releases with breaking changes; multi-GB images | Measure upgrade minutes and CI wall-time per pinned version | Upgrades are cheap in practice | No kWh/CO2e inferred from image size |
| M7 actionable interventions | Pin images by digest; allowlist MCP STDIO commands; check new dependencies against OSV | See §8 | Guardrails add friction without catching anything | Synthetic tasks until approval |

Company claims ("first", "Leader", 70–90% reduction) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study): the stdlib-only Python package `trending_study`, `scripts/`, `research/` and the existing `ci.yml`. The task runs offline. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Reuse OX's open-source **MegaLinter** with the `python` flavor, pinned by image digest at v10.1.0 from `ghcr.io`. Run it as an **opt-in, non-blocking** CI job on pull requests, and compare it with the current CI (unit tests on Python 3.10/3.12/3.13/3.14 plus repository validators). Enable only:
- Python linters;
- the bundled betterleaks secret scanner;
- markdown lint (no link checker, since link checkers need network access).

Do **not** enable the LLM Advisor, ApexGuru or any linter that sends code to an external service. Do not use VibeSec, OX Cloud or any paid account. Do not install agent skills.

**Rights check first:** a human must confirm that running the unmodified AGPL-3.0 image in CI creates no obligation for this repository. Reuse comes first, and no new linter configuration beyond a minimal `.mega-linter.yml` is written.

**Treatment/control and frozen comparable task:**
- **Tasks:** freeze 10 small change tasks, for example a CSV-validator edge case, a CLI flag, a docs table fix or a search-log row. At least three contain a planted defect: a hardcoded token-like string, a broken relative link, and an unsafe `subprocess` call.
- **Hidden tests:** a person other than the patch author writes the hidden acceptance tests and keeps them out of the author's context.
- **Arms:** Arm A is the current CI. Arm B is the current CI plus the MegaLinter job. Task order is randomized.
- **Accepted-task unit:** one PR that passes the hidden functional checks and is accepted by the human reviewer without rework.

**Success and guardrails:**
- **Primary measure:** planted defects caught before merge / all planted defects, plus accepted tasks / all 10 assigned (failed and abandoned tasks included).
- **Secondary measures:** findings per PR, findings the reviewer judges as false positives, triage minutes, and added CI wall-clock minutes.
- **Guardrails:**
  - existing CI stays green and required;
  - no new runtime dependency;
  - no network egress beyond pulling the pinned image;
  - no source code sent to an external service;
  - no paid API spend without explicit approval;
  - commit authorship and attribution stay exactly as the maintainer's existing hooks require.
- **Measured human work:** setup minutes, per-PR triage minutes, and minutes spent on upgrades.
- **Energy:** no energy or CO2e estimate unless metered.

**Stop/reversal rule:** remove the job if any of these holds:
- Arm B catches no planted defect that Arm A missed.
- More than half of its findings are judged false positives.
- It adds more than 10 CI minutes or 5 triage minutes per PR on average.
- A pinned-version upgrade breaks it during the trial.

**No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):**
  - 4 MegaLinter releases (v9.5.0–v10.1.0) with GitHub and npm timestamps, including breaking supply-chain changes.
  - ox-cli: 13 npm versions in window.
  - The empty `ox-vibesec` repo and a demo npm package.
  - Downstream advisories that reference OX's MCP STDIO research (Flowise, Windsurf, LiteLLM).
  - 104 OX-credited OpenSSF malicious-package records.
- **Claims/announcements only:**
  - Gartner MQ "Leader" (report not read).
  - AINAPP "first" and the 70–90% figure.
  - OX Cloud availability.
  - The MCP governance figures.
  - The MCP STDIO scale estimates (150M downloads, 200,000 servers).
  - Shai-Hulud clone attribution.
- **Conjectures and unknowns:**
  - H1–H4 in §6.
  - The whole OX blog, research and newsroom corpus (unreadable).
  - Exact VibeSec feature release dates.
  - The MegaLinter acquisition date.
  - Whether Docker Hub publishing resumed after 2026-08-08.
- **Important contradictory or null evidence:**
  - LiteLLM says its issue needed authentication and was patched in April; NVD later lists CVSS 9.8 (CI2026-100-005 vs -014).
  - Anthropic called the STDIO behaviour expected. OX disputes this, and CSA calls the published scale a lower bound. Neither side's figures were independently measured.
  - The Agentic Pentester docs page says "Early Access … not generally available", while the July release says the four-component platform is "available now".
  - The `ox-vibesec` "plugin marketplace" repo was empty at access.
  - mega-linter-runner 9.6.0 reached npm 10 days after the GitHub release.
  - The ClickFix malware advisory (GHSA) followed the OSV record by about four weeks.
  - The Register's meta timestamp (22:45Z) differs from its byline (23:45 UTC).
  - The Shai-Hulud typosquat name differs between the quoted text and search snippets.
  - No HN story about OX research was found, and no in-window tier-1 coverage beyond The Register was read.
- **#56 candidates (not minted):**
  - The Register 2026-04-16 (independent report).
  - CSA Labs 2026-04-20 (secondary analysis).
  - LiteLLM 2026-04-21 (affected-project statement).
  - Decrypt 2026-05-20 (secondary report).
  - WorkOS 2026-09-29 (vendor commentary; restates OX numbers).
  Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned. The PR Newswire releases are single first-party sources and must not be counted as independent.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

A second agent re-fetched the cited sources on 2026-10-16 and compared each figure, date and quote with the raw text or API response. Robots.txt was checked first for every host. The Register disallows `*` but explicitly allows `Claude-User`, so the original screen's truthful `Claude-User` fetch falls under the contract exception, and this check repeated it the same way. VentureBeat (HTTP 429), BleepingComputer (robots 403) and the Cloudflare-challenged www.ox.security pages were correctly left unread and not bypassed. No other disallowed path was fetched, so no row needed `E0_UNVERIFIABLE_ROBOTS_DISALLOWED_SOURCE`.

| Row | Outcome | Note |
|---|---|---|
| CI2026-100-001 | confirmed | Repo advisory 2026-04-15T13:36:44Z, global 2026-04-16T21:18:17Z, critical, patched 3.1.0; NVD 9.9 from the GitHub CNA; NVD references cite two OX posts |
| CI2026-100-002 | confirmed | NVD published 2026-04-15T16:16Z, status Deferred, ADP CVSS 8.0, Windsurf 1.9544.26; only reference is the OX advisory URL |
| CI2026-100-003 | confirmed | "as many as 200,000 servers", "more than 150 million downloads", "10 (so far) high- and critical-severity CVEs", "This change didn't fix anything", "Anthropic did not respond". JSON-LD 22:45Z vs byline 23:45 UTC confirmed |
| CI2026-100-004 | confirmed | CSA note (Published 2026-04-20): nine days, 150 million / 7,000-plus / up to 200,000, "lower bound than a ceiling", allowlist advice, four SDK languages |
| CI2026-100-005 | confirmed | datePublished 2026-04-21; "On April 15, 2026, OX Security published", v1.83.6-nightly, commit 7b7f304, PR #25343, v1.83.7-stable, "not exploitable by unauthenticated users" |
| CI2026-100-006 | confirmed | GitHub API: created and pushed 2026-04-23T09:28:47Z, size 0, no licence, description verbatim |
| CI2026-100-007 | confirmed | 13 in-window versions, 0.47.0 (2026-05-04) to 0.70.0 (2026-10-05); 0.72.0 on 2026-10-14; "SEE LICENSE IN LICENSE"; single `bundle.js` bin, no dependencies |
| CI2026-100-008 / 013 / 016 / 019 | confirmed | GitHub release and npm upload times match (9.6.0 gap 06-28 → 07-08 confirmed). v9.5.0 ghcr-only and Docker Hub frozen at v9.4.0; v10.0.0 "Removed 14", REPOSITORY_BETTERLEAKS, 300 s timeout, prerun, payload v2, 4.55 GB → 4.13 GB (-9%); v10.1.0 OrcaRouter, Biome, OpenTofu, ApexGuru, three sub-agents. MegaLinter repo AGPL-3.0, runner MIT |
| CI2026-100-009 | confirmed | OSV MAL-2026-4196 published 2026-05-20T08:33Z, credits OX Security, pinno-loggers → terminal-logger-utils postinstall dropper |
| CI2026-100-010 | confirmed | Decrypt: "On Sunday", wallet/SSH/env theft, DDoS botnets, "almost exact copy of the leaked source code", TeamPCP. The page text says "chalk-template". `datePublished` 2026-05-20T23:00:04 carries no timezone, so the UTC date is as displayed |
| CI2026-100-011 / 023 | confirmed | MAL-2026-4519 (2026-05-25, Amazon Inspector + OX, "100+ identified as of September 2026", modified 2026-09-30) and MAL-2026-17381 (2026-10-12, OX). Re-running the code search gave 119 hits; the OSV API gave 104 OX-credited records (May 5, Aug 19, Sep 35, Oct 45), 76 citing the PhantomSub post from 2026-05-25 to 2026-10-12 — identical to the screen |
| CI2026-100-012 | confirmed | PR Newswire 2026-06-18 12:11 ET; report dated June 17, 2026, ID G00843814; Gartner disclaimer present; three principles verbatim |
| CI2026-100-014 | confirmed | NVD published 2026-07-15T22:16Z, Awaiting Analysis, ADP 9.8 with PR:N, LiteLLM 1.18.10; references the LiteLLM blog and the OX advisory |
| CI2026-100-015 | confirmed | "70–90% reduction" in "benchmark testing", Copilot/Cursor/Claude Code, "available now to customers", "$94 million … $60 million Series B led by DTCP" |
| CI2026-100-017 | confirmed | npm 1.0.0 at 2026-08-11T07:30:59Z, MIT, description verbatim |
| CI2026-100-018 | confirmed | MAL-2026-15607 published 2026-08-26, index.html only, no lifecycle script; GHSA-4vx3-9fv9-qg2m (malware) published 2026-09-23T02:44Z |
| CI2026-100-020 | confirmed | AIDR, AASM, CSPM/KSPM/DSPM, reachability prioritisation, "available now"; docs GPL page gives "earliest request date is October 15, 2025" |
| CI2026-100-021 | confirmed | 15,465 / 5,095 / 15.6% (796) / 19 China / 18 Russia / 0.45% / 2.3% / six domains / $4–$12 / Always-Allow with Haiku 3.5, blocked by Opus 4.6 and 4.7 — all verbatim |
| CI2026-100-022 | confirmed | WorkOS post dated 2026-09-29; restates "15,465 MCP Servers, 0 Governance" across three registries |
| Entity baseline | confirmed | Globes (2025-05-07): $60M Series B led by DTCP, $94M total, founded about three and a half years earlier by Check Point veterans; GitHub org `megalinter` description verbatim |

**Counts:** 23 of 23 ledger rows checked, plus the entity baseline. 23 confirmed, 0 corrected, 0 wrong, 0 unverifiable. The search log's statement that ledger figures were checked against raw text held for every row checked here. No personal identifier was sent in any request (generic `Mozilla/5.0`, or truthful `Claude-User` for The Register only; no sec.gov access).

*This is an AI-assisted spot-check, not qualified human review.*
