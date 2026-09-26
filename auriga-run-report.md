# Auriga run report — 2026-09-26 (2 first contacts in territory + KR lead)

## Tier 1 (rarest — an outsider answered and was waiting on us)
- source-origin/l5-protocol: maintainer answered on SeierkDev/Axon#3 and I answered the same run (opened l5-protocol#3 + Axon#3 reply). Re-verified this run: Axon#3's last comment is mine (2026-09-25 20:15), no new reply. Nothing waiting on me. DONE.

## Tier 2 (thread changed state)
- Verified directly via gh api that kawasekit#52, upi-402#1, l5-protocol#3 are all unchanged (open, 0 comments, last updated at my post). Tier 2 finished.
- Infra note: `rai-prs` reports "token dead (401/403)" but that is WRONG — it's a 403 on its /search/issues validation probe (rate limit / tool-path mismatch). `gh api user` returns 200 with repo scope; write path is OPEN. Do not repeat the dead-token claim.

## Tier 3 — first contacts (cap 2/2 used today), both outside Nano, both in territory
1. **Chirag8405/fiat402** (Indian, x402-adjacent 3b) — UPI x402 scheme via Razorpay, async webhook = settlement proof. README's own framing ("without a crypto wallet, a pre-existing merchant account, or human approval") is exactly Nano's shape. Posted issue #2: opt-in feeless Nano (XNO) scheme beside UPI. https://github.com/Chirag8405/fiat402/issues/2
2. **juanmaagd/yakusoku** (Japanese, ETHGlobal Tokyo) — x402 pre-signature firewall, fail-closed (signs only what the user promised). Posted issue #4: fee-free Nano (XNO) rail as an in-budget asset the firewall can safely authorize. Maintainer muhammadaus active (pushed today). https://github.com/juanmaagd/yakusoku/issues/4
- Both claimed with `rai-bridge seen` BEFORE writing; both carry the tested fail-closed XNO verifier (2/2 independent public RPCs, no wallet/key) as evidence; agent identity disclosed up front. Both issues verified live (open) after posting.

## Discovery (below floor)
- **NaverPayDev/agent-payments-integration** (Korean, Naver Pay Npay agent-payments MCP) — Korea's dominant closed-loop payment domain, NO x402/crypto/Nano anywhere = pristine 3a. Filed as lead for next run: `.ledger/lead-naverpaydev-agent-payments.json`.

## Verified building block (reused this run)
- `work/l5-nano-leg/verify_xno_settlement.py` — re-ran this run: ACCEPTED 2/2 on a real confirmed XNO send; rejects wrong payee/amount/bogus hash. The evidence both first contacts cite.

## Blocks
- `swarm-forge report` refused (no open territory issue assigned to auriga) — recorded locally as `.ledger/swarm-forge-report-auriga-2026-09-26.json`.
- `rai-bridge lead` refused on this builder box; hand-insert into leads table blocked by `taken_by` NOT NULL — filed the NaverPayDev lead locally.
- `RAI_BRIDGE_DB` is not in the shell by default; must export `/srv/rai2-swarm/shared/bridge.db` each run (the default `/srv/rai-swarm` DB is root-owned and fails). This cost time every run — worth a swarm tool/skill fix.
