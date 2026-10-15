# Vercel (027) — provisional search and screening log, 2026-10-16

> **PROVISIONAL, AI-assisted, NOT reviewed by a qualified human.** This log accompanies the [report](027-vercel.md) and the [event ledger](027-vercel.events.csv) for issue [#94](https://github.com/MSKazemi/github-trending-1000-study/issues/94). It is a reproducible **lead inventory**, not a systematic review. Factual/link review, source-access/rights review and methods review are pending.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Search and reading date:** 2026-10-16. The UTC run time of each query was not recorded.

**Tools used:**

- a public web-search tool;
- direct page fetches (rendered to text and summarized by the fetch tool);
- authenticated read-only `gh api` calls against public GitHub repositories.

**Not captured:** hit counts for each query, result ranks, screened-URL denominators and byte-hash snapshots of the pages. These are **unknown**, not zero.

**Exclusions:** no paywalled, login-gated or private sources were accessed. No scraping beyond single page reads was done.

## Query and source log

| # | Segment | Exact query or direct source | Pages opened/read | Decision |
|---|---|---|---|---|
| Q01 | all | direct read: `https://vercel.com/changelog` and `/changelog/page/2` | both pages | All 16 visible entries were dated Oct 13–15 (out of window); no row. In-window changelog entries were reached through links instead |
| Q02 | all | direct read: `https://vercel.com/blog` (index) | index; 619 posts reported, text truncated at 2024-08 | Used to enumerate the in-window titles. Each included post was then opened on its own |
| Q03 | Apr | `Vercel security incident April 2026` | [KB bulletin](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident), [CyberInsider](https://cyberinsider.com/vercel-confirms-security-incident-as-hackers-claim-to-sell-internal-access/), [Trunk](https://trunk.io/blog/vercel-april-2026-incident) | Included as **one** incident (CSV 003). Search results from gigazine, bastion.tech and penligent were seen and **not used**: they are secondary or SEO and add claims (sale price, record counts) that cannot be verified |
| Q04 | Apr | `Vercel news 2026 funding IPO valuation agents`; `Vercel $500 million run-rate revenue August 2026` | [TechCrunch 2026-04-13](https://techcrunch.com/2026/04/13/vercel-ceo-guillermo-rauch-signals-ipo-readiness-as-ai-agents-fuel-revenue-surge/) | Included (001). Several results were **excluded**: the "$500M run-rate / Amit Agarwal board" claim, because only a syndicated tag page was seen; the "S-1 filed May 14, 2026" claim, which appeared on one aggregator only and was not confirmed; and investor-marketing pages. The Information piece is paywalled and was not read |
| Q05 | Apr | direct: [Workflows post](https://vercel.com/blog/a-new-programming-model-for-durable-execution) | read | Included (002) |
| Q06 | Apr | blog index | "2026 Vercel AI Accelerator recap" (Apr 28), Zo Computer customer story (Apr 17) | Excluded: a program recap and a customer testimonial |
| Q07 | May | direct: [deepsec](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base), [AI Gateway index](https://vercel.com/blog/ai-gateway-production-index), [token theft](https://vercel.com/blog/protecting-against-token-theft) | read | Included (004, 006, 007) |
| Q08 | May | `Next.js security advisory 2026 CVE vercel/next.js GHSA`; `nextjs.org blog May 2026 security release Next.js 16.2.6`; `gh api repos/vercel/next.js/security-advisories` | [Netlify May 8 changelog](https://www.netlify.com/changelog/2026-05-08-react-nextjs-security-vulnerabilities.md); GitHub advisory list | Included (005). The official nextjs.org May post was **not found** by search. Third-party guides (rabinarayanpatra.com, essamamdani.com) were excluded |
| Q09 | May | blog index | Conductor (May 27), Superset, KIKO, General Intelligence and GitBook stories | Excluded: customer testimonials |
| Q10 | Jun | direct: [Enterprise Apps & Agents](https://vercel.com/blog/vercel-for-enterprise-apps-and-agents), [Connect](https://vercel.com/blog/introducing-vercel-connect), [eve](https://vercel.com/blog/introducing-eve), [AI SDK 7](https://vercel.com/blog/ai-sdk-7), [Services](https://vercel.com/blog/vercel-services-run-full-stack-on-vercel), [Ship 2026 recap](https://vercel.com/blog/vercel-ship-2026-recap) | all read | Included (008–012). The recap is used only as a cross-check. Discrepancy: the recap gives Services as "available July 1" while the Services post says "public beta" |
| Q11 | Jun | `Vercel Ship 2026 announcements TechCrunch OR "The Register" OR "The New Stack" June 2026` | community.vercel.com weekly posts and event listings (results only) | **No independent press coverage found.** The event date is inconsistent across listings (London Jun 17 versus NY Jun 25/30) and is not resolved |
| Q12 | Jun | blog index | Flags (Jun 22), Dockerfile (Jun 30), Hydrogen/Shopify (Jun 30), Agent Stack (Jun 20) | Seen but not ledgered: bounded selection. They remain candidates for a second pass |
| Q13 | Jul | `Vercel acquires Better Auth July 2026` | [Vercel post](https://vercel.com/blog/vercel-acquires-better-auth); [The New Stack](https://thenewstack.io/vercel-acquires-better-auth/) (fetched, but no body or date was readable); Dealroom (search result only) | Included (013). The license was checked through the GitHub API: `better-auth/better-auth` is MIT |
| Q14 | Jul | direct: [Vercel Agent](https://vercel.com/blog/vercel-agent); `gh api` advisories | read | Included (014, 015). DeepsecBench (Jul 27) and the Hydrogen rebuild (Jul 30) were seen on the index and not opened |
| Q15 | Aug | direct: [Next.js 16.3](https://nextjs.org/blog/next-16-3); `gh api repos/vercel/next.js/releases` | read | Included (016). v16.3.0 was published on GitHub on 2026-08-03T21:03Z |
| Q16 | Aug | direct: [v0 API](https://vercel.com/blog/introducing-the-new-v0-api), [Agent Plugins](https://vercel.com/blog/introducing-agent-plugins), [changelog entry](https://vercel.com/changelog/introducing-agent-plugins-1-0-0), [Sandbox challenge](https://vercel.com/blog/one-million-dollar-hacker-challenge-for-vercel-sandbox), [Connect GA](https://vercel.com/blog/the-end-of-credential-sprawl-for-agents), [Run SDK](https://vercel.com/blog/introducing-run) | all read | Included (017–021). `https://vercel.com/changelog/vercel-connect-is-now-generally-available` returned **404**, so the GA date was taken from the blog |
| Q17 | Aug | `"Agent Plugins" specification Vercel OpenAI Cursor GitHub August 2026 news` | search results only (createwith, developersdigest, blakecrosley, upstash) | Used only for the limitation note that v1 has no signing or provenance layer (a third-party analysis that was not fetched). The spec license was read from the repository's LICENSE.md |
| Q18 | Aug | direct: `https://nextjs.org/blog/august-2026-security-release` | **HTTP 504, inaccessible** | Replaced by the GitHub advisory GHSA-2xp9-vwfh-vxw4 plus the [Netlify Aug 25 changelog](https://www.netlify.com/changelog/2026-08-25-nextjs-security-vulnerabilities.md) (022) |
| Q19 | Sep | direct: [libheif write-up](https://vercel.com/blog/reproducing-disclosing-and-fixing-the-libheif-vulnerability-with-hacktron-and-the-maintainers), [bug bounty](https://vercel.com/blog/the-vercel-bug-bounty-program-is-now-publicly-available), [State of agent skills](https://vercel.com/blog/state-of-agent-skills), [Flat Rate CDN](https://vercel.com/blog/introducing-flat-rate-cdn), [Sandbox Secure Compute changelog](https://vercel.com/changelog/vercel-sandbox-now-supports-secure-compute); `gh api repos/strukturag/libheif/security-advisories/GHSA-g89c-p67h-r497` | all read | Included (023–025). Flat Rate CDN (pricing only) and Secure Compute (an Enterprise network feature) are **not ledgered**. The Sep 22 (1) and Sep 30 (7) Next.js advisories were seen through the API and are mentioned in the report but **not ledgered** |
| Q20 | Oct 1–12 | `site:community.vercel.com "Vercel weekly" October 2026`; direct: [weekly Oct 5](https://community.vercel.com/t/vercel-weekly-october-5-2026/50269), [Next.js 16.4](https://nextjs.org/blog/next-16-4), [Rogo story](https://vercel.com/blog/how-rogo-ships-agent-written-code-to-production-in-5-minutes-on-vercel); `Vercel changelog October 2026 "now available" ...` | read | Included: Next.js 16.4 (026), whose GitHub release v16.4.0 is dated 2026-10-07T10:03Z. Excluded: the Rogo (Oct 2) and Rillet (Oct 9) customer stories, which are vendor-authored testimonials. The weekly items carry no individual dates |
| Q21 | out of window | blog and changelog index | [Sandbox challenge findings, 2026-10-14](https://vercel.com/blog/findings-from-the-1-million-dollar-vercel-sandbox-challenge); Oct 15 posts (Drives, Python GA, Vercel for Enterprise); Next.js advisories of Oct 14 | **Excluded: published after Oct 12.** The Oct 14 findings are cited only as a limitation on 019 |
| Q22 | identity/licensing | `gh api repos/{vercel/eve, vercel-labs/deepsec, vercel-labs/run, agentplugins/agent-plugins-spec, better-auth/better-auth, vercel/workflow, vercel/ai, vercel/next.js}`; LICENSE files read for `vercel/ai`, `vercel-labs/run` and the agent-plugins spec | API metadata | eve, deepsec and workflow are Apache-2.0. ai and run report NOASSERTION in the API, but their LICENSE files read as Apache-2.0. The agent-plugins spec is CC-BY-4.0 (text) plus Apache-2.0 (code). better-auth is MIT and next.js is MIT. **Corporate ownership was not verified at filing level** |

## Months with no findings

**None.** Every segment has at least one ledger row:

| Segment | Ledger rows |
|---|---|
| Apr 12–30 | 001–003 |
| May | 004–007 |
| Jun | 008–012 |
| Jul | 013–015 |
| Aug | 016–022 |
| Sep | 023–025 |
| Oct 1–12 | 026 |

October 1–12 is thin: one ledgered release. This reflects selection effort, not company inactivity.

## Inclusion and validity decisions

- **26 ledger rows.** Several rows cite a GitHub advisory index or a single advisory that represents a **batch**. Rows are not independent confirmations of company success.
- **Deduplication:** the April incident is one row (003). CyberInsider and Trunk are recorded as independent checks, not as extra events. Rows 022 (Next.js AVIF RCE) and 023 (libheif write-up) share the duplicate group `027-libheif-avif-rce`, because they describe one vulnerability chain. Connect beta (009) and Connect GA (020) are distinct availability events.
- **Primary versus independent:** most rows are E1 vendor statements. The E2 rows add a readable public artifact (repository/license, GitHub release or advisory) or a second-entity document (TechCrunch, CyberInsider, Netlify, the libheif advisory). A second Vercel-hosted page is documentary corroboration only. **No E3 evidence was found.**
- **Fetch-tool caveat:** page contents were read through an automated text extraction and summarization step. Figures quoted in the ledger (pricing, counts, percentages) should be spot-checked against the live pages by a human reviewer before any reuse. This applies above all to the Connect pricing discrepancy between the June 17 and August 25 pages.
- **Re-run guidance:** a future reviewer should re-run Q01–Q22 with recorded UTC timestamps and hit counts, archive the pages, page deeper through `vercel.com/changelog`, and look for neutral coverage (Reuters, The Register, InfoQ) of eve, AI SDK 7, Agent Plugins and the April incident.
