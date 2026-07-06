---
name: survey
description: "计算机科学调研入口：面向可替换文章主题，按主题宽检索有声誉的相关顶会/顶刊和强相邻领域，执行文献检索、下载前筛选、单篇论文证据蒸馏、论文精读、证据矩阵、综述、选题、相关工作和创新性判断；投稿目标会议/期刊是可选适配信息，不默认限制检索范围；路由到 cs-literature-search、paper-evidence-distiller、paper-reading-synthesizer、cs-idea-discovery-pipeline 和 benchmark-baseline-registry，用于发现结构性空白、提出可验证假设并通过本机小实验验证可行性。"
---

# Survey

用于学术调研阶段，默认服务计算机科学论文选题与相关工作构建。

## 覆盖内容

- 论文检索与筛选
- 单篇论文证据卡蒸馏
- PDF 下载后的精读与证据矩阵
- 文献综述与脉络梳理
- 研究空白与创新点识别
- 选题收敛与问题定义
- 相关工作组织
- 计算机科学论文选题闭环：文献池 -> 结构性空白 -> 失败机理 -> 新假设 -> subagent 审查 -> 本机 pilot 实验 -> 论文大纲

## 路由建议

- 开始一个新方向：先用这里
- 文献检索、论文下载前筛选、无 API key 搜索：使用 `cs-literature-search`
- 单篇 PDF 或 Markdown 需要压成“最小但完整”的可回链证据卡，后面还要反复用于 related work、rebuttal、benchmark 比较或 gap 论证：先用 `paper-evidence-distiller`
- 下载后精读、结构化 paper notes、claim-evidence matrix：使用 `paper-reading-synthesizer`
- 计算机科学论文选题闭环：使用 `cs-idea-discovery-pipeline`。主题和实际检索范围必须从用户输入或任务上下文锁定；投稿目标会议/期刊是可选项，用于 idea 适配，不默认限制文献检索范围。联邦学习/隐私保护/密码学/隐私计算只是默认示例方向，不是固定范围。
- 需要确定数据集、baseline、攻击和指标：使用 `benchmark-baseline-registry`
- 只下载论文、批量下载、已有 DOI/arXiv/title 列表：能通过 Codex 网络检索找到官方/OA/arXiv PDF 就直接下载；批量、失败项、WebVPN 或 DOI/title 解析再转 `tools/scansci-pdf`，不要强行走 OpenAlex 检索。
- 需要正式相关工作写作：转到 `writing`
- 需要审稿人视角攻击 idea：转到 `review`
- 需要实验验证：转到 `experiment`

## 关键子技能

- `cs-literature-search`: DBLP/proceedings 优先的 CS 文献检索和标题/摘要筛选；按主题宽检索有声誉的相关顶会/顶刊和强相邻领域，OpenAlex 只作显式补充源，下载交给 `scansci-pdf`。
- `paper-evidence-distiller`: 把单篇 PDF/Markdown 压成带原文锚点的 `.distilled.md` 证据卡；适合在全文精读前先保留样本、时间范围、主张、系数、图表位置和限制，供后续综合与写作复用。
- `paper-reading-synthesizer`: 精读 PDF/论文笔记，生成 evidence matrix、failure modes、local pilot 线索和 idea 关系。
- `cs-idea-discovery-pipeline`: 从近三年顶会/顶刊文献出发，发现结构性空白，推导新假设，经过 subagent 审查和本机小实验验证后输出可实现 idea 与论文大纲。
- `benchmark-baseline-registry`: 为 CS 论文整理 benchmark、baseline、攻击、指标和公平比较约束。

## 默认顺序

1. `cs-literature-search`：检索、标题/摘要筛选、下载队列。
2. `paper-evidence-distiller`：对核心 PDF 或已有 Markdown 生成单篇证据卡；这一步优先服务可回链、可 grep、可后续复用。
3. `paper-reading-synthesizer`：对核心论文做全文精读，把证据卡和原文阅读结果汇入 evidence matrix。
4. `related-work-synthesizer`、`cs-idea-discovery-pipeline`、`benchmark-baseline-registry`：分别处理写作综合、选题闭环和评测要素。

默认不要在“下载完成”后立刻对所有论文做长篇精读。先用 `paper-evidence-distiller` 保留单篇证据骨架，再决定哪些论文值得进入全文精读和证据矩阵。

## 保留资料

- `lit-review/`: 旧文献综述资料，按需参考。
- `lit-review-assistant/`: 旧文献阅读/综述辅助资料，按需参考。
- `novelty-check/`: 旧创新性检查资料，按需参考。
- `index.md`: 旧索引，保留不删。
