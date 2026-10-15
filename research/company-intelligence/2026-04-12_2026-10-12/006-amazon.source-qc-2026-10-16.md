# Amazon / AWS (006) — source QC of existing ledger rows and spot-check of new rows (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](006-amazon.md), the [event ledger](006-amazon.events.csv) and the [search log](006-amazon.search-log.md) are **provisional, AI-assisted documentary source leads**, **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#72](https://github.com/MSKazemi/github-trending-1000-study/issues/72) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Method.** On 2026-10-16 each existing row's `source_url` was opened once with an AI web reader (public pages only; no login). Checked: reachable, displayed date equals `published_utc`, `claim_summary` and `status` supported by the page text. No page bytes, hashes or archive captures were stored, so later page edits cannot be excluded. Reader output is a model summary of the page, not a verbatim capture; quotations below are what the reader returned as page text.

## 1. Existing rows (9 rows from `main`)

| event_id | URL | Reachable? | Date matches? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI2026-006-001 | https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/ | yes | yes — "30 APR 2026" | yes — IDE plugins and paid subscriptions reach end of support 2027-04-30; new sign-ups stop 2026-05-15; Console, docs/marketing sites, Console Mobile App and Chat Apps (Slack/Teams) "not impacted" | none |
| CI2026-006-002 | https://kiro.dev/blog/faster-smarter-specs/ | yes | yes — May 12, 2026 | mostly — page describes parallel execution of *independent tasks* in dependency-graph waves, quick plan mode and requirements analysis; "independent subtasks" in the claim is a paraphrase, not page wording | limitation appended (wording note); status/confidence unchanged |
| CI-006-02 | https://kiro.dev/blog/introducing-kiro-web/ | yes | yes — May 18, 2026 | yes — "launching Kiro Web in preview for all paid subscribers — Pro, Pro+, and Power" | none |
| CI-006-03 | https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/ | yes | yes — "19 JUN 2026" | yes for the integration description; page carries **no** preview/GA label, so `shipped` = vendor-described availability only | limitation appended (no availability label on page); status unchanged |
| CI-006-04 | https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/ | yes | yes — "30 JUL 2026" | yes — two pillars (author-time, build-time), controls tagged deterministic/non-deterministic/human; guidance, not a product | none |
| CI-006-05 | https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/ | yes | yes — "05 AUG 2026" | partly — AWS Continuum for code vulnerabilities is "available in preview" (sign-up); the integrations with Claude Code, Codex and Kiro were "coming soon" at publication, so "partner-integrated workflow" was not yet available | limitation appended (integrations announced only); status `preview` kept for the Continuum service itself |
| CI2026-006-005 | https://kiro.dev/changelog/web/introducing-workflows/ | yes | yes — September 30, 2026 | yes — "Workflows are now available as an opt-in feature in Kiro Web cloud sessions" | none |
| CI2026-006-003 | https://kiro.dev/blog/cli-3/ | yes | yes — October 9, 2026 | yes — V3 opt-in since June; startup prompt "Starting October 12"; default with CLI 3.0 "at end of October" (future relative to cutoff) | none |
| CI2026-006-004 | https://kiro.dev/changelog/cli/ | yes | yes — 2.30.0 shown as Oct 12, 2026 | yes — 2.30.0 adds V3 startup prompt and model-fallback notices | limitation appended: URL is a paginated index (newer 2.31.x entries already above it on 2026-10-16); per-version path `/changelog/cli/2-30/` shown on the index, not opened separately |

**Outcome:** 9/9 reachable, 9/9 dates match, 7 fully supported, 2 partly supported (CI2026-006-002 wording, CI-006-05 integration scope) plus 2 clarifications (CI-006-03 no availability label, CI2026-006-004 index URL). **No status changed, no row deleted, no event_id changed.** Only the `limitation` column of four rows was appended to, as stated above.

## 2. Spot-check of new rows (added 2026-10-16)

All 21 new rows (CI2026-006-006 … CI2026-006-026) were written only after their source page was opened on 2026-10-16. Seven were re-read specifically against the final CSV wording:

| event_id | URL | Reachable? | Date matches? | Claim supported? | Note |
|---|---|---|---|---|---|
| CI2026-006-008 | https://www.theregister.com/software/2026/04/29/amazon-tells-its-engineers-to-review-all-ai-output/5224124 | yes | yes — 29 April 2026 | yes — named interviewee (Amazon Stores director); "Nothing ships without someone looking at it and validating it" | Independent outlet, single interview; not a controlled study |
| CI2026-006-009 | https://aws.amazon.com/security/security-bulletins/2026-035-aws/ | yes | yes — 05/22/2026 PDT | yes — CVE-2026-9255, kiro-cli < 1.28.0, fixed 1.28.0, `--no-interactive` workaround | Search-result summary also cited it; ledger relies on the bulletin page itself |
| CI2026-006-014 | https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/ | yes | yes — Jun 17, 2026 | yes — "generally available today"; Strands export; Claude Agent SDK "coming soon" | Search summary suggested Jun 18 for the ML blog; that blog was **not** opened |
| CI2026-006-019 | https://kiro.dev/blog/introducing-kiro-crew/ | yes | yes — August 4, 2026 | yes — open source, runs on Kiro CLI; 39,000 internal builders is a vendor claim | GitHub API (read-only): `kirodotdev/KiroCrew` Apache-2.0, created 2026-07-16, v0.1.0 2026-07-22 |
| CI2026-006-020 | https://aws.amazon.com/security/security-bulletins/2026-074-aws/ | yes | yes — 08/04/2026 PDT | yes — two CVEs, Windows only, fixed IDE 1.0.228 / CLI 2.10.0 | — |
| CI2026-006-023 | https://kiro.dev/blog/diagnostics-over-time/ | yes | yes — August 26, 2026 | yes — ~1.5M conversations, 406K diagnostics calls; authors' own caveat "A clean diagnostic check does not mean correct code" | Vendor analysis of internal users |
| CI2026-006-026 | https://kiro.dev/changelog/general/kiro-is-now-in-scope-for-fedramp-class-c/ | yes | yes — October 12, 2026 | yes — "in scope", US East (N. Virginia) only | Not an authorization letter |

**Outcome of spot-check:** 7/7 reachable, dates match, claims supported as worded. Not verified: vendor numbers (adoption, PR counts, error rates), the actual fix behaviour of any CVE, compliance-scope documents.

## 3. Doubtful or excluded material

- The Hacker News article on a Kiro web-page prompt-injection flaw (July 2026) returned **HTTP 403**; it is not cited. Third-party claims tying it to CVE-2026-10591 stay unverified.
- Search-result summaries named two other Kiro bulletins (2026-001, 2026-009) dated **before** the window; they are excluded.
- The `aws/amazon-q-developer-cli` README (GitHub API, read 2026-10-16) says the Apache-2.0 project "is no longer being actively maintained" and that Q Developer CLI "is now available as Kiro CLI, a closed-source product". Its last release (v1.19.7) is dated 2025-11-17, before the window, so it is used as rights baseline only, not as a ledger row.
- AWS's security-bulletin index shows only recent items; the full 2026-04-12…2026-10-12 bulletin set was **not** enumerated, so other Kiro, Q or AgentCore advisories may exist.
