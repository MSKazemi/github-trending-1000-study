# Semgrep: provisional six-month technology intelligence screen (092)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](092-semgrep.events.csv) and its [search log](092-semgrep.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 092
- **Research issue:** [#160](https://github.com/MSKazemi/github-trending-1000-study/issues/160). Evidence corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` item was minted here; candidates are listed in §9.
- **Ownership and product boundaries (as of 2026-10-12):**
  - **Entity:** Semgrep, Inc. ("© 2026 Semgrep, Inc."; founded 2017 per its [about page](https://semgrep.dev/about)). It is privately held and venture-funded. The about page lists a $100M Series D led by Menlo Ventures, which is pre-window baseline.
  - **Ownership changes:** no parent company, acquisition of Semgrep, or in-window funding round was found.
  - **Earlier names:** a former company name was **not** verified from fetched sources.
  - **Corporate filings:** filing-level verification was not performed, and SEC EDGAR was deliberately not contacted.
- **Product URL and company newsroom:** there is no separate newsroom. Primary channels are:
  - [semgrep.dev](https://semgrep.dev/) and the [blog](https://semgrep.dev/blog)
  - [release notes](https://docs.semgrep.dev/release-notes) (monthly through June 2026, then weekly)
  - [semgrep/semgrep](https://github.com/semgrep/semgrep) (LGPL-2.1) and [PyPI `semgrep`](https://pypi.org/project/semgrep/)
  - the [status page](https://status.semgrep.dev/history)
  - the [licensing page](https://docs.semgrep.dev/licensing)
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). The ledger has 39 rows across all seven calendar segments.
- **Source coverage:**
  - **Official channels:** 85 blog pages fetched raw (67 dated in window); 16 in-window release-notes pages; 21 GitHub releases (v1.160.0–v1.180.0) checked against PyPI upload times.
  - **Other sources:** the GitHub org repository list; the status RSS feed (May 13 – Oct 15 only); the Opengrep fork's releases; the HN Algolia API (18 stories); four web searches.
  - **Not obtained:** no tier-1 independent news story about Semgrep was found in the window. Business Wire and VMBlog were inaccessible. Details are in the [search log](092-semgrep.search-log.md).

## 1. Search and inclusion audit

This is a summary only. Exact requests, opened URLs and exclusions are in the [search log](092-semgrep.search-log.md). Web-search totals were not shown, so they are recorded as unknown, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | semgrep.dev sitemap + raw HTML | all `/blog/2026/` posts, lastmod ≥ 2026-03-15 | 67 in window | 67 | 21 URLs used | opinion, events, third-party incident write-ups (log) | sitemap lastmod is not a publication date; byline date used |
| 2026-10-16 | docs.semgrep.dev release notes | Apr/May/Jun monthly + 13 weekly pages | 16 | 16 | 11 rows | minor UI fixes | weekly pages display no publication date |
| 2026-10-16 | GitHub API + PyPI JSON | semgrep/semgrep releases; org repos; opengrep releases; advisories | 21 + 20 releases | all | 5 rows | routine parser/language changes | no GHSA or in-window CVE found |
| 2026-10-16 | status.semgrep.dev RSS | incident history | 25 (May 13 – Oct 15) | 25 | 3 rows | others summarized in §3 | Apr 12 – May 12 not shown; the feed may be capped |
| 2026-10-16 | HN Algolia + 4 web searches | Semgrep, Opengrep, Replit, tier-1 outlets | 18 + unknown | ~45 | 3 rows | aggregators graded E0 and unused | Business Wire / VMBlog inaccessible |

## 2. Verified company/product identity and baseline

Semgrep sells a code-security platform. Its products are:

| Product | Licence | Notes |
|---|---|---|
| **Semgrep Community Edition (CE)** | LGPL 2.1 | open-source engine |
| **Semgrep Code** (SAST with the proprietary Pro Engine for cross-file analysis) | proprietary | — |
| **Supply Chain** (reachability, malicious-package detection, SBOM, licence policy) | proprietary | — |
| **Secrets** | proprietary | — |
| **Multimodal** (LLM-assisted detection, triage, Autofix and "Memories") | proprietary | — |
| **AppSec Platform** | proprietary | — |
| **Guardian** | proprietary | in-window product for AI coding agents |

Licences are per the [licensing page](https://docs.semgrep.dev/licensing) (dateModified 2026-06-02). That page states that all rules in `semgrep-rules`, Community and Pro alike, are under the **Semgrep Rules License v1.0**, which is "available only for internal business use". It says vendors "cannot use Semgrep-maintained rules in competing products or SaaS offerings".

**Licence history and the Opengrep fork (baseline, pre-window):**
- [Opengrep](https://github.com/opengrep/opengrep) is an LGPL-2.1 fork. Its GitHub repository was created 2024-12-14.
- Semgrep's own comparison page says the fork was taken from CE at v1.100.0. That page was modified **2026-10-15 (post-window)**, so it is context only.
- Press and vendor accounts of the fork's 2025 launch, which followed Semgrep's late-2024 rules-licence change, surfaced only in search snippets and pre-window articles. They were not re-read for this screen.
- In the window the fork stayed active: 20 releases, including a Python-free 2.0.0 alpha ([CI2026-092-031](092-semgrep.events.csv)).

**MCP:**
- The standalone [semgrep/mcp](https://github.com/semgrep/mcp) repo (MIT) is **archived**; its last push was 2025-10-28.
- MCP is now part of the CLI. In-window fixes appear in 1.162.0 and 1.173.0.
- Guardian bundles "the Semgrep MCP server, Hooks, and Skills" ([docs](https://docs.semgrep.dev/semgrep-guardian/overview)).

**Pre-window baseline (context only, not counted):** Multimodal launch (2026-03-19), Cursor plugins (2026-03-11), Autofix public beta (2026-03-16), Custom Workflows (2026-03-18). The Oct 14 Cursor Origin post and CE v1.181.0 (Oct 14) are **post-window** and excluded.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | OpenAI Trusted Access for Cyber / grant (Apr 17); Mythos replication research and `mythos-bench` repo (Apr 16–17); TeamPCP "not affected" statement (Apr 23); agent security skills guidance (Apr 28); PyTorch Lightning malware (Apr 30) | [blog](https://semgrep.dev/blog/2026/semgrep-chosen-to-be-part-of-openais-trusted-access-for-cyber-program), [blog](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training) | PyPI shows lightning 2.6.2/2.6.3 absent; HN 465 points | CE 1.160.0 (Apr 16) and 1.161.0 (Apr 22) are routine |
| 2026-05 | Dynamic Dependency Resolution beta (May 7); CLI 1.162.0 credential-hygiene fixes (May 7); April notes incl. read-only-user overwrite fix (May 12); competitor benchmark (May 25) | [release](https://github.com/semgrep/semgrep/releases/tag/v1.162.0), [notes](https://docs.semgrep.dev/release-notes/april-2026) | [Trent.ai](https://trent.ai/blog/claude-code-codex-semgrep-codeql-trent-vs-cwe-bench-cve/) (competitor) | Status: May 13 slowness, May 19–20 scheduling/login incidents (not ledgered) |
| 2026-06 | Pyro Caml OSS (Jun 2); performance series (Jun 5, Jun 10); 3.5x benchmark (Jun 12); GLM 5.2 benchmark (Jun 22); **Guardian launch (Jun 23)**; AI-skills-rules incident (Jun 25) | [blog](https://semgrep.dev/blog/2026/introducing-semgrep-guardian-real-time-security-for-ai-written-code), [status](https://status.semgrep.dev/incidents/p8222qljjxf1) | HN thread on GLM post (critical comments) | Guardian launch had 4 HN points; no trade coverage found |
| 2026-07 | Bedrock opt-out bypass and secrets-in-guidance fixes (week of Jul 6); June notes (Jul 8); Unified Policies GA and plaintext-credential fix (week of Jul 13); benchmark self-audit (Jul 17); OSS harness comparison (Jul 20); **Agentic Workflows public beta (Jul 28)** | [notes](https://docs.semgrep.dev/release-notes/2026-07-06), [blog](https://semgrep.dev/blog/2026/introducing-semgrep-agentic-workflows-automate-deep-vulnerability-hunting-at-scale) | Enterprise AI World (Aug 5) restates the release | Status: Jul 15–23 minor incidents |
| 2026-08 | Policies sunset announced (Nov 1) (week of Aug 3); Replit Security Center integration (Aug 11); GPT-5.6 Luna default (week of Aug 17); bad-release outage (Aug 25); Homebrew Intel drop (Aug 26); Mythos IDOR comparison (Aug 25/27); Autofix for all and permission fixes (week of Aug 31) | [notes](https://docs.semgrep.dev/release-notes/2026-08-03), [DEVOPSdigest](https://devopsdigest.com/semgrep-and-replit-expand-integration) | DEVOPSdigest (press-release reprint) | Status: Aug 12 lockfile-less scans, Aug 13 9-minute outage (not ledgered) |
| 2026-09 | Incomplete 1.176.1 PyPI release (Sep 4); Opengrep 2.0 alpha (Sep 5); minimal-retention workflows (week of Sep 7); SCIM beta and API deprecation policy (week of Sep 21); **Malware Detection and Response Automation** (Sep 24); Guardian signed binaries / Cursor Origin beta (week of Sep 28); SusVibes study (Sep 29) | [status](https://status.semgrep.dev/incidents/4p36pmnqykdq), [blog](https://semgrep.dev/blog/2026/introducing-malware-detection-and-response-automation) | none beyond vendor | Status: Sep 3, 10, 14, 22, 30 incidents (Sep 22 scan-upload interruption cited) |
| 2026-10-01..12 | MCP-vs-hooks post and Grok Build partnership (Oct 5); CE 1.180.0 removes QL language (Oct 7); "End Is Nigh for Code Review" direction post (Oct 9) | [blog](https://semgrep.dev/blog/2026/mcp-vs-hooks-ai-agent-security), [release](https://github.com/semgrep/semgrep/releases/tag/v1.180.0) | none found | CE 1.179.0 (Oct 2) adds `bun.lock` parsing (not ledgered); Oct 5 login incident on status page |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](092-semgrep.events.csv): 39 rows, IDs `CI2026-092-001`…`039`. Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-092-007 | 2026-05-07 | CLI 1.162.0: `semgrep ci` stops sending SCM tokens; credential redaction in telemetry; MCP `refs` parameter | Fixes imply earlier exposure surfaces; scope not disclosed | [GitHub release](https://github.com/semgrep/semgrep/releases/tag/v1.162.0) | PyPI upload 2026-05-07T16:04Z | E2 |
| CI2026-092-009 | 2026-05-25 | Competitor test: Semgrep 3.6% file-level detection on 28 CVEs vs Claude Code 8.7%, Trent 25% | Conflict of interest; configuration unstated | [Trent.ai](https://trent.ai/blog/claude-code-codex-semgrep-codeql-trent-vs-cwe-bench-cve/) (third-party vendor) | none | E1 |
| CI2026-092-001 / -013 | 2026-04-17 / 06-12 | Multimodal multiplier "up to 8x" vs LLMs alone, later 3.5x vs a tuned guided prompt | Vendor revised its own headline downward | [blog](https://semgrep.dev/blog/2026/3-5x-more-true-positives-how-we-benchmark-ai-powered-detection) | none | E1 |
| CI2026-092-015 | 2026-06-23 | Guardian: agent-time scanning via MCP, hooks and skills; Cursor and Claude Code partner | Hosted plugin uses a fixed ruleset that ignores org Policies; agent decides whether to regenerate | [blog](https://semgrep.dev/blog/2026/introducing-semgrep-guardian-real-time-security-for-ai-written-code) | [docs](https://docs.semgrep.dev/semgrep-guardian/overview) | E2 (documentary) |
| CI2026-092-016 | 2026-06-25 | Bad release of AI-skills rules broke scans (exit code 7); rule removed within ~1 h | Official status record; no postmortem | [status](https://status.semgrep.dev/incidents/p8222qljjxf1) | — | E2 |
| CI2026-092-017 / -019 | weeks of Jul 6 and Jul 13 | AI pipeline fixes: Bedrock opt-out bypass, secrets in saved AI guidance, plaintext workflow credentials | No advisory or CVE found | [notes](https://docs.semgrep.dev/release-notes/2026-07-06), [notes](https://docs.semgrep.dev/release-notes/2026-07-13) | CE 1.170.0 release | E2 |
| CI2026-092-022 | 2026-07-28 | Nine Agentic Workflows (public beta), 70+ CWEs, on AI credits | Proprietary; trade press restates the release | [blog](https://semgrep.dev/blog/2026/introducing-semgrep-agentic-workflows-automate-deep-vulnerability-hunting-at-scale) | [weekly notes](https://docs.semgrep.dev/release-notes/2026-07-27) | E2 |
| CI2026-092-030 | 2026-09-04 | Incomplete 1.176.1 PyPI release could not use the Pro Engine; pin advice issued | Resolved same day | [status](https://status.semgrep.dev/incidents/4p36pmnqykdq) | PyPI 2026-09-04T20:28Z | E2 |
| CI2026-092-035 | week of Sep 28 | Guardian binaries signed and verified ("SLSA Level 3"); auto-update; AI actions need triage permission | SLSA level self-declared | [notes](https://docs.semgrep.dev/release-notes/2026-09-28) | none | E2 (documentary) |
| CI2026-092-036 | 2026-09-29 | Opus 5.5 on SusVibes: 93.5% working, 54.8% working and secure; 53% near-identical to real code (memorization) | Single vendor run | [blog](https://semgrep.dev/blog/2026/claude-opus-5-5-susvibes-benchmark) | none | E1 |
| CI2026-092-031 | 2026-09-05 | Opengrep fork: Python-free 2.0 alpha; `OPENGREP_*` env alongside `SEMGREP_*` | Prerelease, testing only | [GitHub](https://github.com/opengrep/opengrep/releases/tag/v2.0.0-nopython.alpha.1) | v1.30.0 release | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent tooling | Guardian (MCP server + hooks + skills; Claude Code, Codex, Cursor, Copilot, VS Code, Kiro, Devin/Windsurf setups); Supply Chain hook; in-agent status reporting; signed auto-updating binaries; Cursor Origin beta; Grok Build partnership claim; Replit Security Center embedding | shipped / beta (vendor) |
| AI detection and remediation | Multimodal default model GPT-5.6 Luna; Agentic Workflows (9, public beta); Autofix for all customers across four SCMs; Memories; AI credits billing | shipped / beta, proprietary |
| Supply chain | Dynamic Dependency Resolution (beta); Rust reachability; CycloneDX 1.5–1.7 SBOM export; malware detection and response automation; malware firewall in Guardian (private beta); `bun.lock` parsing (1.179.0) | mixed |
| Governance | Unified Policies beta → GA, old Policies sunset Nov 1 2026; policies API; read-only tokens; SCIM beta; developer exception requests; API deprecation policy | shipped / announced |
| Security fixes disclosed only in notes | SCM token transmission, credential redaction, token storage, read-only overwrite, Bedrock opt-out bypass, secrets in AI guidance, plaintext workflow credentials, read-only token tag writes, provider-catalog bypass | fixed (vendor) |
| Engine/OSS | Taint engine redesign; file-targeting speedups; libpcre → libpcre2; OCaml 5.4; QL language removed; Dart GA; Pyro Caml 1.0.0 (MIT) | shipped |
| Licensing | CE engine LGPL-2.1; rules under Semgrep Rules License v1.0 (internal business use only); platform proprietary; in-window repos `mythos-bench`, `semgrep-grok-bot`, `guardian-local` have **no detected licence**; `defending-code-harness` NOASSERTION; `semgrep-policies-gitops` MIT | observed via GitHub API |
| Breaking/support changes | Homebrew on Intel macOS dropped; `--x-no-python-schema-validation` replaced; binary files skipped by default; Policies V1/Ruleboard APIs return 410 after migration; QL removed | observed |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Will "sunset the current version of Policies on November 1, 2026" after starting migrations August 24 | [notes, week of Aug 3](https://docs.semgrep.dev/release-notes/2026-08-03) | 2026-11-01 | planned (post-window) | Migration bugs fixed in Jul–Sep notes |
| Agentic Workflows "builds toward a security program that runs itself" | [2026-07-28](https://semgrep.dev/blog/2026/introducing-semgrep-agentic-workflows-automate-deep-vulnerability-hunting-at-scale) | none | uncommitted | Public beta only |
| "AI code review should check every change, and send only the exceptions to a human" | [2026-10-09](https://semgrep.dev/blog/2026/end-is-nigh-for-code-review) | none | opinion / uncommitted | No review-quality data |
| Industry "urgently needs independent auditors and provenance standards for AI models" | [2026-07-10](https://semgrep.dev/blog/2026/ai-supply-chain-problem) | none | advocacy, not a product commitment | — |
| Malware firewall "built into Guardian" (private beta) | [2026-09-24](https://semgrep.dev/blog/2026/introducing-malware-detection-and-response-automation) | none | tentative (private beta) | Efficacy unpublished |
| Hooks, not MCP alone, for mandatory agent security checks | [2026-10-05](https://semgrep.dev/blog/2026/mcp-vs-hooks-ai-agent-security) | none | design position | Guardian's MCP path still exists |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Security scanning for AI-written code moves from CI to authoring time inside the agent loop (hooks), with CI as a backstop | Guardian launch; hooks-vs-MCP argument; Cursor/Claude Code/Replit/Grok integrations | Vendor marketing; agents may ignore findings ("the agent decides whether to regenerate") | Controlled tasks show no fewer accepted vulnerabilities with agent-time scanning than with CI-only scanning | low; no outcome data |
| H2: Public-CVE benchmarks lose value for judging AI code security because of memorization | Semgrep's own SusVibes analysis (53% near-identical); vendor revising its multiplier 8x → 3.5x after a stronger baseline | One vendor's analysis; other benchmarks may control leakage | Held-out or post-cutoff CVE benchmarks show the same ranking and scores | moderate for "benchmarks are fragile", unknown for size |
| H3: Hybrid SAST+LLM tools add new data-governance failure modes on top of classic SAST | Bedrock opt-out bypass, secrets in AI guidance, plaintext workflow credentials, provider-catalog bypass all fixed in window | Normal maturation of new features; disclosure in notes is a positive transparency signal | No similar fixes in the next 12 months of notes; independent audits find none | moderate that the class exists; low on frequency |
| H4: Open-core divergence widens: the LGPL engine and fork track separately from proprietary analysis | Opengrep's 20 releases, Python-free 2.0 alpha, `OPENGREP_*` variables; Semgrep rules licence restricts competitor use; Pro features stay proprietary | The fork may stall; users may not need the cross-file analysis that sits behind the paywall | Fork activity declines or the projects reconverge on a shared rules licence | low–moderate |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Security checks run as agent hooks during authoring | Count opt-in repos with agent-time scanners vs CI-only | Only enterprise teams adopt | Consented configs only |
| M2 accepted task quality | Agent-time scanning may reduce shipped vulnerabilities but raise regeneration loops | Same frozen tasks with and without hook scanning, hidden security tests | No difference in accepted-and-secure rate | All attempts in denominator |
| M3 discoverability | Benchmark posts drew large HN attention (1113 points) while product launches drew little (Guardian: 4 points) | Separate attention from adoption | Attention is not reuse | HN points never used as an outcome |
| M4 verified third-party reuse | CE rules embedded in Replit; Opengrep fork reuses the engine; Pyro Caml MIT | Trace consented downstream repos that actually run the component | Code presence without execution | Pinned commits; executed tests only |
| M5 rights/security/provenance | Rules licence restricts reuse; several new repos have no licence; Guardian claims signed binaries | Licence check before reuse; verify signatures ourselves | A licence or signature claim says nothing about efficacy | Licence files at a pinned commit |
| M6 review/maintenance and lifecycle cost | Weekly CE releases (21 in window), several breaking/support changes, a bad patch release, a Policies sunset | Measure upgrade minutes per pinned minor version | Upgrades cheap in practice | No kWh/CO2e inferred from scan counts |
| M7 actionable interventions | Pinning, cooldowns and pre-commit scanning are low-cost guardrails | See §8 | Guardrails add friction without catching anything | Synthetic tasks until approval |

Company claims such as "3 million scans every week", "95% user agreement" and "hundreds of security teams" are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), Python package `trending_study` plus `scripts/`. This runs as an offline, network-free task. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Add a reused, pinned Semgrep CE scan with community rules as a **pre-commit/CI check** on Python changes, and compare it against the existing review-only process. Reuse comes first: use the LGPL-2.1 `semgrep` CLI from PyPI at one exact version (record it). Before use, a human must confirm that the Semgrep Rules License v1.0 ("internal business use") covers this research repository. If that is unclear, use only rules under an OSI licence, or Opengrep with rules we already have rights to. Opengrep is an equivalent LGPL alternative for a sensitivity check. No hosted platform, Guardian, AI credits or account is used, and nothing is uploaded (`--metrics off`). Do not write new rules or a custom scanner.

**Treatment/control and frozen comparable task:**
- **Tasks:** freeze 12 small synthetic change tasks, e.g. a CSV-validator edge case, a CLI flag, or a file-path handling fix.
- **Hidden tests:** each task has **hidden acceptance tests**, including at least four with a planted security-relevant requirement (path traversal, unsafe YAML/pickle load, subprocess with `shell=True`, hardcoded token). A person other than the patch author writes the tests and keeps them out of the author's context.
- **Arms:** Arm A is review plus the full unit suite. Arm B is the same plus the Semgrep CE pre-commit check. Task order is randomized.
- **Accepted-task unit:** one patch that passes hidden functional and security tests and is accepted by the human reviewer without rework.

**Success and guardrails:**
- **Primary measure:** accepted-and-secure tasks / all 12 assigned (failed, abandoned and timed-out tasks included).
- **Secondary measures:** findings per task, false positives judged by the reviewer, and minutes spent triaging findings.
- **Guardrails:**
  - full unit suite green;
  - no new runtime dependency (Semgrep is a dev-only tool pinned in a separate dev requirements file, or run via `pipx`);
  - no network access during scans;
  - no source code sent to any service;
  - no paid API spend without explicit approval;
  - commit authorship stays with the maintainer.
- **Measured human work:** setup minutes, per-task review minutes, and minutes spent on false positives.
- **Energy:** no energy or CO2e estimate unless metered.

**Stop/reversal rule:** keep Arm A and remove the hook if any of these holds:
- Arm B catches none of the planted security requirements that Arm A missed.
- More than half of its findings are judged false positives.
- It adds more than 5 triage minutes per task on average.
- Upgrading the pinned version breaks the hook within the trial period.

**No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, vendor-sourced):**
  - 21 CE releases v1.160.0–v1.180.0, with GitHub and PyPI dates consistent.
  - CLI credential-hygiene fixes in 1.162.0 and 1.166.0.
  - Guardian, documented with setup pages for many agents.
  - Agentic Workflows public beta; Unified Policies GA; Autofix for all customers; SCIM beta.
  - Malware detection and response.
  - QL language removed; Homebrew Intel support dropped.
  - Pyro Caml 1.0.0 (MIT).
  - Multiple status-page incidents, including two caused by bad releases (Jun 25 rules, Aug 25 platform) and one incomplete PyPI release (Sep 4).
- **Claims/announcements only:**
  - Benchmark multipliers (8x, 3.5x), F1 scores, 63 IDORs vs Mythos, and the SusVibes results.
  - Usage figures (3M scans/week, 95% agreement) and performance figures (75%, P99 60→12 min).
  - The OpenAI grant, Replit's "93.3%" false-positive filtering, the "SLSA Level 3" claim and the Grok Build partnership.
  - Direction statements in §5.
- **Conjectures and unknowns:** H1–H4 in §6; actual detection quality on our code; Guardian data handling on the hosted path; status history before May 13; tier-1 press coverage (none found).
- **Important contradictory or null evidence:**
  - The vendor's own multiplier fell from "up to 8x" (Apr 17) to 3.5x (Jun 12) against a stronger baseline.
  - A competitor benchmark (Trent.ai, conflict of interest, n=28) puts Semgrep's file-level detection at 3.6%.
  - HN commenters criticized the GLM 5.2 post as advertising and IDORs as an easy class.
  - Several security and privacy defects in AI features were disclosed only in release notes, with no advisory. The GitHub advisory and NVD queries returned nothing in-window.
  - The April 2026 release notes list CE 1.157.0 as released in April, but GitHub and PyPI date it 2026-03-31T22:51Z (minor dating inconsistency).
  - Aggregator snippets about a "September outage" and a "co-CTO hire" were not confirmed (E0, unused).
- **#56 candidates (not minted):** Trent.ai 2026-05-25 (competitor benchmark); DEVOPSdigest 2026-08-11 (press-release reprint); Enterprise AI World 2026-08-05 (press restatement). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned. Syndicated copies of one press release must not be counted twice.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
