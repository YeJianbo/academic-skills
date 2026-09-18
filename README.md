# Academic Codex Skills

本仓库整理本机正在使用的学术类 Codex skills，覆盖调研、写作、审稿、实验、论文图表和文献工具链。

当前版本同步于 2026-09-18，共 40 个技能入口。明确的任务直接进入专用技能；跨阶段或范围不清时使用分类入口。用户的任务、文件范围和既有授权优先于技能中的流程建议。

## 结构

- `skills/academic-hub`: 学术任务总入口。
- `skills/survey`: 文献检索、证据蒸馏、精读、选题闭环。
- `skills/writing`: 论文架构、逐节起草、相关工作、安全证明、润色和去 AI 味。
- `skills/review`: 投稿前审查、方法审查、实验复现审查、rebuttal 规划。
- `skills/experiment`: 实验规划、运行、迭代、结果分析、复现包和论文图表。
- `skills/tools`: 学术工作流依赖的工具类 skills。
- `skills/paper-evidence-distiller`: 单篇论文证据卡蒸馏。
- `skills/scipilot-writing-skill`: 指定期刊或跨学科风格的写作适配。
- `skills/scipilot-figure-skill`: 科研数据分析与图型选择。
- `skills/drawio-diagram-builder`: 可编辑 draw.io 技术图与论文示意图。
- `skills/nature-figure`: 投稿级科学图表流程。
- `skills/codex-paper-figure-skill`: 用户明确要求 AI 构图参考时生成并重建可编辑示意图。
- `skills/latex-posters`: LaTeX 科研海报。
- `skills/pdf`: PDF 提取、渲染和版面检查。
- `skills/agy`: 已授权的外部模型后台复查。
- `templates/`: 调研和批量证据蒸馏模板。

科研数据图默认使用 R，继续已有 Python 绘图代码时沿用 Python；Python 环境使用 conda。多代理和 AGY 按用户授权使用。旧的 `context-budget-manager` 已退出当前技能集，历史内容可在 Git 历史中查看。

## 安装

PowerShell:

```powershell
.\scripts\install.ps1
```

默认安装到 `$env:USERPROFILE\.codex\skills`。如果需要指定目录：

```powershell
.\scripts\install.ps1 -Destination "D:\codex-skills"
```

## 校验

安装脚本会替换目标目录内的同名技能目录；已有定制或目录链接时，先安装到独立目录，再比较合并。安装后技能在下一轮对话可用。根目录 `AGENTS.md` 记录当前维护规则，不由安装脚本覆盖到用户全局配置。

工具依赖按任务需要安装：R、conda/Python、LaTeX、PDF 渲染工具，以及对应的浏览器、图像生成或论文下载工具。`agy` 依赖本机已有的 AGY CLI 和 `$CODEX_HOME/tools/agy-background.ps1`；本仓库不分发账号、凭据或机器专用 helper。

安装后可使用 Codex 自带的 `quick_validate.py` 校验单个 skill：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\survey"
```
