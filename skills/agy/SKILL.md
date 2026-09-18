---
name: agy
description: "使用本机 AGY 后台 CLI 调用 Gemini、Claude 等可用模型。用于用户要求 AGY/Gemini 咨询或已授权的外部模型复查；不是普通写作、调试或审稿的自动前置步骤。"
---

# AGY 后台协作

AGY 是外部模型通道，不是 Codex 的 Sol/Terra/Luna 子代理。先确定本次已授权的任务、文件范围和模型；用户指定模型时保留该选择，不静默换模型或供应商。

## 调用

只使用现有后台 helper。在 PowerShell 中按本机 Codex 目录调用：

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
powershell -NoProfile -ExecutionPolicy Bypass -File "$codexRoot\tools\agy-background.ps1" -Prompt '审查指定文件中的具体问题；给出文件和行号依据，不修改文件。' -WorkspacePath 'D:\path\to\project' -OutputPath 'D:\path\to\project\work\agy-review.txt' -Model 'gemini-3.1-pro-high'
```

`-Prompt` 必填；`-WorkspacePath` 默认当前目录；`-OutputPath` 可指定既有任务工作目录。省略输出路径时 helper 使用项目 `.codex/agy-runs/`。`-TimeoutMinutes` 默认 15；现有 PTY 包装器默认上限也是 15 分钟，不承诺仅增大该参数就能突破包装器上限。

`-Model` 可选，传给 AGY 的 `--model`。省略时由 AGY 选择默认模型，不能声称它就是 Gemini 或某个固定版本。模型 ID 与选择建议见 [模型与职责](references/models.md)。需要确认新模型、名单变化或遇到不可用错误时运行 `agy models`；不为每次调用重复查询。

## 任务与结果

- 提示说明实际目标、文件位置、允许的修改范围和完成条件。文件已可直接读取时不先复制大量内容；审查默认只读，外部传输与写入遵守现有授权和权限规则。
- 要求回答不表扬、不奉承，区分 `confirmed issue`、`plausible risk`、`missing evidence`，并给出文件、章节、行号、实验或命令依据。
- helper 返回 PID、模型请求值、stdout 和 stderr 路径。保存这些信息，继续当前线程中不依赖它的工作，不在前台等完整咨询。
- 读取实际输出后才引用结论。进程结束不等于任务成功；检查 stderr、结果完整性和证据。超时或失败如实保留，不重复提交同一咨询、不补写缺失结论。
- 模型意见作为复查或候选，不替代原文、代码执行、实验或证明。只把已验证结果并入最终交付。

当模型不可用时说明实际错误，按用户已有偏好处理替代选择；不自动降级或切换付费通道。
