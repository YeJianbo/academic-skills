---
name: literature-library-manager
description: "计算机科学文献库管理技能。用于管理调研过程中的 PDF、BibTeX、Zotero、Markdown notes、papers.csv、download/read/summarized 状态、去重、重命名、目录分类、citation key、失败下载清单和 evidence matrix 交接；适合 40+ 篇联邦学习、隐私保护、密码学、隐私计算论文批量调研和长期研究记忆维护。"
---

# Literature Library Manager

用于把文献资料组织成可追踪的本地库。它不负责判断 idea 是否成立；它负责让 PDF、BibTeX、notes、状态表和引用键不乱。

## 推荐目录结构

```text
literature/
  papers.csv
  bib/
    library.bib
  pdf/
    core/
    adjacent/
    background/
  notes/
    paper-notes/
    matrices/
  logs/
    search-log.md
    download-failures.csv
    read-status.csv
```

## papers.csv 字段

| Field | Meaning |
|---|---|
| `paper_id` | DOI、arXiv ID、Semantic Scholar ID 或 citation key。 |
| `title` | 标题。 |
| `year` | 年份。 |
| `venue` | 会议/期刊/预印本。 |
| `doi` | DOI。 |
| `arxiv_id` | arXiv ID。 |
| `pdf_path` | 本地 PDF 路径。 |
| `bib_key` | BibTeX key。 |
| `topic` | 主题标签。 |
| `screening_role` | 检索/摘要阶段的阅读优先级：core-candidate、adjacent-candidate、background-candidate、reject。 |
| `evidence_role` | 全文阅读后的证据角色：core-evidence、adjacent-evidence、background-evidence、contradictory-evidence；未读全文必须为空。 |
| `screening_stage` | metadata_found、title_yes、title_maybe、title_no、needs_abstract、auto_abstract_candidate、auto_abstract_maybe、auto_abstract_no、human_abstract_yes、human_abstract_maybe、human_abstract_no、download_queued、downloaded、fulltext_read。 |
| `title_decision_reason` | 标题筛选理由或命中关键词。 |
| `abstract_decision_reason` | 摘要筛选理由或命中关键词。 |
| `download_status` | pending、downloaded、failed、oa-only、manual-needed。 |
| `read_status` | unread、skimmed、read、summarized、matrix-done。 |
| `notes_path` | 本地笔记路径。 |
| `failure_reason` | 下载或解析失败原因。 |

## 工作流

1. **Import**：从 `cs-literature-search` 的摘要筛选结果、BibTeX、DOI 列表或 Zotero 导出导入条目；不要把未过标题筛选的 raw 记录导入核心库。
2. **Normalize**：统一 title、DOI、arXiv ID、venue、year、citation key。
3. **Deduplicate**：按 DOI -> arXiv ID -> normalized title 去重。
4. **Download Tracking**：只把 `human_abstract_yes` 或人工确认的 `human_abstract_maybe` 交给 `scansci-pdf`，记录成功/失败和本地路径。`auto_abstract_candidate` 不得直接下载。
5. **Classify**：按 topic、venue、role、year 分类到目录。
6. **Evidence Role Lock**：只有 `paper-reading-synthesizer` 读完全文并写出证据位置后，才能填写 `evidence_role`。
7. **Note Link**：为每篇论文建立 Markdown note 路径，交给 `paper-reading-synthesizer` 填写。
8. **Status Update**：调研推进时更新 `read_status` 和 `download_status`。

## Zotero 协作

- Zotero 可作为主库；本 skill 维护导出的 BibTeX、PDF 路径和 Markdown notes。
- 可参考 llm-for-zotero 和 zotero-better-notes 的思路：Zotero 负责 PDF/annotation，本地 Markdown 负责可版本化笔记。
- 不强制要求安装 Zotero 插件；没有 Zotero 时使用本地目录和 CSV。

## 输出格式

```markdown
**Library Status**
| Total | Downloaded | Failed | Read | Matrix Done |

**Duplicates**
...

**Download Failures**
| Paper | DOI/arXiv | Reason | Next Action |

**Next Reading Queue**
| Priority | Paper | Role | Why |
```

## GitHub 参考

详细来源见 `references/github-library-workflow-notes.md`。

## 交接

- 检索：`survey/cs-literature-search`。
- 机构授权：`institutional-access-resolver`。
- 下载：`scansci-pdf`。
- 精读：`paper-reading-synthesizer`。
- 写 Related Work：`related-work-synthesizer`。
