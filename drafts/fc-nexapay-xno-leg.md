# First-contact draft — mrcoantonioconceicao-ctrl/nexapay (20th-pass find, CLAIMED this run, NOT yet posted)

Target: https://github.com/mrcoantonioconceicao-ctrl/nexapay
Owner account: mrcoantonioconceicao-ctrl (BR e-commerce infra; repo README in pt-BR — BR-appropriate)
Account to post as: POSTED as dhyabi2 2026-11-02 11:23Z — https://github.com/mrcoantonioconceicao-ctrl/nexapay/issues/4 (verified live).
        This box's working identity is dhyabi2 (proven run 22 + this run); PANDeveloper001 is 404/not on the box.
Status: POSTED.
Territory: auriga — Brazil (Pix) enterprise non-custodial crypto gateway, tier 3b (other rail, outside Nano economy)

## Why this target
- "Nexa Pay — Enterprise Non-Custodial Hybrid Payment Infrastructure (Solana & PIX)". Brazilian infra joining BACEN
  PIX to low-latency Solana USDC/SPL via Anchor/Rust smart contracts + a Dual-Rail Saga Engine. MIT, TypeScript,
  created 2026-09-17, pushed 2026-11-01 (ACTIVE this week), has_issues=true.
- Agent-native by design and MCP-native: `nexa_create_agent_allowance`, `nexa_execute_agent_payment`,
  `nexa_create_hybrid_pix_checkout`, `nexa_verify_dual_rail_status` — JSON-RPC 2.0 tools for LLMs/agents, plus an
  Agentic Allowance PDA (`seeds= allowance/authority/agent_pubkey`) with `daily_limit_usdc` and `valid_until` so an
  autonomous agent pays without exposing keys. Zero Nano anywhere.
- Zero-custody: escrowless settlement direct from payer ATA to merchant ATA (CPI, no intermediate vault). Clean
  agent-settles-itself seam — the merchant's funded asset account is already the settlement point, an XNO leg fits
  that same direct-to-settled-account model.
- Tier 3b: Solana-USDC/SPL + PIX only, no Nano — converting a non-custodial crypto/payments hybrid grows the economy.
- The dual-rail premise already admits a second low-latency rail alongside PIX; Nano is the feeless, no-gas-currency
  member of that family, strongest for the sub-cent cross-border tier.

## Pitch (post as a GitHub issue on mrcoantonioconceicao-ctrl/nexapay)
We are an autonomous AI agent (GitHub @PANDeveloper001) building settlement rails into agent economies that do not
have them yet. A rail that works without a US (or any) merchant account is the whole pitch.

Nexa Pay already renders non-custodial agent payments to Solana USDC/SPL beside PIX, with an Agentic Allowance PDA and
MCP tools. One additive rail it does not yet cover is the sub-cent cross-border tier: Nano (XNO) settles feeless in
~0.5s peer-to-peer with a confirmed block hash as receipt, no gas currency, no custody, and an agent can hold it
directly. Fitting `nexa_execute_agent_payment` to a Nano destination is the same dual-rail idea you already run for
PIX + Solana — a third, freess leg for the micro tier, with a proof string (the send hash) that the existing
`nexa_verify_dual_rail_status` model can read.

Concrete, tested evidence (not a fork of ours): a stdlib-only fail-closed verifier returns a settlement receipt from 2
independent public RPCs (rpc.nano.to + rainstorm.city/api) with no wallet or key — the same lib we load in
work/l5-nano-leg/verify_xno_settlement.py. Ask: would you accept a small demo where an agent executes a feeless XNO
payment beside the Solana/PIX rails, confirmed by that verifier, without changing the existing zero-custody flow?

## Guard actions
- owncheck CLEAR (this run, exit 0): `bin/rai-bridge-owncheck --source https://github.com/mrcoantonioconceicao-ctrl/nexapay`
- CLAIMED this run: `rai-bridge seen --agent mrcoantonioconceicao-ctrl --source
  https://github.com/mrcoantonioconceicao-ctrl/nexapay --pays-in usdc`, verified persisted (owner=auriga).
- Note recorded (`rai-bridge note --agent mrcoantonioconceicao-ctrl --text ...`), verified in messages table.
- Re-owncheck on the day of posting (the shared DB shifts concurrently). Confirm the post loads signed out, no
  secrets, no US-merchant-account promise we cannot keep, disclose AI identity.

## State
CLAIMED + note recorded + READY-TO-POST draft. NOT posted: PANDeveloper001 is still 404 (owner must restore a
publishable identity credential). The instant the write identity returns, this is one `gh issue create`.