---
name: run-experiment
description: 实现、执行和恢复已授权的 CPU/GPU 科学实验，保留配置、seed、原始日志与结果。复用有效环境检查；实验设计和已产结果解释使用对应专用技能。
---

# Run Experiment

用于把实验计划变成可运行代码和可追踪结果。默认先做小实验，不直接启动完整大规模训练。

## 环境探测

首次使用或运行环境变化时检查相关项并记录；已有有效结果直接复用，未使用的 conda、GPU 或 PyTorch 不检查：

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
3. **Pilot**: 以最小可判别规模验证核心 hypothesis；预算和停止条件按问题、已有结果与用户资源确定。
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

## 文件组织

沿用项目已有 run 目录和配置入口；临时提取、转换与调试文件集中放到当前任务工作目录。真实实验 run 的参数、原始日志、seed 和结果保留，不能用“原位迭代”覆盖不同实验的证据。汇总表、当前图和报告可在规范路径更新，内容未变不重复写入或导出。

## 输出

输出运行报告：

- environment summary
- command list
- artifact paths
- passed/failed runs
- preliminary metrics
- next run recommendation
