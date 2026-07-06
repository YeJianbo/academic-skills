---
name: section-drafter
description: "计算机科学论文逐节起草技能。用于根据 paper-architecture-planner 的蓝图，把密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文的某个章节或小节写成 Draft 0 / Draft 1；覆盖摘要、引言段落、问题定义、威胁模型、协议描述、算法说明、定理解释、证明路线、实验设置、结果分析和小节过渡；不做最终润色，后续交给 section-writing-polish 和 academic-paper-de-vibe。"
---

# Section Drafter

用于填补“论文规划”和“语言润色”之间的写作层。它把一节/小节的目标、证据和技术材料转成可继续打磨的论文初稿。默认服务计算机科学论文，不把 Nature/医学/经济学风格作为默认模板。

## 工作原则

1. 一次只写一个章节或小节，不一次性写完整篇论文。
2. 先把本节的 rhetorical job 写清楚，再写正文。
3. 不编造 citation、实验数值、定理、证明结论或 baseline。
4. 缺少材料时写 Draft 0，并用 `TODO:` 标出需要补充的证据。
5. 保留术语、符号、引用键、公式标签和 LaTeX 命令。

## 输入契约

优先要求或读取以下信息：

- Section name：要写的章节/小节标题。
- Section purpose：这一节要让读者理解或相信什么。
- Inputs：定义、协议步骤、算法、定理、证明思路、实验结果、图表或引用。
- Local context：上一节结论和下一节目标。
- Constraints：目标 venue、页数限制、写作语言、中英文、是否保留 LaTeX。

若用户只给粗略想法，先输出一个 mini section plan，再写 Draft 0。

若目标 venue 不明确，默认按 CS 顶会/安全会议写作：贡献明确、问题定义清楚、Related Work 独立、实验/证明可核验。只有用户明确说 Nature/Science/Cell 或跨学科期刊时，才参考 `references/nature-scipilot-writing-notes.md` 调整首段通俗化、篇幅压缩和 display-item 叙事。

## 起草流程

采用 Draft 0 -> 自检 -> Draft 1 的流程：

1. **Section Contract**: 用 3-5 行说明本节职责、读者应获得的信息、禁止展开的内容。
2. **Move Plan**: 规划段落功能，如 motivation move、definition move、construction move、proof-intuition move、evidence move、transition move。
3. **Draft 0**: 写出完整但保守的初稿。每段只承担一个 move。
4. **Self Check**: 检查断言强度、证据支撑、段落任务、术语一致、LaTeX/citation 保留。
5. **Draft 1**: 根据自检修正，形成可交给 `section-writing-polish` 的版本。
6. **Open Slots**: 列出缺失 citation、数值、定义、定理编号、图表引用或实验结果。

## 常见小节模板

### Title

如果用户要求标题，给 5 个候选：

1. 2 个 descriptive title：清楚描述问题、方法或系统。
2. 3 个 declarative title：直接表达关键发现或能力。
3. 标注每个标题更适合 conference、journal、system/security、theory 或 FL/privacy 场景。

避免 "A study of"、"Novel"、"First-ever"、未定义缩写和 5 个以上名词堆叠。

### Introduction Paragraph

段落顺序：

1. 场景或领域共识。
2. 具体安全/隐私/FL 痛点。
3. 现有方法无法覆盖的限制。
4. 本文 insight 或设计方向。
5. 与下一段衔接。

可用 CARS 作为骨架：establish territory -> establish niche -> occupy niche。CS 论文仍应保留清晰 contribution list，不强行写成 Nature 式 broad-audience prose。

### Problem Definition

必须写清：

- parties、inputs、outputs。
- adversary、capability、leakage、trust assumption。
- correctness/security/privacy/utility target。
- what is in scope and out of scope。

### Protocol or Construction

段落顺序：

1. Overview：协议要实现什么。
2. Setup：参与方、参数、密钥、公共信息。
3. Online/offline 或 round-by-round flow。
4. Why each step is needed。
5. Link to correctness/security proof。

### Theorem and Proof Intuition

正文不要只贴 theorem：

1. 先说明 theorem 解决哪个风险或保证。
2. 给出 theorem statement。
3. 用自然语言解释含义。
4. 给 proof roadmap：simulator、hybrids/games、bad event、advantage bound。
5. 标出完整证明是否放 appendix。

### Experiment Setup

必须交代：

- datasets、models、FL setting、non-IID split、client count、local epochs。
- baselines、attacks、privacy budget/security parameter。
- metrics：utility、privacy/security、efficiency。
- implementation and hardware。

### Result Analysis

不要只描述数字：

1. 先说表/图回答什么问题。
2. 给关键结果。
3. 解释为什么结果支持某个设计选择。
4. 说明限制、异常或 tradeoff。
5. 回扣 introduction 的痛点。

### Figure / Table Caption

若用户要求 caption：

1. 第一短句说明 figure/table 的结论，而不是只说展示了什么。
2. 后续说明数据、设置、指标和必要符号。
3. 对 multi-panel figure，逐 panel 解释 a/b/c/d 的角色。
4. 不在 caption 中引入正文没有定义的新结论。

## Draft 质量要求

- 每段第一句承担清晰任务。
- 每个强断言都匹配证明、复杂度分析、实验或攻击评估。
- 技术细节晚于读者所需的直觉和定义。
- 对密码学保证保持精确 hedging。
- 对 FL 实验同时讨论 utility、privacy/security、efficiency。
- 不使用宣传式词汇，如 elegant、seamless、comprehensive、crucial，除非有具体证据。
- 不把 bullet list 当正文，除非用户明确要列表。
- 如果是 LaTeX，保留 `\cite{}`、`\ref{}`、`\label{}`、公式和环境。

## 输出格式

默认输出：

```markdown
**Section Contract**
...

**Move Plan**
...

**Draft 0**
...

**Self Check**
...

**Draft 1**
...

**Open Slots**
...
```

若用户要求“只给正文”，只输出 `Draft 1`。

## 按需参考

- `references/nature-scipilot-writing-notes.md`: 当目标为 Nature/Science/Cell 或用户明确要求参考 Nature/SciPilot 写作流程时读取。

## 后续交接

起草完成后：

- 交给 `section-writing-polish` 做语言、压缩、翻译后编辑或 LaTeX polish。
- 交给 `academic-paper-de-vibe` 检查 AI 味、逻辑断裂、证明/实验与主张脱节。
