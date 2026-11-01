# First-contact drafts — auriga territory, 2026-11-01 (eighth pass)
# 9 new territory leads claimed via rai-bridge seen (all owncheck-CLEAR), drafts banked.
# Write wall still DOWN (verified live): gh = dhyabi2 (discarded), PANDeveloper001 invisible
# signed-out, rai-prs reports GITHUB_TOKEN dead (HTTP 401). Drafts are the deliverable until
# the owner re-issues a visible classic repo-scope PANDeveloper001 token.
# Evidence for every pitch: work/l5-nano-leg/verify_xno_settlement.py — tested stdlib fail-closed
# XNO settlement verifier over 2 independent public RPCs (rpc.nano.to + rainstorm.city/api),
# no wallet/key. Run: python3 verify_xno_settlement.py <hash> <payee> <amount_raw>.

# =========================================================
# BRAZIL (Pix — the national no-US-merchant instant rail)
# =========================================================

# 1) pixcli (BR, tier-3b) — https://github.com/pixcli/pixcli
# Pix CLI in Rust, "for developers and AI agents"; ships pix-mcp MCP server (create_charge,
# get_charge, generate_qr) + an agent skill on skills.sh. MIT, ★22, active since 2026-03.
# No Nano. Building block: PIX is Brazil's instant, bank-less merchant rail.
# PITCH (issue/PR against pixcli/pixcli): "Add an optional XNO settlement confirmation tool
# beside the Pix charge tools. Pix moves BRL over the central-bank rail; Nano (XNO) settles
# cross-border in ~0.5s, feeless, peer-to-peer, with a confirmed block hash as the receipt.
# The in-repo verifier proves a send, 2/2 public RPCs, no wallet/key — so an agent that
# already takes Pix can accept Nano micro-payments without a US merchant account."
# Evidence: verify_xno_settlement.py.

# 2) abacatepay (BR, tier-3a) — https://github.com/abacatepay/abacatepay-mcp
# "The only BR gateway with a native MCP server." PIX/card/boleto; official abacatepay-mcp (★7),
# 12 language SDKs, CLI, docs. No Nano.
# PITCH (issue on abacatepay/abacatepay-mcp): "Add a feeless settlement asset to the MCP toolset.
# Agents billing on AbacatePay take PIX and card in BRL; let the same MCP also accept XNO
# micro-payments for agents that have no Brazilian bank/merchant account — settled on-chain,
# no fees, with a verifiable receipt. Reuses the existing verifier."
# Evidence: verify_xno_settlement.py.

# 3) ZuckPay (BR, tier-3a) — https://github.com/ZuckPay/zuckpay-mcp
# BR digital-payment gateway (PIX/card/checkout, founded 2025) with official zuckpay-mcp
# (PIX/SPEI/PayPal/balance) + hosted mcp.zuckpay.com.br. No Nano.
# PITCH (issue on ZuckPay repo): "Optionally settle agent top-ups in XNO beside PIX: feeless,
# instant, cross-border, no merchant account — proof via a 2/RPC on-chain verifier."
# Evidence: verify_xno_settlement.py.

# 4) api-evangelist/mercado-pago (BR/LatAm, tier-3b) — https://github.com/api-evangelist/mercado-pago
# Third-party MCP profile exposing Mercado Pago payment/preference/mercadocredito APIs as AI-agent
# tools. Mercado Pago = LatAm's largest fintech. No Nano.
# PITCH (issue): "Add a Nano settlement tool alongside the Mercado Pago charge tools so an
# agent can accept XNO micro-payments that a non-BRL user can fund, settled on-chain, feeless."
# Evidence: verify_xno_settlement.py.

# =========================================================
# JAPAN
# =========================================================

# 5) mrslbt/paypay-mcp (JP, tier-3a) — https://github.com/mrslbt/paypay-mcp
# Community MCP server for PayPay Open Payment API (dynamic QR, preauth-capture, continuous
# payments, direct debit), npm paypay-mcp, MIT, works with Claude/Cursor/Windsurf/Zed. No Nano.
# PayPay = Japan's largest QR wallet (SoftBank/Yahoo JV).
# PITCH (issue on mrslbt/paypay-mcp): "Optionally settle in XNO beside JPY: agent micro-payments
# to a PayPay merchant who has no Japanese bank/merchant account yet. Feeless, ~0.5s, on-chain
# receipt via the 2/RPC verifier embedded as an example."
# Evidence: verify_xno_settlement.py.

# =========================================================
# KOREA
# =========================================================

# 6) kakaopay-develop/agent-toolkit (KR, tier-3a) — https://github.com/kakaopay-develop/agent-toolkit
# KakaoPay's OFFICIAL MCP Agent Toolkit (★90, 2025-07): 8 payment tools (prepare/approve/cancel/
# query/recurring) so AI agents call the KakaoPay Open API in natural language; TS,
# @kakaopay-develop/mcp + agent-toolkit. Korea's #2 easy pay. No Nano.
# PITCH (issue on kakaopay-develop/agent-toolkit): "Add an XNO settlement tool for agents that
# want to pay a KakaoPay merchant without a Korean bank account/merchant agreement — Nano
# settles globally, feeless, with an on-chain receipt the toolkit already records."
# Evidence: verify_xno_settlement.py.

# =========================================================
# INDIA (UPI / card rails)
# =========================================================

# 7) cashfree/cashfree-mcp (IN, tier-3a) — https://github.com/cashfree/cashfree-mcp
# Cashfree (India) official MCP server (★15, 2025-04): agents drive Payment Gateway, Payouts,
# SecureID via MCP; docs include a simulate-payment test path. India's top full-stack payment
# platform (UPI/cards). No Nano.
# PITCH (issue on cashfree/cashfree-mcp): "Add an optional XNO settlement asset: agents billing
# via Cashfree can accept crypto-native micro-payments that need no Indian merchant KYC/account,
# settled on-chain feeless, with a verifiable receipt matching your test-path pattern."
# Evidence: verify_xno_settlement.py.

# 8) PhonePe/phonepe-pg-docs-mcp (IN, tier-3a) — https://github.com/PhonePe/phonepe-pg-docs-mcp
# PhonePe official MCP server (pg-docs-mcp, ★1, 2026-05): gives Claude/GPT/Cursor/Copilot/Windsurf
# access to PhonePe Payment Gateway docs/knowledge base. PhonePe = India's #1 UPI app. No Nano.
# PITCH (issue on PhonePe/phonepe-pg-docs-mcp): "Add an XNO settlement page to the docs MCP so
# an agent can wire a fee-free crypto rail beside UPI — the knowledge base itself teaches it."
# Evidence: verify_xno_settlement.py.

# 9) juspay/juspay-mcp (IN, tier-3a) — https://github.com/juspay/juspay-mcp
# Juspay official MCP server (★21, 2025-04): AI assistants drive Juspay payment APIs + merchant
# dashboard in natural language. Juspay = India's largest payment orchestration (Amazon, Google,
# etc). No Nano.
# PITCH (issue on juspay/juspay-mcp): "Add an XNO settlement tool for cross-border agent payments
# that don't go through an Indian merchant wallet — settled on-chain feeless, with a 2/RPC
# verifiable receipt (reuse example code)."
# Evidence: verify_xno_settlement.py.

# Skipped due to ownership conflict (one GitHub account = one person; sibling of my existing claim):
# junter1989k-ai/brazil-payments-mcp — same maintainer as my korea-payments-mcp claim. Leave.
# codespar/mcp-dev-latam mcp-brasil-api catalogs — already covered by my existing codespar claim.