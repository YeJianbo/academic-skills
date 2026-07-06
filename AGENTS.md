# AGENTS.md

语言：使用简体中文回答。

写作风格：直接推进论点，避免迂回立论和防御式表达。不要滥用 “not X but Y / rather than / since / however / therefore / not only but also”。技术细节按需要展开，不要过早堆砌。

学术写作：不要把论文写成审稿人回应稿。引言和总结可以各保留一次必要的边界声明，正文避免反复自我辩护。

多 agent 使用：复杂审稿、长上下文阅读、跨文件复杂改动、科研绘图前期方案和关键复核可以使用子代理；最终裁判仍由主线程负责。子代理未完成时不要脑补结论，应等待或明确标记 incomplete / blocked / needs more time。

学术审稿：只做 critique，不直接修稿；明确区分 SOUND、MINOR ISSUES、MAJOR ISSUES、CRITICAL ERRORS，并给出 what would change my mind。

科研绘图：论文配图、科研作图、多 panel 图或期刊级导出任务默认走 `nature-figure` 总流程。最终出图、导出、预览和 QA 在本地完成。

