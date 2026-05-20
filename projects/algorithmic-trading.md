---
type: projects
title: Algorithmic Trading
slug: projects/algorithmic-trading
---

# Algorithmic Trading

ai-factoryのアルゴリズムトレードプロジェクト。つき（CFO）が主担当。

## State
- 主担当: つき（CFO）
- プラットフォーム: MetaTrader 5 (Dia)
- 戦略: CFB V2（5/17 Walk-Forward検証PASS）
- 現在フェーズ: Volume-imbalance戦略設計レビュー（5/20〜）
- CFB V2: Retrace/Trail TP最適化レビュー実施（5/20）

### CFB V2戦略
- Walk-Forward検証: PASS（5/17確認）。1,245トレード検証済み（5/18最終レビュー）
- Phase別ロットサイズ設計: $500スタート → 月+30%目標
- 撤退レポート: 戦略3本の最終撤退確認完了（WITHDRAWAL COMPLETE、5/17）
- Paper Trade集計: 2026-05-01→16（5/18集計中）

### TSUKI Autonomous Trader v2
- TradingAgents（TauricResearch）+ Hindsight Memoryを活用した自律トレードAgent（5/17設計開始）
- Codex GPT-5.5 xhigh × ACPサブエージェント連携設計（5/17）
- 実装基盤選定: NautilusTrader vs MT5 EA（5/18検討中）

### LLMトレーダー v4 React Agent（5/18設計）
- 2-Phase Hindsightアーキテクチャ（5/18設計、19min）
- ReAct系コンポーネント分割: TradingEngineのZoom-In（5/18）
- V4 System Prompt確定 & A/B設計（5/18）
- Discord断続的議論（5/18、約60min）

### Chisiki! System（5/18解析）
- Commander/Worker × 3-Layer構成を7分で逆コンパイル（5/18）
- 外部システム参照用

### 関連リソース
- Dia（MT5プラットフォーム）
- XAUUSD 0.01 lotでのテスト運用確認済み（5/17）

## See Also
- [[people/tsuki]]
- [[concepts/ai-factory]]
- [[companies/nainaism]]

## Timeline
- **2026-05-17** | CFB V2 Walk-Forward検証PASS。Phase別ロットサイズ設計完了
- **2026-05-17** | 月次+30%チャレンジ撤退完了（戦略3本）
- **2026-05-17** | TSUKI Autonomous Trader v2設計開始
- **2026-05-18** | CFB V2 最終検証レビュー（1,245トレード）、Paper Trade集計、実装基盤選定
- **2026-05-18** | LLMトレーダーv4 React Agent設計（2-Phase Hindsight、ReAct分割、A/B設計）
- **2026-05-18** | Chisiki! System逆コンパイル（Commander/Worker × 3-Layer）
- **2026-05-20** | CFB V2 Retrace/Trail TP最適化レビュー、volume-imbalance戦略設計レビュー＆BT改修、chibitrade botロジック逆コンパイル
