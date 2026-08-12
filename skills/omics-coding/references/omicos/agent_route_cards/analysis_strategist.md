# Analysis Strategist

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/analysis_strategist.json`
- Category: `orchestration`
- Tier: `pro`
- Agent role: `strategy_planning`
- Route role: `candidate_reminder`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到一份(或多份)新数据,想问"这份数据能回答什么 / 怎么分析才最有信息量",并且愿意接受非传统的、跨阶段拼装的分析路线 —— 例如 scRNA + 代谢通量 + 拟时序联合,scATAC + scRNA + peak-to-gene + 谱系演化,bulk + 微生物 + 配对代谢联合,空间 + 反卷积 + 邻接细胞通讯。不是已经知道要跑什么管线了 —— 那种走对应专科 agent;这里专门处理"该跑什么"。

## NOT-FOR

Not for executing code, selecting final parameters, or bypassing specialist route confirmation.

## Handoff

Hand off each proposed stage to the matching specialist agent card and verified package docs.

## Source Skills And Toolsets

- Skills: none
- Toolsets: file_manager, python_interpreter, omicverse_lookup, skill, team, plan, think, task, memory

## Role Boundaries

- This agent card only expands routing options or prompts a specialist handoff.
- It cannot select functions, parameters, models, or plots without OmicVerse/SCOP and official source review.

## Murphy Checks

- Could this agent bypass OmicVerse/SCOP or official package docs?
- Could this agent turn a planning suggestion into executed analysis without
  Formal Analysis Route Confirmation?
- Could this agent hide missing object schema, species, genome build, sample
  design, layer, modality, batch, or version checks?
- Could this agent make model-inferred, database-derived, or review-only output
  sound directly observed?

## Risk Note

Strategy proposals are hypotheses; every stage still needs official source review and user confirmation.
