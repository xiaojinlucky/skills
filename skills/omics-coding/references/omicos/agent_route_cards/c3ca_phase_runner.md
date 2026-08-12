# c3CA Phase Runner

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/c3ca_phase_runner.json`
- Category: `single_cell_analysis`
- Tier: `lab`
- Agent role: `single_cell_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

用于 rust-NMF 3CA 前端各 phase、c3CA 后端 MP-analysis 各 phase、phase 间交接，以及单个 phase 的失败排查

## NOT-FOR

Not for generic cell-cycle scoring unless c3CA phase workflow is explicitly intended.

## Handoff

Hand off upstream QC and clustering to single_cell_preprocessor first.

## Source Skills And Toolsets

- Skills: rust_nmf, sc_c3ca_backend_skill
- Toolsets: file_manager, python_interpreter, shell

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

Phase labels depend on preprocessing, marker sets, species, and cell-state confounders.
