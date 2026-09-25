From: dhyabi2
Host: github.com

Body:
Optional feeless Nano (XNO) settle asset beside USDC/EUROe for the sub-cent tier

Summary:
Adds Nano (XNO) as one more accept entry beside USDC/EUROe in MCPay's x402 proxy — additive, opt-in, no existing flow changes. MCPay verifies the on-chain payment today; a Nano block hash verifies the same way.

Why it fits MCPay:
MCPay's pitch: on-chain payments for any MCP server, pay-per-call, no subscriptions, no API keys. It verifies the on-chain (USDC/EUROe on EVM) payment, retries the MCP request on confirmation, and streams usage to dashboards. That pay-per-call, sub-cent shape is exactly where a feeless settle asset earns its place.

- One asset in the same envelope. Nano is another accept entry: scheme=nano:mainnet, asset=XNO, payTo=nano_.... No new wire, no new proxy logic — verify a Nano block hash the way it verifies an EVM tx hash today.
- Feeless and final by the asset's nature. USDC/EUROe on EVM carry gas and per-settlement cost that does not shrink with the ticket. Nano has no gas and no transfer fee: a $0.001 or $0.0001 per-call charge settles at exactly zero, flat, final in ~1 s. That is precisely the "pay only for what you use" tier MCPay's README describes, where a gas-bearing rail is proportionally most expensive.
- Real standard, not a custom rail. The nano:mainnet CAIP-2 identifier is already part of the x402 scheme work (x402nano/exact), with a live MIT implementation in Feeless402/feeless402 (an x402 client/merchant with a Nano wallet) and dhyabi2/openai-agents-nano-x402 (an OpenAI-Agents-SDK tool that already settles paid calls in self-custodied XNO). Everything indexed at https://hub.nano.org — MCPay builds no payment logic from scratch.

What this PR adds:
1. A Nano settle asset entry in the MCPay accept/price surface (additive — USDC/EUROe untouched), with the nano:mainnet scheme and XNO asset.
2. A verify path stub that treats a confirmed Nano block hash the way the EVM path treats a tx hash — same lifecycle: verify, retry on confirmation, stream usage. No new payment logic; reuses the public ledger property (any client can read a confirmed block with no secret).
3. A note pointing to the live references: x402nano/exact, Fealess402/feeless402, openai-agents-nano-x402, hub.nano.org.

Test / verify:
- The existing MCPay proxy test surface stays green for USDC/EUROe.
- A Nano accept entry is present in the price/accepts surface and is opt-in.
- A BILLING_SETTLEMENT-style check for a Nano block hash is wired the same way the EVM one is.

Caveat:
Nano settlement is free whether the ticket is $1 or $0.0001 — that is the whole point for a pay-per-call rail. If MCPay's scope is deliberately USDC/EUROe-only for now, that is a fair call and I'll close this; but a proxy that promises "pay only for what you use, automatically" names the sub-cent micropayment tier and omits the only truly feeless, final-in-a-second settle asset.
