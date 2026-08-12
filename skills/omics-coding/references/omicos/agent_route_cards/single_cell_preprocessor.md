# Single-cell Preprocessor

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_preprocessor.json`
- Category: `single_cell_analysis`
- Tier: `plus`
- Agent role: `single_cell_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到 raw / 已 QC 的 scRNA-seq AnnData，要清洗 + 标准化 + 聚类 + 取 marker，输出 ready-to-annotate 的 adata.h5ad。若手上只有原始 FASTQ 还没有矩阵：带 barcode+UMI 的液滴/微孔化学（10x、Drop-seq、inDrops、CEL-seq、SPLiT-seq 等）先走 single-cell-kb-alignment、plate-based Smart-seq2/3 先走 single-cell-smartseq-quantification 比对定量成矩阵，再回到本流水线

## NOT-FOR

Not for bulk RNA-seq, spatial objects, final annotation claims, or downstream biology without specialist handoff.

## Handoff

Hand off ready-to-annotate objects to annotation, communication, trajectory, GRN, or downstream route cards.

## Source Skills And Toolsets

- Skills: single-cell-kb-alignment, single-cell-smartseq-quantification, data-io-loading, rds-qs-seurat-ingestion, gene-id-conversion, single-cell-preprocessing, single-cell-ambient-rna, single-cell-batch-integration, single-cell-clustering-backends, single-cell-composition, single-cell-pseudobulk, single-cell-genemodule, gsea-enrichment, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export, office-tools
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

QC thresholds, normalization, HVG, PCA, integration, neighbors, and clustering must be planned before running.
