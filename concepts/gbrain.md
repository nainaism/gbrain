---
title: GBrain
slug: concepts/gbrain
type: concepts
---

# GBrain

Garry Tan作のパーソナルナレッジベースシステム。MCPサーバー経由でHermesに統合。

## State
- バージョン: v0.22.6.1（4/28 git cloneで再インストール）
- インストール: `git clone garrytan/gbrain && bun link`（bun install -g github:... はNG → PGLite WASM Issue #218）
- **エンジン: PostgreSQL（Docker container、5/3移行完了）**
  - `~/.gbrain/config.json`: `{"engine":"postgres","database_url":"postgresql://gbrain:***@localhost:5432/gbrain"}`
  - PGLiteロック競合問題が解消（autopilot/CLI並行動作可能）
  - Embeddings: OpenRouter経由 text-embedding-3-large (1536 dim)
  - 環境変数: `source ~/.hermes/.env` → `OPENAI_API_KEY=$OPENROUTER_API_KEY` → `OPENAI_BASE_URL=https://openrouter.ai/api/v1`
- Brainディレクトリ: ~/ai-factory/gbrain/coo/ (git管理)

### 既知の問題
- **PGLite WASM Issue #223**: runtime initialization error → v0.22.6.1で修正済み（forward reference bootstrap）※PostgreSQL移行で実質無関係化
- **PGLite WASM Issue #218**: `bun install -g github:...` でインストールすると発生 → git cloneで回避
- **0.18.1 schema bug**: PATH問題でWEDGED状態 → `sources`テーブル手動作成 + `init --migrate-only` + `apply-migrations` で3段階修復
- **OpenRouter 402 credit limit**: クレジット枯渇時はembed全失敗。PGLite非依存のエラー（5/3確認）
- **OpenRouter response format mismatch**: embed --allが全ページで `undefined is not an object` で失敗することがある（5/3確認）
- **Autopilot launchd KeepAlive**: CLI実行中にautopilotが再起動してPGLite lockを再取得する罠（5/3確認）※PostgreSQL移行で軽減

### Dream Cycle（4:00 JST cron）
- Step 1: Signal Sync（セッション + Hindsight → GBrain）— Hindsightは第一級入力源
- Step 2: Activity Chronicle → Hindsight retain + GBrain反映
- Step 3-4: Hindsight/Autopilot Watchdog
- Step 5: Lock Contention対応（PostgreSQL移行で軽減済み）
- Step 6-11: リンク検証・ページ再合成・Health Check・Embedding再生成
- Step 12: Git Commit（全変更をまとめて）

### Embed Sync（毎時 cron）
- `gbrain embed --stale` + git push + doctor
- **注意**: `--all`はOpenRouter rate limitで壊れる（CONCURRENCY=20で429 → response.data undefined）。必ず`--stale`を使うこと（4/29確認）

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
- 2026-05-03: PostgreSQL（Docker）移行完了。PGLiteロック競合解消。
