# Hiring source URL lexical host correction — issue #222

**Date:** 2026-10-16. **Scope:** an offline, deliberately limited data-format correction for a *proposed* requisition observation study. No employer page was fetched and no human/source rights approval is inferred.

The current `trending_study.hiring_observations._url` parser enforced canonical public HTTPS sources but used `[a-z0-9]+(?:[.-][a-z0-9]+)*` for hostnames. That pattern wrongly rejected ordinary valid DNS labels with interior hyphens, such as `careers.jobs-board.invalid`. Pre-excluding common host syntax could silently bias the proposed approved-employer source frame.

The guard now accepts ASCII DNS labels of up to 63 characters with letters, digits and *interior* hyphens, but refuses empty labels, leading/trailing hyphens and hosts longer than 253 characters. It preserves rejection of localhost, local/internal domains, non-global literal IPs, credentials, unsafe path encodings, redirects/search-misses treated as missing, and unauthorized network access.

Synthetic tests check valid hyphenated hosts, edge-hyphen and overlong labels, and representative internal/private hosts. Acceptance of a host string is **not** DNS resolution, proof of an actual employer, source permission, time-stamped observation, requisition identity, actual closure or a hire. Future network collection must undergo its own allowlist and connection-time DNS/SSRF security review.

**Practical maintainer lesson:** input validation should reject dangerous/ambiguous evidence without excluding ordinary valid source formats that would distort a sampling frame. Record rejected-source counts as missingness, not verified negative outcomes.
