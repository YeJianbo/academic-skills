---
name: survey
description: "协调研究方向、跨论文调研与选题工作。明确的文献检索、指定论文下载、证据卡或相关工作写作直接交给对应技能。"
---

# Survey

从当前研究问题和已有材料出发；投稿 venue 只在用户指定时限制检索范围。按所需交付选择一条路径，不默认先检索再蒸馏再精读全部论文。

| 交付 | 负责技能 |
|---|---|
| 找外部论文、相近工作和引用候选 | `cs-literature-search` |
| 下载指定论文或批量全文 | `scansci-pdf`；缺少其工具时用可用 OA/官方直链 |
| 将给定论文转成可回链证据卡 | `paper-evidence-distiller` |
| 多篇精读、假设与失败模式对照、证据矩阵 | `paper-reading-synthesizer` |
| 探索或评估研究方向、构造最小验证 | `cs-idea-discovery-pipeline` |
| 整理任务、数据集、baseline 与公平比较边界 | `benchmark-baseline-registry` |
| 依据已读文献写 Related Work | `related-work-synthesizer` |

已有文献和记录直接复用；只为实际缺口、来源冲突或时效变化补查。初步探索不自动升级为投稿判决，下载和关键词筛选不冒充全文阅读。跨阶段文件交接才按需查 `../academic-hub/references/incremental-academic-workflows.md`。

旧 `lit-review/`、`lit-review-assistant/`、`novelty-check/` 和 `index.md` 保留为按需参考，不是额外自动入口。
