---
title: GBrain
slug: gbrain
type: concepts
---

# GBrain

Garry Tan作のパーソナルナレッジベースシステム。MCPサーバー経由でHermesに統合。

## State
- バージョン: v0.22.6.1（4/28 git cloneで再インストール）
- インストール: `git clone garrytan/gbrain && bun install -g`（bun install -g github:... はNG → PGLite WASM Issue #218）
- エンジン: PGLite (local embedded Postgres)
- ストレージ: ~/.gbrain/brain.pglite
- Brainディレクトリ: ~/ai-factory/gbrain/coo/ (git管理)
- Embeddings: OpenRouter経由 text-embedding-3-large (1536 dim)
- 環境変数: `source ~/.hermes/.env` → `OPENAI_API_KEY=$OPENROUTER_API_KEY` → `OPENAI_BASE_URL=https://openrouter.ai/api/v1`
- Ollama Cloud Pro: embedding未対応。OpenRouterのみ。

### 既知の問題
- **PGLite WASM Issue #223**: runtime initialization error → v0.22.6.1で修正済み（forward reference bootstrap）
- **PGLite WASM Issue #218**: `bun install -g github:...` でインストールすると発生 → git cloneで回避
- **0.18.1 schema bug**: PATH問題でWEDGED状態 → `sources`テーブル手動作成 + `init --migrate-only` + `apply-migrations` で3段階修復
- **Autopilot/CLI排他**: PGLite lock競合 → CLI実行前にautopilot stop必須
- **Config path注意**: config.jsonのdatabase_pathがtest pathのままになるとエラー継続

### Dream Cycle（4:00 JST cron）
- Step 1: Signal Sync（セッション + Hindsight → GBrain）— Hindsightは第一級入力源
- Step 2: Activity Chronicle → Hindsight retain + GBrain反映
- Step 3-4: Hindsight/Autopilot Watchdog
- Step 5: PGLite Lock Contention対応
- Step 6-11: リンク検証・ページ再合成・Health Check・Embedding再生成
- Step 12: Git Commit（全変更をまとめて）

### Embed Sync（毎時 cron）
- `gbrain embed --all` + git push + doctor

### Hindsightとの棲み分け
- Hindsight: 会話の事実・イベント（自動保存）
- GBrain: 人・会社・概念の構造化ナレッジ（蒸馏して反映）
- エピソード（「いつ何が起きた」）→ GBrainには載せない
- 事実（「何が正しいか」）に蒸留してからGBrainに反映

## See Also
- concepts/hermes-agent
- concepts/hindsight

## Timeline
- 2026-04-12: 導入プロジェクト開始
- 2026-04-23: gbrain 0.18.1 schema bug → 3段階修復
- 2026-04-28: v0.22.6.1再インストール（git clone法）、PGLite WASM修正確認
- 2026-04-29: Dream Cycle Step 1-3改善（Hindsight第一級入力源化）、Step 2 GBrain反映追加
