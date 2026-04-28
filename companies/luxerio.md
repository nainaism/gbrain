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

## See Also
- companies/nainaism
- concepts/ai-factory

## Timeline
- 2026-04-23: Client ID不一致エラー発生→修正
- 2026-04-27: OAuth再認証完了
- 2026-04-29: GBrainページ作成
