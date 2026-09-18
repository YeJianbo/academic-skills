---
name: paper-architecture-planner
description: 设计或重构论文主线、贡献边界、章节职责和证据布局。用于整稿蓝图与结构决策；不处理已确定结构下的局部润色。
---

# Paper Architecture Planner

用于先规划计算机科学论文，再按章节/小节逐步写作。默认面向密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文。

## 核心职责

只做架构和方向，不把整篇论文一次性写完：

1. 读取 `../../academic-hub/references/publication-story-principles.md`，从已有结果中确定 `release thesis`：解决什么问题、在哪个条件或约束下提供了什么不可替代的价值。
2. 明确研究边界：问题设定、威胁模型、隐私目标、系统假设、适用场景和不覆盖的情况。
3. 设计叙事主线：背景 -> 具体痛点 -> 现有方法缺口 -> key insight -> 构造/协议/算法 -> 证明/评估 -> 贡献。
4. 规划章节和小节职责：每一节只承担一个任务，避免重复 motivation。
5. 建立贡献-证据映射：每个贡献必须对应定义、定理、复杂度分析、实验、攻击评估或消融；为每项证据写明它支持的优势、适用条件和要排除的替代解释。
6. 根据目标 venue 调整证明、实验、artifact 和叙事权重。
7. 产出逐章写作队列，交给 `section-drafter` 一节一节写。

## 输入信息清单

若用户材料不足，先基于已有信息做草案，并标出缺口。优先收集：

- 研究问题和应用场景。
- 核心方法：协议、算法、构造、防御、系统或理论分析。
- 安全/隐私目标：保护对象、攻击者、泄露量、信任假设。
- 联邦学习设定：cross-device/cross-silo、horizontal/vertical、non-IID、客户端数量、聚合规则。
- 隐私计算工具：DP、MPC、HE、secret sharing、ZKP、TEE、secure aggregation 或混合方案。
- 主要 baseline 和本文差异。
- 已有证明、复杂度分析、实验结果、攻击评估和图表。
- 目标 venue 或论文类型：理论密码学、系统安全、FL 隐私、应用型隐私计算。
- venue profile：若不明确，先交给 `review/venue-profile-router` 判断会议适配度和证据要求。

## 规划输出格式

默认输出以下 6 个部分：

1. **Paper Thesis**: 用 1-2 句话写清论文中心主张。
2. **Advantage Frame**: 写清本文赢的是哪一场有意义的比较，以及不应成为主线的非核心维度。
3. **Positioning**: 说明论文更像理论构造、协议系统、FL 隐私防御、攻击分析还是混合型工作。
4. **Narrative Spine**: 给出从问题到贡献的递进链条。
5. **Section Blueprint**: 列出章节/小节标题、每节任务、输入材料、预期输出。
6. **Evidence Map**: 把每个贡献映射到证明、实验、复杂度或攻击评估。
7. **Writing Queue**: 给出建议写作顺序，按章节/小节拆成可逐项完成的小任务。

## 章节规划规则

### Abstract

规划 5-7 句职责，而不是直接堆细节：

1. 领域和价值。
2. 未解决痛点。
3. 本文方案。
4. 技术核心。
5. 安全/隐私或效用/效率结果。
6. 可选贡献或影响。

### Introduction

每段比上一段更窄：

1. 领域共识和应用场景。
2. 具体问题及其安全/隐私/系统后果。
3. 现有方法分组及共同局限。
4. 本文 key insight。
5. 方法概览和贡献列表。

### Background and Problem Definition

必须规划清楚：

- 参与方、输入输出、系统流程。
- FL 设置、数据分布、训练协议或推理流程。
- 安全参数、隐私预算、泄露接口和威胁模型。
- 正确性、隐私性、安全性、鲁棒性或效用目标。

### Construction / Method

按逻辑依赖排列：

1. Overview。
2. Core building blocks。
3. Protocol / algorithm / construction。
4. Correctness。
5. Security/privacy argument。
6. Complexity and implementation notes。

### Security Model and Proofs

规划 theorem 与 proof roadmap：

- 每个 theorem 证明什么。
- 依赖哪些假设。
- adversary 能力是什么。
- simulator、hybrid/game、failure event 和 advantage bound 放在哪里。
- 哪些细节进正文，哪些进 appendix。

### Evaluation

规划 utility/privacy/efficiency 三条线：

- Utility: accuracy、AUC、F1、loss、convergence、client fairness。
- Privacy/security: gradient inversion、membership inference、label inference、property inference、poisoning/backdoor、collusion。
- Efficiency: computation、communication、rounds、latency、throughput、storage、setup/proof/verification cost。
- Fair comparison: matched assumptions、security level、privacy budget、dataset split 和 model scale。

## 逐节写作流程

规划完成后，不直接生成整篇论文。按以下循环推进：

1. 选择下一个小节。
2. 给出该小节的目标、关键论点、需要引用的证据和不应写入的内容。
3. 调用或建议使用 `section-drafter` 生成该小节 Draft 0 / Draft 1。
4. 用 `section-writing-polish` 做语言、压缩和 LaTeX polish。
5. 写完后用 `academic-paper-de-vibe` 检查逻辑、AI 味、符号、证明/实验回扣。
6. 回到架构图，更新章节状态和缺口。

## 与其他写作技能的边界

- `paper-architecture-planner`: 负责论文蓝图、写作方向、章节拆分和证据映射。
- `section-drafter`: 负责按规划逐节起草 Draft 0 / Draft 1。
- `section-writing-polish`: 负责改写、翻译、精简和语言 polish。
- `academic-paper-de-vibe`: 负责最终检查 AI 味、逻辑断裂、证明摆设、实验脱节和夸大表述。

如果用户只给出一段文字并要求润色，不使用本技能，直接转 `section-writing-polish` 或 `academic-paper-de-vibe`。
