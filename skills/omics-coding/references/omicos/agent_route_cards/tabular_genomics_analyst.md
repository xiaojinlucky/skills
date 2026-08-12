# Tabular Genomics Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/tabular_genomics_analyst.json`
- Category: `general_omics_analysis`
- Tier: `pro`
- Agent role: `general_omics_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到 tidy 数据表、直接在表上做统计 —— 临床表型表、per-sample 标量汇总(纯度 / 评分 / 签名分数等单值列)、MAF/突变表,**或已经算好的结果表(DE 结果表、每特征 / 每条件 / 每组织的统计量或 score 表)**。做关联 / 相关 / 偏相关检验、交互效应、亚组比例;**跨集合 / 跨条件的相关与相似度(overlap / Jaccard)及其聚合**;体细胞突变的频率 / TMB / 富集 / 共现 / 通路聚合。**关键判据:输入本身就是表格、你直接在表上统计,不需要从一个基因 × 样本表达矩阵建模。** 一个**整个表达矩阵(数千基因 × 样本)**的基因-性状关联**不归这里** —— 即使措辞是"哪些基因与 X 相关",只要输入是表达矩阵、要从中推导差异表达,那是 RNA-seq 任务,交给 bulk_rna_analyst。也不是 counts 矩阵的差异表达,不是单变异功能效应预测。**也不是 DNA 甲基化 / 表观基因组的区域分析** —— per-CpG 甲基化 beta 矩阵、差异甲基化(DMC/DMR)、启动子 / 基因体 / enhancer / CpG island 的甲基化、或甲基化随基因组距离的分布,需要基因组坐标 / 区域注释 / 表观遗传学判断(enhancer 用激活标记而非抑制标记、覆盖度过滤等),即使输入是 (chr,start)×样本的矩阵或多组学整合也不归这里,交给 bulk_epigenomics_analyst。

## NOT-FOR

Not for raw omics matrices that need preprocessing, normalization, differential testing, or modeling.

## Handoff

Hand off raw matrices to the data-type specialist before using table-level statistics.

## Source Skills And Toolsets

- Skills: tabular-association-analysis, somatic-mutation-analysis, survival-analysis, multi-omics-integration, gene-id-conversion, data-io-loading, data-cleaning, gsea-enrichment, figure-programmatic, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory

## Role Boundaries

- Use this agent card as routing and handoff help only after OmicVerse/SCOP and official docs are checked.
- It cannot override function docs, parameter docs, package versions, visualization gates, or route confirmation.

## Murphy Checks

- Could this agent bypass OmicVerse/SCOP or official package docs?
- Could this agent turn a planning suggestion into executed analysis without
  Formal Analysis Route Confirmation?
- Could this agent hide missing object schema, species, genome build, sample
  design, layer, modality, batch, or version checks?
- Could this agent make model-inferred, database-derived, or review-only output
  sound directly observed?

## Risk Note

Use only for existing result tables; raw expression, count, intensity, or peak matrices need specialist routes.
