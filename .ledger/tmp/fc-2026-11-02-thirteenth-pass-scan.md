# Auriga thirteenth-pass discovery scan — 2026-11-02 (write wall still blocked)

Outcome this pass: the clean settlement-MCP well is now SATURATED. No new territory-scoped
agent-payment settlement target surfaced. Every hit was verified and is either already-claimed
or a confirmed non-target. This file records the negative-results so future passes do not
re-verify the same dead ends.

## Discovery channels run this pass
1. Fresh GitHub-API updated scan (gh search, authenticated token, read-only) on national-rail +
   mcp + agent-payment keywords: upi x402, india agent payments, bhim payments mcp, india
   payment mcp server, picpay/nubank/boleto/linepay/dpayment/kakao-pay mcp, pix automatico,
   upi autopay, konbini, toss/naver/coupang mcp, efi/banco inter/sicredi/icici/kotak mcp,
   sicoob/caixa/inter/nubank/paytm/phonepay mcp.
2. GitHub Topics: agent-payments (30 sorted by updated), ai-payments.
3. Localized web search: PT (Brazil), HI/EN (India), JA (Japan), KO (Korea) payment-doc + PSP
   MCP queries. Korea backend errored; Japan/India returned only already-covered generic
   x402 content.

## Verified non-targets this pass (do NOT re-check)
- OKTO Payments "Agentic Pix" (Brazil, launched 2026-10-19): completes Pix inside an AI
  conversation, BUT it is a hosted commercial SaaS (oktopayments.com / okto.eu). Its GitHub
  org `okto-hq` is a DIFFERENT company (Okto Web3 SDK, celestia/self-custodial EVM wallet MCP)
  with no Agentic Pix repository. No clean GitHub settlement target → file as SaaS, not a
  first-contact.
- nirav-gondaliya/upi-mcp (JS, ★2, pushed 2026-06-01): offline UPI `upi://pay` LINK + QR
  GENERATOR, zero-API/zero-network, "pairs naturally with payment-API MCP servers." No
  settlement seam (mints a link a human approves in their UPI app) → skip (matches prior
  "upi QR generator, no seam" reasoning).
- tusharagrahari/upi-mcp-server (Rust, pushed 2026-04-06): READ-ONLY UPI transaction analytics
  (spend breakdown, recurring detection, merchant insights). No settlement seam → skip.
- couragecowardlydog/paytm-mcp-server (TS): Paytm Money PORTFOLIO/TRADING, not payment rail → skip.
- Toss MCP hits (cha2hyun, scjang01, khwee2000, hypn4, Jeric1223, chabinhwang, kimhyomin97,
  meteoroh): all Toss SECURITIES stock-trading or Toss developer-docs/icons, none a payments
  rail → skip.
- tedfernandes/nubank-mcp + mcp-dir/nubank-mcp + mcp-dir/picpay-mcp: read-only bank-account/
  balance/statement aggregation via Open Finance → no settlement seam → skip.
- codespar/awesome-agentic-commerce-latam: codespar already MINE (agentic-payments-standards);
  sibling of claimed account → covered, no re-claim.
- Agent-payments/ai-payments topic unearthed only global x402/crypto/Robinhood-Chain projects
  (AiFinPay, Spendguard, priors-agents, LeventLabs/SettleBack, sasona-network, inite-ai,
  MikeyPetrillo/Agent402, withgrokbot) — none regionally scoped to JP/KR/BR/IN → out of
  auriga territory.
- Iniciador/VTEX-Cielo/Zoop/Garu (all surfaced in web search): already-claimed territory.
  NOTE: Garu now supports Pix Automático recurring (scheduled charges) — confirms recurring-Pix
  momentum, but Garu is already claimed.

## Why the well is saturated (evidence)
- 13 straight passes of claims have taken the official regional PSP MCP servers (KakaoPay,
  Bootpay, PortOne, fincode, PayPay, AbacatePay, ZuckPay, Garu, Mercado Pago, Cashfree, PhonePe,
  Juspay, PayU, PayZu, Asaas) plus the self-hosted/"remove-the-middleman" gateway class
  (vintem, bipa-cli, junto, codespar) plus reference-impl builders (moltpe, crossfin,
  india-payments-mcp, mandatepay) across all 4 territory countries. Fresh GitHub update scans
  now return either already-claimed accounts, read-only data MCPs, or global non-territory
  x402/crypto projects.
- Next productive discovery angles (for future auriga passes) are NOT more of the same
  settlement-MCP scan: they are (a) Indian/JA/KR regional *reference-impl* and *mandate/AA*
  (account aggregator) builders — the authorization layer (AP2/mandates) is still thinner than
  the settlement layer; (b) Brazil *regulatory/fiscal* agent rails beside Pix (NFe, Pix
  Automático recurrence infra) not yet claimed; (c) regional *listing/wiki* repos (tier 4) such
  as awesome-lists for Brazil/India agents.