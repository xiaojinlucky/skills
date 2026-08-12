# omicverse.space.merge_cluster #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.merge_cluster`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.merge_cluster.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Merge clusters based on hierarchical clustering of their representation.

## Signature

```text
omicverse.space. merge_cluster ( adata , groupby = 'mclust' , use_rep = 'STAGATE' , threshold = 0.05 , plot = True , start_idx = 0 , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing existing cluster labels and embeddings.
- `groupby`: ( str , default='mclust' ) – Cluster label column in adata.obs to merge.
- `use_rep`: ( str , default='STAGATE' ) – Embedding key in adata.obsm used for dendrogram distance.
- `threshold`: ( float , default=0.05 ) – Hierarchical-clustering distance threshold for merging.
- `plot`: ( bool , default=True ) – Whether to display dendrogram with threshold line.
- `start_idx`: ( int , default=0 ) – Index offset applied to original cluster IDs before remapping.
- `**kwargs`: – Extra arguments passed to scanpy.pl.dendrogram .

## Full Documentation

# omicverse.space.merge_cluster #

omicverse.space. merge_cluster ( adata , groupby = 'mclust' , use_rep = 'STAGATE' , threshold = 0.05 , plot = True , start_idx = 0 , ** kwargs ) [source] #

Merge clusters based on hierarchical clustering of their representation.

This function performs hierarchical clustering on existing clusters and merges them based on a distance threshold. It can optionally visualize the dendrogram showing the merging process.

Parameters :

-
adata ( AnnData ) – AnnData containing existing cluster labels and embeddings.

-
groupby ( str , default='mclust' ) – Cluster label column in `adata.obs `to merge.

-
use_rep ( str , default='STAGATE' ) – Embedding key in `adata.obsm `used for dendrogram distance.

-
threshold ( float , default=0.05 ) – Hierarchical-clustering distance threshold for merging.

-
plot ( bool , default=True ) – Whether to display dendrogram with threshold line.

-
start_idx ( int , default=0 ) – Index offset applied to original cluster IDs before remapping.

-
**kwargs – Extra arguments passed to `scanpy.pl.dendrogram `.

Returns :

-
dict – Mapping from original cluster id to merged cluster label.

-
Notes –

-
The function uses scipy’s hierarchical clustering implementation

-
Merged clusters are stored in adata.obs[f’{groupby}_tree’]

-
The dendrogram is stored in adata.uns[f’dendrogram_{groupby}’]

-
Cluster labels in the output are prefixed with ‘c’

-
Examples – >>> import scanpy as sc >>> import omicverse as ov >>> adata = sc.read_h5ad(‘clustered_data.h5ad’) >>> # Merge clusters using STAGATE representation >>> cluster_map = ov.space.merge_cluster(adata, … groupby=’leiden’, … use_rep=’STAGATE’, … threshold=0.1) >>> # Access merged clusters >>> print(adata.obs[‘leiden_tree’])
