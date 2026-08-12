# Chromatin 3D Genome Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/chromatin_3d_analyst.json`
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

拿到 Hi-C / 三维基因组数据 —— bulk 接触矩阵(.cool/.mcool)、pairs 文件,或单细胞 / droplet Hi-C(.scool、per-cell .cool)—— 要分析基因组三维结构:A/B 区室、TAD 结构域、染色质 loop、接触频率衰减,或单细胞层面的 3D 基因组细胞状态 / 细胞周期。不是 bulk ATAC/ChIP/CUT&RUN(→ bulk_epigenomics_analyst),不是 scATAC(→ single_cell_epigenomics_analyst)。

## NOT-FOR

Not for ordinary bulk epigenomics or single-cell epigenomics when no 3D chromatin data are present.

## Handoff

Hand off non-3D epigenomics to bulk_epigenomics_analyst or single_cell_epigenomics_analyst.

## Source Skills And Toolsets

- Skills: hic-analysis, single-cell-hic-analysis, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export, office-tools
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

Resolution, genome build, binning, normalization, and loop or domain caller choices determine interpretation.
