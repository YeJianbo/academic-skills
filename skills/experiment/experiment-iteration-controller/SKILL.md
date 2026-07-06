---
name: experiment-iteration-controller
description: "计算机科学实验迭代控制技能。用于联邦学习、隐私计算、密码学、安全与隐私保护机器学习论文实验的多轮闭环管理：把 hypothesis、claim map、pilot 结果和失败日志转成下一轮 run queue、停止/回退标准、baseline/ablation 补强计划、leaderboard 和可验证结论；适合需要反复小实验验证 idea、失败后重设假设、比较多条方法路线、或决定是否进入主实验。"
---

# Experiment Iteration Controller

用于控制实验从 idea 到可投稿证据的多轮迭代。它不替代 `run-experiment` 执行命令，也不替代 `experiment-results-analyzer` 解释指标；它负责决定下一轮该跑什么、为什么跑、何时停止、何时回到选题。

## 输入

- `experiment-plan` 的 claim map、baseline、attack、ablation、compute budget。
- `run-experiment` 的 run logs、失败原因、artifact paths。
- `experiment-results-analyzer` 的 claim support matrix。
- 目标会议或期刊对实验完整性的要求。
- 本机资源约束：conda 环境、CUDA/cu121/cu128、GPU 数量、可接受运行时长。

## 核心状态

维护一个轻量实验状态表：

| 字段 | 含义 |
|---|---|
| `hypothesis_id` | 当前要验证的科学假设。 |
| `claim` | 论文主张，必须能落到指标或证明。 |
| `run_id` | 具体实验编号。 |
| `stage` | sanity、pilot、main、ablation、sensitivity、robustness、efficiency。 |
| `config` | 数据集、模型、客户端设置、隐私预算、攻击强度、安全参数。 |
| `expected_signal` | 预期观察到的方向和最小效果。 |
| `actual_result` | 已观察指标或错误。 |
| `decision` | continue、retry、modify、drop、escalate-to-review、return-to-survey。 |
| `reason` | 决策依据，不能只写“效果不好”。 |

## 工作流

1. **初始化队列**：从 claim map 生成最小 run queue，先 sanity 和 pilot，再主实验。
2. **设置停止标准**：每个 hypothesis 必须有 go/no-go 标准，例如最小 utility gain、attack reduction、latency ceiling、communication budget。
3. **运行后归档**：每轮后读取结果分析报告，更新状态表和 failure log。
4. **判定下一步**：
   - 实现或环境失败：交回 `run-experiment` 修复，不作为科学失败。
   - 指标无信号：缩小变量，检查 baseline、公平性和超参，再决定是否 drop。
   - 单一数据集有效：补跨数据集或分布设置。
   - 只在弱 baseline 上有效：补强 baseline 或降低 claim。
   - 隐私/安全主张未被实验覆盖：转 `security-privacy-auditor` 或增加攻击/泄漏评估。
5. **形成 leaderboard**：同一 hypothesis 下保留所有候选方法、baseline 和 ablation 的最好可信结果，不只保留成功 run。
6. **收敛**：当主 claim 有主实验、消融、敏感性、效率和失败案例支撑时，交给 `paper-figure` 和 `reproducibility-packager`。

## 失败分类

- `implementation_bug`: 代码、数据、指标或日志错误。
- `environment_failure`: CUDA、驱动、依赖、显存、路径问题。
- `underpowered_pilot`: 数据太小、epoch 太少、seed 太少，不能下结论。
- `hypothesis_unsupported`: 控制变量充分后仍无效果。
- `baseline_gap`: baseline 不公平、不够强或缺关键方法。
- `metric_mismatch`: 指标不能支持论文 claim。
- `threat_model_gap`: 攻击者能力、信任假设或泄漏定义不匹配。
- `compute_infeasible`: 本机无法在合理时间实现投稿级证据。

## 输出

默认输出：

```markdown
**Iteration State**
| Hypothesis | Stage | Best Evidence | Decision | Reason |

**Run Queue**
| Priority | Run | Purpose | Config | Stop Criterion |

**Failure Log**
| Run | Failure Type | Evidence | Fix or Decision |

**Leaderboard**
| Method | Dataset/Setting | Utility | Privacy/Security | Efficiency | Notes |

**Next Action**
...
```

## GitHub 工作流参考

当需要借鉴外部 CS 实验代理或复现模板时，读取 `references/github-experiment-workflow-notes.md`。这些参考只提供工作流启发，不复制其模板，也不把通用 ML 自动化流程直接套到密码学或隐私计算论文上。

## 交接

- 需要执行命令和收集 artifact：交给 `run-experiment`。
- 需要判断指标是否支持 claim：交给 `experiment-results-analyzer`。
- 需要审查实验公平性：交给 `review/evaluation-reproducibility-auditor`。
- 小实验失败且无合理补救路径：回到 `survey/cs-idea-discovery-pipeline` 重新选题。
