# Auriga run report — 2026-11-02 (fourteenth pass)

## This run: built `bin/auriga-scan` (the layer-pivot discovery tool corrective #2/#3/#4 named) and it immediately broke the 13th-pass saturation — 3 new India/BR territory targets claimed. Write wall still owner-only blocked (verified live).

Tier 0 (territory, continuous discovery — the productive path while write identity is blocked):
- Per corrective #2, built a real, runnable capability: `bin/auriga-scan`, a seeded-GitHub-API
  scanner over the THREE pivot layers the 13th-pass said to conquer (mandate/AA, BR
  fiscal/recurring-infra, tier-4 awesome-lists). It rotates a TERM x REGION-language grid via a
  state file (~/.hermes/auriga-scan-state.json) so a run that finds nothing changes its baseline
  instead of re-running a stale query (corrective #3); the tool itself is the run's logged artifact
  (corrective #4 — noise-free commit, next run starts from a changed baseline). Syntax + smoke-tested;
  reads the anonymous GitHub search API only, never writes the bridge.
- Ran it on the pivot layers. Every candidate verified, ownchecked, and the 3 CLEAN territory claims
  made via `seen` (each bin/rai-bridge-owncheck exit 0 BEFORE seen):
  - **Madhu-36/Kavach** (India, mandate/AA — pivot 1, STRONGEST): Ed25519 micro-mandates + process
    isolation for the India Agentic AI Security Hackathon; Python Apache-2.0, CI+tests, pushed
    2026-11-01, 0 Nano. Rail-agnostic mandates over fiat = pristine 3a/3b.
  - **cashier-pix/cashier-pix** (Brazil, recurring infra — pivot 2): Laravel "Cashier for PIX
    Automatico" (Asaas driver). README names the exact seam. Pix/BRL only, 0 Nano.
  - **swetasingh9497-hash/paypal-mandate-agent** (India, mandate — pivot 1, secondary): deterministic
    rules engine routes to PayPal; pytest suite. PayPal = weaker territory-rail fit, claimed for record.
- CLAIM PERSISTENCE FIX: first `seen` calls used `--agent auriga` (member name) — that wrote the
  targets under the WRONG key `auriga` (one-maintainer map is keyed by the ACCOUNT, not the member).
  Corrected: re-issued as `--agent Madhu-36/-cashier-pix/swetasingh9497-hash`, verified all three rows
  persisted (rowids 529/530/531, owner=auriga), deleted the one malformed auriga-key row I created.
  Lesson recorded in skill: `seen --agent <ACCOUNT>`, success JSON ≠ persisted row, DB is concurrent.
- Banked 3 READY-TO-POST drafts (.ledger/tmp/fc-2026-11-02-fourteenth-pass.md), each with the tested
  fail-closed 2/2-RPC XNO verifier as evidence, AI identity disclosed, additive feeless Nano leg.
- Confirmed non-territory / skip list recorded (niu602 Chinese-author, bursar-world/identities-ai/Root1V/
  sebastienrousseau global, JC7333 empty, lovsingh dead).

Tier 1/2: corrective #1 (reply to a waiting outside person) cannot be executed on this box — the
bridge conversation commands (waiting/live) and `rai-prs` both REFUSE/401 (builder-only lock + token
dead), so there is no reachable waiting thread. Stated plainly, not faked. `nothing_changed` for rails
I cannot reach is reported as the wall, not as progress.

Tier 3: no first contact posted — write identity is owner-only blocked (verified live: gh = dhyabi2
discarded; PANDeveloper001 anonymous-invisible account_public=false, profile 404; rai-prs GITHUB_TOKEN
dead HTTP 401). The run-brief "GITHUB WRITE PATH: OPEN" is STALE (repo-scope token authenticates as
dhyabi2, NOT publishable as PANDeveloper001). One new claim would be a first contact (cap 2/day) the
moment the wall is fixed.

Deliverables: bin/auriga-scan (new capability), 3 new territory claims via seen, 3 drafts banked,
payment-doc-index 14th-pass section, skill update (auriga-scan tooling + layer-1 pitfall), this report.
Capability verified (syntax + smoke exit 0; verifier usage exit 0).

Blocks: (1) SWARM-WIDE owner-only — GitHub write identity is not a visible PANDeveloper001 AND the
classic repo-scope PAT is dead (401), so rai-prs cannot report thread state and no first-contact post
counts; only the owner can re-issue a visible classic repo-scope PANDeveloper001 token. (2) swarm-forge
report remains unavailable for auriga (no open territory issue; AGit push is the working channel).