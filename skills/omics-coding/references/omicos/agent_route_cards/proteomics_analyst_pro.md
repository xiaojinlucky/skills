# Proteomics Analyst Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/proteomics_analyst_pro.json`
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

拿到蛋白丰度矩阵(MaxQuant proteinGroups / DIA-NN report / FragPipe combined_protein / Olink NPX / 通用 protein×sample 表),或肽段级 MSstats 长表,要做 QC、缺失值处理、差异表达、通路富集、出报告

## NOT-FOR

Not for RNA expression analysis or metabolomics unless paired proteomics is part of the design.

## Handoff

Hand off paired transcriptome, metabolome, or EV-specific steps to the matching route card.

## Source Skills And Toolsets

- Skills: bulk-proteomics, multi-omics-integration, gsea-enrichment, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
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

Quantification scale, missingness, normalization, peptide-to-protein rollup, and batch correction are route-defining.
