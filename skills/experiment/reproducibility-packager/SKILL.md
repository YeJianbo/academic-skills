---
name: reproducibility-packager
description: "计算机科学论文复现包整理技能。用于把联邦学习、隐私计算、密码学、安全与隐私保护机器学习实验整理成可交付 artifact：README、环境文件、运行脚本、配置、seed、数据说明、结果 manifest、figure/table 生成脚本、硬件与 CUDA 记录、expected outputs 和复现风险清单；适合投稿前 artifact appendix、开源代码、审稿补充材料和内部复现实验。"
---

# Reproducibility Packager

用于把已经跑通的实验整理成别人能复现、自己以后能追溯的研究 artifact。它不补做科学实验；若证据不足，先回到 `experiment-iteration-controller`。

## 输入

- 项目代码目录。
- 已确认的运行命令、配置、日志、metrics、figures、tables。
- `experiment-results-analyzer` 的最终结果摘要。
- 目标会议/期刊的 artifact 或 reproducibility 要求。

## 必备产物

1. **README**：说明论文标题、任务、安装、数据准备、快速复现、完整复现、结果位置。
2. **Environment**：`environment.yml`、`requirements.txt`、Dockerfile 或明确的 conda/pip 安装命令。
3. **Run Scripts**：sanity、pilot、main、ablation、sensitivity、evaluation、figure/table 生成脚本。
4. **Configs**：所有关键 run 的配置文件或命令参数。
5. **Seeds**：每个 run 的 seed；多 seed 结果要保留聚合方式。
6. **Data Manifest**：数据来源、版本、划分、预处理、hash、是否可公开。
7. **Results Manifest**：run id、命令、commit、环境、GPU、输出路径、指标、失败 run。
8. **Expected Outputs**：关键表格、图、指标范围和复现时间估计。
9. **Hardware Record**：GPU 型号与数量、CUDA/cu121/cu128、driver、PyTorch/CUDA runtime、训练时长。
10. **License and Citation**：开源协议、引用、第三方代码或数据集许可。

## 复现层级

- **Smoke Test**：几分钟内验证安装、数据路径、模型 forward、指标解析。
- **Minimal Reproduction**：小数据或少量 round 复现趋势。
- **Main Result Reproduction**：复现论文主表或主图。
- **Full Artifact**：包含消融、敏感性、效率、攻击评估和全部图表。

## 检查清单

- 运行入口不依赖本机绝对路径。
- 所有脚本可从项目根目录执行。
- 结果目录不会覆盖原始结果。
- 随机性来源已记录：Python、NumPy、PyTorch、CUDA、数据划分、client sampling。
- 数据不可公开时，提供 synthetic/sample data 或下载说明。
- 密码学或隐私计算实验记录安全参数、威胁模型、攻击者能力、信任假设。
- 联邦学习实验记录 client 数、采样率、local epochs、non-IID 划分、聚合规则。
- figure/table 能由脚本从保存的 metrics 重新生成。
- README 中的主结果和论文表格一致。
- artifact 中不包含 API key、个人路径、未授权数据或隐私敏感内容。

## 输出格式

~~~markdown
**Reproducibility Package Plan**
...

**Artifact Manifest**
| Item | Path | Status | Notes |

**Commands**
```bash
...
```

**Expected Outputs**
...

**Risks / Missing Items**
...
~~~

## 交接

- 缺少实验证据：交回 `experiment-iteration-controller`。
- 缺少运行命令或环境：交回 `run-experiment`。
- 缺少图表生成脚本：交给 `paper-figure`。
- 需要审查可复现性风险：交给 `review/evaluation-reproducibility-auditor`。
