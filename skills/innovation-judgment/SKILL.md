---
name: innovation-judgment
description: Judge the innovation and strategic value of a biomedical, bioinformatics, omics, mechanism, or translational research idea. Use when the user asks whether a topic is novel enough, whether prior publication kills the project, what part is truly new, how high the ceiling may be, or whether the novelty can be proved with available evidence. Evaluate difference, importance, provability, and competition without fixed paper-count or impact-factor scoring.
---

# Innovation Judgment

创新不是“别人有没有写过这个名词”，而是你的问题、现象、关系或证据链到底新增了什么。

## 必读

本任务尚未加载时，读 `../../suites/research-master/shared/research-core.md`、`../../suites/research-master/shared/routing-and-authority.md` 和 `../../suites/research-master/shared/expression-core.md`；已经记录在 `loaded_resources` 中就直接复用。

## 合同

- **进入条件**：需要判断课题新不新、值不值得做、被抢发后是否还能推进或投稿上限受什么限制。
- **唯一负责的决定**：给出创新点的类型、强弱、可证明性和当前竞争策略。
- **退出条件**：明确保留、重构或放弃哪项创新主张，以及需要什么证据才能把它写进主线。
- **交接对象**：`topic-convergence`、`hypothesis-construction`、`pre-experiment-design`、`grant-and-opening`。

## 工作流

1. 先核对真实的已知边界。需要当前文献时调用 `nature-academic-search`。
2. 分别判断：新现象、新对象或情境、新关系、新机制层次、新方法能力和新转化价值。
3. 每个创新点同时检查科学重要性、可区别于已有工作之处、可验证性和竞争窗口。
4. 如果已有论文部分重叠，定位剩余空间：人群或模型、时间窗、细胞来源、表型深度、机制关系或因果证据。
5. 给出结论：真正的主创新是什么，哪些只是包装，最快需要补哪项证据。

不用“一篇撞题就没创新”“几篇就死亡”之类硬规则，也不拿影响因子替代具体判断。
