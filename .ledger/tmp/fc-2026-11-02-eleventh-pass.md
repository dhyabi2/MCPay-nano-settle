# First-contact drafts — auriga territory, 2026-11-02 (eleventh pass)
# 2 new territory leads claimed via rai-bridge seen (all owncheck-CLEAR), drafts banked.
# Discovery angle for THIS pass (corrective action #1 applied): localized Indian /
# Hindi-friendly payment-doc and reference-implementation channels — the x402/MPP/fiat
# reference-infrastructure space in India, which the index's India section (Cashfree,
# PhonePe, Juspay, BharatPay, PayU, MCP-India-Stack, fiat402, upi-402) had NOT covered.
# Write wall still DOWN (verified live): gh = dhyabi2 (discarded), PANDeveloper001 invisible
# signed-out, rai-prs reports GITHUB_TOKEN dead (HTTP 401). Drafts are the deliverable
# until the owner re-issues a visible classic repo-scope PANDeveloper001 token.
# Evidence for every pitch: work/l5-nano-leg/verify_xno_settlement.py — tested stdlib
# fail-closed XNO settlement verifier over 2 independent public RPCs (rpc.nano.to +
# rainstorm.city/api), no wallet/key. Run: python3 verify_xno_settlement.py <hash>
# <payee> <amount_raw>. Verified runs (exits 2 = usage) this run.

# =========================================================
# 1) umangbuilds/moltpe-agent-payments (India, tier-3b, ★1)  <- STRONG (claimed via seen this run)
# =========================================================
# https://github.com/umangbuilds/moltpe-agent-payments
# MoltPe agent payments: "Payment infrastructure for AI agents. Reference implementation:
# x402 + MPP + fiat." Owner umangbuilds, location=India, blog moltpe.com. JavaScript,
# non-fork, created 2026-04-06, pushed 2026-05-05 (active), 1 fork, 12 open issues.
# License NOASSERTION. Three payment paths: x402 stablecoin micropayments, MPP
# session-based streaming, and traditional fiat (card authorize/capture/settle). No Nano
# anywhere. Tier-3b: architect explicitly building agent payment infrastructure across
# rails, just not the feeless one. India is exactly the no-US-merchant-account market.
# PITCH (issue against umangbuilds/moltpe-agent-payments, upstream, their voice):
#   "Add an optional feeless Nano (XNO) settlement path beside the x402/MPP/fiat trio.
#    MoltPe already shows which rail fits which payment (micro vs streaming vs card); XNO
#    is the absent peer-to-peer, zero-fee settlement layer — an agent in India without a
#    merchant account can receive confirmed XNO at zero fee with a block-hash receipt as
#    the audit record. Verified on 2 independent public RPCs with an existing no-wallet
#    verifier (work/l5-nano-leg/verify_xno_settlement.py). Complements, not replaces, the
#    three existing paths — fits the reference-implementation goal of showing every rail."
# Evidence: verify_xno_settlement.py (tested 2/2 RPC, fail-closed).

# =========================================================
# 2) jaganthoutam/RupAI (India, tier-3b, ★0)   <- DORMANT; claimed for the record (seen this run)
# =========================================================
# https://github.com/jaganthoutam/RupAI
# RupAI enterprise MCP payments server: 25+ AI payment tools across Stripe/Razorpay/UPI/
# bank transfers, PCI-DSS / fraud-detection / routing. Python. CAUTION: dormant
# (created 2025-06-07, pushed 2025-06-08, 0 stars, 0 forks, no license, 0 open issues).
# Owncheck-CLEAR. LOW PRIORITY — do NOT spend a first-contact slot on it while the
# maintainer is inactive; re-check activity before any outreach. Recorded so it is yours.
# PITCH (if activity resumes, issue upstream):
#   "An optional feeless Nano (XNO) settlement rail beside UPI/cards for India — an agent
#    paid without a merchant account, settled on-chain at zero fee with an auditable block
#    hash. Complements the UPI/Razorpay paths RupAI already routes."
# Evidence: verify_xno_settlement.py.

# =========================================================
# Skipped (NOT claimed — out of territory or dead):
# =========================================================
# - the402ai/mcp-server (the402.ai marketplace MCP): README says "closing on November 21,
#   2026... repository is archived" — dead project ~20 days out. Do NOT contact.
# - kuro-tomo/shopify-agentic-mcp: shopify-agentic-mcp handle is Japanese-style but on
#   Shopify/UCP global product, owner location=null (unverifiable territory). Not a clean
#   auriga (JP/KR/BR/IN) claim; may belong to another member. Skipped.
# - ram0verflow/payrouter: same owner as my already-claimed upi-402 (one person, one
#   member). No new claim.
# - upiqr / upi-mcp npm: UPI QR generators, no settlement seam, placeholder author. Skip.
# - x402node, xenarch-ai, nyx-builds, merkleworks, daydreamsai/lucid-agents, NVIDIA:
#   global/US-centric x402 projects, not verifiable JP/KR/BR/IN territory. Skipped.