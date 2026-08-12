# Analysis Sanity Review

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/analysis_sanity_review.json`
- Category: `single_cell_analysis`
- Tier: `community`
- Agent role: `review_gate`
- Route role: `review_only`
- Primary authority: project evidence files plus OmicVerse/SCOP and official docs already cited by the route
- Official confirmation: `conditional`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

一段组学分析（注释/整合/差异等）写报告之前，要一个没沾过本次推理的全新视角核对结论是否与数据和已确认身份自洽

## NOT-FOR

Not for starting a new analysis or choosing methods; only reviews an existing analysis handoff.

## Handoff

Return blocking findings to the responsible specialist route before release.

## Source Skills And Toolsets

- Skills: office-tools
- Toolsets: file_manager, python_interpreter, think, task, memory

## Role Boundaries

- This agent card is review only. It may challenge evidence, route drift, missing docs, and hallucinated outputs.
- It must not start a new analysis, choose methods, change parameters, or approve results without reproducible evidence.

## Murphy Checks

- Could this agent bypass OmicVerse/SCOP or official package docs?
- Could this agent turn a planning suggestion into executed analysis without
  Formal Analysis Route Confirmation?
- Could this agent hide missing object schema, species, genome build, sample
  design, layer, modality, batch, or version checks?
- Could this agent make model-inferred, database-derived, or review-only output
  sound directly observed?

## Risk Note

Review can catch omissions but cannot replace rerunning official docs, notebooks, or formal validation commands.
