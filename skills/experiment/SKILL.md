---
name: experiment
description: "协调实验设计、执行、迭代与结果交付。明确的运行、日志分析、作图或复现包任务直接进入专用技能。"
---

# Experiment

围绕本次科学问题安排必要工作，复用已有实验和环境检查，不把所有阶段设为每次运行的前置流程。

| 交付 | 负责技能 |
|---|---|
| hypothesis、指标、消融、攻击与证据结构设计 | `experiment-plan` |
| 查找或整理 benchmark 与 baseline | `benchmark-baseline-registry` |
| 多轮 run 队列、停止/回退与下一轮决策 | `experiment-iteration-controller` |
| 实现、执行与恢复具体实验 | `run-experiment` |
| 分析日志和已产生结果，判断假设支持程度 | `experiment-results-analyzer` |
| 组织主结果/消融图表组合及 LaTeX 接入 | `paper-figure` |
| 单张数据图或已有图局部修改 | `nature-figure` |
| 打包代码、环境、参数与复现说明 | `reproducibility-packager` |

实验规模与 pilot 预算由假设和资源决定。首次使用或环境变化才检查相关依赖，CPU/理论任务不默认检查 GPU。保留 seed、代码版本、配置、原始日志和结果；不得覆盖不同 run 的证据。

只有需要重构研究主线时才读 `../academic-hub/references/publication-story-principles.md`。文件交接按需读 `../academic-hub/references/incremental-academic-workflows.md`。已有 GUIDE、绘图配方、编译与展示资料继续按需使用。
