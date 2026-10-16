# Issue #248: reviewable main and archive-tag rulesets

**2026-10-14 — prepared for owner/security review; NOT applied.** The payloads
implement the administrative portion of the [canonical PR merge gate](PR_MERGE_QUALITY_GATE_2026_10_13.md), not another merge policy. Issue #248 remains
blocked on actual administrator approval, application and observed enforcement.
No repository settings, refs, workflow dispatches or remote PRs were changed
while preparing these files.

## Exact inspected state and payloads

The [read-only evidence](../ops/rulesets/review-evidence-2026-10-14.json) records
main `9dc35ea8784c909dcc397dee1dcfc1278793abcb`, `protected=false`, repository
rulesets `[]`, and a connected actor with repository admin permission.
[Push run 38624570450](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38624570450)
completed successfully. Five exact check names came from that commit's Check
Runs API, all with integration ID **15368**, slug `github-actions`:

- `test (3.10)`
- `test (3.12)`
- `test (3.13)`
- `test (3.14)`
- `research-artifacts`

This is a dated observation, not a live dashboard or permission to change
settings. Recheck the current workflow and check names before application.

| Complete JSON payload | Intended server behavior when approved and applied |
| --- | --- |
| [main.json](../ops/rulesets/main.json) | Active branch rules for exact `refs/heads/main`; PR required, one approving review, stale-review dismissal, approval of the latest reviewable push by somebody other than its pusher, resolved conversations, all five GitHub Actions checks and strict latest-base checks; force pushes and deletion forbidden; no bypass actors |
| [branch-archive-tags.json](../ops/rulesets/branch-archive-tags.json) | Active rules for `refs/tags/branch-archive/**/*`; updates and deletion forbidden with no bypass actors; creation is not prohibited by this ruleset |

The main payload retains the repository's observed merge/squash/rebase methods.
Code-owner approval is false because no qualified CODEOWNERS assignment has
been reviewed; the one-review rule remains mandatory. A GitHub approval count
cannot establish scientific expertise or actual independent source review.
Strict status checks require current integration tests; no merge queue is
introduced. The workflow and manual policy still require fresh exact-head and
post-merge CI evidence.

**Solo-maintainer effect:** the PR author cannot satisfy the required approval
with self-review; the latest pusher also needs someone else's approval. Even a
repository administrator has no configured merge/ref bypass in these payloads.
An eligible separate collaborator must review before normal integration can
continue. Do not silently lower these requirements to make an agent-authored PR
mergeable. Administrators retain the ability to edit settings; an empty bypass
list is not proof that the owner cannot change the rules.

The archive rules allow new recovery tags but do not authorize creating them,
retiring a branch or enabling deletion. The existing retirement safety hold,
qualified security review, approved SHA-pinned plan and verified recovery
requirements remain in force. An `update` rule is deliberately absent from
main because it would restrict ordinary PR merges to bypass actors; PR-only
integration is enforced by the `pull_request` rule instead.

## Archive pattern and pagination compatibility

GitHub's official [ruleset targeting documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#using-fnmatch-syntax)
uses Ruby `File.fnmatch` with `File::FNM_PATHNAME`: a `*` wildcard does not
match `/`. Its explicit recursive example is `qa/**/*` for names containing
any number of slashes after `qa`. The official
[`about-fnmatch` source blob](https://api.github.com/repos/github/docs/git/blobs/bd3f0a7f9158d4942665099bbc8f1ee045557927)
was read and its Git blob SHA verified. Accordingly the tag payload uses
**`refs/tags/branch-archive/**/*`**, rather than a bare trailing `**` that can
miss nested archive paths. Read-only inspection found 59 current archive refs,
all nested as `refs/tags/branch-archive/<date>/<category>/<branch>`; the
recursive pattern covers their intended prefix/path layout. This documented
matching check is not a production server enforcement test. New nested names
under that prefix receive the same intended protection; creation stays allowed.

The runbook supports the installed `gh 2.46.0`, which has `--paginate` but no
`--slurp`. Paginated responses are saved as `.json-stream` files; Python's
`JSONDecoder.raw_decode` consumes each adjacent page array and stores a normal
JSON array-of-pages for review. Malformed or non-array pages fail. The entire
read-only preflight, including fresh repository/main/rules/check/workflow GETs
and all assertions, was executed successfully with that CLI version.

## Authoritative API schema

Payload fields were checked against GitHub's official
[`github/rest-api-description` OpenAPI Git blob](https://api.github.com/repos/github/rest-api-description/git/blobs/541d9c23ff62c59bc9e2e071346d14210555b56c),
`descriptions/api.github.com/api.github.com.json`, blob SHA
`541d9c23ff62c59bc9e2e071346d14210555b56c`; the downloaded Git blob hash was
verified. Relevant schemas are `POST /repos/{owner}/{repo}/rulesets`,
`repository-rule-pull-request`, `repository-rule-required-status-checks`,
`repository-rule-params-status-check-configuration`,
`repository-rule-update`, `repository-rule-deletion`,
`repository-rule-non-fast-forward` and `repository-ruleset-conditions`.
The official schema includes `require_last_push_approval` and
`strict_required_status_checks_policy`. No beta required-reviewer configuration
or guessed Actions integration ID is used.

The [REST reference](https://docs.github.com/en/rest/repos/rules#create-a-repository-ruleset)
is also the administrator's endpoint guide. The documentation site returned
HTTP 403 in this environment; the authoritative OpenAPI source was read via
GitHub's read-only Git Blob API instead. Offline schema validation does not
prove GitHub will accept the payload for a particular account/plan or that a
rule rejected an attempted update.

## Administrator preflight — read-only

The following commands are a reviewable future operator procedure. They were
**not run as an administrative mutation** by the preparation agent. Run from
a checkout containing the reviewed payloads. Use existing secure `gh`
authentication; never print tokens or save credentials in these files.

**2026-10-16 correction:** The dated `9dc35ea...` SHA in the original
evidence above is a historical snapshot, **not** an executable pin for future
operations. Before each administrator session, independently inspect current
`main`, the exact workflow/check integration IDs, inherited rules and the two
unchanged payload blobs. Only after qualified security/owner review, export
`RULESET_EXPECTED_MAIN_SHA` to the **40-character commit SHA the administrator
actually reviewed**. Do not populate this variable automatically from a new
live GET: a moving value would defeat the stale-state stop gate. A new main
commit requires a new approval/readback decision; no secret or token belongs
in this document.

```bash
set -euo pipefail
ruleset_repo=MSKazemi/github-trending-1000-study
: "${RULESET_EXPECTED_MAIN_SHA:?export the independently reviewed 40-hex main SHA before preflight}"
export RULESET_EXPECTED_MAIN_SHA
ruleset_audit=$(mktemp -d /tmp/github-ruleset-review.XXXXXX)
gh api --method GET -H 'X-GitHub-Api-Version: 2022-11-28' \
  "repos/$ruleset_repo" > "$ruleset_audit/repository-before.json"
gh api --method GET -H 'X-GitHub-Api-Version: 2022-11-28' \
  "repos/$ruleset_repo/branches/main" > "$ruleset_audit/main-before.json"
gh api --method GET -H 'X-GitHub-Api-Version: 2022-11-28' \
  "repos/$ruleset_repo/rulesets?includes_parents=true&per_page=100" \
  --paginate > "$ruleset_audit/rulesets-before.json-stream"
python - "$ruleset_audit" <<'PY'
import json, os, pathlib, re, sys
root = pathlib.Path(sys.argv[1])
repo = json.loads((root / 'repository-before.json').read_text())
main = json.loads((root / 'main-before.json').read_text())
# gh 2.46 --paginate emits adjacent JSON page arrays, not one JSON array.
raw = (root / 'rulesets-before.json-stream').read_text()
decoder, pages = json.JSONDecoder(), []
while raw.strip():
    raw = raw.lstrip()
    page, offset = decoder.raw_decode(raw)
    assert isinstance(page, list), 'Unexpected ruleset pagination shape'
    pages.append(page)
    raw = raw[offset:]
assert pages, 'No pagination response'
(root / 'rulesets-before-pages.json').write_text(json.dumps(pages, indent=2) + '\n')
assert repo['permissions']['admin'] is True, 'Administrator access required'
assert repo['default_branch'] == 'main', 'Review changed default-branch scope'
assert main['protected'] is False, 'Review existing/composed protection first'
assert not any(pages), 'Review existing/inherited rules; never replace them blindly'
expected_sha = os.environ["RULESET_EXPECTED_MAIN_SHA"]
assert re.fullmatch(r"[0-9a-f]{40}", expected_sha), "Expected main SHA must be 40 lowercase hex characters"
assert main['commit']['sha'] == expected_sha, 'Reviewed main moved; re-review before application'
print(main['commit']['sha'])
PY
```

If any assertion fails, stop and refresh the review rather than overwrite a
changed state. Save the current main workflow, checks, reviews, permission and
ruleset evidence. With the independently pinned and verified main SHA
printed above, inspect fresh checks and the exact workflow:

```bash
gh api --method GET \
  "repos/$ruleset_repo/commits/$RULESET_EXPECTED_MAIN_SHA/check-runs?per_page=100" \
  > "$ruleset_audit/checks-before.json"
gh api --method GET \
  "repos/$ruleset_repo/contents/.github/workflows/ci.yml?ref=$RULESET_EXPECTED_MAIN_SHA" \
  > "$ruleset_audit/workflow-before.json"
python - "$ruleset_audit/checks-before.json" <<'PY'
import json, os, sys
checks = json.load(open(sys.argv[1]))['check_runs']
expected = {'test (3.10)', 'test (3.12)', 'test (3.13)', 'test (3.14)', 'research-artifacts'}
assert len(checks) == 5 and {c['name'] for c in checks} == expected
assert all(c['head_sha'] == os.environ["RULESET_EXPECTED_MAIN_SHA"] and
           c['app']['id'] == 15368 and c['app']['slug'] == 'github-actions' and
           c['status'] == 'completed' and c['conclusion'] == 'success' for c in checks)
PY
```

## Apply only after explicit owner/security review

Do not continue after a failed preflight or with an unset/guessed
`RULESET_EXPECTED_MAIN_SHA`. Directly before the **first** privileged POST,
recheck that main is unchanged and that no other ruleset appeared. Both checks
must fail closed; this narrows (but cannot eliminate) concurrent changes:

```bash
actual_main_sha=$(gh api --method GET "repos/$ruleset_repo/branches/main" --jq '.commit.sha')
test "$actual_main_sha" = "$RULESET_EXPECTED_MAIN_SHA" || {
  printf '%s\n' 'main changed since qualified review: stop' >&2
  exit 1
}
gh api --method GET "repos/$ruleset_repo/rulesets?includes_parents=true&per_page=100" \
  --paginate > "$ruleset_audit/rulesets-before-apply.json-stream"
python - "$ruleset_audit/rulesets-before-apply.json-stream" <<'PY'
import json, pathlib, sys
raw = pathlib.Path(sys.argv[1]).read_text()
decoder, pages = json.JSONDecoder(), []
while raw.strip():
    page, n = decoder.raw_decode(raw.lstrip())
    assert isinstance(page, list), "Unexpected ruleset page shape"
    pages.append(page)
    raw = raw.lstrip()[n:]
assert pages and not any(pages), "Ruleset state changed: stop for independent re-review"
PY
```


Record the approved payload commit, reviewer, change/incident reference,
planned review window and recovery plan outside this public repository.
Application requires a deliberate administrator decision because these active
rules will immediately restrict normal integration and archive updates.
Neither admin permission nor the maintenance request supplies the independent
security review required by the repository's governance issue.

Apply archive protection first, then main. Calls are separate operations;
there is no atomic pair transaction. If the second call fails, retain the first
response and inspect the partial state. Do not repeat POST blindly and create
duplicate rulesets. Use complete response files to capture newly allocated IDs:

```bash
gh api --method POST -H 'X-GitHub-Api-Version: 2022-11-28' \
  "repos/$ruleset_repo/rulesets" --input ops/rulesets/branch-archive-tags.json \
  > "$ruleset_audit/archive-created.json"
# Separate pre-main gate: confirm the same reviewed main and only the archive
# ruleset just created in this recorded transaction. Do not create main if
# the archive response is missing/invalid or if another ruleset appeared.
actual_main_sha=$(gh api --method GET "repos/$ruleset_repo/branches/main" --jq '.commit.sha')
test "$actual_main_sha" = "$RULESET_EXPECTED_MAIN_SHA" || {
  printf '%s\n' 'main changed after archive protection: stop' >&2
  exit 1
}
gh api --method GET "repos/$ruleset_repo/rulesets?includes_parents=true&per_page=100" \
  --paginate > "$ruleset_audit/rulesets-after-archive.json-stream"
python - "$ruleset_audit/rulesets-after-archive.json-stream" "$ruleset_audit/archive-created.json" <<'PY'
import json, pathlib, sys
raw = pathlib.Path(sys.argv[1]).read_text()
created = json.loads(pathlib.Path(sys.argv[2]).read_text())
assert type(created.get("id")) is int and created["id"] > 0
decoder, pages = json.JSONDecoder(), []
while raw.strip():
    page, n = decoder.raw_decode(raw.lstrip())
    assert isinstance(page, list), "Unexpected ruleset page shape"
    pages.append(page)
    raw = raw.lstrip()[n:]
assert pages
found = [item for page in pages for item in page]
assert len(found) == 1 and found[0]["id"] == created["id"], (
    "Archive ruleset state changed: stop before main POST"
)
PY
gh api --method POST -H 'X-GitHub-Api-Version: 2022-11-28' \
  "repos/$ruleset_repo/rulesets" --input ops/rulesets/main.json \
  > "$ruleset_audit/main-created.json"
python - "$ruleset_audit" <<'PY'
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
for name, expected_target in [('archive', 'tag'), ('main', 'branch')]:
    result = json.loads((root / f'{name}-created.json').read_text())
    ident = result['id']
    assert type(ident) is int and ident > 0
    assert result['target'] == expected_target and result['enforcement'] == 'active'
    (root / f'{name}-ruleset-id.txt').write_text(str(ident) + '\n')
PY
```

If a response is lost, query the complete live list and identify the new
ruleset by repository, exact name, target and reviewed fields; require an
administrator to reconcile duplicates before doing anything further. Never
infer a ruleset ID from a name alone or copy an old ID from this document.

## Get and verify the created rulesets

Recover IDs from the operation's saved response; no IDs are prefilled here:

```bash
main_ruleset_id=$(python -c 'import json,sys; x=json.load(open(sys.argv[1]))["id"]; assert type(x) is int and x>0; print(x)' "$ruleset_audit/main-created.json")
archive_ruleset_id=$(python -c 'import json,sys; x=json.load(open(sys.argv[1]))["id"]; assert type(x) is int and x>0; print(x)' "$ruleset_audit/archive-created.json")
gh api --method GET "repos/$ruleset_repo/rulesets/$main_ruleset_id" \
  > "$ruleset_audit/main-after.json"
gh api --method GET "repos/$ruleset_repo/rulesets/$archive_ruleset_id" \
  > "$ruleset_audit/archive-after.json"
gh api --method GET "repos/$ruleset_repo/rules/branches/main" \
  > "$ruleset_audit/effective-main-rules.json"
gh api --method GET "repos/$ruleset_repo/branches/main" \
  > "$ruleset_audit/main-after-branch.json"
python - "$ruleset_audit" <<'PY'
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
for name, payload_name in [('main', 'main.json'), ('archive', 'branch-archive-tags.json')]:
    expected = json.loads((pathlib.Path('ops/rulesets') / payload_name).read_text())
    actual = json.loads((root / f'{name}-after.json').read_text())
    assert actual['bypass_actors'] == []
    for field in ('name', 'target', 'enforcement', 'conditions', 'rules'):
        assert actual[field] == expected[field], f'Review server normalization or changed {field}'
assert json.loads((root / 'main-after-branch.json').read_text())['protected'] is True
PY
```

Rule order/default normalization can differ in the response; if the strict
comparison stops, inspect it against the intended semantics rather than
loosening a field silently. GET metadata or `protected=true` alone does not
prove enforcement. Save both IDs, payload/commit hashes, GET responses,
effective main rules, verification actors and test results as the admin audit.

## Manual negative verification — do not execute during preparation

An authorized administrator must choose disposable verification refs/PRs,
independent reviewers and an approved recovery plan before testing. Keep the
retirement workflow disabled. Never make uncontrolled force/delete attempts on
main or irreplaceable archive tags merely to discover whether protection works.
Where using a disposable repository/ref with copied rules, record that this is
not direct proof that the production target rejected the same attempt; combine
it with production scope/effective-rule checks and explicitly retain any
untested production requirement as pending.

| Case | Required observation and retained evidence |
| --- | --- |
| Missing independent approval | An authorized throwaway PR with no qualifying review is rejected; retain exact head/base SHAs, merge attempt result and rule ID |
| Latest-push/stale approval | After a qualified approval, append a new reviewable commit; old approval must not suffice, and approval from the latest pusher cannot satisfy the latest-push requirement |
| Failed/missing required check | Make a designated test check fail or remain absent; the merge attempt must be rejected, including a result from the wrong integration ID |
| Base advanced | Advance the test base through its approved PR flow; stale branch/check success must not suffice until refreshed integration checks pass |
| Unresolved conversation | An outstanding review thread blocks merge even when CI and approval otherwise pass |
| Direct push / force / deletion | Under a separately approved disposable-ref plan, observe rejection of a direct update, history rewrite and ref deletion; preserve actual server errors, not only client dry-run output |
| Archive immutability | Create one explicitly approved sacrificial tag under `branch-archive/**/*` at a known commit; record allowed creation, then observe rejection of its update and deletion, including admin-without-bypass behavior |
| Positive path | A genuinely independently reviewed, current-head/current-base passing non-draft throwaway PR succeeds through the permitted merge method; confirm post-merge push CI separately |

Pre-adjudicate what each test may change and restore. Save rejected server
responses, exact identities/SHAs, check/app IDs, actual approval/thread state,
rule IDs and timestamps. An unexpected successful destructive operation is an
incident: stop, preserve evidence and follow the approved recovery plan. An
agent-generated checkbox, local mock or an API GET never counts as an observed
negative enforcement result.

## Rollback and emergency owner policy

There is **no permanent admin bypass** in the payloads. Any emergency exception
needs a separately authorized, logged incident: reason, owner and independent
security reviewer where available, exact affected rule IDs/fields, shortest
expiry, preserved refs/CI evidence, permitted actions and mandatory restoration
plus follow-up review. Do not add a wildcard actor or permanent bypass as a
routine workaround for solo-maintainer review. Ruleset-edit access itself
remains a powerful owner/admin capability and must be governed outside code.

Rollback removes protection and is another explicit administrator decision.
Freeze ref/retirement operations first. Read the current rulesets and compare
with the operation's saved responses; if somebody changed either ruleset,
stop and review rather than delete their changes. Remove **only** the IDs
created by this recorded operation, never all rulesets or an inherited rule:

```bash
# After separate rollback approval and current-ID/current-content review:
gh api --method GET "repos/$ruleset_repo/rulesets/$main_ruleset_id" \
  > "$ruleset_audit/main-before-rollback.json"
gh api --method GET "repos/$ruleset_repo/rulesets/$archive_ruleset_id" \
  > "$ruleset_audit/archive-before-rollback.json"
# The administrator reviews these against main-created.json/archive-created.json.
gh api --method DELETE "repos/$ruleset_repo/rulesets/$main_ruleset_id"
gh api --method DELETE "repos/$ruleset_repo/rulesets/$archive_ruleset_id"
gh api --method GET "repos/$ruleset_repo/rulesets?includes_parents=true&per_page=100" \
  --paginate > "$ruleset_audit/rulesets-after-rollback.json-stream"
python - "$ruleset_audit" <<'PY'
import json, pathlib, sys
root = pathlib.Path(sys.argv[1])
raw = (root / 'rulesets-after-rollback.json-stream').read_text()
decoder, pages = json.JSONDecoder(), []
while raw.strip():
    raw = raw.lstrip()
    page, offset = decoder.raw_decode(raw)
    assert isinstance(page, list), 'Unexpected ruleset pagination shape'
    pages.append(page)
    raw = raw[offset:]
assert pages, 'No pagination response'
(root / 'rulesets-after-rollback-pages.json').write_text(json.dumps(pages, indent=2) + '\n')
PY
gh api --method GET "repos/$ruleset_repo/branches/main" \
  > "$ruleset_audit/main-after-rollback.json"
```

Partial application/rollback must be reconciled using the actual saved IDs and
GET responses. Leave unrelated existing protections intact. At the inspected
empty-ruleset baseline, deleting these new protections may return main and
archive tags to an unprotected state; report that explicitly. Preserve any new
archive tags and their original SHAs even if the rules are removed. Do not
close #248 until actual owner review, successful application and required
negative/positive server-enforcement evidence are complete.
