# Documentation review, 2026-10-26

## Scope and outcome

The help center now has 27 merchant pages per language, 81 total, with 11 scenarios per language. Chinese remains at the original root URLs; English uses `en/`, Japanese uses `ja/`. No existing public page was moved. The floating WeChat contact changes from the preceding task are preserved.

The local Mintlify checkout was edited because this session exposes no callable Mintlify Admin or Search MCP tools. Mintlify product behavior was checked against the official custom-scripts, SEO, settings-seo, writing and product-context references. No publish, commit or push was performed.

## Changes grounded in source

| Documentation fact | Source evidence under adjacent `xiangou/` |
| --- | --- |
| Home entries and four rule categories | `app/routes/app._index.jsx` |
| New quantity rule action is 创建并启用; edits use 保存并启用 | `app/routes/app.quantity-limits.rules.new.jsx` |
| New customer rule uses 创建并启用; tags optional for sign-in-only | `app/routes/app.customer-limits.rules.new.jsx` |
| Quantity list action is 创建规则; dedicated list order matters | `app/routes/app.quantity-limits.rules._index.jsx` |
| Product/variant rows use 限制状态, 最小值, 最大值 and 保存 | `app/routes/app.quantity-limits.products.jsx` |
| Feature switches and separate quantity validation | `app/routes/app.quantity-limits._index.jsx` |
| Current amount, store currency, scopes and price editor labels | `app/routes/app.price-limits.rules.new.jsx`, `app/price-limits.server.js`, `extensions/price-limit-validation/src/cart_validations_generate_run.js` |
| Weight units, variant data and thresholds | `app/routes/app.weight-limits.rules.new.jsx`, `extensions/weight-limit-validation/src/cart_validations_generate_run.js` |
| Individual product aggregation, relaxed merges, variant checks, first purchase and recorded totals | `extensions/quantity-limit-validation/src/cart_validations_generate_run.js` |
| Additional order records are not tied to rule activation time or payment completion | `app/routes/webhooks.orders_create.jsx`, `app/quantity-history.server.js` |
| Customer template tokens itemName and productTitle | `app/routes/app.customer-limits._index.jsx` |

The app editor contains lifetime helper text claiming only orders after activation and completed orders count. Actual recording code does not gate on rule activation or paid state. Merchant docs preserve the verified behavior: recorded new orders can predate rule activation; recording is based on order creation; there is no refund/cancellation rollback or periodic reset. This is a source/UI inconsistency, not a documentation promise to replicate.

## New beginner paths

- `getting-started/choose-rule`: choose from actual business goals and understand four rule families.
- `getting-started/product-variant-limits`: product maximum 3, blue variant maximum 1, with four test carts.
- `getting-started/launch-checklist`: allowed/boundary/blocked/scope/identity tests, pause/restore and reproducible evidence.
- `scenarios/login-required`: leave tags empty, require sign-in, select one product and test identities.

All four have full English and Japanese versions. Existing scenarios retain original numeric examples and boundaries, with prerequisites, exact create/save actions, explicit enablement and troubleshooting added. FAQs now include activation, pausing, sign-in without tags, scoped minimums and message languages.

## SEO work and verification boundaries

- Unique titles and descriptions for all 81 pages; specific topic keywords rather than repeating the title as a keyword.
- Concise localized descriptions, avoiding padding CJK text to an English character count.
- One page H1, H2/H3 body structure, localized related links and task-based navigation.
- `seo.indexing` is `navigable`; internal notes and editorial scripts are explicitly excluded via `.mintignore`.
- Localized `og:site_name` and `og:locale` path metadata; retain Mintlify automatic social cards instead of inventing screenshots or social profiles.
- Retain native canonical, sitemap and structured-data generation. No hard-coded domain, fake author, verification token, or invented published dates.
- Local preview confirms page title/description and rendered Mermaid diagrams. Production canonical, sitemap, hreflang, robots, social cards, Search Console and indexing must be checked after deployment on the real public domain. Local dev does not provide those production metadata signals; do not claim they were verified.
- Search traffic or ranking improvement has not been measured or promised.

## Media and execution deliverables

- `screenshot-plan.md`: Article-by-article capture instructions for 16 foundation/navigation pages and 11 scenario recipes, with individual filenames, priorities, settings, placement and localized front-end filenames.
- `screenshot-manifest.json`: machine-readable assets and reuse map.
- `social-content-plan.md`: 11 scenario video storyboards, draft narration, five-page post copy, captions and localized landing paths, plus six introductory/FAQ topics.
- Six rendered Mermaid diagrams across two conceptual guides in three languages.
- Captures are pending from the user. Only invisible editorial comments are present; no broken image URLs or fabricated app screenshots.
- Code/source review and editorial walkthrough are complete. This is not a claim that a novice has completed an observed usability test on a live store.

## Checks

- `python3 .mintlify/audit-content.py`: required metadata, unique metadata, H1 structure, navigation coverage, local page targets, language parity, localized links, scenario table numeric sets and supported template-token parity. Japanese “1 点 2 kg” is normalized as a per-unit phrase for numeric comparison.
- `mint validate`: Mintlify build validation.
- `mint broken-links`: native link validation.
- `git diff --check`: whitespace and patch integrity.

Final machine-readable content results are stored in `content-audit.json`. Screenshots of the documentation preview are under `.mintlify/screenshots/`. These are review evidence for the help-center layout, not substitutes for the user-supplied app screenshots.
