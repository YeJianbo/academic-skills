---
name: cs-idea-discovery-pipeline
description: "计算机科学论文选题调研闭环技能。用于任意可替换 CS 主题，按主题宽检索近三年有声誉的相关顶会/顶刊和强相邻领域文献，必要时先将核心论文用 paper-evidence-distiller 压成可回链证据卡，再识别结构性研究空白，推理现有方法失效原因，提出可验证新假设，调用多代理评估可行性、创新性和候选投稿 venue 适配度，并在本机环境做小实验、原型或可复现实证验证；实验不成立则回到候选 gap 队列继续迭代，直到得到可实现 idea、候选投稿 venue 和论文大纲。"
---

# CS Idea Discovery Pipeline

用于把“调研”推进到“可在本机实现的论文 idea”。默认领域是计算机科学；主题、检索范围、年份窗口、可用资源和实验形式都必须在每次任务开始时锁定。投稿目标会议/期刊是可选项；用户未指定时，先按主题宽检索有声誉来源，idea 稳定后再给 2-3 个候选投稿 venue。密码学、联邦学习、隐私计算、安全与隐私保护机器学习只是一个常用 profile，不是固定范围。

## 触发场景

当用户要求以下任务时使用本技能：

- 查找指定 CS 主题在指定年份窗口内的顶会/顶刊论文。
- 面向指定投稿目标会议或期刊评估 idea 适配度、贡献形态和拒稿风险。
- 从失败机理倒推出可验证新假设。
- 下载并阅读大量论文后生成可投稿 idea。
- 需要通过本机小实验验证 idea 可行后再停止。
- 需要 agy、5.5、5.4 等 subagent 参与可行性和会议适配度讨论。

## Topic/Venue Profile

每次启动前先写出 profile，不得沿用上一次任务的主题或会议：

| Field | Meaning |
|---|---|
| `topic` | 用户指定的 CS 主题，如 LLM agent、systems、security、database、HCI、vision、NLP、FL/privacy 等。 |
| `target_venue` | 可选投稿目标会议/期刊。用户指定时用于判断 idea 定位、贡献形态、实验强度、写作口径和拒稿风险；用户未指定时设为 `unspecified`，后续输出候选投稿 venue。它不是默认检索边界。 |
| `search_scope_venues` | 文献检索范围。默认按主题宽检索有声誉的相关顶会/顶刊、arXiv、出版社页面和强相邻领域，不限于 `target_venue`；只有用户明确要求时才缩到某个会议。 |
| `year_window` | 默认最近三年；用户指定时按用户要求。 |
| `reputation_policy` | 默认现场上网核验声誉：优先官方会议/期刊页面、CCF 推荐国际学术会议和期刊目录、DBLP/proceedings、学会或出版社页面、领域 survey/benchmark 论文；CCF A/B/C 可作参考，不作为唯一过滤器，B/C 中强相关或领域公认 venue 可以保留。 |
| `venue_fit_axis` | 若有投稿目标 venue，记录该 venue 看重什么；若未指定，则在 idea 收敛后为 2-3 个候选 venue 分别记录适配轴。 |
| `must_include_sources` | 用户指定会议、论文列表、数据库、学校访问或本地 PDF。 |
| `exclude_scope` | 明确排除的子方向、低质量 venue、纯应用包装或无法本机验证的路线。 |
| `local_validation_type` | 本机可做的验证：ML pilot、系统 microbenchmark、形式化证明草案、复现实验、数据分析、用户研究原型等。 |

若用户给了目标 venue，把它记为 `target_venue`，同时仍按主题设置宽检索的 `search_scope_venues`。例如“目标投 AAAI，主题是 FL/privacy”时，检索范围应覆盖 AAAI、NeurIPS、ICML、ICLR、IJCAI、AISTATS、CCS、USENIX Security、S&P、NDSS、PETS、TIFS、TDSC、arXiv 和相关出版社页面；AAAI 只用于后续 venue fit 和论文定位。若用户只给主题、没有目标 venue，则先按主题常见且有声誉的顶会/顶刊做宽检索，并把 `target_venue=unspecified`；不要要求用户先补会议，idea 初步成型后再给 2-3 个候选投稿 venue 和各自风险。

## Fresh Run Manifest

每次开始新调研都必须在 run 根目录创建 `run_manifest.md`。用户说“从头开始”“不要看之前的”“重新找论文”时，必须启用 fresh-start boundary，并在 manifest 写明禁用的旧目录。可用脚本：

```powershell
python scripts/init_research_run.py --out-dir "<run-dir>" --topic "<topic>" --year-window "2024-2026" --target-venue "unspecified" --search-scope "<reputable venues and adjacent fields>" --fresh-start --forbidden-old-dir "<old-run-dir>"
```

Manifest 至少记录：

| Field | Meaning |
|---|---|
| `topic` | 文章主题。 |
| `target_venue` | 可选投稿目标；未指定为 `unspecified`。 |
| `search_scope_venues` | 实际检索范围。 |
| `reputation_policy` | 声誉核验依据：现场上网、CCF、官方 proceedings、DBLP、学会/出版社、领域共识。 |
| `forbidden_old_dirs` | fresh run 禁止引用的旧目录。 |
| `evidence_count_ledger` | 当前各 gate 数量和来源文件。 |

## Evidence Count Ledger

每个调研 run 必须维护 `metadata/evidence_counts.md`，并在每个 gate 后更新。可用脚本：

```powershell
python scripts/evidence_count_ledger.py --screening metadata/screening_matrix.csv --download-status metadata/download_status.csv --read-status metadata/read_status.csv --evidence-matrix notes/matrices/core_evidence_matrix.md --out metadata/evidence_counts.md
```

必须区分这些计数：

| Count | Meaning |
|---|---|
| `metadata_found` | 只找到元数据。 |
| `title_yes/title_maybe` | 只通过标题筛选。 |
| `auto_abstract_candidate` | 脚本根据摘要关键词打分得到的候选，不等于已读摘要。 |
| `human_abstract_yes/human_abstract_maybe` | 主线程或人工读过摘要后的判断，只有这些才能进入下载队列。 |
| `downloaded` | PDF 已在本地，不等于读过。 |
| `fulltext_read` | 已全文阅读并进入 evidence matrix。 |
| `evidence_matrix_rows` | 可支撑 gap 的强证据行。 |

## 总体闭环

不要只做文献列表或普通综述。必须按以下闭环推进：

1. **Topic/Venue profile lock**: 明确主题、宽检索范围、年份窗口、关键词、排除范围和可用本机验证方式；投稿目标 venue 可选，未指定时后续输出候选 venue fit。
2. **Run manifest**: 写入 `run_manifest.md` 和初始 `metadata/evidence_counts.md`；fresh run 必须声明禁用旧目录。
3. **Reputation scope check**: 现场上网或查 CCF/官方 proceedings/DBLP 等来源，确认检索范围包含有声誉 venue；不要用固定内置名单替代当前核验。
4. **Title seed scan**: 先用 `cs-literature-search` 的 `--sources quick` 和缓存生成 20-50 条候选标题；只做标题/venue/year 筛选，不下载全文。
5. **Abstract gate**: 只对标题通过的候选补摘要并筛选；脚本输出的 `auto_abstract_candidate` 必须经主线程/人工读摘要确认成 `human_abstract_yes` 后，才进入文献库和下载队列。
6. **Core PDF download**: 只下载 `human_abstract_yes` 或人工确认的 `human_abstract_maybe`；下载失败记录原因，不用低质量论文硬凑数量。
7. **Core evidence distillation**: 对核心 PDF 或已有 Markdown 优先调用 `paper-evidence-distiller`，生成 `.distilled.md` 证据卡，保留样本、时间范围、主张、表图锚点、系数和限制；这一步是 gap mining 前的单篇证据骨架，不等于全文精读完成。
8. **Core reading pass**: 用 `paper-reading-synthesizer` 结合核心 PDF 和 `.distilled.md` 精读核心论文，生成 paper notes 和 evidence matrix。
9. **Reading gate**: 只有 evidence matrix 已覆盖足够核心论文，才允许进入结构性空白识别。
10. **Structural gap mining**: 基于已读论文和可回链证据卡整理方法类别、共同假设、共同失败场景和未填逻辑缺口。
11. **Failure-first reasoning**: 对每个候选空白回答“原方法为什么会失效”，定位关键瓶颈。
12. **Gap shortlist discussion**: 归纳 2-5 个候选 gap，先用证据、可实现性和 venue fit 讨论出最可行的一个，不要直接锁死第一想法。
13. **Targeted adjacent expansion**: 只有当候选 gap 暴露具体缺口、反例、危险相似工作、baseline 或理论边界需要核验时，才围绕该 gap 定向检索相邻论文；禁止在未读核心池前自动启动“额外 40 篇”。
14. **Hypothesis inversion**: 从失败瓶颈倒推出可验证新假设。
15. **Subagent quorum**: 调用 agy、5.5、5.4 或可用的多代理工具，从可行性、会议适配度、审稿人攻击角度评估。
16. **Venue fit gate**: 若用户指定投稿目标 venue，用 `review/venue-profile-router` 或现场网络检索判断该 venue 适配度、近期偏好和主要拒稿风险；若未指定，比较 2-3 个有声誉候选 venue 的适配度。
17. **Reviewer attack loop**: 用 `review/cs-paper-reviewer`、`security-privacy-auditor`、`evaluation-reproducibility-auditor` 或与主题匹配的审查标准检查硬伤。
18. **Phenomenon pilot**: 先验证 gap 对应的现象或失败机理是否真实存在。
19. **Method pilot**: 现象成立后再验证候选方法是否优于强 baseline。
20. **Iteration gate**: 若现象或方法 pilot 不支持假设，记录失败原因并回到 gap shortlist 选择下一个；若支持，输出 idea、证据、论文大纲和后续实验计划。

## 硬门禁

这些规则优先级高于数量目标：

- 未完成标题筛选，不得补摘要、不得下载全文。
- 未完成摘要筛选，不得把条目加入核心文献库。
- 未创建 `run_manifest.md` 和 `metadata/evidence_counts.md`，不得进入 gap mining。
- `auto_abstract_candidate` 不等于 `human_abstract_yes`；脚本摘要候选不得直接进入下载队列。
- `downloaded` 不等于 `fulltext_read`；本地 PDF 数量不得用于支撑结构性空白。
- `.distilled.md` 不等于 `fulltext_read`；证据卡只能作为单篇证据骨架和回链索引，不能替代 evidence matrix。
- 不得把 `target_venue` 当作默认检索边界；除非用户明确要求“只查某会议/期刊”，否则必须按主题宽检索有声誉的相关顶会/顶刊和强相邻领域。用户未指定投稿目标时，不得停下来要求先选会议。
- 未下载或无 PDF 的论文只能标记为 `metadata-only`，不能支撑强结论。
- 未完成核心证据卡蒸馏和核心论文精读并生成 evidence matrix，不得声称发现结构性空白。
- 自动脚本生成的 role 统计、关键词分类、screening matrix 不等于 evidence matrix。
- 未形成结构性空白证据，不得启动泛泛的“第二批 40 篇”相邻扩展。
- 未形成 2-5 个候选 gap 的对比表，不得直接锁定最终 idea，除非用户明确只要求评估单个 idea。
- 未完成危险相似工作检索，不得进入 method pilot。
- 未完成 failure-first reasoning，不得提出最终 idea。
- 未通过 subagent quorum、reviewer attack 和 pilot，不得输出“最终 idea”或论文大纲。
- 数量目标不能覆盖质量门禁；宁可先读 20 篇高相关核心论文，也不要下载 80 篇低质量 PDF。

## 禁止的错误流程

以下行为必须立即停止并回退到对应 gate：

- 只看标题或摘要就直接确定 idea。
- 检索花费很久后，为了“继续推进”跳过全文阅读。
- 第一批核心论文尚未形成 evidence matrix，就自动启动第二批“额外 40 篇”。
- 精读后只拿一个 gap 直接开实验，没有比较其他候选 gap。
- 没有查危险相似工作，就声称 idea 有新意。
- 先把 PDF 下载数量凑够，再反过来决定哪些算核心论文。
- 用 subagent 的概念性判断替代论文阅读证据。
- 把 `metadata-only`、下载失败、未读论文写进结构性空白证据。
- 把脚本生成的 core/adjacent/background 分类当作已读证据。
- 用关键词统计或误匹配修正后的统计直接生成 gap summary。

正确回退：

- idea 已被提前提出：标记为 `provisional hypothesis`，回到 core reading pass 验证。
- 第二批已提前启动：暂停扩展，把已有结果标为 `unused adjacent candidates`，先完成第一批 evidence matrix。
- 单个 gap 被过早锁定：回到 gap shortlist，至少补 2 个替代 gap 和危险相似工作表。
- 下载队列过大：只保留 `human_abstract_yes` 的 Tier 1/Tier 2 和少量高价值 `human_abstract_maybe`，其他条目标记 `metadata_only`。

## 检索要求

### 第一批：顶会/顶刊主池

- 年份：默认 2024-2026；若当前日期变化，按“最近三年”滚动更新。
- 数量：先形成 20-40 篇高相关核心候选；只有标题/摘要筛选质量达标后，再扩展到 40 篇以上。
- 来源：按主题宽检索相关顶会/顶刊 proceedings、OpenAlex、Semantic Scholar、arXiv、DBLP、Google Scholar、publisher pages；投稿目标会议只作为必须关注来源之一，不限制检索范围。
- 搜索范围：优先覆盖该主题的主流发表场域和强相邻场域。例如 AI/ML + privacy 选题应同时看 AI/ML 会议、安全/隐私会议、隐私计算/密码学相关期刊和高质量预印本。
- 声誉核验：默认现场上网查官方 proceedings、CCF 推荐目录、DBLP、学会/出版社页面和近年领域综述；记录每个核心 venue 的声誉依据。CCF B/C 或未列入 CCF 的 venue 只要主题强相关、领域公认或论文质量高，可以进入候选池。
- API 限流：Semantic Scholar、OpenAlex、Crossref 或 arXiv 被限流、429、额度耗尽或连续超时时，记录到 search log，不反复重试；转官方 proceedings、OpenReview、USENIX/ACM/IEEE/IACR/PoPETs 页面、DBLP、arXiv、作者主页和普通网页搜索继续建池。
- 领域关键词：从 Topic/Venue Profile 生成 2-4 组英文查询，覆盖问题、方法、数据/系统 setting、评价指标和常见 baseline。不要把 FL/privacy/crypto 关键词默认套到其他主题。
- 必须去重，并记录 DOI/arXiv、venue、年份、代码链接、数据集、任务类型。

先做快速种子池：

- 每个方向先跑 2-4 个核心查询，不超过 50 条结果。
- 若前 20 条相关性低，立即改检索式，不继续下载。
- 只有种子池相关性达标后，才扩大到 40+ 主池。
- repeated query 必须复用 `cs-literature-search` 的缓存目录。
- 如果已有 30-40 篇高质量 PDF，不要为了数量把低质量条目硬塞入核心池；先读核心池并形成 gap，再定向补齐缺口。
- PDF 下载分层执行：直接 OA/arXiv 优先，DOI/出版社条目排队，只有标题的条目不阻塞主流程。
- 第一批的完成标准不是“下载数量”，而是“核心论文 evidence matrix 能支持 gap 判断”。
- 若核心论文已有 `.distilled.md`，第二步阅读必须优先复用其中的主张、限制和锚点，再回原文补核；不要每次从 PDF 零散重找。

### 第二批：相邻问题扩展池

- 触发条件：第一批核心论文已经精读，evidence matrix 明确指出需要核验的缺口、反例、攻击面、baseline 或理论边界。
- 数量：按缺口分批检索，先 10-20 篇；仍不足以回答缺口时再扩展，不默认一次性启动 40 篇。
- 围绕已证据化的候选空白扩展到与主题匹配的危险相似工作、强 baseline、理论边界、系统实现、数据集/benchmark、评价指标、部署约束和反例论文。
- 不只找支持 idea 的论文，也要找可能否定 idea 的论文。
- 第二批不能用来替代第一批阅读；它只能回答第一批阅读后产生的具体问题。

### 下载与引用

- 优先使用 `tools/literature-library-manager` 维护文献状态，`tools/scansci-pdf` 下载 PDF。
- 需要保存下载清单、失败清单、检索式和筛选理由。
- 不能声称“所有论文都读过”，除非 `paper-reading-synthesizer` 已生成阅读矩阵记录。

## 阅读矩阵

每篇核心论文至少记录：

| Field | Meaning |
|---|---|
| Problem | 解决什么问题 |
| Setting | 任务、数据、系统、用户、模型、威胁或部署 setting，按主题填写 |
| Assumption / Model | threat model、data model、system model、user model、learning setup 或理论假设 |
| Method | 论文使用的方法、算法、协议、系统设计、模型架构或实验范式 |
| Claim | 论文核心保证或效果 |
| Evidence | theorem、experiment、attack eval、complexity、ablation、user study、benchmark、artifact 等 |
| Failure Mode | 方法在哪些条件下会失败 |
| Missing Piece | 理论上该解决但没解决的缺口 |
| Local Implementability | 本机能否复现或做 pilot |

若同名 `.distilled.md` 已存在：

- 先读取证据卡中的“关键主张与证据”“证据如何产生”“边界与未解决问题”“复核记录”。
- 把证据卡当作单篇导航和 grep 入口，用于快速定位表格、图、系数、样本和限制。
- 发现证据卡没有覆盖当前需要的 proof、attack、ablation 或 appendix 细节时，再回原 PDF 精读补齐。
- 不得直接把证据卡内容原样复制成 gap 结论；gap 结论只能来自跨论文比较后的 evidence matrix。

## 空白识别标准

只把“结构性空白”作为候选 idea，不把简单增量当空白。

合格空白应满足：

- 多类方法共享同一个隐藏假设或失败场景。
- 现有论文承认但没有解决，或解决方案只在弱模型/小规模/不公平设定下成立。
- 可以形成明确 hypothesis。
- 可以设计本机现象验证和方法 pilot。
- 有潜在候选投稿 venue 适配度。

不合格空白：

- “缺少更多实验”但没有新科学问题。
- “把 A 方法换到 B 数据集”但没有机制变化。
- “组合两个已有模块”但没有解释为什么原方法失败。
- 只能靠大规模资源验证，本机无法起步。

## Subagent Quorum

当多代理工具可用时，必须调用：

- `agy`: 负责高层研究判断、选题价值、逻辑闭环。
- `5.5 subagent`: 负责技术可行性、方法设计、实验可实现性。
- `5.4 subagent`: 负责审稿人攻击、会议适配度、硬伤排查。

若这些具体 subagent 工具不可用，必须明确记录“不可用”，并用三个独立角色进行替代评估；不要假装已经调用。

每轮 quorum 必须输出：

1. idea 是否有新意。
2. 指定投稿目标或候选投稿 venue 是否匹配。
3. 关键技术瓶颈。
4. 现象 pilot 与方法 pilot 设计。
5. 最可能被 reviewer 拒绝的理由。
6. 是否进入实验，或回到文献扩展。

## Pilot Experiment Gate

必须在本机做最小验证后才能最终停止。验证形式由 Topic/Venue Profile 决定。默认环境：

- Python 使用 conda 环境。
- CUDA 已配置，可能有 cu121 和 cu128。
- 先探测 `conda info`、`nvidia-smi`、`python`、`torch`、CUDA 可用性。
- 优先做 1-3 小时内可完成的小实验、microbenchmark、复现片段、证明检查或数据分析；避免一开始就做完整主实验。

Pilot 类型按主题选择，包括：

- ML/CV/NLP/LLM：小模型、小数据、多 seed sanity、attack/eval 复现、ablation stub。
- Systems/DB/OS/Networks：microbenchmark、trace replay、吞吐/延迟/资源占用、可扩展性小样本。
- Security/Privacy/Crypto：攻击复现、威胁模型 sanity、协议开销 microbenchmark、证明草案核验。
- HCI/CSCW：原型任务、pilot user study 设计、日志/问卷分析、可用性风险检查。
- PL/SE：小型 benchmark、静态分析样例、bug corpus replay、工具原型。
- 小规模 FL 模拟。
- gradient inversion / membership inference 攻击复现。
- DP noise/privacy-utility 曲线。
- secure aggregation / MPC / HE 通信或延迟 microbenchmark。
- 非 IID 程度、客户端数量、恶意比例、隐私预算的敏感性小实验。

实验 gate：

- 若结果支持假设：用 `experiment/experiment-results-analyzer` 汇总证据，进入论文大纲和完整实验计划。
- 若结果不支持：用 `experiment/experiment-results-analyzer` 记录失败原因，回到空白识别或 hypothesis inversion。
- 若环境失败：先修复环境或降级 CPU/microbenchmark，不能把环境失败当作科学结论。

## 输出格式

最终输出必须包含：

1. **Search Log**: 检索式、来源、年份、可选投稿目标 venue、实际检索范围、下载数量、失败数量。
2. **Run Manifest**: `run_manifest.md`，包含主题、可选投稿目标、实际检索范围、声誉核验策略、fresh-start 禁用旧目录和 evidence count ledger。
3. **Screening Gate Report**: metadata_found、title_yes/title_maybe/title_no、needs_abstract、auto_abstract_candidate、human_abstract_yes/human_abstract_maybe、downloaded、fulltext_read 数量；明确这是 screening/counting，不是 evidence。
4. **Core Distilled Card Index**: 核心论文的 `.distilled.md` 清单、覆盖范围和已知抽取限制；明确它是单篇证据骨架，不是全文阅读完成证明。
5. **Core Evidence Matrix**: 已全文精读核心论文的结构化矩阵；未读论文不能列入强证据，不能用 screening role、下载状态或 distilled card 替代 evidence role。
6. **Gap Evidence Map**: 每个候选空白对应哪些已读论文、哪些 failure mode 和 missing piece。
7. **Gap Shortlist Decision**: 2-5 个候选 gap 的新意、可行性、venue fit、危险相似工作和 pilot 成本对比。
8. **Adjacent Expansion Plan**: 只有在 gap evidence map 触发时输出；列明为什么需要扩展、查什么、先查多少篇。
9. **Dangerous Similar Work Table**: 每个候选 idea 最可能撞车的论文、区别、反证和 reviewer 攻击点。
10. **Adjacent Paper Matrix**: 第二批定向扩展论文矩阵；没有触发扩展时标记为 not started。
11. **Failure Mechanism**: 每个空白对应的原方法失效原因。
12. **Hypotheses**: 可验证新假设。
13. **Subagent Quorum Report**: agy、5.5、5.4 或替代角色的讨论结论。
14. **Reviewer Attack Report**: 硬伤、缺实验、基准、可控变量、证明风险。
15. **Phenomenon Pilot Report**: 现象是否存在、指标、代码路径、结果和失败原因。
16. **Method Pilot Report**: 方法是否优于强 baseline、matched setting、代码路径、结果和失败原因。
17. **Selected Idea**: 最终 idea、为什么可行、为什么有新意、适合哪些候选投稿 venue；若用户指定了目标会议，说明为什么适配该会议。
18. **Paper Outline**: 标题候选、摘要骨架、贡献列表、章节大纲、实验计划。
19. **Next Actions**: 完整实验、写作、审稿、风险缓解路线。

## 停止条件

只有满足以下条件才能停止：

- 已完成标题筛选、摘要筛选、核心 PDF 下载和核心全文阅读矩阵，或明确说明哪个 gate 被阻塞。
- 结构性空白来自已读论文 evidence matrix，而不是来自标题、摘要或模型推测。
- 若启动第二批扩展，必须说明它由哪个 gap 触发；若未触发，不应为了数量自动启动。
- 已比较多个候选 gap，或明确说明为何只有一个 gap 可评估。
- 已检查危险相似工作，不能只查支持 idea 的论文。
- 至少一个 idea 通过 subagent quorum。
- 至少一个现象 pilot 支持 gap 真实存在，且至少一个方法 pilot 支持候选方法优于强 baseline；如果只完成现象 pilot，只能输出 provisional idea。
- 已用 reviewer attack loop 检查并修正重大硬伤。
- 输出可执行论文大纲和下一步实验计划。

若现象 pilot 不成立，换下一个 gap。若现象成立但方法 pilot 不成立，保留现象证据，回到 hypothesis inversion 或换候选方法；不允许直接输出“最终 idea”。
