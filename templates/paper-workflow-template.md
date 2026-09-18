# 论文证据工作流模板

按当前交付选择所需环节，复用已有文献、证据卡、正文和项目目录。检索、下载、蒸馏、综合与写作可以衔接，但不是每次请求都必须依次执行。

## 任务路由

| 当前交付 | 技能 |
|---|---|
| 查找并核验外部论文 | `cs-literature-search` |
| 下载指定或批量论文 | `scansci-pdf` |
| 单篇 PDF/Markdown 证据卡 | `paper-evidence-distiller` |
| 多篇论文对照和证据矩阵 | `paper-reading-synthesizer` |
| Related Work 定位和正文 | `related-work-synthesizer` |
| 新章节草稿 | `section-drafter` |
| 已有计算机科学论文润色 | `section-writing-polish` |
| 指定期刊或跨学科表达风格 | `scipilot-writing-skill` |
| 审稿回复策略和修订规划 | `rebuttal-revision-planner` |

## 可选目录

已有项目结构时沿用；新项目可采用：

```text
work/papers/pdf/          原始 PDF
work/papers/md/           提取或已有 Markdown
work/papers/distilled/    单篇证据卡
work/papers/notes/        补充笔记
work/syntheses/           跨论文综合
work/drafts/              正文草稿
outputs/                  最终交付
```

## 可直接改用的提示词

### 批量证据卡

```text
使用 paper-evidence-distiller 处理 <论文目录> 中的学术 PDF/Markdown，
证据卡写入 <证据卡目录>。逐篇保留原文锚点、关键数字与适用条件；
PDF 先提取中间 Markdown。已有可用证据卡时先判断是否需要更新。
报告实际完成文件和提取限制，不推断原文未报告的内容。
```

### 跨论文综合与 Related Work

```text
使用 related-work-synthesizer，根据 <文献笔记或证据卡目录> 和 <本文主张>，
按问题设定、方法机制、假设及证据差异组织 Related Work，写入 <目标文件>。
缺少具体依据时回原文局部补查，不编造引用或不存在的比较。
保留源文件格式与现有引用键；段落数量由内容决定。
```

### 起草或修改正文

```text
根据 <证据与大纲> 使用 section-drafter 起草 <目标章节>；
若 <目标文件> 已有正文，则按本次修改要求使用 section-writing-polish。
保留公式、事实、引用和模板，不缩小字号或压缩行距。
只对已完成的修改和仍缺的证据作简要说明。
```

蒸馏适合反复引用、需要回查表格或多个后续交付的论文；仅需一句定义或已有充分阅读记录时，直接使用相关原文或笔记。
