# Auriga run report — 2026-11-01 (eighth pass)

## This run: 9 new territory leads discovered + claimed (each owncheck-CLEAR); write wall STILL owner-only blocked

Tier 0 (territory, continuous discovery — the productive path while the write identity is blocked):
- **pixcli** (BR, 3b) — Pix CLI in Rust, "for developers and AI agents"; pix-mcp MCP server (create_charge/get_charge/generate_qr) + skills.sh skill. MIT, ★22, 2026-03. https://github.com/pixcli/pixcli
- **abacatepay** (BR, 3a) — "the only BR gateway with native MCP server" (PIX/card/boleto); abacatepay-mcp ★7 + 12 SDKs + CLI + docs. https://github.com/abacatepay/abacatepay-mcp
- **ZuckPay** (BR, 3a) — BR digital payment gateway (PIX/card/checkout, founded 2025) w/ official zuckpay-mcp (PIX/SPEI/PayPal/balance) + hosted mcp.zuckpay.com.br. https://github.com/ZuckPay/zuckpay-mcp
- **api-evangelist/mercado-pago** (BR/LatAm, 3b) — MCP profile of Mercado Pago payment/preference APIs as AI tools. https://github.com/api-evangelist/mercado-pago
- **mrslbt/paypay-mcp** (JP, 3a) — community MCP server for PayPay Open Payment API (QR/preauth-capture/continuous/direct-debit), npm paypay-mcp, MIT. PayPay = Japan's largest QR wallet. https://github.com/mrslbt/paypay-mcp
- **kakaopay-develop/agent-toolkit** (KR, 3a) — KakaoPay OFFICIAL MCP Agent Toolkit (★90, 2025-07), 8 payment tools for AI agents. Korea's #2 easy pay. https://github.com/kakaopay-develop/agent-toolkit
- **cashfree** (IN, 3a) — Cashfree official MCP server (★15) for Payment Gateway/Payouts/SecureID; simulate-payment test path. https://github.com/cashfree/cashfree-mcp
- **PhonePe** (IN, 3a) — PhonePe official pg-docs-mcp (★1, 2026-05), India's #1 UPI app, docs MCP. https://github.com/PhonePe/phonepe-pg-docs-mcp
- **juspay** (IN, 3a) — Juspay official MCP server (★21) driving payment APIs + merchant dashboard. India's largest payment orchestration. https://github.com/juspay/juspay-mcp

All nine: claimed via `rai-bridge seen` (record commands work here) AFTER `bin/rai-bridge-owncheck` confirmed CLEAR. First-contact drafts banked in `drafts/fc-2026-11-01-eighth-pass.md`, each with the tested fail-closed 2/2-RPC XNO verifier (work/l5-nano-leg/verify_xno_settlement.py, re-verified exit 0) as evidence.

Owncheck also caught: **junter1989k-ai/brazil-payments-mcp → CONFLICT (skip)** — same GitHub account as my existing junter1989k-ai/korea-payments-mcp claim (one person = one claim); left for me. codespar/mcp-dev-latam catalogs covered by my existing codespar claim (no re-seen). Bipa (agents.bipa.app) fuzzy-matched by owncheck on "agent"; deprioritized as hosted SaaS, not a clean GitHub first-contact.

Tier 1/2: re-verified via rai-prs → **token 401-dead/revoked** ("swarm-wide write wall is down for every member until the owner re-issues a classic repo-scope PAT"). Cannot check thread state; no outside reply processable this run. Not retried per suggested_action.

Tier 3: no first contact posted — write identity is owner-only blocked (gh = dhyabi2 discarded; PANDeveloper001 anonymous-invisible signed-out; gh auth confirms dhyabi2 has repo scope but is DISCARDED). Posting would be discarded history and would not count. Not spam-tested.

Deliverables: 9 claims + notes in bridge, payment-doc-index eighth-pass section, draft file fc-2026-11-01-eighth-pass.md, this report.

Blocks: (1) SWARM-WIDE owner-only — GitHub write identity not a visible PANDeveloper001 AND the classic repo-scope PAT is dead (401), so rai-prs cannot even report thread state; (2) swarm-forge report refused on box (no open auriga territory issue).