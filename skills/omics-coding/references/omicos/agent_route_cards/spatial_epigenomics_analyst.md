# Spatial Epigenomics Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/spatial_epigenomics_analyst.json`
- Category: `spatial_analysis`
- Tier: `pro`
- Agent role: `spatial_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到空间分辨的染色质可及性数据 —— AtlasXomics 空间 ATAC / DBiT-seq、tixel×peak 或 tixel×gene-activity 矩阵（带 obsm['spatial'] 坐标），或 fragments + 空间 barcode 布局 —— 要做 QC、降维聚类、空间域、基因活性、chromVAR 转录因子活性、跨切片整合，或样本组间差异可及性/motif 活性。不是 scRNA 空间表达（→ spatial_omics_orchestrator），不是非空间 scATAC（→ single_cell_epigenomics_analyst），不是 bulk ATAC/ChIP（→ bulk_epigenomics_analyst）。

## NOT-FOR

Not for standard spatial transcriptomics when no epigenomic modality is present.

## Handoff

Hand off transcriptomic-only spatial work to spatial_omics_orchestrator.

## Source Skills And Toolsets

- Skills: spatial-epigenomics, spatial-multisample-integration, spatial-pseudobulk, spatial-data-io-loading, spatial-domain-detection, spatial-publication-plots, scatac-chromvar, scatac-peak-to-gene, tf-footprinting, gene-id-conversion, report-html-generation, notebook-export, office-tools
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

Spatial coordinates, epigenomic modality, genome build, feature definition, and registration quality are critical.
