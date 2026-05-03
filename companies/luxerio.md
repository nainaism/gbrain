---
title: Luxerio
slug: companies/luxerio
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

### スタイルグループ HP / microCMS
- スタイルグループのWebサイト制作プロジェクト（5/2開始）
- microCMSでスキーマ定義書作成済み
- ロードマップ整理中
- Google Drive素材（Lstyle/Rstyle）確認済み
- **Next.js版公式HPデザイン仕様把握・再構築進行中**（5/3 Activity Chronicle）
- **VALTEN**: リサーチ対象ブランド（5/3確認）
- **Paseo連携**: 「Notionページからデザイン再構築」追加検討（5/3）

### Builto×Luxerio POS連携
- Builto（外部企業）とLuxerio POSの連携MTG継続中
- Luxerio POS Prototype確認済み（5/2）

### kintone業務
→ companies/si に移動済み（2026-05-01）

## See Also
- companies/nainaism
- concepts/ai-factory

## Timeline
- 2026-04-23: Client ID不一致エラー発生→修正
- 2026-04-27: OAuth再認証完了
- 2026-04-29: GBrainページ作成
- 2026-04-30: kintone ACL再設計（App8/App37）+ 予算未入力店舗洗い出し設計
- 2026-05-01: City Heaven競合分析（55グループ店舗特定不完全で中止）
- 2026-05-02: Builto×Luxerio POS MTG + Prototype確認、スタイルグループHP/microCMS設計開始
- 2026-05-03: Lounge R Style HP再構築開始（Next.js版）、VALTENリサーチ
