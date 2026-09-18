---
name: tools
description: "学术文件与工具任务分流：编译排版、文献库和全文访问等目标不清时使用。明确的工具任务直接进入专用技能。"
---

# Academic Tools

只解决当前产物需要的工具问题，不为普通学术任务加载整套工具目录。

| 交付 | 负责技能 |
|---|---|
| LaTeX/Typst 集成、编译、引用/标签与模板检查 | `latex-paper-integrator` |
| PDF 页面提取、版面或导出检查 | `pdf` |
| 文献库去重、BibTeX、阅读状态和文件整理 | `literature-library-manager` |
| 指定论文下载、引文导出或批量全文 | `scansci-pdf` |
| 实际需要机构订阅的授权与访问恢复 | `institutional-access-resolver` |
| 数值绘图、图型判断、可编辑示意图 | 分别直达 `nature-figure`、`scipilot-figure-skill`、`drawio-diagram-builder` |

引用是否支持主张属于相应证据审查，找新论文属于检索；不要把二者混成格式检查。已有有效工具与登录态直接复用。其他工具文档按具体需要读取，不重新启用泛化上下文预算入口。
