# omicverse.space.calculate_gene_signature #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.calculate_gene_signature`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.calculate_gene_signature.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a marker-gene signature table for each cell type in a reference scRNA-seq dataset.

## Signature

```text
omicverse.space. calculate_gene_signature ( adata_sc , clustertype , rank = True , key = 'rank_genes_groups' , foldchange = 2 , topgenenumber = 20 )
```

## Parameters

- `adata_sc`: ( AnnData ) – Single-cell reference AnnData.
- `clustertype`: ( str ) – Cell-type label key in adata_sc.obs .
- `rank`: ( bool ) – Whether to use ranked markers from differential expression analysis.
- `key`: ( str ) – adata.uns key for ranked genes (used when rank=True ).
- `foldchange`: ( float ) – Fold-change threshold for marker selection.
- `topgenenumber`: ( int ) – Number of top marker genes retained per cell type.

## Full Documentation

# omicverse.space.calculate_gene_signature #

omicverse.space. calculate_gene_signature ( adata_sc , clustertype , rank = True , key = 'rank_genes_groups' , foldchange = 2 , topgenenumber = 20 ) [source] #

Build a marker-gene signature table for each cell type in a reference scRNA-seq dataset.

Parameters :

-
adata_sc ( AnnData ) – Single-cell reference AnnData.

-
clustertype ( str ) – Cell-type label key in `adata_sc.obs `.

-
rank ( bool ) – Whether to use ranked markers from differential expression analysis.

-
key ( str ) – `adata.uns `key for ranked genes (used when `rank=True `).

-
foldchange ( float ) – Fold-change threshold for marker selection.

-
topgenenumber ( int ) – Number of top marker genes retained per cell type.

Returns :

Gene-signature matrix where each column corresponds to one cell type and each cell stores a marker gene (padded with NA when needed).

Return type :

pandas.DataFrame

Examples

```text
>>> gene_sig = ov.space.calculate_gene_signature(adata_sc, clustertype='celltype', topgenenumber=50)

```
