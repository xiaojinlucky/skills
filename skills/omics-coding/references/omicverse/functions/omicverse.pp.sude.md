# omicverse.pp.sude #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.sude`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.sude.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

SUDE (Scalable Unsupervised Dimensionality reduction via Embedding) dimensionality reduction.

## Signature

```text
omicverse.pp. sude ( adata , n_pcs = None , * , no_dims = 2 , use_rep = None , k1 = 20 , normalize = True , large = False , initialize = 'le' , agg_coef = 1.2 , T_epoch = 50 , key_added = None , copy = False )
```

## Parameters

- `adata`: ( AnnData ) – Annotated data matrix.
- `n_pcs`: ( Optional [ int ] (default: None )) – Number of principal components to use for preprocessing. If None, uses the full data matrix.
- `use_rep`: ( Optional [ str ] (default: None )) – Key for the representation to use. If None, uses adata.X.
- `no_dims`: ( int (default: 2 )) – The number of dimensions of the embedding.
- `k1`: ( int (default: 20 )) – Number of nearest neighbors for PPS (Probabilistic Point Sampling) to sample landmarks. Must be smaller than the number of observations. If set to 0, all points are used as landmarks.
- `normalize`: ( bool (default: True )) – Whether to normalize the data using min-max normalization. Should be set to True if features are on different scales.
- `large`: ( bool (default: False )) – Whether to use the large-scale version that splits data into blocks to avoid memory overflow. Recommended for datasets with >10k cells.
- `initialize`: ( str (default: 'le' )) – Method for initializing the embedding before manifold learning. Options: ‘le’ (Laplacian eigenmaps), ‘pca’ (PCA), ‘mds’ (MDS).
- `agg_coef`: ( float (default: 1.2 )) – Aggregation coefficient for computing modified distance matrix. Controls the influence of shared nearest neighbors.
- `T_epoch`: ( int (default: 50 )) – Maximum number of epochs for optimization.
- `key_added`: ( Optional [ str ] (default: None )) – If not specified, the embedding is stored as obsm [‘X_sude’] and the parameters in uns [‘sude’] . If specified, the embedding is stored as obsm [key_added] and the parameters in uns [key_added] .
- `copy`: ( bool (default: False )) – Return a copy instead of writing to adata .

## Full Documentation

# omicverse.pp.sude #

omicverse.pp. sude ( adata , n_pcs = None , * , no_dims = 2 , use_rep = None , k1 = 20 , normalize = True , large = False , initialize = 'le' , agg_coef = 1.2 , T_epoch = 50 , key_added = None , copy = False ) [source] #

SUDE (Scalable Unsupervised Dimensionality reduction via Embedding) dimensionality reduction.

Perform SUDE dimensionality reduction for visualization of single-cell data. SUDE is a scalable unsupervised dimensionality reduction method that can handle large-scale datasets efficiently by using landmark sampling and constrained locally linear embedding.

SUDE was proposed for scalable dimensionality reduction of single-cell data. It uses a two-stage approach: first computing embeddings for landmark points, then interpolating the remaining points using constrained locally linear embedding.

Parameters :

-
adata ( `AnnData `) – Annotated data matrix.

-
n_pcs ( `Optional `[ `int `] (default: `None `)) – Number of principal components to use for preprocessing. If None, uses the full data matrix.

-
use_rep ( `Optional `[ `str `] (default: `None `)) – Key for the representation to use. If None, uses adata.X.

-
no_dims ( `int `(default: `2 `)) – The number of dimensions of the embedding.

-
k1 ( `int `(default: `20 `)) – Number of nearest neighbors for PPS (Probabilistic Point Sampling) to sample landmarks. Must be smaller than the number of observations. If set to 0, all points are used as landmarks.

-
normalize ( `bool `(default: `True `)) – Whether to normalize the data using min-max normalization. Should be set to True if features are on different scales.

-
large ( `bool `(default: `False `)) – Whether to use the large-scale version that splits data into blocks to avoid memory overflow. Recommended for datasets with >10k cells.

-
initialize ( `str `(default: `'le' `)) – Method for initializing the embedding before manifold learning. Options: ‘le’ (Laplacian eigenmaps), ‘pca’ (PCA), ‘mds’ (MDS).

-
agg_coef ( `float `(default: `1.2 `)) – Aggregation coefficient for computing modified distance matrix. Controls the influence of shared nearest neighbors.

-
T_epoch ( `int `(default: `50 `)) – Maximum number of epochs for optimization.

-
key_added ( `Optional `[ `str `] (default: `None `)) – If not specified, the embedding is stored as `obsm `[‘X_sude’] and the parameters in `uns `[‘sude’] . If specified, the embedding is stored as `obsm ``[key_added] `and the parameters in `uns ``[key_added] `.

-
copy ( `bool `(default: `False `)) – Return a copy instead of writing to adata .

Returns :

-
Returns None if copy=False , else returns an AnnData object. Sets the following fields

-
`adata.obsm[‘X_sude’ | key_added]` ( `numpy.ndarray `(dtype float )) – SUDE coordinates of data.

-
`adata.uns[‘sude’ | key_added]` ( `dict `) – SUDE parameters.

Examples

```text
>>> import omicverse as ov
>>> adata = ov.datasets.pbmc3k()
>>> ov.pp.sude(adata)
>>> ov.pl.sude(adata, color='leiden')

```
