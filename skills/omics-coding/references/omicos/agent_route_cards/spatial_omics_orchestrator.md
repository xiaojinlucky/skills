# Spatial Omics Orchestrator

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/spatial_omics_orchestrator.json`
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

拿到 SpaceRanger outs/ 或空间 .h5ad，要做 tissue domain 检测、空间可变基因、scRNA 参考反卷积、空间出图（细胞通讯 / 多切片整合见 Phase 2）

## NOT-FOR

Not for pure scRNA, bulk RNA, or H&E-only prediction without measured or explicitly predicted spatial omics data.

## Handoff

Hand off single-cell reference tasks to single-cell specialists and H&E prediction to he_to_st_predictor first.

## Source Skills And Toolsets

- Skills: spatial-data-io-loading, spatial-domain-detection, spatial-variable-genes, spatial-deconvolution, spatial-publication-plots, gene-id-conversion, report-html-generation, notebook-export, office-tools
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

Platform geometry, image registration, spot or cell resolution, SVGs, deconvolution, and native plots must be confirmed.
