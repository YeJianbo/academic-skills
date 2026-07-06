---
name: cs-literature-search
description: "计算机科学文献检索与阶段门控筛选技能。用于任意 CS 主题的宽范围候选标题返回、标题级筛选、摘要级筛选、入库、下载队列和全文阅读交接；默认按主题检索有声誉的相关顶会/顶刊、强相邻领域和高质量预印本，投稿目标会议/期刊是可选适配信息且不默认限制检索范围；默认不强制 OpenAlex，优先使用 Codex 网络检索、DBLP、Crossref、arXiv、Semantic Scholar、会议 proceedings 和用户给定 DOI/arXiv/title 列表，OpenAlex 只作为显式可选补充源；能从官方/OA/arXiv/作者主页直接下载 PDF 时直接下载，批量和困难下载交给 scansci-pdf。"
---

# CS Literature Search

用于先找到论文，再把下载和阅读交给后续流程。默认不依赖商业数据库 API key。核心原则：先返回候选标题，标题筛选后才补摘要，摘要通过后才入库和下载全文。文献检索以主题为主，默认宽覆盖有声誉的相关顶会/顶刊和强相邻领域；目标投稿会议只用于后续 venue fit，不是默认检索范围。若网络检索已经找到官方 PDF、arXiv PDF、会议 proceedings PDF 或作者主页 PDF，可直接下载，不必绕到 OpenAlex。

## 默认策略

1. **Web/OA first when obvious**：Codex 网络检索能找到官方 PDF、arXiv PDF、会议 proceedings PDF、作者主页 PDF 时，直接下载并记录 URL/source。
2. **Download is separate**：用户要“下载论文/批量下载/给 DOI 或 arXiv”时，优先直接下载或转 `tools/scansci-pdf`，不要强行先跑 OpenAlex 或本 skill。
3. **Fast seed first**：需要主题检索时默认先用 Codex 网络检索/DBLP 生成快速标题种子池；命中不足时再查 Crossref；arXiv、Semantic Scholar、会议 proceedings 或网页只在需要补漏时使用。
4. **No forced OpenAlex**：OpenAlex 只在用户明确要求、其他源召回不足、或需要 cited_by/abstract_inverted_index 等元数据时显式使用。
5. **Topic first**：默认按文章主题检索，不要求用户先给投稿会议。
6. **Submission venue is not search scope**：用户给出的目标会议/期刊是投稿定位约束，不默认限制检索范围；只有用户明确说“只查某会议/期刊”时才收窄。
7. **Reputable venue broad search**：按主题覆盖有声誉的 CS 顶会/顶刊、强相邻领域和高质量预印本；用会议名、年份、关键词、DBLP/proceedings、arXiv title match 组合补漏。
8. **Institutional access for download**：学校账户只用于全文访问和下载；调研前授权交给 `tools/institutional-access-resolver`，批量/困难下载交给 `tools/scansci-pdf`。
9. **Key-only optional**：IEEE Xplore、Lens、Scopus、Web of Science 只在用户已配置 key 或学校平台可网页访问时作为增强源。
10. **Deduplicate before download**：下载前按 DOI、arXiv ID、title normalized key 去重。
11. **Rate-limit fallback**：Semantic Scholar、OpenAlex、Crossref、arXiv 等元数据 API 被限流、429、当天额度用尽或连续超时时，不要反复重试；在 search log 写明不可用原因，立即转官方 proceedings、OpenReview、USENIX/ACM/IEEE/IACR/PoPETs 页面、DBLP、arXiv API、作者主页和普通网页搜索。

## 下载优先级

摘要通过或用户明确要求下载时，按以下顺序尝试：

1. **Direct PDF from web**：Codex 网络检索到官方 PDF、arXiv PDF、OpenReview PDF、USENIX/ACM/IACR/IEEE proceedings PDF、作者主页 PDF，直接下载并记录来源。
2. **arXiv ID / DOI direct**：已有 arXiv ID 或 DOI，单篇可直接打开/下载；批量交给 `scansci-pdf`。
3. **scansci-pdf**：需要批量、断点续传、多源并行、BibTeX 导入、标题解析、WebVPN、机构权限或下载失败重试时使用。
4. **Institutional access**：付费出版社全文且学校可能订阅时，先走 `institutional-access-resolver` 授权，再用 `scansci-pdf` 或浏览器登录态下载。
5. **Manual-needed**：只有标题、无 DOI/arXiv、无稳定 PDF 链接时，标记为 `manual-needed`，不阻塞已下载核心池阅读。

记录字段至少包含：`pdf_url`、`pdf_source`、`download_method`、`download_status`、`failure_reason`。

## 速度优先模式

默认不要一开始并行铺开所有数据库。先跑快速种子检索：

```powershell
python scripts/cs_lit_search.py --query "<topic keywords> <target method/problem>" --year-from 2024 --limit 30 --sources quick --min-results 10 --cache-dir .lit-cache
```

规则：

- `quick`：先查 DBLP；去重后达到 `--min-results` 就停止；不足时查 Crossref，不默认等待 arXiv，不默认使用 OpenAlex。
- `all`：需要更高召回率时查 DBLP + Crossref + arXiv；OpenAlex 不包含在默认 all 中。
- `openalex`：显式补充源；只在用户要求或其他源不足时使用。
- `dblp`：CS title/venue 种子默认源，适合 proceedings 补漏。
- `crossref`：DOI 元数据 fallback。
- `arxiv`：只找预印本、最新版本或标题核验时使用。
- repeated query 必须加 `--cache-dir`，避免同一检索式反复打远端接口。
- OpenAlex、Semantic Scholar 或 Crossref 频繁返回 429/限流/额度耗尽时，不要反复重试；改用 DBLP/proceedings/arXiv/官方网页/作者主页。显式需要 OpenAlex 时可加 `--mailto <学校邮箱>`。
- 只有快速种子池不足、主题关键 venue 缺失、或 citation chaining 需要补漏时，才扩展到更多源；不要因为已有投稿目标 venue 就跳过其他相关 venue。

## 阶段门控流程

严格按以下顺序执行，不要从 raw metadata 直接下载全文：

1. **Topic contract**：确定主题、关键词、年份、实际检索范围、排除范围和停止条件；投稿目标 venue 可选。
2. **Metadata/title retrieval**：只取 title、year、venue、DOI/arXiv、URL、source；不下载 PDF，不逐条打开 publisher 页面。
3. **Title screening**：按标题、venue、year、关键词分成 `title_yes`、`title_maybe`、`title_no`。
4. **Abstract enrichment**：只对 `title_yes` 和高分 `title_maybe` 补摘要；不要给全部 raw 记录补摘要。
5. **Abstract screening**：脚本只能产出 `auto_abstract_candidate` 或 `auto_abstract_maybe`；主线程/人工读过摘要后才能改成 `human_abstract_yes`、`human_abstract_maybe` 或 `human_abstract_no`。
6. **Library import**：只把 `human_abstract_yes` 和少量高价值 `human_abstract_maybe` 写入文献库，状态为 `download_queued` 或 `metadata_only`。
7. **PDF download**：先尝试网络直链/OA PDF；批量、WebVPN、失败重试再交给 `scansci-pdf`。下载失败记录原因，不阻塞阅读已有核心池。
8. **Full reading**：只对 core PDF 做全文精读和 evidence matrix。

阶段状态必须写入 CSV/JSON，避免下一轮重复筛选：

| Status | Meaning |
|---|---|
| `metadata_found` | 已找到元数据，未筛标题。 |
| `title_yes` | 标题明确相关，进入摘要队列。 |
| `title_maybe` | 标题可能相关，按分数或 venue 决定是否补摘要。 |
| `title_no` | 标题不相关，不补摘要不下载。 |
| `needs_abstract` | 标题通过但缺摘要，需要补摘要。 |
| `auto_abstract_candidate` | 脚本根据已有摘要和关键词打分出的候选，必须人工/主线程复核。 |
| `auto_abstract_maybe` | 脚本根据已有摘要和关键词打分出的弱候选，必须人工/主线程复核。 |
| `auto_abstract_no` | 脚本根据已有摘要和关键词打分出的不相关候选；可抽样复核，不能作为强结论。 |
| `human_abstract_yes` | 人工/主线程读过摘要后确认相关，进入文献库和下载队列。 |
| `human_abstract_maybe` | 人工/主线程读过摘要后认为可能相关，作为 adjacent/background 或人工复核。 |
| `human_abstract_no` | 人工/主线程读过摘要后确认不相关，不下载。 |
| `download_queued` | 已准备下载全文。 |
| `downloaded` | PDF 已下载。 |
| `fulltext_read` | 已读全文并写入矩阵。 |

## 慢流程诊断

如果用户反馈“文献检索很慢”，先区分慢在哪一段：

| 阶段 | 典型症状 | 处理 |
|---|---|---|
| 元数据检索慢 | OpenAlex/arXiv 请求等待或 429 | 不默认用 OpenAlex；用 `--sources quick --timeout 12 --cache-dir .lit-cache`，命中足够就停止。 |
| API 限流 | Semantic Scholar、OpenAlex、Crossref 429 或 quota exceeded | 停止重试，记录到 search log，转官方 proceedings、OpenReview、USENIX/CCS/PoPETs、arXiv、作者页和普通网页搜索。 |
| raw 记录筛选慢 | 从几百/几千条筛 100+ 条耗时 | 先按标题/摘要/venue/year 本地打分，选 top 30-60；不要对每条做网络 URL 探测。 |
| PDF 下载慢 | 逐条 DOI、出版社 URL、arXiv title match | 先确认是否绕过了 title/abstract gate；能直接从官方/OA/arXiv 下载就直接下，批量和失败项再交给 `scansci-pdf`。 |
| arXiv 标题匹配慢 | 对缺 URL 条目逐条查 arXiv | 只对 keep=yes 且高分 top N 做 title match；结果写入缓存。 |
| citation chaining 慢 | 对全部候选做引用扩展 | 只对 5-10 篇 seed paper chaining。 |

下载前筛选的默认分层：

1. **Tier 1**：已通过摘要筛选，且已有官方/OA/arXiv/conference PDF URL，直接下载。
2. **Tier 2**：有 DOI/arXiv 但无直接 PDF，交给 `scansci-pdf` 分批下载。
3. **Tier 3**：只有标题或出版社页面，先保留 metadata，不阻塞核心池。
4. **Tier 4**：相关性低、年份不符、或不在主题检索范围内，不进入下载队列。不要仅因不是投稿目标 venue 就排除。

当第一阶段已经有 30-40 篇高质量 PDF 时，不要为了凑满数量把低质量条目硬塞入核心池。应先阅读已有核心池，再按结构性缺口定向补文献。

## 工作流

1. **Query design**：把中文需求转成 2-4 组英文查询；先覆盖核心概念，不要一次性展开全部同义词。
2. **Fast seed search**：每组查询先用 DBLP/`--sources quick`，限制年份、主题领域和宽检索 venue，生成 20-50 条标题候选。
3. **Title screening**：先筛标题、主题相关性、年份和 venue 质量；若前 20 条明显偏题，改检索式，不继续补摘要或下载。
4. **Abstract queue**：只对标题通过的候选补摘要。
5. **Abstract screening**：脚本候选先进入 `auto_abstract_candidate`；主线程/人工读摘要后决定 `human_abstract_yes`、`human_abstract_maybe`、background 或 reject。
6. **Escalation search**：核心池不足、强相关 venue 缺失、危险相似工作不足或投稿目标 venue 样本不足时，再用 `--sources all`、arXiv title match、Semantic Scholar、网页和 proceedings 补漏。
7. **Seed expansion**：只对 5-10 篇核心论文做 backward/forward citation chaining，不对整个结果池 chaining。
8. **Library handoff**：把摘要通过条目交给 `literature-library-manager`，写入 papers.csv 和状态字段。
9. **Access handoff**：需要学校权限时，先交给 `institutional-access-resolver` 完成一次授权和测试。
10. **Download handoff**：摘要通过后，先尝试可见直链 PDF；批量 DOI/arXiv、失败项和需要学校权限的条目交给 `scansci-pdf`。
11. **Research handoff**：选题闭环交给 `cs-idea-discovery-pipeline`，相关工作写作交给 `related-work-synthesizer`。

## 学校账户 / WebVPN

学校账号不能直接替代 OpenAlex/arXiv/Crossref 这类元数据 API。它的作用是让下载请求经过学校图书馆订阅代理访问出版社全文。

使用顺序：

1. 先用本 skill 找到 DOI/arXiv ID。
2. 用 `institutional-access-resolver` 完成学校授权：查询学校 -> 设置学校 -> CAS 登录 -> 测试连接。
3. 下载时使用 `scansci-pdf` 和 `use_vpnsci=true`。
4. 若目标期刊学校未订阅，仍可能下载失败；此时改用 OA、作者主页、arXiv、conference proceedings 或请求用户提供可访问链接。

## 本地脚本

可用 `scripts/cs_lit_search.py` 做无 key 初筛。默认 `--sources quick`，比全源检索快：

```powershell
python scripts/cs_lit_search.py --query "<topic keywords> <target method/problem>" --year-from 2024 --limit 30 --sources quick --cache-dir .lit-cache --out results.json
```

脚本只做元数据检索和去重，不下载 PDF。

需要高召回时再运行：

```powershell
python scripts/cs_lit_search.py --query "<topic keywords> <target method/problem>" --year-from 2024 --limit 80 --sources all --cache-dir .lit-cache --out results_all.json
```

标题/摘要阶段筛选：

```powershell
python scripts/stage_gate_screen.py --input results.json --keywords "<topic keywords comma separated>" --out screening.csv --abstract-queue abstract_queue.csv --download-queue download_queue.csv
```

该脚本只做本地筛选和队列生成；不联网、不下载 PDF。

脚本输出是 `screening_matrix`，不是 `evidence_matrix`。它只能决定摘要队列和下载队列，不能用于声明研究空白、方法失败原因或 idea 成立。

## 输出格式

```markdown
**Search Plan**
...

**Source Status**
| Source | Key Required | Used | Mode | Notes |

**Scope Contract**
| Topic | Optional Submission Venue | Reputable Search Scope Venues | Explicitly Excluded |

**Screening Table**
| Stage | Decision | Title | Year | Venue | DOI/arXiv | Source | Why Relevant |

**Abstract Queue**
| Title | DOI/arXiv | Reason |

**Download Queue**
| Title | DOI/arXiv | Tier | Reason |

Only `human_abstract_yes` and selected `human_abstract_maybe` rows can enter the download queue.

**Speed Diagnosis**
| Stage | Bottleneck | Action |

**Gaps**
...
```

## GitHub 参考

需要设计更复杂的检索代理或本地文献库时，读取 `references/github-literature-search-notes.md`。只吸收 workflow，不复制外部项目模板。
