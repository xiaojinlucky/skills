# Phylogenomics Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/phylogenomics_analyst.json`
- Category: `phylogenomics`
- Tier: `plus`
- Agent role: `phylogenomics_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

用户提到 multiple sequence alignment / 系统发生树 / phylogeny / phylogenomics / gene tree / species tree / polytomy / rapid radiation / mirror tree / treeness / RCV / LB score / parsimony informative sites / 饱和度 / saturation / MSA 准确性 / sum-of-pairs / column score。或者用户上传了 `.fa` / `.fasta` / `.aln.fa` / `.tre` / `.treefile` / `.newick` 文件请求分析。

## NOT-FOR

Not for generic gene-list enrichment, expression analysis, or structure modeling without phylogenomic inputs.

## Handoff

Hand off expression or pathway interpretation to bulk, single-cell, or enrichment route cards.

## Source Skills And Toolsets

- Skills: phykit-alignment-quality, phykit-tree-quality, phykit-gene-tree-discordance, phykit-trait-history, phykit-phylogenetic-signal, phykit-trait-ordination, phykit-phylogenetic-regression, phykit-trait-evolution-models, phykit-phylo-visualization
- Toolsets: file_manager, python_interpreter, shell, notebook, omicverse_lookup, team, plan, think, task, skill, memory

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

Orthology, alignment, tree model, genome build, and taxon sampling drive phylogenomic conclusions.
