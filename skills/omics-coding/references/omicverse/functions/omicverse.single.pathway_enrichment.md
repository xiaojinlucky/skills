# omicverse.single.pathway_enrichment #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.pathway_enrichment`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.pathway_enrichment.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Perform pathway enrichment analysis on gene expression data.

## Signature

```text
omicverse.single. pathway_enrichment ( adata , pathways_dict , organism = 'Human' , group_by = 'louvain' , cutoff = 0.05 , logfc_threshold = 2 , pvalue_type = 'adjust' , plot = True )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData with rank_genes_groups results and cluster labels.
- `pathways_dict`: ( dict ) – Mapping from pathway/set name to member genes.
- `organism`: ( str ) – Organism name used by enrichment backend.
- `group_by`: ( str ) – adata.obs key used as grouping variable.
- `cutoff`: ( float ) – Significance cutoff for pathway filtering.
- `logfc_threshold`: ( float ) – Minimum log2 fold-change threshold for DE genes.
- `pvalue_type`: ( str ) – P-value type used for final filtering: 'adjust' or 'raw' .
- `plot`: ( bool ) – Whether to draw per-cluster barplots for enriched pathways.

## Full Documentation

# omicverse.single.pathway_enrichment #

omicverse.single. pathway_enrichment ( adata , pathways_dict , organism = 'Human' , group_by = 'louvain' , cutoff = 0.05 , logfc_threshold = 2 , pvalue_type = 'adjust' , plot = True ) [source] #

Perform pathway enrichment analysis on gene expression data.

Parameters :

-
adata ( anndata.AnnData ) – AnnData with `rank_genes_groups `results and cluster labels.

-
pathways_dict ( dict ) – Mapping from pathway/set name to member genes.

-
organism ( str ) – Organism name used by enrichment backend.

-
group_by ( str ) – `adata.obs `key used as grouping variable.

-
cutoff ( float ) – Significance cutoff for pathway filtering.

-
logfc_threshold ( float ) – Minimum log2 fold-change threshold for DE genes.

-
pvalue_type ( str ) – P-value type used for final filtering: `'adjust' `or `'raw' `.

-
plot ( bool ) – Whether to draw per-cluster barplots for enriched pathways.

Returns :

-
pd.DataFrame – Enrichment result table with cluster labels and pathway statistics.

-
Examples – >>> # Perform pathway enrichment analysis on adata using pathways_dict >>> res = pathway_enrichment(adata, pathways_dict)

-
Reference – The code for pathway_enrichment() function was adapted from scanpy workflows: https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html#Gene-set-enrichment-analysis .
