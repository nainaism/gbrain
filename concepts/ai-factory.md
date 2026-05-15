---
title: ai-factory
slug: concepts/ai-factory
type: concepts
---

# ai-factory

AIエージェントチーム（かえでCOO・ハカセCTO・はなびCMO・つきCFO）+ パグオカで構成される自律型開発・マーケティングチーム。NotionをSSOTとして運用。

## State
- エージェント: かえで(COO), ハカセ(CTO), はなび(CMO), つき(CFO), パグオカ(Luxerio業務)
- Notion Workspace: nainaism
- 通信チャネル: Discord #team-internal (1490011531692347392)
- 作業ディレクトリ: ~/ai-factory
- Spaces: ~/ai-factory/spaces/

### Key Databases
- Projects DB: collection://2bb2253a-20eb-4dee-9e00-5ee6d9bf7549
- Tasks DB: collection://478eba9e-72cd-48f5-9fa3-9d5c54c06129
- Factory Jobs DB: collection://c0bfdaa495af43b996700eb8af00fb2f

### Spaces
- nainaism: メイン（ai-factory運営）
- luxerio: Luxerio業務（Meeting Notesのみ）
- si-corp: SI役員会議（#si-corp 1491278621460140072）
- proj-kintone: SI Corp子Space。Kanban board + GitHub nainaism/proj-kintone + Notion Tasks + Discord #si-corp連携（5/14作成）

### 運用ルール
- プロジェクト管理はai-factory NotionがSSOT
- スキル変更は事前に成田さん確認必須
- git管理下のファイル変更は即座にcommit
- 長文のDiscord投稿はNotionページにしてリンク送信
- タスク完了時: Progressセクションに`成果:` + `詳細:` を必ず記載（5/1成田さん指示）
- プロジェクト完了時: 全タスクのProgressから成果を集約してプロジェクトbodyにレポート
- Discord DM報告: 概要2-3行 + Notionリンクのみ（スレッドリンク不要、5/1成田さん指示）

### Job ↔ Kanban 1:Nモデル（5/13確定, 5/15大幅改修）
- Job（Notion DB_factory_jobs）を1:NでKanban tasksに分解して自律実行
- Event-driven優先: webhook即時起動、cronはfallback
- Webhook自動起動: job-queue-poller（launchd 5分間隔）→ HMAC署名付きPOST → かえで自動起動→Kanban tasks分解
- 完全E2E確認済み: Job→Queued→webhook→orchestrator→Kanban tasks→dispatcher→done
- **意味単位分解（5/15）**: 機械的3-taskテンプレ廃止。Job内容から意味のある作業単位でタスクを分解
- **Sync = 動的再プランニング（5/15）**: 各まとまり終了後にSync挟み、成果レビュー + Notion本文追記 + 残りtodo再調整 + 新規タスク生成
- **`--skill`注入（5/15）**: Syncに`--skill job-orchestrator`注入で再帰的に動的調整可能。ReportはbodyのDelivery指示 + Notion Thread URL解決のみ

### Cron Jobs
- ambient-observer (73分): DB_x_bookmarks + DB_documents + Meeting Notes監視
- gbrain-dream-cycle (4:00): Signal Sync + Activity Chronicle + メンテナンス
- gbrain-embed-sync (毎時): Embedding再生成 + git push
- factory-radar-collector (日曜6-9時JST): 外部プロジェクト収集
- factory-radar-evaluator: Watch候補スコアリング
- factory-radar-reporter (週次): レポート生成・Discord出力
- self-evolution-weekly (日曜5:00): スキル自動最適化（テスト期間5/29迄）
- project-driver (30分): Projects/Tasks自動監視・ディスパッチ
- project-driver-daily (9:00): 日次進捗レポートDM
- project-worker: かえで担当タスク自動実行
- write-journal-digest (21:00): 日次ジャーナルダイジェスト
- factory-radar系 (週次/月次): 外部環境スキャン

### Factory Radar
- 4-set構成: Watch DB + Evaluate DB + Test DB + Execution Plan DB（4/29成田さん承認）
- 週次collector (日曜6-9時JST): 8情報ソースから革新的プロジェクト候補を収集
- evaluator: 4軸スコアリング + Hindsight参照
- reporter: 週次レポート → #team-internal
- test: 3点セット作成・期間監視・効能レポート
- fast-track: 成田さんが「導入したい」と言ったツールはWatch/EvaluateをスキップしてTest直行

### プロジェクト化基準（5/14変更）
- 意味ベース判定: 複数フェーズ必要、複数人協業、明確なマイルストーン、分解して完全な成果物を生成する必要があるもの
- 機械的ルール廃止: 工数>1週間・3+サブタスク分解可能 は削除

### スキル運用
- nainaism-blog-article: ブログ執筆ワークフロー（かえでオーサリング→はなび執筆→かえでQA→成田さんレビュー）
- blog-cover-gen: Cover画像生成（GPT-image-2）。グローバル化済み。
- space-provisioning: 新規Space追加ワークフロー（3箇所設定: ローカル/GitHub, Discord, Notion）
- kintone-reminder-notifications: kintoneリマインダー通知の運用・トラブルシューティング（5/14作成）
- kintone-js-customization: kintoneカスタムJS開発・修正ワークフロー（5/14作成）

## See Also
- [[people/narita]]
- [[people/kaede]]
- [[people/hakase]]
- [[people/hanabi]]
- [[people/tsuki]]
- [[people/pugoka]]
- [[concepts/hermes-agent]]
- [[companies/nainaism]]

## Timeline
- **2026-04-12** | Brainページ作成
- **2026-04-22** | パグオカHermes移行完了
- **2026-04-26** | Factory Radar初回セットアップ、space-provisioningスキル作成
- **2026-04-28** | nainaism-blog-articleスキル大幅更新
- **2026-04-29** | GBrain入力パイプライン統合完了（セッション+Chronicle+議事録）
- **2026-05-01** | タスク/プロジェクト完了時の報告フォーマット変更（成果詳細 + Notion集約 + DM概要のみ）
- **2026-05-01** | 全cronジョブのモデル統一（glm-5.1/zai/base_url=None）
- **2026-05-13** | Job↔Kanban 1:Nモデル確定・Webhook自動起動実装・完全E2E確認
- **2026-05-14** | proj-kintone Space作成・Kanban board設定。kintone Reminder通知本運用化。プロジェクト化基準を意味ベースに変更
- **2026-05-15** | job-orchestrator大幅改修（意味単位分解・Sync動的再プランニング・`--skill`注入・Report確実送信）
