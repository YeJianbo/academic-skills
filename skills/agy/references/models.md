# 模型与职责

2026-09-07 使用本机 `agy models` 核验以下 ID。可用名单随账号和 AGY 更新变化；下述职责是本地选用建议，不是性能评测结论，也不保证每次调用成功。

## AGY 模型

| 模型 | 精确 ID | 建议用途 |
|---|---|---|
| Gemini 3.8 Flash | `gemini-3.8-flash-high` / `gemini-3.8-flash-medium` / `gemini-3.8-flash-low` | 快速粗读、提取、候选生成；按问题难度选档 |
| Gemini 3.7 Flash | `gemini-3.7-flash-high` / `gemini-3.7-flash-medium` / `gemini-3.7-flash-low` | 用户指定旧版本、复现既有流程或比较版本 |
| Gemini 3.6 Flash | `gemini-3.6-flash-high` / `gemini-3.6-flash-medium` / `gemini-3.6-flash-low` | 用户指定旧版本或既有流程兼容 |
| Gemini 3.1 Pro | `gemini-3.1-pro-high` / `gemini-3.1-pro-low` | 较深入的长材料分析、实验设计候选与反方审查 |
| Claude Sonnet 4.6 Thinking | `claude-sonnet-4-6` | 已授权的 Claude 实现建议、代码复查与文稿分析 |
| Claude Opus 4.6 Thinking | `claude-opus-4-6-thinking` | 已授权的复杂 Claude 论证或架构复查 |
| GPT-OSS 120B Medium | `gpt-oss-120b-medium` | 用户指定该模型的补充视角或比较 |

用户只说 Gemini：简单提取或粗读可选 `gemini-3.8-flash-medium`，深入审查可选 `gemini-3.1-pro-high`，调用时说明选择。只说 AGY 且目标明确时同样可按任务选择 Gemini；不能因此把 Claude 调用视为自动获准。精确模型、供应商或成本边界有明确要求时按原要求执行。

`agy --help` 还提供 `--effort low|medium|high`，但当前后台 helper 不单独暴露该参数。不要给不支持的 helper 参数；Gemini 名单中的档位使用完整模型 ID 选择。

## Codex 原生模型：不是 AGY ID

| 模型 | 当前配置 | 职责 |
|---|---|---|
| Astra | 主线程 `gpt-6-astra` | 端到端协调、复杂判断和最终交付 |
| Sol | `sol` → `gpt-5.6-sol`，high | 复杂实现、设计分析、反方复查 |
| Terra | `terra` → `gpt-5.6-terra`，high | 实现检查、兼容性、调试与验证 |
| Luna Max | `lunamax` → `gpt-5.6-luna`，max | 按明确计划执行独立、边界清楚的工作 |

这些角色只在委派获授权且任务适合时调用。主模型升级不意味着自动替换既有子代理；本次没有改动各角色模型和推理等级。
