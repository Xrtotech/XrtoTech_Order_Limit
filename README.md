# 订单限制

基于 Mintlify 的中、日、英三语 Shopify 商家手册（中文默认），采用品牌紫色和固定浅色主题。

## 内容结构

- `index.mdx`：中文应用介绍首页，保留现有根路径。
- `ja/`：完整日文文档。
- `en/`：完整英文文档。
- `about/`：服务与支持、功能优势与插件选型。
- `quickstart.mdx`：第一条限购规则。
- `scenarios/`：10 个经营场景及场景索引。
- `features/`：数量、价格、重量、客户与历史购买说明。
- `settings/`：规则组合和顾客提示。
- `troubleshooting/`：排查步骤与测试清单。
- `.mintlify/product-brief.md`：内容定位与核对依据。

## 本地预览

```bash
npm install -g mint
mint dev --no-open
```

## 内容校验

```bash
mint validate
mint broken-links
```

文档能力依据相邻 `xiangou` 应用源码核对。示例数值不代表产品默认值。修改功能后同步更新场景测试与边界说明。品牌图片保留在 `images/order-limit-brand.png`，紫色为 `#A07EC8`。

文档语言已确认为中文、日文、英文，中文为主。修改中文内容时，同步对应的日文、英文页面并保持站内链接语言一致。发布前需用真实店铺复核操作界面。此仓库的本地编辑不代表已发布上线。
