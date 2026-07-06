---
name: run-experiment
description: "计算机科学实验运行技能。用于在本机 conda/CUDA/cu121/cu128 或远程 GPU 环境中实现、部署和运行联邦学习、隐私计算、安全与隐私保护机器学习实验；覆盖环境探测、sanity check、pilot experiment、批量运行、日志管理、失败恢复和结果收集。"
---

# Run Experiment

用于把实验计划变成可运行代码和可追踪结果。默认先做小实验，不直接启动完整大规模训练。

## 环境探测

运行前检查并记录：

- `conda info`
- `nvidia-smi`
- Python 路径和版本
- PyTorch / CUDA 可用性
- 当前 git 状态或代码版本
- 可用 GPU、显存、驱动、CUDA runtime

若存在多个 CUDA 环境，如 cu121 和 cu128，优先选择当前项目依赖已安装且 `torch.cuda.is_available()` 为 true 的环境。

## 运行顺序

1. **Preflight**: 安装/导入检查，数据路径检查，配置解析。
2. **Sanity**: tiny data、1 seed、1 epoch 或最小 protocol run。
3. **Pilot**: 小规模验证核心 hypothesis，控制在 1-3 小时内。
4. **Batch Runs**: 多 seed、多配置、主实验。
5. **Ablation/Sensitivity**: 按 `experiment-plan` 指定矩阵执行。
6. **Collection**: 汇总 logs、metrics、artifacts、failed runs。

## 记录要求

每次运行都保存：

- run id、时间、命令、conda env、GPU、seed。
- config 文件或参数。
- stdout/stderr log。
- metrics csv/json。
- checkpoints 或中间结果路径。
- failure reason 和 retry policy。

## 失败处理

- 环境失败：修环境或降级 CPU/microbenchmark，不当作科学结论。
- OOM：降低 batch/model/client count，记录降级。
- 数值异常：先 tiny debug，再检查 loss、梯度、数据归一化。
- pilot 不支持假设：交给 `experiment-results-analyzer` 判断是否回到 `survey/cs-idea-discovery-pipeline`。

## 输出

输出运行报告：

- environment summary
- command list
- artifact paths
- passed/failed runs
- preliminary metrics
- next run recommendation
