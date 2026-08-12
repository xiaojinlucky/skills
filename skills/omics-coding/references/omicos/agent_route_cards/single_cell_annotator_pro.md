# Single-cell Annotator Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_annotator_pro.json`
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

拿到已聚类的 AnnData (`scmarker_preprocessor` 输出 / 任何带 `leiden`/`louvain` 的 .h5ad)，要给每个 cluster 标 cell type，并要可审计的文献证据

## NOT-FOR

Not for final biological labels without marker-level and reference provenance checks.

## Handoff

Hand off poor QC or missing clustering to single_cell_preprocessor before annotation.

## Source Skills And Toolsets

- Skills: celltype-annotation-pro, single-cell-preprocessing, gene-id-conversion, single-cell-composition, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, office-tools, notebook-export
- Toolsets: file_manager, python_interpreter, omicverse_lookup, plan, think, task, skill, memory

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

Consensus or model labels can hide systematic bias; inspect disagreements and marker support.
