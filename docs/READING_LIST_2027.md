# Source-based reading list for a 2027-relevant GitHub/coding-agent study

**Compiled and linked:** 2026-10-11. **Status:** source discovery and verification pass; **NOT** a formal systematic review or meta-analysis. The tabular [machine-readable source register](../references/study_sources_2026.json) has identifiers and caveats; see [selection](SELECTION_PROTOCOL_2027.md), [agent detection](AGENT_ADOPTION_MEASUREMENT.md), and [metric definitions](METRIC_REGISTER_2027.md).

**Evidence rule:** primary peer-reviewed/working papers first; surveys and product providers second (with denominators); news is for discovery, chronology and counterpoints, never a second independent sample of a research paper.

## Peer-reviewed scientific papers

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| P01, 2014 | [The Promises and Perils of Mining GitHub](https://doi.org/10.1145/2597073.2597074) — Kalliamvakou et al. | Selection validity, GitHub mining pitfalls | Historical study; not about agents |
| P02, 2021 | [The SPACE of Developer Productivity](https://doi.org/10.1145/3454122.3454124) — Forsgren, Storey et al. | Multidimensional developer productivity metrics | Framework; not proof of causal outcomes |
| P03, 2026-06-26 | [Agentic Much? Adoption of Coding Agents on GitHub](https://doi.org/10.1145/3822180) — Robbes et al. | 128,018 project study; 22.20–28.66% detected adoption as of Feb 21 2026 | Method dependent; silent use missed; sample-specific |
| P06, 2026-10 | [Does Working with AI Agents Change How Developers Code, Test, and Review?](https://doi.org/10.4230/LIPIcs.ESEM.2026.67) — ESEM 2026 authors | Longitudinal agent influence: DiD 669 treated developers, 228 controls | Observational; temporal shocks and exposure measurement |
| P07, 2026-04 | [More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment towards AI-generated Pull Requests](https://doi.org/10.1145/3793302.3793622) — Huang et al. | Code reuse, redundancy, reviewer response to agent PRs | MSR mining challenge sample; limited generalization |

## Working papers (check version carefully)

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| P10, 2026-08 | [Artificial Intelligence in the Firm: Bottlenecks in Software Production](https://fion.ac/) — Fiona Chen, James Stratton | Study using proprietary engineering events and staggered DiD; downstream review bottleneck | Author homepage describes newer 718-firm version; linked PDF at inspection was Jan 2026 preliminary 500-firm edition: version discrepancy MUST be reconciled before quoting statistics |

## Preprints (not automatically peer reviewed)

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| P04, 2026-02-09 | [AIDev: Studying AI Coding Agents on GitHub](https://arxiv.org/abs/2602.09185) — Li, Zhang, Hassan | Agentic PR dataset methodology | PR-only detection incomplete; acceptance not value |
| P05, 2026-06-23 | [Detecting AI Coding Agents in Open Source: A Validated Multi-Method Census of 180 Million Repositories](https://arxiv.org/abs/2606.24429) — Khosravani, Mockus | Multiple-source agent trace detection, precision audits | Preprint; detection coverage and false negatives |
| P08, 2025-07 | [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) — Becker et al. (METR) | RCT 16 developers 246 tasks; on studied tasks AI 19% slower | Early 2025 tools and mature project tasks only |
| P11, 2026-07 | [Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout](https://arxiv.org/abs/2607.01418) — Murphy-Hill, Butler, Savelieva | Enterprise adoption and PR throughput; peer-network diffusion | Merged PR proxy != user value; enterprise-specific |
| P12, 2026-05 | [Coding Beyond Your Training: Claude Code and the Technological Frontier of Software Developers](https://arxiv.org/abs/2605.25438) — Quispe | Staggered adoption, language diversity outcomes | Confounding; commit volume not functionality |
| P13, 2026-06 | [The Shift to Agentic AI: Evidence from Codex](https://arxiv.org/abs/2606.26959) — Johnston et al. | Vendor-linked usage statistics and tasks, parallel-agent use | Provider sample; selected into product; tokens not value |
| P14, 2026-06 | [Agentic Very Much! Adoption of Coding Agent in New GitHub Projects](https://arxiv.org/abs/2606.07448) — Robbes et al. | Agent adoption in new projects; contrast established | New-project sampling; trace methodology |

## Empirical research updates

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| P09, 2026-02-24 | [We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/) — METR | Later experiment selection and time-tracking problems | No reliable current universal speedup estimate |

## Reviews (screen rigor and scope)

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| P15, 2026 | [Vibe Coding in Software Development: A Multivocal Literature Review](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7194448) — Siddeeq et al. | Grey vs peer research synthesis and evidence limits | Review quality and version need independent check |

## Developer surveys

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M01, 2026-10-06 | [Stack Overflow Developer Survey 2026: coding-agent and assistant use](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) — Stack Overflow | n=12,255 question respondents: Claude Code 65.5%, GitHub Copilot 58.7%, Codex 29.5%, Cursor 25.5% | Multiple-response question; opt-in nonrepresentative sample; not all developers |

## Survey methodology

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M02, 2026-10 | [Stack Overflow Developer Survey 2026: methodology](https://survey.stackoverflow.co/2026/methodology) — Stack Overflow | n=30,903 valid survey overall, fielded Jun 23-Aug 5 | Community opt-in channels and non-probability recruitment |

## Platform studies and descriptive reports

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M03, 2025-10-28 | [Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) — GitHub | GitHub repository, contributor, PR and AI-related activity trends | GitHub-defined populations; activity is not usefulness |

## Official developer-agent launch milestones

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M04, 2025-02-24 | [Claude 3.7 Sonnet and Claude Code](https://www.anthropic.com/news/claude-3-7-sonnet) — Anthropic | Claude Code limited preview start | Not repository agent adoption |
| M05, 2025-05-16 | [Introducing Codex](https://openai.com/index/introducing-codex/) — OpenAI | Cloud preview May 16; references Codex CLI in April | Availability not uptake |
| M06, 2025-05-19 | [GitHub Copilot coding agent in public preview](https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/) — GitHub | Delegated issue/PR agent launch | Preview phased availability |
| M07, 2025-10-06 | [Codex is now generally available](https://openai.com/index/codex-now-generally-available/) — OpenAI | Codex GA and broadened SDK/admin integrations | Product release alone not adoption |
| M08, 2026-02-02 | [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/) — OpenAI | New desktop agent orchestration interface | Not launch of Codex itself |

## Provider-reported active user counts

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M09, 2026-03-19 | [OpenAI to acquire Astral](https://openai.com/index/openai-to-acquire-astral/) — OpenAI | Codex >2m weekly active users reported | Includes any Codex user, not only OSS developers |
| M10, 2026-06-02 | [Codex is becoming a productivity tool for everyone](https://openai.com/index/codex-for-knowledge-work/) — OpenAI | Codex >5m weekly active users, ~20% knowledge workers | Vendor defined WAU, not total Github people or repo adoption |
| M11, 2026 | [Anthropic raises $30B Series G](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) — Anthropic | Claude Code weekly active user count doubled vs Jan 2026 | No absolute Claude Code active user count in announcement |

## Official platform sampling and measurement constraints

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M12, 2026-07-17 | [Repository-level GitHub Copilot usage metrics generally available](https://github.blog/changelog/2026-07-17-repository-level-github-copilot-usage-metrics-generally-available/) — GitHub | Authorized org/enterprise daily repo agent PR metrics | Not public metadata for arbitrary repositories |
| M13, 2026 | [GitHub REST search limits](https://docs.github.com/en/rest/search/search) — GitHub Docs | Search caps and relevance ranking; sampling limitations | No guarantee of uniform public repo sample |

## Historical data infrastructure

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| M14, 2011+ | [GH Archive hourly public event archive](https://www.gharchive.org/) — GH Archive | Historical public events and partial time-series frame | Not archive of Trending page rankings; incomplete events/history possible |

## Technology news and independent reporting

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| N01, 2025-05-20 | [OpenAI’s Codex is part of a new cohort of agentic coding tools](https://techcrunch.com/2025/05/20/openais-codex-is-part-of-a-new-cohort-of-agentic-coding-tools/) — TechCrunch | Contemporaneous trend and agent/assistant distinction | News analysis, not controlled scientific evidence |
| N02, 2026-06-02 | [Exclusive: Office workers drive OpenAI's Codex growth](https://www.axios.com/2026/06/02/openai-codex-knowledge-workers) — Axios | Independent reporting of vendor adoption claims | Usage figures originate with OpenAI |
| N03, 2026-02-03 | [GitHub ponders kill switch for pull requests to stop AI slop](https://www.theregister.com/software/2026/02/03/github-ponders-kill-switch-for-pull-requests-to-stop-ai-slop/) — The Register | Maintainer overload and GitHub response | Anecdotes and platform commentary; not prevalence study |
| N04, 2026-10-09 | [AI coding agents generate more code, but not more software](https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/) — Ars Technica | News synthesis of Chen/Stratton; +30% code/longer review | Not separate empirical dataset; check primary working-paper version |
| N05, 2026-08-24 | [OpenAI is building AI agents for everything. Will everyone use them?](https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/) — TechCrunch | Market/agent workflows and distribution differences | Interviews and journalism, not randomized comparison |

## Practical platform review guidance

| ID / date | Source | Why it matters | Interpretation limit |
|---|---|---|---|
| N06, 2026-05-07 | [Agent pull requests are everywhere. Here's how to review them.](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/) — GitHub Blog | Review burden and code reuse risk | Platform authored guidance, not an independent experiment |

## Structured literature-screening protocol (to be completed)

1. Predefine review questions about agent adoption, repo selection bias, usefulness, quality, maintainability, reviewer burden, cost and late-2027 outcomes.
2. Record exact search queries, dates, indexing scope and API response counts from ACM DL, IEEE Xplore, OpenAlex/Scopus and Google Scholar. Use backward/forward citation snowballing.
3. Deduplicate DOI/arXiv IDs, retain all excluded-paper rationale, dual screen at least a sample of title/abstract and full texts, and resolve discrepancies.
4. Extract study population, sample frame, agent definition, exposure time, controls, outcomes, uncertainty, missingness, confounding, source availability and whether the effect is causal, associational or reported by a vendor.
5. Prefer journal/conference version over preliminary preprint if methods/results changed; maintain version-specific results. Chen/Stratton: the author's homepage describes a later expanded paper while the currently linked PDF may be an earlier 500-firm edition—do not silently mix it with news figures describing 718 firms.
6. Preserve a PRISMA-style screening flow only if a complete systematic review is actually performed. No fabricated search counts or citation metrics.
7. Literature-revision checkpoint: 2027-01-15, 2027-04-15, 2027-07-15, 2027-10-15. Dates are planned, not performed.
