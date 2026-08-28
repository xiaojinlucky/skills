<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="做科研的大师兄：帮助研究生把课题从发现问题推进到下一步的中文科研思路 Skills" />
</p>

<p align="center">
  <img src="./assets/readme/avatar.jpg" width="112" alt="做科研的大师兄账号头像" />
</p>

<h1 align="center">一条能持续推进课题的科研思路流</h1>

<p align="center">
  从文献中学习别人怎样发现问题，从自己的数据与异常中形成候选，<br />
  再把课题收敛成可判断、可验证、可写成论文主线的下一步。
</p>

<p align="center">
  <code>中文科研</code>&nbsp;&nbsp;
  <code>研究生友好</code>&nbsp;&nbsp;
  <code>生物医学与生信</code>&nbsp;&nbsp;
  <code>从 GAP 到下一步</code>
</p>

## 先从你现在卡住的地方开始

你不需要先把课题整理完整。说出当前最真实的卡点，`meta-research-hub` 会先判断最值得解决的未决问题，再组织真正相关的方法。

| 你现在的状态 | 可以推进到 |
| --- | --- |
| 只有一个大方向，不知道从哪里切入 | 找到值得追问、能够判断的课题入口 |
| 读了很多文献，还是找不到 GAP | 学习论文的发现路径，划清已知边界与研究空白 |
| 候选很多，结果彼此矛盾 | 区分技术原因、真实窗口与需要继续收敛的问题 |
| 有现象，却还不是科学假设 | 形成可证伪的假设与决定性预测 |
| 不知道选什么分析或预实验 | 选择能改变判断的最低充分动作 |
| 结果不少，却讲不成论文主线 | 排清证据顺序、Figure 逻辑与结论边界 |

## 一条清楚的科研推进路径

**课题发现** → **文献找 GAP** → **形成假设** → **分析设计** → **预实验判断** → **论文主线** → **继续、收缩或停止**

重点不是一次堆多少方法，而是每一步都回答一个会改变课题主线、方法选择或下一行动的问题。

## 科研主线模块

| 阶段 | 你要回答的问题 | 对应 Skill |
| --- | --- | --- |
| 找到入口 | 我手里的方向、数据或现象，哪里值得先追？ | [`research-entry`](./skills/research-entry/) |
| 找到 GAP | 别人怎样发现问题，已知边界在哪里？ | [`literature-mining`](./skills/literature-mining/) |
| 收敛课题 | 哪个问题最值得成为当前主线？ | [`topic-convergence`](./skills/topic-convergence/) |
| 判断创新 | 新论文出现后，课题还剩什么空间？ | [`innovation-judgment`](./skills/innovation-judgment/) |
| 形成假设 | 哪个解释可以被证伪，结果会如何改变判断？ | [`hypothesis-construction`](./skills/hypothesis-construction/) |
| 设计验证 | 怎样把候选关系推进成机制链与关键验证？ | [`mechanism-design`](./skills/mechanism-design/) |
| 校准因果 | 现有证据能说相关、必要、充分还是中介？ | [`causality-rescue`](./skills/causality-rescue/) |
| 快速试错 | 最小预实验怎样判断候选值不值得继续？ | [`pre-experiment-design`](./skills/pre-experiment-design/) |
| 组织主线 | 怎样把开题、论文、综述或答辩讲成一条线？ | 见完整方法地图 |

<details>
<summary><strong>展开完整的 13 个方法 Skill</strong></summary>

| Skill | 主要用途 |
| --- | --- |
| [`research-entry`](./skills/research-entry/) | 从方向、数据、现象或技术中找到科研入口 |
| [`literature-mining`](./skills/literature-mining/) | 学习高质量论文的发现路径，寻找已知边界与 GAP |
| [`topic-convergence`](./skills/topic-convergence/) | 把宽方向、候选和异常收敛成研究问题 |
| [`innovation-judgment`](./skills/innovation-judgment/) | 审计实质重合、创新窗口与课题去向 |
| [`hypothesis-construction`](./skills/hypothesis-construction/) | 把观察压成可证伪、可验证的假设 |
| [`mechanism-design`](./skills/mechanism-design/) | 从候选关系推进到机制链和关键验证 |
| [`causality-rescue`](./skills/causality-rescue/) | 区分相关、必要、充分、中介与直接作用 |
| [`pre-experiment-design`](./skills/pre-experiment-design/) | 用最小成本判断候选、方法与风险 |
| [`grant-and-opening`](./skills/grant-and-opening/) | 组织开题、基金与科研计划的科学主线 |
| [`sci-writing-and-revision`](./skills/sci-writing-and-revision/) | 把结果、Figure 与证据组织成论文故事 |
| [`review-writing`](./skills/review-writing/) | 搭建综述观点，并按影响排序停止修改 |
| [`thesis-and-defense`](./skills/thesis-and-defense/) | 组织学位论文、答辩与外审准备 |
| [`research-mindset`](./skills/research-mindset/) | 把资源与压力转成继续、收缩、暂停或停止决策 |

</details>

## 30 秒开始

把需要的 Skill 放入支持 Agent Skills 的 AI 工具，然后直接描述你的真实情况。复杂问题建议从总入口开始：

```text
请用 meta-research-hub 作为我的科研思路流。
先判断当前最需要解决的未决问题，再组织真正相关的方法。
请把结果按「产出—影响—下一步」收束，不要一开始给我大而全的方案。
```

<details>
<summary><strong>查看 3 个可以直接使用的提问示例</strong></summary>

### 结果互相矛盾

```text
我有一个候选基因，单细胞结果和预后方向相反。
请先解释和复核这个矛盾，再判断候选如何收敛，不要为了得到一致结论直接换方向。
```

### 课题被新论文覆盖

```text
我的具体课题刚被一篇新论文覆盖。
请先做实质重合、GAP 和创新窗口审计，再告诉我继续、收缩、重定位还是停止。
```

### 论文不知道怎样收口

```text
我的结果已经基本齐全。
请先判断最适合的论文主线，再按影响排序告诉我哪些补充仍会改变结论，哪些可以停止。
```

</details>

## 这套方法坚持什么

- **从高质量论文学习发现，不搬论文答案。** 重点学习作者如何找到 GAP、产生候选和升级证据。
- **先有科学问题，再选方法。** 分析、实验和 Figure 都要服务核心问题与论文主线。
- **探索可以积极，结论必须诚实。** 可以追踪有意义的信号，但不制造结果，也不把相关性写成因果。
- **每轮都要落到下一步。** 输出说明现在得到什么、它会改变什么、接下来最值得做什么。

## 使用边界

这是一套科研思路指导系统，不替代真实实验、伦理审批、临床诊疗、统计审查或导师的最终决定；不会编造文献、数据与实验结果，也不保证论文发表。

正式分析、代码、图表和实验执行仍应使用适合任务的专业工具。这套 Skills 负责让它们围绕正确的问题展开。

---

<p align="center">
  <strong>从一句真实的卡点开始：</strong><br />
  我现在最担心的是……
</p>
