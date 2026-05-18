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

### RTK CLI（5/13導入）
- brew経由でv0.39.0インストール済み（`/opt/homebrew/bin/rtk`）
- rtk-hermes plugin v1.2.3（Hermes venvにpip install済み）
- config.yaml `rtk-rewrite` enabled
- モード: `rewrite`（デフォルト、コマンド自動書き換え）/ `suggest`（候補のみ）/ `off`
- 環境変数: `RTK_HERMES_MODE`, `RTK_HERMES_TIMEOUT_MS`（デフォルト2000ms）
- テスト期間: 5/13〜6/13

### Providers（5/12更新）
- **ZAI**: メインプロバイダ（glm-5.1）。cronジョブ統一モデル
- **Ollama Cloud**: サブプロバイダ。ハカセCTO・はなびCMOはOllamaをメインに設定変更可能
- **OpenCode Go**: 5/4追加。環境変数 `OPENCODE_GO_API_KEY` + `OPENCODE_GO_BASE_URL`。provider名: `opencode-go`、デフォルトモデル: `deepseek-v4-flash`。全5プロファイル（COO/CTO/CMO/CFO/PUGOKA）に設定済み
  - HindsightのLLMもopencode-go deepseek-v4-flashに統一（5/5）
- **TinyFish**: 5/11追加。web.search_backend + web.extract_backend。環境変数 `TINYFISH_API_KEY`。全4プロファイル（COO/CTO/CMO/CFO）に設定完了。パグオカは未設定
- **Crof.ai**: 5/18追加。つき(CFO)のプライマリプロバイダー変更（glm-5.1-precision → deepseek-v4-pro）。provider名: `crof-ai`

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

### Kanban（5/12更新）
- **アーキテクチャ**: SQLiteベースのタスク管理（`~/.hermes/kanban.db`）。dispatcher + worker構成、単一ホスト専用
- **Toolset**: `kanban_*` ツール群（create/list/show/comment/block/unblock）。workerは`_check_kanban_mode()`で自動有効化（HERMES_KANBAN_TASK環境変数）
- **Discord通知**: gatewayの`_kanban_notifier_watcher`が5秒ポーリングでイベント検知→自動通知。完了・ブロック等がDiscordに即時反映
- **HITL**: P5 Human-in-the-loopパターン。block/unblock/commentで人間が介入可能。`/kanban` slash command or 自然言語からtool call
- **Notion同期**: kanban-notion-syncスキル作成済み（5/9）。一方通行同期の詳細設計あり。ステータスマッピング7→6状態、assignee→Leader relation等の課題解決済み
- **Job ↔ Kanban 1:Nモデル**: 5/13設計確定、5/15大幅改修。Job（Notion）を1:NでKanban tasksに分解して自律実行。意味単位分解・Sync動的再プランニング・`--skill`注入で再帰的調整可能
- **Webhook自動起動**: 5/13実装。job-queue-poller（launchd 5分間隔、ncli、LLM不使用）がDB_factory_jobsをチェック→HMAC署名付きPOSTでlocalhost:8644/webhooks/job-queue→かえで自動起動→Kanban tasks分解
- **Parent-completion invariant**: 5/12復元。claim_taskが親未完了の子タスクのclaimを拒否（CAS UPDATE前regressionチェック）。E2E検証済み
- **curl -d & 背景**: terminal toolで`-d`に`&`を含むインラインJSONを書くとbackgrounding誤検知→ブロック。`-d @/tmp/file.json`で回避（5/13確認）
- **coo profile**: `~/.hermes/profiles/coo/`（空ディレクトリ）が存在し、dispatcherが認識する。以前`default`との混同で`assignee=coo`がspawnされない問題があった（5/11解決: symlink→空ディレクトリ）
- **Kanban × Goal flow**: Research Jobのserial chain実績あり（t_35caed22→t_65ee25d7→t_d2606a52、5/11）
- **Notion DB_factory_jobs Status許容値**: Draft, Queued, Running, Blocked, Done, Failed（「In Progress」は不可）
- **`--skill`フラグ**: `hermes kanban create --skill <name>`でタスク作成時にスキルを強制ロード。spawnされたworkerが自動でスキルを読む（5/15確認）

### Skill管理
- skills.disabled: opencode（ゾンビプロセス問題により4/30無効化。delegate_taskがopencode serveを終了させずメモリ肥大化）
- Curator機能（自動スキル保守）: upstream/hermes/curator-infraブランチで開発中、main未マージ

### Paseo ACP統合（5/18実装）
- ACP（Agent Communication Protocol）経由でPaseoデスクトップアプリからhermes-coo/hermes-cfoと対話
- カスタムプロバイダーアイコン: かえで🐕 = `kaede-icon.tsx`（柴犬シルエット）、つき🐰 = `tsuki-icon.tsx`（ウサギシルエット）
- `provider-icons.ts` で `hermes-coo` → 柴犬、`hermes-cfo` → ウサギ マッピング
- ビルドバージョン: Paseo v0.1.57-rc.1（5/18）
- **コード署名注意**: ad-hoc署名（identityName=- identityHash=none）はmacOS Gatekeeperで弾かれる。回避策: 既存署名済み.appのJSバンドルだけ差し替え、または `xattr -cr /Applications/Paseo.app`
- index.htmlのバンドル名参照ズレ注意: リビルド後はindex.html内のJS filename参照も更新が必要（5/18確認）

### 既知の問題
- [SILENT]強調しすぎるとLLMがスクリプト実行をスキップする（アンチパターン）
- opencode serveがゾンビプロセス化しやすい（TUI終了時にserve残存、delegate_taskのcleanup漏れ）
- Notion AIの`ask`コマンドがcron contextでサイレント失敗する（5/4確認。workspace switch→message送信は成功扱いだがhistory=[]で応答なし）

### Computer Use（5/13有効化）
- cua-driver v0.1.9インストール済み（`hermes tools enable computer_use`で有効化）
- macOSアクセシビリティ・画面収録権限付与済み
- テストで20要素検出確認（5/13）

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
- **2026-05-11** | TinyFish web provider設定（COO/CTO/CMO/CFO）。coo profile問題解決（mkdir -p ~/.hermes/profiles/coo/）。Kanban×Goal serial chain初実績
- **2026-05-12** | claim_task parent-completion invariant復元。ACP adapter fallback_model/credential_pool fix（401 crash回避）
- **2026-05-13** | Job↔Kanban 1:Nモデル確定。Webhook自動起動実装・E2E完了。RTK CLI v0.39.0 + rtk-hermes plugin導入（テスト期間5/13〜6/13）。curl -d & 背景誤検知pitfall確認。cua-driver v0.1.9インストール・computer_use有効化
- **2026-05-15** | job-orchestrator大幅改修（意味単位分解・Sync動的再プランニング・`--skill`フラグ注入・Report確実送信）
- **2026-05-18** | Crof.ai provider追加（つきCFO プライマリ deepseek-v4-pro）。Paseo ACPカスタムアイコン実装（かえで🐕・つき🐰）