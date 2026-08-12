# Single-cell Perturbation Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_perturbation_analyst.json`
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

用于单细胞 in-silico KO/KD/OE、scTenifoldKnk、CellOracle、RegVelo TF regulon 阻断、调控扰动、velocity 感知扰动或细胞命运效应分析；只做 GRN 推断用 single_cell_grn_analyst

## NOT-FOR

Not for ordinary differential expression if perturbation design, guide assignment, or controls are absent.

## Handoff

Hand off non-perturbation scRNA tasks to preprocessing and downstream analysis routes.

## Source Skills And Toolsets

- Skills: single-cell-in-silico-perturbation, single-cell-regvelo-perturbation, single-cell-grn-inference, gene-id-conversion, geneset-scoring, gsea-enrichment, single-cell-publication-plots, single-cell-report-authoring, report-html-generation, notebook-export
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, skill, team, plan, think, task, memory

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

Guide calling, perturbation design, replicate structure, controls, and batch define valid perturbation inference.
