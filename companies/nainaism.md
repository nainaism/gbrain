---
title: nainaism
slug: companies/nainaism
type: companies
---

# nainaism

成田さんが代表を務める組織。ai-factoryの運営元。

## State
- 代表: 成田（Hiroki Narita）
- Notion Workspace: nainaism (HOME=~/.config/ncli-profiles/nainaism)
- セカンダリ: luxerio (Meeting Notesのみ)
- 主な活動: AIエージェントを活用した自律型チーム運営
- ブログ: nainaism.com (Astro + @astro-notion/loader)
- Blog Articles DB: 5413eece9b3d44b5a997dbadd91646c3

### ブログ記事パイプライン
- かえで(COO)がオーサリング・構成設計
- はなび(CMO)が執筆
- 成田さんがレビュー・公開承認
- Cover画像: blog-cover-genスキル（GPT-image-2）で生成、page cover + Coverプロパティの2箇所必須

### ブログデプロイ
- Notion API timeoutMs: 120秒（60秒→120秒、7ページ並列レンダリング対応）（4/24）
- patch-notion-loader.cjs: timeout時 throw error（サイレント失敗防止）（4/24）
- CI cache: `.astro/data-store/` のcache/restore+saveで未変更ページのAPI skip（4/24）
- Rate limit: ~3 req/sec、ページ数50超えたら並列度制限を検討（4/24）

## See Also
- people/narita
- concepts/ai-factory
- companies/luxerio

## Timeline
- 2026-04-12: Brainページ作成
- 2026-04-24: Notion API timeoutMs 120秒化、patch-notion-loader.cjs追加
- 2026-04-28: ブログ記事「AIで会社紹介スライド49枚を作った話」完成（レビュー3回、修正20箇所以上）
