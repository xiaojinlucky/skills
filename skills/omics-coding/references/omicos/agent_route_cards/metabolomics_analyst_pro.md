# Metabolomics Analyst Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/metabolomics_analyst_pro.json`
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

拿到代谢组学 peak intensity 表（MetaboAnalyst CSV / LC-MS / NMR / lipidomics）/ 多 batch 队列 / 配对 microbe-metabolite 数据，要跑预处理 + 统计 + 通路 + 出报告

## NOT-FOR

Not for microbiome-only, transcriptome-only, or proteomics-only analysis without paired metabolomics evidence.

## Handoff

Hand off paired microbiome-metabolomics to the matching multi-omics skill route if used.

## Source Skills And Toolsets

- Skills: bulk-metabol-preprocessing, bulk-metabol-multivariate, bulk-metabol-pathway-multifactor, bulk-metabol-untargeted-lipidomics, micro-metabol-paired, gene-id-conversion, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
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

Feature annotation confidence, imputation, normalization, transformation, and validation design affect every claim.
