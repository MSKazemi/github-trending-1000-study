# Prior research and methodological foundations

These are **verified starting references**, not a completed systematic literature review. Additional Scopus/ACM/IEEE/Semantic Scholar searches should be preregistered with dates, query strings, inclusion/exclusion and screening decisions before claiming comprehensive coverage.

## Empirical GitHub research
1. Kalliamvakou, E. et al. (2014). **The Promises and Perils of Mining GitHub**. MSR. DOI: [10.1145/2597073.2597074](https://doi.org/10.1145/2597073.2597074). Critical discussion of sampling, repository vs project, PR merge data and inactive/non-software repos.
2. Borges, H., Valente, M. T., Hora, A., Coelho, J. (2015). **On the Popularity of GitHub Applications: A Preliminary Note**. [arXiv:1507.00604](https://arxiv.org/abs/1507.00604). Star-growth trajectories, popularity as distinct from functionality.
3. **What's in a GitHub Star? Understanding Repository Starring Practices in a Social Coding Platform**. Journal of Systems and Software (2018/2019). [Publisher](https://www.sciencedirect.com/science/article/abs/pii/S0164121218301961). Survey and longitudinal patterns; stars reflect interest/bookmarking and warrant caution in sampling and interpretation.
4. Gousios, G., Spinellis, D. (2017). **Mining Software Engineering Data from GitHub**, ICSE companion. [Tutorial & replication links](https://github.com/ghtorrent/tutorial). Data availability pitfalls, GHTorrent/archives, collection methods.
5. **Will you come back to contribute? Investigating the inactivity of OSS core developers in GitHub**. *Empirical Software Engineering*. [Article](https://link.springer.com/article/10.1007/s10664-021-10012-6). Notes explicit selection bias when sampling from Trending.
6. **Research artifacts in software engineering publications: Status and trends** (2024), *Journal of Systems and Software*. [DOI](https://doi.org/10.1016/j.jss.2024.112032). Limited validity of stars and code smells as project impact/quality proxies.

## Community health and standards
7. CHAOSS. **Starter Project Health**: [model](https://www.chaoss.community/kb/metrics-model-starter-project-health/). First human response, change-request closure, contributor absence factor, release cadence.
8. CHAOSS. **Issue Response Time**: [metric](https://www.chaoss.community/kb/metric-issue-response-time/). Exclusion of bots and self-response; precise event times.
9. CHAOSS. **Community Service and Support**: [model](https://www.chaoss.community/kb/metrics-model-community-service-and-support/). Censoring/definitions important for open issues.
10. GitHub. **REST starring endpoints**: [docs, API 2026-03-10](https://docs.github.com/en/rest/activity/starring?apiVersion=2026-03-10). Public aggregate counts and star history; stargazer-list restrictions since July 2026.
11. GitHub. **Repository traffic**: [docs](https://docs.github.com/en/rest/metrics/traffic). Privileged write-access data over limited rolling period, not generally available for sample.
12. GitHub. **Rate limits**: [docs](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api). Separate search API and secondary rate limits.
13. [GitHub Trending](https://github.com/trending). Observed ranking surface only; platform does not publish the complete ranking formula.
14. [GitHub Trending Today methodology](https://githubtrending.today/methodology/). A third-party collection example, not authoritative ranking methodology.
15. [GithubTrends trending-boost study](https://githubtrends.app/research/trending-boost/). A non-peer-reviewed comparative reference; follow-up star count differences should not be interpreted as causal effects of Trending.

## Intended research novelty
The individual ingredients (stars, Trending scrapes, OSS health metrics) already exist. Novelty must be demonstrated in **joint temporal design**, prospective controls and robust estimates, transparent black-box ranking audit, validated documentation/repository-type rubrics, and reproducible evidence-weighted recommendations. Do not claim first-ever study.

## Structured literature-review plan
- Search ACM DL, IEEE Xplore, Scopus/OpenAlex, and Google Scholar (for discovery), queries combining `GitHub Trending`, `repository popularity`, `star growth`, `open source health`, `repository ranking`, `visibility`, `GitHub algorithm`, `mining software repositories`.
- Record search dates, deduplicate DOIs, screen title/abstract then full text with logged exclusions; apply backward/forward snowballing. Separate peer-reviewed articles from blog posts and vendor claims.
- Extraction schema: paper/year/venue/DOI, sample frame/size, outcomes, time window, covariates, confounders, statistical approach, code/data, threats and direct relevance to each RQ.
- Quality appraisal: prospective vs retrospective outcomes; sampling and leakage risk; construct validity; controls/uncertainty; public replication artifacts. Report a PRISMA-style flow if review becomes systematic.


## Green, reusable code and environmental measurement (new study direction)
- Jahanshahi, Reid & Mockus. **Beyond Dependencies: The Role of Copy-Based Reuse in Open Source Software Development**, ACM TOSEM, Oct 2025. [DOI](https://doi.org/10.1145/3715907). Critically important finding: substantial reused code originates in small/medium projects; Trending-only samples would miss important reuse sources. This is copy-based reuse, not a direct measure of avoided electricity.
- Wu et al. **An Empirical Study of Code Clones from Commercial AI Code Generators**, FSE 2025. [DOI](https://doi.org/10.1145/3729397). Shows specific clone concerns, not universal carbon waste.
- Huang et al. **More Code, Less Reuse**, ACM 2026. [DOI](https://doi.org/10.1145/3793302.3793622). Agent PR redundancy and reviewer sentiment; interpret source-sample scope.
- **Software reuse cuts both ways**, JSS (2020). [Full article](https://www.sciencedirect.com/science/article/pii/S0164121220301199). Copying/importing more dependencies can also raise security risks.
- [ISO/IEC 21031:2024](https://www.iso.org/standard/86612.html), **Software Carbon Intensity**. Environmental boundary, energy, location-specific carbon intensity, embodied hardware and functional unit.
- [GSF SCI for AI](https://greensoftware.foundation/standards/sci-ai/) (ratified extension), [Impact Framework](https://if.greensoftware.foundation/), [CodeCarbon](https://docs.codecarbon.io/3.3/explanation/power-estimation/). Measurement tools have limitations; provider model energy is not automatically visible.
- [Joule 2026 inference energy study](https://doi.org/10.1016/j.joule.2026.102430). Large workload/model effects mean tokens alone cannot be converted into a universal energy saving.

Full fields and caveats: [green/reuse references](../references/green_reuse_sources_2026.json). Separate a bibliographic starting list from a systematic literature review.
