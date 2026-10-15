# Docker (037): provisional source-query and inclusion log, 2026-10-16

> **PROVISIONAL, AI-ASSISTED FIRST-PASS SCREEN. NOT HUMAN-REVIEWED.** This log goes with the [report](037-docker.md) and the [event ledger](037-docker.events.csv). Factual/link review, source-access/rights review and methods review are all **pending**. It does not close [issue #104](https://github.com/MSKazemi/github-trending-1000-study/issues/104).

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Sources accessed:** 2026-10-16.

**Tools used:**
- A public web search tool. Result totals are not exposed, so they are **unknown**, not zero.
- Direct fetches of official pages. The fetch tool summarises page bodies. For eight Desktop release items, the exact sentences were re-fetched verbatim as a spot check.
- The GitHub REST API via `gh api`, for repository license, creation date, PR merge date and release timestamps.

Query-run UTC times, complete excluded-hit denominators and archived page hashes were **not captured**. This log is **not exhaustive**.

## Query log by segment

| Segment | Exact query or fetched index | Pages opened and decision |
|---|---|---|
| All months (backbone) | Fetched [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/) (first 100k characters, which cover 4.69.0 on 2026-04-13 through 4.95.0 on 2026-10-12) | **Included:** 4.71.0, 4.80.0, 4.81.0, 4.86.0, 4.93.0 and 4.94.0 as rows. 4.72.0 and 4.74.0 are cited inside other rows. **Seen but not given rows:** the remaining weekly releases (usability, installer, WSL, Kubernetes updates). |
| All months (backbone) | Fetched [Docker Engine 29 release notes](https://docs.docker.com/engine/release-notes/29/) | **Included:** 29.4.2, 29.4.3, 29.7.0 and 29.8.2. **Seen, not given rows:** 29.4.1, 29.5.0–29.5.3 (including the docker cp CVEs in 29.5.1), 29.6.0–29.6.2, 29.7.1/29.7.2, 29.8.0/29.8.1 and 29.9.0. **Excluded:** 29.9.1 (published 2026-10-14, out of window). The notes mention no Engine 30.x. |
| All months (backbone) | Fetched [docker/compose releases](https://github.com/docker/compose/releases) | Compose releases v5.1.2 through v5.6.0 seen. **Included:** only the AI policy (via PR #13550). **Not given rows:** v5.2.0 reconciliation, v5.3.0 init containers, v5.6.0 partial jobs. |
| All months (index) | Fetched [docker.com/blog](https://www.docker.com/blog/) pages 1–9 | Used to enumerate dated posts from Mar 12 to Oct 14. Bodies were read only for the posts cited in the ledger. Posts seen **only as titles** were not counted: Apr 14, Apr 16, Apr 23, May 1, May 7, May 15, Jun 11, Aug 3 audit logs, Aug 20 Verified Publisher self-serve. |
| All months (index) | Fetched [docker.com/company/newsroom](https://www.docker.com/company/newsroom/) (`docker.com/press-room/` returned 404) | **In-window press releases:** only Aug 18 (leadership) and Sep 24 (Cloud Sandboxes). "In the news" listed The Register (Sep 24), Techstrong.ai (Sep 26) and DevOps.com (Sep 28). **No press releases in April through July.** |
| Apr 12–30 | `Docker announces 2026 AI agents sandbox` | Search results were secondary sites (letsdatascience, morphllm, techintelpro, traeai, zeli.app) and were **not used**. They point to a March 2026 local Sandboxes launch, which is pre-window. In-window row: Desktop 4.71.0 (Apr 27). |
| May | `Docker press release May 2026`; `Docker Gordon AI agent generally available May 2026 news`; `"Docker AI Governance" launch devops.com OR theregister OR thenewstack 2026`; `"Docker" "Copy Fail" CVE-2026-31431 containers news May 2026`; `Docker Desktop Model Runner CVE-2026-5843 container escape` | **No May press release.** Opened the Gordon GA, AI Governance and Copy Fail blogs. Opened [heise](https://heise.de/-11308355) and included it as an independent row. **Excluded:** Ubuntu docker.io packaging updates (threatcluster), which are not Docker Inc. events. Excluded the hawkdive, byteiota and casino88 repackaging sites as low quality. Excluded a traeai.com page whose Copy Fail details contradict Docker's own post. CVE aggregators (Wiz, stack.watch, cvefeed) were noted only as the source of the CVSS disagreement. |
| June | Blog index pages 5–6 | Opened the Athena coalition and DCT retirement posts. Desktop 4.80.0 comes from the release notes. **No June press release. No independent coverage found.** |
| July | Blog index page 4; `Docker news April 2026 OR June 2026 OR July 2026 theregister OR thenewstack OR infoworld Docker Hardened Images sandboxes` | Opened the NVIDIA alliance and OIDC posts. The search returned **no Register, New Stack or InfoWorld coverage for April, June or July**. The cybersecuritynews "Aug 25 2026" DHI page seems to restate December 2025 news and was **excluded**. |
| August | Blog index pages 2–3 | Opened the VMM beta post and the leadership press release. Opened [Agentic Platform release notes](https://docs.docker.com/agentic-platform/release-notes/), whose entries run Aug 26–Sep 24 and have no version numbers. **No independent coverage found.** |
| September | `docker.com press release Cloud Sandboxes September 2026`; `Docker Sandboxes generally available sbx CLI 2026` | Opened the press release (fetched as `https://www.docker.com/?p=94083`; the ledger uses the newsroom-listed canonical path), the Cloud Sandboxes blog, the Kit spec/CNCF blog, [The Register](https://www.theregister.com/ai-and-ml/2026/09/24/dockers-new-sandboxes-aim-to-contain-ai-agents-for-real/5298964), [DevOps.com](https://devops.com/docker-introduces-open-sandbox-kit-spec-for-ai-agent-permissions/), the [sandbox-kit-spec repo](https://github.com/docker/sandbox-kit-spec), [compose PR #13550](https://github.com/docker/compose/pull/13550) and the [Sandboxes release notes](https://docs.docker.com/ai/sandboxes/release-notes/) (0.45.0 on Sep 21 to 0.47.0 on Oct 5). A search snippet claiming Docker Sandboxes reached full production on 2026-01-30 came from a third-party blog, was **unconfirmed** and was not used. Techstrong.ai (Sep 26) was listed in the newsroom but **not opened**. |
| Oct 1–12 | `Docker Hub personal access tokens organization conversion vulnerability October 2026` | Opened the Docker Hub advisory and [BleepingComputer](https://www.bleepingcomputer.com/news/security/docker-hub-flaw-let-attackers-impersonate-users-tamper-with-images/). BleepingComputer was published 2026-10-13, **outside the window**, so it is used only as `independent_check_url`. The Hacker News and securityonline results were **not opened**. A search summary gives CVSS v4 9.4 Critical; this was **not verified** against NVD in the first pass. *(2026-10-16 spot-check: NVD lists Docker's CNA CVSS 4.0 score as 9.4 Critical; the record is Awaiting Analysis.)* **Excluded as out of window:** Oct 14 blog posts (Harbor evals, agent security risks). |
| Identity / ownership | `Docker Inc acquisition OR funding OR layoffs 2026` | **No confirmed 2026 acquisition, funding or layoff.** Results were old articles (2017–2019 funding stories, the Mirantis deal) and a third-party valuation estimate (TrueUp), which was not used. A search summary named a CEO and joining year that could not be confirmed and contradicts the researcher's prior knowledge. It was **discarded**. Ownership remains **unverified**. |

## GitHub API checks (2026-10-16)

- `repos/docker/compose/contents/AI_POLICY.md`: the file exists on `main`.
- `repos/docker/compose/commits?path=AI_POLICY.md`: three commits, all dated 2026-09-29T13:46:11Z. The latest is "docs(ai-policy): adopt the centralized moby/.github AI usage policy".
- `repos/docker/compose/pulls/13550`: merged 2026-09-29T13:46:13Z.
- `repos/docker/compose/releases/tags/v5.6.0`: published 2026-10-02T16:07:06Z.
- `repos/docker/sandbox-kit-spec`: created 2026-09-16T16:39:00Z, license `Apache-2.0`.

## Inclusion, exclusion and validity decisions

- **Included: 25 rows**, at least one in each of the seven segments (Apr 1, May 5, Jun 3, Jul 4, Aug 4, Sep 6, Oct 2). This was a purposive selection for agent isolation, supply-chain and credential security, reuse and contributor governance. It is not a Docker release census.
- **Duplicate groups:**
  - `037-copy-fail` (-002, -003).
  - `037-mr-cve-2026-5843` (-001, -006).
  - `037-gordon` (-005, -014).
  - `037-cloud-sandboxes` (-017, -018, -020). These are one launch with **two first-party "release" dates**, Aug 26 "Initial release" and Sep 24 "Experimental public release"/press release. The conflict is left unresolved, not invented away.
- **Independent vs vendor:**
  - heise, The Register and DevOps.com are independent publishers, but each relays vendor or advisory material and none performed independent tests. They are not E3.
  - BleepingComputer falls outside the window.
  - No independent coverage was found for Gordon GA, AI Governance, OIDC, DCT retirement or the VMM beta.
- **Negative evidence retained:**
  - the 29.4.2 hardening regression (-002)
  - the removal of the experimental `docker sandbox` plugin (-009)
  - the ECI enforcement gap (-021)
  - API keys written in clear to logs (-024)
  - the two-year Hub PAT flaw (-025)
- **Access:** public pages only. No account login, paywall, private advisory, exploitation or personal data. Two fetches of the full Desktop release-notes page covered only its first 100k characters, which span the whole window.

**What a reviewer should re-check:**
- Re-run the queries with captured result totals and UTC times.
- Verify CVE IDs and CVSS scores against NVD.
- Read the final `AI_POLICY.md` text.
- Confirm Cloud Sandboxes availability between Aug 26 and Sep 24.
- Resolve corporate ownership from a primary filing or official statement.
