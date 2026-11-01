# Auriga run report — 2026-11-02 (twelfth pass)

## This run: 5 new territory leads claimed (each owncheck-CLEAR) via a fresh GitHub-API updated scan; write wall STILL owner-only blocked (verified live); strongest ever single lead — vintem (Pix-without-gateway)

Tier 0 (territory, continuous discovery — the productive path while the write identity is blocked):
- **vintemhq/vintem** (BR, 3a, ★1) — "Pix sem gateway": self-hosted multi-bank Pix gateway, Pix Automático (recurring), ships a `vintem mcp` MCP server for AI agents (scoped read-only key). Active (2026-10-30), alpha but Efí adapter handles real Pix live. **PERFECT fit**: its whole pitch is removing the middleman fee — literally the same claim Nano makes. Pinned first slot. https://github.com/vintemhq/vintem
- **amrav69/mandatepay** (IN, 3b, ★1) — Ed25519 signed payment mandates (spend caps/expiry/replay) for AI agents, verified before any Razorpay order. Razorpay AI Buildathon 2026 Track01 Agentic Commerce. Active (2026-10-31). Agent control layer on fiat, zero Nano. https://github.com/amrav69/mandatepay
- **tejamaddimsetty/india-payments-mcp** (IN, 3a, ★1) — MCP server + TS SDK across Indian gateways (Razorpay/PayU/Cashfree/CCAvenue/Paytm/PhonePe/...), 759 tests, npm, active (2026-10-29). Distinct maintainer. https://github.com/tejamaddimsetty/india-payments-mcp
- **bipa-app/bipa-cli** (BR, 3a, ★7) — "Payment rails for AI agents — Pix, BRL, and beyond." Rail-first framing. Active (2026-10-21). https://github.com/bipa-app/bipa-cli
- **theYahia/asaas-mcp** (BR, 3a, ★0) — MCP for Asaas Pix gateway (BR). Official-regional-PSP MCP class. Account claimed once. https://github.com/theYahia/asaas-mcp

All five claimed via `rai-bridge seen` + `note` (record commands work here) AFTER `bin/rai-bridge-owncheck` confirmed CLEAR (exit 0 each). Discovery angle for THIS pass: fresh GitHub-API `sort=updated` scan on the national-rail + mcp + agent-payment keyword set (`upi x402`, `india payments mcp`, `brazil payments mcp`, `pix mcp`, `korea payments mcp`) — a channel that surfaced targets prior localized-web and PSP-MCP sweeps never touched (vintem, mandatepay, bipa-cli are all new to the index).

First-contact drafts banked: `.ledger/tmp/fc-2026-11-02-twelfth-pass.md` — all 5. **vintemhq/vintem and amrav69/mandatepay are STRONG and READY TO POST** the instant a visible write identity returns, each with the tested fail-closed 2/2-RPC XNO verifier (work/l5-nano-leg/verify_xno_settlement.py; re-verified exit-0 usage this run) as evidence.

Skipped with reasons (each checked): codespar/mcp-dev-latam (★277) = CONFLICT, already mine via codespar/agentic-payments-standards (confirms earlier claim well-placed); viztfxyz/qrbaton + handcart, Faiziimam/agentcart (IN agent-shopping = human-gated UPI approval, no clean agent-settles-itself seam); ggCheckout/ggcheckout-mcp (global, not verifiable JP/KR/BR/IN); singh-shreya27/VoicePay, Drix10/guardian-gpt, Rerunix/sentinel (anti-scam/UX prototypes, no settlement seam); Siyuan-chat/miseport, bb4rjfl/korea-trip-concierge (read-only, no seam).

Tier 1/2: `rai-prs` on this box refuses ("GitHub token dead or revoked, HTTP 401/422") before reporting thread state — cannot check, not re-run per its own suggested_action. Bridge conversation (`waiting`/`live`) + `lead` refused here by the builder-only lock (`seen`/`note` are the record path that works).

Tier 3: no first contact posted — write identity is owner-only blocked (gh = dhyabi2 discarded; PANDeveloper001 anonymous-invisible: account_public=false, profile 404, anonymous_api_login=null). Posting would be discarded history and would not count. The run brief's "GITHUB WRITE PATH: OPEN" is stale: the repo-scope token mechanically exists but authenticates as dhyabi2, NOT publishable as PANDeveloper001.

Deliverables: 5 claims + notes in bridge (vintemhq, amrav69, tejamaddimsetty, bipa-app, theYahia), payment-doc-index twelfth-pass section, draft file fc-2026-11-02-twelfth-pass.md, this report.

Blocks: (1) SWARM-WIDE owner-only — GitHub write identity is not a visible PANDeveloper001 AND the classic repo-scope PAT is dead (401), so rai-prs cannot report thread state and no first-contact post counts; (2) swarm-forge report remains unavailable for auriga on this box (no open auriga territory issue to comment on).