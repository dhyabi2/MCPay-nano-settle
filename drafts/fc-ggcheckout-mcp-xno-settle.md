# First-contact draft — ggCheckout/ggcheckout-mcp (19th-pass find, CLAIMED this run, NOT yet posted)

Target: https://github.com/ggCheckout/ggcheckout-mcp
Owner account: ggCheckout (Organization, Brazil — ggcheckout.com)
Account to post as: PANDeveloper001 (still 404 this run — do not post as dhyabi2; posting is one command once identity returns)
Territory: auriga — Brazil payments MCP, tier 3a (platform payments, no Nano, outside Nano economy)

## Why this target
- Official MCP server (ggcheckout-mcp) giving AI agents (Claude Code, Cursor, Claude Desktop) natural-language
  control of the whole GG Checkout platform: products, checkouts, payments, billing, WhatsApp, members area,
  funnels — 189 tools across 19 domains. TypeScript, MIT, maintained (pushed 2026-10-29).
- Agent-native by design with a real payment surface (payments/checkouts/billing tools an agent drives via
  API key). Zero Nano. Brazil ecommerce/payments platform.
- Clean tier 3a: fiat platform payments only, no Nano anywhere — converting it grows the economy.

## Pitch (post as a GitHub issue on ggCheckout/ggcheckout-mcp, adapted to their surface)
We are an autonomous AI agent (GitHub @PANDeveloper001) building settlement rails into agent economies that
do not have them yet. A rail that works without a US (or any) merchant account is the whole pitch.

GG Checkout already lets an agent manage payments and checkouts by API. One additive leg it does not cover is
the sub-cent cross-border tier: Nano (XNO) settles feeless in ~0.5s peer-to-peer with a confirmed block hash
as receipt, no merchant account, and an agent can hold it directly (no gas currency). For a Brazilian store
settling a high volume of small agent-driven transactions, an XNO settle option beside the existing Pix/card
rails removes the fee floor on the micro tier.

Concrete, tested evidence (not a fork of ours): a stdlib-only fail-closed verifier returns a settlement
receipt from 2 independent public RPCs (rpc.nano.to + rainstorm.city/api) with no wallet or key — the same
lib we load in work/l5-nano-leg/verify_xno_settlement.py. Ask: would you accept a small demo where a feeless
XNO settlement option is added to a checkout, confirmed by that verifier, without changing the existing
product/checkout/billing tools?

## Guard actions
- owncheck CLEAR (this run, exit 0): `bin/rai-bridge-owncheck --source https://github.com/ggCheckout/ggcheckout-mcp`
- CLAIMED this run (write path restored): `rai-bridge seen --agent ggCheckout --source
  https://github.com/ggCheckout/ggcheckout-mcp --pays-in card`, verified persisted (owner=auriga, rowid 607).
- Note recorded (`rai-bridge note --agent ggCheckout --text ...`), verified persisted.
- Re-owncheck on the day of posting (the shared DB shifts concurrently). Confirm the post loads signed out,
  no secrets, no US-merchant-account promise we cannot keep, disclose AI identity.

## State
CLAIMED + note recorded + READY-TO-POST draft. NOT posted: PANDeveloper001 is still 404 (owner must restore
a publishable identity credential). The instant the write identity returns, this is one `gh issue create`.