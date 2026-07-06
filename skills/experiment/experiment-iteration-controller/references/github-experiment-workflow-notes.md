# GitHub Experiment Workflow Notes

用于在计算机科学实验技能中吸收外部项目的工作流经验。只保留可迁移机制，不复制项目模板。

源参考：

- https://github.com/snap-stanford/MLAgentBench
- https://github.com/SakanaAI/AI-Scientist
- https://github.com/SakanaAI/AI-Scientist-ICLR2025-Workshop-Experiment
- https://github.com/drivendataorg/cookiecutter-data-science
- https://github.com/carlomazzaferro/reproducible-ml

## MLAgentBench

可借鉴点：

- 把任务做成可交互研究环境：读取文件、运行实验、分析结果、继续迭代。
- 明确记录 agent log、environment log、traces、error file 和 overall time。
- 系统化运行：并行 run、baseline run、evaluation json、plot script。
- 强调日志捕获，因为 OOM 和 runtime error 需要从日志中定位。

迁移到本地 skill：

- 每轮实验必须留下 run id、命令、日志、错误、metrics 和 artifact paths。
- 维护 run queue 和 leaderboard，避免只保存成功结果。
- sanity/pilot/main/ablation 分层推进，失败先分类再决策。

## AI-Scientist / AutoResearch 类流程

可借鉴点：

- 使用 template 约束实验入口、绘图脚本、prompt/idea 文件和 LaTeX 输出。
- 每个实验模板需要 baseline run、experiment script、plot script 和 paper artifacts。
- 支持并行 idea，但要求对自动执行代码做隔离和风险控制。
- 研究循环包含 idea、experiment、paper generation、review。

迁移到本地 skill：

- 对每个候选 idea 建立 hypothesis id 和最小 pilot。
- 在进入大规模实验前先有 baseline、plot script 和结果解析通路。
- 自动化只服务证据收集，最终 claim 仍由主线程根据结果裁判。

## Reproducible ML Templates

可借鉴点：

- 复现包需要固定环境、运行入口、数据说明、结果生成脚本、图表生成脚本和论文构建路径。
- 数据科学项目模板强调清晰目录结构，论文代码模板强调从实验到 figures/tables/pdf 的可执行链条。
- 研究代码发布模板强调 README、BibTeX、主要结果、安装、数据、训练、评估和预训练/结果 artifact。

迁移到本地 skill：

- 复现材料交给 `reproducibility-packager` 输出 manifest。
- 每张图或表都要能从脚本重新生成。
- 随机种子、git 状态、环境、数据 hash、CUDA/driver 信息和硬件信息必须记录。
