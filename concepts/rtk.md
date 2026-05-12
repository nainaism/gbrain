---
title: RTK CLI
slug: concepts/rtk
type: concepts
---

# RTK CLI

Terminal command optimization tool。コマンド実行前に最適化候補を提案・適用する。Hermes Agentとの統合プラグインあり。

## State
- バージョン: v0.39.0（brew経由インストール、`/opt/homebrew/bin/rtk`）
- rtk-hermes plugin: v1.2.3（Hermes venvにpip install済み）
- config.yaml: `rtk-rewrite` enabled
- テスト期間: 2026-05-13 〜 2026-06-13

### 動作モード
- **rewrite**（デフォルト）: terminalコマンド実行前に自動的に`rtk rewrite`を呼び、書き換え可能なら適用
- **suggest**: 書き換え候補をログ出力のみ（実際には書き換えない）
- **off**: 完全無効化

### 環境変数
- `RTK_HERMES_MODE`: モード切替（rewrite/suggest/off）
- `RTK_HERMES_TIMEOUT_MS`: タイムアウト（デフォルト2000ms）

## See Also
- [[concepts/hermes-agent]]

## Timeline
- **2026-05-13** | 導入・テスト期間開始