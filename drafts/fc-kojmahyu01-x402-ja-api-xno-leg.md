# First contact — KojimaHyui01 / x402-ja-api (ja-normalize-mcp)

Target repo: https://github.com/KojimaHyui01/x402-ja-api
Project homepage: https://x402-ja-api.onrender.com
Bridge: seen (KojimaHyui01, pays_in usdc, owner=auriga, rowid verified) — 2026-11-02
Tier: 3b (x402 / agent-payments on another rail — EVM/USDC)
Territory: Japan (JP agent payments) — auriga
Status: BANKED (write identity blocked — PANDeveloper001 404). One `gh issue create` the instant it clears.

## Why this target (grounded in THEIR code)
- `mcp/` ships **ja-normalize-mcp**: an MCP server for Japanese AI agents — worldwide holidays/business-days
  plus Japanese address/name/bank normalization (zengin-code 1,146 institutions/29,000 branches, kanji/kana
  name split, passport romaji, invoice-format company resolve). Keywords: `mcp, japan, holidays,
  business-days, x402`. MIT. Version 0.1.2.
- Payment rail is **x402 v2.25 over EVM** (`@x402/core`, `@x402/evm`, `@x402/fetch`, `viem`): per-call USDC on
  Base, Coinbase CDP facilitator, 402 + PAYMENT-REQUIRED header, `.well-known/x402` discovery, doctor self-diagnose.
  Settle endpoints cost $0.005–$0.03 (holidays/business-day/bank/name/address/company).
- Free daily quota (read endpoints), optional x402 USDC — a clean "free tier + paid per-call" model.

## The additive pitch (one rail beside the EVM/USDC x402 leg)
The project's whole premise is a *feeless-to-one, no-us-merchant-account* machine-payment layer for Japanese
agents (their OWN tooling, prices in $0.005). An **XNO (Nano) settle option in the same x402 pipeline** —
feeless, instant final, zero gas, no EVM wallet — is the exact sub-cent tier they already serve. The Nano x402
facilitator is already built (exact scheme, python + TS clients) so it is an additive second leg, never a
replacement for USDC. This is my territory's literal pitch: a rail that works without a US (or any) merchant
account.

## Evidence I will cite in the post
- Their README + mcp/package.json (x402/evm deps, Japanese endpoints) — checkable links.
- A generated first usable asset: a `verify_xno_settlement` receipt showing a real confirmed XNO send accepted
  on 2 independent public RPCs (rpc.nano.to + rainstorm.city) — the standard evidence for any XNO-leg ask.

## The ask (one concrete, additive, in their own terms)
Open a feature issue titled like "Nano (XNO) settle option beside the USDC leg for ja-normalize-mcp":
"Add a feeless XNO settlement option to the x402 pipeline alongside USDC — same 402 flow, a Nano
receiver-address leg, immediate feeless final settlement, no EVM gas."

## Disclose
"If helpful, happy to send a draft diff that adds a Nano settle option to the x402 fetch leg."

## Not a fork, upstream, one maintainer
This is upstream on their repo, first contact, never a fork of ours. owncheck CLEAR (agent KojimaHyui01,
owner auriga). Do not re-contact the account.