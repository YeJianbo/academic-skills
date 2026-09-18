---
name: evaluation-reproducibility-auditor
description: 审查实验公平性、攻击评估、baseline、指标和复现证据。输出问题与修复条件；实验设计、运行和图表美化各有专用技能。
---

# Evaluation Reproducibility Auditor

用于判断实验是否足以支撑论文主张。重点不是“指标是否好看”，而是比较是否公平、攻击是否覆盖、隐私/效用/效率权衡是否完整、复现信息是否足够。

## 审查维度

1. **Task and setting**: 数据集、模型、FL 类型、non-IID 划分、客户端数量、local epochs、aggregation rule。
2. **Baselines**: 是否覆盖经典方法、近年 SOTA、同类 threat model 和同等安全等级。
3. **Attacks and privacy tests**: gradient inversion、membership inference、property inference、label inference、poisoning/backdoor、collusion。
4. **Utility metrics**: accuracy、AUC、F1、loss、convergence、client fairness、task-specific metrics。
5. **Efficiency metrics**: computation、communication、rounds、latency、throughput、memory、storage、setup/proof/verification cost。
6. **Ablation and sensitivity**: privacy budget、security parameter、client count、non-IID degree、model size、malicious ratio。
7. **Reproducibility**: code、data、seeds、hardware、libraries、crypto backend、DP accountant、curve/field/modulus。

## Fairness Checks

- Matched privacy budget/security level.
- Matched model architecture and dataset split.
- Matched adversary knowledge and attack budget.
- Same communication accounting.
- Same preprocessing and client sampling.
- Report variance across runs, not one lucky seed.

## 输出格式

```markdown
**Evaluation Verdict**
...

**Missing or Unfair Comparisons**
...

**Attack Evaluation Gaps**
...

**Utility/Privacy/Efficiency Tradeoff Issues**
...

**Reproducibility Gaps**
...

**Experiments to Add First**
...
```
