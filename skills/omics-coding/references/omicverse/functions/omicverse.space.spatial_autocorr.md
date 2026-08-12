# omicverse.space.spatial_autocorr #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.spatial_autocorr`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.spatial_autocorr.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute spatial autocorrelation statistics for gene expression.

## Signature

```text
omicverse.space. spatial_autocorr ( adata , connectivity_key = 'spatial_connectivities' , genes = None , mode = 'moran' , transformation = True , n_perms = None , two_tailed = False , corr_method = 'fdr_bh' , layer = None , seed = None , copy = False , n_jobs = 1 )
```

## Parameters

- `adata`: – AnnData with a spatial connectivity matrix in adata.obsp .
- `connectivity_key`: ( str (default: 'spatial_connectivities' )) – Key of the spatial connectivity matrix in adata.obsp . Default: ‘spatial_connectivities’.
- `genes`: (default: None ) – Gene names or indices to test. None tests all genes. Default: None.
- `mode`: ( str (default: 'moran' )) – 'moran' (Moran’s I) or 'geary' (Geary’s C). Default: ‘moran’.
- `transformation`: ( bool (default: True )) – Row-normalise the connectivity matrix before scoring. Default: True.
- `n_perms`: (default: None ) – Number of label-permutation iterations for empirical p-values. None uses only the analytical p-value. Default: None.
- `two_tailed`: ( bool (default: False )) – Use two-tailed test for the normal-approximation z-score. Default: False.
- `corr_method`: (default: 'fdr_bh' ) – Multiple-testing correction method passed to statsmodels.stats.multitest.multipletests (e.g. 'fdr_bh' ). Default: ‘fdr_bh’.
- `layer`: (default: None ) – Expression layer to use. None uses adata.X . Default: None.
- `seed`: (default: None ) – Random seed for permutation testing. Default: None.
- `copy`: ( bool (default: False )) – Return the result DataFrame instead of (also) storing it in adata.uns . Default: False.
- `n_jobs`: ( int (default: 1 )) – Reserved for future parallel permutation support. Default: 1.

## Full Documentation

# omicverse.space.spatial_autocorr #

omicverse.space. spatial_autocorr ( adata , connectivity_key = 'spatial_connectivities' , genes = None , mode = 'moran' , transformation = True , n_perms = None , two_tailed = False , corr_method = 'fdr_bh' , layer = None , seed = None , copy = False , n_jobs = 1 ) [source] #

Compute spatial autocorrelation statistics for gene expression.

Moran’s I ( `mode='moran' `) measures positive spatial autocorrelation on `(-1, 1] `; Geary’s C ( `mode='geary' `) measures the opposite – values near 0 indicate strong clustering. P-values are computed analytically under the normal approximation and optionally via label permutation.

Parameters :

-
adata – AnnData with a spatial connectivity matrix in `adata.obsp `.

-
connectivity_key ( `str `(default: `'spatial_connectivities' `)) – Key of the spatial connectivity matrix in `adata.obsp `. Default: ‘spatial_connectivities’.

-
genes (default: `None `) – Gene names or indices to test. `None `tests all genes. Default: None.

-
mode ( `str `(default: `'moran' `)) – `'moran' `(Moran’s I) or `'geary' `(Geary’s C). Default: ‘moran’.

-
transformation ( `bool `(default: `True `)) – Row-normalise the connectivity matrix before scoring. Default: True.

-
n_perms (default: `None `) – Number of label-permutation iterations for empirical p-values. `None `uses only the analytical p-value. Default: None.

-
two_tailed ( `bool `(default: `False `)) – Use two-tailed test for the normal-approximation z-score. Default: False.

-
corr_method (default: `'fdr_bh' `) – Multiple-testing correction method passed to `statsmodels.stats.multitest.multipletests `(e.g. `'fdr_bh' `). Default: ‘fdr_bh’.

-
layer (default: `None `) – Expression layer to use. `None `uses `adata.X `. Default: None.

-
seed (default: `None `) – Random seed for permutation testing. Default: None.

-
copy ( `bool `(default: `False `)) – Return the result DataFrame instead of (also) storing it in `adata.uns `. Default: False.

-
n_jobs ( `int `(default: `1 `)) – Reserved for future parallel permutation support. Default: 1.

Returns :

Results with columns `I `/ `C `, `pval_norm `, and optionally `pval_sim `, `pval_z_sim `, `pval_adj `. Also stored in `adata.uns['moranI'] `or `adata.uns['gearyC'] `.

Return type :

DataFrame

Examples

```text
>>> import omicverse as ov
>>> ov.space.spatial_neighbors(adata, n_neighs=6)
>>> df = ov.space.spatial_autocorr(adata, mode='moran')
>>> df.head()

```
