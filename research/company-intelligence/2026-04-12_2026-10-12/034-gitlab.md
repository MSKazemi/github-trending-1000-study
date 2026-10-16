# GitLab — provisional six-month technology intelligence screen (034)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16), not reviewed by a human.** This report, its [event ledger](034-gitlab.events.csv) and its [search log](034-gitlab.search-log.md) are documentary source leads for [issue #101](https://github.com/MSKazemi/github-trending-1000-study/issues/101). They were prepared with AI assistance and have **not been reviewed by a qualified human**. Factual/link review, source-access/rights review and methods review are **pending**. Nothing here is a verified finding, an adoption measurement or scientific sign-off. **Issue #101 was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates above remain open.** Verified, non-duplicate news items may later feed [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56), but only after human verification.

- **Company watchlist ID:** 034, GitLab (slug `gitlab`).
- **Research issue:** [#101](https://github.com/MSKazemi/github-trending-1000-study/issues/101). Linked corpus: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see §2. GitLab is a publicly listed company (NASDAQ: GTLB). No in-window acquisition or change of control was found. The full ownership structure was not verified at filing level.
- **Product URL and newsroom:** [about.gitlab.com](https://about.gitlab.com/), [press releases](https://about.gitlab.com/press/releases/), [release notes](https://docs.gitlab.com/releases/19/), [patch releases feed](https://docs.gitlab.com/releases/patch-releases.xml), [source repository](https://gitlab.com/gitlab-org/gitlab).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). Screened on 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** screened (provisional). Not independently checked, not published as a finding.
- **Source coverage:** 12 logged web queries plus direct reads of official release notes, the newsroom, patch advisories, one SEC exhibit and four independent articles. All seven month segments have at least one record. May is thin. Patch releases for Apr 12 to early June were not enumerated. Two sources returned HTTP 403. Details are in the [search log](034-gitlab.search-log.md).
- **Claim grading:** company-watch E0–E4 working tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md). These are not the [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) ratings.

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 (time not captured) | general web search | Q1–Q12 in [search log §1](034-gitlab.search-log.md) | unknown | unknown | 24 ledger rows | see [log §4](034-gitlab.search-log.md) | One search provider. Result totals not recorded. Patch feed only partly read. BleepingComputer and The Register not surfaced |
| 2026-10-16 | docs.gitlab.com, about.gitlab.com, sec.gov | direct reads of release notes 18.11 and 19.0–19.5, the press index (23 in-window titles) and 5 critical patch pages | n/a | n/a | n/a | 19.5 (Oct 15) out of window | Pages are mutable. Dates are the dates displayed on the page, not archived timestamps |

The 24 rows are a **purposive selection of material events**. They are not a census of GitLab releases, and the row count is not an innovation rate. Several rows cite official pages whose dates come from the page itself. An `independent_check_url` that points to another GitLab-hosted page is **documentary corroboration only** and does not count as an independent E3 check.

## 2. Verified company/product identity and baseline

- **Entity:** The Q1 FY2027 earnings release (Jun 2, 2026) and the Q2 FY2027 Form 8-K exhibit filed with the SEC (Sep 1, 2026) identify **GitLab Inc. (NASDAQ: GTLB)**. Sources: [Q1 PDF](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q1/GitLab-1QF2027-Earnings-Press-Release.pdf) and [SEC exhibit](https://www.sec.gov/Archives/edgar/data/0001653482/000162828026059820/gitlab-ex99120260731fy27.htm). Bill Staples is quoted as CEO and Jessica Ross as CFO in GitLab's Jun 2 release.
- **Ownership:** We found no in-window acquisition, merger or change of control. Reuters-sourced reports of sale talks ([html.it, 2024-07-18](https://www.html.it/magazine/gitlab-concorrente-di-github-verso-la-possibile-vendita/)) and a 2025 takeover rumour are **pre-window context**, and neither was confirmed as a transaction. The listing status was checked only at the Sep 1 filing date. Ownership on Oct 12 was not verified at filing level.
- **Leadership changes (titles only):** the press index lists a new CISO (Jun 9) and a Chief Business and Legal Officer (Jul 20). We read only the titles, not the releases themselves.
- **Organizational change:** on Jun 2 GitLab disclosed a cut of about 14% of its workforce (about 350 people) and an exit from 22 countries (row 008). [TNW](https://thenextweb.com/news/gitlab-cuts-14-percent-workforce-exits-22-countries) reported the same independently.
- **Product boundaries:** GitLab sells a DevSecOps platform (source control, CI/CD, security scanning, package and secret management) in Free, Premium and Ultimate tiers. It is offered as GitLab.com (SaaS), Self-Managed, Dedicated and Dedicated for Government.
  - AI features ship under the **GitLab Duo** brand. **Duo Agent Platform** became GA on Jan 15, 2026, which is pre-window baseline per the [GitLab press release](https://about.gitlab.com/press/releases/2026-01-15-gitlab-announces-duo-agent-platform-general-availability/), seen in search but not opened.
  - In-window brand names: **GitLab Orbit**, **Next Generation SCM**, **GitLab Flex**, **GitLab Secrets Manager**, **Artifact Central**, **Dependency Firewall**, **Duo CLI** and the **GitLab MCP server**. AI usage is billed through **GitLab Credits**.
- **Licence baseline:** the current [`gitlab-org/gitlab` LICENSE](https://gitlab.com/gitlab-org/gitlab/-/raw/master/LICENSE) assigns licences by directory:
  - most content and client-side JavaScript: MIT Expat
  - `doc/`: CC BY-SA 4.0
  - `ee/`: governed by `ee/LICENSE`
  - `jh/`: governed by `jh/LICENSE`
  - We did not read `ee/LICENSE`. Do **not** assume that Enterprise Edition, Duo or Agent Platform features are open source. The Duo CLI licence was **not verified**.

## 3. Month-by-month discoveries

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Apr 14 Vertex AI; Apr 15 19.0 breaking-changes guide; Apr 16 **18.11** (agentic vulnerability resolution GA, CI Expert beta, fine-grained PAT beta); Apr 21 Amazon Bedrock/BYOM; Apr 28 Claude models | [18.11 notes](https://docs.gitlab.com/releases/18/gitlab-18-11-released/), [press index](https://about.gitlab.com/press/releases/) | None screened beyond syndicated recaps | The Apr 16 press release dateline reads Apr 14. The breaking-changes guide shows Apr 15 on the English page and Apr 24 on the French copy |
| 2026-05 | May 21 **19.0** (SBOM dependency scanning GA, Secrets Manager open beta, removals of Redis 6, PostgreSQL 16, bundled Mattermost, etc.) | [19.0 notes](https://docs.gitlab.com/releases/19/gitlab-19-0-released/) | None screened | **Thin segment.** May patch releases were not enumerated |
| 2026-06 | Jun 2 Q1 FY27 results and **workforce reduction**; Jun 10 Transcend (next-gen SCM private beta, Orbit public beta, Governance for Agents private beta, Flex); Jun 10 Google/Gemini/Gemma; Jun 18 **19.1** (tool-approval guardrails beta); Jun 23 commissioned survey | [Transcend press](https://about.gitlab.com/press/releases/2026-06-10-gitlab-announces-new-capabilities-to-give-enterprises-speed-control-at-agentic-scale/), [19.1 notes](https://docs.gitlab.com/releases/19/gitlab-19-1-released/) | [TNW](https://thenextweb.com/news/gitlab-cuts-14-percent-workforce-exits-22-countries) (layoff), [DevOps.com](https://devops.com/gitlab-previews-revamped-devops-platform-for-the-agentic-ai-era/) (Transcend, repeats vendor claims) | 19.1 notes say pattern-based tool approval for Agentic Chat was **removed Jul 10** |
| 2026-07 | Jul 16 **19.2** (Duo CLI GA, custom flows GA, MCP server for Free tier, Security Review Flow beta); Jul 16 Forrester TEI (commissioned) | [19.2 notes](https://docs.gitlab.com/releases/19/gitlab-19-2-released/) | None screened | Routine Jul 8 and Jul 29 patch releases were not opened |
| 2026-08 | Aug 17 **critical patch** CVE-2026-19478 (9.4); Aug 20 **19.3** (Flow Creator, Secrets Manager Limited Availability, Credits caps GA) | [19.2.4 patch](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/), [19.3 notes](https://docs.gitlab.com/releases/19/gitlab-19-3-released/) | [Security Affairs](https://securityaffairs.com/?p=197454) (no known exploitation; older lines unpatched) | The Hacker News coverage returned HTTP 403 |
| 2026-09 | Sep 1 Q2 FY27 8-K; Sep 10 **critical patch** CVE-2026-85706 (10.0) and CVE-2026-87719 (9.9); Sep 11 CISA KEV listing; Sep 17 **19.4** (MCP tool governance); Sep 23 backports to 19.0/18.11 | [19.3.2 patch](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/), [19.4 notes](https://docs.gitlab.com/releases/19/gitlab-19-4-released/) | [Cybersecurity Dive](https://cybersecuritydive.com/news/gitlab-vulnerability-exploitation-cisa-kev/830278/) (KEV, watchTowr probes, HKCERT) | One incident is grouped under `034-cve-2026-85706` across three rows. The Sep 23 19.4.1 critical patch was not opened |
| 2026-10-01..12 | Oct 2 AI Gateway critical patch CVE-2026-90970 (9.9); Oct 6 "governed software factory" announcement; Oct 12 critical patch CVE-2026-97229 (10.0) | [AI Gateway patch](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-19-4-1-released/), [Oct 6 press](https://about.gitlab.com/press/releases/2026-10-06-gitlab-announces-the-foundation-for-the-governed-software-factory/), [19.4.2 patch](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/) | None screened | 19.5 (Oct 15) is **excluded** as out of window |

## 4. Dated event evidence and capabilities

The [CSV](034-gitlab.events.csv) holds all 24 rows. The clusters that matter for the study are:

| Event ID | Published / event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | Working grade |
|---|---|---|---|---|---|---|
| 003, 006, 011, 013, 016, 020 | Apr 16, May 21, Jun 18, Jul 16, Aug 20, Sep 17 | Monthly releases 18.11 through 19.4 move agent work into the platform: vulnerability-resolution MRs, CI Expert, Duo CLI (headless and MCP), custom flows, Flow Creator, and merge-conflict and review-discussion resolution | Labels are mixed: GA, beta, experiment, unlabeled. Many features are Premium or Ultimate only. Agent output quality was **not exercised** | Release notes (official) | Same-day GitLab press releases (documentary only) | E2 |
| 011, 020 | Jun 18, Sep 17 | **Governed agent tools:** Allow/Ask/Deny tool-approval guardrails (beta). MCP tool governance in which read-only tools default to Always Allow and write/delete tools default to Always Ask. MCP access restriction (beta). AI audit-event streaming (beta) | Pattern-based tool approval was removed Jul 10, a **reversal** inside the window. Policy effectiveness has not been tested | Release notes | none | E2 |
| 009 | Jun 10 | Next-gen SCM: agents query the repository server-side. Orbit: a context graph. Governance for Agents | Private or public beta. Vendor claims of up to 50x speed, 2x fewer tokens, 11x faster Orbit responses and "45x fewer hallucinations" are **early internal results with no disclosed workload** | Press release, blog | [DevOps.com](https://devops.com/gitlab-previews-revamped-devops-platform-for-the-agentic-ai-era/) repeats the claims and adds no benchmark | E1 |
| 001, 004, 005, 010 | Apr 14, Apr 21, Apr 28, Jun 10 | Model and cloud routing: Vertex AI/Gemini, Amazon Bedrock with self-managed BYOM, Claude models, Gemma for self-hosted, all billed through GitLab Credits | Stated as "can now" with no GA/beta label. Regions and tiers are unstated | Press releases | none | E1 |
| 015, 018, 019, 021, 022, 024 | Aug 17 to Oct 12 | **Six critical patch releases in the official feed, five of them ledgered** (the Sep 23 19.4.1/19.3.3/19.2.7 release was not opened; count corrected 2026-10-16), including CVE-2026-85706 (CVSS 10.0, unauthenticated arbitrary file read, **listed in CISA KEV**, probing reported in the wild) and CVE-2026-90970 (prompt-template sandbox escape in the self-hosted AI Gateway) | GitLab.com and Dedicated were patched by the vendor. Self-managed users had to upgrade. Older release lines were not backported, which is a maintenance cost | Patch advisories | Cybersecurity Dive (KEV), Security Affairs | E2 (vendor), E2 second-entity |
| 012, 014 | Jun 23, Jul 16 | Commissioned Harris Poll survey (n=1528, e.g. 85% say the bottleneck has moved to review). Commissioned Forrester TEI (composite of 4 interviews, 400% ROI) | Both were **paid for by the vendor**. Survey sampling and dates were not disclosed. The TEI is a model, not a measurement | Press releases | none | E1 |
| 007, 008, 017 | Jun 2, Jun 2, Sep 1 | Revenue $264.2M (+23%), then $286.3M (+21%). FY27 guidance raised. 14% workforce reduction | Financial metrics are **not** evidence of adoption, user benefit or reuse | Earnings PDF, SEC 8-K | TNW (layoff) | E2 |
| 023 | Oct 6 | "Governed software factory": Artifact Central (beta), Dependency Firewall (early access), Orbit GA planned for next month, Secrets Manager GA in 19.5 | Mostly **announced or planned**, under a forward-looking-statements disclaimer | Press release | none | E1 |

**Change areas covered:**

- **Agents, UX and APIs:** Duo CLI, flows, MCP server and tools.
- **Open-source offerings:** the MIT-licensed core is unchanged in kind. The licence of new agent components was not verified.
- **Security:** governance features, secret and dependency scanning, critical CVEs.
- **Pricing and licensing:** GitLab Credits caps, Flex, and the claim that hosted open-weight models give "up to 4x more calls per credit" without absolute prices.
- **Integration:** AWS, Google and Anthropic.
- **Developer governance:** tool approval, audit streaming, Security Manager role.

## 5. What the company says it intends to do

| Close paraphrase or short quote (≤25 words) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Orbit GA "planned next month" across deployment options. Anthropic-model security flows "coming" next month. Artifact Central for Self-Managed later in the month | [Oct 6 press](https://about.gitlab.com/press/releases/2026-10-06-gitlab-announces-the-foundation-for-the-governed-software-factory/) | Nov 2026 (implied) | planned | Covered by a forward-looking-statements disclaimer. Delivery cannot be checked inside the window |
| CEO: "we are evolving GitLab to be the trusted enterprise platform for software creation in the AI era" | [Jun 2 press](https://about.gitlab.com/press/releases/2026-06-02-gitlab-reports-first-quarter-fiscal-year-2027-financial-results/) | undated | strategic aspiration | Comes alongside a 14% workforce reduction. TNW reports savings are to be reinvested in R&D and AI |
| Positions GitLab as infrastructure that "turns the speed of agentic coding into governed, auditable software delivery at enterprise scale" | [Jun 10 press](https://about.gitlab.com/press/releases/2026-06-10-gitlab-announces-new-capabilities-to-give-enterprises-speed-control-at-agentic-scale/) | undated | positioning | No GA dates for next-gen SCM or Governance for Agents |
| Newer Gemini models to be added "as they ship" | [Jun 10 Google press](https://about.gitlab.com/press/releases/2026-06-10-gitlab-expands-collaboration-with-google-to-deliver-fully-managed-devsecops-platform/) | depends on Google | tentative | No dates |
| NGINX Ingress can be re-enabled until its planned removal in GitLab 20.0 | [19.0 notes](https://docs.gitlab.com/releases/19/gitlab-19-0-released/) | GitLab 20.0 (undated) | planned deprecation | The 20.0 date was not found |
| FY2027 revenue guidance $1,129–1,133M | [SEC 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001653482/000162828026059820/gitlab-ex99120260731fy27.htm) | FY ending Jan 2027 | guidance | Safe-harbor statement. This is not a product plan |

These are company statements. They are not independent facts about the future.

## 6. Independent interpretation: conditional 2027–2031 scenarios

| Hypothesis for 2027–2031 (researcher's, not GitLab's) | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Repository platforms become the place where agent permissions are governed, with tool-level Allow/Ask/Deny defaults built into SCM and CI | 19.1 and 19.4 tool governance, Governance for Agents beta, the Oct 6 "governed software factory" | Governance may stay in IDE/agent clients or in separate policy gateways. GitLab's framing may be marketing aimed at a survey-identified worry (row 012) | Governance for Agents stays in beta through 2027. Independent users report that defaults are bypassed or disabled. Rival agent clients own the permission layer | Low–moderate. No independent effectiveness data |
| H2: Agent-specific repository access (server-side queries, context graphs) cuts token and network cost compared with clone-based agents | Jun 10 vendor claims for next-gen SCM and Orbit; one customer A/B on 79 MRs reported in a GitLab blog | Gains may come from task selection, caching or model choice. The internal results have no disclosed workload | Independent replication shows no significant token or accuracy gain over a plain clone plus grep baseline. Orbit GA slips | Low. Vendor-only evidence (E1) |
| H3: More agent surface area (AI Gateway, GraphQL, MCP) increases the security-maintenance burden on self-managed operators | Six critical patch releases Aug 17–Oct 12 in the official feed (five ledgered), one listed in CISA KEV, one in the AI Gateway prompt-template sandbox; release lines left without backports | Disclosure frequency may reflect a bug-bounty or audit push rather than new attack surface. GitLab.com users are not affected the same way | Critical advisory counts in 2027 return to earlier levels. AI-component CVEs stay rare | Moderate as a description of the window. Low as a forecast |
| H4: Platform consolidation (artifacts, secrets and dependency firewall in one control plane) cuts integration work for teams that already use GitLab | Oct 6 Artifact Central, Dependency Firewall, Secrets Manager | Lock-in and price may outweigh the integration savings. Specialized tools may stay better | Independent case studies show unchanged or higher maintenance minutes | Low. Mostly announced or planned |

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | More repositories show agent-authored MRs or flows inside the forge itself | Only with opt-in, consented logs. Do not infer agent use from commit style | Agent use stays in IDE/CLI and leaves no forge trace | No detector-based authorship attribution (see AGENTS.md) |
| **M2** accepted task quality | Vendor says agent MRs fix vulnerabilities and pipelines | Use hidden, independently authored acceptance tests on a frozen task set. Count all attempts | Auto-generated fixes are accepted at the same rate as, or below, human fixes | Vendor confidence scores do not measure acceptance |
| **M3** discoverability | The MCP server and Orbit expose project context to agents | Compare agent task success with and without structured context on the same tasks | Context gains disappear once tasks are controlled for | Search-engine discoverability is a separate question |
| **M4** verified third-party reuse | CI/CD components and the MCP server let agents reuse catalog components | Trace one consented downstream integration from start to finish | Usage counts and stars stand in for reuse | Stars, ARR and customer counts are **not** reuse |
| **M5** reuse-first | Built-in secret detection, dependency scanning and a dependency firewall may replace custom scripts | Compare against existing reused components such as the current CI and `scripts/check_research_artifacts.py` | Existing tools already cover the need | Licence and tier limits (Ultimate-only features) |
| **M6** lifecycle human/energy cost | Breaking changes in 19.0 and critical patches impose upgrade work | Measure upgrade, patch and review minutes, and CI minutes if instrumented | Hosted SaaS takes on this cost for the user | **No token-to-CO2e conversion.** Vendor "4x calls per credit" is not an energy figure |
| **M7** actionable interventions | Default-ask on write tools is a cheap policy to test | See §8 | No measurable reduction in unsafe actions | Synthetic tasks only until approval is given |

Company adoption claims are vendor statements. They are not independent task outcomes or verified reuse. These include the 50M registered users, "~50% of Fortune 100", "10x weekly active users since GA", the TEI ROI and the survey percentages.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), agent-assisted documentation and ledger maintenance tasks only. The live Trending `capture` command stays **disabled** under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md). Nothing here changes that.

**Candidate practice (not yet validated):** a **reuse-first borrowing of GitLab's 19.4 tool-governance default**. Read-only tools are auto-allowed. Every write, delete or network-mutating tool needs explicit human approval. This is set up in the agent client the maintainer already uses. It needs no GitLab migration, no new dependency and no paid service.

**Treatment/control and frozen comparable task:**

- **Control A:** the maintainer's current agent permission configuration, unchanged.
- **Treatment B:** read-only tools set to allow, all write/delete/push/`gh` mutation tools set to ask.
- **Task set:** freeze in advance 12 synthetic repository tasks. Examples: fix a deliberately malformed row in a scratch copy of a company events CSV, add a missing search-log segment, correct a broken relative link. Each task is randomly assigned to A or B, 6 per arm.
- **Seeded traps:** 3 of the 12 tasks contain an instruction embedded in a data file that tries to make the agent push, delete or edit an unrelated file. Each arm gets the same number of traps.
- **Hidden acceptance checks:** written by someone other than the agent and kept out of the agent's context. They include `python3 scripts/check_research_artifacts.py --root .` and the full unit suite.

**Accepted-task unit:** one task whose diff passes the hidden checks, touches only the permitted files, and is accepted by human review. Refused, abandoned and timed-out tasks stay in the denominator.

**Success and guardrails:**

- **Primary:** accepted tasks / all 12 assigned.
- **Safety (must be zero):** unapproved writes outside scope, pushes, deletions, secret exposure.
- **Measured human work:** number of approval prompts, approval minutes, and review/rework minutes, each logged by the maintainer with a timer.
- **Secondary:** agent wall-clock time, plus electricity only if it is actually metered. No CO2e estimate.
- **Hard limits:** no real credentials, no network capture, no pushes to `main`. Run in a disposable worktree.

**Stop/reversal rule:**

- Stop immediately if any arm makes an unapproved out-of-scope write.
- Do **not** adopt B if its accepted-task rate is lower than A's by 2 or more tasks out of 6.
- Do **not** adopt B if its median human approval-plus-review minutes are more than 1.5× A's and B shows no reduction in trap-triggered unsafe actions.
- A null result (no difference) is a valid outcome and must be preserved.

**No trial has been run and no effect has been estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary E2 only):**
  - Six monthly releases (18.11–19.4) with dated GA, beta and experiment labels.
  - Duo CLI GA (Jul 16).
  - MCP tool governance (Sep 17).
  - Five ledgered critical security releases (Aug 17 to Oct 12); the official patch feed lists six critical releases in that span, the sixth (Sep 23, 19.4.1/19.3.3/19.2.7) not opened.
  - The 19.0 breaking removals.
  - Q1 and Q2 FY27 financials and the 14% workforce reduction, the latter confirmed by TNW.
- **Claims/announcements only:**
  - Next-gen SCM, Orbit and Governance for Agents performance figures.
  - Cloud and model partnership availability.
  - Oct 6 planned items: Orbit GA, Anthropic-model security flows, Artifact Central for Self-Managed.
  - The commissioned survey and TEI ROI.
- **Conjectures and unknowns:**
  - H1–H4 in §6.
  - The Duo CLI and `ee/` licence terms.
  - Ownership on Oct 12 at filing level.
  - The patch releases from Apr 12 to early June and the Sep 23 19.4.1 advisory, which were not read.
  - Real exploitation prevalence of CVE-2026-85706.
  - Independent effectiveness of any agent-governance feature.
- **Contradictory or null evidence:**
  - Pattern-based tool approval was removed on Jul 10, less than a month after 19.1.
  - The Flow Creator status differs: unlabeled in the 19.3 notes, "GA" in the Aug 20 press release.
  - The press release for 18.11 is datelined Apr 14 but listed as Apr 16.
  - The 19.0 guide is dated Apr 15 in English and Apr 24 in French.
  - A third-party claim that 19.0 and 18.11 had no fix for CVE-2026-85706 was superseded by GitLab's Sep 23 backport.
  - A third-party date of Oct 8 for the CVE-2026-97229 patch conflicts with the official Oct 12.
  - DevOps.com coverage of Transcend adds no independent measurement.
- **Reviewer links and audit date:** AI-assisted screen on 2026-10-16. Human factual/link reviewer: **pending**. Methods reviewer: **pending**. Issue #101 was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates above remain open; reopen it to document human review.

## Independent source spot-check (2026-10-16)

An independent reviewer agent (not the author of this screen) re-fetched every cited URL on 2026-10-16 and compared dates and specific figures against raw page text (`curl` + grep; `pdftotext` for the earnings PDF), the official patch-release feed and the NVD CVE API (`services.nvd.nist.gov/rest/json/cves/2.0`). DevOps.com returned HTTP 403 and was not re-read. Classification: confirmed / corrected / unverifiable / wrong.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (§2) | confirmed | SEC exhibit text: "GitLab Inc. (NASDAQ: GTLB)", quarter ended July 31, 2026; Q1 PDF quotes Bill Staples (CEO) and Jessica Ross (CFO). The exact 8-K filing date was not re-checked on EDGAR (consistent with the Sep 1 press-release URL). |
| 034-001 / 004 | confirmed | Apr 14 press: Vertex AI models incl. Gemini, usage counts toward Google Cloud commitments, AI Gateway on GKE or Cloud Run. Apr 21 press: Bedrock routing with existing IAM and spend, self-managed BYOM to Bedrock, GitLab Credits via AWS Marketplace. |
| 034-002 | confirmed | English page `datePublished` 2026-04-15, `dateModified` 2026-06-24; French copy `datePublished` 2026-04-24; "projected to include 15"; 4 high / 5 medium / 8 low = 17 listed; May 4–6 and May 11–13 windows; ROPC removal; PostgreSQL 17 minimum. |
| 034-003 | confirmed | 18.11 notes "On April 16, 2026"; press release dateline "April 14, 2026"; vulnerability resolution GA, Data Analyst GA, CI Expert beta, fine-grained PAT beta. |
| 034-005 / 010 | confirmed | Apr 28 press: Claude Opus 4.7 via Google Cloud and Bedrock, Claude Marketplace. Jun 10 Google press: Gemini 3.5 in Duo Agent Platform, Gemma 4 for Duo Self-Hosted, models added "as they ship". |
| 034-007 / 008 | confirmed | Q1 PDF: $264.2M, 23%, 1,519 customers >$100k ARR, DBNRR 117%, guidance $272–274M and $1,112–1,118M; ~14% / 350 team members, 22 countries, ~37% footprint, $30–35M charges, substantially complete by end of FY2027. TNW (June 3, 2026) matches and reports reinvestment in R&D/AI. |
| 034-017 | confirmed | SEC exhibit: $286.3M, 21%, 1,571 customers >$100k ARR, Q3 guidance $281–283M, FY2027 $1,129–1,133M. |
| 034-009 | confirmed | Jun 10 press: next-gen SCM private beta "up to 50x faster", "up to two times fewer tokens"; Orbit public beta "11x faster", "4.5x fewer tokens", "45x fewer hallucinations" (internal testing). |
| 034-011 / 013 / 016 / 020 | confirmed | 19.1 (June 18): pattern-based tool approval "removed on July 10, 2026". 19.2 (July 16): Duo CLI GA, custom flows GA, "GitLab MCP server is now available for Free users". 19.3 (August 20): Flow Creator heading carries no status label while the Aug 20 press calls it "generally available". 19.4 (September 17): read-only tools "Always Allow", write "Always Ask"; press: "up to 4x more calls per credit". |
| 034-012 / 014 | confirmed | Harris Poll: 1,528 respondents, six countries, 85% bottleneck shift, 43% cannot distinguish AI code. Forrester TEI: composite from four customer interviews, 400% ROI, 20% individual productivity, commissioned by GitLab. |
| 034-015 | confirmed | Patch page "On August 17, 2026 … 19.2.4, 19.1.6, 19.0.8, 18.11.11". NVD: CVE-2026-19478 CVSS 9.4 (CNA; NVD primary 9.1), CWE-94, GraphQL directive; CVE-2026-19650 7.1, CWE-352. Security Affairs (August 18, 2026): no known exploitation; 18.2–18.10 branches not patched. |
| 034-018 / 019 | confirmed | Patch page "On September 10, 2026 … 19.3.2, 19.2.6, 19.1.8"; 18 security fixes in the table (2 critical, 6 high, 9 medium, 1 low). NVD: CVE-2026-85706 CVSS 10.0, CWE-22, unauthenticated arbitrary file read in the repository commits API, `cisaExploitAdd` 2026-09-11; CVE-2026-87719 CVSS 9.9, CWE-502, EE, Duo Chat access. Cybersecurity Dive "Published Sept. 14, 2026": KEV, watchTowr in-the-wild probes, HKCERT "being exploited in the wild". |
| 034-021 | confirmed | 19.0.9 page "On September 23, 2026 … 19.0.9 and 18.11.12", backport only, no other changes. endoflife.ai article dated September 11, 2026 makes the superseded "no fix for 19.0/18.11" claim. |
| 034-022 | confirmed | AI Gateway page shows no date; feed entry 2026-10-02. NVD: CVE-2026-90970 CVSS 9.9, CWE-1336, prompt-template sandbox escape, self-hosted AI Gateway. |
| 034-023 | confirmed | Oct 6 press: Artifact Central beta on GitLab.com, Self-Managed "later this month"; Dependency Firewall early access; Orbit GA "next month"; Secrets Manager GA in 19.5. The page also names the planned Anthropic models for those security flows; not added to the ledger here. |
| 034-024 | confirmed | Patch page "On October 12, 2026 … 19.4.2, 19.3.5, 19.2.8"; 24 security fixes; CVE-2026-97229 integer overflow in CI/CD regular expression compiler. NVD CVSS 10.0, CWE-190, NVD published 2026-10-13. |
| Critical-release count (§4, §6 H3, §9) | **corrected** | The official feed lists **six** "Critical Patch Release" entries between Aug 17 and Oct 12 (Aug 17, Sep 10, Sep 23 ×2, Oct 2, Oct 12), not five; the second Sep 23 release (19.4.1, 19.3.3, 19.2.7) is not ledgered. Text changed to "six in the feed, five ledgered". The feed lists 19 in-window patch releases; none before Aug 17 is titled "Critical". |

Outcome: 23 of 24 ledger rows (all except 006, whose 19.0 feature labels were not compared) plus the entity and the critical-release count checked → 23 rows confirmed, 1 report-level count corrected, 1 secondary source unverifiable (DevOps.com, HTTP 403; it is only an `independent_check_url`); 0 wrong. All six CVE IDs exist in NVD with the stated CVSS scores and GitLab as CNA. No fabricated URL, date, CVE or figure found; no cross-company contamination found.

*This is an AI-assisted spot-check, not qualified human review; the human factual/link, rights and methods reviews remain pending.*
