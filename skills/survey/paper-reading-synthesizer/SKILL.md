---
name: paper-reading-synthesizer
description: 精读并对照多篇论文的假设、方法、证据和失败条件，形成研究笔记与证据矩阵。单篇证据卡、外部检索和正文写作分别交给对应技能。
---

# Paper Reading Synthesizer

用于把“下载了论文”变成“读过并能支撑判断的证据矩阵”。它不负责检索和下载；检索和标题/摘要筛选交给 `cs-literature-search`，下载交给 `scansci-pdf`，本地库管理交给 `literature-library-manager`。若已有 `paper-evidence-distiller` 生成的 `.distilled.md`，优先把它当作单篇证据骨架和回链索引，再补全文阅读。注意：筛选矩阵不是证据矩阵，只有读过 PDF 并记录位置证据的论文才能进入 evidence matrix。

## 输入

- PDF 文件夹、BibTeX、论文列表 CSV/Markdown，或 Zotero 导出的条目。
- 可选：与 PDF/Markdown 同名的 `.distilled.md` 证据卡。
- 当前研究问题、实际检索范围、筛选标准和可选投稿目标 venue。
- 需要回答的问题：结构性空白、现有方法失效原因、baseline、主题相关 assumption/model、实验或验证可复现性。

## 阅读流程

1. **Queue Check**：只读取已经通过摘要筛选并下载到本地的 core/adjacent PDF；`metadata-only` 和 `needs_abstract` 不能进入全文精读。
2. **Screening Role Check**：`core`、`adjacent`、`background` 在下载前只表示阅读优先级，不表示已经形成证据。
3. **Distilled Card Check**：若存在 `.distilled.md`，先读证据卡，获取样本、时间范围、主张、图表/表格锚点、限制和复核记录；把它当作全文阅读导航，而不是全文替代。
4. **Count Boundary Check**：`downloaded` 不等于 `fulltext_read`；只有已读全文并写入 evidence matrix 的论文才能计入 gap 证据。
5. **Focused Reading**：核心论文至少读 abstract、introduction、method、assumption/model、proof/security model 或 evaluation、experiments、limitations。
6. **Evidence Extraction**：每条主张都绑定来源位置，如 page/section/figure/table/equation。若证据卡已有锚点，复用并在必要时回原文核对。
7. **Failure Reading**：主动找失败条件、隐藏假设、未覆盖 threat model、实验缺口和作者承认的 limitation。
8. **Relation Mapping**：判断该论文支持、反驳、补充还是竞争当前 idea。
9. **Matrix Update**：把阅读结果写入统一 evidence matrix，供 `cs-idea-discovery-pipeline` 和 `related-work-synthesizer` 使用，并同步更新 `metadata/evidence_counts.md`。

## 两种矩阵

必须区分：

| Matrix | 来源 | 允许字段 | 禁止用途 |
|---|---|---|---|
| `screening_matrix` | title、abstract、venue、year、关键词、下载状态 | screening_stage、screening_role、download_status、why_relevant | 不能支撑 gap、failure mechanism、idea novelty。 |
| `evidence_matrix` | 已读 PDF 正文、图表、定理、实验、limitations | claim、evidence_location、evidence_type、failure_mode、gap_signal | 不能包含未读全文或无证据位置的论文。 |

如果只有标题、摘要或脚本分类，输出必须叫 `screening_matrix` 或 `reading_queue`，不得叫 `evidence_matrix`、`core paper matrix` 或 `gap summary`。

## 单篇 Paper Note 模板

```markdown
**Citation Key**
...

**Problem / Setting**
...

**Core Method**
...

**Assumption / Model**
...

**Main Claims**
| Claim | Evidence Location | Evidence Type | Strength |

**Baselines / Metrics / Datasets**
...

**Failure Modes / Hidden Assumptions**
...

**Local Implementability**
...

**Relation to Our Idea**
support / contradict / compete / background / adjacent

**Follow-up Questions**
...
```

## Evidence Matrix 字段

| Field | Meaning |
|---|---|
| `paper_id` | DOI、arXiv ID 或本地 citation key。 |
| `screening_role` | 检索/摘要阶段的阅读优先级：core-candidate、adjacent-candidate、background-candidate、reject。 |
| `evidence_role` | 读完全文后的证据角色：core-evidence、adjacent-evidence、background-evidence、contradictory-evidence。 |
| `read_status` | fulltext_read、partial_read、metadata_only。 |
| `problem` | 解决的问题。 |
| `setting` | 任务、数据、系统、用户、模型、威胁或部署场景。 |
| `assumption_model` | threat model、data model、system model、user model、learning setup 或理论假设。 |
| `method` | 方法、算法、协议、系统设计、模型架构或实验范式。 |
| `claim` | 核心主张。 |
| `evidence_location` | page/section/table/figure/equation。 |
| `evidence_type` | theorem、experiment、attack eval、complexity、ablation、user study、benchmark、artifact。 |
| `failure_mode` | 方法失效条件。 |
| `gap_signal` | 是否暴露结构性空白。 |
| `local_pilot` | 本机可做的小实验或 microbenchmark。 |

## 质量规则

- 不声称“读过”未进入 evidence matrix 的论文。
- 不把 `downloaded`、`auto_abstract_candidate`、`human_abstract_yes` 计为全文阅读证据。
- 不把 `.distilled.md` 证据卡本身计为 `fulltext_read`；证据卡只能加速导航和后续综合。
- 不把 abstract 复述当作精读结论。
- 每个重要判断必须有位置或出处。
- 对无 PDF 的论文，标记为 metadata-only，不能用于强结论。
- 自动脚本只能生成 screening matrix 或 reading queue，不能生成 gap summary 或 evidence matrix。
- 关键词误匹配必须进入人工复核；例如 `TEE` 不能只因普通单词里的 `tee` 命中就归类为 TEE 论文。
- 对当前 idea 不利的论文必须保留，不能只保留支持材料。
- 读 40+ 篇时优先产出矩阵和 gap map，不写长篇泛综述。

## GitHub 参考

需要理解设计来源时读取 `references/github-reading-workflow-notes.md`。参考项目已下载到 `C:\Users\YeJianbo\.skills-manager\external-references\github-lit-review`，只作本地资料，不自动加载。

## 交接

- 文献检索：`cs-literature-search`。
- 单篇证据卡：`paper-evidence-distiller`。
- PDF/BibTeX/Zotero 管理：`literature-library-manager`。
- 选题空白闭环：`cs-idea-discovery-pipeline`。
- Related Work 写作：`writing/related-work-synthesizer`。
- 引用真实性审查：`review/submission-readiness-checker` 或后续 citation checker。
