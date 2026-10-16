# Cohere (008) — source QC of the existing ledger rows and spot-check of new rows (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](008-cohere.md), the [event ledger](008-cohere.events.csv) and the [search log](008-cohere.search-log.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #74 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Scope:** an assistant-performed, read-only recheck on 2026-10-16 of every source URL in the five rows (CI-008-01 … CI-008-05) that existed on `main` before this upgrade, plus a spot-check of new rows. Pages were read through a web reader (rendered text, summarised by the tool) and, for the Cohere docs changelog, through the page's embedded navigation metadata (entry dates). No page snapshot or hash was stored. This is **not** independent human factual QA.

## 1. Existing rows (from `main`)

| event_id | URL | Reachable? | Displayed date == published_utc? | Claim / status supported? | Action |
|---|---|---|---|---|---|
| CI-008-01 | https://cohere.com/blog/command-a-plus | yes | yes — "May 20, 2026"; docs changelog entry [command-a-plus-05-2026](https://docs.cohere.com/changelog/command-a-plus-05-2026) also dated May 20, 2026 | yes. Page says Command A+ (`command-a-plus-05-2026`, 218B total / 25B active MoE) "is available today on Hugging Face, as well as through Model Vault", open weights under Apache 2.0. `shipped` supported as a vendor availability claim. The old generic claim ("updated enterprise language-model offering") is under-specific but not wrong. | none (ok). Detail added in the report, not in the row. |
| CI-008-02 | https://cohere.com/blog/north-mini-code | yes | yes — "Jun 09, 2026"; [docs changelog](https://docs.cohere.com/changelog/north-mini-code-1-0) June 9, 2026 | yes. 30B total / 3B active MoE, Apache 2.0, weights `CohereLabs/North-Mini-Code-1.0`, also Cohere API, Model Vault, OpenRouter. | none (ok). Hugging Face artifact still not downloaded/hashed. |
| CI-008-03 | https://cohere.com/blog/introducing-north-automations-ai-workflows | yes | yes — "Jul 27, 2026" | yes. "Automations is available today to all North customers"; approval steps, per-step model routing, MCP custom tools. | none (ok). |
| CI-008-04 | https://cohere.com/blog/parse | yes (the old limitation recorded a reader error; the blog was readable on 2026-10-16) | yes — "Aug 27, 2026"; [docs changelog /changelog/parse](https://docs.cohere.com/changelog/parse) August 27, 2026 | yes. "Parse is now generally available via the Cohere API, Model Vault, Microsoft Foundry, and AWS SageMaker"; `parse-v5.0`. Blog gives no licence/open-weights statement. | none (ok). The historical limitation text is left unchanged (it describes the 2026-10-12/13 access attempt). |
| CI-008-05 | https://cohere.com/blog/introducing-north-2 | yes | yes — "Oct 05, 2026" | **partly.** Features (memory, skills, libraries, connectors incl. GitHub/Jira, model-agnostic, self-hosted/VPC/hybrid/on-prem/air-gapped) are described, but the page **does not state availability** (GA, preview, waitlist); the only availability line is "Contact sales to book a demo today." `shipped` is therefore not supported by the cited page. | **corrected:** `status` shipped → `reported_undetermined`; `confidence` → "provider-attributed only; availability not stated (QC 2026-10-16)"; `limitation` → "QC 2026-10-16: page states features but no GA/preview/waitlist status (only 'Contact sales to book a demo today'); tenancy and pricing vary; vendor-only capability claim." No other column changed. |

Other source URL cited by the old report and rechecked: https://docs.cohere.com/changelog/north-mini-code-1-0 — reachable (HTTP 200), entry dated June 9, 2026; https://cohere.com/blog — reachable (blog index, paginated).

**Summary for the old rows:** 5/5 reachable; 5/5 dates match; 4 ok; 1 corrected (CI-008-05 status). 0 unreachable.

## 2. Spot-check of new rows (second pass, same session, 2026-10-16)

Method: a second, independent retrieval of the raw page HTML (plain HTTPS GET, displayed date extracted by pattern) or of the GitHub API record, compared with the ledger values written in the first pass. Still the same AI analyst — not an independent reviewer.

| event_id | URL | Reachable? | Date matches? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI-008-08 | https://github.com/cohere-ai/cohere-python/releases/tag/7.0.0 | yes (API) | yes — `published_at` 2026-05-22T18:44:39Z | yes — only change listed: Python floor ^3.8 → ^3.10 (BREAKING) | none |
| CI-008-13 | https://cohere.com/blog/cohere-and-aleph-alpha-sign-agreement | yes | yes — "Sep 16, 2026" | yes — definitive business combination agreement; subject to regulatory approvals; `announced_only` appropriate | none |
| CI-008-14 | https://cohere.com/blog/compass-cloud-beta | yes | yes — "Sep 25, 2026" | yes — "entering private beta"; `preview` appropriate | none |
| CI-008-15 | https://cohere.com/blog/embed-5 | yes | yes — "Sep 30, 2026" | yes — "generally available today" | none |
| CI-008-16 | https://cohere.com/blog/vllm-integration-and-quality-recovery-techniques-explained | yes | yes — "Apr 22, 2026" | yes; upstream PRs #23198/#29691 merged 2025-08-24 / 2025-12-09 (pre-window) — recorded in `limitation` | none |
| CI-008-18 | https://cohere.com/blog/cohere-security-ai-agent-north-wiz | yes (first pass) | Jun 25, 2026 (first pass) | licence: GitHub API `MIT` re-confirmed | none |
| CI-008-19 | https://cohere.com/blog/cohere-signs-eu-code-of-practice | yes | yes — "Jul 31, 2026" | yes — Section 1 signature, vendor-stated | none |
| CI-008-20 | https://cohere.com/blog/megakernels | yes | yes — "Sep 08, 2026" | yes; repo licence Apache-2.0 via GitHub API | none |

**Doubtful / weaker sources flagged:** CI-008-17 (Dealroom aggregator; FT/Reuters originals not opened; valuation and 90/10 split are relayed, not verified) and CI-008-23 (nine-task hobby-scale test) are graded E0. The New Stack article on North Mini Code could not be read through the web reader (no body/date) and was excluded rather than cited.

**Not checked:** Hugging Face weight files or hashes (only public model-API metadata), European Commission signatory list, regulator filings for the Aleph Alpha combination, Reliant AI closing, and any Cohere security advisories outside the GitHub advisory database.
