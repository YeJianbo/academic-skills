---
name: evaluation-reproducibility-auditor
description: "实验与复现专项审查技能。用于审查联邦学习、隐私计算、安全与隐私保护机器学习论文中的实验设计、baseline 公平性、攻击评估、utility/privacy/efficiency tradeoff、消融、超参敏感性、复杂度、实现细节、数据划分、随机性、硬件环境和复现材料。"
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
