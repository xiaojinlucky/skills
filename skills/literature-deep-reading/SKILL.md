---
name: literature-deep-reading
description: Deep-read one or a small set of biomedical, bioinformatics, omics, or mechanism papers to reconstruct the real research origin, logic nodes, evidence chain, unspoken assumptions, avoided weaknesses, transferable design, and better next experiments. Use when preparing journal club, discussing paper logic, learning research design, or comparing a few closely related studies. Use nature-reader for a complete source-grounded full-paper reader and nature-academic-search for retrieval.
---

# Literature Deep Reading

不只看作者讲了什么，还要看每一步为什么这样做、哪条关系其实没有被证明。

## 必读

本任务尚未加载时，读 `../../suites/research-master/shared/research-core.md`、`../../suites/research-master/shared/routing-and-authority.md` 和 `../../suites/research-master/shared/expression-core.md`。按需读 `../../suites/research-master/methods/method-cards.md` 的“从阅读到选题”；已加载就直接复用。

## 合同

- **进入条件**：用户给出一篇或少量论文，想拆研究逻辑、证据强弱、漏洞和可迁移思路。
- **唯一负责的决定**：重建论文真实推理链，并指出最有价值的可迁移设计与未解问题。
- **退出条件**：起点、关键节点、每项主张的证据、替代解释和可改进路线明确。
- **交接对象**：`nature-reader`、`literature-mining`、`hypothesis-construction`、`mechanism-design`。

## 工作流

1. 先核对论文原文、图、补充材料和必要上下文；缺少全文时不能装作完整读过。
2. 逐个 Figure 回答：它解决什么问题，使用什么证据，结论到哪一步。
3. 重建作者没有明说的关键跳步、默认前提、回避的阴性或替代解释。
4. 判断真正的决定性实验和可被削弱的核心边。
5. 提炼用户能带回自己课题的筛选逻辑、实验顺序和改进方案。

输出时把“论文已经得到的生物学结论”和“可迁移的方法与分析体系”明确分开。除非用户明确要求复现或检验某项既有结论，只迁移问题拆解、无偏筛选、分析顺序、证据组织和验证设计；不得把论文结论直接设为用户课题的假设、评分终点或期望答案。迁移后的新结论必须由用户自己的数据产生。

如果用户要逐段双语全文读本，转给 `nature-reader`，不要重复造一套全文解析。
