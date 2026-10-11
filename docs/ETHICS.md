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
