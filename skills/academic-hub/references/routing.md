# 学术技能责任与触发边界

仅在入口冲突、复杂任务分工或技能维护时读取。明确的日常任务由目录描述直接选定专用技能，不把本文件设为额外前置阅读。

## 结构

当前体系保留“总协调 → 可选分类路由 → 专用交付”的层次。请求已经清楚时跳过总协调和分类路由。每项具体产物选择一个负责人；跨多个产物的任务分别确定负责人，在已授权范围内完成整条链。相邻技能是按需能力，不是默认待办列表，也不意味着创建子代理。

| 用户要得到什么 | 当前负责人 | 不应自动扩大为 |
|---|---|---|
| 跨阶段研究路线与任务分工 | academic-hub | 加载所有学术技能 |
| 一个研究方向的探索、改进或可行性判断 | cs-idea-discovery-pipeline | 尚未授权的完整训练或投稿评分 |
| 找新的外部论文/相近工作 | cs-literature-search | 写整篇 Related Work |
| 获取指定论文或批量全文 | scansci-pdf | 重新发现用户已经指定的文献 |
| 给定论文的证据卡 | paper-evidence-distiller | 全文质量评分或跨论文综述 |
| 多篇论文的证据对照 | paper-reading-synthesizer | 为凑引用数再做宽检索 |
| benchmark/数据集/baseline 清单与比较条件 | benchmark-baseline-registry | 直接启动实验 |
| 整稿主线与章节蓝图 | paper-architecture-planner | 对现有一句话重新规划论文 |
| 从给定技术材料写新正文 | section-drafter | 每次只交一节然后等待 |
| 改写、翻译和精简已有正文 | section-writing-polish | 无请求地改研究问题或补实验 |
| 用已有文献写 Related Work | related-work-synthesizer | 对整库再筛选/蒸馏一遍 |
| 设计安全定义、定理和证明 | security-proof-builder | 将未证假设写成定理 |
| 显式去 AI 味/去防御性表达 | academic-paper-de-vibe | 对纯检索、运行或绘图启动改稿 |
| 设计实验和结果表需要包含的证据 | experiment-plan | 改善已有表格颜色与排版 |
| 执行代码/协议/训练实验 | run-experiment | 无差别 GPU 检查 |
| 已有结果的科学解释 | experiment-results-analyzer | 创造缺失的结果或曲线 |
| 决定下一轮运行、回退或停止 | experiment-iteration-controller | 不受请求约束的无限优化 |
| 主结果/消融图表组合与 LaTeX 接入 | paper-figure | 包办每张图的渲染实现 |
| 数据图制作与局部修图 | nature-figure | 重设计实验或默认 image_gen |
| 数据应使用何种图型 | scipilot-figure-skill | 系统架构图 |
| 直接可编辑架构图、流程图、图源修改 | drawio-diagram-builder | 强制先出位图再重画 |
| 明确要求 AI 构图参考再重建 | codex-paper-figure-skill | 接管普通数值图 |
| 整篇诊断、评分、成熟度或修订前后比较 | cs-paper-reviewer | 没有授权就改稿 |
| 安全/隐私模型和证明专项审查 | security-privacy-auditor | 五个独立代理的默认评审组 |
| 实验公平性、攻击与复现专项审查 | evaluation-reproducibility-auditor | 没有授权就重跑完整实验 |
| 审稿回复、response letter、修订安排 | rebuttal-revision-planner | 普通稿件写作被写成答辩 |
| LaTeX/Typst 集成、编译、模板和引用链接 | latex-paper-integrator | 重写科学内容 |
| 复现材料打包 | reproducibility-packager | 创建没有实际运行依据的成功报告 |

## 交接判断

1. 看当前产物，不靠“论文”“图”“review”等单个关键词加载整组技能。
2. 用户同时要求审查并修改时，检查给出具体修改依据后继续修改；只要审查时不碰原稿。
3. 普通写作由写作负责人吸收去防御性表达原则；显式去防御性请求可以由 de-vibe 直接处理。不要求两份相同的报告。
4. 用已有结果画图不触发新实验；设计指标或消融不触发绘图；引用不足只补具体缺口。
5. 责任不清才使用 survey、writing、review、experiment、tools 这些短路由器。同一明确请求无需重复经过它们。
6. 确需跨轮状态时复用既有文件，按 [增量工作流](incremental-academic-workflows.md) 交接有效要求、产物位置和下一项工作。

## 旧入口与外部结构

`top-conference-paper-writing` 的重复入口停用；其知识保留在 `paper-architecture-planner/references/legacy-top-conference-paper-writing.md`。context-budget-manager 维持原停用状态。

本结构适配 CCFA Skills v0.10.0 的单一负责人、职责边界和按需协作思想。保留本地密码学/隐私专项能力、R 默认和已有工具路径，不另安装一组 ccf-* 别名或强制 ccfa.yaml。上游来源和许可见 incremental-academic-workflows.md。
