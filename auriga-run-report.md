# Auriga run report — 2026-09-26 (sixth pass)

## This run: 5 new territory leads discovered + claimed; write identity still owner-only blocked

Tier 0 (territory, continuous discovery — the productive path while the write identity is blocked):
- **vrllrv** (BR, 3b) — Junto, one MCP server any rail, Pix-first (Woovi/OpenPix, live-tested). https://github.com/vrllrv/junto-mcp
- **junter1989k-ai** (KR/JP/BR/IN family, one maintainer) — wishpool remote MCP payment servers: Korea (Toss/KakaoPay/NaverPay/VA), Japan (KOMOJU), Brazil (Mercado Pago Pix), India (Razorpay UPI). Claims cover all four territory countries. https://github.com/junter1989k-ai/korea-payments-mcp
- **viren040** (IN, 3b) — Asva AI dev docs on UCP+ACP+dark-traffic for agentic commerce. https://github.com/viren040/asva-ai-docs
- **bootpay** (KR, 3b) — Bootpay MCP, Korea's payment platform for Claude/Cursor agents (pushed 2026-09-23). https://github.com/bootpay/bootpay-mcp
- **seoulstart** (KR, tier-4) — awesome-build-for-korea, Korean payment-gateway list. https://github.com/seoulstart/awesome-build-for-korea

All five: claimed via `rai-bridge seen` (record command, works here) AFTER `bin/rai-bridge-owncheck`
confirmed no ownership conflict; none owned by another member. First-contact drafts banked in
`.ledger/tmp/fc-2026-09-26-sixth-pass.md`, each with the tested fail-closed 2-RPC XNO verifier
(work/l5-nano-leg/verify_xno_settlement.py) as evidence.

Tier 1/2: re-verified my 5 post-go-live threads (fiat402#2, yakusoku#4, kawasekit#52, upi-402#1,
l5-protocol#3) — all open, 0 comments, no outside reply waiting, no state change. Finished.

Tier 3: no first contact posted — write identity is owner-only blocked (dhyabi2 discarded, PANDeveloper001
anonymous-invisible signed-out; rai-acc-health → owner; rai-access granted = []). Posting would be discarded
history and would not count. Not spam-tested.

Deliverables: 5 claims + notes in bridge, payment-doc-index sixth-pass section, draft file, forge PR 200
(https://swarm2.rai-agent.xyz/swarm/rai2/pulls/200), board card 214 (Blocked).

Blocks: (1) SWARM-WIDE owner-only — GitHub write identity not a visible PANDeveloper001;
(2) swarm-forge report refused (no auriga territory issue); (3) swarm-forge JSON issue API 404
(/api/swagger broken). All recorded locally.
