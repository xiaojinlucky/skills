# omicverse.space.moranI #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.moranI`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.moranI.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute Moran’s I spatial autocorrelation for gene expression.

## Signature

```text
omicverse.space. moranI ( adata , connectivity_key = 'spatial_connectivities' , genes = None , transformation = True , n_perms = None , two_tailed = False , corr_method = 'fdr_bh' , layer = None , seed = None , copy = False , auto_spatial_neighbors = False , n_neighs = 6 , radius = None , spatial_key = 'spatial' )
```

## Parameters

- `adata`: – AnnData with spatial coordinates in adata.obsm and optionally a precomputed connectivity in adata.obsp .
- `connectivity_key`: ( str (default: 'spatial_connectivities' )) – Key of the spatial connectivity matrix in adata.obsp . Default: ‘spatial_connectivities’.
- `genes`: (default: None ) – Gene names/indices to test. None tests all genes. Default: None.
- `transformation`: ( bool (default: True )) – Row-normalise the weight matrix before scoring. Default: True.
- `n_perms`: (default: None ) – Permutations for empirical p-values; None uses only the analytical value. Default: None.
- `two_tailed`: ( bool (default: False )) – Two-tailed z-score test. Default: False.
- `corr_method`: (default: 'fdr_bh' ) – Multiple-testing correction ( 'fdr_bh' , 'bonferroni' , …). Default: ‘fdr_bh’.
- `layer`: (default: None ) – Expression layer to use; None uses adata.X . Default: None.
- `seed`: (default: None ) – Random seed for permutation reproducibility. Default: None.
- `copy`: ( bool (default: False )) – Return the result DataFrame. Default: False.
- `auto_spatial_neighbors`: ( bool (default: False )) – Automatically build the spatial neighborhood graph if connectivity_key is absent from adata.obsp . Default: False.
- `n_neighs`: ( int (default: 6 )) – Number of KNN neighbours used when auto_spatial_neighbors is True . Default: 6.
- `radius`: (default: None ) – Radius for radius-based graph when auto_spatial_neighbors is True . Default: None.
- `spatial_key`: ( str (default: 'spatial' )) – Key in adata.obsm holding 2-D coordinates. Default: ‘spatial’.

## Full Documentation

# omicverse.space.moranI #

omicverse.space. moranI ( adata , connectivity_key = 'spatial_connectivities' , genes = None , transformation = True , n_perms = None , two_tailed = False , corr_method = 'fdr_bh' , layer = None , seed = None , copy = False , auto_spatial_neighbors = False , n_neighs = 6 , radius = None , spatial_key = 'spatial' ) [source] #

Compute Moran’s I spatial autocorrelation for gene expression.

A convenience wrapper around `spatial_autocorr() `with `mode='moran' `. Set auto_spatial_neighbors to `True `to build the spatial neighborhood graph automatically via `spatial_neighbors() `when the connectivity matrix is missing from `adata.obsp `.

Parameters :

-
adata – AnnData with spatial coordinates in `adata.obsm `and optionally a precomputed connectivity in `adata.obsp `.

-
connectivity_key ( `str `(default: `'spatial_connectivities' `)) – Key of the spatial connectivity matrix in `adata.obsp `. Default: ‘spatial_connectivities’.

-
genes (default: `None `) – Gene names/indices to test. `None `tests all genes. Default: None.

-
transformation ( `bool `(default: `True `)) – Row-normalise the weight matrix before scoring. Default: True.

-
n_perms (default: `None `) – Permutations for empirical p-values; `None `uses only the analytical value. Default: None.

-
two_tailed ( `bool `(default: `False `)) – Two-tailed z-score test. Default: False.

-
corr_method (default: `'fdr_bh' `) – Multiple-testing correction ( `'fdr_bh' `, `'bonferroni' `, …). Default: ‘fdr_bh’.

-
layer (default: `None `) – Expression layer to use; `None `uses `adata.X `. Default: None.

-
seed (default: `None `) – Random seed for permutation reproducibility. Default: None.

-
copy ( `bool `(default: `False `)) – Return the result DataFrame. Default: False.

-
auto_spatial_neighbors ( `bool `(default: `False `)) – Automatically build the spatial neighborhood graph if connectivity_key is absent from `adata.obsp `. Default: False.

-
n_neighs ( `int `(default: `6 `)) – Number of KNN neighbours used when auto_spatial_neighbors is `True `. Default: 6.

-
radius (default: `None `) – Radius for radius-based graph when auto_spatial_neighbors is `True `. Default: None.

-
spatial_key ( `str `(default: `'spatial' `)) – Key in `adata.obsm `holding 2-D coordinates. Default: ‘spatial’.

Returns :

Moran’s I results with columns `I `, `pval_norm `, and optionally `pval_sim `, `pval_z_sim `, `pval_adj `. Also stored in `adata.uns['moranI'] `.

Return type :

DataFrame

Examples

```text
>>> import omicverse as ov
>>> ov.space.spatial_neighbors(adata, n_neighs=6)
>>> df = ov.space.moranI(adata)
>>> df.head()
>>> # One-liner with auto graph building
>>> df = ov.space.moranI(adata, auto_spatial_neighbors=True)

```
