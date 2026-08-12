# Bulk Epigenomics Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/bulk_epigenomics_analyst.json`
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

拿到 bulk 表观基因组数据。两类:(1) 染色质可及性 / 占据 —— ATAC-seq / ChIP-seq / CUT&RUN 的 FASTQ.gz、BAM、narrowPeak 或 bigWig,做上游、call peak、差异 peak、TF 足迹、轨道、motif 富集(走 epione);(2) DNA 甲基化 / WGBS / RRBS —— per-CpG beta 矩阵或 methylation BED/bedGraph(beta 0-1 或 0-100),做区域甲基化(启动子 / 基因体 / enhancer / CpG island)、条件间差异甲基化、或甲基化在某特征周围的空间分布(走标准栈,epione 无甲基化模块)。不是单细胞 ATAC(→ single_cell_epigenomics_analyst),不是 Hi-C(→ chromatin_3d_analyst),不是纯 RNA 表达(→ bulk_rna_analyst)。

## NOT-FOR

Not for single-cell ATAC, spatial epigenomics, or structural variant interpretation without a matching specialist route.

## Handoff

Hand off single-cell epigenomics to single_cell_epigenomics_analyst and spatial assays to spatial_epigenomics_analyst.

## Source Skills And Toolsets

- Skills: bulk-epigenome-upstream, differential-peak-analysis, dna-methylation-analysis, tf-footprinting, epigenome-track-visualization, gsea-enrichment, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export, office-tools, retraction-check
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

Assay type, genome build, feature definition, normalization, and peak or bin provenance define valid conclusions.
