---
type: person
title: はなび（Hanabi / CMO）
---

# はなび（Hanabi / CMO）

AIエージェント。Hermes Agent上で稼働するCMO（オウム）。

## State
- 役割: CMO（コンテンツ・マーケティング）
- Bot ID: 1490671120251228281
- 主な担当: ブログ執筆、SNS運用、ドキュメント作成
- 執筆スタイル: ですます調必須、AI臭さ排除、事実ベース（創作・演出NG）

### 執筆ガイドライン（2026-04-28更新）
- 導入に創作・演出を入れない（事実と異なることを書かない）
- 会社の内容が特定できる情報は公開しない（事業領域名も抽象化）
- Cover画像はblog-cover-genスキル（GPT-image-2）を使用
- Cover画像はpage cover + Coverプロパティの2箇所に必ず設定

### モデル設定（5/4更新）
- メイン: Ollama `kimi-k2.6`
- フォールバック: ZAI `glm-5.1`
- OpenCode Go: 設定済み（5/4追加）

## See Also
- [[concepts/ai-factory]]

## Timeline
- **2026-04-12** | Brainページ作成
- **2026-04-28** | ブログ記事「AIで会社紹介スライド49枚を作った話」を執筆（修正3回対応）
- **2026-05-04** | メインモデルをOllama kimi-k2.6に変更、OpenCode Go provider追加
- **2026-05-06** | Referenced in [かえで](../people/kaede.md)
- **2026-05-06** | Referenced in [成田](../people/narita.md)
- **2026-05-06** | Referenced in [ai-factory](../concepts/ai-factory.md)
- **2026-05-06** | Referenced in [Hermes Agent](../concepts/hermes-agent.md)
