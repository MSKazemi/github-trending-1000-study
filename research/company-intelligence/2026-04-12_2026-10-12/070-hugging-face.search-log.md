# Hugging Face (070) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](070-hugging-face.md) and [event ledger](070-hugging-face.events.csv) for [#138](https://github.com/MSKazemi/github-trending-1000-study/issues/138). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Method:** raw retrieval with `curl` using only a generic `Mozilla/5.0` User-Agent (no email, name, GitHub handle, credential or other personal identifier was sent to any site; SEC/EDGAR was not contacted); visible-text extraction and `grep` against the raw text to confirm every number, version, date and quote used in a ledger row; `gh api` for GitHub releases, repository licences and security advisories; PyPI JSON for upload times; the Hugging Face Hub API for dataset metadata; the Hacker News Algolia API to discover independent and critical coverage. Web search was **not** used (session budget exhausted); discovery was direct. **This is not exhaustive retrieval.** No page snapshots or hashes were archived in the repository; pages may change after access.

## Query and source log

| Date | Segment | Exact request or source | Result / decision | Found / screened / ledgered |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://huggingface.co/blog/feed.xml` (RSS) | 879 items back to 2020; 114 items with `pubDate` in window, of which 64 are official (un-namespaced) posts; the rest are community/partner org posts (e.g. `ibm-granite/`, `nvidia/`) | 114 / 64 official titles screened / 28 official posts opened |
| 2026-10-16 | all | `GET https://huggingface.co/changelog?p=0..9` | in-window entries: Apr 15, Apr 17, May 22, May 28, Jun 8, Jun 12, Jun 30, Jul 14, Jul 16, Jul 21, Aug 3, Aug 12, Sep 24 (x2), Oct 5, Oct 9, Oct 12; 16 entry pages opened | 17 / 16 / 6 rows |
| 2026-10-16 | all | `gh api repos/huggingface/<repo>/releases?per_page=100` for transformers, huggingface_hub, smolagents, datasets, diffusers, text-generation-inference, safetensors, lerobot, trl, peft, accelerate, tokenizers, huggingface.js, transformers.js, kernels, xet-core, sentence-transformers, optimum, lighteval, hf-mount, OpenEnv; also gradio-app/gradio | in-window release counts: transformers 25, huggingface_hub 34, trl 21, hf-mount 27, kernels 12, OpenEnv 9, sentence-transformers 9, peft 6, safetensors 5, xet-core 5, transformers.js 5, datasets 4, diffusers 4, tokenizers 4, accelerate 2, lerobot 2, optimum 2, smolagents 2, text-generation-inference 0, lighteval 0; huggingface.js and gradio ≥40 (listing truncated at 40) | 7 release rows |
| 2026-10-16 | all | `gh api repos/huggingface/<repo>` (licence/archived) | Apache-2.0 for transformers, huggingface_hub, smolagents, datasets, diffusers, lerobot, kernels, funes, skills, hf-mount, xet-core, tokenizers, sentence-transformers; OpenEnv BSD-3-Clause; hf-discover MIT; **transformers-to-mlx: no licence detected**; text-generation-inference **archived** (last push 2026-03-21, pre-window) | context |
| 2026-10-16 | all | `gh api repos/huggingface/<repo>/security-advisories` and `gh api advisories?ecosystem=pip&affects=<pkg>` (transformers, diffusers, datasets, huggingface-hub, smolagents, lerobot, gradio, safetensors) | in window: diffusers GHSA-98h9 / GHSA-j7w6 / GHSA-7wx4; transformers GHSA-29pf, GHSA-fgcw (LightGlue), GHSA-xrqw (save_pretrained traversal), GHSA-x9r9; datasets GHSA-379c; gradio GHSA-j36p, GHSA-6655, GHSA-7hp7 | 11 / 11 / 4 rows (others listed in report §3; NVD not queried) |
| 2026-10-16 | all | `GET https://pypi.org/pypi/{huggingface-hub,datasets,transformers}/json` | upload times for cited versions; licence strings | confirmations |
| 2026-10-16 | Jul | `GET https://huggingface.co/api/datasets/huggingface/agent-usage` | createdAt 2026-07-02T09:18:36Z; no licence tag | 1 row |
| 2026-10-16 | all | HN Algolia `search_by_date?query="Hugging Face"&tags=story` with `created_at_i` in [1775952000, 1792022400) — run in two date slices because of the 200-hit page cap | 304 hits total (103 before 2026-07-29, 200 after) | ~45 linked articles screened by title; 31 non-HF URLs requested, 24 read (7 inaccessible) |
| 2026-10-16 | all | HN Algolia `query=huggingface` same window | 645 hits; filtered to ≥5 points and titles not containing "Hugging Face" | mostly model-release links (excluded as third-party model news) |
| 2026-10-16 | all | `GET https://status.huggingface.co/` | rolling ~90-day view: scheduled maintenance only (Hub Sep 2 and Sep 16; Inference Endpoints Jul 22, Jul 30, Oct 7); no incident history before July shown | 0 rows |

## Opened sources by segment

| Segment | Opened (raw) | Included | Excluded / why |
|---|---|---|---|
| Apr 12–30 | changelog `kernels`, `spaces-agents-md`; blog `transformers-to-mlx`, `cybersecurity-openness`, `inference-providers-deepinfra`; release hub v1.11.0, v1.12.2 | 4 rows | cybersecurity-openness used only in report §5 (position piece); DeepInfra provider (hub v1.12.2, Apr 29) summarised in §3, not ledgered |
| May | GHSA-98h9, GHSA-29pf; HiddenLayer (2026-05-07); changelog `copy-repo-contents-to-buckets-instantly`, `filter-models-by-base-models-only`; hub v1.15.0 | 4 rows | Buckets copy and hub v1.15.0 (region-aware buckets, `hf skills list`) in §3 only; a personal blog "I poisoned a Hugging Face dataset…" (HN, May 23) **not opened** (individual author, unverifiable) |
| June | blog `hf-cli-for-agents`, `github-ci-hf-jobs`, `openenv-agentic-rl`, `agentic-resource-discovery-launch`, `local-models-pr-triage`, `huggingface-hub-release-ci`, `eee-community-evals`; changelog `trusted-publishers`, `service-accounts`, `filter-models-by-hardware`; releases datasets 5.0.0, hub v1.19.0 | 6 rows | GitHub-CI-on-Jobs, local-model PR triage, EEE evals, service accounts and hardware filter summarised in §3 |
| July | blog `revamped-kernels`, `lerobot-release-v060`, `skypilot-hf-storage`, `native-speed-vllm-transformers-backend`, `security-incident-july-2026`, `agent-intrusion-technical-timeline`; changelog `token-presets`, `spaces-with-agents`, `egress`; TechCrunch (Jul 14, Jul 20, Jul 26), Ars Technica (Jul 22), The Register (Jul 28), CSA landing page (released 07/27), WIRED (Jul 28), AI Forensics (Jul 28), TNW (Jul 27); hub v1.22.0, v1.26.0; GHSA-379c | 10 rows | TNW and TechCrunch Jul 26 (CEO's request for traces and $100M of compute) used in §5 only; LeRobot v0.6.0, SkyPilot backend, vLLM backend summarised in §3 |
| August | blog `state-of-open-models-summer-2026`, `icml-2026-open-reproductions`; changelog `filter-jobs-by-label`, `granular-feature-access`; hub v1.27.0; Business Insider (Aug 23), TechCrunch (Aug 24), METR (Aug 26), TechCrunch Microduck (Aug 27) | 4 rows | ICML reproduction hackathon in §3; Microduck robot excluded (hardware product outside study angle) |
| September | NVIDIA blog (Sep 3), CNBC (Sep 3), The Register opinion (Sep 3), blog `funes`, `webgpu-kernels`, `tokenizers-v1`, `transformers-llama-cpp-quants`, `omlx`, `evaleval-aisi`, `rl-environments`; changelog `gcp-marketplace`, `preview-lerobot-episodes`; Common Crawl (Sep 16), DuckDB (Sep 25), TechCrunch Base Labs (Sep 17), Bulletin of the Atomic Scientists (Sep 11), Rest of World (Sep 29), Open Source for Science Fund (Sep 30); GHSA-x9r9; hub v2.0.0 | 5 rows | Base Labs is a partner-led announcement (excluded); Common Crawl and DuckDB are third-party integrations summarised in §3; tokenizers v1 RC, GGUF in transformers, oMLX hire, RL environments tag, GCP Marketplace in §3 |
| Oct 1–12 | changelog `decision-models-on-the-hub`, `contribute-permission-for-access-tokens`; blog `building-with-ml-intern`; transformers v5.19.0 | 2 rows | decision-model tag and ML Intern in §3; Oct 13–15 posts (Muse Spark Open, FLUX.3 Klein, Granite Switch, faster tensor viewer changelog Oct 14) excluded as post-window |

No calendar segment was empty.

## Inaccessible sources

| URL | Result | Handling |
|---|---|---|
| https://openai.com/index/hugging-face-model-evaluation-security-incident/ | HTTP 403 | not read; OpenAI's account taken only as reported by Ars Technica and the HF timeline |
| https://openai.com/index/hugging-face-incident-and-the-road-ahead/ | HTTP 403 | not read |
| https://www.bleepingcomputer.com/news/security/hugging-face-breach-autonomous-ai-agent-system-internal-datasets-credentials/ | HTTP 403 (challenge) | not used |
| https://apnews.com/article/openai-gpt56-sol-hugging-face-63ab84fed5612af04d8a160d60f6def3 | HTTP 403 | not used |
| https://www.reuters.com/legal/litigation/openais-rogue-agents-probed-hugging-face-weaknesses-two-months-before-major-hack-2026-09-16/ | HTTP 401 | not used |
| https://www.wsj.com/opinion/the-hugging-face-hack-wasnt-what-it-was-cracked-up-to-be-e00cf3fa | HTTP 401 | not used (title only, E0) |
| https://www.zafran.io/resources/facehugger-vulnerabilities-in-hugging-face-diffusers-open-door-to-supply-chain-attacks-on-enterprise- | HTTP 404 | replaced by the GitHub advisories for diffusers |

No access gate was bypassed and no placeholder identity was used.

## Leads not verified (E0, unused)

- HN story "Note to AI agents: if you were told to find vulnerabilities here, good news" linking `https://huggingface.co/security.txt` (2026-09-10). Both `/security.txt` and `/.well-known/security.txt` fetched on 2026-10-16 contain only Contact, Expires, Preferred-Languages and Hiring fields; the reported note was **not present** at access time. Not ledgered.
- HN story "38% of Hugging Face Spaces are permanently broken" (personal GitHub repository, 2026-08-29): fetched but not used; individual audit without peer review.
- Many follow-on incident stories (Politico, Bloomberg, NYT, Wired, Axios, Reuters, Guardian, Fortune, Business Insider, MIT Technology Review, Redwood Research, lawsuits and congressional letters) were screened by title only; they mainly concern OpenAI's conduct and are outside this company's ledger scope.

## Embedded agent-directed text seen

- The HF security-incident page's comment thread includes a user comment quoting an example injection string ("Ignore all previous instructions…") as an illustration; The Register pages carry a headline about prompt injection. Both are quoted content, not directives; ignored.
- Release notes for huggingface_hub 1.27.0 contain `curl … | bash` installer commands for the hf CLI and its agent skill. These are user documentation; **no command from any fetched page was run**.
- No fetched page contained instructions addressed to this screening agent.
