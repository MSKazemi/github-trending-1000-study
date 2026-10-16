# Chainguard — provisional six-month technology intelligence screen (094)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](094-chainguard.events.csv) and [search log](094-chainguard.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 094
- **Research issue:** [#162](https://github.com/MSKazemi/github-trending-1000-study/issues/162); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Chainguard, Inc. (NIST CMVP vendor name), datelined Kirkland, Washington in its press releases; privately held and venture-funded. No parent company, acquirer or in-window acquisition was found. Pre-window baseline only: a $356M Series D in April 2025 (listed on the [newsroom](https://www.chainguard.dev/newsroom)) and [$280M growth financing from General Catalyst's Customer Value Fund on 2025-10-23](https://www.prnewswire.com/news-releases/chainguard-announces-280-million-growth-financing-from-general-catalyst-to-usher-in-next-era-of-trusted-open-source-software-302592279.html). No in-window funding round was found. Filing-level corporate verification was **not** performed (SEC/EDGAR deliberately not contacted).
- **Product URL and company newsroom:** [chainguard.dev](https://www.chainguard.dev/), [Unchained blog](https://www.chainguard.dev/unchained) ([RSS](https://www.chainguard.dev/unchained/rss.xml)), [newsroom](https://www.chainguard.dev/newsroom), [Chainguard Academy changelog](https://edu.chainguard.dev/chainguard/changelog/), GitHub orgs [chainguard-dev](https://github.com/chainguard-dev) and [wolfi-dev](https://github.com/wolfi-dev).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 44 ledger rows across all seven calendar segments.
- **Source coverage:** full in-window blog RSS (86 items dated 2026-04-12..10-12; all fetched as raw HTML), rolling Academy changelog (entries visible back to 2026-07-22 only), PR Newswire releases, GitHub API (repos, releases, issues, commits), NIST CMVP, Hacker News via the Algolia API, and independent outlets whose robots.txt permits Claude agents (Infosecurity Magazine, SiliconANGLE, IT Brief). The New Stack, Bloomberg, ZDNet, Diginomica and The Register were **not fetched** because their robots.txt disallows Claude agents; Axios and Business Journals were not fetched because their robots.txt returned HTTP 403. See the [search log](094-chainguard.search-log.md).

## 1. Search and inclusion audit

Summary only; exact requests, opened URLs and exclusions are in the [search log](094-chainguard.search-log.md). No web-search engine was used; result totals are therefore not applicable rather than zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | chainguard.dev RSS + raw HTML | all Unchained items 2026-04-12..10-12 (+8 dated 10-13/14 for context) | 86 in window | 86 fetched, ~45 read | 33 rows | 53 (opinion, explainers, guest posts, repeated incident notices, events; see log) | RSS gives `pubDate` only; edits not detectable |
| 2026-10-16 | edu.chainguard.dev changelog | weekly entries | 12 weekly sections visible | all "Product Announcements" | 5 rows (+5 rows corroborated) | image additions/EOL tables, minor admin features | rolling page; Apr 12–Jul 21 not displayed |
| 2026-10-16 | GitHub API | `chainguard-dev`, `wolfi-dev` repos, releases, issues | 134 repos; 6 new in window | 14 repos' releases; 8 issues | 4 rows | dependency-bump releases | stars not used as adoption |
| 2026-10-16 | PR Newswire; NIST CMVP | Athena, 1B manifests, Athena members, $280M (baseline) | 4 | 4 | 2 rows (+2 check URLs) | $280M release is baseline only | press releases are first-party |
| 2026-10-16 | HN Algolia API | `chainguard`, `wolfi` stories and comments, 2026-04-12..10-13 | 16 stories, 20 comments, 212 `wolfi` (noise) | all | 0 rows (1 check URL) | user comments are E0 | prefix matching made `wolfi` query mostly irrelevant |
| 2026-10-16 | independent outlets (robots-permitted) | Infosecurity, SiliconANGLE, IT Brief, Minimus | 4 | 4 | 0 own rows (3 check URLs) | restatements of vendor releases | 7 outlets blocked by robots or 403 |

## 2. Verified company/product identity and baseline

Chainguard sells hardened, continuously rebuilt open source artifacts: **Containers** (minimal images on its own **Chainguard OS**, with the community distribution **Wolfi** underneath), **Libraries** (Java, Python, JavaScript packages rebuilt from source; Go and .NET beta in window), **VMs**, **OS Packages**, **Actions** (hardened GitHub Actions), **Agent Skills**, and a hosted **Chainguard Repository** with a policy engine and malware/"greyware" scanning. The build system is the **Chainguard Factory**; **Guardener** is its migration agent. Open source surface: Apache-2.0 build tools [apko](https://github.com/chainguard-dev/apko), [melange](https://github.com/chainguard-dev/melange), [malcontent](https://github.com/chainguard-dev/malcontent), [wolfictl](https://github.com/wolfi-dev/wolfictl), the [wolfi-dev/os](https://github.com/wolfi-dev/os) package definitions (GitHub reports licence NOASSERTION), and Chainguard staff's earlier work on Sigstore. **The hardened image catalogue beyond the free tier, Libraries, the Repository, the scanner and the Factory are proprietary and paid.**

Pre-window baseline (context only, not counted): Assemble NYC (March 2026) launches of Agent Skills, Actions, OS Packages, Guardener, Commercial Builds and Catalog Starter (PR Newswire releases dated 2026-03-17 listed on the newsroom); Libraries free until 2026-06-30 (blog 2026-04-09); "SecDB is the past, OSV is the future" (2026-04-09; `wolfi-dev/advisories` archived, last push 2026-01-07). **Post-window, excluded:** Assemble London (2026-10-13/14) launches of Chainguard Harness, Checks, Workspaces, MCP, Libraries for Go/.NET blog post, and the first "Mythos harness" disclosure.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Docker "hodgepodge" rebuttal (Apr 15); Cursor partnership (Apr 21); npm worm/xinference response (Apr 22); one-day KEV SLA (Apr 28); FIPS EKS add-ons in AWS Marketplace (Apr 30) | [blog](https://www.chainguard.dev/unchained/going-beyond-cves-chainguards-one-day-kev-sla), [blog](https://www.chainguard.dev/unchained/chainguard-and-cursor-partner-to-bring-secure-open-source-artifacts-to-agentic-coding) | Axios (Apr 21) and The New Stack (Apr 24) listed on newsroom, **not fetched** (robots) | elementary-data (Apr 25) and SAP CAP npm (Apr 29) response posts logged, not ledgered |
| 2026-05 | malcontent v1.23.0 (May 6); RHEL 9/10 RPM compatibility + FINOS (May 11); mini Shai-Hulud response (May 13); "The hardest fork" CEO direction (May 28) | [blog](https://www.chainguard.dev/unchained/chainguard-brings-first-party-rhel-9-and-rhel-10-rpm-support-to-chainguard-os-joins-finos), [release](https://github.com/chainguard-dev/malcontent/releases/tag/v1.23.0) | devops.com critical piece (Jun 2 per HN) returned a 403 challenge | Endor Labs (May 19) and Upwind (May 26) partnerships logged; Upwind folded into row 021 |
| 2026-06 | greyware scanner (Jun 9); Athena launch (Jun 15); Agent Skills open beta (Jun 17); cinc-auditor (Jun 18); **Wolfi package migration questioned** (Jun 19); Java Libraries GA (Jun 23); Actions open beta, Cursor plugin/Kiro power, agent-fleet report (Jun 24); Repository policies + JS GA, Wiz (Jun 25); CVE data report (Jun 30) | [PR Newswire](https://www.prnewswire.com/news-releases/chainguard-launches-athena-the-industry-coalition-to-fix-open-source-vulnerabilities-before-attackers-can-find-them-302799984.html), [issue](https://github.com/wolfi-dev/os/issues/78721), [blog](https://www.chainguard.dev/unchained/everything-we-announced-during-ai-readiness-innovation-week) | [Infosecurity Jun 16](https://www.infosecurity-magazine.com/news/chainguard-bny-open-source-athena/); [SiliconANGLE Jun 25](https://siliconangle.com/2026/06/25/exclusive-chainguard-extends-repository-scanning-policies-java-python-containers/) | Gartner MQ Leader (Jun 18/22) logged, not ledgered (analyst recognition, not product evidence) |
| 2026-07 | Bugcrowd bounty Jul 6–27 (Jul 6); Athena expansion to 40,000+ findings (Jul 7); AsyncAPI analysis (Jul 14); Booz Allen ELA (Jul 21); NeuVector OSV ingestion (Jul 24) | [blog](https://www.chainguard.dev/unchained/expanding-athena), [changelog](https://edu.chainguard.dev/chainguard/changelog/) | PR Newswire India (Jul 7) is a vendor duplicate | Wolfi maintainer reply and FAQ update 2026-07-10 recorded on row 015; sandboxing Athena (Jul 29) engineering post logged |
| 2026-08 | Libraries in AWS Security Hub Extended (Aug 4); Guardener GitHub App beta (Aug 12); npm 403 block reasons (Aug 13); SLSA Build L3 assessment claim (Aug 17); API v2 GA (Aug 19) | [blog](https://www.chainguard.dev/unchained/introducing-the-guardener-github-app), [changelog](https://edu.chainguard.dev/chainguard/changelog/) | [IT Brief Aug 6 (NZT)](https://itbrief.co.uk/story/chainguard-joins-aws-security-hub-for-supply-chain) | Go 1.27 images (Aug 31), SCIM EA (Aug 20), PKCE (Aug 3), malware console (Aug 4) logged |
| 2026-09 | JFrog Libraries (Sep 2); 1B build manifests (Sep 3); apko v1.3.0/v1.4.0 (Sep 9/14); CEO "flood" plan + Sovereign Artifacts beta (Sep 15); FIPS 140-3 cert #5523 (Sep 24); first 14 Athena disclosures + Go/.NET Libraries beta in changelog (Sep 28) | [blog](https://www.chainguard.dev/unchained/athenas-disclosures-begin), [NIST](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5523) | NIST CMVP (independent registry); Diginomica (Sep 1) not fetched (robots) | Morgan Stanley award (Sep 30) logged, not ledgered |
| 2026-10-01..12 | Actions GA, malcontent v1.27.0 (Oct 6); Compliance Dashboard GA (Oct 7); Guardener Early Access, Insights "coming weeks" (Oct 8) | [blog](https://www.chainguard.dev/unchained/chainguard-actions-is-generally-available-hardening-1-000-github-actions-and-removing-transitive-ci-cd-risks), [changelog](https://edu.chainguard.dev/chainguard/changelog/) | none in-window | Oct 13–14 Assemble London launches excluded |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](094-chainguard.events.csv) (44 rows, IDs `CI2026-094-001`…`044`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-094-004 | 2026-04-28 | One-day remediation SLA for CISA KEV CVEs in Containers | contractual for CVE-SLA customers; terms not read | [blog](https://www.chainguard.dev/unchained/going-beyond-cves-chainguards-one-day-kev-sla) | none | E1 |
| CI2026-094-012 / 024 / 039 | 2026-06-15 / 07-07 / 09-28 | Athena coalition: 20,000+ → 40,000+ findings (vendor); first 14 silent-fix disclosures with `CGP-` IDs | release re-issued as a correction; promised July disclosure wave slipped to Sep 28; repo has no detected licence | [PR Newswire](https://www.prnewswire.com/news-releases/chainguard-launches-athena-the-industry-coalition-to-fix-open-source-vulnerabilities-before-attackers-can-find-them-302799984.html), [blog](https://www.chainguard.dev/unchained/athenas-disclosures-begin) | [Infosecurity](https://www.infosecurity-magazine.com/news/chainguard-bny-open-source-athena/); [athena repo](https://github.com/chainguard-dev/athena) (14 entries) | E1 / E1 / E2 |
| CI2026-094-015 | 2026-06-19 (merges 2026-06-09, 06-11) | Package definitions moved out of public Wolfi to a private enterprise repository; maintainer says Wolfi covers only packages for free images | in effect; FAQ updated 2026-07-10 | [wolfi-dev/os#78721](https://github.com/wolfi-dev/os/issues/78721) | commits via GitHub API; [FAQ](https://raw.githubusercontent.com/wolfi-dev/.github/main/profile/README.md) | E2 |
| CI2026-094-018 | 2026-06-24 | Cursor Marketplace plugin and Kiro power for hardened artifacts | plugin repo licence NOASSERTION; Kiro repo no licence | [blog](https://www.chainguard.dev/unchained/chainguard-plug-in-now-available-on-cursor-marketplace) | [v0.1.0 release](https://github.com/chainguard-dev/chainguard-cursor-plugin/releases/tag/v0.1.0) | E2 (artifact exists) |
| CI2026-094-019 | 2026-06-24 | Internal agents opened 4,700+ standards-fix PRs in 8 weeks; 75% of low-risk ones auto-merged | self-report; no defect/revert denominator | [blog](https://www.chainguard.dev/unchained/this-shit-is-hard-how-ai-keeps-our-code-on-standard) | none | E1 |
| CI2026-094-020 | 2026-06-25 | Repository malware/greyware scanning and policy engine extended to Python, Java, containers; JS Libraries GA | policy types open beta | [blog](https://www.chainguard.dev/unchained/chainguard-repository-adds-new-policies-chainguard-libraries-for-javascript-is-ga) | [SiliconANGLE](https://siliconangle.com/2026/06/25/exclusive-chainguard-extends-repository-scanning-policies-java-python-containers/) (restatement) | E1 |
| CI2026-094-030 | 2026-08-13 | npm returns 403 with reasons such as `MALWARE_DETECTED` for withheld packages | not exercised | [changelog](https://edu.chainguard.dev/chainguard/changelog/) | — | E2 (documentary) |
| CI2026-094-038 | 2026-09-24 (validated 2026-09-15) | FIPS 140-3 cert #5523 with hybrid ML-KEM key exchange | NIST: Active, Level 1, sunset 2031-09-14 | [blog](https://www.chainguard.dev/unchained/announcing-chainguards-industry-first-validated-fips-140-3-module-delivering-post-quantum-readiness) | [NIST CMVP](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5523) | E2 |
| CI2026-094-040 | 2026-09-28 | Libraries for Go and .NET invite-only beta | blog/PR dated Oct 14 (out of window) | [changelog](https://edu.chainguard.dev/chainguard/changelog/) | — | E2 (documentary) |
| CI2026-094-041 | 2026-10-06 | Actions GA, 1,000+ hardened Actions | 30-day trial; vendor copies | [blog](https://www.chainguard.dev/unchained/chainguard-actions-is-generally-available-hardening-1-000-github-actions-and-removing-transitive-ci-cd-risks) | changelog Oct 6 | E2 (documentary) |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent tooling | Agent Skills open beta + private registry; Actions migration skill; Cursor plugin; Kiro power; Guardener GitHub App and Early Access; npm 403 reason codes | shipped / beta |
| Registry security | greyware/malware scanner (npm → Python, Java, containers); policy engine across artifacts; upstream fallback with cooldown; malware console | shipped / open beta |
| Libraries | Java GA + CVE-remediation beta (Spring ecosystem); JavaScript GA; Go/.NET invite-only beta; JFrog, Wiz, Upwind, AWS Security Hub recognition | GA / beta |
| Containers / OS | KEV one-day SLA; FIPS EKS add-ons; RHEL 9/10 RPM compatibility (preview); cinc-auditor STIG image; Go 1.27 images; Compliance Dashboard GA | shipped / preview |
| Provenance / assurance | SLSA Build L3 assessor claim (Coalfire, report not public); FIPS 140-3 cert #5523; Sovereign Artifacts beta (EU byte storage only) | mixed |
| Vulnerability coordination | Athena coalition; 14 `CGP-` disclosures; Akrites hand-off | operational per vendor |
| APIs | Chainguard API v2 GA; PKCE; SCIM EA; group-role mapping GA | shipped |
| Open source tools | apko 57 releases, melange 41, malcontent 26 (incl. recurring false-positive-reduction rule passes), wolfictl 20 | released, Apache-2.0 |
| Licensing / scope | Wolfi narrowed to packages needed by free images; new repos `chainguard-cursor-plugin` (NOASSERTION), `chainguard-kiro-power`, `chainctl`, `athena` (no detected licence), `cg-skills`, `license` (Apache-2.0) | observed via GitHub API |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "building the infrastructure to fork, maintain, and distribute thousands of them" | [2026-05-28](https://www.chainguard.dev/unchained/the-hardest-fork) | none | uncommitted | Athena patches flow first to members/customers |
| Organisations joining "before the first coordinated disclosure wave next month are covered under embargo" | [PR 2026-06-15](https://www.prnewswire.com/news-releases/chainguard-launches-athena-the-industry-coalition-to-fix-open-source-vulnerabilities-before-attackers-can-find-them-302799984.html) | July 2026 | slipped | First disclosures 2026-09-28 |
| "We start disclosing Athena findings this month, beginning with 50." | [2026-09-15](https://www.chainguard.dev/unchained/the-flood-is-coming-and-the-pipes-were-already-full) | September 2026 | partly delivered | 14 disclosed 2026-09-28 |
| Sandbox, harness and CI tooling: "over the coming quarters, we're going to start opening them up directly" | same | coming quarters | planned | Products announced 2026-10-14 (out of window) |
| Scanner surface "will expand to other language ecosystems" ("Soon") | [2026-06-09](https://www.chainguard.dev/unchained/the-expanding-threat-landscape-chainguard-now-scans-source-code-for-traditional-malware-and-greyware) | soon | delivered 2026-06-25 | — |
| Sovereign Artifacts is "the first milestone on our sovereignty roadmap"; later phases to move auth and builds | [2026-09-15](https://www.chainguard.dev/unchained/announcing-the-sovereign-artifacts-beta) | none | planned | Seeking design partners |
| Insights dashboard "will be available in the coming weeks" | [2026-10-08](https://www.chainguard.dev/unchained/introducing-the-chainguard-console-insights-dashboard-powered-by-guardener) | weeks | planned | — |
| CEO: wants to find out "how far" full vertical integration "can take us" | [2026-10-01](https://www.chainguard.dev/unchained/what-five-years-of-chainguard-have-taught-us) | none | uncommitted | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Package trust for AI coding agents will move to curated registries with policy gates (cooldown, malware/greyware, provenance) rather than per-package human review | Cursor/Kiro integrations; Repository policies; npm 403 reason codes; agent-skill catalog | Registry gating may mainly serve regulated enterprises; open registries may add equivalent defaults (trusted publishing, cooldowns) | Public registries ship comparable default protections and curated-registry uptake stalls; controlled tasks show no fewer malicious installs than plain lockfiles + cooldowns | low–moderate; no task-level data |
| H2: "Free hardened base" scope will narrow as vendors compete, increasing reuse risk for open source projects built on community distributions | Wolfi package migration (Jun 9–11) and maintainer reply; competitor free-tier launch the same month (Minimus, 2026-06-23) | Pruning may be ordinary maintenance-cost control | Wolfi package count grows again or Chainguard restores migrated packages | moderate for "narrowing happened", unknown for trend |
| H3: Pre-disclosure, member-first patch distribution (Athena) will compete with traditional CVE-based disclosure for AI-found bugs | Athena intake claims; `CGP-` identifiers outside CVE; Akrites hand-off | Coalition may converge into existing CNA/OSV processes | `CGP-` items routinely receive CVE/OSV IDs and public patches at the same time as members | low; n=14 disclosures |
| H4: Agent-authored maintenance PRs with deterministic auto-merge gates will become normal in large monorepos | 4,700+ PRs/8 weeks, 75% low-risk auto-merged (self-report) | Survivorship: only easy standards fixes are automated | Published revert/defect rates for auto-merged agent PRs exceed human baseline | low; self-reported |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Agents increasingly configured to pull from curated registries and hardened CI Actions | Count consented repos whose agent configs/plugins point to curated sources | Only enterprises adopt; open source repos unaffected | Config files at pinned commits only |
| M2 accepted task quality | Registry blocks with reason codes may change agent failure modes | Same dependency-adding tasks with public vs curated registry, hidden tests | No accepted-task difference | All attempts, including blocked installs |
| M3 discoverability | Heavy press/award volume (Gartner, Morgan Stanley, Booz Allen) | Separate press counts from reuse | Press ≠ reuse | Stars/press never outcomes |
| M4 verified third-party reuse | Rebuilt packages and backported forks diverge from upstream; Wolfi scope narrowed | Track downstream repos whose builds break after package migration | Few public repos depended on removed packages | Build logs at pinned commits |
| M5 rights/security/provenance | SLSA L3 claim, FIPS cert, unlicensed new repos (`athena`, Kiro power), NOASSERTION plugin, vendor OSV feeds suppressing scanner findings | Licence check before reuse; compare scanner output with/without vendor advisories | Suppression could hide true positives as well as false ones | Repository licence files; scanner versions pinned |
| M6 review/maintenance and lifecycle cost | Agent-authored migration PRs (Guardener) shift review load; 1B build manifests imply continuous rebuild compute | Measure reviewer minutes per migration PR | Migration PRs are trivial to review | No kWh/CO2e inferred from build counts |
| M7 actionable interventions | Dependency cooldown + registry malware gate + SHA-pinned Actions as cheap guardrails | See §8 | Guardrails add friction without blocking real attacks | Synthetic tasks only until approval |

Company adoption claims (e.g., 6,000 Booz Allen engineers, coalition member counts, 1B manifests) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) GitHub Actions workflows and Python dependency intake, run as a **synthetic, network-limited** exercise. The disabled Trending `capture` command stays disabled; no supply-chain product makes unapproved scraping permissible.

**Candidate practice (not yet validated):** Reuse first: pin every third-party GitHub Action to a full commit SHA and add a dependency cooldown (refuse package versions younger than N days) using existing free tooling (Dependabot/Renovate `minimumReleaseAge`-style settings, `zizmor`/`actionlint`, `pip` hash-checking), and compare that with a curated-registry arm (Chainguard Actions / Libraries free trial) only if trial terms permit. Do not build a new scanner.

**Treatment/control and frozen comparable task:** Freeze 10 synthetic maintenance tasks (e.g. add a small pure-Python dependency, bump a test tool, add a CI step), each with **hidden acceptance tests written by someone other than the operator**. Control: current workflow. Arm A: SHA-pinned Actions + 7-day cooldown + hash-checked installs. Arm B (optional, only with approval and no paid spend): Arm A plus curated registry/Actions. Same operator, same tasks, randomized order. Accepted-task unit: a change that passes hidden tests, keeps the full unit suite green, and is accepted by the human reviewer without rework.

**Success and guardrails:** Primary: accepted tasks / all assigned tasks (blocked, abandoned and timed-out included). Security guardrail: a planted, clearly fake "malicious" package version published within the cooldown window (local index only) must be refused in Arms A/B; any install of it is a failure. No real credentials or tokens in the environment; no new runtime dependency kept in the repo after the trial. Measured human work: setup minutes, review minutes per task, minutes spent diagnosing blocked installs. Cost: only invoiced line items if any (none expected); no energy or CO2e estimate unless metered.

**Stop/reversal rule:** Keep the control if Arm A does not block the planted package or adds more than 10 minutes of human work per task on average. Drop Arm B if it requires paid spend, sends repository contents or credentials to a third party, or if licence/terms for the curated artifacts cannot be confirmed. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** NIST CMVP certificate #5523 (Active, Level 1, initial validation 2026-09-15); 14 `CGP-` advisories in `chainguard-dev/athena`; Wolfi package-definition migration commits (2026-06-09, 06-11) and the 2026-07-10 FAQ update; Cursor plugin release v0.1.0 (2026-06-15); in-window release counts for apko (57), melange (41), malcontent (26), wolfictl (20), terraform-provider-chainguard (28) from the GitHub API; changelog-dated launches from 2026-07-22 onward.
- **Claims/announcements only:** customer-safety claims in incident posts; KEV SLA performance; greyware/malware block counts (52,000+; 70+ per week); Athena intake (20,000+ → 40,000+); 886 CVEs remediated Mar–May; 1B manifests / 3,000 images / 675,000 variants; 4,700+ agent PRs and 75% auto-merge; SLSA Build L3 (assessor report not public); 6,000 Booz Allen engineers; future direction items in §5.
- **Conjectures and unknowns:** H1–H4 in §6; real-world false-positive and false-negative rates of the greyware scanner; whether the Go/.NET and JFrog JS/Python follow-ups shipped as stated; changelog content before late July.
- **Important contradictory or null evidence:** (a) Wolfi users publicly objected to packages moved to a private repository without public PRs; Chainguard's answer was that Wolfi only covers free images — a scope reduction for community reusers; (b) Athena's launch release was re-issued as a correction, and the promised July disclosure wave and "beginning with 50" both under-delivered (14 on 2026-09-28); (c) Athena launch dated 2026-06-15 (PR Newswire, 19:38 ET) vs 2026-06-16 (Infosecurity Magazine); (d) Go/.NET Libraries: changelog "Launched September 28, 2026" vs blog/PR dated 2026-10-14; (e) a Hacker News commenter disputed the Docker-rebuttal post's handling of scanners (E0); (f) competitor Minimus launched a free hardened-image Community Edition on 2026-06-23, the same month Wolfi narrowed (relationship not established); (g) the devops.com critical article and The Register's summer-vulnerabilities piece were not read (403 / robots).
- **#56 candidates (not minted):** Infosecurity Magazine 2026-06-16; SiliconANGLE 2026-06-25; IT Brief 2026-08-06; wolfi-dev/os#78721 (community record); NIST CMVP #5523. Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned; vendor-release restatements must not be counted as independent confirmation.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

Raw sources were re-fetched with a generic `Mozilla/5.0` User-Agent after checking robots.txt for `*` and for ClaudeBot / Claude-User / anthropic-ai / Claude-SearchBot / Claude-Web (RFC 9309 longest-match). Every cited path on www.chainguard.dev, edu.chainguard.dev, prnewswire.com, infosecurity-magazine.com, siliconangle.com, itbrief.co.uk, csrc.nist.gov and github.com is permitted. hn.algolia.com and raw.githubusercontent.com return 404 for robots.txt, meaning no rules. The search log's skip decisions were re-confirmed against current robots.txt: thenewstack.io, bloomberg.com, zdnet.com and diginomica.com disallow ClaudeBot/anthropic-ai, theregister.com disallows `/` for `*`, and axios.com robots.txt returns 403. No ledger row relies on a robots-disallowed source, so none was marked `E0_UNVERIFIABLE_ROBOTS_DISALLOWED_SOURCE`.

| Row | Outcome | Note |
|---|---|---|
| CI2026-094-003 | confirmed | 22 npm libraries, xinference 2.6.0–2.6.2, "refuses to build packages that depend on install-time scripts", TeamPCP attribution "still pending". RSS date 2026-04-22 |
| CI2026-094-004 | confirmed | "within one calendar day" KEV SLA, "less than 20-hour average" for Critical, 2-day median |
| CI2026-094-006 | confirmed | malcontent v1.23.0 was published 2026-05-06T21:21Z. 26 in-window releases, v1.22.0 (Apr 15) to v1.27.1 (Oct 7) |
| CI2026-094-008 | confirmed | "A new supply chain worm hit 400+ packages in the last 24 hours. Chainguard customers were not affected". The npm attribution comes from the post's title and context |
| CI2026-094-010 | confirmed | 100,000+ packages a day, 52,000+ blocked, npm upstream fallback |
| CI2026-094-011 | confirmed | "Seventy-seven minutes" (spelled out). Fix landed Apr 30. GitHub advisory database caught up "on May 7, six days later". RSS date 2026-06-10 |
| CI2026-094-012 | confirmed | PR Newswire correction re-issue, 2026-06-15 19:38 ET. Founding-member list, 20,000+ findings, 2,000+ patches, 500 projects, "first wave of disclosures begins next month". Infosecurity Magazine (2026-06-16T11:00Z) says "announced … on June 16" |
| CI2026-094-013 | confirmed | cg-skills repo created 2026-06-22T22:37Z, Apache-2.0 |
| CI2026-094-015 | confirmed | wolfi-dev/os#78721 opened 2026-06-19 and names spark/keycloak plus a "private enterprise repo". Commit 227baf7 (2026-06-09): 29 files, 4,128 deletions. Commit dcf7584 (2026-06-11): 139 files. MEMBER reply on 2026-07-10 matches the paraphrase. The commit message says "move … to enterprise-packages" |
| CI2026-094-018 | confirmed | Licences: cursor plugin NOASSERTION, kiro-power none. Cursor plugin v0.1.0 was published 2026-06-15 |
| CI2026-094-019 | confirmed | "more than 4,700" (4,746) PRs over 8 weeks, 75% auto-merged of those judged low-risk |
| CI2026-094-022 | confirmed | 886 / 377 / 154 CVEs, March–May, "over 63% were high-severity" |
| CI2026-094-023 | confirmed | Bugcrowd event July 6–27, up to $200,000 |
| CI2026-094-024 | confirmed | 40,000+ processed, 42% critical/high. All eight named new members appear, as does Akrites |
| CI2026-094-026 | confirmed | "More than 6,000 Booz Allen engineers will now have access" |
| CI2026-094-030 | confirmed | Changelog "Launched August 13, 2026": npm 403 naming e.g. MALWARE_DETECTED instead of 404 |
| CI2026-094-032 | confirmed | "Launched August 19, 2026": API v2 GA at /v2/ replacing v2beta1, cursor pagination |
| CI2026-094-033 | confirmed | JFrog: Java shipped, JavaScript and Python "by the end of September 2026" |
| CI2026-094-034 | confirmed | PR Newswire 2026-09-03 12:00 ET: 1 billion manifests, doubled "from 500 million in just six months", 3,000 images, 675,000 variants |
| CI2026-094-035 | confirmed | apko 57 in-window releases (v1.2.3–v1.4.11) and melange 41 (v0.49.0–v0.62.1). v1.3.0 on Sep 9, v1.4.0 on Sep 14 |
| CI2026-094-036 | confirmed | "beginning with 50" ("All 50 are silent fixes") and "We joined Anthropic's Project Glasswing", both as vendor statements |
| CI2026-094-038 | confirmed | NIST #5523: Chainguard, Inc., Active, Overall Level 1, initial validation 9/15/2026 (atsec), sunset 9/14/2031, ML-KEM listed. Blog: v3.6, opt-in from October 1, 2026 |
| CI2026-094-039 | confirmed | 14 disclosures (1 critical, 1 high, 8 medium, 4 low), five through Akrites. athena repo created 2026-09-25T12:21Z with no licence and 14 `CGP-` advisory entries |
| CI2026-094-040 | confirmed | Changelog: "Chainguard Libraries for Go and .NET (invite-only beta) Launched September 28, 2026" |

Totals: 24 rows checked, 24 confirmed, 0 corrected, 0 wrong, 0 unverifiable. The search log's "figures confirmed against raw text" statement held for every figure re-checked here. That is a sample, not an exhaustive re-verification.

*This is an AI-assisted spot-check, not qualified human review.*
