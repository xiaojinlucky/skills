# omicverse.single.get_celltype_marker #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.get_celltype_marker`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.get_celltype_marker.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Get marker genes for each cluster/cell type.

## Signature

```text
omicverse.single. get_celltype_marker ( adata , clustertype = 'leiden' , log2fc_min = 2 , scores_type = 'scores' , pval_cutoff = 0.05 , rank = True , key = 'rank_genes_groups' , method = 'wilcoxon' , foldchange = None , topgenenumber = 10 , unique = True , global_unique = False , use_raw = None , layer = None , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData containing cluster annotations and expression matrix.
- `clustertype`: ( str ) – Column in adata.obs used to define groups.
- `log2fc_min`: ( int ) – Minimum log2 fold-change threshold when extracting DE markers.
- `scores_type`: ( str ) – Statistic field used for thresholding (for example 'scores' ).
- `pval_cutoff`: ( float ) – Maximum adjusted p-value cutoff for retained markers.
- `rank`: ( bool ) – Whether to run sc.tl.rank_genes_groups before extraction.
- `key`: ( str ) – Key in adata.uns storing ranked-gene results.
- `method`: ( str ) – Differential-expression method for rank_genes_groups .
- `foldchange`: ( float or None ) – Optional manual score threshold; auto-derived when None .
- `topgenenumber`: ( int ) – Maximum number of markers retained per cluster.
- `unique`: ( bool ) – Whether to deduplicate markers within each cluster.
- `global_unique`: ( bool ) – Whether to enforce uniqueness across all clusters.
- `use_raw`: ( Optional [ bool ] ) – Forwarded to rank_genes_groups to control raw usage.
- `layer`: ( Optional [ str ] ) – Layer passed to rank_genes_groups .
- `**kwargs`: – Additional keyword arguments for rank_genes_groups .

## Full Documentation

# omicverse.single.get_celltype_marker #

omicverse.single. get_celltype_marker ( adata , clustertype = 'leiden' , log2fc_min = 2 , scores_type = 'scores' , pval_cutoff = 0.05 , rank = True , key = 'rank_genes_groups' , method = 'wilcoxon' , foldchange = None , topgenenumber = 10 , unique = True , global_unique = False , use_raw = None , layer = None , ** kwargs ) [source] #

Get marker genes for each cluster/cell type.

Parameters :

-
adata ( anndata.AnnData ) – AnnData containing cluster annotations and expression matrix.

-
clustertype ( str ) – Column in `adata.obs `used to define groups.

-
log2fc_min ( int ) – Minimum log2 fold-change threshold when extracting DE markers.

-
scores_type ( str ) – Statistic field used for thresholding (for example `'scores' `).

-
pval_cutoff ( float ) – Maximum adjusted p-value cutoff for retained markers.

-
rank ( bool ) – Whether to run `sc.tl.rank_genes_groups `before extraction.

-
key ( str ) – Key in `adata.uns `storing ranked-gene results.

-
method ( str ) – Differential-expression method for `rank_genes_groups `.

-
foldchange ( float or None ) – Optional manual score threshold; auto-derived when `None `.

-
topgenenumber ( int ) – Maximum number of markers retained per cluster.

-
unique ( bool ) – Whether to deduplicate markers within each cluster.

-
global_unique ( bool ) – Whether to enforce uniqueness across all clusters.

-
use_raw ( Optional [ bool ] ) – Forwarded to `rank_genes_groups `to control raw usage.

-
layer ( Optional [ str ] ) – Layer passed to `rank_genes_groups `.

-
**kwargs – Additional keyword arguments for `rank_genes_groups `.

Returns :

Dictionary mapping cluster labels to marker gene lists.

Return type :

dict
