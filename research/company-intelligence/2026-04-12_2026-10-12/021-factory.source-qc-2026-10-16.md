# Factory (021) — source QC of existing ledger rows and spot-check of new rows (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](021-factory.md), [event ledger](021-factory.events.csv) and [search log](021-factory.search-log.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #88 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Method:** on 2026-10-16 an AI assistant opened each existing row's `source_url` (read-only public HTTPS, no login) and compared the displayed title, displayed publication date, `claim_summary` and `status`. Page text is publisher-controlled and may change; no archived byte hash was captured. This is **not** independent human factual review.

## A. Existing rows (6) — QC outcome

| event_id | URL | Reachable? | Displayed date == published_utc? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI2026-021-001 | https://factory.ai/news/automated-qa | Yes — **307 redirect** to https://factory.com/news/automated-qa | Yes (April 23, 2026) | Yes; page says "available today in all Factory plans" → `shipped` supported | None. URL kept verbatim; redirect noted only here. |
| CI2026-021-002 | https://factory.ai/news/factory-router | Yes — resolves to https://factory.com/news/factory-router | Yes (June 1, 2026) | Yes; "private research preview" (CLI + Desktop App), vendor-reported 20–25% token-spend reduction | None. |
| 021-E01 | https://factory.com/news/software-factory | Yes | Yes (June 15, 2026) | Yes — mostly vision; names existing components (Droids, Automations, Droid Computers, Missions, Router) and a desktop-app update but gives no release dates/specs. `announced_only` kept as the label for the *vision*; the named components are not newly dated by this page. | None. |
| CI2026-021-003 | https://factory.ai/news/wiki | Yes — resolves to https://factory.com/news/wiki | Yes (June 17, 2026) | Yes; "available to all plans today"; `/install-wiki` creates a GitHub Actions or GitLab CI workflow; incremental diff-based regeneration | None. |
| 021-E02 | https://factory.com/news/model-routing-belongs-in-the-harness | Yes | Yes (August 24, 2026; author Abhay Singhal) | Yes; 58% aggregate cost reduction across production sessions vs frontier-model-for-every-call | None. |
| 021-E03 | https://factory.com/news/factory-router-inference-savings | Yes | Yes (September 23, 2026) | Yes; 63% aggregate vs published frontier-model rates on the same workload; Router available in **Factory Private (private preview)** for VPC/on-prem/air-gapped | None. |

**Outcome:** 6/6 reachable, 6/6 dates match, 6/6 claims and status supported. **No existing row corrected.** Two event_id schemes (`CI2026-021-NNN` and `021-E0N`) were inherited from two merged drafts and are preserved unchanged; new rows continue `CI2026-021-NNN` from 004.

## B. Spot-check of new rows (7 of 24)

Each new row was written from a page/API response read on 2026-10-16; the rows below were re-checked after the CSV was written (GitHub rows by a second `gh api` call; web rows against the narrow-prompt reading logged in the [search log](021-factory.search-log.md)).

| event_id | URL | Reachable? | Date matches? | Claim supported? | Note |
|---|---|---|---|---|---|
| CI2026-021-015 | https://github.com/Factory-AI/vfs/releases/tag/v1.0.0 | Yes (API) | Yes, `published_at` 2026-08-08T07:30:03Z | Yes — release notes: "First release under Factory's own identity", fork diverged from agentfs after 0.6.4 | `repos/Factory-AI/vfs/license` returns 404 → "no licence detected", not "unlicensed" |
| CI2026-021-025 | https://github.com/Factory-AI/droid-action/releases/tag/v10 | Yes (API) | Yes, 2026-10-06T20:08:04Z | Yes — `ghs_` long-token redaction fix (#160) | `status=corrected` = disclosed mitigation; exposure unknown |
| CI2026-021-022 | https://factory.com/news/legacy-bench-specialized-intelligence-index | Yes | Yes (September 24, 2026) | Yes — 60.0% vs 52.0%; ten tasks on GitHub | `Factory-AI/legacy-bench` licence Apache-2.0 per GitHub API |
| CI2026-021-020 | https://factory.com/news/5-billion-valuation | Yes | Yes (September 15, 2026) | Yes — $200M, $5B; no lead named on page | Neither the page nor TNW (Sep 17) names a lead; a search-result summary (S1) described four investors as leading — unverified, so the row says only "investors listed include" |
| CI2026-021-011 | https://factory.com/news/droid-shield-2-0 | Yes | Yes (July 1, 2026) | Yes — "research preview", Qwen 3.6 35B A3B, HF weights | HF API: no licence tag on either model |
| CI2026-021-004 | https://factory.com/news/series-c | Yes | Yes (April 16, 2026) | Yes — $150M, $1.5B, Khosla lead; Gunderson note concurs | Page now also mentions the later $5B round (edited after publication) |
| CI2026-021-014 | https://www.cityam.com/?p=2447558 | Yes (shortlink) | Yes (04 August 2026) | Yes — unnamed sources, Factory no response, Blackstone declined | Superseded on valuation by CI2026-021-020; kept as contradictory/unconfirmed press |

**Doubtful items flagged for human review:** (1) Factory's attribution of CVE-2026-42876 to its automated reviews (CI2026-021-007/-009) is a vendor claim; the GHSA credits were not checked to identity level. (2) The Series C page has been edited since publication (it references the September round), so its original text is not preserved. (3) The changelog page is long (≈214k characters) and was read through two windowed fetches; entries were summarised by a fetch model, so exact version/date pairs deserve a human re-read.
