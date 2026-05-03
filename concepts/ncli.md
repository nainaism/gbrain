---
title: ncli
slug: concepts/ncli
type: concepts
---

# ncli

Notion CLIツール。OAuth認証によるNotion APIアクセスを提供する。

## State
- バージョン: 最新（bun global）
- インストール: `/opt/homebrew/bin/ncli`
- プロファイル: NCLI_WORKSPACE_DIR環境変数で切り替え
  - nainaism: `~/.hermes/workspaces/nainaism/`
  - luxerio: `~/.hermes/workspaces/luxerio/`

### 認証
- MCP OAuth方式（ブラウザ認証）
- プロファイル切り替え時の注意: `HOME=` でプロファイル分離が必要
- ncli本体は `NCLI_WORKSPACE_DIR` を参照せず `envPaths("ncli")` 固定（本体パッチNG）

### 既知のバグ
- **Token消失**: localhost HTTP serverのポート不一致で `tokenStore.deleteClientInfo()` が発火。global `client.` が上書きされる。
  -対策: `NCLI_WORKSPACE_DIR` 指定時でもglobal pathに書き込む仕様 → wrapperでHOME=分離
  - 恒久対策: `tokenStore.deleteClientInfo()` を無効化するパッチ適用済み
- **並列実行不可**: nainaism/luxerio同時実行でlock競合 → client消失（4/23確認）

### 関連スキル
- `ncli`: 全Notion操作のプライマリスキル。read/write/whoami wrapper使用
- `ncli-ai`: Notion AI（BrowserBridge経由）
- wrapper scripts: `~/.openclaw/skills/ncli/` (ncli-direct.sh, ncli-wrapper.sh, ncli-safe-login.sh)

## See Also
- concepts/hermes-agent
- companies/nainaism

## Timeline
- 2026-04-23: Token消失バグ発見・パッチ適用
- 2026-04-27: 6スキルのworkspaceパス更新（~/.openclaw/ → ~/.hermes/workspaces/）
- 2026-04-29: GBrainページ作成
