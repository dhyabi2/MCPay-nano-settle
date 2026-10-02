# MCPay-nano-settle — audit 2026-10-01

First audit of this repository. Lens: can an agent settle an MCPay charge in XNO with this,
today? Tier 0 lists it in group 1 (paying and settling in XNO) as
"XNO settle asset beside USDC for the sub-cent tier".

## Checked

- Whole tree, all three files, and all four commits of history.
- Secret scan of tree and history.

## Found

**There is no XNO settlement code in this repository, and never has been.** The tree is:

```
AGENTS.md              893 lines
README.md                2 lines
auriga-run-report.md    83 lines
```

`git log --all --name-only` lists exactly those three paths across the whole history. The
repository was created on 2026-09-24 ("Initial commit", `e5e1c9c`) and its next commit the
same day was `4dd96ab` "Add rai2/AGENTS.md with territory, tier order and run protocol".

What the files actually contain is the **rai2 swarm's workspace rules and run reports** —
another swarm's operating instructions, which opens:

```
README.md:1  # rai2
README.md:2  Rai2 swarm: rules, tools and the work
AGENTS.md:1  # Rai workspace rules (~/nano-agent)
```

So an agent that reads `swarm-decisions/TIER0.md`, picks this entry as the way to settle an
MCPay charge in XNO and clones it finds no package, no module, no quickstart and no MCPay
integration — it finds a different swarm's AGENTS.md. That is the first step a new agent
would take, and it fails completely. **This is a cataloguing/misdirected-push problem, not a
code defect**: there is no code here to fix, and building the settle asset would be a new
feature, which is out of this routine's scope.

Two choices belong to the owner, and neither is one a cloud session should make
unilaterally, which is why this audit only records it:

1. If the rai2 workspace rules belong in their own repository, move them there and let this
   name hold the MCPay XNO settle asset it is listed as.
2. If the MCPay settle asset was never started (the history says it was not), the entry
   should leave Tier 0 `included` — or be marked the way `dual-rail` and `nano-finality-proof`
   are, as "listed but not yet created" — so routines stop selecting a repository with
   nothing in it to audit.

## No secret found

`AGENTS.md` mentions credentials only as **environment-variable names and CLI procedure** —
`VERCEL_TOKEN` and `ACCESS_<SERVICE>_KEY` in `~/.hermes/.env`, read over SSH by the owner.
No key, token, seed or password **value** appears in the tree or in any of the four commits.
The file in fact forbids the agent from ever requesting passwords, bank or card data, seed
phrases, wallet private keys or one-time codes. Nothing to rotate.

## Could not verify

Nothing was testable: there is no manifest, no dependency, no entry point and no test to
run. `npm`, `pytest` and `py_compile` have nothing to act on.
