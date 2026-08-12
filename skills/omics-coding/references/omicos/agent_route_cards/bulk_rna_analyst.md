# Bulk RNA-seq Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/bulk_rna_analyst.json`
- Category: `general_omics_analysis`
- Tier: `community`
- Agent role: `general_omics_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到 bulk RNA-seq 表达矩阵(genes × samples,counts/TPM)、多批次队列、TCGA、FASTQ —— 需要你从这个矩阵建模 / 推导。"哪些基因与某个样本变量相关 / 关联 / 差异表达"的问题归这里:变量是分组、连续性状(病程 / 年龄 / 剂量 / 严重度评分)、还是时间点都一样 —— 差异表达就是把表达矩阵建模为一个 design matrix 的函数,连续协变量只是 design 里的一列,措辞是 "correlation / associated with / track" 不改变这一点。**关键判据:输入确实是一个基因 × 样本的表达矩阵、分析要从中建模。** 若输入已经是算好的结果表(DE 结果表、每特征 / 每条件的统计量或 score 表),任务只是在这些表上做相关 / 相似度 / 聚合,那是表格统计,归 tabular_genomics_analyst。也做富集 / 共表达网络 / 报告。

## NOT-FOR

Not for raw scRNA matrices, generic result-table statistics, or spatial transcriptomics downstream.

## Handoff

Hand off scRNA to single_cell_preprocessor and existing result tables to tabular_genomics_analyst.

## Source Skills And Toolsets

- Skills: gene-id-conversion, data-io-loading, data-cleaning, sample-metadata-alignment, tcga-preprocessing, survival-analysis, bulk-combat-correction, bulk-deg-analysis, time-course-analysis, multi-omics-integration, sample-clustering, gsea-enrichment, bulk-wgcna-analysis, bulk-stringdb-ppi, bulk-celltype-deconvolution, bulk-to-single-deconvolution, report-html-generation, notebook-export, office-tools
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory

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

Counts versus TPM, design matrix, contrasts, batch variables, and replicate structure define the valid route.
