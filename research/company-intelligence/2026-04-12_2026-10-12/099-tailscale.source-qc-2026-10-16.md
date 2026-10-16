# Tailscale #099 — independent source re-QC of the 26-row ledger (2026-10-16)

> **Provisional source-lead screen (re-checked 2026-10-16):** this note, the [report](099-tailscale.md), [event ledger](099-tailscale.events.csv), [search log](099-tailscale.search-log.md) and the earlier [2026-10-15 source-QC note](099-tailscale.source-qc-2026-10-15.md) are **provisional, AI-assisted documentary source leads**, unreviewed by a qualified human; factual/link, source-access/rights and methods review are pending. Merging is not scientific or security sign-off; issue [#167](https://github.com/MSKazemi/github-trending-1000-study/issues/167) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Scope and method.** A fresh, assistant-performed, read-only re-check of every existing ledger row (CI2026-099-001 … 026) on **2026-10-16**. Each cited `source_url` (and, where used, `independent_check_url`) was fetched once over HTTPS with a generic User-Agent containing no personal identifier; displayed dates were compared with `published_utc` (blog posts also via their embedded `datePublished` metadata), and the row's `claim_summary`/`status` were compared with the page text. GitHub release dates and licence metadata were read with read-only `gh api` calls (`repos/tailscale/tailscale/releases`, `repos/tailscale/tailscale`, `repos/tailscale/tailcat`, `repos/tailscale/tailcat/releases`). No login, paywall, scraping of github.com/trending or bulk crawl was used. Page snapshots were kept only in a session scratch folder and are **not** committed or immutable archives; a human re-check may see edited pages.

This is not an independent human check: the same model family that drafted the ledger performed this re-QC.

## Row-by-row outcome

Legend: **ok** = reachable, date matches, claim and status supported; **limitation+** = row kept, only `limitation` extended with a dated `QC 2026-10-16:` note (no `status`/`confidence` change was warranted).

| event_id | Source URL | Reachable? | Date matches? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI2026-099-001 | https://tailscale.com/changelog | yes (HTTP 200) | yes — "Apr 23, 2026" Aperture (beta) | yes — pre-LLM-call PII/tool hooks, log retention to zero, quotas | ok |
| CI2026-099-002 | https://tailscale.com/changelog | yes | yes — Apr 27 | yes — v1.5.2 removes Node 20 deprecation warning | ok |
| CI2026-099-003 | https://tailscale.com/changelog | yes | yes — Apr 29 | yes | ok |
| CI2026-099-004 | https://tailscale.com/changelog | yes | yes — May 13 (v1.98.1; Linux build withdrawn) and May 15 v1.98.2 | yes | limitation+: GitHub releases API has no v1.98.1 release object and shows v1.98.2 at 2026-05-18 UTC vs changelog May 15 |
| CI2026-099-005 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-002 dated May 13 | partly — "permitted changes" is broader than the bulletin, which describes **clearing** exit-node and advertised-subnet settings via an empty `/api/routes` body | limitation+: narrowed impact; bulletin names 1.98.0 as fixed but changelog says 1.98.0 was a release candidate only. `claim_summary` left unchanged (contract: only status/limitation/confidence may change) |
| CI2026-099-006 | https://tailscale.com/blog/aperture-cli-AI-experimentation | yes | yes — May 20 (page and `datePublished` 2026-05-20T14:15Z) | yes — alpha; bridge mode puts only the proxy connection on the tailnet | ok (page `<title>` differs from H1 "Introducing: Aperture CLI"; ledger title matches H1) |
| CI2026-099-007 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-003 May 29 | yes — Mar 1–May 29 tokens, one-hour lifetime, now redacted, no customer action | ok |
| CI2026-099-008 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-005 Jun 3 | yes — fixed 1.98.9 | ok |
| CI2026-099-009 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-004 Jun 3 | yes — bulletin says fixed 1.98.9; Jul 28 v1.98.10 changelog says it "addresses" TS-2026-004 | limitation+: v1.98.9 changelog does not list TS-2026-004; treat 1.98.10 as conservative minimum |
| CI2026-099-010 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-006 Jun 11 | yes | ok |
| CI2026-099-011 | https://tailscale.com/changelog (check: /blog/ai-without-lock-in) | yes / yes | yes — Jun 16 (blog `datePublished` 2026-06-16T13:00Z) | yes — connectors and chat "public alpha", sandboxes "private alpha" | ok |
| CI2026-099-012 | https://tailscale.com/blog/azure-blob-storage-streaming | yes | yes — Jun 17 (changelog also Jun 17) | yes | limitation+: blog limits destination to Premium and Enterprise plans |
| CI2026-099-013 | https://tailscale.com/changelog | yes | yes — Jun 30 | yes — "(alpha)" | ok |
| CI2026-099-014 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-007 Jul 10 | yes | ok |
| CI2026-099-015 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-008 Jul 13 | yes (bulletin adds that Funnel exposure means unauthenticated internet origin) | ok |
| CI2026-099-016 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-009 Jul 13 | yes | ok |
| CI2026-099-017 | https://tailscale.com/changelog | yes | yes — changelog Jul 14 | yes — entry cites TS-2026-005 … 009 | limitation+: GitHub release object v1.98.9 published 2026-07-20 UTC (6 days later); entry does not cite TS-2026-004 |
| CI2026-099-018 | https://tailscale.com/security-bulletins | yes | yes — TS-2026-010 Jul 24 | yes | ok |
| CI2026-099-019 | https://huggingface.co/blog/agent-intrusion-technical-timeline (check: /blog/hugging-face-intrusion) | yes / yes | yes — Jul 27 (`datePublished`); Tailscale response Jul 31 | yes — 181 enrollments with one stolen auth key; tailscale-phase 07-11 21:23 → 07-13 13:37; campaign 07-09 02:28 → 07-13 14:14 UTC; Tailscale says no Tailscale vulnerability found or exploited | ok |
| CI2026-099-020 | https://tailscale.com/changelog | yes | yes — Aug 3; GitHub release 2026-08-03 UTC | yes | ok |
| CI2026-099-021 | https://tailscale.com/blog/aperture-ga | yes | yes — blog Aug 26 (`datePublished` 2026-08-26T16:00Z); changelog Aug 25 (discrepancy already recorded) | yes — model tokens/credit, Tailscale and SSH MCP endpoints, Projects, default tool permissions | ok |
| CI2026-099-022 | https://tailscale.com/blog/tailcat | yes | yes — Aug 31 | yes — open-source Go package + CLI, no control plane, Tailscale-run DERP is rate-limited | limitation+: licence resolved via GitHub API (BSD-3-Clause), first tag v0.1.0 at 2026-08-30 UTC |
| CI2026-099-023 | https://tailscale.com/blog/kubernetes-operator-1102 | yes | yes — Sep 9 | yes — PeerRelay CR, IPv6/4via6 egress, certificate retries | ok |
| CI2026-099-024 | https://tailscale.com/blog/making-tailscale-faster | yes | yes — Sep 22 | yes — buffer memory "expected in v1.104"; multi-queue "planned for a release after v1.104"; netmap caching "expected to arrive by default in v1.104" | limitation+: points to new row 029 (Oct 7 v1.104.1 ships desktop netmap caching). `announced_only` kept because it describes this source as of Sep 22 |
| CI2026-099-025 | https://tailscale.com/blog/meta-muse-ai-agent-tailscale | yes | yes — Sep 30 | yes — Muse joins the tailnet as its own node, outbound-only, first-connection confirmation | ok |
| CI2026-099-026 | https://tailscale.com/blog/codex-cloud-tailscale | yes | yes — Oct 6 | yes — no partnership; reusable+ephemeral tagged key; HTTP/HTTPS + TCP via CONNECT; no MagicDNS/split DNS/UDP/ICMP/inbound/SSH; Codex Cloud "rolling out … over time" | ok |

**Summary:** 26/26 rows reachable; 26/26 displayed dates match `published_utc`; 25/26 claims fully supported and 1 (CI2026-099-005) partly over-broad, handled by a limitation note. **0 status changes, 0 confidence changes, 7 limitation extensions** (004, 005, 009, 012, 017, 022, 024). No row deleted and no `event_id` changed.

Also re-checked: report links <https://tailscale.com/docs/aperture> (HTTP 200), <https://tailscale.com/blog/sovereign-ai-patricia-prewitt> (HTTP 200; `datePublished` 2026-10-13 — correctly **excluded**, outside window) and the `tailscale/tailscale` licence (GitHub API: BSD-3-Clause). No page contained instructions aimed at AI agents.

## 2026-10-16 follow-up — missing in-window events

**Checked (no WebSearch calls used; 0 of the ≤4 allowed):** full in-window section of <https://tailscale.com/changelog>; all 2026 entries of <https://tailscale.com/security-bulletins>; <https://tailscale.com/blog> (index renders 5 posts) and its RSS feed <https://tailscale.com/blog/index.xml> (15 items, Jul 31 → Oct 13); `gh api repos/tailscale/tailscale/releases`. Not executed: any news/independent-press search (budget kept for other agents) — so independent reporting on the events below is **unknown**, not absent.

**Appended rows (3), accessed 2026-10-16:**

| New event_id | Source | Published | Why material | Spot-check |
|---|---|---|---|---|
| CI2026-099-027 | [security bulletins — TS-2026-011](https://tailscale.com/security-bulletins); check: [changelog Aug 19 v1.102.3](https://tailscale.com/changelog) | 2026-08-18 | Security advisory: 4via6 subnet routers allowed ACL-permitted peers to reach host-scoped addresses incl. cloud metadata (instance credentials) and loopback; fixed 1.102.3. Omitted from the original ledger, which listed TS-2026-002 … 010 | Bulletin date Aug 18 and "fixed in 1.102.3 or newer" confirmed; changelog Aug 19 cites TS-2026-011; GitHub release v1.102.3 at 2026-08-20 UTC |
| CI2026-099-028 | [Tailscale PAM beta blog](https://tailscale.com/blog/tailscale-pam-beta); check: [changelog Aug 26](https://tailscale.com/changelog) | 2026-08-27 | New product line (privileged access management, beta) in the window | Blog `datePublished` 2026-08-27T14:00Z; changelog lists "Tailscale PAM … (beta)" on Aug 26 — same two-date pattern as Aperture GA, recorded as one event |
| CI2026-099-029 | [changelog Oct 7 v1.104.1](https://tailscale.com/changelog); check: [GitHub release v1.104.1](https://github.com/tailscale/tailscale/releases/tag/v1.104.1) | 2026-10-07 | Ships part of the Sep 22 performance roadmap (desktop netmap caching, WireGuard buffer memory) — converts part of row 024's "announced" direction into a shipped release; multi-queue not listed | Changelog date and contents confirmed; GitHub release published 2026-10-07T22:09:57Z |

**Seen but not added (judged lower materiality or out of window):** Aug 24 "TailscaleUp 2026" product-preview post (preview of items already recorded); Aug 28 Control D DNS-filtering post and Aug 31 "Build with Tailscale" post (not opened); Jul 29 tailnet creation API (alpha); Jul 6 self-serve IdP change (beta); Jul 23 admin-console URL change; Oct 6 declarative node sharing (alpha); Oct 8 device-posture monitoring (beta); Sep 22 GitHub Action v4.2.0; May 15 Terraform provider v0.29.0 (OIDC). **Excluded as out of window:** TS-2026-012 (Oct 13, libtailscale), Oct 13 sovereign-AI post, Oct 14 IdP-change GA, Apr 8 pricing change.

**Ledger after follow-up:** 29 rows (26 → 29). Segment counts: Apr 12–30: 3; May: 4; Jun: 6; Jul: 6; Aug: 5; Sep: 3; Oct 1–12: 2 (by `published_utc`; before the follow-up Aug was 3 and Oct 1–12 was 1). Counts are a purposive screen, not a census.

## Open gates (unchanged)

Independent human factual/link and security review of version matrices, source-access/rights review, methods review and any real opt-in task comparison remain **pending**. Vendor bulletins state potential impact under stated conditions, not prevalence or exploitation; GitHub release-object timestamps can trail changelog dates and neither is an immutable archive capture.
