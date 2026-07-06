---
name: rebuttal-revision-planner
description: "审稿回复与修订规划技能。用于处理审稿意见、meta-review、rebuttal、response letter、revision plan、R&R 二轮回复；将 reviewer comments 分类为 misunderstanding、missing evidence、valid flaw、scope disagreement、presentation issue，并生成逐条回应策略、修订优先级和可执行修改清单。"
---

# Rebuttal Revision Planner

用于收到审稿意见后制定回应和修订计划。默认不粉饰问题；先判断哪些意见必须承认并修，哪些可以澄清，哪些可以礼貌反驳。

## 工作流程

1. Parse comments: 按 reviewer、severity、topic 分解意见。
2. Classify each comment:
   - `valid flaw`: 真实缺陷，需要修。
   - `missing evidence`: 需要补实验、证明、引用或说明。
   - `misunderstanding`: 表述导致误读，需要澄清并改文。
   - `scope disagreement`: 目标范围分歧，需要解释边界。
   - `presentation issue`: 结构、图表、术语、语言问题。
3. Build response strategy: concede、clarify、add evidence、push back、defer to future work。
4. Build revision plan: manuscript edits、new experiments、new proof、new discussion、limitations。
5. Draft response skeleton.

## 回复原则

- 先感谢，再回应实质问题，不写空话。
- 每条回复必须说明 manuscript 中哪里会改。
- 对 valid flaw 不要强辩；给出修复和新增证据。
- 对 misunderstanding 不责怪 reviewer；承认表达不清并改写。
- 对 scope disagreement 礼貌解释边界，并在 limitations 中补充。
- 不承诺做不到的实验或证明。

## 输出格式

```markdown
**Revision Strategy**
...

**Comment Taxonomy**
| Reviewer | Comment | Type | Severity | Response Strategy | Manuscript Change |
...

**Must-Do Revisions**
...

**Optional / Pushback Items**
...

**Response Letter Skeleton**
...
```
