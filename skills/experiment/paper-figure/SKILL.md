---
name: paper-figure
description: "论文图表生成技能。用于从计算机科学实验结果生成投稿级 figures/tables，包括 FL/privacy/security 的主结果图、消融图、隐私-效用曲线、通信/延迟图、攻击成功率图、多面板图和 LaTeX include snippets；数据图优先用可复现 matplotlib/seaborn，复杂示意图按需转 nature-figure 或 scipilot-figure-skill。"
---

# Paper Figure

用于把实验结果转成论文图表。默认不改变数据，不美化掩盖结论。

## 发布会式视觉叙事

先读取 `../../academic-hub/references/publication-story-principles.md`，为每个主图指定一个可证实的结论。把最强证据放在首个视觉层级，caption 首句直接说明图支持的能力、条件和意义。不要修改数据、弱化必要统计信息或通过不公平轴范围制造优势。

## 图表类型

- Main comparison table / bar chart。
- Privacy-utility tradeoff curve。
- Communication / latency / throughput plots。
- Attack success rate vs defense strength。
- Ablation and sensitivity plots。
- Convergence curves。
- Multi-panel summary figure。

## 工作流程

1. 明确图要支持 `release thesis` 的哪个 claim、在哪些条件下成立。
2. 读取结果数据和 experiment plan。
3. 选择图型：有时间/round 用 line，方法比较用 grouped bar/table，tradeoff 用 curve，矩阵用 heatmap。
4. 生成可复现脚本，不手改最终图片。
5. 导出 PDF/SVG/PNG。
6. 检查文字裁切、标签、legend、色盲安全、灰度可读、单位和统计量。
7. 生成 LaTeX include snippet 和 caption 草稿。

## 协作

- 数据可视化顾问：可参考 `scipilot-figure-skill`。
- Nature/high-impact 多面板图：可转 `nature-figure`。
- 图表 caption 写作：转 `writing/section-drafter` 或 `section-writing-polish`。
