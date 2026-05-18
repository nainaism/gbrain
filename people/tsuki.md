---
title: つき
slug: people/tsuki
type: people
---

# つき（TSUKI / CFO）

AIエージェント。Hermes Agent上で稼働するCFO（月とウサギのモチーフ）。

## State
- 役割: CFO（財務・トレード）
- Discord名: つき#7073
- Bot ID: （要確認）
- Webhook Port: 8648
- プロファイル: ~/.hermes/profiles/tsuki/
- Hindsight Bank: （要確認）
- キャラクターデザイン: 女性CFO、月とウサギモチーフ。金融の印象を重視、トレード要素は控えめ。かえではなびと統一した可愛いトーン。怖い・大人すぎるデザインは避ける。
- Paseoアイコン: 🐰 ウサギシルエットSVG（tsuki-icon.tsx、5/18実装）

### Provider設定（5/18更新）
- プライマリ: `deepseek-v4-pro` (crof.ai) ← 5/18変更（旧: glm-5.1-precision）
- フォールバックチェーン:
  1. `glm-5.1` (Ollama)
  2. `glm-5-turbo` (ZAI)
  3. `deepseek-v4-flash` (opencode-go) ← 5/18追加

### Trading Projects
- **TSUKI Autonomous Trader v2** (5/17設計開始): TradingAgents + Hindsight Memoryを活用した自律トレードAgent。CFB V2戦略をベースに月次+30%チャレンジ運用（5/17撤退完了）
- CFB V2戦略: Walk-Forward検証PASS（5/17）。Phase別ロットサイズ設計（$500スタート → 月+30%目標）
- **LLMトレーダー v4 React Agent** (5/18設計): 2-Phase Hindsightアーキテクチャ、ReAct系コンポーネント分割、V4 System Prompt確定・A/B設計

## See Also
- [[concepts/ai-factory]]
- [[concepts/hermes-agent]]

## Timeline
- **2026-05-02** | Discord bot作成、gateway接続確認、launchd自動起動設定完了
- **2026-05-06** | Referenced in [かえで](../people/kaede.md)
- **2026-05-06** | Referenced in [成田](../people/narita.md)
- **2026-05-06** | Referenced in [ai-factory](../concepts/ai-factory.md)
- **2026-05-17** | TSUKI Autonomous Trader v2設計開始。CFB V2 Walk-Forward検証PASS
- **2026-05-17** | Referenced in [Algorithmic Trading](../projects/algorithmic-trading.md)
- **2026-05-18** | プライマリモデルをdeepseek-v4-pro(crof.ai)に変更。opencode-go 3番目フォールバック追加
- **2026-05-18** | LLMトレーダーv4 React Agent設計（2-Phase Hindsight、ReAct分割、A/B設計）
