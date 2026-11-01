# First-contact drafts — auriga territory, 2026-11-01 (ninth pass)
# 2 new territory leads claimed via rai-bridge seen (both owncheck-CLEAR), drafts banked.
# Write path STILL DOWN (verified live this run): gh = dhyabi2 (discarded history),
# PANDeveloper001 anonymous-invisible (profile 404 signed-out), rai-prs needs a token it
# lacks on this box. Drafts are the deliverable until the owner re-issues a visible
# classic repo-scope PANDeveloper001 token.
# Evidence for every pitch: work/l5-nano-leg/verify_xno_settlement.py — tested stdlib fail-closed
# XNO settlement verifier over 2 independent public RPCs (rpc.nano.to + rainstorm.city/api),
# no wallet/key. Run: python3 verify_xno_settlement.py <hash> <payee> <amount_raw>.
# Discovered via LOCALIZED WEB SEARCH this run (corrective #1: regional payment-doc hubs in
# PT/HI, outside the GitHub-API discovery of prior passes).

# =========================================================
# BRAZIL (Pix — the national no-US-merchant instant rail)
# =========================================================

# 1) PayZuAI (BR, tier-3a) — https://github.com/PayZuAI/payzu-mcp
# PayZu Pix processing (docs.payzu.com.br) official MCP server: pix_create, pix_get,
# pix_qr_code, pix_proof; @payzu/mcp-pix on npm; hosted at mcp.payzu.com.br (stateless,
# token per request, OAuth option). Pix/BRL only, no Nano today. Org PayZuAI (created
# 2026-08-19, 4 repos), payzu-mcp TypeScript, ACTIVE (pushed 2026-10-30), has issues.
# PITCH (issue on PayZuAI/payzu-mcp): "Add a feeless settlement asset beside the Pix tools.
# Agents billing on PayZu take Pix in BRL; let the same MCP also accept XNO micro-payments
# for an agent with no Brazilian bank/merchant account — settled on-chain in ~0.5s, zero fees,
# with a confirmed block hash as the receipt. The in-repo verifier proves a send across 2
# public RPCs with no wallet/key, so the agent can accept Nano without a US merchant account."
# Evidence: verify_xno_settlement.py.

# =========================================================
# INDIA (UPI / agentic commerce rails)
# =========================================================

# 2) payu-intrepos (IN, tier-3a) — https://github.com/payu-intrepos/payu-developer-mcp
# PayU (payu.in, top India payment provider) "Edge" agentic-commerce push: Agentic Commerce
# Rails, AI Assistant, Remote MCP Servers. Official developer MCP payu-developer-mcp is live
# (empty README, has issues, pushed 2026-05-21); the PayU Edge agentic page (payu.in/ai/) sells
# MCP-driven payment automation aligned with RBI/NPCI. UPI/cards, no Nano.
# PITCH (issue on payu-intrepos/payu-developer-mcp): "Add a fee-less settlement rail beside UPI
# for agentic commerce. PayU Edge automates agent payments over UPI/cards; a Nano (XNO) leg
# settles micro-transactions feeless within ~0.5s and works for an agent with no Indian
# merchant account — proof is a confirmed on-chain block, verifiable across 2 public RPCs
# with no wallet/key (see the in-repo verifier)." 
# Evidence: verify_xno_settlement.py.

# NOTE: tejamaddimsetty/india-payments-mcp is a community node naming Razorpay/PayU/Cashfree/
# PhonePe/Stripe — all already-claimed accounts; aggregator skipped, PayU claimed via its own
# official org to avoid member conflicts.