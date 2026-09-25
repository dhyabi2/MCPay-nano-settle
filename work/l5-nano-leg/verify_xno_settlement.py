#!/usr/bin/env python3
"""
verify_xno_settlement.py — verified XNO settlement leg for ORIGIN L5's TRANSFER_NATIVE rail.

What this is:
  A self-contained, independently re-runnable proof that a Nano (XNO) block is a confirmed,
  final SEND to a given payee — the "native" settlement evidence for ORIGIN's L5 x402 rail.
  It verifies on >=2 independent public read-only Nano RPCs (fail-closed) and emits an
  ORIGIN-format `settlement_receipt` (docs/SETTLEMENT-ESCROW.md §5.1) whose `on_chain_anchor`
  is the XNO block hash.

Why:
  ORIGIN's L5 escrow uses a dual ledger — (A) on-chain balance movement, (B) an off-chain
  receipt anyone can re-hash — and its `native` rail is expressed as chain-level records on
  an L1 with no EVM execution layer. Nano (XNO) settles peer-to-peer, feeless, in ~0.5 s, and
  a confirmed block hash is itself a chain-level record. So an XNO send is the natural native
  leg: the block hash anchors ledger B, exactly like the `on_chain_anchor` field expects.

Disclosure (up front, per ORIGIN's condition):
  - No wallet, no seed, no API key required. Uses two PUBLIC read-only RPCs:
      https://rpc.nano.to        (POST JSON-RPC, read actions)
      https://rainstorm.city/api (POST JSON-RPC, read actions, 5000 req/hr shared)
  - The verifier only READS chain state; it never signs, never broadcasts, holds no funds.
  - A "settlement" here means: prove a confirmed XNO send to the payee ONCE, then emit its
    receipt. It does not mint, move or hold YUAN; the YUAN-denominated `balance_delta` is a
    separate conversion step this snippet deliberately leaves to the caller.

Run:
  python3 verify_xno_settlement.py <block_hash> <payee_address> <amount_raw>
  e.g.
  python3 verify_xno_setlement.py \
    ECCB8CB65CD3106EDA8CE9AA893FEAD497A91BCA903890CBD7A5C59F06AB9113 \
    nano_1111111111111111111111111111111111111111111111111111hifc8npp \
    205676479000000000000000000000000000000

Exit codes: 0 = verified + receipt written; 1 = fail-closed rejection; 2 = usage; 3 = network.
"""

import json
import sys
import urllib.request

# Two independent public read-only Nano RPCs. Both are needed and BOTH must confirm a SEND
# or the verification rejects (fail-closed). No keys, no wallet.
ENDPOINTS = [
    "https://rpc.nano.to",
    "https://rainstorm.city/api",
]


def rpc_call(url, action, params):
    body = json.dumps({"action": action, **params}).encode("utf-8")
    # rpc.nano.to rejects the bare Python-urllib UA with 403; these are public read
    # actions, so a plain browser-like UA is all that is needed (no key, no secret).
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "l5-xno-settlement-leg/0.1"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normalize_block_info(raw):
    """Canonicalize any node's block_info shape. FAILS CLOSED on missing proofs."""
    contents = raw.get("contents") or {}
    account = raw.get("block_account") or contents.get("account")
    subtype = (
        raw.get("subtype")
        or contents.get("type")
        or contents.get("subtype")
        or (contents.get("link") and "send")
    )
    destination = raw.get("link_as_account") or contents.get("destination") or contents.get("link")
    confirmed = raw.get("confirmed")
    if isinstance(confirmed, str):
        confirmed = confirmed.lower() == "true"
    amount = raw.get("amount") or contents.get("amount")
    if confirmed is not True or amount is None:
        return None
    return {"account": account, "subtype": subtype, "destination": destination, "amount_raw": str(amount)}


def verify_send(block_hash, payee, amount_raw):
    """Verify a confirmed SEND to `payee` of `amount_raw` on >=2 independent RPCs (fail-closed)."""
    confirmed_on = 0
    consulted = 0
    reasons = []
    normalized = []
    for url in ENDPOINTS:
        consulted += 1
        try:
            raw = rpc_call(url, "block_info", {"json_block": "true", "hash": block_hash})
        except Exception as exc:  # network / JSON error — endpoint counts as unhealthy
            reasons.append(f"{url}: error {exc}")
            continue
        if "error" in raw:
            reasons.append(f"{url}: node error {raw['error']}")
            continue
        norm = normalize_block_info(raw)
        if norm is None:
            reasons.append(f"{url}: cannot prove confirmed+amount")
            continue
        normalized.append(norm)
        if norm["subtype"] != "send":
            reasons.append(f"{url}: not a send (type={norm['subtype']})")
            continue
        dest = norm["destination"] or ""
        if dest.rstrip() != payee:
            reasons.append(f"{url}: destination {dest} != payee {payee}")
            continue
        if str(norm["amount_raw"]) != str(amount_raw):
            reasons.append(
                f"{url}: amount {norm['amount_raw']} != expected {amount_raw}"
            )
            continue
        # A confirmed send implies finality on Nano (cemented blocks cannot be reverted).
        confirmed_on += 1

    ok = confirmed_on >= 2 and confirmed_on == consulted
    return {
        "ok": ok,
        "confirmed_on": confirmed_on,
        "consulted": consulted,
        "reasons": reasons,
        "normalized": normalized,
    }


def build_receipt(block_hash, payee, amount_raw, verified):
    # ORIGIN docs/SETTLEMENT-ESCROW.md §5.1 — the receipt written when value moves.
    return {
        "agreement_id": "x402-native-xno",
        "release_decision": "auto_condition",
        "balance_delta": {
            "charged": amount_raw,   # raw XNO that moved, feeless
            "refunded": "0",
            "asset": "XNO",          # actual asset that moved; YUAN conversion is caller's step
        },
        "evidence_digest": f"sha256:{block_hash.lower()}",
        "on_chain_anchor": {"tx": block_hash, "block": "confirmed-on-2-rpcs"},
        "verdict_ref": None,
        "finality": "final",
        "_verify": {
            "confirmed_on": verified["confirmed_on"],
            "consulted": verified["consulted"],
            "endpoints": ENDPOINTS,
            "disclosure": "no wallet, no key, read-only public RPCs",
        },
    }


def main(argv):
    if len(argv) != 4:
        print(__doc__)
        return 2
    block_hash, payee, amount_raw = argv[1], argv[2], argv[3]
    result = verify_send(block_hash, payee, amount_raw)
    if not result["ok"]:
        print("REJECTED (fail-closed):", json.dumps(result, indent=2))
        return 1
    receipt = build_receipt(block_hash, payee, amount_raw, result)
    print("ACCEPTED. Confirmed on %d/%d independent RPCs." % (result["confirmed_on"], result["consulted"]))
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
