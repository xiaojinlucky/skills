<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="Meta Research Hub：13 个中文科研方法 Skills，帮助研究生把真实卡点推进成可验证的下一步" />
</p>

<p align="center">
  面向研究生的中文科研思路流：先判断真正值得解决的问题，再用文献、假设、分析、预实验与写作持续推进课题。
</p>

<p align="center">
  <code>研究生友好</code>
  <code>中文科研</code>
  <code>生物医学 / 生信</code>
  <code>从 GAP 到下一步</code>
</p>

## 从一个真实卡点开始

`meta-research-hub` 是总入口。你不需要先把课题整理得很完整，只要说清楚现在最困扰你的问题：方向太大、文献找不到 GAP、候选互相矛盾、假设不够清楚、下一步不知道做分析还是实验，或结果已经很多却讲不成论文。

它会优先回答三件事：

1. **现在最值得解决的未决问题是什么？**
2. **哪一步最可能改变对课题的判断？**
3. **什么结果意味着继续、收缩、转向或停止？**

> **发现问题 → 文献找 GAP → 课题收敛 → 形成假设 → 分析 / 预实验判断 → 组织论文主线 → 决定下一步**

## 13 个核心 Skills

复杂问题从 [`meta-research-hub`](./skills/meta-research-hub/) 开始；任务已经明确时，可以直接进入下面对应的专业 Skill。

### 发现与收敛

- [`research-entry`](./skills/research-entry/) — 从零建立科研入口，形成问题意识与第一段学习路径。
- [`literature-mining`](./skills/literature-mining/) — 从高质量论文学习发现路径、筛选逻辑与 GAP，而不是搬运论文结论。
- [`topic-convergence`](./skills/topic-convergence/) — 把大方向、候选或矛盾结果收敛成具体科学问题。
- [`innovation-judgment`](./skills/innovation-judgment/) — 判断具体课题的实质重合、创新空间与可继续推进的窗口。

### 假设与验证

- [`hypothesis-construction`](./skills/hypothesis-construction/) — 把观察与候选压成可证伪假设，明确竞争解释和决定性预测。
- [`mechanism-design`](./skills/mechanism-design/) — 从项目自己的证据出发，设计最低充分的机制验证链。
- [`causality-rescue`](./skills/causality-rescue/) — 区分相关、必要、充分、中介与直接作用，让因果表述匹配证据。
- [`pre-experiment-design`](./skills/pre-experiment-design/) — 用最小预实验尽早完成 go / no-go 判断。

### 写作与交付

- [`grant-and-opening`](./skills/grant-and-opening/) — 把科学主线组织成开题、标书或科研计划。
- [`sci-writing-and-revision`](./skills/sci-writing-and-revision/) — 组织论文主线、Figure 证据顺序、返修与回复材料。
- [`review-writing`](./skills/review-writing/) — 搭建综述框架、凝练观点并组织段落论证。
- [`thesis-and-defense`](./skills/thesis-and-defense/) — 围绕真实工作组织学位论文、答辩与外审准备。

### 投入与收口

- [`research-mindset`](./skills/research-mindset/) — 在结果矛盾、被抢发或资源有限时，决定继续、收缩、暂停、转向或停止。

## 30 秒开始

把 `meta-research-hub` 和本页列出的 13 个 Skills 导入支持 Agent Skills 的 AI 工具，然后直接用自然语言描述你的课题和卡点。首次使用可以复制下面这段：

```text
请用 meta-research-hub 帮我推进这个课题。

先判断当前最值得解决的未决问题，不要一开始给我大而全的方法清单。
对每个建议说明：
1. 这一步会产出什么；
2. 它会改变什么判断；
3. 什么结果意味着继续、收缩、转向或停止。

优先给我信息增量最高、成本最低的下一步。
如果继续优化已经不会改变主线或结论，请明确告诉我停止。
```

<details>
<summary><strong>三个常见场景的直接问法</strong></summary>

### 从文献找 GAP

```text
我已经有一个大方向，但没有具体课题。
请不要直接搬论文结论，先分析高质量论文怎样发现问题和形成候选，
再帮我找仍然可判断、可验证的 GAP。
```

### 结果互相矛盾

```text
我的不同分析得到相反方向的结果。
请先判断这是技术原因、真实生物学窗口还是候选边界问题，
然后只给会改变主线判断的复核与下一步。
```

### 论文不知道什么时候该停

```text
我的主要结果已经齐全。
请先判断最合适的核心 claim 和 Figure 主线，
再按影响排序哪些补充会改变结论，哪些只是锦上添花。
如果没有高影响缺口，请明确建议停止继续补。
```

</details>

## 方法原则

- **学习发现路径，不搬论文答案。** 文献用于理解未知、筛选逻辑与证据升级，不替代项目自己的数据和判断。
- **科学问题先于方法清单。** 只有能改变判断、验证假设或加强主线的方法，才值得优先投入。
- **探索可以积极，结论必须诚实。** 不制造结果、不隐藏决定性反证，也不把相关性包装成因果。
- **把预算留给信息增量。** “还能改”不等于“现在应该改”；停止标准本身也是科研设计的一部分。

## 使用边界

这是一套科研思路与方法判断 Skills，不替代真实实验、实验平台 SOP、伦理审批、临床诊疗、正式统计审查，以及学校、期刊或基金的当前官方规则，也不保证论文发表。

需要代码、正式数据分析、图表制作或实验执行时，请使用对应的专业工具；这些 Skills 的作用，是让工具围绕正确的问题、证据和主线展开。

---

<p align="center">
  <strong>从一句真实的卡点开始：</strong><br />
  我现在最需要判断的是……
</p>
