# Redis — provisional six-month technology intelligence screen (074)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](074-redis.events.csv) and [search log](074-redis.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 074
- **Research issue:** [#142](https://github.com/MSKazemi/github-trending-1000-study/issues/142); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Redis Ltd./Redis Inc. ("Redis"), formerly Redis Labs, privately held and venture-funded; founded in Israel in 2011, CEO Rowan Trollope since 2023 (per [Globes](https://en.globes.co.il/en/article-1001549107) and [Calcalist](https://calcalistech.com/ctechnews/article/cyzy6sb6u), 2026-07-13). No acquisition of Redis was found. Redis acquired Featureform (stated as "last October" in the [2026-04-20 post](https://redis.io/blog/introducing-redis-feature-form/)) and Decodable (newsroom, September 2025; pre-window baseline). Filing-level corporate verification was **not** performed and no regulatory filing source was contacted.
- **Product URL and company newsroom:** [redis.io](https://redis.io/), [blog](https://redis.io/blog/) ([RSS](https://redis.io/blog/feed/), covers only 2026-07-11 onward), [newsroom](https://redis.io/company/news/), [redis/redis releases](https://github.com/redis/redis/releases), [security advisories](https://github.com/redis/redis/security/advisories), [redis-py](https://github.com/redis/redis-py), [PyPI `redisvl`](https://pypi.org/project/redisvl/).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 35 ledger rows across all seven calendar segments.
- **Source coverage:** redis/redis GitHub releases, PRs and security advisories via `gh api`; redis.io blog via RSS, blog sitemaps (1,123 URLs; 373 with lastmod ≥ 2026-04-10 triaged) and raw HTML of 44 posts; PyPI JSON (redis, redisvl, agent-memory-server, langgraph-checkpoint-redis, fastapi-redis-sdk); NVD CVE API; Hacker News Algolia API per month; independent reporting (Globes, Calcalist, Shopify Engineering, charlesleifer.com) and one web search. Times of Israel returned HTTP 403. The X/Twitter post about Kimi K3 was not read. See the [search log](074-redis.search-log.md).

## 1. Search and inclusion audit

Summary only; exact requests, opened URLs and exclusions are in the [search log](074-redis.search-log.md). Search-engine result totals were not exposed and are **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | GitHub API | redis/redis releases 2026-04-12..10-12; security advisories; PRs #15162/#15191/#15722 | 36 releases | 36 | 9 rows | patch-only repeats folded into security rows | API text only; binaries not built |
| 2026-10-16 | redis.io RSS + sitemaps + raw HTML | blog 2026-04-12..10-12 | 373 sitemap URLs triaged; ~50 feed items | 44 opened | 19 rows | SEO explainers ("Tech DE"), case studies, re-dated old posts | RSS only from Jul 11; sitemap lastmod is not a publication date |
| 2026-10-16 | PyPI / GitHub repos | redis, redisvl, agent-memory-server, fastapi-redis-sdk, adk-redis | 5 packages | 5 | 3 rows (+checks) | routine redisvl/langgraph releases | — |
| 2026-10-16 | HN Algolia + 1 web search | `Redis` stories per month; `Redis layoffs 200 employees July 2026 Israel` | 136 HN hits; 9 web results | ~20 | 4 rows | competitors, clones, Show HN projects | HN is a lead source, not coverage of record |
| 2026-10-16 | NVD API | CVE-2026-81934, -23479, -62356 | 2 records, 1 missing | 3 | used as checks | — | NVD status "Awaiting Analysis" for 81934 |

## 2. Verified company/product identity and baseline

Redis develops **Redis Open Source** (server; GitHub repo licence field `NOASSERTION`; the `LICENSE.txt` history shows the 2024-03-20 change from BSD-3 to RSALv2+SSPLv1 and the 2025-05-01 addition of **AGPLv3** as an option, corrected 2025-05-06; **no licence commit in the window**), proprietary **Redis Cloud** and **Redis Software**, and AI-oriented components: RedisVL (MIT), LangCache, Redis Agent Memory, Redis Data Integration (RDI), and since May 2026 the **Redis Iris** context-engine bundle. Client libraries (redis-py MIT, node-redis, go-redis) are separate repositories.

Pre-window baseline (context only, not counted): Redis 8.6.0 (2026-02-10), agent skill for writing Redis code (blog 2026-02-03), LangCache public preview (2025-09-04), Decodable acquisition (2025-09-05). The 8.2 line is described in-window as eligible for up to five years of extended support ([2026-10-08](https://redis.io/blog/redis-oss-is-now-available-on-aws-marketplace/)).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | 8.8-M02 milestone with GCRA rate limiter (Apr 16); Feature Form (Apr 20); adk-redis for Google ADK (Apr 21); OpenTelemetry client metrics (Apr 24) | [8.8-M02](https://github.com/redis/redis/releases/tag/8.8-m02), [blog](https://redis.io/blog/introducing-redis-feature-form/) | none read (TechTarget cited by Redis, not read) | 8.8-M03 (Apr 28) folded; Google Cloud Ready post is dated 2026-04-16 but metadata 2026-03-26, excluded as partner certification |
| 2026-05 | antirez on AI-assisted Array development (May 4); five CVEs fixed (May 5); GCRA held out of 8.8 (May 14); Redis Iris preview (May 18); 8.8.0 GA (May 25); redis-py 8.0.0 (May 28) | [advisory](https://redis.io/blog/security-advisory-cve202623479-cve202625243-cve-2026-25588-cve202625589-cve-2026-23631/), [Iris](https://redis.io/blog/context-is-all-you-need/), [8.8.0](https://github.com/redis/redis/releases/tag/8.8.0) | [charlesleifer.com critique](https://charlesleifer.com/blog/redis-and-the-cost-of-ambition/); [Shopify moved reservations to MySQL](https://shopify.engineering/scaling-inventory-reservations) | Dynamic endpoints post (May 12) metadata is March; not ledgered |
| 2026-06 | 8.8 announcement and perf claims (Jun 2); RDI GA in Redis Cloud on AWS (Jun 8); RedisVL MCP (Jun 11) | [8.8 blog](https://redis.io/blog/announcing-redis-8-8/), [RDI](https://redis.io/blog/redis-data-integration-in-redis-cloud-is-now-ga-in-aws/), [RedisVL MCP](https://redis.io/blog/connect-your-redis-index-to-ai-agents-with-redisvl-mcp/) | HN discussion of the 8.8 blog (Jun 3, lead only) | Iris FAQ (Jun 17) not ledgered; 8.6.4 bug-fix release (Jun 4) not ledgered |
| 2026-07 | agent-memory-server moved into `V0/` behind managed product (Jul 9); layoffs reported (Jul 13) and announced, ~200 roles (Jul 15); Kimi K3 exploit claims (Jul 22–23); security releases across 7 branches (Jul 23); Redis response (Jul 27); 8.10.0 GA (Jul 29) | [PR #319](https://github.com/redis/agent-memory-server/pull/319), [CEO post](https://redis.io/blog/ceo-rowan-trollopes-organizational-announcement-to-redis-employees/), [response](https://redis.io/blog/security-update-redis-response-to-the-kimi-k3-vulnerability-claims/) | [Globes](https://en.globes.co.il/en/article-1001549107), [Calcalist](https://calcalistech.com/ctechnews/article/cyzy6sb6u); [PoC repo](https://github.com/berabuddies/redis-poc) | Times of Israel 403; X post unread |
| 2026-08 | Agent Memory on Snowflake Marketplace (Aug 6); security releases 8.10.1…6.2.24 (Aug 17); CVE-2026-81934 advisory and severity dispute (Aug 28) | [Snowflake post](https://redis.io/blog/how-redis-brings-persistent-memory-to-snowflake-cortex-agents/), [8.10.1](https://github.com/redis/redis/releases/tag/8.10.1), [advisory](https://redis.io/blog/security-advisory-cve-2026-81934/) | NVD record | HIMPORT tutorial (Aug 24) and ~15 SEO explainers excluded |
| 2026-09 | ChatGPT Work/Codex plugin (Sep 11); 8.10 announcement (Sep 14); Agent Memory LongMemEval harness (Sep 15); security releases incl. cluster-bus protected mode (Sep 17); Radar/RDI/Smooth Scaling/Search on Flex/Datadog (Sep 22); official FastAPI SDK (Sep 24); AWS SCA (Sep 29) | [plugin](https://redis.io/blog/put-redis-data-and-engineering-guidance-to-work-in-chatgpt-work/), [8.10.2](https://github.com/redis/redis/releases/tag/8.10.2), [launch](https://redis.io/blog/redis-introduces-new-capabilities-0926/) | none read beyond HN leads | Azure migration and Python HA posts (Sep 23) and all-RAM post (Sep 30) excluded as marketing/tutorial |
| 2026-10-01..12 | Official Redis Open Source AMI on AWS Marketplace (Oct 8); Redis Docs MCP (Oct 9) | [AMI](https://redis.io/blog/redis-oss-is-now-available-on-aws-marketplace/), [Docs MCP](https://redis.io/blog/how-we-built-the-redis-docs-mcp-for-agents/) | none | Post-window posts not screened |

## 4. Dated event evidence and capabilities

Full detail is in the [CSV](074-redis.events.csv) (35 rows, `CI2026-074-001`…`035`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-074-005 | 2026-05-04 | Redis creator reports Array type designed and implemented with heavy AI assistance plus line-by-line human review | narrative; PR #15162 merged 2026-05-13 | [antirez.com](https://antirez.com/news/164) (staff blog) | [PR](https://github.com/redis/redis/pull/15162) | E1 |
| CI2026-074-009 | 2026-05-14 | GCRA rate limiter shipped in milestones then compiled out before 8.8 GA | reversed; future undecided | [PR #15191](https://github.com/redis/redis/pull/15191) | [8.8-RC1 notes](https://github.com/redis/redis/releases/tag/8.8-rc1) | E2 |
| CI2026-074-010 | 2026-05-18 | Redis Iris: Context Retriever (auto-generated MCP tools) and Agent Memory in preview | preview; "43%" adoption claim unaudited | [blog](https://redis.io/blog/context-is-all-you-need/) | none | E1 |
| CI2026-074-012 | 2026-05-28 | redis-py 8.0.0: RESP3 default, breaking type hints, new timeouts/retries | PyPI 2026-05-28T12:45Z | [release](https://github.com/redis/redis-py/releases/tag/v8.0.0) | PyPI | E2 |
| CI2026-074-016 | 2026-07-09 | Open-source agent-memory-server moved to `V0/`; root points to managed Agent Memory | Apache-2.0 kept per PR text | [PR #319](https://github.com/redis/agent-memory-server/pull/319) | PyPI: no in-window release | E2 |
| CI2026-074-017/018/019 | 2026-07-13 / 07-13 / 07-15 | ~200 roles cut globally; Israel figures 80 (Globes) vs ~70 (Calcalist) | company post vs anonymous-source reports | [CEO post](https://redis.io/blog/ceo-rowan-trollopes-organizational-announcement-to-redis-employees/) | Globes, Calcalist | E1 |
| CI2026-074-020/021/022 | 2026-07-22 / 07-23 / 07-27 | Public RCE PoCs (claimed found with Kimi K3); fixes in 7 branches; Redis says the 3 documented issues were duplicates of bug-bounty reports | post-authentication; TopK fix later | [PoC repo](https://github.com/berabuddies/redis-poc), [8.8.1](https://github.com/redis/redis/releases/tag/8.8.1), [response](https://redis.io/blog/security-update-redis-response-to-the-kimi-k3-vulnerability-claims/) | cross-entity | E2 (documentary), not E3 |
| CI2026-074-026 | 2026-08-28 | CVE-2026-81934: initial 9.8 vs Redis 7.5 (v4) | NVD now 7.5/7.1 but description still says unauthenticated | [advisory](https://redis.io/blog/security-advisory-cve-2026-81934/) | [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-81934) | E2 |
| CI2026-074-035 | 2026-10-09 | Public Docs MCP at redis.io/mcp; 135 of 374 commits had an agent as author | self-report | [blog](https://redis.io/blog/how-we-built-the-redis-docs-mcp-for-agents/) | none | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Core server (Redis Open Source) | 8.8: Array type, INCREX, XNACK, subkey notifications; 8.10: compact hashes, HIMPORT, BACKUP, TLS peer-cert server auth, JSONPath extensions | shipped (GitHub GA) |
| Withdrawn features | GCRA rate limiter (milestones only) | reversed |
| Security | five CVEs (May 5; three also as GitHub advisories), further fixes listed in the Jul/Aug/Sep releases, opt-in `cluster-bus-port-protected-mode` (default `no`) | shipped |
| Agent tooling | Iris (Context Retriever, Agent Memory preview), RedisVL MCP, Docs MCP, agent-skills plugin for ChatGPT Work/Codex, adk-redis, Agent Memory on Snowflake | preview / shipped (vendor) |
| Clients/SDKs | redis-py 8.0.0 (breaking), OTel client metrics, official fastapi-redis-sdk (MIT, pre-1.0) | shipped |
| Managed/proprietary | Feature Form, RDI GA on AWS, Radar GA, Search on Flex preview, Smooth Scaling, Datadog private preview | mixed |
| Licensing | No change to the server tri-licence in window; agent-memory-server Apache-2.0 kept but repositioned behind managed product; GitHub API licence fields show `NOASSERTION` for both repos | observed |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "We're investing in multiple lanes at once: real-time context for agents, token and latency optimization, high-performance search, and now a more complete feature platform" | [2026-04-20](https://redis.io/blog/introducing-redis-feature-form/) | none | uncommitted | No dated deliverables |
| R&D re-engineered so AI is used in how software is "designed, written, tested, shipped"; smaller Product/Engineering teams | [2026-07-15](https://redis.io/blog/ceo-rowan-trollopes-organizational-announcement-to-redis-employees/) | ongoing | stated, in progress | Coincides with ~200 role cuts; no productivity data |
| Open-source TopK fix "will be published soon" | [2026-07-27](https://redis.io/blog/security-update-redis-response-to-the-kimi-k3-vulnerability-claims/) | soon | possibly delivered in 8.10.1 (Aug 17) — link unconfirmed | Release notes do not cite the response |
| Search on Flex: "Full parity with in-memory Search is the goal for GA" | [2026-09-22](https://redis.io/blog/search-on-flex-comes-to-redis-cloud-pro/) | none | planned | Preview limitations apply |
| Expanded AWS collaboration on Bedrock reference architectures, migration and Marketplace | [2026-09-29](https://redis.io/blog/redis-expands-strategic-collaboration-agreement-with-aws-to-accelerate-real-rime-and-ai-applications/) | none | announced only | No AWS-side statement read |
| GCRA: "still no decision is made on whether it will be kept or not in the future" | [PR #15191, 2026-05-14](https://github.com/redis/redis/pull/15191) | none | tentative | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Agent-facing "context/memory" functions will move from open-source reference code to managed, proprietary services, with OSS kept as reference | agent-memory-server moved to `V0/` behind managed Agent Memory; Iris components are Cloud previews; no in-window OSS memory-server release | Normal productization; the OSS repo may keep receiving releases | New OSS agent-memory-server releases and feature parity with the managed service through 2027 | moderate for direction; unknown for durability |
| H2: AI-assisted vulnerability discovery will raise the rate of public, post-authentication memory-safety findings in mature C servers, increasing patch-release frequency | 4 multi-branch security release dates in window; Kimi K3 PoC claims; CVSS dispute | Bug bounty and fuzzing improvements could explain the rate without AI; claims of AI discovery are unverified | Patch cadence returns to pre-2025 levels; no further AI-attributed findings | low; n is small and attribution unknown |
| H3: Vendors will ship machine-readable "agent surfaces" (MCP servers, skills plugins, llms.txt) as a discovery channel | Docs MCP, RedisVL MCP, ChatGPT/Codex plugin, Context Retriever MCP tools | Marketing cycle; agents may keep relying on web search and pretraining | Controlled tasks show no accepted-task gain vs docs-only | low; untested |
| H4: Client-library churn (RESP3 defaults, breaking typing) will impose migration cost on downstream reusers | redis-py 8.0.0 breaking changes; 8.8 Array GA vs client "preview" mismatch | Changes may be cheap; agents may absorb migration | Measured migration time for pinned apps ~0 | moderate that churn exists; cost unknown |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Core-maintainer and docs-team self-reports of heavy agent use (Array; 135/374 agent-authored commits); Cursor Bugbot reviews in redis/redis PRs | Count agent-authored commits/reviews in consented repos over time | Disclosure practices, not practice, changed | Only explicit metadata; never infer authorship from style |
| M2 accepted task quality | Agent-assisted code coexists with frequent memory-safety fixes | Compare defect/fix rates before and after declared agent use, with matched C projects | No association, or confounding by more fuzzing | Public fix records; no attribution to individuals |
| M3 discoverability | Vendor MCP/skills channels for coding agents | Agent task with and without Docs MCP access | Agents ignore the channel | Accepted tasks only |
| M4 verified reuse | Integrations (ADK, FastAPI, Snowflake) are vendor-announced | Trace consented downstream repos that import and run them | Announcement without use | Pinned commits, executed tests |
| M5 rights/security/provenance | Tri-licence unchanged; NOASSERTION licence fields; unauthenticated-by-default cluster bus remains opt-in | Licence + secure-default checklist before reuse | Licence text adequate despite API field | LICENSE files at pinned commits |
| M6 review/maintenance/lifecycle | 4 security-release waves across up to 8 branches; client breaking changes | Measure upgrade minutes per release for a pinned app | Upgrades trivial | No energy or CO2e inferred |
| M7 actionable interventions | Default-deny exposure and pinned, patched versions | See §8 | Guardrails add friction without benefit | Synthetic tasks until approval |

Company adoption claims (e.g., "43% of enterprise AI agent stacks", "$300M" run rate reported by Calcalist) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** a generic pilot on one of the maintainer's own Python services that already uses (or is evaluating) a cache/state store; if none uses Redis, the pilot runs on a throwaway synthetic service in a local container. The study's disabled Trending `capture` command stays disabled; nothing here involves network collection.

**Candidate practice (not yet validated):** reuse-first state layer — use an existing, maintained component (Redis Open Source 8.x image pinned by digest via the stock `redis-py` client, or the already-present SQLite/Postgres) instead of writing custom caching/agent-memory code, and adopt a "secure-default and pinned-patch" checklist: auth required, bound to localhost/private network, `protected-mode` on, image pinned and upgraded on each security release.

**Treatment/control and frozen comparable task:** Freeze 8 small synthetic tasks (e.g., add a TTL cache to an endpoint, add a rate limit, persist a session) with **hidden acceptance tests written by someone other than the implementer** and kept out of any assistant's context. Arm A: implement with the existing relational store only. Arm B: implement with pinned Redis + `redis-py` (record exact server and client versions). Same implementer, time budget and task order randomized per task. Accepted-task unit: one change passing hidden tests and accepted by a reviewer without rework.

**Success and guardrails:** Primary: accepted tasks / 8 assigned (failed, abandoned, timed-out included). Guardrails: no instance reachable without authentication (checked by a local connection attempt without credentials, which must fail); no new dependency beyond the one pinned client; full test suite green; licence of every added component recorded at a pinned version (AGPLv3/RSAL/SSPL implications reviewed by a human before any distribution). Measured human work: setup minutes, per-task review minutes, minutes spent on the next upgrade (one security release). No paid API or managed service is used; no energy or carbon estimate unless metered. Commits are authored by the maintainer only.

**Stop/reversal rule:** Keep Arm A if Arm B does not raise the accepted-task rate, adds more than 10 setup/review minutes per task on average, or the upgrade to the next security release takes more than 30 minutes. Stop immediately if any unauthenticated connection succeeds. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** Redis 8.8.0 (2026-05-25) and 8.10.0 (2026-07-29) GA on GitHub; GCRA withdrawn before 8.8 GA; security releases on 2026-05-05, 07-23, 08-17 and 09-17 (GitHub API timestamps); redis-py 8.0.0 (PyPI 2026-05-28T12:45Z); fastapi-redis-sdk 0.7.0–0.8.1 on PyPI (MIT); agent-memory-server repositioning (PR merged 2026-07-09); no server licence change in window.
- **Claims/announcements only:** Iris adoption figure (43%), token savings (up to 90%), 8.8/8.10 performance numbers, Feature Form GA, RDI GA, Radar GA, Snowflake no-egress claim, Docs MCP commit share and retrieval metrics, AWS SCA scope, 8.2 extended support "up to five years".
- **Conjectures and unknowns:** H1–H4 in §6; real task outcomes, whether AI tools found the July bugs, the exact redisvl version that first shipped MCP.
- **Important contradictory or null evidence:** (a) Israel layoffs 80 (Globes) vs ~70 (Calcalist) vs company total ~200 without a regional figure; (b) CVE-2026-81934 initial 9.8 vs Redis 7.5, and NVD's description ("remote, unauthenticated") vs Redis ("authenticated"); (c) CVE-2026-23479 GitHub CNA 7.7 (v4) vs NVD 8.8 (v3.1); (d) CVE-2026-62356 named in 8.10.1 notes but absent from NVD on 2026-10-16; (e) Kimi K3 PoC "patch bypass" framing vs Redis "duplicates of known findings"; (f) blog dates lag GitHub GA (8.8: Jun 2 vs May 25; 8.10: Sep 14 vs Jul 29); (g) Array called GA in 8.8 notes but "preview" in redis-py 8.0.0; (h) OpenTelemetry "metrics" (Apr 24 post) vs "tracing" (May 8 recap); (i) Shopify's migration away from Redis and a critical independent essay.
- **#56 candidates (not minted):** Globes 2026-07-13; Calcalist 2026-07-13; Shopify Engineering 2026-05-12; charlesleifer.com 2026-05-12. Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
