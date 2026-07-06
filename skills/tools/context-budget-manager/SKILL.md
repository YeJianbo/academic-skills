---
name: context-budget-manager
description: "Codex 上下文预算与 token 节约技能。用于长任务、学术调研、论文写作/审稿、实验日志分析、代码库探索、多子代理协作、跨轮交接、用户提示很长或任务范围发散时；通过任务压缩、最小读取、搜索前计划、子代理窄化、输出压缩和 handoff brief 减少无效 token，同时保留必要证据与可复现信息。"
---

# Context Budget Manager

用于控制 Codex 长任务中的上下文消耗。它不替代 `survey`、`writing`、`review`、`experiment`、`tools` 等专业 skill，只约束“怎么读、怎么查、怎么委派、怎么交接”。

参考来源：`references/github-token-saver-notes.md`。该文件只记录外部项目思想，不要求照搬 Claude hooks。

## 触发时机

在以下场景优先使用：

- 用户提示很长、叙述重复、任务边界发散。
- 需要读大量文件、论文、日志、实验结果或 diff。
- 准备调研 40+ 篇论文、做 venue 搜索、批量下载/精读。
- 需要调用 AGY、Claude、DeepSeek 或多个子代理。
- 快到上下文上限，需要保留状态给下一轮。
- 需要 review、日志分析、结果总结，但原始材料很长。

## 总原则

1. 先压缩目标，再行动。
2. 先找入口，再读全文。
3. 先做最小检索计划，再扩大范围。
4. 子代理只拿窄任务、窄材料、窄输出格式。
5. 工具输出只总结关键事实；除非用户要求或精确文本必要，不整段粘贴。
6. 每轮结束保留可恢复 handoff，避免下一轮重读。
7. 省 token 不能牺牲正确性：必须联网核验、必须读原文、必须跑实验的任务不能省略，只能分批、摘要和落盘。

## 模式选择

| 场景 | 使用模式 | 产物 |
|---|---|---|
| 请求很长或目标不清 | `compact-task` | 目标、约束、完成条件、第一步 |
| 不知道读哪些文件 | `entry-finder` | 起始文件、理由、下一批读取 |
| 调研或搜索范围发散 | `minimal-research` | 假设、最小检查、停止条件 |
| 要开子代理 | `subagent-budget` | 子代理任务包和返回格式 |
| review/log/diff 很长 | `review-compress` | 最多 5 条 findings |
| 要跨轮继续 | `handoff-brief` | 状态、事实、剩余工作、风险 |

## Compact Task

在正式工作前，把用户请求压成 8 行以内：

```markdown
Goal:
Constraints:
Non-goals:
Inputs:
Success criteria:
First action:
Open questions:
```

规则：

- 保留用户的硬约束、路径、领域、模型、会议、时间范围。
- 删除客套、重复背景和不影响执行的叙述。
- 最多列 2 个开放问题；能合理假设时直接假设。

## Entry Finder

代码库或 skill 库探索时，不要上来全量读文件。默认顺序：

1. 用 `rg --files` 列候选路径。
2. 用 `rg -n "<关键词>" <小范围路径>` 找入口。
3. 首批最多读 3 个文件。
4. 读完先判断是否足够行动，再决定下一批。

输出：

```markdown
Best starting files:
Why:
Next reads:
Stop condition:
```

禁止模式：

- 未限定路径的大范围 `Get-ChildItem -Recurse` 后直接读大量文件。
- 把整份日志、整篇论文、整批 PDF 文本塞进上下文。
- 已有结构化 summary 时重复读取原始大材料。

## Minimal Research

搜索、调研、venue 查找或论文选题前，先写最小调查计划：

```markdown
Hypothesis:
Minimal checks:
Stop condition:
Escalation trigger:
```

规则：

- 最多 3 个首批检查。
- 每个检查必须有来源类型：官方 CFP、accepted/program、OpenAlex/arXiv、PDF 原文、实验日志、代码路径。
- 明确什么时候停止扩大搜索。
- 对用户指定的 exhaustive 任务，分批执行并落盘 evidence matrix，不把全部结果留在聊天上下文。

## Subagent Budget

调用子代理前，先判断它是否真的节省主线程 token 或带来外部视角。满足以下任一条件再开：

- 子代理能只读本地目录或文件，避免主线程先读大材料。
- 子任务可并行，且输出能压缩为 5-10 条证据。
- 需要 AGY/Claude 做反方审查、长上下文粗读、会议适配度讨论。
- 低成本 worker 可做机械整理、表格抽取、第一轮清理。

子代理任务包必须包含：

```markdown
Task:
Inputs:
Do not:
Output format:
Budget:
Return status:
```

返回格式默认：

```markdown
Status: done | incomplete | blocked
Confirmed issues:
Plausible risks:
Missing evidence:
Next action:
```

规则：

- 不让多个子代理重复读同一材料，除非明确做交叉审查。
- 子代理输出过长时，要求它重交压缩版，不由主线程脑补。
- 主线程负责最终判断，不把子代理意见当最终事实。

## Review Compress

压缩 review、CI、实验日志、diff 或审稿意见时：

- findings first，按严重性排序。
- 最多 5 条。
- 每条包含影响和证据位置。
- 没有问题时明确写“未发现 blocker”，再列 residual risk。

格式：

```markdown
Critical:
Major:
Minor:
Residual risk:
Next action:
```

## Handoff Brief

长任务每完成一个阶段，或即将跨轮继续时，生成 120-180 中文字的 handoff。必要时保存到项目内的 `notes/`, `docs/`, `literature/` 或任务指定目录。

格式：

```markdown
Status:
Key facts:
Files changed/read:
Remaining work:
Risks:
Next command:
```

只写会影响下一步的信息，不复述过程。

## 学术工作流适配

- `survey`: 大规模文献检索必须把 `papers.csv`、BibTeX、PDF 路径、paper notes 和 evidence matrix 落盘；聊天中只保留检索式、批次状态和结构性空白候选。
- `writing`: 先用 `paper-architecture-planner` 规划，再逐节调用 `section-drafter`；不要一次把整篇论文和全部参考资料塞入上下文。
- `review`: 长审稿意见压成 `Critical/Major/Minor/What would change my mind`；需要引用核验时只读相关段落和 bibliography。
- `experiment`: 日志先转 CSV/JSON summary，再读关键异常、指标表和配置；大日志不整段贴。
- `venue-profile-router`: 直接联网查找仍必须执行；省 token 的方式是记录 search trace、只打开官方命中页、把候选 venue 分批核验。

## 输出习惯

- 简单任务：直接执行，不额外输出预算说明。
- 长任务：先给 3-6 行执行 brief。
- 最终回复：只说改了什么、验证了什么、还剩什么风险。
