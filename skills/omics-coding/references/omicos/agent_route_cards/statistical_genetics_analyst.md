# Statistical Genetics Analyst

- Source OmicOS agent JSON: `../raw_agents/public_cloud_agents/statistical_genetics_analyst.json`
- Category: `general_omics_analysis`
- Tier: `plus`
- Agent role: `general_omics_analysis`
- Route role: `route_card`
- Primary authority: OmicVerse/SCOP function docs plus official package/tutorial docs
- Official confirmation: `always`

OmicOS agent is not an authority layer. Use this card only as an internal
routing and handoff reminder after OmicVerse/SCOP and official docs have been
checked.

## Use When

拿到 GWAS summary statistics、基因型数据(PLINK .bed/.bim/.fam、VCF、dosage 矩阵),或要做 eQTL 定位、精细定位(credible set / PIP)、GWAS 与 eQTL 共定位、孟德尔随机化(暴露→结局的因果)、TWAS、SNP 遗传力 / 遗传相关(LD score regression)、scDRS 找疾病相关细胞类型。不是体细胞 / 癌症突变表的频率·富集分析(→ tabular_genomics_analyst),不是蛋白氨基酸突变的功能 / 致病效应(→ variant_analyst),不是表达矩阵的差异表达(→ bulk_rna_analyst)。

## NOT-FOR

Not for expression-matrix DEG or pathway analysis when no genetic association data are present.

## Handoff

Hand off downstream expression or functional interpretation to the matching omics specialist route.

## Source Skills And Toolsets

- Skills: gwas-eqtl-analysis, gene-id-conversion, data-io-loading, sample-metadata-alignment, gsea-enrichment, figure-programmatic, report-html-generation, notebook-export, office-tools
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

Genome build, ancestry, LD reference, covariates, variant QC, and multiple testing define valid inference.
