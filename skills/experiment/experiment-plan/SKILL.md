---
name: experiment-plan
description: "计算机科学实验规划技能。用于把联邦学习、隐私计算、密码学、安全与隐私保护机器学习论文 idea 或 claim 转成可执行实验路线，包含 claim-evidence map、baseline、攻击评估、消融、超参敏感性、计算预算、运行顺序和复现要求。"
---

# Experiment Plan

用于在写代码和跑实验前，把论文主张拆成可验证证据。

## 发布会式实验设计

先读取 `../../academic-hub/references/publication-story-principles.md`，再确定实验。先从已有先导结果或机制推断中选择一个可证实的 `release thesis`；不要为了凑完整指标表而把非优势维度设为主战场。每个实验 block 必须写明它服务的 thesis、支持条件、关键对比和要排除的替代解释。

## 输入

- paper idea 或 hypothesis。
- 目标会议/论文 claim。
- 方法概要：FL 算法、隐私协议、攻击/防御、DP/MPC/HE/TEE/secure aggregation 等。
- 可用数据集、模型、代码库、GPU/CPU 资源。
- 预期比较对象和指标。

## 输出

默认输出：

1. **Claim Map**: 每个论文主张对应需要什么证据，并标注是否属于核心 `release thesis`。
2. **Experiment Blocks**: sanity、pilot、main comparison、ablation、sensitivity、robustness、efficiency；每个 block 标明论证职责。
3. **Baselines and Attacks**: 需要比较的算法、协议、攻击和防御。
4. **Metrics**: utility、privacy/security、efficiency、reproducibility。
5. **Run Order**: 先跑什么，失败如何停止或回退。
6. **Compute Budget**: 数据规模、epoch、seed、GPU、预计耗时。
7. **Risk Register**: 可能失败的点、会影响 thesis 的反例和替代实验。

## CS/FL/隐私计算必检项

- FL: cross-device/cross-silo、horizontal/vertical、non-IID、client sampling、local epochs、aggregation rule。
- Privacy: DP budget、attack success、leakage、collusion、trust assumptions。
- Crypto/system: communication、rounds、latency、throughput、storage、setup/proof/verification cost。
- Fairness: matched security level、matched model、matched dataset split、matched attacker knowledge。

## 交接

- 计划完成后交给 `run-experiment`。
- 实验设计争议交给 `review/evaluation-reproducibility-auditor`。
- 结果回来后交给 `experiment-results-analyzer`。
