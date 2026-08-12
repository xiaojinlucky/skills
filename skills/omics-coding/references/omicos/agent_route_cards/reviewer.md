# Reviewer

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/reviewer.json`
- Category: `general_omics_analysis`
- Tier: `community`
- Agent role: `review_gate`
- Route role: `review_only`
- Primary authority: project evidence files plus OmicVerse/SCOP and official docs already cited by the route
- Official confirmation: `conditional`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

由 review 编排在一次分析回合结束后自动 spawn，传入指向本回合对话记录的指针，用一个没参与过本次推理的全新视角复核结论与产物。不作为根 agent 直接调用、也不承接新分析任务；正常分析请求请路由到对应的专家。

## NOT-FOR

Not for direct user routing, new analysis execution, or method selection.

## Handoff

Return pass, warning, or fail findings to the responsible route owner before release.

## Source Skills And Toolsets

- Skills: none
- Toolsets: file_manager, python_interpreter, think

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

Independent review reduces hallucination risk but does not replace reproducible commands or source verification.
