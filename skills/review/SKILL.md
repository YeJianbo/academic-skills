---
name: review
description: "确定学术审查范围并协调专项检查。整篇评审、安全证明、实验复现或审稿回复已有明确目标时，直接使用相应专用技能。"
---

# Review

按被审查对象和用户需要的判断选择负责人。仅审查时不改稿；若用户同时授权修订，交接具体问题后继续修改，不追加一次许可询问。

| 交付 | 负责技能 |
|---|---|
| 整篇论文审查、写作评审、评分或版本对比 | `cs-paper-reviewer` |
| threat model、泄露、定义与证明专项检查 | `security-privacy-auditor` |
| baseline、公平性、攻击评估和复现专项检查 | `evaluation-reproducibility-auditor` |
| 审稿意见回复、response letter 与修订安排 | `rebuttal-revision-planner` |
| 按已知意见改写正文 | `section-drafter` 或 `section-writing-polish` |

问题须有原文、代码、来源或实验位置。遵守适用的 SOUND/MINOR ISSUES/MAJOR ISSUES/CRITICAL ERRORS 严重度；每个主要问题说明能改变判断的证据。整体 readiness 只在范围足够时给出，局部检查不强制整篇录用分数。

对版本比较，将相对进步和当前成熟度分开；单线程多视角检查与独立代理复审如实区分。默认不扩成五个代理或完整检索，必要证据缺口才转对应技能。

旧 `academic-paper-reviewer/`、`paper-review/`、`paper-self-review/` 保留为参考。复杂版本交接按需读 `../academic-hub/references/incremental-academic-workflows.md`。
