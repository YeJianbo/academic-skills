---
name: experiment-results-analyzer
description: "计算机科学实验结果分析技能。用于汇总和解释联邦学习、隐私计算、安全与隐私保护机器学习实验日志、CSV/JSON 指标、表格和曲线，判断 hypothesis 是否被支持，定位失败原因，生成下一轮实验计划、论文结果表述和审稿风险。"
---

# Experiment Results Analyzer

用于把实验输出转成科学结论和下一轮行动。

## 输入

- metrics csv/json、训练日志、攻击评估结果、复杂度/延迟/通信统计。
- experiment plan 或 claim map。
- 配置文件、seed、数据集、模型、baseline 信息。

## 分析流程

1. **Load and normalize**: 统一 run id、seed、metric、dataset、method、setting。
2. **Aggregate**: mean/std、confidence interval、best/last、convergence rounds。
3. **Compare**: against baselines, attacks, privacy budget, client count, non-IID level。
4. **Claim support**: 判断每个 claim 是 supported、partially supported、unsupported、inconclusive。
5. **Failure diagnosis**: 区分实现 bug、环境失败、超参问题、假设不成立、baseline 太强、数据不适配。
6. **Next experiments**: 给出最小下一步实验，不生成无边界 wishlist。

## 输出格式

```markdown
**Result Summary**
...

**Claim Support Matrix**
| Claim | Evidence | Status | Notes |
...

**Key Tables/Figures to Produce**
...

**Failure Diagnosis**
...

**Next Experiment Plan**
...

**Paper-Writing Notes**
...
```

## 写作交接

- 图表交给 `paper-figure`。
- Results 段落交给 `writing/section-drafter`。
- 审稿风险交给 `review/evaluation-reproducibility-auditor`。
