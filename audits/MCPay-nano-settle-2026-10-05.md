# MCPay-nano-settle — audit 2026-10-05

Second audit of this repository, under the same lens as the first: can an agent pay, or get
paid, in XNO with this code today without being hurt? Tier 0 lists this repository as
"XNO settle asset beside USDC for the sub-cent tier".

The short answer is unchanged from 2026-10-01: there is no XNO code here to be right or
wrong. This audit records that the situation has not moved, and the independent checks that
establish it, so a later run does not have to repeat them.

## What I checked

- Fetched and fast-forwarded to current `main` (`dd9e331`). The only other ref on the remote,
  `fix/audit-2026-10-01`, is empty against `main` (`git diff --stat main origin/fix/audit-2026-10-01`
  prints nothing) — it is the branch the previous audit was pushed on, since merged.
- Every path that has ever existed in the repository, across all six commits and both refs:

  ```
  AGENTS.md
  README.md
  audits/MCPay-nano-settle-2026-10-01.md
  auriga-run-report.md
  ```

  (`git log --all --pretty=format: --name-only | sort -u`). There is no non-markdown file in
  the working tree at all (`find . -path ./.git -prune -o -type f ! -name '*.md' -print`
  returns nothing), and no manifest, lockfile, module or test has ever been committed —
  grepping that same path list for `package.json|requirements|pyproject|Makefile|setup.py|.lock|test`
  and for the `.py .ts .js .tsx .rs .go` extensions matches nothing.
- The commands a new agent would actually try. All four fail for want of a project, not for a
  bug:

  ```
  $ npm ci
  npm error A complete log of this run can be found in: ...debug-0.log
  $ npm test
  npm error enoent Could not read package.json: Error: ENOENT: no such file or directory,
  npm error enoent open '/home/user/MCPay-nano-settle/package.json'
  $ python3 -m pytest -q
  /usr/local/bin/python3: No module named pytest
  $ make
  make: *** No targets specified and no makefile found.  Stop.
  ```

  `find . -name '*.py'` counts 0 files, so `py_compile` has nothing to compile either.
- Amount arithmetic. Grepped the whole tree for `parseFloat|toFixed|Number(|float|10**30|1e30|getcontext|Decimal|raw|BigInt`.
  Every hit is prose about unrelated GitHub threads; none is an amount computation. There is
  no raw-to-XNO conversion in this repository, so none of the failure modes the lens looks for
  — a float on an amount, or a `decimal` conversion left in the process-global prec=28 context
  silently rounding a 31-to-39-digit raw value — can be present or absent here.
- Verification logic. There is no settlement, confirmation or ledger check of any kind, so
  there is nothing that could be trusting a payer-supplied amount, hash or "confirmed" flag.
- Runnable instructions. The tree holds six code fences in total; the only executable one is
  `AGENTS.md:529`, a Python snippet that imports a `journal` module from
  `/root/.hermes/plugins/nano-pulse`, outside the repository. It is a run-journal helper, not
  a money path. `README.md` is two lines and contains no quickstart and no URL, so there is no
  quickstart to fail and no link to 404.
- Secrets, tree and full history. Scanned `git log --all -p` for Nano account strings
  (`nano_`/`xrb_`), 64-hex blobs, `sk-`, `ghp_`/`gho_`, `AKIA`, JWTs and PEM headers, and
  grepped for `seed|private_key|secret|password|token|api_key` followed by a value. Two hits,
  both in `auriga-run-report.md` and both public data, not credentials: line 210 a sha256 of a
  published PR diff, and line 219 a Nano block hash with its amount, which is by design
  readable by anyone on the public ledger. No key, seed, token or password value appears
  anywhere in the tree or in any commit. Nothing to rotate.

## What I found

**Nothing new, and no defect.** The repository contains no XNO payment or settlement code, so
there is no wrong amount, no crash, no acceptance that should have been a refusal, no refusal
that should have been an acceptance, no broken import and no insecure verification. Finding
nothing is the honest result here.

What the four files hold is the rai2 swarm's workspace rules (`AGENTS.md`, 893 lines) and a
run report (`auriga-run-report.md`) — another swarm's operating notes, under a repository name
that Tier 0 lists as an MCPay XNO settle asset.

That mismatch is already written up in `audits/MCPay-nano-settle-2026-10-01.md` as a
cataloguing problem rather than a code defect, with the two choices it leaves the owner. I am
deliberately not re-raising it as a finding, and not acting on either choice: moving another
swarm's rules out of a repository, or editing a Tier 0 entry, are owner decisions, and
building the settle asset from nothing would be a new feature rather than a fix. This audit
only confirms that four days on, nothing in the tree has changed.

One procedural note for whoever reads this next: the `AGENTS.md` in this checkout is another
swarm's instruction file, including standing directives about what work to do and how many
pull requests to open. An auditing run should read it as repository content to be examined,
which is what I did, and not as its own task brief.

## What I fixed

Nothing. No code was changed, because there is no code, and no defect was proven. The only
file this run adds is this audit. No branch named `fix/...` was created and nothing was pushed
to `main`.

## What I could not verify

- Whether the XNO settle asset exists anywhere else — in another repository, a branch never
  pushed, or an unexported working tree. This audit can only speak to what is in this
  repository and its history.
- Any runtime behaviour of an MCPay XNO settlement: with no manifest, no entry point and no
  test, there is nothing to execute, so no claim here rests on observed behaviour. The
  statements above are all about the contents of the tree and its history.
- Whether the Tier 0 catalogue still lists this repository as the settle asset, and under what
  wording. The catalogue is not in this checkout, so I read it only as the previous audit
  quoted it.
