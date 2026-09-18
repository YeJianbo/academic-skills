---
name: paper-figure
description: 组织实验论文的主结果、消融及多图多表组合，选择证据呈现和 LaTeX 接入。绘制交由 nature-figure；单张已有图的局部修改直接使用绘图技能。
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
4. 使用 `nature-figure` 生成可复现脚本并执行；沿用已明确的后端，未指定时使用 R，不手改最终图片。
5. 导出 PDF/SVG/PNG。
6. 检查文字裁切、标签、legend、色盲安全、灰度可读、单位和统计量。
7. 生成 LaTeX include snippet 和 caption 草稿。

## 协作

- 数据可视化顾问：可参考 `scipilot-figure-skill`。
- 科研绘制、导出和实际视觉检查：使用 `nature-figure`。
- 图表 caption 写作：转 `writing/section-drafter` 或 `section-writing-polish`。
