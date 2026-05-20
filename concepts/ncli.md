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
- **npm updateでパッチ消失**: `npm update` が `NCLI_WORKSPACE_DIR` パッチとポートパッチを上書きする（5/20確認）。再適用手順: `grep 'NCLI_WORKSPACE_DIR' node_modules/@anthropic-ai/notion-cli/build/cli.js` で確認、消失時はパッチ再適用
- **tokens.jsonパス不一致**: wrapper(`ncli-direct.sh`)は `~/.config/ncli-profiles/nainaism/.../ncli/` を探すが、グローバルは `~/Library/Preferences/ncli/` に保存する。認証後に対象ディレクトリにコピーが必要（5/20確認）

### 関連スキル
- `ncli`: 全Notion操作のプライマリスキル。read/write/whoami wrapper使用
- `ncli-ai`: Notion AI（BrowserBridge経由）
- wrapper scripts: `~/.openclaw/skills/ncli/` (ncli-direct.sh, ncli-wrapper.sh, ncli-safe-login.sh)

## See Also
- [[concepts/hermes-agent]]
- [[companies/nainaism]]

## Timeline
- **2026-04-23** | Token消失バグ発見・パッチ適用
- **2026-04-27** | 6スキルのworkspaceパス更新（~/.openclaw/ → ~/.hermes/workspaces/）
- **2026-04-29** | GBrainページ作成
- **2026-05-20** | npm updateでNCLI_WORKSPACE_DIRパッチ・ポートパッチが消失、tokens.jsonパス不一致でClient ID mismatch誤診断
