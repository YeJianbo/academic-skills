---
name: review
description: "计算机科学论文审查总入口：面向密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文的投稿前自审、模拟审稿、安全/隐私证明审查、实验与复现审查、rebuttal 与修订规划；路由到 cs-paper-reviewer、security-privacy-auditor、evaluation-reproducibility-auditor、rebuttal-revision-planner，并保留 academic-paper-reviewer、paper-review、paper-self-review 等旧资料为参考。"
---

# Review

用于计算机科学论文、实验和修订材料的质量审查。默认只生成审查报告，不直接改论文正文；需要重写或润色时转到 `writing`。

## 主审查工作流

1. `cs-paper-reviewer`: 论文整体投稿前审查或模拟审稿；结合 `academic-paper-reviewer` 的多 reviewer + editorial synthesis 框架。
2. `security-privacy-auditor`: 威胁模型、安全/隐私定义、定理、证明和攻击模型专项审查。
3. `evaluation-reproducibility-auditor`: 实验设计、baseline、公平比较、复现性和效率评估专项审查。
4. `rebuttal-revision-planner`: 根据审稿意见制定 rebuttal、response letter 和修订路线。

## 路由表

| 用户需求 | 使用技能 | 输出 |
|---|---|---|
| 投稿前整体把关、模拟审稿、判断能否投 | `cs-paper-reviewer` | CS 专版多视角 peer review、editorial synthesis、评分、风险、修订优先级。 |
| 检查 threat model、security/privacy claim、proof 是否站得住 | `security-privacy-auditor` | 模型/定义/证明/假设/泄露边界问题清单。 |
| 检查 FL/隐私计算实验、攻击评估、效率、复现性 | `evaluation-reproducibility-auditor` | 实验充分性、公平性、复现性和缺失实验报告。 |
| 收到审稿意见后准备回复和修订 | `rebuttal-revision-planner` | comment taxonomy、response strategy、revision plan、response letter skeleton。 |
| 泛学术多视角审稿或期刊式模拟 | 参考 `academic-paper-reviewer/GUIDE.md` | EIC + 多 reviewer 模拟流程。 |
| 通用 peer review、paper reading、review response guide | 参考 `paper-review/` | 通用审稿资料包。 |
| 简单投稿前 checklist | 参考 `paper-self-review/GUIDE.md` | 自查 checklist。 |

## 审查输出规范

所有审查都按以下顺序输出：

1. **Decision / Readiness**: Accept-like、Weak Accept、Borderline、Weak Reject、Reject-like，或 Ready / Not Ready。
2. **Critical Issues**: 会推翻核心结论或导致拒稿的问题。
3. **Major Issues**: 需要补实验、补证明、改设定或重写主张的问题。
4. **Minor Issues**: 术语、表达、图表、引用、组织上的修复项。
5. **Questions for Authors**: 需要作者确认的信息。
6. **What Would Change My Mind**: 每个 Critical/Major 问题必须说明什么证据、证明或实验能解决。
7. **Revision Priority**: 按先后顺序给出可执行修订路线。

## 严重性标准

- `Critical`: threat model 错、定理不支持主张、实验反驳结论、baseline 不可比、核心攻击漏掉。
- `Major`: 缺关键定义、证明路线不清、实验设置不完整、缺主要 baseline、复现信息不足。
- `Minor`: 写法、符号、表述、caption、引用密度、术语一致性问题。
- `Question`: 信息不足，不能直接判定。

## 与 Writing 的关系

- 先写作：`writing` 的规划 -> 起草 -> 润色 -> de-vibe。
- 后审查：本 `review` 做投稿前体检和模拟审稿。
- 审查发现需要重写：回到 `writing/section-drafter` 或 `writing/section-writing-polish`。
- 审查发现 AI 味：回到 `writing/academic-paper-de-vibe`。

## 保留资料

原有资料不删除，只作为按需参考：

- `academic-paper-reviewer/`: 多 reviewer 模拟、editorial decision、质量 rubric；已作为 `cs-paper-reviewer` 的基础审稿框架。
- `paper-review/`: 通用 peer review、paper critique、paper reading、rebuttal/response guide。
- `paper-self-review/`: 投稿前 checklist。
- `references/legacy-review-router.md`: 旧 review 入口备份。
