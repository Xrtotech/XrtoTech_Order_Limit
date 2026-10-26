# 可选问答助手方案

默认状态：不展示 Mintlify AI 入口，不集成第三方助手，不发起模型调用。保留普通搜索。
站点 CSS 仅控制页面显示；Mintlify 账户内的助手开关、Pro 试用与订阅需要在后台单独管理。

## 推荐：轻量检索 + DeepSeek

- 保留目前的 Mintlify 文档站，不迁移文档。
- 构建时从导航中的 MDX 提取正文、标题、语言和页面 URL，按小节生成检索索引。排除 `.mintlify/` 等内部文件。
- 浏览器将问题与当前语言提交到自己的后端。后端先检索少量相关小节，再调用 DeepSeek。
- 系统提示要求仅依据文档回答、使用用户语言、给出原文链接；找不到依据时明确告知。
- API key 仅存储在服务端环境变量。设置问题长度、上下文、回答长度、调用频率和每日请求限额。
- 不必为当前文档规模先采购向量数据库。可从支持中日韩分词的全文检索开始，评估召回效果后再决定是否添加向量检索。
- 未配置服务端 API key 和接口地址时，聊天入口保持关闭。
- 现阶段未安装依赖、注册服务或调用付费 API。

## 可用平台

- Dify Cloud Sandbox：免费试用核心功能；当前定价页列出 200 message credits、50 份知识文档、50 MB 知识存储和 10 次知识请求/分钟。200 credits 并未标为每月续赠。现有三语手册共 69 页，可先导入中文 23 页试用。
- Dify Community Edition：自行部署软件，无 Dify Cloud 订阅月费；另计运行设备、模型和可能的嵌入模型费用。按其许可证使用。
- AnythingLLM：可自行部署，具有文档问答和网页嵌入能力；另计运行设备与模型费用。部署前确认选定版本支持的模型提供商和嵌入配置。

## 价格示例

2026-10-26 查询 DeepSeek 官方定价：deepseek-flash 的高峰未缓存输入为 $0.30/百万 tokens、输出为 $1.20/百万 tokens。
若每轮实际计费总输入 4,000 tokens、总输出 600 tokens，1,000 轮约 $1.92；仅为模型示例估算，不含托管、检索/嵌入及额外推理 tokens。多轮历史、长上下文、重试会增加费用。

## 官方资料

- https://www.mintlify.com/docs/assistant/configure
- https://api-docs.deepseek.com/quick_start/pricing
- https://dify.ai/pricing
- https://github.com/langgenius/dify
- https://github.com/Mintplex-Labs/anything-llm
