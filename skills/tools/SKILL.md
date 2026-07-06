---
name: tools
description: "工具入口：LaTeX/Typst 论文集成、引用、统计、数据、检索、文献库管理、图表、上下文预算管理与工作流支持。"
---

# Tools

用于学术工作的共享工具层。

## 覆盖内容

- `latex` / `typst`：论文排版、模板、公式、编译、cross-reference、匿名化检查；论文项目集成使用 `latex-paper-integrator`
- `citation`：引用管理、Bib 检查、参考文献核验
- `statistics`：统计建模、假设检验、功效分析
- `data`：清洗、转换、分析、结果汇总
- `diagram` / `dataviz`：流程图、学术插图、论文图表
- `research` / `search`：数据库检索、引文追踪、文献发现；CS 文献检索优先走 `survey/cs-literature-search`
- `institutional-access`：调研前学校账号/WebVPN/SeamlessAccess 授权与全文验证，使用 `institutional-access-resolver`
- `paper-download`：全文下载、BibTeX、学校 WebVPN 机构访问，已有 DOI/arXiv/title 列表时直接走 `scansci-pdf`，不强行 OpenAlex 检索
- `literature-library`：PDF、BibTeX、Zotero、Markdown notes、papers.csv 和阅读状态管理，使用 `literature-library-manager`
- `context-budget`：长任务、批量调研、多子代理、代码库探索和跨轮交接的 token/context 节约，使用 `context-budget-manager`
- `workflow` / `code-exec`：执行环境、自动化、复现流程

## 使用规则

- 这里只放工具类入口
- 具体学术任务优先从 `academic-hub` 或四个流程分类进入
