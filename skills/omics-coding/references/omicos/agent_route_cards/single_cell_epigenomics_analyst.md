# Single-Cell Epigenomics Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_epigenomics_analyst.json`
- Category: `single_cell_analysis`
- Tier: `pro`
- Agent role: `single_cell_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到单细胞 ATAC-seq 数据 —— fragments 文件、10x scATAC 输出、cell×peak 或 cell×tile 矩阵 —— 要做 QC、降维聚类、基因活性打分、簇级 call peak、chromVAR 转录因子活性、peak-to-gene 调控连接、多样本整合或从 scRNA 迁移细胞类型标签。不是 bulk ATAC/ChIP/CUT&RUN(→ bulk_epigenomics_analyst),不是单细胞 Hi-C(→ chromatin_3d_analyst),不是 scRNA 表达分析(→ single_cell 注释类 agent)。

## NOT-FOR

Not for scRNA-only workflows or bulk epigenomics without single-cell epigenomic data.

## Handoff

Hand off paired scRNA integration to single_cell_preprocessor or single-multiomics skill routes as needed.

## Source Skills And Toolsets

- Skills: scatac-preprocessing, scatac-chromvar, scatac-peak-to-gene, scatac-integration, tf-footprinting, gsea-enrichment, gene-id-conversion, data-io-loading, figure-programmatic, single-cell-publication-plots, report-html-generation, notebook-export, office-tools
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

Peak set, genome build, fragments, modality pairing, and accessibility normalization determine interpretability.
