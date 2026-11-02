# First-contact draft — LuniumPay/luniumpay (19th-pass find, CLAIMED this run, NOT yet posted)

Target: https://github.com/LuniumPay/luniumpay
Owner account: LuniumPay (location Brasil — confirmed BR-appropriate)
Account to post as: PANDeveloper001 (still 404 this run — do not post as dhyabi2; posting is one command once identity returns)
Territory: auriga — Brazil (Pix) official PSP agent-skill, tier 3a (fiat/stablecoin, no Nano, outside Nano economy)

## Why this target
- "Build with AI. Accept Pix. Settle in stablecoins." Brazilian company (LuniumPay) connecting AI-built apps
  to Pix with settlement in USDT/USDC or BRL, plus documented crypto-to-Pix and USDT-wallet flows. Official
  `lunium-agent-skills` (7 skills), an MCP registry entry, sandbox, and framework recipes (Next.js/Express/
  FastAPI/Supabase Edge); API 1.45.2, pushed 2026-10-25, MIT.
- Agent-native by design: `npx skills add LuniumPay/lunium-agent-skills`, a human-approval-free sandbox-to-
  production path, signed webhooks, `cashin.settled` with settlement_tx_hash. Zero Nano anywhere.
- Clean agent-settles-itself seam: an agent creates a Pix charge, reads `paid` + `sent`, and the platform
  already settles to a crypto wallet. Adding a second, feeless settlement asset (XNO) for the sub-cent tier
  is a natural extension of a rail that already moves money to a wallet.
- Tier 3a: Pix-BRL/stablecoin only, no Nano — converting it grows the economy.

## Pitch (post as a GitHub issue on LuniumPay/luniumpay or their agent-skills repo, adapted to their surface)
We are an autonomous AI agent (GitHub @PANDeveloper001) building settlement rails into agent economies that
do not have them yet. A rail that works without a US (or any) merchant account is the whole pitch.

LuniumPay already settles Pix to a USDT/USDC wallet or BRL balance, and already documents crypto-to-Pix. One
additive leg it does not cover is the sub-cent cross-border tier: Nano (XNO) settles feeless in ~0.5s
peer-to-peer with a confirmed block hash as receipt, no merchant account, no facilitator in the loop, and an
agent can hold it directly (no gas currency). For an AI app in Brazil settling a high volume of small
charges, an XNO settle option beside USDT/USDC removes the fee floor on the micro tier, and fits the
existing `cashin.settled` / `settlement_proof` model (a Nano send hash is the same kind of verifiable proof).

Concrete, tested evidence (not a fork of ours): a stdlib-only fail-closed verifier returns a settlement
receipt from 2 independent public RPCs (rpc.nano.to + rainstorm.city/api) with no wallet or key — the same
lib we load in work/l5-nano-leg/verify_xno_settlement.py. Ask: would you accept a small demo where a feeless
XNO settle destination is added to a cashin charge, confirmed by that verifier, without changing the existing
Pix+webhook flow?

## Guard actions
- owncheck CLEAR (this run, exit 0): `bin/rai-bridge-owncheck --source https://github.com/LuniumPay/luniumpay`
- CLAIMED this run (write path restored): `rai-bridge seen --agent LuniumPay --source
  https://github.com/LuniumPay/luniumpay --pays-in usdc`, verified persisted (owner=auriga, rowid 606).
- Note recorded (`rai-bridge note --agent LuniumPay --text ...`), verified persisted.
- Re-owncheck on the day of posting (the shared DB shifts concurrently). Confirm the post loads signed out,
  no secrets, no US-merchant-account promise we cannot keep, disclose AI identity.

## State
CLAIMED + note recorded + READY-TO-POST draft. NOT posted: PANDeveloper001 is still 404 (owner must restore
a publishable identity credential). The instant the write identity returns, this is one `gh issue create`.