---
name: writing
description: "计算机科学论文写作总入口：面向密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文的规划、逐节起草、相关工作综合、安全/隐私证明起草、语言润色和去 AI 味检查；路由到 paper-architecture-planner、section-drafter、related-work-synthesizer、security-proof-builder、section-writing-polish、academic-paper-de-vibe，并按需协作本地 scipilot-writing-skill、nature-figure、scipilot-figure-skill、review 等技能。"
---

# Writing

用于计算机科学论文与学术文本写作。默认流程是先规划，再按章节/小节起草，再润色，最后检查。

## 主工作流

1. `paper-architecture-planner`: 确定论文架构、写作方向、章节职责和证据映射。
2. `section-drafter`: 根据蓝图逐章、逐节、逐小节写 Draft 0 / Draft 1。
3. `related-work-synthesizer`: 把文献池组织成 Related Work 分类、共同局限和本文定位。
4. `security-proof-builder`: 起草 threat model、定义、定理和 proof sketch。
5. `section-writing-polish`: 对已有草稿做语言润色、翻译后编辑、精简和 LaTeX polish。
6. `academic-paper-de-vibe`: 检查 AI 味、逻辑断裂、符号问题、证明/实验脱节和夸大表述。

本地其他技能只作为协作者，不替代上述主流程。需要跨技能时先查 `references/local-skill-integration.md`。

## 路由表

| 用户需求 | 使用技能 | 输出 |
|---|---|---|
| 还没确定论文怎么写、章节怎么排、主线怎么讲 | `paper-architecture-planner` | Paper thesis、narrative spine、section blueprint、evidence map、writing queue。 |
| 已有规划/要点，要写某个章节或小节 | `section-drafter` | Section contract、move plan、draft、open slots。 |
| 有文献池，需要写 Related Work 或定位本文差异 | `related-work-synthesizer` | taxonomy、representative works、common limitations、Related Work draft。 |
| 有 PDF/笔记但还没形成证据矩阵 | `survey/paper-reading-synthesizer` | paper notes、claim-evidence matrix、gap signals。 |
| 需要写 threat model、security/privacy definition、定理和证明草稿 | `security-proof-builder` | definitions、theorems、proof sketch、limitations。 |
| 已有草稿，要润色、翻译、精简、改 Chinglish | `section-writing-polish` | 保留技术含义的 polished version。 |
| 要去 AI 味、深度检查、确认像不像顶会论文 | `academic-paper-de-vibe` | 逻辑/符号/证明/实验/语言问题诊断和修复建议。 |
| 要 Nature/Science/Cell/PNAS/IEEE 风格、投稿信、rebuttal、caption | 参考本地 `scipilot-writing-skill` | 只吸收兼容的期刊风格和自检流程，不覆盖 CS 主线。 |
| 要论文图表、科研绘图、多面板图、Nature 风格 figure | `nature-figure` 或 `scipilot-figure-skill` | 图表设计、生成、导出和 QA。 |
| 要写完后的审稿人视角自审、方法审查、回复策略 | `review` 或 `academic-paper-de-vibe` | review 负责审稿视角；de-vibe 负责文本和逻辑清理。 |
| 新建或修改 skill | 系统 `skill-creator`；必要时参考 `writing-skills/GUIDE.md` | 按 Codex skill 规范创建或更新。 |
| 多步骤工程计划文档 | `writing-plans/GUIDE.md` | 工程任务计划，不属于论文主线。 |

## 推荐写作节奏

不要一次生成整篇论文。按以下循环推进：

1. 用 `paper-architecture-planner` 产出整篇蓝图。
2. 从 Introduction、Problem Definition 或 Related Work 开始，选一个小节交给对应子技能。
3. 对证明/威胁模型内容使用 `security-proof-builder` 起草，再交给 review 审查。
4. 用 `section-writing-polish` 把该小节改到可读、紧凑、术语一致。
5. 用 `academic-paper-de-vibe` 做局部检查。
6. 根据检查结果回到规划，更新 evidence map 和 missing inputs。
7. 继续下一个小节，直到整篇论文闭环。

## 保留资料

原有资料不删除，只降级为按需参考：

- `writing/writing-anti-ai/`: 中英文 AI 写作模式、examples 和 phrase list，核心规则已并入 `academic-paper-de-vibe`。
- `writing/humanizer/`: 泛学术去 AI 模式，按需参考。
- `writing/polish/`: 语言润色细分 guide，核心规则已并入 `section-writing-polish`。
- `paper-architecture-planner/references/legacy-top-conference-paper-writing.md`: 原顶会写作检查表备份。
- `section-drafter/references/nature-scipilot-writing-notes.md`: 从本地 SciPilot/Nature 风格技能抽取的逐节写作参考；仅在目标 venue 或用户要求匹配时读取。
- `references/local-skill-integration.md`: 本地 `.codex/skills` 中相关写作、图表、审稿技能的协作路由。

## GitHub-Informed Design Notes

当前四段式工作流吸收了公开写作技能和本地 SciPilot/Nature 风格资料中的通用思想：先 brainstorm/规划，再生成 Draft 0，自检后形成 Draft 1，再 refine/compress，最后做独立检查。不要直接复制外部模板；只保留适合计算机科学、密码学、联邦学习和隐私计算论文的流程约束。
