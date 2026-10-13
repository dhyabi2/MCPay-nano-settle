# MCPay-nano-settle — audit 2026-10-13

Audited at `0d2a28e`. Third audit (2026-10-01, 2026-10-05). **Still no XNO
settlement code in this repository**, and this note settles that conclusively
so a fourth audit is not needed.

## Nothing to run, and nothing has ever been here to run

The two earlier notes established that the tree holds no code. This run
established the stronger fact — **no code has ever been committed on any ref,
including commits since amended or rewritten away** — by enumerating the whole
object database rather than reading the ref tips:

```
$ git log --all --pretty=format: --name-only | sort -u | sed '/^$/d' | grep -v '\.md$'
(no output: every path ever committed is .md)

$ git cat-file --batch-all-objects --batch-check | awk '$2=="blob"' | wc -l
6                        # all six blobs are Markdown

$ git ls-tree -r --name-only origin/main
AGENTS.md
README.md
audits/MCPay-nano-settle-2026-10-01.md
audits/MCPay-nano-settle-2026-10-05.md
auriga-run-report.md
```

So there is no entry point, no amount handling, no verification and no
accept/refuse decision to read. A float on an amount, a `decimal` context too
short for raw, a payer-supplied value trusted over the ledger, and the
`CREATE TABLE IF NOT EXISTS` migration hazard are all impossible here by
absence rather than by argument: the pattern grep for amount arithmetic
(`parseFloat|toFixed|float|10**30|getcontext|Decimal|BigInt|to_raw|prec`) and
for any schema (`sqlite|CREATE TABLE|ALTER TABLE|migrat`) returns nothing
outside these audit notes.

No manifest, lockfile, build script or test exists, so `npm ci`, `npm test`,
`npm run build`, `make` and `unittest discover` all fail for want of a project,
and `pytest -q` exits 5, "no tests ran". **0 tests exist.** (One correction to
the 2026-10-05 note: it recorded `No module named pytest`; pytest is present in
this environment and reports "no tests ran". Same conclusion, different reason.)

## Secrets: clean, tree and full history

`git log --all -p` across all refs scanned for Nano/xrb account strings,
`sk-`, `ghp_`, `gho_`, `github_pat_`, `AKIA`, `xox[baprs]-`, PEM private-key
headers and JWTs: **zero hits.** The only two 64-hex strings are in
`auriga-run-report.md` and are public by design — a sha256 of a published pull
request diff, and a Nano settlement block hash with its amount, readable by
anyone on the public ledger. Nothing to rotate.

## The standing item, now with both halves of the evidence

What this repository actually holds is **another swarm's rules file**:
`README.md` is two lines, `# rai2` / "Rai2 swarm: rules, tools and the work",
and `AGENTS.md` is 64 KB of rai2 standing instructions. The first step a new
agent takes therefore fails — clone the repository the catalogue lists as the
XNO settle asset and you get rai2's rules.

That was raised on 2026-10-01. Both earlier notes listed the other half —
whether the catalogue still lists it, and in what words — as something they
could not verify, because the catalogue is not in this checkout. It is in a
sibling one, so it was verified this run:

- `swarm-decisions/TIER0.md:3173`, under `## Included - work only on these`,
  group 1 *Paying and settling in XNO*:
  `` - `MCPay-nano-settle` (private) - XNO settle asset beside USDC for the sub-cent tier ``
- `swarm-decisions/tier0.json`, `included` array, entry `dhyabi2/MCPay-nano-settle`.
  That file's header reads `"updated": "2026-10-03"` — the catalogue was
  refreshed two days *after* the mismatch was first raised and still carries the
  entry unchanged.

So this is a cataloguing decision, not a code defect, and it is the owner's:
either mark the entry the way `dual-rail` and `nano-finality-proof` were marked
while they were listed but unbuilt, or move the rai2 rules to their own
repository and let this name hold the settle asset. A routine does not edit
`TIER0.md` from a cloud run. Raised under `## Needs the owner` in the
2026-10-13 report and not acted on here.

**For future runs: do not spend a slot re-auditing this repository.** The
object-database enumeration above does not expire. Audit it again only once a
commit adds a non-Markdown file.

## Could not verify

- URL liveness. Of the real URLs in the tree, the session proxy denied egress
  to every non-GitHub host (`CONNECT tunnel failed, response 403`, confirmed as
  policy denials, not 404s), so **no 404 is claimed**. All of them sit in
  `AGENTS.md` and `auriga-run-report.md` — rai2's rules and run notes — not in
  any XNO payment documentation.
- Whether the MCPay XNO settle asset exists elsewhere: an unpushed branch,
  another account, or an unexported working tree. This note speaks only to this
  repository's 6 commits and 5 refs.
