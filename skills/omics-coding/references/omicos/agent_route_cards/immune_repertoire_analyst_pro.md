# Immune Repertoire Analyst Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/immune_repertoire_analyst_pro.json`
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

拿到 TCR / BCR 测序 (10x V(D)J、AIRR rearrangement、bulk repertoire 表)，要跑克隆型 / 多样性 / 体细胞超突变 / 谱系树 / TCR 特异性分组 / 与转录组联合分析并出报告

## NOT-FOR

Not for ordinary transcriptome annotation unless receptor clonotypes or immune repertoire fields are central.

## Handoff

Hand off paired expression analysis to the single-cell or bulk specialist route.

## Source Skills And Toolsets

- Skills: airr-singlecell, airr-bulk, airr-bcr-immcantation, airr-tcr-specificity, airr-tcr-gex, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
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

Clonotype definition, receptor chain pairing, sample identity, and diversity metrics change the result semantics.
