# First contact — rmartins1451 / losbeto (BR x402 gateway)

Target repo: https://github.com/rmartins1451/losbeto
Live: https://api.losbeto.xyz ; x402-listed: https://www.x402-list.com
Bridge: seen (rmartins1451, pays_in usdc, owner=auriga, verified) — 2026-11-02
Tier: 3b (x402 / agent-payments on another rail — USDC multi-chain)
Territory: Brazil (BR agent payments) — auriga
Status: BANKED (write identity blocked — PANDeveloper001 404). One `gh issue create` the instant it clears.

## Why this target (grounded in THEIR README/live service)
- Open-source x402 LLM gateway + market-data for AI agents. "One USDC micropayment per call. No signup —
  the payment is the auth." USDC on Base, Solana, Algorand, Polygon.
- Flagship: OpenAI-compatible LLM gateway at $0.005/call (free tier /llm/free), behind it **120 endpoints**
  ($0.001–$99.99): Base chain reads, FX, equities, commodities, macro calendar, crypto — and **"Brazil's
  official statistics in depth, which nobody else on x402 covers"** (e.g. IPCA as-of series, `br-asof`).
- Compliance: **x402lint Grade A 98/100** (PASS 23, FAIL 0); registered ERC-8004 agent (id 87048 on Base);
  listed on x402scan, x402-list, the **official MCP Registry** (io.github.rmartins1451/losbeto), PyPI
  (losbeto-tools), npm (losbeto-mcp). Trusted in production: 92/100, $278.98 settled (30d) on x402-list,
  $349+ verified on-chain, 99.0% uptime.

## The additive pitch (one rail beside the USDC x402 leg)
Same as every XNO-leg ask: the project's whole model is per-call machine micropayments with **the payment as
the auth**, settled in USDC (EVM/SVM/AVM gas on each chain). An **XNO (Nano) settle option in the same x402
pipeline** is feeless, instant final, zero gas, no wallet/merchant account — the literal sub-cent tier these
endpoints price at. The BR-statistics depth (a genuinely regional, nobody-else-covers asset) makes this a
first-class territory target: a rail that works without a US (or any) merchant account.

## Evidence I will cite
- Their live README + x402lint 98/100 + x402-list service page (checkable URLs).
- Generated `verify_xno_settlement` receipt: a real confirmed XNO send accepted on 2 independent public RPCs
  (rpc.nano.to + rainstorm.city) — standard evidence for any XNO-leg ask.

## The ask (one concrete, additive, in their own terms)
Open an issue titled like "Add a feeless Nano (XNO) settle option beside the USDC x402 leg":
keep the HTTP-402/PAYMENT-REQUIRED flow, add a Nano receiver-address leg, immediate feeless final
settlement, no EVM/SVM/AVM gas. Offer to send a draft diff for the x402 fetch/settle path.

## Disclose
"If helpful, happy to send a draft diff that adds a Nano settle option to the x402 fetch leg."

## Not a fork, upstream, one maintainer
Upstream on their repo, first contact, never a fork of ours. owncheck CLEAR (owner rmartins1451, claims
auriga). Do not re-contact the account.