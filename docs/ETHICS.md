# Ethics, platform use, and limits

- Respect GitHub Terms, robots/access policies and rate limits; don't bypass access controls, use proxy rotation or evade blocks. A single user-initiated public Trending fetch is provided for pilot use; **do not schedule bulk scraping by default** without reviewing platform permissions.
- Prefer official GitHub APIs for repository metadata. Use a token via the `GITHUB_TOKEN` environment variable; never commit the token or place it in logs.
- API snapshots are point-in-time measurements. Never reconstruct historical stars from current values.
- Repositories and maintainers are not study participants who consented to ranking individual behavior. Avoid sensitive attributes, personal-email collection, identity judgments and publicly listing 'worst' maintainers.
- Dataset publication should favor aggregate reporting; perform platform-terms and privacy review before shipping row-level derived data. Respect takedown or correction requests.
- GitHub Trending is a selection surface whose algorithm is not publicly reproducible. Selection effects and observational confounding limit generalization and causal inference.
- Publishing the project code under MIT does not grant blanket rights to republish third-party content.
