# ORIGIN L5 — Nano (XNO) native settlement leg for `TRANSFER_NATIVE`

A self-contained, independently re-runnable proof that a Nano (XNO) block is a **confirmed
SEND** to a given payee — the "native" settlement evidence for ORIGIN L5's x402 `native`
rail. It verifies on **>=2 independent public Nano RPCs** (fail-closed) and emits an
ORIGIN-format `settlement_receipt` (docs/SETTLEMENT-ESCROW.md §5.1) whose
`on_chain_anchor` is the XNO block hash.

## Why this fits ORIGIN L5

ORIGIN settles through a dual ledger — (A) on-chain balance movement, (B) an off-chain
receipt anyone can re-hash — and its L1 (`origin-1`) has **no EVM execution layer**, so the
`native` rail is expressed as chain-level records, not Solidity. Nano settles
peer-to-peer, feeless, in ~0.5 s, with no facilitator in the loop, and a confirmed block
hash is itself a chain-level record. So an XNO send is a natural `native` leg: the block
hash anchors ledger B exactly as the `on_chain_anchor` field expects — and it is cheap
enough for the escrow's 多退少补 (over/under-charge) tiny adjustments, where the over/under
round trip must not cost more than the job itself.

## Disclosure (up front)

- **No wallet, no seed, no API key.** Uses two public read-only Nano RPCs:
  - `https://rpc.nano.to` — POST JSON-RPC, read actions (a plain browser-like User-Agent
    is required; no key)
  - `https://rainstorm.city/api` — POST JSON-RPC, read actions (~5000 req/hr shared)
- The verifier **only reads chain state**; it never signs, never broadcasts, holds no funds.
- "Settlement" here means: prove a confirmed XNO send to the payee **once**, then emit its
  receipt. It does not mint, move or hold YUAN; the YUAN-denominated `balance_delta` is a
  separate conversion step deliberately left to the caller.

## Requirements

- Python 3.8+ (stdlib only: `json`, `urllib`, `sys`). No pip install.

## Run

```
python3 verify_xno_settlement.py <block_hash> <payee_address> <amount_raw>
```

Real example (a live, confirmed send):

```
python3 verify_xno_settlement.py \
  ECCB8CB65CD3106EDA8CE9AA893FEAD497A91BCA903890CBD7A5C59F06AB9113 \
  nano_1111111111111111111111111111111111111111111111111111hifc8npp \
  205676479000000000000000000000000000000
```

Output (verified 2026-09-25 against both live RPCs):

```
ACCEPTED. Confirmed on 2/2 independent RPCs.
{
  "agreement_id": "x402-native-xno",
  "release_decision": "auto_condition",
  "balance_delta": { "charged": "2056...0", "refunded": "0", "asset": "XNO" },
  "evidence_digest": "sha256:eccb8cb6...",
  "on_chain_anchor": { "tx": "ECCB8CB6...", "block": "confirmed-on-2-rpcs" },
  "verdict_ref": null,
  "finality": "final",
  "_verify": { "confirmed_on": 2, "consulted": 2, "endpoints": [...], "disclosure": "..." }
}
```

## Fail-closed behaviour (verified)

| Case | Result |
|------|--------|
| Real confirmed SEND, correct payee + amount | ACCEPTED, 2/2 RPCs |
| Correct block, wrong payee | REJECTED (exit 1) |
| Correct block, wrong amount | REJECTED (exit 1) |
| Bogus / non-existent block | REJECTED (exit 1) |

A rejection happens if **any** consulted endpoint errors, cannot prove `confirmed`, is not
a `send`, or disagrees on destination or amount. Both endpoints must independently confirm
the same SEND or the receipt is not emitted.

Exit codes: `0` verified+receipt · `1` fail-closed rejection · `2` usage · `3` network.

## Keeping it honest

- Confirmation is read from the chain on each call; nothing is precomputed or cached.
- Nano confirms in ~0.5 s with no reorgs (cemented blocks are terminal), so a block that
  both RPCs report as `confirmed` is final.
- The `asset` is the asset that actually moved (XNO); converting `charged` to a
  YUAN-denominated figure is the caller's step and is not faked here.
