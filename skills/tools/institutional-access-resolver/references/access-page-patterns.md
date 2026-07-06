# Access Page Patterns

用于识别常见机构访问页面，并选择下一步动作。

## SeamlessAccess

常见文本：

- `Access Through`
- `Add or Change Institution`
- `Learn More about SeamlessAccess`
- `Full text access may be available`
- `Sign in via your institution`

动作：

1. 选择学校。
2. 等用户完成 CAS/SSO。
3. 回到出版社页面后找 PDF/full text。

## Shibboleth / SAML

常见文本：

- `Institutional Login`
- `Sign in through your institution`
- `Select your institution`
- `Shibboleth`

动作：

1. 选择学校或国家/地区 federation。
2. 用户手动认证。
3. 若跳转失败，改用学校图书馆 WebVPN。

## WebVPN / Library Proxy

常见 URL 特征：

- 学校图书馆电子资源入口。
- `vpn`、`webvpn`、`libproxy`、`ezproxy`。

动作：

1. 先登录学校代理。
2. 再从代理内访问出版社 DOI 页面。
3. 批量下载时优先用 `scansci-pdf` 的 `use_vpnsci=true`。
