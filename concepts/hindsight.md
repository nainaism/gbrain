# Hindsight

長期記憶プロバイダー（vectorize-io/hindsight）。エージェントの会話事実をベクトルストアに保存。

## State
- バックエンド: Docker (port 8888), Guard Proxy (port 8887)
- Bank: coo (かえで), cto (ハカセ)
- LLM: glm-4.7 (z.ai)
- 設定: ~/.hermes/hindsight/config.json
- Guard Proxy: ~/.hindsight/guard_proxy.py (DELETE保護)

### 特徴
- 非構造化ファクトのベクトル蓄積
- セマンティック検索（自動prefetch）
- sync_turnで会話ターンを自動保存
- 個別削除はバグあり（bank resetのみ安全）

## See Also
- concepts/hermes-agent
- concepts/gbrain

## Timeline
- 2026-04-12: Brainページ作成
