# GBrain

Garry Tan作のパーソナルナレッジベースシステム。MCPサーバー経由でHermesに統合。

## State
- バージョン: v0.7.0
- インストール: bun global (github:garrytan/gbrain)
- エンジン: PGLite (local embedded Postgres)
- ストレージ: ~/.gbrain/brain.pglite
- Brainディレクトリ: ~/brain/ (git管理)
- Embeddings: OpenRouter経由 text-embedding-3-large (1536 dim)
- Query Expansion: Anthropic Claude Haiku (APIキーなしだとスキップ)

### GBrainとのHindsightの棲み分け
- Hindsight: 会話の事実・イベント（自動保存）
- GBrain: 人・会社・概念の構造化ナレッジ（MCP経由で随時更新）
- 両方対等、優先順位なし、独立管理

## See Also
- concepts/hermes-agent
- concepts/hindsight

## Timeline
- 2026-04-12: 導入プロジェクト開始
