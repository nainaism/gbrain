---
title: Hindsight
slug: concepts/hindsight
type: concepts
---

# Hindsight

長期記憶プロバイダー（vectorize-io/hindsight）。エージェントの会話事実をベクトルストアに保存。

## State
- バックエンド: Docker (port 8888), Guard Proxy (port 8887)
- Banks: coo (かえで), cto (ハカセ), pugoka (パグオカ)
- LLM: kimi-k2.6 (ZAI直通)（5/3変更。Ollama Cloud推論バックエンド障害で429/timeout連発→ZAI直通に切替）
- 設定: profiles/{name}/hindsight/config.json（bankId必須、欠落=retain不達）
- Guard Proxy: ~/.hindsight/guard_proxy.py (DELETE保護)

### 特徴
- 非構造化ファクトのベクトル蓄積
- セマンティック検索（自動prefetch）
- sync_turnで会話ターンを自動保存
- 個別削除はバグあり（bank resetのみ安全）

### 既知の問題
- **Ollama Cloud推論障害**: 5/2にOllama Cloudの/chat/completionsエンドポイント全体がtimeout。/v1/modelsは正常。auth通るが推論エンジン不応答。ZAI直通は正常。→ LLMをZAI直通kimi-k2.6に切替で解決（5/3）
- **429 Rate Limit**: glm-4.7 (Ollama Cloud) で頻発（4/24確認）→ cron jobs遅延・スキップ
  - ZAI直通とOllama Cloud経由でrate limitは独立
  - Ollama Cloudはプロキシ経由
- **Docker再起動**: Guard proxyの再起動が必要
- **Stale pending tasks**: 古いworker IDでpendingが停滞する
  - 回避: `SKIP_LLM_VERIFICATION=true`

### Hindsight API (cron context用)
- MCPツールはcron contextで使えない → HTTP API直接呼び出し
- `POST http://localhost:8888/v1/default/banks/{bank}/memories/recall`
- `POST http://localhost:8888/v1/default/banks/{bank}/memories` (retain)

### GBrainとの関係
- Hindsightはエピソード記憶（「いつ何が起きた」）
- GBrainは構造化知識（「何が事実として正しい」）
- Dream Cycle Step 1-3でHindsight→GBrainに蒸留して同期

## See Also
- concepts/hermes-agent
- concepts/gbrain

## Timeline
- 2026-04-12: Brainページ作成
- 2026-04-22: glm-4.7経由retain動作確認
- 2026-04-24: 429 rate limit問題確認
