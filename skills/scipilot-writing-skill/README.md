# scipilot-writing-skill

> SciPilot Skills family. Academic **writing & polishing co-pilot** — a top-journal editor and a harsh reviewer, built into your workflow.
> SciPilot Skills 家族成员 — 学术论文**写作与润色副驾驶**：把"顶刊编辑 + 严苛审稿人"装进你的写作流程。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB.svg)](#依赖--dependencies)
[![Status: v1.0.0](https://img.shields.io/badge/Status-v1.0.0-success.svg)](#)
[![Mode](https://img.shields.io/badge/Mode-Editor%2BReviewer-c41e3a.svg)](#为什么这不只是一份-prompt-清单)
[![Lint](https://img.shields.io/badge/Quality-machine--checked-orange.svg)](#写作质量证据链)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-orange.svg)](https://claude.com/claude-code)

A [Claude Code](https://claude.com/claude-code) / [Codex](https://github.com/openai/codex) / Cursor Skill that takes scientific text the last mile: from a Chinese draft, a rough paragraph, or a whole section, to **submission-grade** English (or Chinese) prose. It covers translation, condensing, expanding, polishing, de-AI / humanizing, logic checking, section drafting (Title / Abstract / Introduction-CARS / Methods / Results / Discussion), figure & table captions, results analysis, reviewer-style self-check, cover letters, and rebuttals. Unlike a prompt cookbook, **writing quality here is a machine-checked contract**: every delivery passes `writing_lint.py` (deterministic AI-tell / LaTeX-escape / Markdown-contamination / full-width-punctuation checks) plus an AI read-back self-review loop.

> [中文文档](#中文文档) | [English](#english)

---

## 中文文档

### 概览

科研写作最磨人的，往往不是"不会写"，而是反复调润色 prompt、改完不知道好没好、投出去才发现满是
中文乱标点 / LaTeX 没转义 / 读着一股 AI 味。`scipilot-writing-skill` 是 SciPilot 家族的写作成员，
专治这"最后一公里"——**先判断后下笔，宁缺毋滥，改完必自检。**

### 本机工作方式

从指定文件和上下文确定范围，已授权任务直接执行；只询问影响正确性的缺项。局部润色默认交付改后文本，回译和日志按需提供。

保留数值、公式、引用、结论、模板与用户已有修改。长篇或批量语言检查可使用 writing_lint.py；风格命中需人工判断。修改文档项目时完成必要编译或渲染检查，报告实际结果。具体执行规则见 [SKILL.md](SKILL.md)。

### 覆盖的写作任务（同类清单的全部 + 更多）

中译英润色 · 英译中 · 中文重写 · 缩写 · 扩写 · 英文润色 · 中文润色 · 逻辑检查 ·
去 AI 味(中/英) · 图标题 · 表标题 · 实验结果分析 · 审稿人视角自检 —— 以上对齐同类 prompt 清单；
**额外**：Title 创作 · Abstract 起草 · Introduction(CARS) · Methods/Results/Discussion 起草 ·
**Cover letter** · **Rebuttal / 审稿回复** —— 高水平 SCI 高频、同类清单普遍缺失的能力。

### 安装

```
请帮我安装这个 Skill：https://github.com/Haojae/scipilot-writing-skill.git
```

或手动：

```bash
git clone https://github.com/Haojae/scipilot-writing-skill.git \
          ~/.claude/skills/scipilot-writing-skill
# 仅处理 .docx 时才需要：
pip install python-docx
```

`writing_lint.py` / `latex_clean.py` / `text_stats.py` 只用 Python 标准库，开箱即用。

### 命令行直接调脚本

```bash
# 写作质量机检（核心）
python scripts/writing_lint.py draft.tex --mode latex --lang en --report lint_report.json
python scripts/writing_lint.py draft.txt --mode word  --lang zh

# LaTeX 转义 + 体检
python scripts/latex_clean.py draft.tex --check
python scripts/latex_clean.py draft.tex            # 转义后输出

# 量化指标：句长节奏 / 被动 / 名词化 / hedging
python scripts/text_stats.py draft.txt --lang en

# 读 Word 为纯文本（喂给机检）
python scripts/docx_text.py read paper.docx --to body.txt
```

### SciPilot Skills 家族

| Skill | 状态 | 功能 |
|---|---|---|
| scipilot-cite-skill | [v1.0.0](https://github.com/Haojae/scipilot-cite-skill) | 文献检索与引用插入 |
| scipilot-figure-skill | [v2.1.0](https://github.com/Haojae/scipilot-figure-skill) | 可视化顾问 + 绘制 + 视觉自检闭环 |
| **scipilot-writing-skill** | **v1.0.0 (本仓库)** | **写作与润色 + 写作质量证据链** |
| scipilot-review-skill | 规划中 | AI 模拟审稿 |
| scipilot-submit-skill | 规划中 | 投稿格式适配 |
| scipilot-read-skill | 规划中 | 论文阅读与翻译 |

### 许可证

[MIT](LICENSE) © 2026 Haojae

---

## English

### Overview

The hardest part of scientific writing is rarely "I can't write" — it's re-tuning polish prompts
forever, never knowing if the result is good, and discovering at submission time that the text is
full of half-width punctuation, unescaped LaTeX, or an unmistakable AI smell.
`scipilot-writing-skill` is the writing member of the SciPilot family, built for that last mile:
**judge before you write, change only what needs changing, and always self-check.**

### Local workflow

Read the supplied text and context, then execute within the authorized scope. Ask only about missing information that materially changes the result. Return revised text by default; back-translation and detailed logs are optional.

Preserve facts, numbers, formulas, citations, templates, and existing edits. Use language lint when useful for long or batch work; style matches require contextual judgment. Run relevant compilation or rendering checks for document changes and report actual outcomes. See [SKILL.md](SKILL.md) for the maintained local rules.

### Tasks covered (everything a prompt list does, and more)

zh→en polish · en→zh · Chinese rewrite · condense · expand · English polish · Chinese polish ·
logic check · de-AI (zh/en) · figure caption · table caption · results analysis · reviewer self-check —
all on par with comparable prompt collections. **Plus**: Title ideation · Abstract drafting ·
Introduction (CARS) · Methods/Results/Discussion drafting · **Cover letter** · **Rebuttal** — high-value
for SCI submission and usually missing from prompt lists.

### Installation

```
Please install this Skill for me: https://github.com/Haojae/scipilot-writing-skill.git
```

```bash
git clone https://github.com/Haojae/scipilot-writing-skill.git \
          ~/.claude/skills/scipilot-writing-skill
pip install python-docx   # only needed for .docx I/O
```

### SciPilot Skills family

| Skill | Status | Purpose |
|---|---|---|
| scipilot-cite-skill | [v1.0.0](https://github.com/Haojae/scipilot-cite-skill) | Reference discovery & insertion |
| scipilot-figure-skill | [v2.1.0](https://github.com/Haojae/scipilot-figure-skill) | Visualization advisor + renderer + visual self-check |
| **scipilot-writing-skill** | **v1.0.0 (this repo)** | **Writing & polishing + writing-quality evidence chain** |
| scipilot-review-skill | Planned | AI peer-review simulation |
| scipilot-submit-skill | Planned | Submission formatting |
| scipilot-read-skill | Planned | Paper reading & translation |

### License

[MIT](LICENSE) © 2026 Haojae

### 依赖 / Dependencies

```
# 核心脚本零依赖（Python 3.9+ 标准库）
python-docx>=1.1   # optional; only for reading/writing .docx
```
