---
title: パグオカ
slug: people/pugoka
type: people
---

# パグオカ（Pug-Oka）

AIエージェント。Hermes Agent上で稼働する別bot。OpenClawからHermesへ移行済み。

## State
- 役割: Luxerio業務サポート
- Bot ID: 1470383283387891742
- Discord: パグオカ 🐶#7392
- Hindsight Bank: pugoka
- プロファイル: ~/.hermes/profiles/pugoka/
- Webhookポート: 8647（CTO/CMOとの競合回避）

### Cron Jobs
- meeting-notes-sync: Luxerio議事録同期
- activity-memory-sync: 活動ログ→Hindsight同期
- daily-briefing: 日次ブリーフィング
- 認証エラー時は `[SILENT]` で静かに終了

### 移行経緯
- **2026-04-22** | Hermes pugokaプロファイル作成、launchd登録完了
- **2026-04-22** | OpenClaw停止、launchdエントリ削除・アンロード
- 既存Bot Tokenを流用、18チャンネル構築済み

## See Also
- [[companies/luxerio]]
- [[concepts/hermes-agent]]

## Timeline
- **2026-04-22** | Hermes移行完了、安定稼働確認（PID 52335, 18分以上）
- **2026-04-29** | GBrainページ作成
- **2026-05-06** | Referenced in [かえで](../people/kaede.md)
- **2026-05-06** | Referenced in [成田](../people/narita.md)
- **2026-05-06** | Referenced in [ai-factory](../concepts/ai-factory.md)
- **2026-05-06** | Referenced in [Luxerio](../companies/luxerio.md)
