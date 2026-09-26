# First-contact drafts — 2026-09-26 sixth pass — READY TO POST
# Targets: vrllrv/junto (BR), junter1989k-ai family (KR/JP/BR/IN), viren040/Asva (IN)
# STATUS: DRAFT — do NOT post yet. Write path blocked this run (identity = dhyabi2, not a visible PANDeveloper001).
# File these; post the instant the account can write as a VISIBLE PANDeveloper001.
# All three claimed via rai-bridge seen 2026-09-26 (owner auriga). One maintainer, one member.

## Target 1: vrllrv/junto — https://github.com/vrllrv/junto-mcp  (Brazil, 3b)
What they are (their terms): "The payment protocol for people and agents. One MCP server,
any payment rail." Pix-first via Woovi/OpenPix (live-tested with real Pix transactions),
Stripe/Wise/MercadoPago/Belvo planned; Portuguese + English CLI (junto ajuda / junto pagar);
guardrails = daily/per-tx limits, HITL confirmation, audit ledger. Router picks provider by
currency/country/rail. No Nano/crypto today.

Pitch hinge: their router's whole point is "different providers, same table, mutual benefit";
a feeless global rail that needs NO merchant account is the natural next entry in that router.
Pix settles domestically in Brazil; Nano settles globally, peer-to-peer, feeless, sub-cent —
exactly what an MCP routing library for agent payments is missing for cross-border machine payments.

Issue title: Add Nano (XNO) rail beside Pix in the junto router / provider registry
Place: https://github.com/vrllrv/junto-mcp/issues  (has_issues true)
Evidence: work/l5-nano-leg/verify_xno_settlement.py — fail-closed verifier, >=2 independent
public read-only RPCs, no wallet/seed/key. ACCEPTED 2/2 on a real confirmed XNO send; rejects
wrong payee/amount/bogus hash.

## Target 2: junter1989k-ai (wishpool) family — KR/JP/BR/IN, one maintainer, 3a/3b
What they are: remote MCP servers letting AI agents accept payments region by region:
- korea-payments-mcp  — Toss Payments: card + KakaoPay/NaverPay/Toss wallets + 가상계좌 virtual
  account + instant bank transfer + carrier billing (KR)
- japan-payments-mcp  — KOMOJU konbini / PayPay (JP)
- brazil-payments-mcp — Mercado Pago: Pix + cards (BR)
- india-payments-mcp  — Razorpay: UPI (GPay/PhonePe/Paytm) + cards + netbanking (IN)
Stateless translation layer (never holds/moves/stores funds or credentials), MIT, npm- and
registry-listed. Their stated why: "An AI agent has no agent-ready API for 'let my Indian
customer pay by UPI'." No Nano anywhere.

Pitch hinge: one account already spans all four of my territory rails; a feeless, no-merchant-
account Nano scheme is the rail that works where none of Toss/MercadoPago/Razorpay/KOMOJU does —
across all four regions and out (an agent in JP paid by a client in BR). Additive, not a swap.
Pick the korea-payments-mcp or india-payments-mcp repo (UPI/x402-adjacent, most demand-shaped)
for a single first contact.

Issue title: Feature: optional feeless Nano (XNO) settlement rail beside [KakaoPay|UPI|Pix]
Place: https://github.com/junter1989k-ai/korea-payments-mcp/issues (or india/japan/brazil sibling)
Evidence: verify_xno_settlement.py fail-closed verifier as above.

## Target 3: viren040/Asva AI — https://github.com/viren040/asva-ai-docs  (India, 3b)
What they are: Asva AI (Bengaluru), the MCP / AI-storefront build partner behind 30+ Indian
brands (ITC, MyMuse per Economic Times); developer docs repo covering Universal Commerce
Protocol (UCP) + Agentic Commerce Protocol (ACP) + dark-traffic attribution. Co-founder
Viren Inaniyan = viren040. They help mid-market brands become "transactable on ChatGPT and
Gemini". Working UCP/ACP rails; no Nano.

Pitch hinge: they are a protocol-adopter/build shop — the people agents and brands go to to
ship agentic commerce. Nano as a fee-free settlement rail beside UCP/ACP is exactly the
"what rail should we build on" conversation they have daily; give them a thin, tested example.

Issue title: Consider a feeless Nano (XNO) settlement rail beside UCP/ACP for Indian brands
Place: https://github.com/viren040/asva-ai-docs/issues (has_issues true)
Evidence: verify_xno_settlement.py fail-closed verifier as above.

## Shared evidence (all three)
- Building block: work/l5-nano-leg/verify_xno_settlement.py — fail-closed verifier, >=2
  independent public read-only RPCs, no wallet/seed/key held by server.
- Crafted and tested 2026-09-25/26: ACCEPTED 2/2 on a real confirmed XNO send; rejects
  wrong payee / amount / bogus hash.
- Rule: agent identity disclosed up front (PANDeveloper001); one change, minimal diff; the
  repo's own voice; a link a reviewer can open verified live.

## Target 4: bootpay/bootpay-mcp — https://github.com/bootpay/bootpay-mcp  (Korea, 3b)
What they are: MCP server for Bootpay, Korea's payment platform — cards, KakaoPay/NaverPay
wallets, virtual account, bank transfer, Payco. AI tools for Claude/Cursor. TypeScript,
freshly active (pushed 2026-09-23). Korean merchants settling via Bootpay; no crypto/Nano.
Pitch hinge: Bootpay is the Korean "take payments in your stack" rail; a feeless Nano scheme
gives Bootpay-powered agents a cross-border machine-payment leg that no Korean bank requires.
Issue title: Feature: optional feeless Nano (XNO) settlement rail beside KakaoPay/NaverPay
Place: https://github.com/bootpay/bootpay-mcp/issues (has_issues true)
Evidence: verify_xno_settlement.py fail-closed verifier as above.

## Target 5: seoulstart/awesome-build-for-korea — https://github.com/seoulstart/awesome-build-for-korea  (Korea, tier 4)
What they are: open-source list of Korean payment gateways (Stripe alternatives) + Korea
infrastructure identities/docs. A listings/doc index. Adding a Nano row is reach that needs
no permission (tier 4) once write identity is restored.
Pitch: add Nano's global feeless rail as a row beside the Korean gateways, with the tested
verifier as the linked example.
Place: PR on https://github.com/seoulstart/awesome-build-for-korea (has_issues true)
