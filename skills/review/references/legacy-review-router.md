---
name: review
description: "审稿入口：自审、外审模拟、方法审查、引用检查与回复信。"
---

# Review

用于论文、实验和代码的质量审查。

## 覆盖内容

- 论文自审与投稿前体检
- 模拟同行评审与审稿意见生成
- rebuttal 与 response letter
- 方法、识别策略、实验设计、结果解释审查
- 引用、Bib、事实一致性检查

## 常见分流

- 论文整体把关：`academic-paper-reviewer`
- 去 AI 味后的再审：`academic-paper-de-vibe` 之后回到这里
- 引用核查：使用 citation 类工具
- 代码与实验问题：联动 `experiment`
- **SOUND** — Design is valid, implementation is correct
- **MINOR ISSUES** — Fixable concerns, none threatening core results
- **MAJOR ISSUES** — Significant concerns that could change conclusions
- **CRITICAL ERRORS** — Fundamental design flaw or incorrect implementation

Save report to `quality_reports/[file]_strategy_review.md`

### Manuscript Polish (`--proofread`)
Dispatch **writer-critic** standalone:
- 6 categories: structure, claims-evidence, ID fidelity, writing, grammar, compilation
- Save report to `quality_reports/[file]_proofread_report.md`

### Cross-Language Replication (`--replicate [language]`)
1. Auto-detect source language from file extension
2. Dispatch **Coder** in replication mode — re-implement in target language
3. **coder-critic** reviews both implementations
4. Compare numerical outputs per `.claude/references/domain-profile.md` Quality Tolerance Thresholds
5. Save replicated script and comparison report

---

## Verifier Pass/Fail Definition

The Verifier produces a binary PASS/FAIL result:

**For papers (`.tex`):**
- LaTeX compiles error-free (warnings acceptable, errors not)
- All figures referenced exist and render
- All references resolve (no `??`, no undefined citations)
- All tables render correctly
- Bibliography compiles without errors

**For code (`.R`, `.py`, `.do`, `.jl`):**
- Script runs without errors from start to finish
- All packages loaded at top of script
- No hardcoded absolute paths
- `set.seed()` present once at top if stochastic
- Output files created at expected paths

**For replication packages:**
- All scripts run in declared order
- Outputs match paper tables/figures within tolerance
- README accurately describes the pipeline

Verifier score maps to 0 (FAIL) or 100 (PASS) for weighted aggregation.

---

## Scoring

| Mode | Blocking? | Gate |
|------|-----------|------|
| Comprehensive | Yes | 80 commit, 90 PR |
| Peer Review | Yes | Editorial decision |
| Stress Test | Advisory | Reported, non-blocking |
| Code Review | Yes | 80 commit |
| Causal Audit | Yes | 80 commit |
| Proofread | Yes (paper), Advisory (talks) | 80 commit |

---

## Principles
- **Smart routing.** File type determines the default review mode.
- **Flags override.** Use explicit flags for targeted reviews.
- **Critics never edit.** All reviews produce reports only.
- **Journal drives everything.** The journal profile shapes the editor's bar, referee selection, and review culture.
- **Referees vary.** Different dispositions and pet peeves mean running `/review --peer` twice gives different feedback — just like submitting to two journals would.
- **"What would change my mind."** Every major comment must include the specific evidence or analysis that would resolve the concern.
- **Design-opinionated, package-flexible.** Recommend standard packages (fixest, did, rdrobust, etc.) but accept and validate alternatives. The design matters more than the package.
- **Sequential phases in causal audit.** Never skip to robustness before verifying the core design holds.
- **Proportional severity.** Missing `set.seed()` is Major; missing comment is Minor.
- **Worker-critic separation.** The reviewer never fixes code or rewrites text — it only critiques.
- **Actionable output.** Every issue must have a concrete fix, not vague advice.
