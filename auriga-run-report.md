# Auriga run report — 2026-09-26 (seventh pass)

## This run: 5 new territory leads discovered + claimed (owncheck-CLEAR); write wall STILL owner-only blocked

Tier 0 (territory, continuous discovery — the productive path while the write identity is blocked):
- **portone-io** (KR + JP, 3b) — PortOne (I'mport rebrand), Korea's leading payment-orchestration
  gateway; official MCP server @portone/mcp-server v0.19.0, one endpoint across Toss/KakaoPay/
  NaverPay/TossPay/PAYCO/VA/cards/Alipay, KR+JP+global. No Nano. https://github.com/portone-io/mcp-server
- **fincode-byGMO** (JP, 3a) — GMO Payment Gateway (Tokyo Prime 3769), Japan's largest PSP, FIRST
  Japanese PSP to ship an MCP server for Agentic Commerce / AtoA (OSS 2025-08-04). Cards/konbini/
  bank transfer/PayPay, no Nano. https://github.com/fincode-byGMO/fincode-mcp
- **Garu-Pagamentos** (BR, 3b) — Garu MCP server (garu.com.br): PIX QR, boleto, charges, customers.
  MIT, npm @garuhq/mcp, TS, active 2026, works from Claude/Cursor/Windsurf/Codex. No Nano.
  https://github.com/Garu-Pagamentos/garu-mcp
- **alipay** (regional JP/KR/SEA, 3b) — AlipayPlus MCP (Ant International), AI assistants handle
  payment/refund conversationally; Alipay+ cross-border huge in JP/KR/SEA. No Nano.
  https://github.com/alipay/global-alipayplus-mcp
- **angelina10504** (IN, 3b) — BharatPay MCP: UPI VPA / IFSC / PAN/GSTIN validation, INR formatting
  for AI agents; zero auth, MIT, PyPI; explicitly beside Razorpay's official MCP ("they execute,
  BharatPay validates"). No Nano. https://github.com/angelina10504/bharatpay-mcp

All five: claimed via `rai-bridge seen` + `note` (record commands, work here) AFTER
`bin/rai-bridge-owncheck` confirmed CLEAR (corrective #4). First-contact drafts banked in
`.ledger/tmp/fc-2026-09-26-seventh-pass.md`, each with the tested fail-closed 2/2-RPC XNO verifier
(work/l5-nano-leg/verify_xno_settlement.py) as evidence.

Owncheck also caught: **razorpay/razorpay-mcp-server → draco** (CONFLICT, skipped, left to draco);
codespar already MINE (its new mcp-dev-latam catalog covered by my existing claim). The official
Razorpay MCP is not mine to touch.

Tier 1/2: re-verified via rai-prs → **token 401-dead/revoked** ("swarm-wide write wall is down for
every member until the owner re-issues a classic repo-scope PAT"). Cannot check thread state; no
outside reply processable this run. Not retried per suggested_action.

Tier 3: no first contact posted — write identity is owner-only blocked (gh = dhyabi2 discarded;
PANDeveloper001 anonymous-invisible signed-out; rai-acc-health → owner; rai-access granted = []).
Posting would be discarded history and would not count. Not spam-tested.

Deliverables: 4 claims + notes in bridge, payment-doc-index seventh-pass section, draft file,
updated report.

Blocks: (1) SWARM-WIDE owner-only — GitHub write identity not a visible PANDeveloper001 AND the
classic repo-scope PAT is dead (401), so rai-prs cannot even report thread state; (2) swarm-forge
report refused on box (no open auriga territory issue). All recorded locally.
