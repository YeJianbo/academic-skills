---
name: related-work-synthesizer
description: 依据已有文献池和阅读证据组织 Related Work 分类、定位与正文。缺少具体来源时补查相应证据，不默认重做完整检索。
---

# Related Work Synthesizer

用于把调研结果转成论文可用的 Related Work 结构。它不负责检索论文；检索和下载交给 `survey` 或 `tools/scansci-pdf`。

## 输入

- 文献列表、BibTeX、PDF 笔记、`.distilled.md` 证据卡或 survey summary。
- 本文核心问题、方法类别、目标会议。
- 需要强调的差异：threat model、系统假设、隐私定义、效率、泛化、可部署性。

## 输出

1. **Taxonomy**：按技术路线或问题维度分 2-4 类。
2. **Representative Works**：每类列代表性论文和它们解决的问题。
3. **Common Limitation**：每类末尾指出共同局限，直接服务本文动机。
4. **Positioning Sentence**：本文与该类工作的关系，是继承、改进、组合还是不同设定。
5. **Related Work Draft**：可直接放进论文的段落草稿。
6. **Citation Gaps**：缺少近 2-3 年顶会/顶刊或关键早期工作的地方。

## 规则

- 按技术路线分组，不按年份或逐篇排列。
- 每段先讲一类方法的共同思想，再列代表工作。
- 若输入包含 `.distilled.md`，优先复用其中的主张、限制和原文锚点，不必回原 PDF 重找一次，除非锚点不足以支撑当前表述。
- 不贬低前人，用“remain limited under ...”这类可验证边界表达。
- 本文差异必须和问题定义、威胁模型、实验或证明对应。
- 对关键论断标记需要引用的位置，不能编造引用。
- 若发现缺文献，回到 `survey/cs-idea-discovery-pipeline` 或 `tools/scansci-pdf`。

## 交接

- 需要写 Introduction 动机：交给 `section-drafter`。
- 需要润色成英文：交给 `section-writing-polish`。
- 需要检查夸大和 AI 味：交给 `academic-paper-de-vibe`。
