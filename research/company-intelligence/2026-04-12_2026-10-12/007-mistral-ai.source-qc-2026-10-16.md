# Mistral AI (007) — source QC of existing ledger rows and spot-check of new rows (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](007-mistral-ai.md), the [event ledger](007-mistral-ai.events.csv) and the [search log](007-mistral-ai.search-log.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. Merging is not scientific or security sign-off; issue #73 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Scope:** assistant-performed, read-only re-opening of every source URL in the six pre-existing ledger rows (CI-007-01 … CI-007-06, produced by PR #193), on 2026-10-16. Each page was fetched once over public HTTPS; no login, paywall or scraping. "Date matches" compares the page's displayed date with `published_utc`. This is **not** an independent human factual check; page text can change after access and no byte snapshot was stored.

## A. Existing rows (all six re-opened)

| event_id | URL | Reachable? | Date matches? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI-007-01 | https://mistral.ai/news/workflows/ | yes | yes (Apr 27, 2026) | yes — "releasing Workflows in public preview"; "built on Temporal's durable execution engine"; Mistral hosts the Temporal cluster/API/Studio, customer workers run in their own Kubernetes environment | none (status `preview` correct) |
| CI-007-02 | https://mistral.ai/news/connectors/ | yes | yes (May 22, 2026) | **partly** — connectors are real, but the page labels them "in Public Preview", not generally available | **corrected:** `status` `shipped` → `preview`; `limitation` rewritten to record the public-preview label and that GA connector governance controls are a separate Jun 24 row (CI-007-11); `confidence` changed to `corrected 2026-10-16; provider-attributed only`. Other columns (incl. `availability` "vendor-reported availability") unchanged per contract. |
| CI-007-03 | https://mistral.ai/news/vibe-agent/ | yes | yes (May 28, 2026) | yes — Le Chat "now Vibe", Work Mode, Code Mode remote sandboxed sessions ending in a PR, VS Code extension, CLI updates; no specific model (Devstral/Codestral) named | none; `limitation` extended to note that the remote-agent launch itself was first announced May 22 (CI-007-08) and that the page does not state CLI licence (GitHub reports Apache-2.0 for mistralai/mistral-vibe) |
| CI-007-04 | https://mistral.ai/news/manage-prompts-and-skills-in-studio/ | yes | yes (Jul 9, 2026) | yes — immutable versions, rollback, owners, labels, audit logs; "available to Mistral Studio customers today" (no GA/preview label) | none |
| CI-007-05 | https://mistral.ai/news/regional-inference-open-models-new-compute/ | yes | yes (Aug 11, 2026) | **mixed** — the page announces **Regional Endpoints "generally available"** and **Priority Tier "in public preview"** as well as future compute (ECUs, "up to 1 GW of capacity by 2030" in a summary block) | `status` kept `announced_only` because the row's feature is the compute/infrastructure *direction*; `limitation` rewritten to scope it to that direction and to point to new row CI-007-15 for the GA regional endpoints; `confidence` unchanged |
| CI-007-06 | https://mistral.ai/news/mistral-large-4/ | yes | yes (Oct 6, 2026) | yes — "launching a public preview"; "1 trillion-parameter natively multimodal model with 52 billion active parameters"; "We will release the weights by the end of the month"; no weight licence stated | none; `limitation` extended: secondary coverage reports a conflicting 49B-active figure (unresolved); Hugging Face API listing on 2026-10-16 showed no Large 4 weight repository |

**Outcome:** 6/6 reachable; 6/6 displayed dates match; 4 rows supported as recorded, 1 row **corrected** (CI-007-02 status), 1 row **scope-clarified** (CI-007-05 limitation). No row deleted; no event_id changed. No page contained text addressed to AI agents.

## B. Spot-check of new rows (added 2026-10-16)

| event_id | URL | Reachable? | Date matches? | Claim supported? | Note |
|---|---|---|---|---|---|
| CI-007-10 | https://docs.mistral.ai/resources/security-advisories/MAI-2026-002 | yes | yes (published 2026-05-12, updated 2026-05-14) | yes — npm `@mistralai/mistralai` 2.2.2–2.2.4, `-azure`/`-gcp` 1.7.1–1.7.3 and PyPI `mistralai` 2.4.6 compromised; "no impact on Mistral global infrastructure" | Cross-checked against GitHub advisory GHSA-wx9m-wx4f-4cmg (repo advisory published 2026-05-12T12:57:44Z) and LiteLLM's independent May 12 post |
| CI-007-12 | https://mistral.ai/news/leanstral-1-5/ | yes | blog Jul 2 vs docs changelog Jun 30 (**discrepancy recorded**) | yes — 119B/6B-active, Apache-2.0, weights on Hugging Face (HF repo createdAt 2026-07-01) | Docs changelog later lists API model `labs-leanstral-1-5` deprecated with retirement Sep 30, 2026 (CI-007-20) |
| CI-007-14 | https://mistral.ai/news/shieldstral/ | yes | blog Aug 4 vs HF repo createdAt 2026-07-16 (repo creation ≠ public release; not a contradiction by itself) | yes — "3B open-weights, policy-adaptive multimodal safety classifier", Apache 2.0 | Benchmark claims vendor-run, charts only |
| CI-007-18 | https://docs.mistral.ai/resources/security-advisories/MAI-2026-003 | yes | yes (2026-09-14) | yes — six CVEs CVE-2026-87983…87988, fixed in Vibe 2.25.4 (released 12 Sep 2026); HiddenLayer published the CVEs 11 Sep | GitHub API shows release v2.25.4 at 2026-09-12T18:39:34Z; OpenCVE lists CVE-2026-87984 published 2026-09-11, CNA HiddenLayer, CVSS 4.0 9.3 |
| CI-007-17 | https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/ | yes | **article shows no date**; news index lists Sep 8, 2026 | yes — €3B Series D, >€21B post-money, Samsung Electronics lead | Independent Techzine article dated Sep 8, 2026 corroborates amount/lead; valuation and customer figures remain company-sourced |
| CI-007-19 | https://mistral.ai/news/mistral-x-mozilla/ | yes | yes (Sep 16, 2026) | yes — Firefox Smart Window "(beta)" "now powered by Mistral models" in France and North America; UK/Germany "expected to follow later this year" | No model names or on-device claim |

**Spot-check outcome:** 6/6 new rows reachable and supported; two date discrepancies (Leanstral blog vs changelog; €3B article undated) are recorded in the ledger `limitation` field rather than resolved by guess.

## C. Unresolved / for the human reviewer

- Mistral Medium 3.5: docs changelog says released **Apr 28, 2026** as open weights (Modified MIT); the May 22 blog labels it "public preview" on the API; Hugging Face repo `mistralai/Mistral-Medium-3.5-128B` has `createdAt` 2026-03-31 (repo creation, possibly private before release). Public-release day is **unresolved**.
- Large 4 active parameters: official page 52B; secondary aggregators report a 49B figure. Not resolved; official figure recorded as vendor-reported.
- `mistralai/search-starter-app` (MIT per GitHub API) has `created_at` 2026-09-18, but the Aug 20 Agentic Search post links to it — the post may have been edited after publication. Recorded as a provenance caveat.
- CVE record (OpenCVE, 2026-09-11) names no fixed version while Mistral's advisory (2026-09-14) names 2.25.4 — consistent with a record that predates the fix; no contradiction asserted.
