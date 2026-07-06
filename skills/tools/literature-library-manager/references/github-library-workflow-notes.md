# GitHub Library Workflow Notes

本地参考项目目录：`C:\Users\YeJianbo\.skills-manager\external-references\github-lit-review`。

## llm-for-zotero

迁移点：

- Zotero 内阅读、问答、比较论文、保存 notes。
- 支持本地 Markdown 文件夹，如 Obsidian/Logseq。
- 维护 cache-aware context 和 coverage state，适合长周期调研。

## zotero-better-notes

迁移点：

- note template、note link、Markdown 双向同步、导出。
- 知识片段之间建立链接，而不是只保存孤立摘要。

## Beaver Zotero

迁移点：

- 管理 collections、tags、metadata、notes。
- 外部搜索只在本地库信息不足时使用。
- 对自动修改 library 的操作要求用户确认。

## 本地化决策

- 不强依赖 Zotero 插件。
- 默认用 `papers.csv + library.bib + pdf/ + notes/`。
- Zotero 存在时，把 Zotero 当主库，本地 CSV 当调研状态表。
