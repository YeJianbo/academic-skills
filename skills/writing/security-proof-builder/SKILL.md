---
name: security-proof-builder
description: "计算机科学论文安全与隐私证明起草技能。用于密码学、联邦学习、隐私计算、安全与隐私保护机器学习论文中起草和整理 correctness、security/privacy definitions、threat model、adversary capabilities、leakage function、hybrid games、reductions、proof sketches、theorem statements、protocol assumptions 和证明叙事；不替代 security-privacy-auditor 的审查。"
---

# Security Proof Builder

用于把协议或方法的安全/隐私主张写成可审查的定义、定理和证明草稿。它负责起草，最终严谨性检查交给 `review/security-privacy-auditor`。

## 输入

- 协议或算法描述。
- Threat model、adversary capabilities、trust assumptions。
- 安全/隐私目标：correctness、privacy、confidentiality、integrity、robustness、DP、simulation security、leakage profile。
- 用到的密码学原语或系统组件：MPC、HE、TEE、secure aggregation、ZKP、commitment、signature、DP mechanism。

## 输出结构

1. **Setting and Notation**：输入、输出、参与方、通信轮次、随机性和符号。
2. **Threat Model**：攻击者控制范围、可见信息、collusion、adaptive/static、honest-but-curious/malicious。
3. **Security/Privacy Definition**：形式化目标和 leakage function。
4. **Correctness Theorem**：协议输出为何满足功能目标。
5. **Security Theorem**：定理陈述、假设、结论和边界。
6. **Proof Sketch**：hybrid games、simulation、reduction 或 composition 逻辑。
7. **Limitations**：未覆盖攻击、额外信任假设、实现侧信道、参数条件。

## 写作原则

- 每个符号首次出现即定义。
- 定理只声明证明能支撑的内容，不把实验结果写成安全保证。
- 先讲 adversary 能看到什么，再讲它不能区分什么。
- 引用已有安全定义或原语时标明出处。
- 泄漏函数必须显式列出，不用“only leaks minimal information”这类空话。
- 证明草稿写完后必须交给 `security-privacy-auditor` 找硬伤。

## 常见交接

- 需要改论文叙事：交给 `section-drafter` 或 `section-writing-polish`。
- 需要审查证明漏洞：交给 `security-privacy-auditor`。
- 需要把 proof 变成 LaTeX 定理环境：交给 `latex-paper-integrator`。
