# Auriga run report — 2026-09-25 (second pass, final)

## What I found
- 9 new leads discovered in auriga territory this run (5 from GitHub scan in prior run + 4 from web search this run):
  **Prior run (GitHub scan):**
  1. k0yote/kawasekit — Japan-first JPYC-native TypeScript SDK, GA, npm published, 0 issues (STRONGEST Japanese find)
  2. ashutoshanandmehta/agentic-payments — IIT Kanpur MS research, UPI-primary, Python
  3. ram0verflow/upi-402 — open HTTP 402 standard for UPI, PA-agnostic, TypeScript
  4. Chirag8405/fiat402 — UPI scheme for x402 via Razorpay, TypeScript
  5. dharmik-at/x402-UPI — x402+MCP+UPI, stale but not archived

  **This run (web search, after GitHub rate limit):**
  6. Wonderfulian/kbv-server — Korean government data MCP + x402, Seoul solo dev, REAL mainnet payment verified ($0.02 USDC on Base), dev.to article published. STRONGEST Korean find — fills the Korean gap. Tier 3b.
  7. junter1989k-ai/japan-payments-mcp — Japanese payments MCP server. Tier 3b.
  8. alefnt/AgentPay — BTC-native AI agent payment protocol, CKB Fiber Network, zero-gas micropayments, Hold Invoice escrow, MCP integration. MIT, npm published, 37 commits. Tier 3a.
  9. trucore-ai/x402fuel — Go x402 wallet daemon, non-custodial, EIP-3009, USDC on Base, budget caps. MIT, Go binary. Tier 3b.

- All 9 filed in bridge DB (direct SQLite — rai-bridge CLI blocked by env var path bug).
- Telegram bot: upgraded from draft spec to concrete build plan (.ledger/telegram-bot-build-plan.md):
  - 20 Q&A pairs (5 per language × 4 languages)
  - Technical approach: python-telegram-bot, langdetect, JSONL logging
  - 6-step build sequence: benchmark → answer DB → scaffold → test → deploy → follow
  - 4 ledger laws with oracles
  - Open questions documented (community list, reviewer, out-of-database handling, bot token)
- First-contact draft for Wonderfulian/kbv-server written (drafts/first-contact-wonderfulian-kbv.md):
  - Pitch: Nano (XNO) feeless leg alongside existing x402-on-Base
  - Evidence: dev.to article URL, KBV repo URL, live endpoint URL
  - Guard actions documented, reserved for next cap re-arm

## Who answered
- adamkrawczyk/agentpact#152: posted decision package (option 3 = accept PR as offered) at 04:24 UTC on 2026-09-25.
- Re-engagement + referral ask posted by auriga at 15:15 UTC (comment #5834789646).
- No reply from adamkrawczyk since his decision package. Guard blocks further checks on this repo ("another swarm worked it").
- No one else answered this run.

## What I learned
- Korean territory gap FILLED: Wonderfulian/kbv-server is a real, active, x402-using Korean target — the first one beyond kimnamu/x402-lab. He's a solo non-engineer in Seoul who already ships mainnet payments. This is the highest-value target for a future first contact.
- Web search recovers targets that GitHub search misses (rate-limited on GitHub, found 4 targets via web search that were NOT in the GitHub scan results).
- The Telegram bot capability is buildable: low-risk (static answers, no external API beyond Telegram), high-leverage (force multiplier for first contact), aligns with corrective action #2.
- The bridge DB path bug is real and blocks ALL rai-bridge CLI commands: env var RAI_BRIDGE_DB=/srv/rai-swarm/shared/bridge.db (wrong, unreadable) vs correct path /srv/rai2-swarm/shared/bridge.db (208KB, accessible). Workaround: direct SQLite. Owner needs to fix the env var in /root/.hermes/.env.
- GitHub write token is dead (401 on repo-scope check) — blocks rai-prs, gh issue create, gh pr create. Need owner to re-issue classic PAT.
- Swarm-forge report backend is down (404 at swarm2.rai-agent.xyz) — territory issue comment cannot be posted. Report committed to branch instead.

## What blocks me
1. GitHub write token dead (401) — blocks rai-prs, all gh write commands. Need owner to re-issue classic PAT.
2. Bridge DB path env var wrong — blocks rai-bridge CLI (seen, note, thread, list, live, waiting). Workaround: direct SQLite. Owner needs to fix RAI_BRIDGE_DB in /root/.hermes/.env.
3. First-contact cap 2/2 used — no more first contacts today. Next cap re-arm: tomorrow 00:00 UTC.
4. Swarm-forge report backend down (404) — territory issue comment not posted. Report committed to branch instead.
5. Guard blocks adamkrawczyk/agentpact ("another swarm worked it") — cannot re-check thread state or PR status. Re-engagement was done (comment #5834789646 at 15:15 UTC). Waiting for reply.

## Evidence (checkable URLs)
- Wonderfulian/kbv-server: https://github.com/Wonderfulian/kbv-server
- Wonderfulian dev.to article: https://dev.to/wonderfulian/i-made-korean-government-data-agent-payable-with-mcp-and-x402-heres-what-actually-happened-40e8
- KBV live endpoint: https://kbv-server-f7vfitmlkq-du.a.run.app/mcp
- junter1989k-ai/japan-payments-mcp: https://github.com/junter1989k-ai/japan-payments-mcp
- alefnt/AgentPay: https://github.com/alefnt/AgentPay
- trucore-ai/x402fuel: https://github.com/trucore-ai/x402fuel
- adamkrawczyk/agentpact#152 comment #5834789646: https://github.com/adamkrawczyk/agentpact/issues/152#issuecomment-5834789646
- Commit f55fe9a: auriga: 2026-09-25 run — 9 new leads, Telegram bot build plan, Wonderfulian draft

## Distribution share
- 0 first contacts this run (cap 2/2 used in prior run by Mameta29 and kimnamu)
- 9 leads discovered and filed (territory work — tier 0)
- 1 first-contact draft prepared for next cap re-arm
- 1 capability build plan written (Telegram bot)
- 1 payment-doc index updated

## Next run priorities
1. First contact: Wonderfulian/kbv-server (Korean, tier 3b, strongest target, draft ready) — when cap re-arms
2. First contact: junter1989k-ai/japan-payments-mcp (Japanese, tier 3b) — when cap re-arms
3. Build: Telegram bot v1 (6-step build plan ready, 4 ledger laws) — token-free work, can start now
4. Re-engage: adamkrawczyk/agentpact#152 — if reply arrives, answer same run
5. Fix: bridge DB path env var — file network: issue for owner
6. Fix: GitHub write token — file network: issue for owner
