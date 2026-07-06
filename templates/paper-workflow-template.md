# 论文证据工作流模板

这套流程用于把“下载论文 -> 单篇蒸馏 -> 多篇综合 -> 落到写作”固定下来，减少重复读全文和反复找证据锚点。

## 目录约定

```text
work/
  papers/
    pdf/
    md/
    distilled/
    notes/
  syntheses/
  drafts/
outputs/
```

- `papers/pdf/`: 原始 PDF
- `papers/md/`: 手工整理或外部已有的 Markdown
- `papers/distilled/`: `paper-evidence-distiller` 产出的证据卡
- `papers/notes/`: 额外读书笔记或人工补记
- `syntheses/`: 多篇综合结果
- `drafts/`: related work、introduction、rebuttal 等草稿

## 推荐路由

1. 下载阶段
   - 用 `scansci-pdf` 或现有下载流程把论文放进 `work/papers/pdf/`
   - 如果已有高质量 Markdown，放进 `work/papers/md/`

2. 单篇蒸馏阶段
   - 对每篇 PDF/MD 跑 `paper-evidence-distiller`
   - 输出统一放进 `work/papers/distilled/`
   - 目标不是摘要，而是保留可回链证据

3. 多篇综合阶段
   - 要做逐篇结构化精读，用 `paper-reading-synthesizer`
   - 要写 related work、找技术脉络、归纳差异，用 `related-work-synthesizer`
   - 输入优先用 `distilled/` 下的证据卡，而不是原始 PDF

4. 写作阶段
   - 用 `scipilot-writing-skill` 把综合结果写成段落
   - 适合写：related work、motivation、results discussion、response to reviewers

## 固定提示词

### A. 下载后批量蒸馏

```text
Use $paper-evidence-distiller on every PDF in
C:\Users\YeJianbo\Documents\Codex\2026-06-15\github-com-haojae-scipilot-writing-skill\work\papers\pdf
and write outputs to
C:\Users\YeJianbo\Documents\Codex\2026-06-15\github-com-haojae-scipilot-writing-skill\work\papers\distilled .
For each paper, keep source anchors precise and do not infer anything not stated in the paper.
After each file, report the output path and any extraction limitation.
```

### B. 单篇试跑

```text
Use $paper-evidence-distiller on
<paper.pdf or paper.md>
and write the output to
C:\Users\YeJianbo\Documents\Codex\2026-06-15\github-com-haojae-scipilot-writing-skill\work\papers\distilled .
Read the paper end-to-end, keep the six required sections, and preserve all key numbers in 复核记录.
```

### C. 多篇证据综合

```text
Use $related-work-synthesizer on all distilled cards in
C:\Users\YeJianbo\Documents\Codex\2026-06-15\github-com-haojae-scipilot-writing-skill\work\papers\distilled .
Group papers by problem setting, method family, evidence strength, and failure mode.
Do not go back to the original PDFs unless a distilled card is missing a needed anchor.
Write the synthesis to
C:\Users\YeJianbo\Documents\Codex\2026-06-15\github-com-haojae-scipilot-writing-skill\work\syntheses\related-work-map.md .
```

### D. 从综合结果写 related work

```text
Use $scipilot-writing-skill to draft a Related Work section from
C:\Users\YeJianbo\Documents\Codex\2026-06-15\github-com-haojae-scipilot-writing-skill\work\syntheses\related-work-map.md .

载体：.tex
目标：顶会论文 related work
语言方向：英->英
领域：CS
保守度：中等

要求：
1. 只写基于综合结果里已经有证据支撑的内容。
2. 不编造引用，不补不存在的实验比较。
3. 先按主题分组，再写每组内部差异和局限。
4. 输出三段式，并运行写作自检。
```

### E. 从证据卡写 rebuttal 支撑段

```text
Use $scipilot-writing-skill to draft a response-to-reviewers paragraph based on
<one or more distilled cards>
plus the reviewer comment below.

载体：纯文本
目标：rebuttal / response to reviewers
语言方向：英->英
领域：CS
保守度：中等

要求：
1. 只使用证据卡中已有锚点支持的事实。
2. 明确区分作者已有证据、我们当前解释、仍未确认的问题。
3. 不夸大，不把相关写成因果。
```

## 什么时候值得先蒸馏再写

- 论文多于 5 篇，后面还要反复引用
- 需要准确回到表格、图、系数、样本设定
- 要写 rebuttal、related work、benchmark comparison
- 原始 PDF 很长，来回翻成本高

## 什么时候没必要蒸馏

- 只看 1 篇论文，且只是临时问答
- 你已经有人手写的高质量结构化笔记
- 当前任务只需要一句定义或一个公式，不需要整篇证据链

## 执行原则

- 单篇事实提取优先走 `paper-evidence-distiller`
- 跨论文归纳优先走 `paper-reading-synthesizer` 或 `related-work-synthesizer`
- 最终 prose 写作优先走 `scipilot-writing-skill`
- 发现蒸馏卡缺锚点时，再回原文局部补查，不要一上来重新读所有 PDF
