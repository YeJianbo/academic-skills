---
name: experiment
description: "计算机科学实验入口：面向联邦学习、隐私计算、密码学、安全与隐私保护机器学习论文的实验规划、迭代控制、代码实现、conda/CUDA/cu121/cu128 运行、pilot 验证、消融、复现、结果分析、论文图表和 artifact 打包；路由到 experiment-plan、experiment-iteration-controller、run-experiment、experiment-results-analyzer、paper-figure、reproducibility-packager。"
---

# Experiment

用于学术实验全流程。默认服务计算机科学论文，尤其是联邦学习、隐私计算、密码学、安全与隐私保护机器学习。

## 主工作流

1. `experiment-plan`: 把 idea 或论文 claim 转成 claim -> evidence -> run order 的实验计划。
2. `experiment-iteration-controller`: 管理 hypothesis、run queue、失败日志、leaderboard 和 go/no-go 决策。
3. `run-experiment`: 在本机 conda/CUDA 或远程 GPU 上实现、部署、运行实验。
4. `experiment-results-analyzer`: 汇总日志、表格和曲线，判断假设是否成立并规划下一轮。
5. `paper-figure`: 从实验结果生成论文图表、LaTeX snippets 和 figure QA。
6. `reproducibility-packager`: 整理 README、环境、脚本、配置、seed、manifest 和 expected outputs。

## 路由表

| 用户需求 | 使用技能 | 输出 |
|---|---|---|
| idea 已有，需要设计实验、消融、baseline、攻击评估 | `experiment-plan` | claim map、experiment blocks、run order、compute budget、risks。 |
| 需要确定 benchmark、baseline、攻击和指标是否完整 | `survey/benchmark-baseline-registry` | benchmark registry、baseline registry、metric/fairness controls。 |
| 需要多轮 pilot、失败后迭代、决定继续/放弃/回到选题 | `experiment-iteration-controller` | iteration state、run queue、failure log、leaderboard、next action。 |
| 需要写代码、跑训练、跑 pilot、部署到 GPU | `run-experiment` | 环境检查、运行命令、日志路径、结果文件、失败处理。 |
| 已有结果，需要分析是否支持 hypothesis | `experiment-results-analyzer` | result matrix、claim support、失败原因、下一轮实验。 |
| 需要画论文图、表格、曲线、多面板图 | `paper-figure` | publication-ready figures、表格、LaTeX include snippets。 |
| 投稿前需要开源代码、artifact appendix、内部复现包 | `reproducibility-packager` | README、environment、run scripts、configs、manifest、expected outputs。 |
| 需要方法/实验设计审查 | `review/evaluation-reproducibility-auditor` | 公平性、baseline、攻击、复现性审查。 |
| 结果写回论文 | `writing/section-drafter` 或 `section-writing-polish` | Results / Analysis 段落。 |

## 本机环境默认假设

- Python 使用 conda 环境。
- CUDA 已配置，可能有 cu121 和 cu128。
- 每次运行前先探测 `conda info`、`nvidia-smi`、`python`、`torch.cuda.is_available()`。
- 优先做 sanity / pilot，再做完整训练。
- 所有实验必须记录 seed、commit/代码版本、环境、参数、输出路径。

## 实验节奏

1. Sanity: 最小数据、最小 epoch、验证代码和指标通路。
2. Pilot: 1-3 小时内验证核心假设是否有信号。
3. Iteration: 根据 pilot 结果更新 run queue、failure log、leaderboard 和 go/no-go 标准。
4. Main: 标准设置下跑主要对比。
5. Ablation: 移除/替换核心组件。
6. Sensitivity: privacy budget、client count、non-IID、attack strength、security parameter。
7. Robustness: 多 seed、多数据集、不同模型或攻击。
8. Paper artifacts: 结果表、图、LaTeX snippets、实验描述。
9. Reproducibility package: README、环境、脚本、配置、seed、manifest、expected outputs。

## 保留资料

原有 GUIDE 不删除，只降级为按需参考：

- `experiment-plan/GUIDE.md`: 旧 claim-driven experiment plan。
- `experiment-bridge/GUIDE.md`: 从计划到代码和初始结果的桥接流程。
- `run-experiment/GUIDE.md`: 旧 GPU 运行流程。
- `paper-figure/`、`academic-plotting/`: 图表资料。
- `experiment-iteration-controller/references/github-experiment-workflow-notes.md`: 从 MLAgentBench、AI-Scientist、reproducible ML templates 提炼的 CS 实验闭环参考。
- `paper-compile/`、`paper-slides/`、`paper-poster/`: 论文编译、展示材料，默认转 `tools` 或 presentation 相关技能。
- `scientific-critical-thinking/`: 实验假设和证据质量的批判性参考。
