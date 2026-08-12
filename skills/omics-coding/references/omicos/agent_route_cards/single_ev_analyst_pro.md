# Single-EV Proteomics Analyst Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_ev_analyst_pro.json`
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

拿到单个外泌体/EV 分辨率的蛋白测量 (每行=一个囊泡，不是 bulk EV 制备)，要做质控、污染评估、MISEV 标记、单囊泡归一、亚群聚类、共定位、差异分析并出报告

## NOT-FOR

Not for general proteomics without EV isolation/provenance or for vesicle biology claims without markers.

## Handoff

Hand off general proteomics to proteomics_analyst_pro when EV-specific assumptions are absent.

## Source Skills And Toolsets

- Skills: single-ev-proteomics, single-cell-preprocessing, gsea-enrichment, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
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

EV isolation method, marker support, contamination controls, and proteomics missingness determine credibility.
