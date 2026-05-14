---
title: SI
slug: companies/si
type: companies
---

# SI

成田さんが参画するSI企業。kintone業務を担当。

## State
- kintone管理者権限あり

### kintone業務
- App8/App37: ACL（アクセス権）再設計（月次管理アプリ含む）
- App53/App54/App49: 予算管理連携（monthly_budget_v2.js）
- App61: 日次売上未入力リマインダー通知（FIELD_ENTITY: orgターゲット）
- App65: 月次予算未入力リマインダー通知（FIELD_ENTITY: orgターゲット）
- 成田さんが直接kintoneスクリプト設計・ACL構造設計を担当

### Reminder通知の仕組み（5/14本運用化開始）
- **日次売上(App61)**: target_date + 1日 12:00にReminder発火。未入力の場合、sync実行時にtarget_date < 今日のレコードを昨日に更新→翌日再通知
- **月次予算(App65)**: notify_date + 0日 12:00にReminder発火。未入力の場合、sync実行時にnotify_date < 今日のレコードを今日に更新
- **再スケジュール条件**: 通知日がすでに過ぎているのにまだ未入力のレコードのみ。未来の通知日は絶対に触らない
- **ACL**: App61はFIELD_ENTITY(org/brand/jigyoubu)権限。店舗担当者は自分のorgのレコードのみ閲覧・編集可
- **権限変更(5/14承認)**: everyone: 閲覧=✅ 編集=✅ 削除=❌ に変更し、全店舗のreschedulePastUnresolvedを可能にする計画あり
- **sync手動実行**: 現在CLI手動。Hermes cron自動化が未実装

## Timeline
- **2026-04-30** | kintone ACL再設計（App8/App37）+ 予算未入力店舗洗い出し設計
- **2026-05-01** | companies/luxerioから分離・独立ページ化
- **2026-05-06** | Referenced in [nainaism](../companies/nainaism.md)
- **2026-05-06** | Referenced in [Luxerio](../companies/luxerio.md)
- **2026-05-14** | Reminder通知本運用化（App61/App65）。再スケジュール条件修正（未来の通知日は触らない）。App61 ACL調査・権限変更計画
- **2026-05-14** | proj-kintoneボード作成（Kanban board + GitHub + Notion + Discord連携）

## See Also
- [[companies/luxerio]]
- [[companies/nainaism]]
