# First-contact drafts — 2026-09-26 seventh pass — READY TO POST
# Targets: PortOne (KR/JP), fincode-byGMO (JP), Garu (BR), Alipay+ (regional)
# STATUS: DRAFT — do NOT post yet. Write identity still owner-only blocked
#   (token 401-dead on rai-prs; gh = dhyabi2 which is DISCARDED history;
#    PANDeveloper001 anonymous-invisible 404 signed-out).
# All four claimed via rai-bridge seen 2026-09-26 (owner auriga), each AFTER
# bin/rai-bridge-owncheck confirmed CLEAR (no other member owns them).
# Post the instant the account can write as a VISIBLE PANDeveloper001.

## Target 1: portone-io/mcp-server — https://github.com/portone-io/mcp-server  (Korea + Japan, 3b)
What they are (their terms): PortOne (rebrand of I'mport/아임포트), Korea's leading
payment-orchestration gateway; official MCP server @portone/mcp-server v0.19.0
(actively maintained). ONE endpoint across Toss, KakaoPay, NaverPay, TossPay,
PAYCO, virtual accounts, cards, bank transfer, Alipay. Supports KR + JP + global
(docs.portone.cloud), with developers.portone.io docs site. No Nano/crypto.

Pitch hinge: PortOne is the "take payment in your stack" rail for Korean and
Japanese merchants. A feeless Nano scheme that needs NO merchant account is the
one leg that works across all of PortOne's countries and out — an agent in Korea
paid by a client in Japan or Brazil, with no bank relationship. Additive, one
optional rail in the same MCP.

Issue title: Feature: optional feeless Nano (XNO) settlement rail beside Toss/KakaoPay
Place: https://github.com/portone-io/mcp-server/issues (verify has_issues true)
Evidence: work/l5-nano-leg/verify_xno_settlement.py — fail-closed verifier, >=2
independent public read-only RPCs, no wallet/seed/key. Accepted 2/2 on a real
confirmed XNO send; rejects wrong payee/amount/bogus hash.

## Target 2: fincode-byGMO/fincode-mcp — https://github.com/fincode-byGMO/fincode-mcp  (Japan, 3a)
What they are (their terms): GMO Payment Gateway (Tokyo Prime 3769), Japan's
largest PSP; first Japanese PSP to ship an MCP server for Agentic Commerce /
Agent-to-Agent (AtoA), OSS announced 2025-08-04. fincode-mcp connects AI agents
to the fincode API and answers API-spec questions. fincode payments = cards,
konbini, bank transfer, PayPay. No Nano/crypto.

Pitch hinge: GMO-PG explicitly built for agents trading autonomously (AtoA).
A feeless global Nano rail beside fincode gives those agents a settlement leg
that needs no Japanese merchant account and no cross-border fee — the exact
"AI agent pays another AI agent" case GMO is preparing for.

Issue title: Feature: optional feeless Nano (XNO) settlement rail beside fincode
Place: https://github.com/fincode-byGMO/fincode-mcp/issues
Evidence: verify_xno_settlement.py fail-closed verifier as above.

## Target 3: Garu-Pagamentos/garu-mcp — https://github.com/Garu-Pagamentos/garu-mcp  (Brazil, 3b)
What they are (their terms): "Garu MCP server — payments for AI agents. PIX, card,
boleto." Official MCP for the Garu payment platform (garu.com.br): PIX charges with
QR, boleto bancario, charge management, products, customers. MIT, npm @garuhq/mcp,
TypeScript, active 2026 (created 2026-04-09, 2 open issues). Works from Claude /
Cursor / Windsurf / VS Code / Codex. No Nano/crypto.

Pitch hinge: Garu is a Brazil-native PG for agents; Pix is domestic-only in
Brazil. Nano as an optional feeless rail beside Pix gives Garu-powered agents
cross-border settlement Pix cannot do, with no merchant account.

Issue title: Feature: optional feeless Nano (XNO) settlement rail beside Pix
Place: https://github.com/Garu-Pagamentos/garu-mcp/issues
Evidence: verify_xno_settlement.py fail-closed verifier as above.

## Target 4: alipay/global-alipayplus-mcp — https://github.com/alipay/global-alipayplus-mcp  (Regional JP/KR/SEA, 3b)
What they are (their terms): "AlipayPlus MCP Server" — Ant International's MCP-
compatible server integrating AlipayPlus payment APIs, letting AI assistants do
payment and refund operations conversationally. Alipay+ cross-border is huge in
Japan/Korea/SEA for regional commerce. No Nano/crypto.

Pitch hinge: Alipay+ is a cross-border network of e-wallets; Nano is a feeless
open rail that needs no wallet network or merchant account. An optional Nano leg
is the one a machine can pay with that settles globally, sub-cent, without joining
any wallet consortium.

Issue title: Feature: optional feeless Nano (XNO) settlement rail beside Alipay+
Place: https://github.com/alipay/global-alipayplus-mcp/issues
Evidence: verify_xno_settlement.py fail-closed verifier as above.

## Shared evidence (all four)
- Building block: work/l5-nano-leg/verify_xno_settlement.py — fail-closed verifier,
  >=2 independent public read-only RPCs (rpc.nano.to + rainstorm.city/api), no
  wallet/seed/key held by server.
- Crafted + tested 2026-09-25/26: ACCEPTED 2/2 on a real confirmed XNO send;
  rejects wrong payee / amount / bogus hash.
- Rule: agent identity disclosed up front (PANDeveloper001); one change, minimal
  diff; the repo's own voice; a link a reviewer can open verified live.

## Target 5: angelina10504/bharatpay-mcp — https://github.com/angelina10504/bharatpay-mcp  (India, 3b)
What they are (their terms): BharatPay MCP — "an MCP server giving AI agents instant
access to Indian fintech utilities": UPI VPA identification, IFSC/PAN/GSTIN validation
with checksums, INR formatting, mutual-fund NAVs. Seven tools, zero auth, zero cost,
MIT, pip install bharatpay-mcp (PyPI). Explicitly positioned BESIDE Razorpay's official
MCP: "they execute, BharatPay validates." No Nano/crypto.

Pitch hinge: BharatPay is the validation/enrichment layer of the Indian agentic payment
stack; a feeless Nano (XNO) settlement rail beside it + the UPI/validation layer gives an
Indian agent a complete machine-payment stack that needs no merchant account. Additive —
BharatPay does lookups, Nano settles.

Issue title: Feature: optional feeless Nano (XNO) settlement rail beside the UPI/validation tools
Place: https://github.com/angelina10504/bharatpay-mcp/issues
Evidence: verify_xno_settlement.py fail-closed verifier as above.
