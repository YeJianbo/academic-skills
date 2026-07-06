# GitHub Reading Workflow Notes

本地参考项目目录：`C:\Users\YeJianbo\.skills-manager\external-references\github-lit-review`。

## PaperQA2

迁移点：

- 把 PDF、metadata、citation data 和全文检索分开处理。
- 回答必须 grounded，引用到具体 source/page/excerpt。
- 对科学文献使用 query refinement、rerank、contextual summarization。
- 适合指导本 skill 的证据定位和 claim-evidence 结构。

## Beaver Zotero

迁移点：

- 研究回答要有 sentence-level 或 passage-level citation。
- 当前 PDF、整库文献和外部文献应分层使用。
- 对阅读中的论文标注“与我的项目关系”，而不只做摘要。

## LLM Literature Review Assistant

迁移点：

- 初筛输出 CSV：paper metadata + decision + thoughts + note。
- 支持 resume，避免重复处理。
- 每篇论文必须有 inclusion/exclusion reason。

## llm-for-zotero / zotero-better-notes

迁移点：

- notes 应能保存到 Zotero 或本地 Markdown。
- 读书笔记和 PDF annotation 要能互相跳转。
- 维护已读状态、缓存、coverage state，支持长周期调研。
