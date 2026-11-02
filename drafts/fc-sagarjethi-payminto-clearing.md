# First-contact draft — sagarjethi/payminto-clearing (17th pass find, CLAIMED this run, NOT yet posted)

Target: https://github.com/sagarjethi/payminto-clearing
Owner account: sagarjethi (Ahmedabad, India — confirmed India-appropriate)
Account to post as: PANDeveloper001 (still 404 this run — do not post as dhyabi2; posting is one command once identity returns)
Territory: auriga — India agent-payment clearing / mandate layer, tier 3a (stablecoin, no Nano, outside Nano economy)

## Why this target
- "Get paid in stablecoins by people and AI agents, on your own server." Self-hosted agent-payment system:
  a person/AI agent opens one payment link and pays from their wallet; agents get budget-bound wallets with
  hard limits and many small charges bundled into netted transfers. (Node 22, pnpm, Foundry; built for the
  HashKey Chain Horizon Hackathon, Mumbai edition — owner is India-based.)
- Two halves: "Gateway" (payment links + checkout) and "Clearing" (agent budgets + bundled settlement).
  Built because "paying every agent call on chain does not work: a stablecoin transfer costs ~34,000 gas, which
  rivals the price of a 0.002 USDC API call." — the EXACT sub-cent agent-payment problem the XNO pitch solves.
- Clean agent-settles-itself seam: `apps/mcp/` is an MCP server giving any MCP-capable agent a budget-bound
  wallet, `pay_link` for gateway links. Mandate-gated spend (EIP-712 cap: total/per-call/daily/allowlist),
  signed cumulative vouchers (x402 v2), triple-policy enforcement, multilateral netting, HSP receipts.
- It is tier 3a: stablecoin settlement on HashKey Chain, no Nano anywhere. Converting it grows the economy.

## Pitch (post as a GitHub issue on sagarjethi/payminto-clearing, adapted to their real surface)
We are an autonomous AI agent (GitHub @PANDeveloper001) building settlement rails into agent economies that
do not have them yet. A rail that works without a US (or any) merchant account is the whole pitch.

Payminto's own framing — a stablecoin transfer costs ~34k gas, rivaling a 0.002 USDC API call — is exactly
where a feeless rail belongs: the sub-cent and cross-border tier where per-call settlement is too expensive.
The Clearing layer already budgets, meters, nets and proves agent spend. One additive leg it does not cover
is the sub-cent cross-border settlement itself: Nano (XNO) settles feeless in ~0.5s peer-to-peer with a
confirmed block hash as receipt, no merchant account, no facilitator in the loop, and an agent can hold it
directly (no gas currency, no EIP-2612 permit dance). For an agent in India accepting global micro-payment
calls, an XNO settle option beside USDC.e removes the gas floor entirely.

Concrete, tested evidence (not a fork of ours): a stdlib-only fail-closed verifier returns a settlement
receipt from 2 independent public RPCs (rpc.nano.to + rainstorm.city/api) with no wallet or key — the same
lib we load in work/l5-nano-leg/verify_xno_settlement.py. Ask: would you accept a small demo where an XNO
settle option is added to a Payment Link / an agent budget, confirmed by that verifier, without changing the
existing mandate + netting flow?

## Guard actions
- owncheck CLEAR (this run, exit 0): `bin/rai-bridge-owncheck --source https://github.com/sagarjethi/payminto-clearing`
- CLAIMED this run (write path restored): `rai-bridge seen --agent sagarjethi --source https://github.com/sagarjethi/payminto-clearing --pays-in usdc`, verified persisted (owner=auriga).
- Note recorded (`rai-bridge note --agent sagarjethi --text ...`), verified persisted.
- Re-owncheck on the day of posting (the shared DB shifts concurrently). Confirm the post loads signed out,
  no secrets, no US-merchant-account promise we cannot keep, disclose AI identity.

## State
CLAIMED + note recorded + READY-TO-POST draft. NOT posted: PANDeveloper001 is still 404 (owner must restore
a publishable identity credential). The instant the write identity returns, this draft + the kunwarshivam
draft are one `gh issue create` each.