---
name: security-privacy-auditor
description: "安全与隐私专项审查技能。用于审查密码学、联邦学习、隐私计算和安全论文中的 threat model、security/privacy definitions、adversary capabilities、leakage、trust assumptions、correctness、theorems、proof sketches、reductions、hybrid games、DP/MPC/HE/TEE/secure aggregation/ZKP 相关主张是否严谨。"
---

# Security Privacy Auditor

用于专门审查“安全/隐私保证是否真的成立”。不要做语言润色，不要替作者补证明；只指出模型、定义、证明和主张之间的缺口。

## 审查顺序

1. Extract claims: secure/private/robust/ZK/DP/confidential/anonymity 等主张。
2. Match claims to definitions: 每个 claim 是否有正式定义或清晰实验定义。
3. Audit adversary model: honest-but-curious、malicious、adaptive、colluding、external、server/client 能力。
4. Audit leakage and trust: 泄露函数、side information、setup、PKI、CRS、TEE、random oracle、trusted aggregator。
5. Audit proof: theorem statement、assumptions、simulator、hybrids/games、bad events、advantage bounds。
6. Compare wording: 摘要/引言/结论中的强主张是否超过证明范围。

## 常见 Critical 问题

- 声称 privacy/security，但没有定义 adversary 或 protected object。
- 经验攻击下降被写成形式化隐私保证。
- DP 只给 epsilon，不说明 clipping、noise、composition、accounting 或邻接关系。
- secure aggregation 假设和 collusion threshold 不匹配。
- TEE 方案忽略 side-channel、trust boundary 或 attestation。
- HE/MPC 方案没有通信/轮数/泄露/精度分析。
- theorem 证明的模型弱于论文声称的部署场景。

## 输出格式

```markdown
**Claim Inventory**
...

**Model and Assumption Gaps**
...

**Proof Risks**
...

**Overclaiming**
...

**Required Fixes**
...

**What Would Change My Mind**
...
```
