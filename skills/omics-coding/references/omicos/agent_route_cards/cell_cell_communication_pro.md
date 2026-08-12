# Cell-cell Communication Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/cell_cell_communication_pro.json`
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

用于 scRNA-seq 的进阶细胞通讯 / 配体-受体分析：LIANA / LIANA+ consensus、CellPhoneDB v5 兜底、按需 CellChat(R)、条件比较、信号通路排序与差异互作图；只用 CellPhoneDB 的免费路径走 cell_cell_communication_free

## NOT-FOR

Not for unannotated objects, unsupported species databases, or causal signaling claims.

## Handoff

Hand off annotation and preprocessing gaps to single_cell_preprocessor and annotation agents first.

## Source Skills And Toolsets

- Skills: cell-cell-communication, cellchat_rust_h5ad
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory, team

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

Multi-method communication results need database, score, permutation, and visualization semantics checked.
