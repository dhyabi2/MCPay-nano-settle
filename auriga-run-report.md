# Auriga run report — 2026-11-02 (sixteenth pass)

## This run: ROOT-CAUSED and FIXED the swarm-wide false "token dead / write wall down" alarm; discovered the real write blockers; 1 new territory lead found (kunwarshivam/mandate).

Tier 4/5 (self-improvement produced the highest value this run, because it unblocks tiers 1-3 for the WHOLE swarm):

- **FIXED `rai-prs` false "GitHub token dead (401/422)"** — the report that has banked 15 runs of drafts.
  Root cause: one stale malformed row in `outreach-tracker/data.json` (SeierkDev/Axon/issues/3, missing
  `title` and `created_at`). On the PANDeveloper001-search-422-skip retention path track.py re-added that
  row, render() threw KeyError, track.py exited 1, and its stderr carried the benign `422` (the "account
  invisible to search" warning). `classify_failure()` reads ANY stderr containing "422" as a revoked token
  → every member saw "write wall down". The token was NEVER dead: `gh` authenticates with live repo scope,
  and search returned 324 results. Fix: `render()` and the retention loop use `.get()` defaults; a malformed
  stale row can no longer masquerade as a dead token. Committed on `outreach-tracker` main (ed2f209) + a
  regression test (4842730). `rai-prs` now returns the truthful `nothing_changed` instead of the false alarm.
  (System note: `/usr/local/bin/rai-prs` itself could not be edited — `/` is remounted read-only — the fix
  lives in the checkout track.py it invokes.)

- **Verified the REAL write identity this run (supersedes the "effectively down" framing):**
  - `gh api user` → **dhyabi2** (id 32069256), classic token, live `repo` scope. GH writes MECHANICALLY work.
  - `gh api users/PANDeveloper001` → **404** — the sanctioned outreach account does not resolve / is not
    visible; no token on this box authenticates as it.
  - So publishing first contacts under our own name is genuinely blocked (posting as dhyabi2 = discarded
    history per run brief + OWNER-RULES #4). The owner must re-issue a PANDeveloper001 credential.
  - The run brief (and live brief-line) saying "GITHUB WRITE PATH: OPEN / post drafts upstream" is about the
    token's repo scope, NOT that the sanctioned account can publish. I did NOT brute-force post as dhyabi2.

- **NEW infra blocker found: the root filesystem is read-only** (`/` on ext4 `ro,errors=remount-ro`). `/root`
  is a SEPARATE rw mount, but `/srv` (bridge.db), `/usr/local/bin`, `/opt` are on the ro `/`. So even
  `rai-bridge seen/note` FAIL (`unable to open database file`) — claims cannot persist this run — and no
  `/usr/local/bin` tool edit is possible. Read-only `mode=ro` SQLite reads of the bridge DB work. auriga
  (uid 983) cannot remount; root/owner must.

- **Discovery (tier 0) still produced one new lead** via `bin/auriga-scan` layer 1 (seed 8→9):
  - **kunwarshivam/mandate** (IN, 3a) — Rust "autonomous agents on your own brokerage account, inside an
    enforceable mandate: deterministic risk enforcement, journaled decisions, human escalation."
    Created 2026-09, live homepage. Fits auriga India mandate/AA layer; NOT claimed this run (bridge DB
    write-blocked, so a claim could not persist — banked as a verified draft for the next run).
  - Drift correctly skipped: PayPal-AI-Hackathon (niu602/mandatepay, Abm32/errand) and DeFi/crypto-native
    mandate hits (FeeeeelixWong/mandatefi BNB, FlipLabsAI/signo-shield, tyche-institute, adeci, dino1x,
    roshpinacare-sys) — out of JP/KR/BR/IN territory.

## Who answered
Nobody. No outside reply; no publishable write identity (PANDeveloper001 404); bridge conversation refused on the builder box.

## What I learned
- A benign "422" in any tool's stderr is not a dead token. When a token-validation and a downstream tool
  coexist, the specific tagger and the general error line must not blur. The swarm burned 15 runs on this.
- The run brief's "GITHUB WRITE PATH: OPEN" refers to token scope, not account publishability. Verify the
  ACCOUNT (`gh api users/PANDeveloper001`) before trusting any "post it upstream" line.
- A read-only root fs quietly blocks `seen`/`note`/`/usr/local/bin` edits while `/root` work keeps succeeding —
  always test a bridge write readback before trusting "claimed".

## What blocks me
1. PANDeveloper001 account 404 → no publishable outreach identity (owner: re-issue a PANDeveloper001 classic
   repo-scope PAT or make the account visible).
2. Root filesystem read-only → bridge `seen`/`note` can't persist, `/usr/local/bin` tools uneditable
   (owner/root: remount `/` rw after checking `dmesg` for the remount-ro cause).
3. swarm-forge `issue`/`report` refused here (forge API 404 / no territory issue) — kept to local `.ledger/`

Full detail: `.ledger/run-report-auriga-2026-11-02-sixteenth-pass.md` · skill `auriga-territory-ops`