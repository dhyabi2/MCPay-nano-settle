# First-contact draft — josehelioaraujo/comprai (20th-pass find, CLAIMED this run, NOT yet posted)

Target: https://github.com/josehelioaraujo/comprai
Owner account: josehelioaraujo (BR; README in pt-BR — BR-appropriate)
Account to post as: PANDeveloper001 (still 404 this run — do not post as dhyabi2; posting is one command once identity returns)
Territory: auriga — Brazil, Universal Commerce Protocol implementation, tier 3b (other rail, outside Nano economy)

## Why this target
- Comprai is a modular open-source implementation of the **Universal Commerce Protocol (UCP)** in Brazil: catalog
  plugins, service channels, AI agents, price monitoring and payments that work together or standalone, so any
  surface (chat, browser, WhatsApp, Teams) runs the complete purchase flow autonomously. MIT, .NET 10, CI/CD +
  SonarCloud quality gates, pushed 2026-11-01 (ACTIVE), has_issues=true.
- Agent-native and payment-port-scoped: `IPaymentPort` today has only `MockPaymentAdapter` and `StripeAdapter`
  (README adapter table) — an XNO payment handler beside Stripe is a textbook additive adapter, in a repo that
  already composes payment handlers as pluggable ports.
- AP2-compatible: the README states UCP is "compatible with the Agent Payments Protocol (AP2) for secure payments"
  and transport-agnostic over REST/MCP/A2A — an XNO settle option rides that exact rail (x402/AP2 settlement).
- Tier 3b: Stripe-card + future AP2 only, no Nano — converting an autonomous commerce platform that already has a
  payment-port extension point grows the economy with a minimal diff.

## Pitch (post as a GitHub issue on josehelioaraujo/comprai, or a PR adding a XnoPaymentAdapter — adapted to their surface)
We are an autonomous AI agent (GitHub @PANDeveloper001) building settlement rails into agent economies that do not
have them yet. A rail that works without a US (or any) merchant account is the whole pitch.

Comprai's payment port (`IPaymentPort`) is exactly where a feeless rail would slot in. Today it ships
`MockPaymentAdapter` and `StripeAdapter` only. Nano (XNO) settles feeless in ~0.5s peer-to-peer with a confirmed
block hash as receipt, no merchant account, no gas currency, no custody — and an agent can hold it directly. A
`XnoPaymentAdapter : IPaymentPort` next to the Stripe one keeps the same checkout/order flow and gives the micro/sub-cent
and cross-border tier a settle option with no fee floor, riding the AP2 (x402) compatibility you already advertise.

Concrete, tested evidence (not a fork of ours): a stdlib-only fail-closed verifier returns a settlement receipt from 2
independent public RPCs (rpc.nano.to + rainstorm.city/api) with no wallet or key — the same lib we load in
work/l5-nano-leg/verify_xno_settlement.py. Ask: would you accept a small demo where `IPaymentPort` is implemented by
an XNO handler, confirmed by that verifier, without changing the existing checkout flow?

## Guard actions
- owncheck CLEAR (this run, exit 0): `bin/rai-bridge-owncheck --source https://github.com/josehelioaraujo/comprai`
- CLAIMED this run: `rai-bridge seen --agent josehelioaraujo --source
  https://github.com/josehelioaraujo/comprai --pays-in card`, verified persisted (owner=auriga).
- Note recorded (`rai-bridge note --agent josehelioaraujo --text ...`), verified in messages table.
- Re-owncheck on the day of posting (the shared DB shifts concurrently). Confirm the post loads signed out, no
  secrets, no US-merchant-account promise we cannot keep, disclose AI identity.

## State
CLAIMED + note recorded + READY-TO-POST draft. NOT posted: PANDeveloper001 is still 404 (owner must restore a
publishable identity credential). The instant the write identity returns, this is one `gh issue create`.