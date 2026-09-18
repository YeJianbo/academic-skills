---
name: institutional-access-resolver
description: "学术论文机构访问授权与验证技能。用于实际需要订阅全文时通过学校账号、WebVPN、SeamlessAccess、Shibboleth、CAS、图书馆电子资源代理完成一次性手动授权，随后复用登录态下载付费论文；适用于出版社页面出现 Access Through Institution、East China Normal University、Sign in via your institution、Full text access may be available、学校统一身份认证、WebVPN 或机构订阅验证失败等场景。"
---

# Institutional Access Resolver

用于在实际需要机构订阅全文且公开来源不可得时建立或恢复访问状态；公开检索和 OA 下载直接进行，已有有效登录态优先复用。它不保存账号密码，不绕过 CAS/验证码/二次验证；需要认证时，让用户在浏览器中手动登录。

## 目标

- 仅在实际需要机构访问或用户明确要求配置机构访问时处理学校授权。
- 验证当前浏览器、WebVPN 或下载工具是否能访问付费全文。
- 批量下载时复用已登录 session。
- 下载失败时区分登录失效、学校未订阅、出版社限制、网络或 DOI 问题。

## 默认流程

1. **Collect identifiers**：从 `cs-literature-search` 或用户文献列表获取 DOI/arXiv/title。
2. **Choose access path**：
   - 有 DOI 且学校 WebVPN 支持：优先用 `scansci-pdf` 的 WebVPN 流程。
   - 出版社页面显示 `Access Through Institution` / SeamlessAccess：让用户手动点学校并完成 CAS。
   - 已在浏览器登录学校图书馆：优先复用当前登录态。
3. **Manual authorization**：仅在没有有效登录态时，由用户在浏览器完成学校统一身份认证。不要要求用户把密码发给 Codex。
4. **Session test**：用 1-2 篇需要机构权限的 DOI 测试全文访问。
5. **Download handoff**：测试通过后，把 DOI 列表交给 `tools/scansci-pdf`，下载时使用 `use_vpnsci=true` 或复用浏览器/代理登录态。
6. **Failure triage**：失败时记录原因并回退到 OA、arXiv、作者主页、conference proceedings 或手动下载。

## scansci-pdf WebVPN 路径

当 MCP 工具可用时，按这个顺序执行：

```text
1. scansci_pdf_config_set(key="vpnsci_enabled", value="true")
2. scansci_pdf_vpnsci_schools(query="华东师范" 或 "East China Normal")
3. scansci_pdf_vpnsci_set_school(school="匹配到的学校名称")
4. scansci_pdf_vpnsci_login
5. 用户在打开的浏览器中完成 CAS/SSO 登录
6. scansci_pdf_vpnsci_status
7. scansci_pdf_vpnsci_test(doi="本次实际需要机构权限的 DOI")
8. scansci_pdf_download(identifier="...", use_vpnsci=true)
```

若学校不在 vpnsci 支持列表，改用出版社/学校网页登录态路径。

## SeamlessAccess / 出版社页面路径

适用于页面出现：

- `Access Through Institution`
- `Add or Change Institution`
- `Sign in via your institution`
- `Full text access may be available`
- `SeamlessAccess`

操作：

1. 让用户点击 `Access Through <学校名称>` 或重新选择学校。
2. 跳转到学校统一认证页后，由用户手动登录。
3. 登录回到出版社页面后，检查页面是否出现 PDF、Download PDF、Access PDF、Full Text。
4. 如果页面仍要求登录，记录出版社、DOI、错误状态，换 WebVPN 或 OA 路径。

## 判断结果

| 状态 | 判定 | 下一步 |
|---|---|---|
| `authorized` | 测试 DOI 可打开 PDF 或全文 | 开始批量下载。 |
| `login-required` | 跳到 CAS/SSO 或 SeamlessAccess | 等用户手动登录后重试。 |
| `not-subscribed` | 学校登录成功但仍无全文 | 回退 OA/arXiv/作者主页，记录失败。 |
| `session-expired` | 之前可访问，现在重新要求登录 | 重新授权一次。 |
| `network-failure` | DNS、代理、超时、证书问题 | 交给 `scansci-pdf` 网络诊断。 |
| `bad-identifier` | DOI 错、无 DOI、出版社页面不存在 | 回到 `cs-literature-search` 补元数据。 |

## 输出格式

```markdown
**Institutional Access Status**
authorized / login-required / not-subscribed / session-expired / network-failure / bad-identifier

**Access Path**
WebVPN / SeamlessAccess / publisher login / library proxy / OA fallback

**Test DOI**
...

**Next Download Command**
...

**Failures**
| DOI | Reason | Fallback |
```

## 交接

- 检索 DOI/arXiv/title：`survey/cs-literature-search`。
- 下载 PDF、WebVPN 工具调用：`tools/scansci-pdf`。
- 批量下载后的阅读和结构化总结：`survey/cs-idea-discovery-pipeline`。
- 引文/BibTeX 整理：`tools/scansci-pdf` 或 `latex-paper-integrator`。

## 安全边界

- 不保存、不索要、不打印学校账号密码。
- 不自动绕过验证码、短信、二次验证或访问控制。
- 不把学校登录 cookie 写入论文项目目录或公开 artifact。
- 只在用户拥有合法机构访问权限时使用。
