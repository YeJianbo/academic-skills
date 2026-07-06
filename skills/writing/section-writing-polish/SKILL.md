---
name: section-writing-polish
description: "计算机科学论文小节改写与语言润色技能。用于在 section-drafter 起草之后，对密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文段落进行改写、翻译后编辑、Chinglish 修正、学术语气调整、精简表达、LaTeX 段落 polish 和术语一致性检查；默认不重新规划论文主线，质量审查交给 academic-paper-de-vibe。"
---

# Section Writing Polish

用于把已有小节草稿改成更清楚、更自然、更符合学术语气的版本。默认面向密码学、联邦学习、隐私计算、安全与 CS 论文。

## 工作边界

- 根据已有论文蓝图和小节草稿做改写，不重新定义整篇论文主线。
- 保留技术主张、实验结论、安全模型、引用关系和符号含义。
- 如果发现规划缺口，先标出缺口，再给可写版本。
- 不伪造 citation、实验数值、定理结论或证明细节。

## 写作模式

1. `rewrite`: 重写已有草稿，保留含义但改善逻辑和表达。
2. `translation`: 中英学术翻译、译后编辑、Chinglish 修正。
3. `tone`: 调整学术语气、正式程度和 hedging。
4. `concise`: 删除冗余、压缩字数、减少重复。
5. `latex-polish`: 保留 LaTeX 命令、公式、citation key、label，只润色自然语言。
6. `similarity`: 查重前改写，保留技术含义，避免机械同义词替换。

若用户给的是提纲或只有技术要点，应转给 `section-drafter` 先起草。若给的是已有段落，用 `rewrite + tone + concise`。

## 润色流程

每次只处理一个章节或小节：

1. 确认小节任务和原文主张。
2. 修复句间逻辑和段落顺序，但不新增未经证实的技术点。
3. 调整语气、hedging、术语一致性和 LaTeX 附近表达。
4. 删除冗余、模板化连接词和空泛评价。
5. 输出可替换原文的 polished version；必要时列出缺失 citation、数值、定义或图表。

## 密码学/FL/隐私计算写作要求

- 写 threat model 时必须说明 adversary、capability、leakage、trust assumption。
- 写 protocol 时必须说明 parties、messages、rounds、inputs、outputs。
- 写 theorem 前必须已有 definition；写 theorem 后要有 plain-language explanation。
- 写 FL 实验时必须同时交代 utility、privacy/security、efficiency。
- 写 DP 时不要只写 epsilon，说明 clipping、noise、composition 或 accounting。
- 写 MPC/HE/TEE 时说明 trust、setup、communication、computation 和 leakage。

## 语言规则

- 优先具体动词：prove, bound, aggregate, encrypt, perturb, verify, infer, reconstruct。
- 删除空泛评价词，除非有证明或指标支撑。
- 保留必要限定，不把经验结果写成形式化保证。
- 不为了变化而替换术语，同一概念保持一致。
- 避免模板化连接词和连续 bullet；把递进关系写成段落。

## 输出方式

- 用户要求“写这一节”且只有提纲：转 `section-drafter`。
- 用户要求“润色这一节”：输出可直接替换原文的 polished version。
- 用户要求“润色”：只给润色后文本，除非用户要求解释。
- 用户要求“对照修改”：给 Before/After 或简表。
- 处理 LaTeX 时不要改动命令、环境、引用键、公式标签和文件路径。
