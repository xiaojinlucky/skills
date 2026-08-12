---
name: literature-mining
description: Mine biomedical and bioinformatics literature for research designs, screening logic, mechanisms, transferable experiments, contradictions, and open questions rather than merely collecting conclusions. Use when the user wants to learn how studies were conceived, build an idea bank, compare research routes, discover a project entry point, or turn a literature body into testable directions. Delegate real retrieval and citation verification to nature-academic-search.
---

# Literature Mining

读文献不是攒结论，而是拆别人怎样把问题一步步做出来。

## 必读

本任务尚未加载时，读 `../../suites/research-master/shared/research-core.md`、`../../suites/research-master/shared/routing-and-authority.md`、`../../suites/research-master/shared/expression-core.md`。复杂任务可按 `../../suites/research-master/sources/source-index.json` 读取 `../../suites/research-master/methods/method-cards.md` 的“从阅读到选题”；已加载就直接复用。

## 合同

- **进入条件**：用户已有主题或材料范围，希望挖研究思路、设计路径、矛盾和空白。
- **唯一负责的决定**：从文献中提取可迁移的研究设计与候选切入点，并按价值排序。
- **退出条件**：形成带来源的设计模式、证据缺口和候选问题清单，明确哪一项值得进入方向收敛。
- **交接对象**：`topic-convergence`、`innovation-judgment`、`hypothesis-construction`；单篇或少量论文的研究逻辑拆解交给 `literature-deep-reading`，完整双语、图表就位、来源锚定读本交给 `nature-reader`。

## 工作流

1. 先把检索问题拆成对象、现象、机制层次、模型和证据类型。
2. 如需新增论文、当前引用量或期刊信息，调用 `nature-academic-search` 核实，不能凭记忆补文献。
3. 对每项关键研究提取：真正起点、筛选逻辑、关键转折、决定性对照、作者回避的问题和可迁移做法。
4. 把结果按“已经解决、证据冲突、尚未证明、方法上可进入”分类。
5. 输出少而清楚的候选方向：它解决什么问题、依赖什么资源、最小验证是什么、最可能在哪一步被否定。

不设固定文献数量。文献量由问题覆盖度决定，不用影响因子或论文篇数替代科学判断。
