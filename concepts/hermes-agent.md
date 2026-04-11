# Hermes Agent

オープンソースのAIエージェントフレームワーク（NousResearch/hermes-agent）。ai-factoryの基盤。

## State
- リポジトリ: nainaism/hermes-agent (fork), upstream: NousResearch/hermes-agent
- インストール先: ~/.hermes/hermes-agent/
- バージョン管理: main=upstream同期, nainaism=パッチ
- MCP対応: stdio + HTTP servers
- ネイティブメモリ: Hindsight (vectorize-io)
- 設定: ~/.hermes/config.yaml

### 再起動方法
- COO: `launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway`
- CTO: `launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway-cto`
- 絶対に `kill <pid>` 禁止（launchd KeepAliveと競合）

## See Also
- people/kaede
- concepts/ai-factory

## Timeline
- 2026-04-12: Brainページ作成
