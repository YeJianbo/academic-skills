# GitHub Literature Search Notes

用于补强计算机科学文献检索 workflow。只保留可迁移机制，不复制外部项目。

## 值得借鉴的项目类型

- `paper-qa` / `paper-qa2` 类：把论文检索、PDF 获取、向量索引和问答分开，避免把“找到论文”和“理解论文”混成一步。
- `gpt-researcher` / research-agent 类：先生成多组 query，再并行检索、筛选、汇总出处。
- OpenAlex / Semantic Scholar / arXiv 聚合脚本：无 key 或低门槛接口适合默认检索。
- Zotero / Better BibTeX workflow：把最终文献库交给 Zotero 管理，BibTeX 作为论文项目输入。
- Citation graph 工具：从 seed paper 做 backward/forward chaining，比单轮关键词搜索更适合发现结构性空白。

## 本地迁移

- 检索层：OpenAlex、arXiv、Crossref、Semantic Scholar、网页搜索。
- 下载层：`scansci-pdf`，必要时启用 WebVPN。
- 阅读层：PDF 解析、笔记、结构化摘要，交给 survey/review/writing。
- 写作层：`related-work-synthesizer`，不让检索 skill 直接写完整 Related Work。

## API key 策略

- 默认不要求 key。
- OpenAlex 只建议配置 `mailto`，不是 API key。
- Semantic Scholar API key 可提升限速，但不作为必需条件。
- IEEE Xplore、Lens、Scopus、Web of Science 作为增强源，缺 key 时不阻塞主流程。
- 学校账号用于机构下载，不用于元数据 API 鉴权。
