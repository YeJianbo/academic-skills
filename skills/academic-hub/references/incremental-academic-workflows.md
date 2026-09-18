# 增量学术工作流

用于跨阶段协调、版本比较和生成文件整理；明确的单项任务直接使用负责该任务的技能。不是每个学术请求都要加载的前置文档。

## 范围与持续执行

- 探索：给可检验的问题、相近工作风险和下一项证据；未达到投稿成熟度不等于方向没有潜力。
- 局部修改：复用已有论证、数据、格式和有效检查，只处理受影响部分。
- 完整交付：按用户要求完成正文、实验或审查及其必要验证。内部可分阶段，不在第一稿或技能交接处默认停下来等待。
- 用户的新消息通常修订当前任务；保留未撤回要求及有效成果。遇到一个待决定的科学问题时，继续其他已授权工作。

## 一项产物，一个当前来源

优先使用项目已有路径。没有约定时才按需建立 `work/<task>/`，只创建当前需要的 source、assets、cache 或 build 子目录，不先铺整套目录树。

- 当前稿件、图源、汇总表和报告在规范路径持续更新；内容未变不重复写入或导出。
- 原始论文、实验 run、原始日志、用户要求的版本比较和必要复现历史保留，不能被最新汇总覆盖。
- 替换当前文件时按文件类型采用可靠写入方式；需要原子替换时，临时文件与目标放在同一目录。避免同时写同一产物。
- 合并重复的规格、构图提示和 QA 记录；局部修改不新增一套 dated/final-vN 台账。
- 检索缓存保留来源和读取状态，仅对新证据、冲突或时效性变化补查，不用固定文献数量制造重复检索。

## 各阶段的交接

| 工作 | 当前负责技能 | 交接要点 |
|---|---|---|
| 研究问题与证据缺口 | cs-idea-discovery-pipeline | 当前主张、反例、来源、待验证项 |
| 文献与全文 | cs-literature-search / paper-reading-synthesizer | 已读范围、原文位置、缺失来源 |
| 正文起草与修改 | section-drafter / section-writing-polish | 最终请求范围、源格式、有效证据 |
| 去防御性表达 | academic-paper-de-vibe | 科学信息、必要限定、实际修改 |
| 实验执行与分析 | run-experiment / experiment-results-analyzer | 配置、run 证据、实际结果与限制 |
| 数值图与可编辑图 | nature-figure / drawio-diagram-builder | 可编辑源、数据或拓扑、受影响导出 |
| 审稿与修订对比 | cs-paper-reviewer / rebuttal-revision-planner | 原文证据、相对进步、当前成熟度分别报告 |

交接传递位置、变更要求和未决问题，不复制整份报告，也不意味着必须启动另一个 agent。代理和外部模型沿用用户授权与当前主机规则。

## 适配依据

吸收 [CCFA Skills v0.10.0](https://github.com/mikubaka88/CCFA-Skills/releases/tag/v0.10.0) 的 task-modes、artifact-contracts、humanization-policy 和 visual-composer 工作流思想，分别整合到现有技能，不安装第二套 17 个入口。

保留本地选择：R 默认、已有 Python 工作流、直接可编辑图源、科学证据边界、模板字号行距规则和用户指定目录。上游的默认图像生成、Python 配方、`ccfa.yaml` 或固定检索数量不是本地任务的额外前置条件。

上游作者：Chaoyue Li / mikubaka88，MIT 许可；见 [上游许可](ccfa-v010-license.txt)。来源笔记：[CCFA-Skills适配GPT6啦](https://www.xiaohongshu.com/explore/6a9c3ef70000000026030c3f)。本文为针对本地既有技能的适配规则，不表示上游 CI 已验证这些本地改动。
