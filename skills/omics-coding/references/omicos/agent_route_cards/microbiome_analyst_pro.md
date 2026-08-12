# Microbiome Analyst Pro

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/microbiome_analyst_pro.json`
- Category: `general_omics_analysis`
- Tier: `pro`
- Agent role: `general_omics_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到 16S 测序 (raw FASTQ 或已有 ASV/OTU 表) / 多 cohort 16S / 配对 microbe-metabolite 数据，要跑多样性 + 差异丰度 + 通路 / 元分析 + 出报告。仅限 16S / ITS / 18S 扩增子;NOT-FOR:shotgun / 全基因组 宏基因组(Kraken2 / Bracken / MetaPhlAn / HUMAnN / MAG 组装·分箱)不在本 agent 范围,不要把这类任务路由到这里(目前平台无 shotgun 落点 —— 应向用户说明,而非接下只能 plan-不能-run)。

## NOT-FOR

Not for host transcriptomics or metabolomics unless microbiome features are explicitly modeled.

## Handoff

Hand off paired host or metabolite analysis to the relevant omics integration route.

## Source Skills And Toolsets

- Skills: microbiome-16s-amplicon-dada2, microbiome-phylogeny, microbiome-da-comparison, microbiome-meta-analysis, micro-metabol-paired, data-io-loading, figure-programmatic, single-cell-report-authoring, report-html-generation, notebook-export, office-tools, retraction-check
- Toolsets: file_manager, python_interpreter, shell, omicverse_lookup, plan, think, task, skill, memory

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

Compositionality, zero inflation, taxonomy database, ASV/OTU provenance, and batch effects must be explicit.
