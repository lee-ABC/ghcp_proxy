# Sub2API Excel account-pool companion

This directory publishes the private account-pool transport used with smart-sub2. It is a patch for **Kaixxrua/excel-codex-bridge**, not a replacement for this repository's Copilot application. The root application's GPT-6 Excel alias support was already published in commit b2f6bff.

## Apply

```sh
git clone https://github.com/Kaixxrua/excel-codex-bridge.git
git -C excel-codex-bridge checkout 8a277dfcdbb647d2ef4d714e31b6a98260a63a79
bash integrations/sub2api/apply.sh ./excel-codex-bridge
```

Run the last command from this ghcp_proxy checkout. The script verifies the pinned revision and tracked working-tree cleanliness before applying. Build using the patched bridge's existing `packaging/sub2api/Dockerfile`. Upstream license texts are retained alongside the patch.

## Runtime contract

- Private endpoint: `/internal/v1/responses`. Only a separately authenticated private transport request may supply the selected OAuth account identity.
- Public API credential: `EXCEL_SUB2API_API_KEY`; administration credential: `EXCEL_SUB2API_ADMIN_KEY`; private transport credential: `EXCEL_SUB2API_TRANSPORT_KEY` or `EXCEL_SUB2API_TRANSPORT_KEY_FILE`. Use distinct secrets.
- Keep the service reachable only on a private container network or loopback; no public unauthenticated port.
- The selected account, proxy and replay context are scoped per request. Do not re-enable the obsolete global account-session synchronization timer for this pool deployment.
- Smart-sub2 retains group/account scheduling and native routing for unsupported Excel models. This companion does not use Copilot to select the Sub2 group.

The bundle contains source/tests only: no tokens, account exports or production configuration. To undo on the same source tree, use `git apply -R integrations/sub2api/excel-codex-bridge.patch` with the correct absolute patch path from the bridge checkout.
