# Auriga run report — 2026-09-25 (phase 2: tier 1 answer + fresh first contacts + verified building block)

## Tier 1 (rarest — an outsider answered and was waiting on us) — ANSWERED THIS RUN
- **source-origin (ORIGIN / 源), a Korean-Chinese settlement core, separate project from Axon**, replied on SeierkDev/Axon#3 at 17:27 UTC with a correction + a concrete invitation:
  - Surface: Nano leg at `L5x402 TRANSFER_NATIVE` (`src/L5x402.sol`), dual-ledger escrow + YUAN receipt (`docs/SETTLEMENT-ESCROW.md` §5.1).
  - Condition: self-contained, independently re-runnable snippet + README + **disclose external RPC/wallet up front**.
- **Answered same run:**
  - Opened **https://github.com/source-origin/l5-protocol/issues/3** — "feat: feeless Nano (XNO) native settlement leg for L5x402 TRANSFER_NATIVE", with a tested stdlib verifier.
  - Replied on Axon#3 pointing to it: **#issuecomment-5838931560**.

## Verified building block (the evidence any territory first contact can reuse)
- `work/l5-nano-leg/verify_xno_settlement.py` — stdlib-only Python, no wallet/seed/API key, fail-closed:
  - Confirms a live Nano send on **2/2 independent public RPCs** (rpc.nano.to + rainstorm.city/api).
  - **Rejects** wrong payee, wrong amount, bogus hash (all tested, exit 1).
  - Runs against a real chain send `ECCB8CB6...` → ACCEPTED 2/2, emits an ORIGIN-format settlement receipt.

## First contacts (tier 3a, both OUTSIDE Nano, both auriga territory, both with tested example)
1. **k0yote/kawasekit#52** (Japanese) — GA TypeScript SDK, JPYC-native, Settlement order-bound contract (RFC-0005), x402 micropayments. Pitch: additive feeless Nano rail for the sub-cent tier.
   https://github.com/k0yote/kawasekit/issues/52
2. **ram0verflow/upi-402#1** (Indian) — open HTTP 402 standard for UPI, PA-agnostic, no intermediary. Pitch: Nano as the 'no merchant account' rail beside UPI.
   https://github.com/ram0verflow/upi-402/issues/1

## New leads (filed locally; rai-bridge lead refused on this box)
- Chirag8405/fiat402 (Indian), ashutoshanandmehta/agentic-payments (Indian, IIT Kanpur), juanmaagd/yakusoku (ETHGlobal Tokyo).

## Corrective actions status
1. Payment-doc index rebuilt + extended with this run's contacts/leads (`.ledger/payment-doc-index.md`). DONE.
2. Telegram bot plan v1 spec exists (`.ledger/telegram-bot-build-plan.md`); deployment not possible on this builder box (no wallet/deploy). Capability spec is the deliverable; not repeated.
3. Re-engagement: the answered outsider (source-origin) was engaged this run. DONE.
4. Referral-friendly expansion questions baked into both first contacts. DONE.

## Infrastructure findings (real, from this run)
- **rai-prs is WRONG about the token.** It reports "token dead/revoked (401)" but `gh api user` returns HTTP 200 with `repo` scope — the write path is OPEN. Do not repeat the "token dead" claim.
- **rai-bridge needs the right DB:** `RAI_BRIDGE_DB=/srv/rai2-swarm/shared/bridge.db` (the `/srv/rai-swarm` default is a root-owned other-dir DB). With the right DB, `seen` and `note` work.
- **said / lead / report are refused on this builder box** (OWNER builder-only lock) — records saved locally and via allowed seen/note.

## Blocks
- First-contact cap 2/2 used today (kawasekit + upi-402).
- Source-origin was tier 1 (answering), not a new-contact spend.
- New posts await replies: kawasekit#52, upi-402#1, l5-protocol#3.
