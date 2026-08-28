---
name: meta-sci-init
description: Run an interactive zero-to-one research opening workflow for a new biomedical, bioinformatics, single-cell, multi-omics, or experimental project. Use when the user has only a broad direction, dataset, clinical phenomenon, technical capability, or preliminary anomaly and wants to reach a research question, literature map, hypothesis, preliminary plan, opening report structure, and defense outline. This is a composite opening workflow, not a second general orchestrator.
---

# Meta Sci Init

把一个模糊起点推进到能开题的第一版研究方案，但只负责“从零到一”这一段。

## 必读

本任务尚未加载时，读 `~/.codex-shared/suites/research-master/shared/research-core.md`、`~/.codex-shared/suites/research-master/shared/routing-and-authority.md`、`~/.codex-shared/suites/research-master/shared/research-state.md` 和 `~/.codex-shared/suites/research-master/shared/expression-core.md`；已经记录在 `loaded_resources` 中就直接复用。

## 合同

- **进入条件**：新课题只有宽方向、数据、现象、技术或异常，尚未形成可开题的问题和路线。
- **唯一负责的决定**：组织从起点到第一版开题方案的阶段顺序和交付物。
- **退出条件**：形成研究问题、文献边界、候选假设、最小预实验、开题骨架和答辩问题清单。
- **交接对象**：按需要调用 `research-entry`、`literature-mining`、`topic-convergence`、`innovation-judgment`、`hypothesis-construction`、`pre-experiment-design`、`grant-and-opening`。

## 工作流

1. 读取现有材料，恢复用户起点、资源、边界和期限。若起点包含用户自己的数据、异常或初步信号，先由这些证据无偏地产生候选；文献先划定已知空间、提供发现路径和寻找 GAP，不把已发表 biological answer 预填为开题候选。
2. 按实际缺口调用全部相关专业 skill，不设数量上限；已有环节直接复用，不重复问。只有用户明确要求复现、验证、benchmark、外部验证或挑战既有结论时，才把论文结论作为直接验证对象。
3. 每完成一段就更新共享科研状态，前一段的结论作为后一段输入。
4. 输出第一版开题交付：一句话问题、已知边界、核心假设、研究目标、关键路线、最小预实验和答辩风险点。

不承担项目全生命周期调度；课题进入正式执行或跨阶段重排后交给 `meta-research-hub`。

## 长稿能力（按需读取，未丢弃）

短合同是正式入口。原始开题向导里多出来的流程没有删，放到 `references/`，用到再读，以后可以再删减。

| 用户要做什么 | 读取 |
|---|---|
| 交互式开题：问诊、联网调研、推荐 5 个选题、定题、假设与方案、逐节写开题报告 | `references/opening-playbook.md`，并按其中指引读同目录其它卡片 |
| 选题怎么从文献收成 5 个可判断选项 | `references/topic_recommendation.md` |
| 前期基础如何落到假设、Aim 和实验方案 | `references/hypothesis_and_design.md`、`references/research_model.md` |
| 开题报告章节骨架 | `references/proposal_structure.md` |
| 明确说了要做开题答辩 PPT | `references/ppt-generation.md`、`references/ppt_structure.md`；脚本在 `scripts/build_pptx.py` |
| 需要对照或抽回 2026-08-11 原始长稿全文 | `references/archive-original-SKILL.md` |

调用专业 skill 仍然服从上面的短合同和创新隔离墙。长稿负责把「从零到一」走成可交付的开题报告，不能改写 `research-core.md` 的事实边界。
