# CellChat Rust H5AD Runner

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/cellchat_rust_h5ad_runner.json`
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

Use for cell-cell / ligand-receptor communication analysis on single-cell RNA-seq — LIANA (Python, ov.single.run_liana, consensus + permutation test) or CellChat (R) inference, directed sender→receiver questions, signaling-pathway ranking, condition comparison, and differential interaction plots. Accepts an annotated h5ad directly, or raw / unannotated scRNA-seq (text matrices, mtx, unlabeled h5ad) by delegating preprocessing and cell-type annotation to the appropriate specialists first.

## NOT-FOR

Not for CellChat interpretation when the h5ad schema, species, or cell labels are unconfirmed.

## Handoff

Hand off schema and annotation issues before running communication inference.

## Source Skills And Toolsets

- Skills: cell-cell-communication, cellchat_rust_h5ad
- Toolsets: file_manager, python_interpreter, shell, plan, think, task, skill, memory, team

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

H5AD schema, species database, cell labels, and CellChat wrapper version control the output semantics.
