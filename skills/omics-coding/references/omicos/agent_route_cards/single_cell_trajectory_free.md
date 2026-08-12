# Single-cell Trajectory Free

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/single_cell_trajectory_free.json`
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

用于已准备好的单细胞 AnnData 的免费版拟时序 / 分支分析，PAGA/DPT 或 Monocle 风格轨迹够用时走这里；需要 velocity、CellRank、Palantir、Slingshot、scTour、VIA/StaVIA 或多方法对比，用 single_cell_trajectory_pro

## NOT-FOR

Not for unrelated clustering or final lineage claims without root, topology, and marker validation.

## Handoff

Hand off preprocessing and annotation prerequisites before trajectory inference.

## Source Skills And Toolsets

- Skills: single-cell-trajectory-inference-free, single-cell-publication-plots, single-cell-report-authoring
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

Trajectory results depend on root choice, topology, batch effects, cell cycle, and method assumptions.
