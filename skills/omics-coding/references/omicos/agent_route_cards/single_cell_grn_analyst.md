# Single-cell GRN Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_grn_analyst.json`
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

用于单细胞基因调控网络推断、TF-靶基因边表、GRNBoost2/GENIE3/RegDiffusion 先验、SCENIC regulon、AUCell/RSS，或为 RegVelo 准备先验 GRN；若要扰动基因或 TF regulon，用 single_cell_perturbation_analyst

## NOT-FOR

Not for causal TF claims without motif/resource support and sensitivity checks.

## Handoff

Hand off preprocessing and annotation gaps before GRN inference.

## Source Skills And Toolsets

- Skills: single-cell-grn-inference, gene-id-conversion, geneset-scoring, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task

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

GRN outputs depend on species resources, motif database, expression scale, and regulator filtering.
