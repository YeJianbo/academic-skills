---
name: scansci-pdf
description: 下载指定或批量论文、解析 DOI/arXiv/标题、导出引用及处理所需全文访问。使用可用 MCP 或官方/OA 直链；宽主题文献发现由 cs-literature-search 负责。
---

# scansci-pdf — 学术论文下载 MCP 服务

## 概述

scansci-pdf 是一个 MCP 服务器，提供 21 个工具，覆盖学术论文的搜索、下载、引文导出和 WebVPN 机构代理管理。支持 13+ 数据源并行下载，100+ 中国高校 WebVPN。

## 工具可用性

先检查当前会话是否提供所需 MCP 工具；文档中的工具名不等于可调用能力。工具缺失时使用官方网页检索、OA/arXiv/会议或作者 PDF 直链，以及可用的本地下载工具继续已授权任务；只有实际依赖的能力缺失才报告阻碍。不为普通下载要求安装整套插件或机构登录。

## 能力边界

### 直接能力（单工具即可完成）

| 能力 | 对应工具 | 说明 |
|------|----------|------|
| 按 DOI/arXiv ID 下载单篇论文 | `scansci_pdf_download` | 支持 4 种下载策略 |
| 批量下载多篇论文 | `scansci_pdf_batch_download` | 并发下载，默认 10 线程 |
| 关键词搜索论文 | `scansci_pdf_search` | 基于 OpenAlex，支持年份筛选和排序 |
| 导出引文 | `scansci_pdf_citation` | BibTeX / RIS / EndNote 三种格式 |
| 导入 .bib 文件并下载 | `scansci_pdf_import_bib` | 自动提取 DOI 并批量下载 |
| 推送到 Zotero | `scansci_pdf_zotero_push` | 需先下载论文到缓存 |
| 解析论文列表文件 | `scansci_pdf_parse_list` | 支持 APA、BibTeX、DOI 列表 |
| WebVPN 登录/测试/状态查询 | `scansci_pdf_vpnsci_*` 系列 | 5 个工具管理 WebVPN |
| 系统配置和健康检查 | `scansci_pdf_config_*` / `scansci_pdf_health_check` | 配置、缓存、诊断 |

### 组合能力（需编排多工具）

| 能力 | 工具编排 | 流程 |
|------|----------|------|
| 模糊研究查询 → 下载 | search → download | 先搜索获取 DOI，再下载 PDF |
| 论文列表全文下载 | resolve_and_download | 解析列表 → 补全 DOI → 批量下载 |
| 搜索+筛选+批量下载 | search → 人工筛选 → batch_download | 按关键词搜索，选择后批量下载 |
| WebVPN 设置+下载 | vpnsci_set_school → vpnsci_login → download | 5 步 WebVPN 流程 |
| .bib 导入+引文补全 | import_bib → citation | 下载后补充引文格式 |

### 不可实现（超出 MCP 能力）

| 请求 | 原因 |
|------|------|
| 阅读/理解论文内容 | scansci-pdf 只下载 PDF，不解析内容 |
| 翻译论文 | 需要其他工具（如 PDF 阅读+翻译 API） |
| 生成文献综述/摘要 | 需要 LLM 读取 PDF 后生成 |
| 下载非学术 PDF | 不支持普通网页 PDF、报告、发票等 |
| 访问付费期刊全文（无机构代理） | 无合法途径时可能失败 |

## MCP 工具参考

### 论文下载

| 工具 | 描述 | 关键参数 |
|------|------|----------|
| `scansci_pdf_download` | 下载单篇论文 | `identifier`（必需，DOI 或 arXiv ID）、`strategy`（可选）、`use_vpnsci`（可选）、`use_tor`（可选）、`bibtex`（可选） |
| `scansci_pdf_batch_download` | 批量下载多篇论文 | `identifiers`（必需，列表）、`use_vpnsci`（可选）、`use_tor`（可选）、`batch_id`（可选，断点续传 ID）、`resume`（默认 true） |
| `scansci_pdf_resolve_and_download` | 解析列表 → 补全 DOI → 批量下载 | `file_path`（必需）、`resolve_titles`（默认 true） |

**参数约束：**
- `identifier`: DOI（如 `10.1038/nature12373`）、DOI URL、或 arXiv ID（如 `2301.00001`）
- `strategy`: `"fastest"`（默认，多源并行）、`"oa_first"`（OA 优先）、`"scihub_only"`、`"legal_only"`
- `use_vpnsci`: 需先通过 `vpnsci_login` 完成 CAS 认证
- `use_tor`: 启用 Tor 代理（优先使用已运行的外部 Tor，否则自动启动内嵌 Tor）

**返回值：**
- 成功：`{"success": true, "file": "/path/to/paper.pdf", "doi": "...", "source": "..."}`
- 失败：`{"success": false, "error": "..."}`

**下载源（13+ 并行）：**

包括出版商直链、Unpaywall、OpenAlex、SemanticScholar、Crossref、DOAJ、EuropePMC、CORE、PMC、LibGen、Sci-Hub 等。启用 WebVPN 后还可通过高校代理访问。部分高级源需配置 API key。

### 搜索与解析

| 工具 | 描述 | 关键参数 |
|------|------|----------|
| `scansci_pdf_search` | 关键词搜索论文（OpenAlex） | `query`（必需）、`limit`（默认 10，最大 50）、`year_from`、`year_to`、`sort` |
| `scansci_pdf_parse_list` | 解析论文列表文件 | `file_path`（必需，.md/.txt/.bib） |

**参数约束：**
- `sort`: `"cited_by_count"`（被引最多）、`"publication_date"`（最新）、省略为相关性排序
- `year_from` / `year_to`: 整数年份，如 `2020`

**返回值（search）：**
```json
{"results": [{"title": "...", "doi": "...", "authors": [...], "year": 2024, "cited_by_count": 42, "abstract": "..."}]}
```

### 引文管理

| 工具 | 描述 | 关键参数 |
|------|------|----------|
| `scansci_pdf_citation` | 获取论文引文 | `identifier`（必需）、`format`（"bibtex"/"ris"/"endnote"） |
| `scansci_pdf_import_bib` | 导入 .bib 文件并下载全部论文 | `bib_file`（必需） |
| `scansci_pdf_zotero_push` | 推送论文到 Zotero | `identifier`（必需，需先下载） |

### WebVPN 管理

| 工具 | 描述 | 关键参数 |
|------|------|----------|
| `scansci_pdf_vpnsci_login` | 浏览器 CAS 认证登录 | 无 |
| `scansci_pdf_vpnsci_test` | 测试 WebVPN 连接性 | `doi`（可选，默认 10.1038/nature12373） |
| `scansci_pdf_vpnsci_status` | 检查登录状态 | 无 |
| `scansci_pdf_vpnsci_schools` | 搜索支持的大学 | `query`（可选，如"清华"） |
| `scansci_pdf_vpnsci_set_school` | 设置当前大学 | `school`（必需，如"北京大学"） |

### 系统管理

| 工具 | 描述 | 关键参数 |
|------|------|----------|
| `scansci_pdf_setup_check` | 检测系统环境，返回安装建议 | 无 |
| `scansci_pdf_health_check` | 检查所有数据源可用性 | `detailed`（默认 false） |
| `scansci_pdf_source_scores` | 查看各源自适应健康评分（成功率、延迟） | 无 |
| `scansci_pdf_network_diagnose` | 网络诊断：测试 DNS、代理、Tor、FlareSolverr 状态，返回修复建议 | 无 |
| `scansci_pdf_config_get` | 查看当前配置 | 无 |
| `scansci_pdf_config_set` | 修改配置项 | `key`（必需）、`value`（必需） |

**常用配置项：**

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `scihub_enabled` | `true` | 启用 Sci-Hub/LibGen |
| `openalex_api_key` | `""` | OpenAlex Content API key（免费，每天 100 次） |
| `network_proxy` | `""` | 全局代理（如 `socks5://127.0.0.1:1080`） |
| `batch_workers` | `10` | 批量下载并发数 |
| `auto_rename` | `true` | 自动重命名为作者+标题 |
| `download_strategy` | `"fastest"` | 默认下载策略 |
| `scansci_pdf_cache_clear` | 清除下载缓存 | `identifier`（可选，省略清除全部） |

### Tor 管理（内嵌 Tor，无需 Docker）

| 工具 | 描述 | 关键参数 |
|------|------|----------|
| `scansci_pdf_tor_install` | 自动下载安装 Tor Expert Bundle 到 ~/.scansci-pdf/tor/ | 无 |
| `scansci_pdf_tor_start` | 启动内嵌 Tor SOCKS5 代理 | `use_bridges`（默认 false，受限网络启用 obfs4 桥接） |
| `scansci_pdf_tor_stop` | 停止内嵌 Tor 代理 | 无 |

**使用流程：**
1. `scansci_pdf_tor_install` — 首次使用时下载 Tor 二进制（~30MB）
2. `scansci_pdf_tor_start` — 启动 Tor SOCKS5 代理（自动分配端口）
3. 下载时设置 `use_tor=true`，自动通过 Tor 代理访问
4. 在受限网络（如防火墙封锁 Tor）中，使用 `scansci_pdf_tor_start(use_bridges=true)` 启用 obfs4 桥接

## 工作流编排指南

### 检索与下载分工

- 单篇/批量论文下载：只要用户给 DOI、arXiv ID、BibTeX、论文标题列表、论文清单文件，优先直接用本 skill，不要强行先走 `survey/cs-literature-search` 或 OpenAlex。
- 网络直链可下载：如果 Codex 网络检索已经找到官方 PDF、arXiv PDF、OpenReview PDF、会议 proceedings PDF 或作者主页 PDF，可以直接下载并记录来源；不必调用本 skill。
- 元数据检索和初筛：只有用户是在探索主题、需要候选标题池、标题/摘要筛选时，才用 `survey/cs-literature-search`。
- 实际需要机构订阅全文、公开来源不可得时，使用 `institutional-access-resolver`；公开元数据和 OA 下载直接进行。
- 批量、断点续传、多源并行、WebVPN、标题解析、BibTeX 导入、下载失败重试：使用本 skill。
- 学校账户/WebVPN 只解决出版社全文访问，不替代文献检索；但已有 DOI/arXiv/title 时，下载不需要先跑 OpenAlex。

### 流程 1：模糊研究查询

用户说"帮我下载 2020 年后植物功能性状对气候变化响应的论文"：

```
1. scansci_pdf_search(query="plant functional traits climate change", year_from=2020, limit=20, sort="cited_by_count")
2. 按用户主题、年份、数量和相关性筛选；已有下载授权时直接形成下载清单
3. scansci_pdf_download(identifier=筛选后的DOI) 或 scansci_pdf_batch_download(identifiers=[...])
```

**关键点：** 复用已有下载授权，在指定范围内筛选和下载，不机械下载全部搜索结果。范围存在影响结果的歧义时才补问；用户只要求搜索时交付候选，不擅自扩成批量下载。

### 流程 1A：已有 DOI/arXiv/title 列表直接下载

用户给 DOI、arXiv ID、BibTeX、CSV 或论文标题列表时：

```
1. 如果是 DOI/arXiv 列表：scansci_pdf_batch_download(identifiers=[...])
2. 如果是 BibTeX：scansci_pdf_import_bib(bib_file="...")
3. 如果是标题/引用列表文件：scansci_pdf_resolve_and_download(file_path="...", resolve_titles=true)
```

**关键点：** 这是“下载任务”，不需要先调用 `cs-literature-search`，也不要为了下载强行 OpenAlex 初筛。若 title resolve 慢或失败，再要求用户补 DOI/arXiv 或把条目分批。

### 流程 1B：网络直链 PDF 下载

用户给论文标题或页面，Codex 网络检索能直接找到稳定 PDF 链接时：

```
1. 确认 PDF 来源：official proceedings / arXiv / OpenReview / author homepage / institutional page
2. 直接下载 PDF 到目标目录
3. 记录 pdf_url、pdf_source、download_method=direct-web、download_status=downloaded
4. 若直链失败，再切换到 scansci_pdf_download 或 scansci_pdf_resolve_and_download
```

**关键点：** 直链 PDF 成功时不需要额外调用 OpenAlex 或 scansci-pdf；失败项再进入本 skill 的多源下载流程。

### 流程 2：论文列表全文下载

用户提供一个包含论文引用的文件：

```
1. scansci_pdf_parse_list(file_path="papers.md") → 查看解析结果
2. scansci_pdf_resolve_and_download(file_path="papers.md") → 自动补全 DOI + 批量下载
```

**关键点：** `resolve_and_download` 内部会自动调用 OpenAlex 补全缺失的 DOI。

### 流程 3：WebVPN 设置

用户想通过学校代理下载论文：

```
1. scansci_pdf_config_set(key="vpnsci_enabled", value="true")
2. scansci_pdf_vpnsci_set_school(school="你的学校名称")
3. scansci_pdf_vpnsci_login → 浏览器打开 CAS 认证
4. scansci_pdf_vpnsci_test → 确认连接正常
5. scansci_pdf_download(identifier="...", use_vpnsci=true)
```

只有实际需要机构访问的论文才进入上述流程；优先复用有效登录态，失效时由用户手动重新认证。用当前所需全文验证访问后继续该批订阅论文，其他公开论文独立下载。

若 `scansci_pdf_vpnsci_schools` 找不到学校，或学校没有支持的 WebVPN 模板：

1. 让用户提供学校图书馆/电子资源/WebVPN 登录入口 URL。
2. 优先尝试学校网页手动登录后下载，或让用户在浏览器中打开出版社页面。
3. 对已经拿到 DOI 的论文，继续尝试 OA、arXiv、作者主页、conference proceedings。
4. 不要要求用户把学校账号密码发给 Codex；认证应在浏览器/CAS 页面由用户完成。

### 流程 4：故障排查

下载失败时的诊断流程：

```
1. scansci_pdf_network_diagnose → 一键诊断网络（DNS、代理、Tor、FlareSolverr）
2. 根据诊断结果修复：
   - "检测到系统代理但未使用" → config_set network_proxy "<代理地址>"
   - "DNS 解析失败" → 配置代理或更换 DNS
   - "连接超时" → 配置代理绕过封锁
   - "FlareSolverr 未运行" → docker run -d -p 8191:8191 ghcr.io/flareSolverr/flareSolverr
3. 重试下载，失败结果中 hint.guidance 包含针对性建议
```

**关键点：** 下载失败时，结果中的 `hint.guidance` 字段会自动给出具体操作步骤（配置代理、切换策略、启用 WebVPN 等），无需手动排查。

## 常见边界情况

| 场景 | 处理方式 |
|------|----------|
| 用户只给了论文标题，没有 DOI | 先用 `search` 搜索标题获取 DOI，再用 `download` 下载 |
| 用户想下载的论文不在 OpenAlex 中 | 告知用户需要提供 DOI 或 arXiv ID |
| 用户想批量下载 100+ 篇 | 使用 `batch_download`，并发数由配置 `batch_workers` 控制 |
| 用户所在网络封锁 Sci-Hub | 建议使用 `strategy="legal_only"` 或配置代理 |
| 用户想下载的论文需要机构权限 | 建议设置 WebVPN（需要有高校账号） |
| 用户想读取已下载论文的内容 | 超出能力，建议使用 PDF 阅读工具 |
| 用户环境缺少组件 | 调用 `setup_check` 诊断并按返回的建议引导 |

## 环境安装引导

当用户首次使用或遇到下载问题时，用 `scansci_pdf_setup_check` 诊断环境：

```
1. scansci_pdf_setup_check → 获取环境状态和安装建议
2. 根据 readiness 判断：
   - "ready" → 一切就绪，可直接使用
   - "partial" → 部分功能受限，按建议安装缺失组件
   - "limited" → 核心组件缺失，部分下载源不可用
3. 按返回的建议逐步引导用户安装
```

### 组件说明

| 组件 | 用途 | 必需？ |
|------|------|--------|
| Tor | 匿名访问 Sci-Hub/LibGen，自动下载管理 | 可选（Sci-Hub 被封时需要） |
| WebVPN | 通过高校代理访问付费论文 | 可选（需要高校账号） |

### 快速安装

```
# 1. 自动下载安装 Tor（首次使用）
scansci_pdf_tor_install

# 2. 启动 Tor 代理
scansci_pdf_tor_start
# 受限网络（防火墙封锁 Tor）：
scansci_pdf_tor_start(use_bridges=true)

# 3. 使用 Tor 下载论文
scansci_pdf_download(identifier="10.1038/nature12373", use_tor=true)
```
