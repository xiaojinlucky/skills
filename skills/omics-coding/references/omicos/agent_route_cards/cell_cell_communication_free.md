# Cell-cell Communication Free

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/cell_cell_communication_free.json`
- Category: `single_cell_analysis`
- Tier: `community`
- Agent role: `single_cell_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

用于已注释 scRNA-seq AnnData 的免费版细胞通讯 / 配体-受体分析，CellPhoneDB v5 够用时走这里；不跑 LIANA consensus、LIANA+、CellChat(R) 或手写兜底统计

## NOT-FOR

Not for unannotated objects, unsupported species databases, or causal signaling claims.

## Handoff

Hand off annotation and preprocessing gaps to single_cell_preprocessor and annotation agents first.

## Source Skills And Toolsets

- Skills: cell-cell-communication-free
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, team

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

Communication scores are expression-derived inference; sender, receiver, database, and plot semantics need review.
