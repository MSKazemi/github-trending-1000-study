# Ethics, platform use, and limits

- Respect GitHub Terms, robots/access policies and rate limits; don't bypass access controls, use proxy rotation or evade blocks. A single user-initiated public Trending fetch is provided for pilot use; **do not schedule bulk scraping by default** without reviewing platform permissions.
- Prefer official GitHub APIs for repository metadata. Use a token via the `GITHUB_TOKEN` environment variable; never commit the token or place it in logs.
- API snapshots are point-in-time measurements. Never reconstruct historical stars from current values.
- Repositories and maintainers are not study participants who consented to ranking individual behavior. Avoid sensitive attributes, personal-email collection, identity judgments and publicly listing 'worst' maintainers.
- Dataset publication should favor aggregate reporting; perform platform-terms and privacy review before shipping row-level derived data. Respect takedown or correction requests.
- GitHub Trending is a selection surface whose algorithm is not publicly reproducible. Selection effects and observational confounding limit generalization and causal inference.
- Publishing the project code under MIT does not grant blanket rights to republish third-party content.

## AI-era extension (research-draft safeguards)
- Do not infer a named contributor's AI usage, motives or competence from code style, AGENTS.md, PR labels alone or automated detectors. Such classifiers have false positives and false negatives.
- Obtain appropriate informed consent for personal developer workflow/timing/token logs; avoid raw prompt transcripts because they may include passwords, proprietary code or sensitive user context. Favor aggregated measurements and narrow retention.
- Publishing a derived repo dataset does not authorize private logs, traffic data, hidden telemetry, identity scraping, or sharing revoked/removed content.
- Treat paid/organic star manipulation, spam PRs and inflated activity as invalid research interventions and counter to the study's purpose.
- Risk-sensitive software requires stronger verification; tool-generated 'go' guidance is not a security or legal clearance.


## Additional protections for the 2027 gold set and human externalities
- Candidate search results and source URLs may point to malicious packages; no automatic installation or execution inside credentialed GitHub Actions, uncontrolled development environments or machines with secrets.
- Opt-in experimental upstream interaction must not spam uninvolved maintainers. Measure upstream cost only with permission and appropriate anonymization.
- No forced ranking of niche/educational/public-interest software as 'garbage'. Evaluate against declared function and audience.
- A verified reusable candidate requires documented permission/license/compatible obligation checks; repository publicity does not establish right to copy.
- Evaluator contamination from known public patches/AI training and self-authored acceptance suites needs independent review.

## Trending source-access review checkpoint (2026-10-12)

At this checkpoint, the retrieved official [GitHub robots.txt](https://github.com/robots.txt) lists `Disallow: /*since=*` under `User-agent: *`, covering the repository's present `/trending?since=...` URLs. The official [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) restrict automated excessive activity and condition research use of public, non-personal information. Do not infer collection permission from a green parser test, public page visibility or the general research-use clause. **Pause those URL fetches until source-access authority is actually verified by a human reviewer.** Recheck policies when deciding a future capture method, and preserve the negative permission decision if authorization is unavailable. The newly implemented independent page-QA utility reads only local files; it is not a workaround for obtaining unpermitted HTML.
