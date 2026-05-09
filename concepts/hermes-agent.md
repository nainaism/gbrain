---
type: concepts
title: Hermes Agent
---

# Hermes Agent

オープンソースのAIエージェントフレームワーク（NousResearch/hermes-agent）。ai-factoryの基盤。

## State
- リポジトリ: nainaism/hermes-agent (fork), upstream: NousResearch/hermes-agent
- インストール先: ~/.hermes/hermes-agent/
- バージョン管理: main=upstream同期, nainaism=パッチ
- MCP対応: stdio + HTTP servers
- ネイティブメモリ: Hindsight (vectorize-io)
- 設定: ~/.hermes/config.yaml
- バージョン: v0.13.0（5/8アップデート。upstream +720 commits, 25パッチ適用, 4コンフリクト解決）

### 再起動方法
- COO: `launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway`
- CTO: `launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway-cto`
- 絶対に `kill <pid>` 禁止（launchd KeepAliveと競合）

### Providers（5/5更新）
- **ZAI**: メインプロバイダ（glm-5.1）。cronジョブ統一モデル
- **Ollama Cloud**: サブプロバイダ。ハカセCTO・はなびCMOはOllamaをメインに設定変更可能
- **OpenCode Go**: 5/4追加。環境変数 `OPENCODE_GO_API_KEY` + `OPENCODE_GO_BASE_URL`。provider名: `opencode-go`、デフォルトモデル: `deepseek-v4-flash`。全5プロファイル（COO/CTO/CMO/CFO/PUGOKA）に設定済み
  - HindsightのLLMもopencode-go deepseek-v4-flashに統一（5/5）

### Cronシステム
- `cronjob` CLIでジョブ管理
- 設定: ~/.hermes/cron/jobs.json
- 全ジョブ統一モデル: `glm-5.1` + `zai` + `base_url=None`（5/1設定統一。以前はOllama URL混在で401エラー）
- deliver=null: ローカル実行（Hermes配送なし）
- [SILENT]: レスポンス先頭に配置で配送スキップ（scheduler.py+base.py検知あり）
- feedback-learning-cycle: 毎週日曜6:00 JST（SOUL.md思考プロトコルの一部、漏れ拾い）
- **429回避策**: GLM-5（ZAI）のweekly usage limit到達時、brief trigger cronに切替で回避（5/9確認。133minポッドキャスト作業中に発生）

### LCM (Lossless Context Management)
- context.engine: lcm
- submodule: plugins/context_engine/lcm/
- LCM_FRESH_TAIL_COUNT: 24, LCM_LEAF_CHUNK_TOKENS: 5000, LCM_DYNAMIC_LEAF_CHUNK_ENABLED: true
- 圧縮不发火条件: large tool outputでbacklogがfresh_tail外に落ちてthreshold 20000を下回る（4/23確認）
- 詳細: `devops/lcm-compression-troubleshoot` スキル参照

### Kanban（5/10調査）
- **アーキテクチャ**: SQLiteベースのタスク管理（`~/.hermes/kanban.db`）。dispatcher + worker構成、単一ホスト専用
- **Toolset**: `kanban_*` ツール群（create/list/show/comment/block/unblock）。workerは`_check_kanban_mode()`で自動有効化（HERMES_KANBAN_TASK環境変数）
- **Discord通知**: gatewayの`_kanban_notifier_watcher`が5秒ポーリングでイベント検知→自動通知。完了・ブロック等がDiscordに即時反映
- **HITL**: P5 Human-in-the-loopパターン。block/unblock/commentで人間が介入可能。`/kanban` slash command or 自然言語からtool call
- **Notion同期**: 未実装（5/10設計完了。一方通行同期の詳細設計あり。ステータスマッピング7→6状態、assignee→Leader relation等の課題解決済み）
- **現状**: kanban toolsetはどのプロファイルのconfig.yamlでも有効化されていない（5/10確認）。有効化には各プロファイルのtoolsetsに`kanban`を追加必要
- **Notion移行検討**: 成田さん「今のNotionタスク管理（PD/Worker cron）がうまく動いていない」。Kanban導入で安定化の可能性（SQLite即時反映 vs Notion API遅延、構造的アサイン vs LLM毎回判定）

### Skill管理
- skills.disabled: opencode（ゾンビプロセス問題により4/30無効化。delegate_taskがopencode serveを終了させずメモリ肥大化）
- Curator機能（自動スキル保守）: upstream/hermes/curator-infraブランチで開発中、main未マージ

### 既知の問題
- [SILENT]強調しすぎるとLLMがスクリプト実行をスキップする（アンチパターン）
- opencode serveがゾンビプロセス化しやすい（TUI終了時にserve残存、delegate_taskのcleanup漏れ）
- Notion AIの`ask`コマンドがcron contextでサイレント失敗する（5/4確認。workspace switch→message送信は成功扱いだがhistory=[]で応答なし）

## See Also
- [[people/kaede]]
- [[people/hakase]]
- [[people/hanabi]]
- [[concepts/ai-factory]]
- [[concepts/hindsight]]
- [[concepts/gbrain]]
- [[concepts/ncli]]

## Timeline
- **2026-04-12** | Brainページ作成
- **2026-04-23** | LCM圧縮不发火トラブルシュート、cron jobs設定
- **2026-04-28** | v0.10.0
- **2026-05-01** | v0.12.0「The Curator Release」確認、全cronジョブモデル統一（glm-5.1/zai）
- **2026-05-04** | OpenCode Go provider追加（全5プロファイル）、Notion AI ask cron silent failure確認
- **2026-05-08** | v0.13.0アップデート（upstream +720 commits, 4コンフリクト解決: web_tools→web_providers/, MCP resilience→upstream採用, display_config streaming除外, run_agent credential pool共存）
- **2026-05-10** | Kanban機能調査完了（アーキテクチャ・Discord HITL・Notion同期設計）。kanban-notion-sync / hermes-kanban スキル作成
