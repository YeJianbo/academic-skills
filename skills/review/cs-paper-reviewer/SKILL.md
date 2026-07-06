---
name: cs-paper-reviewer
description: "计算机科学论文整体审查技能，结合 academic-paper-reviewer 的多视角 peer review 和 editorial synthesis 框架。用于密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文的投稿前自审、模拟审稿、顶会/安全会议质量评估、结构与贡献审查、claim-evidence 对齐、相关工作定位、图表和实验完整性检查；不直接改稿，只输出 findings-first 审查报告。"
---

# CS Paper Reviewer

用于整篇论文的投稿前审查或模拟审稿。默认标准面向 CS 顶会/安全会议/隐私会议，如 CCS、USENIX Security、IEEE S&P、NDSS、PETS、CRYPTO、EUROCRYPT、ASIACRYPT、TCC、NeurIPS、ICML、ICLR。

本技能继承 `academic-paper-reviewer` 的好用框架：先配置 reviewer 视角，再独立审稿，最后做 editorial synthesis。区别是 reviewer 角色、评分维度和 blocking risks 都改成 CS/密码学/FL/隐私计算语境。

## 审查流程

1. Identify paper type: theory crypto、protocol/system、FL privacy、attack/defense、privacy-preserving ML、hybrid.
2. Extract central thesis: problem、model、method、guarantee、evidence、claimed improvement.
3. Configure reviewer panel.
4. Run independent perspective reviews.
5. Build claim-evidence map: every contribution must map to proof、experiment、complexity analysis、attack evaluation、or ablation.
6. Synthesize reviewer disagreement into editorial decision and revision roadmap.
7. Produce findings first, ordered by severity.

## Reviewer Panel

Use 5 perspectives by default:

1. **Area Chair / EIC**: venue fit, novelty, significance, paper maturity, likely decision.
2. **Security and Privacy Reviewer**: threat model, privacy/security definitions, assumptions, leakage, proofs.
3. **FL / Systems / Evaluation Reviewer**: experimental design, baselines, utility/privacy/efficiency tradeoff, reproducibility.
4. **Domain and Related Work Reviewer**: positioning, missing literature, comparison fairness, contribution clarity.
5. **Devil's Advocate Reviewer**: strongest rejection case, hidden assumptions, overclaiming, alternative explanations.

Each reviewer must review independently. The final synthesis may aggregate and resolve disagreements, but it must not invent comments not supported by the perspective reviews.

## Scoring Dimensions

Score each dimension from 1-5, adapted from `academic-paper-reviewer`:

| Dimension | Weight | CS-specific meaning |
|---|---:|---|
| Originality and positioning | 15% | New problem, construction, attack/defense, system, or insight beyond prior work. |
| Technical rigor | 25% | Correct definitions, protocol/algorithm soundness, proof validity, implementation faithfulness. |
| Evidence sufficiency | 20% | Claims supported by theorems, experiments, complexity analysis, attacks, or ablations. |
| Model and assumption clarity | 15% | Threat/privacy model, leakage, trust assumptions, FL setting, scope boundaries. |
| Evaluation and reproducibility | 10% | Fair baselines, matched assumptions, attack coverage, released details, parameter reporting. |
| Argument coherence and writing | 10% | Clear narrative, section roles, claim-evidence alignment, readable prose. |
| Impact and venue fit | 5% | Relevance to target CS venue and field-level significance. |

Decision calibration:

- `Accept-like`: no Critical issues, weighted score >= 4.0, strong venue fit.
- `Weak Accept / Minor Revision`: no Critical issues, most dimensions >= 3.5, fixes are local.
- `Borderline / Major Revision`: promising but has Major issues requiring new proof, experiment, positioning, or restructuring.
- `Reject-like`: any unresolved Critical issue or core evidence/model failure.

## 核心审查维度

- **Problem fit**: 问题是否真实、具体、与目标 venue 匹配。
- **Novelty and positioning**: 与现有密码学/FL/隐私计算工作差异是否清楚。
- **Model validity**: threat model、privacy model、trust assumption 是否明确且合理。
- **Technical correctness**: 构造、算法、协议、定理、证明是否支持主张。
- **Evaluation sufficiency**: baseline、attack、utility、privacy、efficiency、ablation 是否足够。
- **Reproducibility**: 数据、代码、参数、随机种子、硬件、实现细节是否可复现。
- **Writing and organization**: 论文主线是否递进，章节是否各司其职。

## Perspective Review Output

For each reviewer perspective, produce:

- `Recommendation`: Accept-like / Weak Accept / Borderline / Weak Reject / Reject-like.
- `Confidence`: 1-5.
- `Strengths`: 2-4 specific strengths with section/page references when available.
- `Weaknesses`: 3-5 issues with severity and concrete fixes.
- `What would change my mind`: required for every Critical/Major issue.

Then synthesize:

- consensus issues,
- reviewer disagreements,
- final decision,
- revision roadmap.

## 输出格式

```markdown
**Decision / Readiness**
...

**Reviewer Panel Summary**
| Perspective | Recommendation | Confidence | Key Concern |
...

**Scorecard**
| Dimension | Score | Rationale |
...

**Critical Issues**
...

**Major Issues**
...

**Minor Issues**
...

**Questions for Authors**
...

**What Would Change My Mind**
...

**Revision Priority**
...
```

若用户要求 quick review，只输出 top 5 blocking risks 和 next actions。

## Academic Paper Reviewer References

Use these existing references only when a deeper simulated-review structure is needed:

- `../academic-paper-reviewer/GUIDE.md`: multi-agent review workflow.
- `../academic-paper-reviewer/references/review_criteria_framework.md`: universal review dimensions and scoring logic.
- `../academic-paper-reviewer/references/editorial_decision_standards.md`: decision calibration.
- `../academic-paper-reviewer/templates/peer_review_report_template.md`: reviewer report structure.
