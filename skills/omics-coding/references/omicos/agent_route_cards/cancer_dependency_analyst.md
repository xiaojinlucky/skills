# Cancer Dependency Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/cancer_dependency_analyst.json`
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

拿到癌症依赖 / 必需性数据 —— DepMap/CCLE 的 CRISPR/RNAi 必需性评分、患者层面预测依赖评分、突变矩阵 + 多组学 —— 要找某癌种的选择性依赖 / 生物标志物 / 可干预靶点,或预测某 LOF 事件的合成致死伙伴,或判定某一对具名基因是否合成致死(仅给基因名 + 上下文、需自己取依赖数据也可)。不是普通 RNA-seq 差异表达(→ bulk_rna_analyst),不是体细胞突变频率统计(→ tabular_genomics_analyst),不是 GWAS / eQTL(→ statistical_genetics_analyst)。

## NOT-FOR

Not for unvalidated causal claims or clinical actionability without external evidence.

## Handoff

Hand off expression, mutation, or pathway-specific substeps to the relevant omics route card.

## Source Skills And Toolsets

- Skills: cancer-dependency-analysis, synthetic-lethality-discovery, target-druggability-pro, somatic-mutation-analysis, tabular-association-analysis, gsea-enrichment, gene-id-conversion, data-io-loading, data-cleaning, figure-programmatic, report-html-generation, notebook-export, office-tools, retraction-check
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

Screen design, dependency score model, lineage covariates, and batch structure must be declared before claims.
