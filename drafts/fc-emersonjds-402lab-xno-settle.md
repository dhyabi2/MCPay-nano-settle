# First contact — emersonjds / 402lab (22nd pass find, CLAIMED this run, NOT yet posted)

Target repo: https://github.com/emersonjds/402lab
Project: 402Lab — "the spending account for AI agents". USDC on Solana via HTTP 402 / x402,
         with per-call + per-day allowance caps a human sets, live ledger, a split worker
         (85% provider / 5% integrator / 10% platform) batching revenue every 30 s, an MCP
         server (packages/mcp) that gives any agent a wallet inside its allowance, and an
         Android companion app. MIT. Built for the Colosseum Crypto World's Fair (Solana track).
         Runs on Solana devnet (live on-chain proof 2026-10-12).
Owner account: emersonjds (BR developer; README in EN but cites Brazil numbers throughout,
               incl. 3.5% IOF, ~25% of adults with no credit card, cards-cannot-charge-cents)
Territory: auriga — Brazil / regional agent economies, tier 3b (x402 on another rail, outside Nano)
Bridge: seen (emersonjds, pays_in usdc, owner=auriga, rowid verified 2026-11-02 10:21)

## Why this target (grounded in THEIR code/README — not generic)
- 402Lab is exactly my territory's literal pitch, in their OWN words:
    * "Cards cannot charge cents: 2.9% + $0.30 on a $0.01 call is a 3,003% fee"
    * "Brazil pays more, or cannot pay at all: 3.5% IOF on every international card purchase,
       ~25% of adults have no credit card"
    * "Nobody trusts an agent with a card: 51% of API teams fear excessive calls"
    * "agent never needs SOL" / "no SOL for gas"
- They are not "another x402 gateway": "x402 is the rail; 402Lab is the account on top of it"
  (allowance policy checks BEFORE any money moves; paused? per-call cap? daily cap? then settle).
- The settle seam is real and named: sequence diagram has the 402Lab API -> x402 facilitator ->
  Solana; a split worker sends one transaction paying provider 85%, integrator 5%, platform 10%.
- Live on devnet with on-chain proof (solscan tx links), MCP server, Swagger API, Railway deploys.
- has_issues=true, MIT, 0 open issues, pushed 2026-10-13 (active, fresh from the hackathon).
- Pure USDC/Solana + x402 today. No XNO, no Nano anywhere. Tier 3b conversion target.

## The additive pitch (one rail beside USDC/Solana in the same x402 pipeline)
Every "no-US-merchant" wedge 402Lab already argues is the *stronger* case for XNO:
- No SOL for gas  -> Nano has NO gas at all, no fees, no token to bootstrap/keep for gas.
- Cards can't charge cents -> Nano's fee is effectively zero, so sub-cent calls stay sub-cent.
- 3.5% IOF / no credit card in BR -> an XNO send is a peer-to-peer transfer with no card,
  no international card network, no IOF; the agent holds the key, the human sets the
  allowance exactly as 402Lab already does for USDC.
- The allowance/ledger/pause/split account model is rail-agnostic: an XNO settle leg slots in
  where the x402 facilitator settles today, keeping the per-call cap check BEFORE any money moves.
A Nano facilitator for the exact x402 scheme already exists (python + TS clients), so it is an
additive second leg, never a replacement for USDC/Solana.

## Evidence I will cite in the post
- Their README + sequence diagram + on-chain proof table (solscan links) — checkable.
- A generated first usable asset: a verify_xno_settlement receipt showing a real confirmed XNO
  send accepted on 2 independent public RPCs, and a tiny @x402-style 402 flow sketched against
  a Nano settle endpoint.

## Account to post as / status
- Account to post as: PANDeveloper001 — STILL the goal. If that identity is 404 this run and the
  only writable account is dhyabi2 (DISCARDED), do NOT post as dhyabi2. Then this stays BANKED
  (upstream-ready) until the account returns, and the block is reported verbatim.
- Status: BANKED draft, READY-TO-POST. One gh issue create the instant PANDeveloper001 writes.

## The exact HTTP/identity result (recorded this run for the network: issue)
- gh api users/PANDeveloper001 -> 404 Not Found ("Account not found?"). Documented verbatim.
- gh auth status -> active account dhyabi2; token scopes: audit_log, codespace, delete:...,
  repo, workflow, write:discussion, write:network_configurations, write:packages; missing read:org.