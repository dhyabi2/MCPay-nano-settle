# First-contact drafts — auriga territory, 2026-11-02 (twelfth pass)
# 5 new territory leads claimed via rai-bridge seen (all owncheck-CLEAR), drafts banked.
# Discovery angle for THIS pass: fresh GitHub-API updated scans on the national rail + mcp
# + AI-agent-payment keywords (upi x402, india payments mcp, brazil payments mcp, pix mcp)
# — surfaces targets that NEVER came up in prior passes' localized-web or PSP-MCP sweeps.
# Write wall STILL DOWN (verified live this run): rai-prs reports GITHUB_TOKEN dead
# (HTTP 401/422), gh authenticates as dhyabi2 (discarded), PANDeveloper001 anonymous-invisible
# (rai-acc-health: account_public=false, profile_http=404, anonymous_api_login=null).
# Drafts are the deliverable until the owner re-issues a visible classic PANDeveloper001 token.
# Evidence for every pitch: work/l5-nano-leg/verify_xno_settlement.py — tested stdlib
# fail-closed XNO settlement verifier over 2 independent public RPCs (rpc.nano.to +
# rainstorm.city/api), no wallet/key. Verified this run (exit 0 usage path).

# =========================================================
# 1) vintemhq/vintem (Brazil, tier-3a, ★1)  <- STRONGEST; PERFECT pitch fit
# =========================================================
# https://github.com/vintemhq/vintem
# "Pix sem gateway" = self-hosted, multi-bank Pix gateway. One binary speaks the Central
# Bank's Pix API, per-bank adapters, mTLS + webhook normalization. INCLUDES PIX AUTOMATICO
# (recurring Pix). Ships a 'vintem mcp' MCP server for AI agents (create/check/list/cancel/
# refund Pix charges; API-key scoped read-only). Go, Apache-2.0, org vintemhq, alpha but
# Efí adapter receives REAL Pix payments live. created 2026-10-28, pushed 2026-10-30
# (ACTIVE). Tier-3a pristine: the ENTIRE pitch is removing the middleman fee from Pix —
# literally the same claim Nano makes (feeless rail). vintem.dev docs + roadmap.
# PITCH (issue upstream against vintemhq/vintem, in THEIR voice):
#   "Add an optional feeless Nano (XNO) settlement path beside Pix Automático. Vintém's
#    whole reason to exist — no middleman, no fee, your money yours — is exactly what Nano
#    is: a zero-fee, instant, final settlement rail an agent can verify on-chain without a
#    wallet or a bank account. A buyer in India (or an MCU/embedded payer) can settle a
#    Vintém charge in XNO at zero fee and the agent gets a block-hash receipt as the audit
#    record — no gateway, no card network, no merchant account. Verified on 2 independent
#    public RPCs with an existing no-wallet verifier (work/l5-nano-leg/verify_xno_settlement.py).
#    Complements, never replaces, the Pix legs already in Vintém."
# Evidence: verify_xno_settlement.py (tested 2/2 RPC, fail-closed).
# NOTE: alpha — frame as a contribution/direction, not a demand. Pinned for first slot.

# =========================================================
# 2) amrav69/mandatepay (India, tier-3b, ★1)
# =========================================================
# https://github.com/amrav69/mandatepay
# Signed payment mandates for AI agents. Rust, MIT, ACTIVE (created 2026-08-24, pushed
# 2026-10-31). Ed25519 intent mandates with spend caps, expiry and replay protection,
# verified before any Razorpay order executes. Built for Razorpay AI Buildathon 2026
# Track 01: Agentic Commerce; README says ACP/AP2/x402 and NPCI's UAP are converging on
# agent payments. Tier-3b: architect explicitly building an agent-payment control layer on
# fiat (Razorpay), zero Nano. India = the no-US-merchant-account market.
# PITCH (issue upstream against amrav69/mandatepay, their voice):
#   "Add a Nano (XNO) settlement oracle alongside the Ed25519 mandate. MandatePay's cheque
#    is the control layer — 'should this agent move this money, right now?' — and XNO is
#    the settlement layer it can clear against at zero fee and instant finality, verifiable
#    on-chain by any agent via 2 public RPCs (no wallet, no secret). A signed XNO mandate
#    keeps the same spend-cap/expiry/replay discipline on the feeless tier the USDC/card
#    tiers already have. Evidence: existing tested no-wallet verifier
#    (work/l5-nano-leg/verify_xno_settlement.py). Complements, not replaces, Razorpay."
# Evidence: verify_xno_settlement.py.

# =========================================================
# 3) tejamaddimsetty/india-payments-mcp (India, tier-3a, ★1)
# =========================================================
# https://github.com/tejamaddimsetty/india-payments-mcp
# One MCP server + TypeScript SDK for Indian gateways: Razorpay, PayU, Cashfree, CCAvenue,
# Paytm, PhonePe, Stripe, Dodo Payments, Skydo, Infinity. Amounts in minor units (paise),
# webhooks normalized to one model, 759 tests pass. TypeScript, MIT, npm package, ACTIVE
# (created 2026-10-28, pushed 2026-10-29). Tier-3a: a fiat gateway aggregator MCP, zero Nano.
# PITCH (issue upstream, their voice):
#   "Add an optional Nano (XNO) gateway adapter beside the fiat adapters. The whole premise
#    is agent settlement across India's rails with one normalized model; XNO is the missing
#    zero-fee, no-merchant-account, instant-finality rail — an agent paid in India without a
#    bank account can receive confirmed XNO and the payments_verify_payment tool can return
#    the block-hash receipt instead of a card auth. Evidence: existing tested no-wallet
#    verifier (work/l5-nano-leg/verify_xno_settlement.py). Complements the 10 existing
#    gateways; fits the add-any-rail architecture."
# Evidence: verify_xno_settlement.py.

# =========================================================
# 4) bipa-app/bipa-cli (Brazil, tier-3a, ★7)
# =========================================================
# https://github.com/bipa-app/bipa-cli
# "Payment rails for AI agents — Pix, BRL, and beyond." Pre-built binaries and managed
# installer, agents.bipa.app. MIT, org bipa-app, ACTIVE (created 2026-03-09, pushed
# 2026-10-21). Rail-first framing — the exact seam Nano wins. Tier-3a fiat-only.
# PITCH (issue upstream, their voice):
#   "Offer a Nano (XNO) bailment/rail beside Pix and BRL. Bipa's pitch — payment rails an
#    agent uses directly — is where XNO belongs: zero fee, instant, final, verifiable on 2
#    public RPCs with no wallet/API key (work/l5-nano-leg/verify_xno_settlement.py). Cross-
#    border or sub-cent tiers that Pix/BRL can't cover reach an agent in Japan/in India with
#    no merchant account. Additive; keeps the Pix/BRL rails untouched."
# Evidence: verify_xno_settlement.py.

# =========================================================
# 5) theYahia/asaas-mcp (Brazil, tier-3a, ★0)  <- official-PSP-MCP class
# =========================================================
# https://github.com/theYahia/asaas-mcp   (npm: @theyahia/asaas-mcp)
# MCP server for Asaas payments + Pix gateway (Brazil): create/get/list payments, Pix QR,
# billing. theYahia also ships mcp-skills (40+ MCP workflows across BR/MENA/Gulf/Africa/
# SEA/CIS). Account claimed ONCE via asaas-mcp (sibling repos are the same person).
# Tier-3a: official-regional-PSP MCP (highest-value discovery class). No settlement seam
# beyond fiat Pix. PITCH similar to others: optional feeless XNO leg for the Pix QR/charge
# tier, verified on 2 public RPCs via the existing verifier. Evidence: verify_xno_settlement.py.

# =========================================================
# Skipped (NOT claimed — out of territory or weak seam):
# =========================================================
# - codespar/mcp-dev-latam (LatAm commerce MCP, ★277): owncheck CONFLICT, already MINE
#   (auriga) via codespar/agentic-payments-standards. No new claim needed — it surfaced
#   again on the fresh scan, confirming the earlier claim was well-placed.
# - viztfxyz/qrbaton + viztfxyz/handcart (IN): agent shops, human approves UPI QR on phone.
#   Human-gated settlement — no clean agent-settles-itself seam for a Nano leg. Skipped.
# - Faiziimam/agentcart (IN): agent fills cart, hands UPI QR to human. Same human-gated
#   approval flow; no autonomous agent settlement. Skipped.
# - ggCheckout/ggcheckout-mcp: 189 tools, but global checkout/funnels platform (WhatsApp,
#   members area), not verifiable JP/KR/BR/IN territory. Skipped.
# - singh-shreya27/VoicePay, Drix10/guardian-gpt, Rerunix/sentinel: IN but anti-scam/voice
#   UX prototypes, no settlement seam. Skipped.
# - Siyuan-chat/miseport (JP read-only catalogs), bb4rjfl/korea-trip-concierge: no
#   settlement seam. Skipped.