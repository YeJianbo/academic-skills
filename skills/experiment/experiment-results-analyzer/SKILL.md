---
name: experiment-results-analyzer
description: 分析已有实验日志、指标和结果，判断假设支持程度、失败原因和下一步。保留真实数值及条件；新实验执行和图形渲染使用对应技能。
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
4. **Story selection**: 读取 `../../academic-hub/references/publication-story-principles.md`，标记最强、可复核且能支持 `release thesis` 的结果、条件和比较口径。
5. **Claim support**: 判断每个 claim 是 supported、partially supported、unsupported、inconclusive；核心 claim 的反证不能从分析中省略。
6. **Failure diagnosis**: 区分实现 bug、环境失败、超参问题、假设不成立、baseline 太强、数据不适配。
7. **Next experiments**: 给出最小下一步实验，不生成无边界 wishlist。

## 输出格式

```markdown
**Result Summary**
...

**Claim Support Matrix**
| Claim | Evidence | Status | Notes |
...

**Key Tables/Figures to Produce**
...

**Release Evidence Frame**
| Core thesis | Strongest evidence | Valid conditions | Figure/table role |
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
