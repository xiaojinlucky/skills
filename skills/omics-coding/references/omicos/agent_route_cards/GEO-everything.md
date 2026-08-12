# GEO Everything

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/GEO-everything.json`
- Category: `data_acquisition`
- Tier: `pro`
- Agent role: `data_acquisition`
- Route role: `route_card`
- Primary authority: public archive docs plus OmicVerse/SCOP data-loading docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

想从 NCBI GEO / SRA / ENA / DDBJ / GSA 拉公共数据 —— 入口可以是关键词、GSE/GSM/SRR/PRJNA accession、或一篇论文的 DOI / PMID;做的是搜索数据集、解析样本元数据、下载 FASTQ/补充文件、按论文反查 accession。NOT-FOR(数据落地之后的分析不归本 agent):不做 scRNA/10x 的 QC / 归一化 / HVG / PCA / 整合 / 聚类 / 注释(这条链给 single_cell_preprocessor,它再串注释与下游)、不做 bulk 差异表达(→ bulk_rna_analyst)、不做空间下游(→ spatial_omics_orchestrator);本 agent 的职责终点是"FASTQ 落盘 + 样本表解析成 AnnData + 下载报告",随后交棒。若落地的是单细胞**原始 FASTQ**(还没有 gene×cell 矩阵):10x 液滴走 `single-cell-kb-alignment`、plate-based Smart-seq2/3 走 `single-cell-smartseq-quantification` 先比对定量成矩阵,再进 `single_cell_preprocessor`。

## NOT-FOR

Not for QC, normalization, DEG, spatial downstream, or biological interpretation after files are landed.

## Handoff

Hand off landed matrices/files to single-cell, bulk, spatial, microbiome, proteomics, or other specialist routes.

## Source Skills And Toolsets

- Skills: geo-sra-search, geo-metadata-fetch, sra-fastq-download, dataset-linkout, data-io-loading, gene-id-conversion, report-html-generation
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, web, plan, think, task, skill, memory

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

Data acquisition stops at files and metadata; downstream analysis must use specialist route cards and official docs.
