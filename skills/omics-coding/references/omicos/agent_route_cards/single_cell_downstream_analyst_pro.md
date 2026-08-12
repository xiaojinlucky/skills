# Single-cell Downstream Analyst Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_downstream_analyst_pro.json`
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

已经有 QC 过 + 已注释的 scRNA-seq AnnData（cell-type 列填好），要做"注释完之后"的功能/差异分析；GRN/SCENIC 请走 single_cell_grn_analyst，基因/RegVelo 扰动请走 single_cell_perturbation_analyst，细胞通讯请走 cell_cell_communication_*，pseudotime 请走 single_cell_trajectory_*

## NOT-FOR

Not for raw matrix preprocessing or final annotation when those stages are incomplete.

## Handoff

Hand off raw or unannotated objects to preprocessing and annotation route cards first.

## Source Skills And Toolsets

- Skills: single-cell-metabolism-inference, single-cell-composition, single-cell-genemodule, single-cell-pseudobulk, geneset-scoring, gsea-enrichment, gene-id-conversion, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export, office-tools
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

Downstream menus must be split into one verified method per question, not run as an unreviewed bundle.
