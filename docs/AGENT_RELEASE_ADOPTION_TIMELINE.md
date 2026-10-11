# Dates and adoption evidence: why these historical windows? (reviewed 2026-10-11)

**Crucial:** product release ≠ actual adoption, self-reported survey ≠ population prevalence, provider WAU ≠ public-repo agent authors, AI SDK import ≠ agent coding. Dates below relate to developer coding agents, **not** generative-AI inventions in general.

## Reproducible primary-source timeline

| Date | Launch/adoption event | Source | Research use |
|---|---|---|---|
| Before 2025 | Copilot completion, Cursor, Aider and other agents/assistants already exist | [Kalliamvakou historical mining](https://doi.org/10.1145/2597073.2597074) + period-qualified product history | 2024 is a baseline against *later wider adoption*, NOT untreated/no-AI |
| 2025-02-24 | Anthropic introduces Claude Code as **limited research preview** | [Anthropic announcement](https://www.anthropic.com/news/claude-3-7-sonnet) | Early agent-availability reference |
| 2025-04 | Codex CLI released | [OpenAI May 16 retrospective explicitly states prior-month CLI launch](https://openai.com/index/introducing-codex/) | Earlier terminal-agent availability |
| 2025-05-16 | OpenAI introduces Codex cloud agent preview | [OpenAI launch](https://openai.com/index/introducing-codex/) | Delegated cloud PR/workflow availability |
| 2025-05-19 | GitHub Copilot coding agent public preview | [GitHub changelog](https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/) | Native GitHub issue-to-PR agent entry point |
| May 2025 | Claude Code generally available, per later Anthropic statement | [Anthropic September 2025 release](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation) | Broadening access, **not** repo-level evidence |
| 2025-10-06 | Codex general availability | [OpenAI official](https://openai.com/index/codex-now-generally-available/) | Mature distribution phase |
| 2026-02-02 | Codex desktop app with parallel agents | [OpenAI official](https://openai.com/index/introducing-the-codex-app/) | Agent orchestration broadens |
| 2026-02-21 | Estimated agent-trace adoption: **22.20–28.66% in 128,018-project academic sample** | [Robbes et al. 2026 ACM TOSEM](https://doi.org/10.1145/3822180) | Explicit study-population adoption estimate; imperfect trace sensitivity |
| 2026-03-19 | OpenAI reports **>2m Codex weekly active users** | [OpenAI release](https://openai.com/index/openai-to-acquire-astral/) | Product uptake; **not** GitHub repo users |
| 2026-06-02 | OpenAI reports **>5m Codex weekly active users**; ~20% knowledge-worker users | [OpenAI official](https://openai.com/index/codex-for-knowledge-work/) | Vendor-reported product users; overlaps other tools and includes non-developers |
| 2026-07 | Anthropic reports Claude Code weekly active usage doubled since January 2026 (no absolute number in cited announcement) | [Anthropic Series G announcement](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) | Growth index, **not** count; revenue cannot infer individual users |
| 2026-10-06 | Stack Overflow 2026 survey released | [2026 usage data](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent), [methodology](https://survey.stackoverflow.co/2026/methodology) | Self-reported named-tool adoption, not population prevalence |

## 2026 self-reported use (do not confuse denominators)
In the 2026 Stack Overflow named coding-agent/assistant question (`n=12,255` **question respondents**, multiple selection possible), Claude Code 8,030 (**65.5%**), GitHub Copilot 7,196 (**58.7%**), OpenAI Codex 3,620 (**29.5%**), Cursor 3,127 (**25.5%**). Overall 2026 survey `n=30,903` valid respondents, fielded June 23–Aug 5 and recruited largely through Stack Overflow/community channels. Named-tool percentages are **not** percentages of all GitHub users, all software developers or unique active installations; cannot add categories. Survey groups 'agents and assistants' together in the named-tool question.

A separate Stack Overflow question `n=17,464` reports **65.9%** use AI coding assistants or agents at work, and **26.2%** use agents or automated workflows; this has a different denominator/definition. Source: [AI data](https://survey.stackoverflow.co/2026/ai/data). Do not present these figures as interchangeable.

## 2027 start point
- **Do not simply use 2025-02-24 as a repo 'treatment' date.** Use it as a global release marker for descriptive windows.
- For a repository-level adoption event study, index `t=0` at the repo's **first verified observable coding-agent action**, plus separate controls not-yet-observed using agents; mark first detection as an imperfect *upper bound* on first actual use (actual undisclosed use could be earlier). For actual treatment date, obtain consented tool-usage logs where possible.
- We plan main 2026-11–2027-04 recruitment, outcomes 7/30/90/180 days after enrolment, with comparison histories before observed adoption. Late-2027 lessons are attainable if these timelines and access hold; no guarantee of sufficient N.
- Do not treat agent-launch as exogenous causal shock: availability, advertising, ecosystem trends and developer choice co-evolve.

## What counts as 'how many people use it'?
| Source | Can count | Cannot claim |
|---|---|---|
| OpenAI >5m weekly users Jun 2026 | Provider's product weekly active accounts/users by their definition | Number of repos built with Codex, agent PRs or independent developer users |
| Anthropic doubling 2026 | Relative Claude Code active weekly-user growth | Absolute Claude Code users in 2026 |
| Stack Overflow named-tool n=12,255 | Among surveyed respondents who answered this question, tool used in last year | Random representative global market share |
| ACM 128,018 projects | Estimated trace adoption within academic frame and method | All GitHub repos or all AI-assisted code |
| GitHub agent metrics for consenting organizations | Verified GitHub Copilot coding-agent activity (authorized org/enterprise reporting) | General publicly accessible metric for all third-party repos |
| GH Archive traces | Observable public commits, PR and events within archive coverage | Verified origin of silent AI editing or true unique people |

Review numbers, sources and definitions every quarter; adoption may change faster than static papers can capture.
