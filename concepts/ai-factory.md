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

### 運用ルール
- プロジェクト管理はai-factory NotionがSSOT
- スキル変更は事前に成田さん確認必須
- git管理下のファイル変更は即座にcommit
- 長文のDiscord投稿はNotionページにしてリンク送信
- タスク完了時: Progressセクションに`成果:` + `詳細:` を必ず記載（5/1成田さん指示）
- プロジェクト完了時: 全タスクのProgressから成果を集約してプロジェクトbodyにレポート
- Discord DM報告: 概要2-3行 + Notionリンクのみ（スレッドリンク不要、5/1成田さん指示）

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

### スキル運用
- nainaism-blog-article: ブログ執筆ワークフロー（かえでオーサリング→はなび執筆→かえでQA→成田さんレビュー）
- blog-cover-gen: Cover画像生成（GPT-image-2）。グローバル化済み。
- space-provisioning: 新規Space追加ワークフロー（3箇所設定: ローカル/GitHub, Discord, Notion）

## See Also
- people/narita
- people/kaede
- concepts/hermes-agent
- companies/nainaism

## Timeline
- 2026-04-12: Brainページ作成
- 2026-04-22: パグオカHermes移行完了
- 2026-04-26: Factory Radar初回セットアップ、space-provisioningスキル作成
- 2026-04-28: nainaism-blog-articleスキル大幅更新
- 2026-04-29: GBrain入力パイプライン統合完了（セッション+Chronicle+議事録）
- 2026-05-01: タスク/プロジェクト完了時の報告フォーマット変更（成果詳細 + Notion集約 + DM概要のみ）
- 2026-05-01: 全cronジョブのモデル統一（glm-5.1/zai/base_url=None）
