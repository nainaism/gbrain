---
title: Luxerio
slug: luxerio
type: companies
---

# Luxerio

合同会社ルクセリオ。成田さんが参画する事業。

## State
- Notion Workspace: luxerio (HOME=~/.config/ncli-profiles/luxerio)
- Meeting Notes DB: 033870de-418b-4725-9085-f09a299e4d7f
- View URL: view://2ed7b51e-a59c-4e07-8f08-6c35f098063b
- 用途: Meeting Notesのみ（DB_documentsの重複を避けるため）

### OAuth
- ブラウザ認証が必要（自動認証不可）
- 認証エラー時は成田さんに手動再認証を依頼
- 2026-04-27: OAuth再認証完了（last-known-good stateから復旧）

### ambient-observer監視
- 73分ごとにMeeting Notesをスキャン
- 新規エントリ→Draft Job作成 + Hindsight retain + GBrain反映
- Space=luxerioとしてJobを作成

### City Heaven / ヘブンランキング対策
- シティヘブン（City Heaven）への掲載・ランキング対策を検討中
- 55グループ（GOGOグループ, 55group.tv）: すすきので複数店舗展開する待ち合わせ式デリヘル、ヘブン月額100万円以上投資
- IP制限（403）でブラウザからの直接アクセス不可（API/スクレイピングに工夫が必要）
- 競合分析PDFレポート作成プロジェクトあり（5/1 Failed: 55グループ店舗特定不完全）

### kintone業務
- App8/App37: ACL（アクセス権）再設計（月次管理アプリ含む）
- App53/App54/App49: 予算管理連携（monthly_budget_v2.js）
- 成田さんが直接kintoneスクリプト設計・ACL構造設計を担当

## See Also
- companies/nainaism
- concepts/ai-factory

## Timeline
- 2026-04-23: Client ID不一致エラー発生→修正
- 2026-04-27: OAuth再認証完了
- 2026-04-29: GBrainページ作成
- 2026-04-30: kintone ACL再設計（App8/App37）+ 予算未入力店舗洗い出し設計
- 2026-05-01: City Heaven競合分析（55グループ店舗特定不完全で中止）
