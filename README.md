# Academic Codex Skills

本仓库整理本机正在使用的学术类 Codex skills，覆盖调研、写作、审稿、实验、论文图表和文献工具链。

## 结构

- `skills/academic-hub`: 学术任务总入口。
- `skills/survey`: 文献检索、证据蒸馏、精读、选题闭环。
- `skills/writing`: 论文架构、逐节起草、相关工作、安全证明、润色和去 AI 味。
- `skills/review`: 投稿前审查、方法审查、实验复现审查、rebuttal 规划。
- `skills/experiment`: 实验规划、运行、迭代、结果分析、复现包和论文图表。
- `skills/tools`: 学术工作流依赖的工具类 skills。
- `skills/paper-evidence-distiller`: 单篇论文证据卡蒸馏。
- `skills/scipilot-writing-skill`: SciPilot 写作与润色 skill。
- `skills/scipilot-figure-skill`: SciPilot 科研数据可视化 skill。
- `skills/drawio-diagram-builder`: 可编辑 draw.io 技术图与论文示意图。
- `skills/nature-figure`: 投稿级科学图表流程。
- `templates/`: 调研和批量证据蒸馏模板。

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

安装后可使用 Codex 自带的 `quick_validate.py` 校验单个 skill：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\survey"
```

