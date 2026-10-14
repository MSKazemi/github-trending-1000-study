# GitGuardian — provisional six-month source-ledger companion (#164)

- **Company watchlist ID:** 096, GitGuardian (label recorded in the existing ledger; historical ownership/product identity review remains pending).
- **Research issue:** [#164](https://github.com/MSKazemi/github-trending-1000-study/issues/164).
- **Analysis window:** 2026-04-12 through 2026-10-12 inclusive, UTC dates.
- **Status:** collecting; provisional documentary companion, **not independently checked or completed research**.
- **Preparation date:** 2026-10-14. Factual/source reviewer and human review: **pending**.
- **Inputs:** existing [19-row event ledger](096-gitguardian.events.csv), [company issue register](../../../references/ai_software_company_issue_index_2026-10-12.csv), [company research method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), and [report template](../../../templates/company_six_month_intelligence.md).

This report summarizes what the existing CSV records. No external pages were fetched, no software was installed or exercised, and no new sources, independent observations or human approval were obtained while preparing it. The source records and citations are preserved unchanged. **Issue #164 remains incomplete.**

## 1. Search and inclusion audit

The CSV records `accessed_utc=2026-10-14` for all 19 rows, at date precision only. This is an inherited source-access assertion, not an authenticated request timestamp or a newly performed check. It is after the retrospective window and must not be treated as contemporary observation of each event. Exact queries, search engine/site runs, found/screened/excluded denominators, inaccessible sources and complete month-by-month search logs are not supplied by this branch.

Rows have publication or underlying-event dates inside the specified window. Rows 002, 004, 005, 008, 009, 011, 015 and 017 have no publication date; their event-date fields cannot fill that gap. Row 007 records publication on July 7 and event on July 8; preserve that distinction. Rows 006 and 014 have no underlying event date. Inclusion here is a summary of recorded fields, not an independent date verification.

## 2. Company/product baseline and source boundaries

The index associates watchlist entry 096 with [GitGuardian's vendor site](https://www.gitguardian.com/). The ledger distinguishes GitGuardian SaaS, self-hosted releases, ggshield versions, agent-skills, Developer Endpoint Protection, Public Monitoring, vendor security research and Harbor registry integration. These are recorded product labels; company ownership as of October 12, historical licensing, plan entitlement and availability are not independently verified here.

Six ggshield rows (002, 004, 005, 009, 011, 015) cite the same **mutable** [GitHub `main` changelog](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md). A current changelog heading is not a frozen historical artifact or a release-publication timestamp. Before documentary acceptance, locate and review appropriate immutable commits/tags and permitted source provenance; preserve the original URLs and distinguish tag/commit dates from announcement dates. No pin, checksum or historical source-access attestation is invented in this report. The agent-skills row's current-license assertion likewise does not establish a historical license or agent-support matrix.

## 3. Calendar-segment coverage in the supplied ledger

| UTC segment | Recorded lead IDs | Source-search completeness |
|---|---|---|
| 2026-04-12..30 | 001, 002 | Unknown; systematic search log missing |
| 2026-05 | 003, 004 | Unknown; systematic search log missing |
| 2026-06 | 005, 006 | Unknown; systematic search log missing |
| 2026-07 | 007, 008, 009 | Unknown; systematic search log missing |
| 2026-08 | 010, 011, 012 | Unknown; systematic search log missing |
| 2026-09 | 013, 014, 015, 016, 017 | Unknown; systematic search log missing |
| 2026-10-01..12 | 018, 019 | Unknown; systematic search log missing |

Short IDs above mean `GG096-2026-NNN`. A row in every calendar segment does **not** prove the entire six-month window was searched. The 19 rows are source leads, not 19 independently verified distinct product releases. Rows 015 and 016 share `duplicate_event_group=ggshield-1.55-output-protection`; retain both sources without double-counting that claimed capability.

## 4. Recorded event leads and limitations

The table retains every event ID and source URL. Summaries, dates, status and E1/E2 labels below are **inherited ledger claims awaiting source review**. All 19 `independent_check_url` fields are blank. Under the company-watch method, E1 denotes first-party announcement evidence and E2 documentary artifacts; the labels here remain provisional, particularly where source versions are unpinned. They are not the study's E0–E5 causal lesson grades and do not imply E3 independent behavior testing or E4 replicated impact.

`shipped` below means vendor-reported availability, not an independently installed/tested release. `preview` preserves beta/progressive-rollout limits; `reported_undetermined` supplies no verified deployment date. Missing dates stay unknown.

| Event ID | Recorded publication / event date | Recorded claim and original source | Recorded status / tier | Existing limitation (unverified source assertion) |
|---|---|---|---|---|
| GG096-2026-001 | 2026-04-13 / 2026-04-13 | [Control team access to any Internal Monitoring source type](https://docs.gitguardian.com/releases/saas/2026/04/13/changelog): access governance for non-VCS sources | shipped / E1 | Vendor notice; plan and historical rollout independent verification absent |
| GG096-2026-002 | unknown / 2026-04-28 | [ggshield CHANGELOG 1.50.0](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md): Sigstore plugin wheel identity verification; OS keyring; default fail-closed on server 5xx | shipped / E2 | Dated changelog heading; publication timestamp unavailable; --allow-unsigned and file-store fallback limit protections |
| GG096-2026-003 | 2026-05-21 / 2026-05-21 | [Open-source agent skills - teach AI coding assistants to use ggshield](https://docs.gitguardian.com/releases/saas/2026/05/21/changelog): Published agent skills for Claude Code and Cursor | shipped / E2 | MIT repo visible now; historical supported-agent feature matrix must not be inferred from current main |
| GG096-2026-004 | unknown / 2026-05-26 | [ggshield CHANGELOG 1.51.0](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md): Codex AI hook; signed GitHub Artifact Attestations; headless auth; MCP inventory | shipped / E2 | Changelog states added; actual hook enforcement and attestation verification not exercised |
| GG096-2026-005 | unknown / 2026-06-15 | [ggshield CHANGELOG 1.52.0](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md): Historical Claude MCP activity discovery; AWS honeytoken CLI; auth verification for agent hook install | shipped / E2 | History uploads and token-scope expansion require permission review |
| GG096-2026-006 | 2026-06-16 / unknown | [Extending Our Mission with Developer Endpoint Protection](https://blog.gitguardian.com/extending-our-mission-with-developer-endpoint-protection/): Vendor introduced endpoint protection positioning for AI tools and developer machines | reported_undetermined / E1 | Announcement does not independently establish GA dates or plan eligibility |
| GG096-2026-007 | 2026-07-07 / 2026-07-08 | [Generic Detectors landing on your non-VCS sources, powered by the False Positive Remover](https://docs.gitguardian.com/releases/saas/2026/07/08/changelog): Generic password and high-entropy detection for Jira; Slack; Confluence; Teams with vendor LLM false-positive filtering | shipped / E1 | Vendor-reported 25-40% false-positive filtering is internal benchmark, not replicated; publish vs release differs |
| GG096-2026-008 | unknown / 2026-07-24 | [2026.7 - Required](https://docs.gitguardian.com/releases/self-hosted/2026-07-changelog): Required release with license-gated Public Monitoring and optional MCP server; Endpoint Protection known nonfunctional | shipped / E2 | Vendor explicitly warns self-hosted Endpoint Protection not functional in 2026.7.0; no installation test |
| GG096-2026-009 | unknown / 2026-07-28 | [ggshield CHANGELOG 1.53.0](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md): experimental raw agent activity upload; machine setup/doctor; detect core.hooksPath shadowing | shipped / E2 | Activity upload is experimental and privacy-sensitive; release heading may differ from GitHub tag timestamp |
| GG096-2026-010 | 2026-08-14 / 2026-08-14 | [Set your own validity status on a secret](https://docs.gitguardian.com/releases/saas/2026/08/14/changelog): Customer API can supply secret validity for otherwise unreachable systems | shipped / E1 | Customer-provided validation is not an independent verification; requires secrets:write permission |
| GG096-2026-011 | unknown / 2026-08-26 | [ggshield CHANGELOG 1.54.0](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md): Native Rust AI hook dispatcher; Mistral Vibe support; fixes for skipped content and hook handling | shipped / E2 | Vendor mock API latency numbers not independent benchmark; fixes disclose earlier bypass paths |
| GG096-2026-012 | 2026-08-27 / 2026-08-27 | [GitGuardian agents tell you which Public Monitoring incidents are actually yours](https://docs.gitguardian.com/releases/saas/2026/08/27/changelog): AI company attribution; Related/Uncertain/Unrelated verdicts and model risk scores | preview / E1 | Progressive beta availability; unrelated risk score 0 can hide genuine events; no FPR/FNR measured |
| GG096-2026-013 | 2026-09-07 / 2026-09-07 | [See all your AI agents across the fleet. Stop them leaking your secrets.](https://docs.gitguardian.com/releases/saas/2026/09/07/changelog): fleet MCP/agent inventory and hooks for Codex; Vibe; Claude; Cursor; Copilot; VS Code | shipped / E1 | Vendor claims support not independently tested; entitlement; personal subscription metadata governance |
| GG096-2026-014 | 2026-09-22 / unknown | [GitHub App Private Keys: 474 Leaked Keys Exposed](https://blog.gitguardian.com/github-app-private-keys-leaked/): Vendor tested 4802 selected GitHub-context keys; reports 474 valid keys tied to 440 Apps | reported_undetermined / E1 | Vendor-run self-selected 4802-key frame from >500000 RSA detections; no independent replication; not product efficacy |
| GG096-2026-015 | unknown / 2026-09-24 | [ggshield CHANGELOG 1.55.0](https://github.com/GitGuardian/ggshield/blob/main/CHANGELOG.md): Kiro IDE/CLI and Junie CLI hooks; tool-output protection; Windows Cursor BOM fix; Git hook precedence fixes | shipped / E2 | Junie IDE excluded; tool-output blocking not uniform; grouped with 25 Sep SaaS detail |
| GG096-2026-016 | 2026-09-25 / 2026-09-25 | [AI Hooks keep leaked tool output away from the model](https://docs.gitguardian.com/releases/saas/2026/09/25/changelog): Documented model vs local transcript boundaries and agent-specific output interception | shipped / E1 | Not independent product test; Codex/Vibe local session output persists; other agents may expose tool output |
| GG096-2026-017 | unknown / 2026-09-25 | [2026.9](https://docs.gitguardian.com/releases/self-hosted/2026-09-changelog): Release compatibility and changed Jira/Confluence Data Center PAT renewal behavior | shipped / E1 | Compatibility minimum and upgrade notes must be checked against installed version; no field deployment |
| GG096-2026-018 | 2026-10-07 / 2026-10-07 | [Environments, Classified at the Secret Level For You](https://docs.gitguardian.com/releases/saas/2026/10/07/changelog): Classify secret environments with contextual tags and scanner metadata | shipped / E1 | Dependent tooling/version prerequisites and historic rollout not tested |
| GG096-2026-019 | 2026-10-09 / 2026-10-09 | [Scan your Harbor container registry for secrets](https://docs.gitguardian.com/releases/saas/2026/10/09/changelog): Beta scanning of Harbor image layers; Dockerfiles and metadata via read-only robot account | preview / E1 | Beta; secrets only, not malware/SBOM/license/vulnerability scanner; network bridge and permission risks |

## 5. Company intentions and analyst interpretation

No independently verified binding roadmap, future release schedule or 2027–2031 company commitment is established by these records. Row 006 records vendor positioning for Developer Endpoint Protection; that announcement is not a confirmed general-availability date. The source leads suggest questions about agent-hook enforcement, credential handling and monitoring, but do not establish product efficacy, adoption, hiring priorities, total investment or future strategy.

**Conditional hypothesis only:** properly configured, independently tested existing secret-scanning components could improve a bounded agent workflow's handling of synthetic credentials. Alternatives include incomplete hook coverage, transcript leakage, false negatives/positives, plan restrictions, permission expansion and increased operator effort. Failure to meet independently frozen safety criteria would disconfirm the practical hypothesis. No empirical benefit, numeric energy saving or causal lesson is claimed.

## 6. Study mapping and one proposed repository task

The CSV's mappings concern **M1** workflow change, **M2** accepted quality, **M5** verified reuse and **M6** lifecycle cost. They are research-question pointers, not observed outcomes. M3 attention and M4 downstream use cannot be inferred from vendor announcements; M7 ethical adoption requires its own evidence and permissions.

**Proposed task, not executed:** before integrating any tool, an independent reviewer would freeze a small offline workflow containing only synthetic credential-shaped strings and harmless controls, exact tool/version/license provenance, and required fail-closed behavior. Compare a reviewed existing scanning component with the same workflow's existing baseline; install or run nothing without the separate rights/security review. Keep agent hooks, scanning and public claims within the independently accepted task scope.

Measure all attempted cases, misses, false alarms, handling of scanner failure and unintended disclosure to transcripts or networks, plus reviewer/repair and maintenance effort. Independent acceptance must assess safety as well as detection. Stop if a safety requirement fails, identities/rights are unresolved or telemetry exceeds consented scope. A null result or greater operator cost remains a valid outcome. No tool recommendation, human trial authorization or token-to-kWh conversion follows from this proposal.

## 7. Remaining review and completion gates

- Establish historical company/product identity, source access/retention rights and version/plan/license constraints; no full copyrighted descriptions, real credentials or personal traces belong in the public report.
- Complete documented searches across all seven calendar segments, including independent reporting, negative/conflicting evidence and inaccessible sources; retain denominators and omissions.
- Verify source text, publication/event dates and claim-to-source attribution; pin the mutable ggshield artifacts through a separately reviewed provenance record without rewriting the original ledger.
- Reconcile duplicate event groups and availability boundaries. The vendor-reported filtering percentages, selected-key research counts and performance figures are not independently replicated efficacy estimates.
- Obtain genuine independent factual/link QA and qualified human review. This offline companion and passing artifact/tests checks authenticate neither sources nor reviewer independence.
- Establish any actual accepted task, downstream reuse or lifecycle outcome separately before producing a validated lesson or closing [#164](https://github.com/MSKazemi/github-trending-1000-study/issues/164).

See the [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) and [scientific merge gate](../../../docs/PR_MERGE_QUALITY_GATE_2026_10_13.md). This report supplies the missing companion document; it does **not** fulfil the independent six-month research issue.
