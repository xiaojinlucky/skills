---
name: mechanism-design
description: Design a mechanism-study route for biomedical, bioinformatics, omics, molecular, cellular, animal, or translational research. Use when a phenotype or association is established and the user needs to decide which mechanistic layer to test, which pathway or direct target matters, how deep to go, or which experiments can distinguish competing mechanisms. Do not force a transcriptomics-GSEA-Co-IP pipeline or universal thresholds.
---

# Mechanism Design

机制不是实验技术清单。先看你要解释的那条关系，再决定该往哪一层打。

## 必读

本任务尚未加载时，读 `../../suites/research-master/shared/research-core.md`、`../../suites/research-master/shared/routing-and-authority.md`、`../../suites/research-master/shared/research-state.md` 和 `../../suites/research-master/shared/expression-core.md`。按需读 `../../suites/research-master/methods/method-cards.md` 的“从假设到机制”；已加载就直接复用。

## 合同

- **进入条件**：关键表型或关系已有基础证据，需要解释作用过程或直接下游。
- **唯一负责的决定**：选择最能回答当前问题的机制层次、关键节点和实验顺序。
- **退出条件**：机制链每一步的主张、实验、对照、替代解释和停止条件都明确。
- **交接对象**：`causality-rescue`、`pre-experiment-design`、`sci-writing-and-revision`。

## 工作流

1. 写清机制问题：是在找通路、直接靶点、细胞间关系、代谢过程、时空顺序，还是另一类机制。
2. 根据分子属性、细胞环境、已有证据和可用模型选择候选层次。
3. 先做能排除大类替代解释的实验，再进入昂贵或精细的直接机制。
4. 每一层都写明：操纵什么、读出什么、关键对照是什么、怎样区分相关和作用。
5. 到足以支撑核心主张时停止加深；投稿定位或结论确实依赖时才继续补层次。

组学筛选、通路富集、结合实验和遗传操纵都只是工具，不能自动组成一条可信机制链。
