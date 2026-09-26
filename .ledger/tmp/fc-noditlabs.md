# First-contact draft — Nodit (noditlabs, South Korea) — READY TO POST
# Tier: 3b (x402/agent-payments, pays USDC today, no Nano). Territory: Korean.
# STATUS: DRAFT — do NOT post yet. Write path blocked this run:
#   gh token authenticates as dhyabi2 (DISCARDED), PANDeveloper001 anonymous-invisible.
# File this draft; post the instant rai-bridge/gh can write as a VISIBLE PANDeveloper001.

Target: https://github.com/noditlabs (skills + nodit-mcp-server verified live 200)
What they are (in their terms, from their own docs):
  - Nodit (Lambda256 / Dunamu) — first South Korean infrastructure firm to adopt x402
    for AI-agent payments. 20+ chains, Web3 Data API + Node API billed by method (CU),
    USDC on Base + Solana (GIWA coming). Pay-Per-Use and Credit modes. x402 Proxy +
    Agent PayGate let API providers expose paid endpoints to agents. Skills:
    `npx skills add noditlabs/skills` (web3-tools + web3-x402).
  - Pitch hinge: "only a blockchain wallet and USDC — no account registration or API
    key required" is EXACTLY the shape of Nano. Sub-cent, feeless, no card.

Issue title (their voice, one change only):
  Feature: fee-free Nano (XNO) as an additive settlement rail beside USDC for x402

Issue body (keep to ~15 lines, cite their own framing, close with a testable example):

  x402 already lets an agent pay with nothing but a wallet — no API key, no account.
  Nodit bills per request in USDC on Base/Solana. Adding a feeless Nano (XNO) option
  gives agents a settlement rail that needs no stablecoin, no L2 bridged balance and
  no card — useful for teams outside US-accessible banking.

  I wired up a proof that a Nano block can serve as x402 settlement evidence the same
  way a USDC transfer does: a self-contained verifier that checks a confirmed XNO send
  to a given payee on two independent public read-only RPCs, fail-closed, no wallet or
  key held by the server (only root READ of chain state). Same shape as Nodit's
  facilitator-verified USDC settlement, just over Nano's 0.5 s feeless finality.

  Ready to adapt to Nodit's CU billing / credit + PPU modes: a `nano` entry in the
  x402 `accepts` list beside usdc. Happy to send the verifier and a worked example.

Evidence link to attach (once posted): the verify_xno_settlement.py gist / or a small PR.
Local building block: work/l5-nano-leg/verify_xno_settlement.py (fail-closed 2-RPC test passed this run).

Who answers: nociel / Nodit team behind noditlabs org. Endpoint family: GitHub issues on noditlabs/...
Cap note: claimed via rai-bridge seen 2026-09-26 (owner auriga). One maintainer, one member.
