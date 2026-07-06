---
name: benchmark-baseline-registry
description: "计算机科学论文 benchmark、baseline、数据集、任务、攻击/威胁、系统负载、用户研究和评测指标注册技能。用于任意 CS 主题的调研、实验规划和审稿前检查：整理有声誉 venue 中近年常用基准、强 baseline、数据/任务划分、模型或系统设置、攻击/安全/效率/质量指标、硬件/运行环境和公平比较约束；投稿目标会议/期刊是可选适配信息，不限制文献检索范围。"
---

# Benchmark Baseline Registry

用于把“该和谁比、在什么设置下比、用什么指标比”固定下来。它服务 `survey`、`experiment-plan` 和 `review/evaluation-reproducibility-auditor`，不直接跑实验。

## 输入

- 研究方向：任意 CS 主题，如 ML/CV/NLP/LLM、systems、database、security/privacy/crypto、HCI/CSCW、PL/SE 等。
- 可选投稿目标会议或期刊。它用于确定审稿标准、常见 benchmark、实验强度和写作口径；未指定时，按主题从有声誉 venue 中整理通用强 baseline。
- 方法类型：算法、模型、系统、协议、工具、用户研究、attack/defense 或理论方法。
- 候选数据集、模型、攻击者能力、系统环境、用户任务、trace、benchmark 或 proof setting。

## 输出

默认输出一个 registry：

| 类别 | 内容 |
|---|---|
| Benchmark | 数据集、任务、划分、trace、workload、user task、预处理或 proof setting。 |
| Baseline | 经典方法、近 2-3 年 SOTA、同类协议、系统 baseline、工具 baseline 或 human/user baseline。 |
| Attack / Threat | 仅在相关主题启用：攻击者能力、泄漏面、collusion、poisoning、inversion、abuse 或安全边界。 |
| Metrics | accuracy/F1/mAP、utility、privacy/security、latency、throughput、memory、cost、quality、usability、proof/setup/verify cost。 |
| Fairness Controls | 同模型、同数据划分、同安全级别、同预算、同硬件、同 workload、同用户任务或同统计检验。 |
| Missing Evidence | 当前计划缺少的 baseline、攻击、数据集或指标。 |

## 领域检查点

- ML/CV/NLP/LLM：数据划分、模型容量、pretraining/fine-tuning 设置、prompt/eval protocol、seed、compute budget。
- Systems/DB/OS/Networks：workload、trace、hardware、latency/throughput、tail latency、资源占用、并发度、failure mode。
- HCI/CSCW：用户任务、招募标准、样本量、问卷/日志指标、统计检验、伦理和可用性风险。
- PL/SE：benchmark suite、bug corpus、static/dynamic analysis setting、false positive/negative、runtime overhead。
- FL：client 数、sampling rate、local epochs、heterogeneity、cross-device/cross-silo、aggregation rule。
- Privacy ML：epsilon/delta、attack success rate、privacy-utility curve、threat model alignment。
- Crypto：security parameter、correctness error、leakage、communication rounds、setup/proof/verify cost。
- Privacy computing systems：trust assumptions、TEE/HE/MPC setup cost、network latency、collusion model、failure mode。

## 使用规则

- 先列“必须比较”的 baseline，再列“可选增强”的 baseline。
- 对每个 baseline 说明为什么相关，避免只因知名而加入。
- 不能把安全级别、隐私预算、模型容量或数据划分不同的结果直接比较。
- 发现缺关键 baseline 时，回到 `experiment-plan` 更新 run order。
- 发现威胁模型不可比时，交给 `security-privacy-auditor`。
