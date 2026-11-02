# First-contact drafts — auriga territory, 2026-11-02 (fifteenth pass)
# 4 new INDIA mandate/AA-layer territory claims, all owncheck-CLEAR, via seen+note + verified persisted.
# auriga-scan advanced layer 1 (mandate/AA) to seed 5 & new query offsets; found these past the
# dry settlement-MCP well. All fiat-only India, zero Nano/crypto — clean tier-3a.
# Write wall STILL DOWN (re-verified live: rai-prs GITHUB_TOKEN 401; gh auth = dhyabi2 discarded;
# PANDeveloper001 invisible). Drafts are the deliverable until the owner re-issues a visible
# classic repo-scope PANDeveloper001 token.
# Evidence for every pitch: work/l5-nano-leg/verify_xno_settlement.py — tested stdlib fail-closed
# XNO settlement verifier over 2 independent public RPCs (rpc.nano.to + rainstorm.city/api),
# no wallet/key. Run: python3 verify_xno_settlement.py <hash> <payee> <amount_raw>.

# =====================================================================
# INDIA — MANDATE / AUTHORIZATION-AUTH LAYER (pivot layer 1, fiat-only)
# These are Razorpay-ecosystem agent-spend-control projects: the exact
# layer the 13th-pass saturation said to conquer, and they have ZERO Nano/crypto.
# The pitch: an additive feeless XNO settlement-confirmation leg beside the
# INR mandate/policy engine, for the sub-cent / cross-border tier the RBI
# e-mandate rule does not cover.
# =====================================================================

# 1) R-Abinav/mandate (IN, tier-3a, mandate/AA layer) — https://github.com/R-Abinav/mandate
# Deterministic, LLM-free policy gateway governing what an AI agent may spend through Razorpay's
# RECURRING payment APIs, enforced at the HTTP transport layer against the unmodified razorpay-go SDK.
# Cites RBI Circular RBI/DPSS/2026-27/396 (E-mandate Framework 2026): recurring debits up to 15,000
# rupees may run without extra AFA; no per-agent/aggregate spend-cap exists in razorpay-go / -mcp-server
# / -cli. Go, active (2026-09). No Nano.
# PITCH (issue on R-Abinav/mandate): "Beside the INR policy engine, accept an optional XNO settlement-
# confirmation tool: for agents paying a Razorpay merchant across borders (or sub-cent), Nano settles
# ~0.5s feeless peer-to-peer with a confirmed block hash as receipt — no Indian merchant KYC. The
# in-repo 2/RPC verifier proves the send, fail-closed, no wallet/key." Evidence: verify_xno_settlement.py.

# 2) Divyansh-Singh05/PRISM-Payment-Request-Intent-Security-Model (IN, tier-3a, mandate/AA) — https://github.com/Divyansh-Singh05/PRISM-Payment-Request-Intent-Security-Model
# "Agentic Wallet": LLM plans the purchase, a Go engine holds every credential AND the money; dual-key
# mandates, settlement state machine, hash-linked audit trail, 460+ tests. Every rupee explainable,
# bounded, gated; the agent physically cannot reach the DB or Razorpay. Active (2026-09). No Nano.
# PITCH (issue on PRISM): "Add an XNO settlement leg beside the INR dual-key mandate engine: for a
# cross-border counterpart to an INR agent payment, Nano settles feeless & instant with a verifiable
# on-chain receipt your audit chain can record as-is. The 2/RPC verifier proves a send, fail-closed."
# Evidence: verify_xno_settlement.py.

# 3) themayursinha (IN, tier-3a, authorization/authority layer) — https://github.com/themayursinha/mcp-visor
# "MCP Visor Trust Plane" research program (mcp-visor ★5, authority-graph-simulator, agent-identity-plane,
# capability-delta-receipts): runtime policy enforcement + audit for MCP tool execution; counterfactual
# delegation analysis (reachable_authority(G) ⊆ mandate). India security-research territory. No Nano.
# One account = one person; several sibling MCP-authorization repos, claim once via mcp-visor.
# PITCH (issue on themayursinha/mcp-visor): "Extend the MCP policy plane with a settlement-integrity
# check: confirm an agent's XNO payment before the tool result is applied, using a fail-closed 2/RPC
# verifier so the audit plane also proves money actually moved on-chain — not just that the call was
# allowed." Evidence: verify_xno_settlement.py.

# 4) thisizaro/Momotaro (IN, tier-3a, mandate/recovery) — https://github.com/thisizaro/Momotaro
# Razorpay AI Buildathon Track 03 (AI Revenue Recovery): event-driven payment-failure & mandate-recovery
# agent that watches Razorpay webhooks for failed payments/mandates, works out the root cause, then runs
# ONE bounded auditable intervention per cause (no generic retry). Go, active (2026-09). No Nano.
# PITCH (issue on thisizaro/Momotaro): "Add an auto-recovery path for the case where the payee has no INR
# rail at all: settle the recovered invoice in XNO — the recovery agent already reasons about root cause,
# and a feeless on-chain settle with a verifiable receipt closes the gap where Razorpay cannot." 
# Evidence: verify_xno_settlement.py.

# NOTE on Brazil (wandersonchaves/power-camp-registrations, Efí Pix Automático) — owncheck-CLEAR but
# NOT claimed: it is a production church registration app (no clean agent-settles-itself seam), not an
# agent-payments project. Per the skill's skip heuristics (human/hand-rolled, no settlement seam) it is
# the wrong shape for a first contact. Left for tier-4 (a real Pix Automático mTLS reference) if wanted.