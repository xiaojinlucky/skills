# omicverse.space.clusters #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.clusters`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.clusters.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Perform clustering analysis on spatial transcriptomics data using multiple methods.

## Signature

```text
omicverse.space. clusters ( adata , methods , methods_kwargs , batch_key = None , spatial_key = 'spatial' , lognorm = 500000.0 )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData object to be clustered/embedded.
- `methods`: ( list ) – Ordered list of methods to run, e.g. ['STAGATE', 'GraphST'] .
- `methods_kwargs`: ( dict ) – Method-specific configuration dictionary.
- `batch_key`: ( str , optional ) – Batch/sample key in adata.obs for multi-sample methods.
- `spatial_key`: ( str , default='spatial' ) – Spatial coordinate key in adata.obsm .
- `lognorm`: ( float , default=50*1e4 ) – Target-sum scale used when recovering counts from log-normalized data.

## Full Documentation

# omicverse.space.clusters #

omicverse.space. clusters ( adata , methods , methods_kwargs , batch_key = None , spatial_key = 'spatial' , lognorm = 500000.0 ) [source] #

Perform clustering analysis on spatial transcriptomics data using multiple methods.

This function supports multiple clustering methods including STAGATE, GraphST, CAST, and BINARY. Each method processes the spatial data differently and stores its results in the AnnData object.

Parameters :

-
adata ( AnnData ) – Spatial AnnData object to be clustered/embedded.

-
methods ( list ) – Ordered list of methods to run, e.g. `['STAGATE', 'GraphST'] `.

-
methods_kwargs ( dict ) – Method-specific configuration dictionary.

-
batch_key ( str , optional ) – Batch/sample key in `adata.obs `for multi-sample methods.

-
spatial_key ( str , default='spatial' ) – Spatial coordinate key in `adata.obsm `.

-
lognorm ( float , default=50*1e4 ) – Target-sum scale used when recovering counts from log-normalized data.

Returns :

-
AnnData – Updated AnnData containing method-specific embeddings/layers.

-
Notes –

-
For STAGATE: If n_top_genes is specified, highly variable genes are selected

-
For GraphST: Requires counts matrix in adata.layers[‘counts’]

-
For CAST: Requires spatial coordinates in adata.obsm[‘spatial’]

-
For BINARY: Can handle both raw counts and normalized data

-
Examples – >>> import scanpy as sc >>> import omicverse as ov >>> adata = sc.read_h5ad(‘spatial_data.h5ad’) >>> methods = [‘STAGATE’, ‘GraphST’] >>> methods_kwargs = { … ‘STAGATE’: {‘num_batch_x’: 3, ‘num_batch_y’: 2}, … ‘GraphST’: {‘device’: ‘cuda:0’, ‘n_pcs’: 30} … } >>> adata = ov.space.clusters(adata, methods, methods_kwargs)
