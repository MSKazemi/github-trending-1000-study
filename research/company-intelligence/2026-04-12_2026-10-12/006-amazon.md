# Amazon / AWS — provisional six-month technology intelligence screen (006)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](006-amazon.events.csv), [search log](006-amazon.search-log.md) and [source-QC note](006-amazon.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads** under the maintainer's 2026-10-15 integration decision (precedent: PRs #67/#81/#86/#87/#93/#301). They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. Merging is not scientific or security sign-off; issue [#72](https://github.com/MSKazemi/github-trending-1000-study/issues/72) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 006; [issue #72](https://github.com/MSKazemi/github-trending-1000-study/issues/72). Scope: Amazon / AWS coding-agent products — **Kiro** (IDE, CLI, Web, Crew), **Amazon Q Developer**, **Amazon Bedrock AgentCore** and related AWS developer-security services.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened on 2026-10-16** (earlier passes 2026-10-12…15). Per-query UTC times, search-hit totals, page snapshots and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen — 30 source leads covering all seven calendar segments**; not reviewed by a qualified human. Not independently verified task outcomes, exhaustive retrieval or scientific completion. [Study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md); [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).
- **Official channels checked:** [AWS DevOps blog](https://aws.amazon.com/blogs/devops/), AWS Security blog, [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/), [AWS security bulletins](https://aws.amazon.com/security/security-bulletins/), [Kiro blog](https://kiro.dev/blog/), [Kiro changelog](https://kiro.dev/changelog/), [AgentCore release notes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html), and GitHub repositories via read-only `gh api`. **Claim grading** is company-watch E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [2026-10-16 search log](006-amazon.search-log.md) records the five web searches and ~30 page reads actually run, with include/exclude decisions per segment; the [2026-10-14 query log](source-audits/006-amazon.2026-10-14-qa.md) is preserved unchanged. The ledger grew from **9 to 30 rows**: Apr 12–30 **4**, May **3**, June **8**, July **3**, August **6**, September **3**, Oct 1–12 **3**. The earlier statement that September and October 1–12 had no documented event was already superseded on 2026-10-15 and is now further corrected.

Coverage is **purposive**: Kiro blog/changelog page 1, AWS What's New items found by search, and AWS security bulletins found by search. Third-party model-availability posts in Kiro (many per month) were excluded by rule. Amazon Q Developer feature changes beyond the sunset notice were **not searched** (query logged as not executed), so Q-side activity is **unknown**, not zero. Search-hit and exclusion denominators are unknown.

## 2. Corporate/product identity and rights baseline

Amazon.com, Inc. operates Amazon Web Services (AWS). Kiro, Amazon Q Developer and Amazon Bedrock AgentCore are **distinct products** with separate support, data and billing boundaries; Kiro is billed through its own plans (Pro, Pro+, Pro Max, Power) and AWS identity integration (IAM Identity Center, Service Quotas). Corporate ownership was not re-checked at filing level (SEC EDGAR skipped because it demands a personal identifier).

**Open-source and licence status (GitHub API, read 2026-10-16):**

| Repository | Licence (GitHub-detected) | What it is | Note |
|---|---|---|---|
| [kirodotdev/Kiro](https://github.com/kirodotdev/Kiro) | none detected | Public issue/feedback tracker | README: "The Kiro product source code is not hosted here." Kiro IDE/CLI are closed source |
| [aws/amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli) | Apache-2.0 | Former open-source Q Developer CLI | README: "no longer being actively maintained and will only receive critical security fixes"; now "available as Kiro CLI, a closed-source product". Last release v1.19.7 on 2025-11-17 (pre-window) |
| [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | Apache-2.0 | Open-source agent workspace (created 2026-07-16; v0.1.0 2026-07-22; v0.8.0 2026-10-09) | Runs on the closed-source Kiro CLI |
| [aws/bedrock-agentcore-sdk-python](https://github.com/aws/bedrock-agentcore-sdk-python) | Apache-2.0 | AgentCore Python SDK | 26 releases dated in window (v1.6.2 Apr 13 … v1.24.1 Oct 7); SDK licence does not cover the hosted AgentCore service |
| strands-agents/sdk-python → `strands-agents/harness-sdk` (API redirect) | Apache-2.0 | Strands agent SDK, the AgentCore harness export target | Renaming not investigated |

**Rights consequence:** the one AWS coding-agent CLI that was open source (Q Developer CLI) has been replaced by a closed-source successor. Reusable open code in this ecosystem is the SDK/workspace layer (AgentCore SDK, Strands, Kiro Crew), not the agent clients.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | Apr 13 [Kiro CLI headless mode](https://kiro.dev/blog/introducing-headless-mode/) (API key, `--no-interactive`); Apr 22 [AgentCore managed harness preview, CLI and skills](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/); Apr 29 [The Register interview](https://www.theregister.com/software/2026/04/29/amazon-tells-its-engineers-to-review-all-ai-output/5224124); Apr 30 [Q Developer IDE end-of-support notice](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) | Harness is **preview** in 4 Regions. Q sunset is **2027-04-30** for IDE plugins and paid subscriptions only; new sign-ups stop 2026-05-15 |
| May | May 12 [Specs faster/smarter](https://kiro.dev/blog/faster-smarter-specs/) (parallel independent tasks, quick plan, requirements analysis); May 18 [Kiro Web preview](https://kiro.dev/blog/introducing-kiro-web/); May 22 [2026-035-AWS / CVE-2026-9255](https://aws.amazon.com/security/security-bulletins/2026-035-aws/) Kiro CLI tool approval bypass via piped stdin | Kiro Web **preview** for paid plans; CVE fixed in kiro-cli 1.28.0 |
| June | Jun 2 [CVE-2026-10591](https://aws.amazon.com/security/security-bulletins/2026-037-aws/) file-write to execution-sensitive paths; Jun 11 [Kiro Web specs + GitLab](https://kiro.dev/blog/kiro-web-specs-gitlab/); Jun 11 [Pro Max $100/mo](https://kiro.dev/blog/kiro-pro-max/); Jun 15 [CVE-2026-11931](https://aws.amazon.com/security/security-bulletins/2026-045-aws/) world-readable token cache; Jun 17 [AgentCore harness GA](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/); Jun 18 [scheduled automations](https://kiro.dev/blog/introducing-automations/); Jun 19 [Kiro power for AWS DevOps Agent](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/); Jun 25 [Agent Focus (experimental)](https://kiro.dev/blog/introducing-agent-focus/) | Harness **GA** (Jun 17 on What's New; Jun 18 suggested for a blog not opened). Automations live inside a still-**preview** Kiro Web. Two security fixes in the IDE |
| July | Jul 2 [overage caps / prepaid credits](https://kiro.dev/blog/cap-prepay-overage/); Jul 14 [One year of Kiro](https://kiro.dev/blog/one-year/) (direction and adoption claims); Jul 30 [control framework for AI coding agents](https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/) | Adoption numbers are vendor claims. Framework is guidance. A third-party July report on a Kiro prompt-injection flaw returned HTTP 403 and is not cited |
| August | Aug 4 [Kiro Crew open source](https://kiro.dev/blog/introducing-kiro-crew/); Aug 4 [CVE-2026-18656/18657](https://aws.amazon.com/security/security-bulletins/2026-074-aws/) Windows search path; Aug 5 [AWS Continuum for code vulnerabilities](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/); Aug 6 [AgentCore runtime instances GA](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/); Aug 18 [cloud sessions preview](https://kiro.dev/blog/cloud-sessions/); Aug 26 [diagnostics-over-time analysis](https://kiro.dev/blog/diagnostics-over-time/) | Continuum is **preview**; its Claude Code/Codex/Kiro integrations were **"coming soon"** (QC correction). Cloud sessions us-east-1 only. Crew repo existed and released v0.1.0 before the blog |
| September | Sep 8 [ISO/IEC 27001 scope](https://kiro.dev/blog/iso-27001/); Sep 18 [1,000 PRs in a week](https://kiro.dev/blog/software-factory-1000-prs/); Sep 30 [Kiro Web Workflows opt-in](https://kiro.dev/changelog/web/introducing-workflows/) | ISO is inclusion in AWS's certificate scope, not a Kiro certificate. PR count without defect/revert data |
| Oct 1–12 | Oct 9 [Kiro CLI V3 rollout](https://kiro.dev/blog/cli-3/); Oct 12 [CLI 2.30.0 changelog](https://kiro.dev/changelog/cli/); Oct 12 [FedRAMP Class C scope](https://kiro.dev/changelog/general/kiro-is-now-in-scope-for-fedramp-class-c/) | V3 general default planned for **end of October** (after cutoff). Oct 13 sign-in controls and Oct 14 local sandboxing **excluded** |

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited documents support | Non-equivalence or counterexample |
|---|---|---|
| Q Developer → Kiro migration (-001; Q CLI README) | Future IDE-plugin sunset; Kiro positioned as successor; Q CLI now closed-source Kiro CLI | Not a 2026 shutdown of Q; Console, docs sites, mobile and Chat Apps not impacted. Migration also moves users from an Apache-2.0 client to a closed one |
| Spec-driven, multi-surface agent (-002, CI-006-02, -011, -015, -016, -005, -022, -003) | Specs, parallel tasks, Web, automations, workflows, cloud sessions and CLI V3, all vendor-described | Most surfaces are **preview, experimental or opt-in**; no accepted-task, review-load or cost data |
| AgentCore harness preview → GA (-007, -014), runtime instances (-021) | Configuration-defined agents, export to Strands code, EC2-hosted runtimes | Export portability untested; Claude Agent SDK export announced only; compute billed separately |
| Kiro security bulletins (-009, -010, -013, -020) | Four vendor CVE disclosures in the window: tool-approval bypass, file-write to auto-exec paths, world-readable token cache, Windows search path | Disclosures, not exploitation evidence. They show that agent tool permissions and workspace trust are real attack surfaces. Other bulletins in the window were not enumerated |
| Governance guidance and security products (CI-006-04, CI-006-05, -024, -026) | Control framework (deterministic/non-deterministic/human controls); Continuum preview; compliance-scope inclusions | Guidance and compliance scope are not measured risk reduction |
| Vendor self-measurement (-018, -023, -025, -019) | Adoption counts, internal diagnostics error rates, 1,000 merged PRs, 39,000 internal Crew users | Unaudited; internal Amazon users; diagnostics authors state "a clean diagnostic check does not mean correct code"; no defect/revert counts |
| Independent reporting (-008) | Named Amazon Stores director: all AI output human-reviewed; spec-driven work "reduces" hallucination "at best" | One interview, internal retail teams, no denominator |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Stated intention | Classification on 2026-10-12 |
|---|---|---|
| [Apr 30 Q Developer notice](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) | Move IDE users to Kiro by 2027-04-30 | **Announced** future sunset; sign-up stop 2026-05-15 |
| [Apr 22 AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/04/agentcore-new-features-to-build-agents-faster/) / [Jun 17 GA](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/) | Terraform support; skills for Claude Code/Codex/Cursor; Claude Agent SDK export | Harness **GA**; the named extensions **announced only** (delivery not checked) |
| [Jul 14 One year of Kiro](https://kiro.dev/blog/one-year/) | "the roadmap ahead is the most ambitious we've ever had"; partner/community-driven evolution | **Aspiration**, no dated commitments |
| [Aug 5 Continuum](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/) | Integrations with Claude Code, Codex and Kiro | **Announced only** ("coming soon"); Continuum itself preview |
| [Sep 18 1,000 PRs](https://kiro.dev/blog/software-factory-1000-prs/) | Crews that propose their own work once governance and cost controls are "fully tested" | **Aspiration**; authors: "A capability an enterprise cannot control, audit, or afford is a demo, not a product" |
| [Oct 9 CLI V3](https://kiro.dev/blog/cli-3/) | V3 default with CLI 3.0 "at end of October" | **Planned**, after the cutoff |

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company forecasts)

| Testable scenario | Rival explanation | Disconfirming observation |
|---|---|---|
| Spec-first agent workflows lower review effort per accepted change | Gains come from task selection or more reviewers, not specs | Same frozen tasks show equal accepted-change rate and review minutes with a plain test-first prompt |
| Closed agent clients plus open SDK/export layers (Strands, Crew) keep agent logic portable | Export paths lag the hosted features and lock-in grows through billing and identity | An exported harness fails the same acceptance suite outside AWS, or needs major rework |
| Agent tool-permission CVEs keep appearing as agent surfaces multiply | Early-product defect density that falls as the products mature | Bulletin count for Kiro falls across 2027 while surfaces grow |

## 7. M1–M7 study relevance

| Construct | Prospective measurement (not an inferred conclusion) |
|---|---|
| **M1** agent workflow change | Opt-in, version-pinned records of spec/automation/cloud-session use; availability is not adoption |
| **M2** accepted quality and review load | Frozen external acceptance suites; count all attempts, review minutes and reverts (the 1,000-PR post gives none) |
| **M3** discoverability | Not addressed by these sources |
| **M4** verified third-party reuse | Audited outside use of Kiro Crew or the AgentCore SDK; stars, "tried" counts and internal users are not reuse |
| **M5** reuse vs rebuilding, rights and security | Licence/closed-source status per client; CVE fixed-version checks; harness export vs hand-written Strands code |
| **M6** lifecycle cost | Credits, overage caps, EC2 runtime and human minutes per accepted task; no token-to-CO2e conversion |
| **M7** maintainer intervention | Below: one controlled spec-first task trial |

## 8. One falsifiable reuse-first maintainer experiment

**Target:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline only (live Trending `capture` stays disabled under the source-access decision).

**Practice to test:** for a small change to the *existing* offline parser/CLI, write a short frozen spec card (requirements, design, task list, acceptance tests) before any agent edits, versus the current prompt-plus-docs workflow. Reuse the existing CLI and fixtures; build nothing new.

**Arms:** A = current docs plus a plain task prompt; B = the same task with the spec card. Same repository SHA, pinned agent/model version, synthetic fixtures, time cap and evaluator. Any coding agent may be used; Kiro is not required.

**Acceptance test (frozen first, by a second person):** existing unit suite passes, plus 6 hidden synthetic parser cases (3 valid, 3 malformed that must be rejected). Agent-authored tests do not count.

**Verified external-use signal:** none expected from this trial; record it as **not measured**, not zero.

**Outcomes:** accepted changes / all assigned tasks (including refusals and time-outs), reviewer minutes, reverts within 30 days, agent credits or tokens where billed.

**Cost cap and stop rule:** 6 tasks per arm and 4 reviewer-hours in total. Stop and keep arm A if B does not raise the accepted-change share by at least 1 task out of 6 **or** raises reviewer minutes by more than 25 %. Stop immediately on any agent write outside the repo or any use of an unapproved network source. **Not run; no effect estimated.**

## 9. Evidence quality, alternative outcomes and release checklist (2026-10-16)

- **Inventory:** 30 CSV rows across all seven segments: 22 first-party announcements or documents, 4 official security bulletins (E2), 1 independent news interview, 3 vendor analysis, case-report or strategy posts. This is a **purposive screen**, not a census.
- **QC of the 9 earlier rows:** all reachable, all dates match; two claims partly supported and two clarified (`limitation` appended, no status change). See [source QC](006-amazon.source-qc-2026-10-16.md).
- **Contrary or adverse evidence:** four in-window Kiro CVEs; the Register interview on mandatory human review; vendor authors' own caveats on diagnostics and the 1,000-PR pipeline.
- **Unknowns:** Q Developer in-window changes; bulletins not found by search; Kiro blog/changelog pages beyond page 1; actual first availability per account or Region; the Jun 17 vs Jun 18 harness GA date across AWS pages; independent replication of any vendor number.
- **Pending:** qualified human factual/link review, source-access/rights review and methods review; any task trial.
- **Cross-link:** distinct verified articles may enter the [#56 news corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) after their own verification; no `NEWS-` ID minted here.

## Earlier screen (preserved)

The first screen came from original PR #192 and draft [PR #229](https://github.com/MSKazemi/github-trending-1000-study/pull/229), integrated into `main` as commit `2cc5411` ("research(006): provisional initial Amazon / AWS evidence screen (#229)") on 2026-10-15. Its full texts remain in git history, in [the archived first-screen Markdown](source-archives/006-amazon.2026-10-13-first-screen.md), [the archived 22-column ledger](source-archives/006-amazon.2026-10-12-source-ledger.csv) and [the 2026-10-14 QA log](source-audits/006-amazon.2026-10-14-qa.md). It claimed:

- **5 then 9 dated publisher leads**, all E0/E1: the Apr 30 Q Developer notice (`CI-006-01` → `CI2026-006-001`), [Specs faster/smarter](https://kiro.dev/blog/faster-smarter-specs/), [Kiro Web](https://kiro.dev/blog/introducing-kiro-web/), [Kiro power for AWS DevOps Agent](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/), [control framework](https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/), [AWS Continuum](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/), [Kiro Web Workflows](https://kiro.dev/changelog/web/introducing-workflows/), [Kiro CLI V3](https://kiro.dev/blog/cli-3/) and the [CLI 2.30.0 changelog](https://kiro.dev/changelog/cli/).
- Direction: "AWS publicly shifts coding workflow focus from Q Developer IDE plugins toward Kiro's specification-led agent environment while extending hosted/cloud agent operations." The 2026-10-16 evidence supports this as a vendor-stated direction and adds the closed-source move of the Q CLI.
- Key caveat, still valid: "do not misreport this as a 2026 product shutdown" (AWS user guide on [Q Developer IDE end of support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html), linked by the 2026-10-14 audit and not re-opened on 2026-10-16).
- Its September and October 1–12 "no event documented" entries were superseded on 2026-10-15 and again here. Its description of Continuum as a "partner-integrated code-security workflow" is narrowed by the 2026-10-16 QC: the partner integrations were "coming soon".
- Its earlier maintainer experiment (frozen spec card vs baseline on the existing offline parser) is kept and tightened in §8.
