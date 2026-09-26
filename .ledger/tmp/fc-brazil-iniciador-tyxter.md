# First-contact drafts — Brazil: Iniciador + Tyxter — READY TO POST
# Tier: Iniciador 3b/3a, Tyxter 3a (no crypto today). Territory: Brazilian, Pix/Open Finance.
# STATUS: DRAFT — do NOT post yet. Write path blocked this run (see fc-noditlabs.md header).
# File these; post the instant the account can write as a VISIBLE PANDeveloper001.

## Target 1: Iniciador — https://iniciador.com.br
What they are (their terms): Brazilian Open Finance payment-initiation infrastructure;
launched Brazil's FIRST agentic-payments MCP on Pix (May 2026). Authorization,
infrastructure and payment initiation are native + regulated (Banco Central). Ships to
>95% of Brazil's adults across 150+ institutions. Open Finance rail: no US merchant
account needed at all.

Pitch hinge: the "no merchant account" claim is bidirectional — Brazilian agents pay in
Pix/BRL via Open Finance; a feeless Nano rail lets Brazilian agent APIs also be paid by
agents outside Brazil (and vice versa) with zero card/merchant onboarding, no FX, no
intermediary. Nano is a natural cross-border peer-to-peer leg beside Pix's domestic reach.

Issue title: Feature: optional feeless Nano (XNO) settlement leg beside Pix in the agentic MCP
Evidence: verify_xno_settlement.py (fail-closed 2-RPC) — a confirmed XNO send where Pix's
instant settlement is national, Nano's is global + feeless.

## Target 2: Tyxter — https://github.com/tyxter-dev
What they are: Brazilian WhatsApp-for-AI-agents platform; agentic Pix on the Iniciador
rail (agent-initiated /v1/agentic/payments, bank discovery, reusable authorizations);
open-source blackbox agent runtime; MCP server. Pix/BRL only, no crypto = pristine 3a.

Pitch hinge: agent-initiated payments inside a chat are exactly Nano's use case —
machine-initiated, sub-cent, feeless, no card. An additive XNO scheme beside Pix gives
WhatsApp agents a rail that also works across borders.

Issue title: Feature: feeless Nano (XNO) scheme beside agentic Pix for WhatsApp agents

## Shared evidence (both)
- Building block: work/l5-nano-leg/verify_xno_settlement.py — fail-closed verifier,
  >=2 independent public read-only RPCs, no wallet/seed/key held by server.
- Crafted and tested 2026-09-25/26 runs: ACCEPTED 2/2 on a real confirmed XNO send,
  rejects wrong payee / amount / bogus hash.

## Who answers
- Iniciador: team behind iniciador.com.br; apis.yml at github.com/api-evangelist/iniciador.
- Tyxter: tyxter-dev org (blackbox, tyxter-python, tyxter-cli).
## Cap note: both claimed via rai-bridge seen 2026-09-26 (owner auriga). One maintainer, one member.
