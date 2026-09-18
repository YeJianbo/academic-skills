---
name: scipilot-writing-skill
description: 按明确的期刊或跨学科风格改写学术文本、caption 和投稿信。用于 Nature/Science/Cell 等指定表达风格；普通计算机科学论文润色直接使用 section-writing-polish。
license: MIT
---

# SciPilot Academic Writing

## 范围与信息

先读取用户指定的文件或片段，从请求、文件格式和上下文确定语言方向、处理范围、目标格式与修改深度。已给出的信息直接复用；只询问无法推断且会实质改变结果的缺项。未指定期刊时沿用原稿或通用学术表达；未指定深度时保守润色。收到修改任务即可在授权范围内执行。

局部润色、翻译或 caption 直接处理片段；不要扩成论文架构规划或完整审稿。只有任务需要时才读取下表中的参考。

## 内容与格式约束

1. 润色只改表达，不擅自改数值、公式、引用键、结论方向、实验事实或技术含义。发现疑似事实错误时保留原值并单独指出；不编造文献、数据或证明。
2. 原文已清晰准确时保留，避免为换词而换词。去 AI 味时保留作者观点、领域术语和必要的限定语。
3. 断言强度匹配证据；相关性不能改成因果，单项研究不能写成普遍结论。不同证据层次分清。
4. 保留模板默认字号、行距与结构，不用 `vspace` 挤版面。LaTeX 保留数学、自定义命令、`cite`、`
ef`、`label`；只修复正文中的真实转义错误，不批量改写公式和命令。
5. Word 文档保留已有样式和结构；交付供粘贴的正文时避免 Markdown 污染。列表是否保留由内容逻辑和模板决定。
6. 写文件时保留用户已有修改，检查差异是否越过授权范围。

## 执行与检查

起草或改写后重读相关段落，核对原意、事实、逻辑、术语与格式。验证范围匹配改动：一句润色做直接核对；修改 LaTeX 项目时运行必要编译；涉及文档布局时检查实际渲染。

长篇语言检查、批量处理或用户要求量化检查时，可运行：

```bash
python scripts/writing_lint.py <文件> --mode {latex|word|markdown|plain} --lang {en|zh} --report <工作目录>/lint_report.json
```

词表、句长、被动比例等风格命中是提示，不是必须改写的结论。结合原文判断，必要术语可保留；实际编译错误、损坏的引用、乱码和改变原意的问题应修复。只有新增修改或未解决问题需要时才重跑相关检查。如实报告已运行命令及未解决的实际问题，不把没运行的检查写成通过。

辅助脚本按需使用：`scripts/latex_clean.py` 检查 LaTeX 字符；`scripts/text_stats.py` 提供语言统计；`scripts/docx_text.py` 辅助提取 DOCX。先核对脚本行为，避免覆盖数学、自定义命令或文档样式。

## 交付

默认提供改后文本或修改后的文件。较长或语义敏感的改写附简短修改说明；用户需要逐项审阅时再提供详细日志。直译、回译仅在用户要求或具体语义歧义需要核对时提供，不要求固定三段式。

仅在实际运行脚本时生成 lint 报告；不为一句话润色创建配套日志文件。用户只要求 critique 时输出问题与建议，不直接改稿。

## 按需参考

| 任务 | 参考 |
|---|---|
| 翻译、精简、扩写等具体写作操作 | `references/prompt_library.md` |
| 时态、衔接、简洁和证据措辞 | `references/sci_writing_principles.md` |
| 章节起草 | `references/section_playbooks.md` |
| 已指定期刊的语言与报告要求 | `references/journal_styles.md` |
| 去 AI 味和自然表达 | `references/de_ai_humanize.md` |
| 投稿信、逐条审稿回复 | `references/cover_letter_and_rebuttal.md` |
| 复杂载体与边界情况 | `references/workflow.md` |

参考中的示例按本次任务取用，不扩大修改范围。引用检索与核验使用 `cs-literature-search` 和原始来源；排版与 BibTeX 集成使用 `latex-paper-integrator`。科研配图使用 `nature-figure`；正式审稿使用 `review`；整体论文架构使用 `paper-architecture-planner`。
