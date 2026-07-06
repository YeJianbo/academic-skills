---
name: latex-paper-integrator
description: "计算机科学论文 LaTeX/Typst 集成技能。用于把分节草稿、算法伪代码、定理证明、实验表格、BibTeX、figures、captions 和 supplementary/artifact 内容整合进 CS 论文项目；检查编译、cross-reference、citation、匿名化、页数、图表路径、算法环境、theorem environment 和 conference template 兼容性。"
---

# LaTeX Paper Integrator

用于把写作、实验和图表产物落进论文项目。它关注项目集成和编译一致性，不负责重新设计论文主线。

## 输入

- LaTeX 或 Typst 项目目录。
- 分节草稿、图表、表格、算法、证明、BibTeX。
- 目标模板：ACM、IEEE、USENIX、NDSS、CCS、NeurIPS、ICML、ICLR、CVPR 或其他 CS venue。

## 工作流

1. **Project Scan**：识别主文件、章节文件、bibliography、figures、tables、style files。
2. **Insertion Plan**：决定新内容放入哪个 `.tex`、`.typ`、`.bib` 或 figure/table 目录。
3. **Reference Hygiene**：检查 `\label`、`\ref`、`\cite`、`\autoref`、算法编号、定理编号。
4. **Compile Check**：运行可用的编译命令，记录错误和 warning。
5. **Template Constraints**：检查匿名化、页数、字体、图表位置、supplementary 和 artifact 要求。
6. **Consistency Check**：确认正文 claim、表格数字、figure caption、实验结果文件一致。

## 输出

- 修改计划或已修改文件列表。
- 编译命令和结果。
- unresolved citations/references。
- page/template/anonymization 风险。
- 下一步需要写作、实验或审稿补充的内容。

## 规则

- 不凭空改实验数字。
- 不把审稿回复口吻写进正文。
- 不删除用户已有手写内容，除非用户明确要求。
- 引用缺失时标记 `TODO:CITE` 或返回 citation gap，不编造 BibTeX。
- 需要正式投稿前审查时，交给 `submission-readiness-checker`。
