# Technology news, journals and conference evidence watch (2026–2027)

**Compiled:** 2026-10-12. **Status:** curated monitoring and publication-planning recommendation, **not** systematic literature review, prospectively captured cohort or submission. All venue dates and publication policies should be rechecked on official CFPs before acting.

**Goal:** supply historical context and current contradictory evidence for the [reuse-first, useful and sustainable software mission](GREEN_REUSE_MISSION_2027.md). This is a supplement to [READING_LIST_2027](READING_LIST_2027.md), the existing [news/paper register](../references/study_sources_2026.json), [green reuse sources](../references/green_reuse_sources_2026.json), and [selection protocol](SELECTION_PROTOCOL_2027.md). Curated feed metadata: [source watch register](../references/source_watch_2026.json). It does not supersede their evidence or the selection dates.

## 1. Time windows: do not confuse news coverage with study enrollment

| Window | Use | Important qualification |
|---|---|---|
| Pre-2021, citation-driven | Foundational mining validity, clone/reuse economics, software quality and sustainable computing | Include seminal work irrespective of publication year. |
| 2021-01 to 2023-12 | Historical AI code assistance, early GitHub Copilot era, changes in OSS practices | Not an untreated period; use original release evidence and historic events. |
| 2024-01 to 2024-12 | Coding-assistant evolution and early autonomous task orchestration | Historical comparator, not assumed human-only. |
| 2025-01 to 2025-12 | Coding-agent capability and distribution changes (Claude Code, Codex, Copilot coding agent) | Launch announcements are event markers, never observed repo adoption. |
| 2026-01 to 2027-12 | Intensive news surveillance and formal study of adoption, redundant code, verified reuse, maintenance, human cost, energy and security | Record source *publication date* separately from *event date*. |
| 2028–2031 | Prospectively refresh longitudinal impacts, benchmarks, lifecycle measures and replication | Conditional research waves; not a claim about future events. |

**Search starting point:** use 2021–2027 as the core peer-reviewed/working-paper query period, backfill seminal pre-2021 papers with snowballing. For journalistic retrospective chronology, perform focused coverage from 2024-01, with earlier 2021–2023 primary launch citations. Main prospective GitHub Trending pilot and enrollment remain as defined in [SELECTION_PROTOCOL_2027.md](SELECTION_PROTOCOL_2027.md): 2026-10-15–31 pilot and proposed 2026-11-01–2027-04-30 recruitment, conditional on permission/feasibility; no inference from news that enrollment occurred. Agent adoption is measured from independently verifiable repository or opt-in developer events where possible, **not product launch dates**.

## 2. Evidence hierarchy and source roles

1. **Primary audited data / registered controlled experiments / reproducible peer-reviewed studies**: basis for effectiveness, use, productivity and comparative sustainability claims, subject to study validity.
2. **Official vendor/platform announcements, policy and standards**: authoritative for their *own* release and policy dates; self-reported population and usage denominators may be selected and unverified externally.
3. **Independent technology reporting**: event discovery, cross-checking and obtaining multiple perspectives, not an independent replication of the study it reports.
4. **Community posts, Hacker News, GitHub issues**: early qualitative signals to frame questions, not representative frequencies or scientific proof.
5. **Preprints/working papers**: prospective leads, not automatically peer reviewed; reconcile version of record and publication date.

Never count a primary study and 3 articles reporting it as 4 independent empirical samples. Record unsupported or contradictory evidence and genuine null findings. For AI-authorship, stars, model use, or carbon, see [ETHICS](ETHICS.md), [AGENT_RELEASE_ADOPTION_TIMELINE](AGENT_RELEASE_ADOPTION_TIMELINE.md) and [CRITICAL_RESEARCH_GAPS_2027](CRITICAL_RESEARCH_GAPS_2027.md).

## 3. Independent technology reporting to screen

| Priority | Outlet and source | Look for | Risk |
|---|---|---|---|
| P1 | [Ars Technica](https://arstechnica.com/) | AI coding regressions, developer evidence, real-world testing and review | Often summarizes a linked study; open primary paper |
| P1 | [The Register](https://www.theregister.com/) | Agent-generated PR overload, maintainer burden, incidents and platform decisions | Anecdotes are not rates |
| P1 | [Reuters Technology](https://www.reuters.com/technology/) | Dated launch/adoption announcements, policy, financing, industry shifts | Release ≠ adoption |
| P1 | [IEEE Spectrum](https://spectrum.ieee.org/) | Systems engineering, energy/hardware and measured AI constraints | Check cited experimental setup |
| P1 | [MIT Technology Review](https://www.technologyreview.com/) | Societal/technical tradeoffs and independent AI scrutiny | Analysis ≠ empirical sample |
| P1 | [InfoQ](https://www.infoq.com/) | Practitioner engineering, production examples, architecture and tooling | Case study may lack controls |
| P2 | [TechCrunch](https://techcrunch.com/) | Agent startup launches, capabilities, market change | Hype/selection and vendor claims |
| P2 | [Axios Technology](https://www.axios.com/technology) | AI adoption and enterprise usage reporting | Often repeats vendor-defined metrics |
| Discovery | [Hacker News](https://news.ycombinator.com/) | Complaints, engineer experiences and overlooked projects to investigate | Highly self-selected, unverified |

## 4. Official, security, sustainability and measurement feeds

| Priority | Source | What it establishes / use |
|---|---|---|
| P1 | [GitHub Blog](https://github.blog/), [Changelog](https://github.blog/changelog/) | Platform dates, Copilot coding agent availability, policy, GitHub measurement access |
| P1 | [OpenAI News](https://openai.com/news/) | Codex availability and vendor-reported usage, with precise denominators |
| P1 | [Anthropic News](https://www.anthropic.com/news) | Claude Code release milestones, models, provider reported usage |
| P1 | [Google Developers Blog](https://developers.googleblog.com/) | Gemini and agent tooling developments |
| P1 | [OpenSSF](https://openssf.org/blog/) | Provenance, open-source supply chain, malicious dependencies, agent workflows |
| P1 | [Green Software Foundation](https://greensoftware.foundation/) and [SCI for AI](https://greensoftware.foundation/standards/sci-ai/) | Measurement standards, boundary assumptions, versioned specifications |
| P2 | [OSV](https://osv.dev/) | Version-specific known vulnerabilities, *not* proof of absolute safety |
| P2 | [SLSA](https://slsa.dev/) | Supply-chain levels and attestations, not proof a component meets user requirements |
| P2 | [GH Archive](https://www.gharchive.org/) | Historical public GitHub events subject to coverage caveats; not historic Trending rank |
| P2 | [Stack Overflow Survey](https://survey.stackoverflow.co/) | Self-reported developer/agent use with question-specific opt-in denominators |
| P2 | [METR](https://metr.org/) | Experiment methods, longitudinal developer productivity issues |
| P2 | [arXiv cs.SE](https://arxiv.org/list/cs.SE/recent) | Early research discovery; preprints must be screened |
| P2 | [OpenAlex](https://openalex.org/) | DOI/source search and citation discovery; search API coverage, pricing and versions checked at execution |

Never automatically execute untrusted downloaded projects in a credentialed environment; do not assume security scanner result, license file or stars imply code is safe and reusable.

## 5. Journals: reading priorities AND potential submission fit

Ranked by **fit to the project's research questions**, not impact factors or inferred acceptance chance.

| Fit | Journal and official site | Best potential article | Minimum evidence burden |
|---|---|---|---|
| 1 | [ACM Transactions on Software Engineering and Methodology (TOSEM)](https://dl.acm.org/journal/tosem) | Agent adoption, cross-project reuse and repository bias | Rigorous software engineering contribution, sampling validity, thorough quantitative/qualitative audit |
| 1 | [Empirical Software Engineering (EMSE)](https://link.springer.com/journal/10664) | Trending vs utility, 2027 registered task/reuse study | Transparent empirical protocol, representativeness/selection, effect sizes, replication |
| 1 | [IEEE Transactions on Software Engineering (TSE)](https://www.computer.org/csdl/journal/ts) | Independently validated cross-tool agent/reuse comparison | Strong original software engineering evidence, methodological novelty, reproducibility |
| 1 | [Journal of Systems and Software (JSS)](https://www.sciencedirect.com/journal/journal-of-systems-and-software) | Reuse and maintenance lifecycle | Engineering utility, tasks, system tradeoffs and adequate follow-up |
| 1 | [Information and Software Technology (IST)](https://www.sciencedirect.com/journal/information-and-software-technology) | Adoption/quality/maintainer outcomes or systematic evidence review | Explicit contribution, appropriate rigorous evidence, careful review procedure |
| 2 | [SoftwareX](https://www.sciencedirect.com/journal/softwarex) | Reproducible open-source research harness, dataset/tool | Actual installable/reusable tool with validation and documented use |
| 2 | [IEEE Software](https://www.computer.org/csdl/magazine/so) | Evidence-based engineering guidance | Practical applicability, well-supported claims; magazine, not interchangeable with TSE research journal |
| 2 | [Sustainable Computing: Informatics and Systems](https://www.sciencedirect.com/journal/sustainable-computing-informatics-and-systems) | Bounded measured lifecycle energy/carbon for comparable tasks | Functionally matched baseline, environmental measurement with uncertainty and maintenance boundary |
| 2 | [IEEE Transactions on Sustainable Computing](https://www.computer.org/csdl/journal/su) | Resource-aware agent software engineering | Reproducible energy, systems and environmental comparison |
| Conditional | [Joule](https://www.sciencedirect.com/journal/joule) | A broad, high-impact energy finding, only if supported | High-quality calibrated physical energy evidence and broader significance; **not** justified by token savings alone |

**Submission strategy:** (a) methods/visibility study -> EMSE/TOSEM/JSS/IST; (b) independently accepted agent-workflow experiment -> TSE/TOSEM/EMSE; (c) validated open-source software artifact -> SoftwareX; (d) truly measured energy/lifecycle result -> Sustainable Computing or IEEE T-SUSC. Do not claim journal ranking, impact factor, APC or deadlines without checking the current official publisher page.

## 6. Conferences for literature, peer feedback and future papers

| Fit | Venue | Main study connection |
|---|---|---|
| P1 | [ICSE](https://conf.researchr.org/home/icse-2027) | Broad software engineering methods, agents, usefulness |
| P1 | [MSR](https://2027.msrconf.org/) | GitHub sampling, trending bias, repository signals and reused-code discovery |
| P1 | [FSE](https://conf.researchr.org/home/fse-2027) | Functional quality, agent engineering, reuse-first effectiveness |
| P1 | [ASE](https://conf.researchr.org/) | Autonomous programming, automated generation and repair |
| P1 | [ESEM](https://conf.researchr.org/) | Design, measurement, experiments and productivity |
| P1 | [SANER](https://conf.researchr.org/) | Source-level reuse, code clones, software evolution |
| P1 | [ICSME](https://conf.researchr.org/) | Maintenance, review debt and software evolution |
| P1 | [ICPC](https://conf.researchr.org/home/icse-2027) | Comprehension of others' code and safe adaptation |
| P1 | [FORGE](https://conf.researchr.org/home/icse-2027) | Foundation models, AI agents, benchmark validity |
| P2 | [CAIN](https://conf.researchr.org/home/icse-2027) | AI systems engineering |
| P2 | [EASE](https://conf.researchr.org/) | Evidence synthesis and empirical studies |
| P2 | [ICST](https://conf.researchr.org/) | Independent functional testing of reuse candidates |

Consult edition-specific calls for papers and track policies. Conference URLs above may point to a conference-series discovery page rather than an edition CFP.

### Time-sensitive submission feasibility on 2026-10-12 (not a commitment)

- **MSR 2027 Registered Reports + EMSE:** best near-term option **if** the study design can be responsibly frozen. Official [RR call](https://2027.msrconf.org/track/msr-2027-registered-reports): **2026-11-13 abstract**, **2026-11-20 Stage 1 report**; approved registration presented at MSR, Stage 2 full paper to EMSE targeted **by 2027-09-30**. Study's feasibility, power, access/ethics and design must precede submission; Stage 1 is not final journal acceptance. The call explicitly supports confirmatory and exploratory designs and can publish meaningful negative results.
- **MSR 2027 technical track:** [official dates](https://conf.researchr.org/dates/msr-2027) list **2026-10-20 abstract** and **2026-10-23 paper**. A new longitudinal sample cannot generate 180-day outcomes by then. Submit only an independently complete methods/tool/earlier-data paper, not fictional results.
- **MSR 2027 Data/Tool Showcase:** [official dates](https://conf.researchr.org/dates/msr-2027) list **2026-11-05 abstract**, **2026-11-10 paper**. Appropriate only if a real validated tool/dataset exists, not protocol-only fixtures.
- **FSE 2027 main research track:** [official CFP](https://conf.researchr.org/track/fse-2027/fse-2027-papers) full paper deadline **2026-10-02** (closed as of this note). Some other tracks may have later deadlines: verify separately.
- **ICSE 2027 main research track:** [official CFP](https://conf.researchr.org/track/icse-2027/icse-2027-research-track) paper deadline **2026-06-30** (closed). Journal-first is for already published/accepted eligible journal work, not a bypass for a new submission.
- Journal rolling submissions (after checking scope, editorial status, APC, dual-submission policy) and **2028 conferences** are realistic alternatives if data arrive late-2027.

**Recommendation:** prioritize a *Registered Report only after feasibility/pilot design review*, and keep the main 2027 longitudinal manuscript for publication after actual +180d outcome data. Do not accelerate sampling, report early outcomes as complete, or submit the same work simultaneously.

## 7. Screen by six research themes, not just 'AI is popular'

1. **AI coding agent uptake:** Claude Code, Codex, Copilot coding agent, Cursor, Aider, Gemini; availability versus verified adoption, user and repository denominator.
2. **Reuse versus repeated generation:** code search/retrieval, dependencies, copied snippets, duplicate functions, suitable existing versions and repositories that never trended.
3. **Correctness/security/licensing:** independent acceptance, package provenance, supply chain, vulnerabilities, licensing, copied code and hallucinated packages.
4. **Human and maintainer outcomes:** time-to-solution, code review time, repair burden, new-developer comprehension, fatigue and upstream externalities.
5. **Green lifecycle:** measured local/CI/cloud energy with unknowns, hardware/grid/carbon assumptions, inference and indexing cost, lifetime runtime and rebound.
6. **Sampling, discovery and visibility:** trending rank versus baseline stars, promotion/visibility shocks, ecosystem/language confounders, unobserved niche-but-reused libraries.

### Example literature and news queries

Search DOI-indexed bibliographic systems with publication-year, language and document-type restrictions recorded:

- `("coding agent" OR "AI software engineer" OR "Claude Code" OR "Codex") AND (adoption OR productivity OR evaluation OR reliability)`
- `("AI-generated code" OR "agent-generated pull request") AND (reuse OR duplication OR redundancy OR clone OR maintainability)`
- `("software reuse" OR "code reuse") AND (discovery OR retrieval OR "open source" OR "reuse economics")`
- `("GitHub Trending" OR "repository popularity" OR stars) AND (validity OR selection OR adoption OR reuse)`
- `("green software" OR "software carbon intensity" OR "energy consumption") AND ("code generation" OR software OR agent)`
- `("dependency security" OR SBOM OR SLSA OR OpenSSF) AND ("coding agent" OR "AI generated code")`

For vendor/platform releases, include model/tool names, release date, provenance and usage metric denominators separately. Run backward/forward snowballing from the reviewed papers in [READING_LIST_2027](READING_LIST_2027.md).

## 8. Monitoring cadence and source-record protocol (weekly briefing scheduled)

| Cadence | Activity | Output |
|---|---|---|
| 2–3 times/week during 2026–2027 | Scan official releases, independent news and security/SCI feeds | Dated *candidate* events with official cross-links, duplicates and open questions |
| Weekly | Screen arXiv cs.SE, OpenAlex/ACM/IEEE/Springer/Elsevier literature and conference proceedings | Bib IDs, publication status, methods, populations, preprint-to-venue mapping |
| Monthly | Screen all included evidence by RQ, DOI and publication version, cross-check adverse results | Updated claim ledger with confidence and source overlap |
| Quarterly (already planned) | Revalidate release/adoption chronology, journal/CFP conditions, threat models and prospective design | Frozen vintage + dated corrections in advisory evidence template |


**2026-10-12 operational update:** A weekly *evidence briefing*, separate from GitHub Trending collection, was scheduled for **Monday mornings around 08:00 Europe/Rome**, beginning **2026-10-19**. It is a flexible delivery window, not a guaranteed exact-minute publication. Each run should check the latest repository sources first, review the prior seven days, capture primary links/DOIs and contradictory results, then **attempt to save a dated research note via a GitHub branch and PR for human review if connector permissions allow**. If repo write fails, it must declare that plainly and supply repository-ready Markdown. This scheduled briefing does **not** authorize bulk scraping, create an automatic GitHub Action, amend a frozen cohort or automatically merge PRs; no weekly findings have been produced yet.

**For each reviewed item, retain at minimum:** `source_id, source_type, outlet, title, authors/organization, url, doi_or_persistent_id, published_date, event_date, retrieved_at_utc, peer_review_status, version, study_design, population_frame, denominator, treatment/exposure_definition, comparator, outcomes, uncertainty, funding/conflicts, relevant_RQs, positive_negative_neutral, limitations, duplicates_or_derivative_of, reviewer, decision, exclusion_reason`. A vendor claim should have `vendor_self_reported=true` and any rate should store its exact numerator, denominator and collection interval. No invented or universal claims. A source *on a watch list* is not evidence it has been comprehensively screened.

**Reproducibility:** cache only permissible metadata/links; protect copyright, personal information, platform access policies and API usage limits. A systematic review needs protocol, per-database time-stamped queries, deduped counts and documented exclusions; until then this is a curated source list, **not PRISMA-compliant findings**.

## 9. Research-paper allocation (conditional)

| Paper | Primary research idea | First-fit venues | When ready |
|---|---|---|---|
| A — visibility vs use | Trending attention vs separately verified cross-project integration and quiet software reuse | MSR, EMSE, TOSEM, IST | Real frozen sampled cohort + baseline/controls + peer audit |
| B — agent vs reuse-first | Registered human/agent × generate/reuse-first task trials, independently accepted functionality and human costs | EMSE/MSR Registered Reports, TSE, ICSE/FSE, ASE | Prospective independent tests, consent, power and genuine randomization |
| C — maintenance/security | 30/90/180d repair/maintainer burden, dependency/version evidence and functional correctness | JSS, TSE, ICSME, SANER | Versioned verified outcomes and appropriate follow-up |
| D — green break-even | Function-equivalent workflows with observed/calibrated energy and lifetime/boundary uncertainty | Sustainable Computing, IEEE T-SUSC | Defensible full or explicitly partial system boundaries |
| E — benchmark/tool | Reusable query/candidate gold set, verifiable acceptance harness, screening tool | MSR Data/Tool, SoftwareX, FSE artifact | Actually tested and publicly reusable artifact; no simulated 'success' |

Future manuscripts are options, not promises of 5 publications. Avoid duplicate publication of substantially overlapping analyses. Citations and flags in source watch must be checked again at submission time.

## 2026-10-12 independent source and schedule verification checkpoint

For this curated watch (not a full literature review), official track sources were checked independently when integrating this PR:

- [MSR 2027 official dates](https://conf.researchr.org/dates/msr-2027) confirm 2026-10-20/23 technical abstracts/papers, 2026-11-05/10 data/tool abstracts/papers, and 2026-11-13/20 Registered Report initial abstract/report.
- [MSR 2027 Registered Reports CFP](https://2027.msrconf.org/track/msr-2027-registered-reports) confirms the Stage 1 design-before-execution requirement, the 2027-02-04 decision, and the conditional 2027-09-30 EMSE Stage 2 submission. **Stage 1 approval is not acceptance of the completed manuscript.**
- [ICSE 2027 Research CFP](https://conf.researchr.org/track/icse-2027/icse-2027-research-track) confirms the 2026-06-30 deadline has passed and explicitly warns authors that fabricated references can cause desk rejection.
- A user-authorized weekly evidence-briefing automation with first scheduled Monday **2026-10-19 08:00 Europe/Rome** was independently found configured and enabled at integration time. No briefing has yet run; it is not a GitHub crawler, and future deliveries depend on task/tool permissions.

**No systematic source screening, discovered empirical effect or scientifically validated strategy is implied.** Record dated updates when deadlines or calls change; these links are **edition-specific** and should not be projected into 2028 schedules.
