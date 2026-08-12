# omicverse.space.nmf_tissue_zones #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.nmf_tissue_zones`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.nmf_tissue_zones.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Discover tissue zones via NMF on a per-spot cell-abundance matrix.

## Signature

```text
omicverse.space. nmf_tissue_zones ( adata , obsm_key = 'q05_cell_abundance_w_sf' , n_factors = 10 , * , cell_type_names = None , top_k = 5 , obsm_added = 'X_tissue_zones' , factor_prefix = 'zone' , normalize = None , init = 'nndsvd' , max_iter = 500 , tol = 0.0001 , seed = 0 )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData with a cell-abundance matrix in adata.obsm .
- `obsm_key`: ( str (default: 'q05_cell_abundance_w_sf' )) – Where to read the cell-abundance matrix from. Cell2location writes q05_cell_abundance_w_sf (q05 posterior estimate of absolute abundance × size factor) — the recommended input for downstream interpretation. Other deconvolvers may use different keys; pass whatever 2-D float array adata.obsm entry you want to factorise.
- `n_factors`: ( int (default: 10 )) – Number of tissue zones to extract. Cell2location’s tutorial recommends trying several values ( n_fact = [5, 10, 15, 20] ) and picking the one that separates biology best. Start with around the number of cell types you expect to cluster together.
- `cell_type_names`: ( Optional [ Sequence [ str ]] (default: None )) – Explicit names for the cell-type axis. When omitted we read adata.uns[f'{obsm_key}_names'] (Cell2location writes this) or fall back to cell_type_0 ... cell_type_{C-1} .
- `top_k`: ( int (default: 5 )) – For each factor, report the top_k cell types with the highest loadings in result.factor_top_cell_types . Default 5.
- `obsm_added`: ( str (default: 'X_tissue_zones' )) – Where to write the per-spot factor activations. Default X_tissue_zones . Also written back to adata.obsm[obsm_added] so downstream plotting (Scanpy sc.pl.spatial , ov.pl.embedding ) can colour spots by zone directly. The run’s metadata ( n_factors , source_obsm , cell_type_names , factor_names , reconstruction_err ) goes to adata.uns['tissue_zones'][obsm_added] , so a saved AnnData still says where its zone matrix came from — the array on its own does not.
- `factor_prefix`: ( str (default: 'zone' )) – Prefix for factor names; the i-th factor is f'{factor_prefix}_{i+1}' .
- `normalize`: ( Optional [ str ] (default: None )) – None (default) to feed the matrix straight to NMF, or 'rows' to row-sum-normalise each spot to 1 first — recommended when obsm_key carries mapping probabilities or any non-abundance quantity where per-spot total-signal is not biologically meaningful (for example Tangram’s tangram_ct_pred ). Skip for Cell2location’s q05_cell_abundance_w_sf , which is an absolute-abundance scale and should be fed as-is so inter-spot abundance differences are preserved.
- `init`: ( str (default: 'nndsvd' )) – Forwarded to sklearn.decomposition.NMF . init='nndsvd' gives deterministic initialisation; 'random' + seed gives multiple-restart behaviour if you loop manually.
- `max_iter`: ( int (default: 500 )) – Forwarded to sklearn.decomposition.NMF . init='nndsvd' gives deterministic initialisation; 'random' + seed gives multiple-restart behaviour if you loop manually.
- `tol`: ( float (default: 0.0001 )) – Forwarded to sklearn.decomposition.NMF . init='nndsvd' gives deterministic initialisation; 'random' + seed gives multiple-restart behaviour if you loop manually.
- `seed`: ( int (default: 0 )) – Forwarded to sklearn.decomposition.NMF . init='nndsvd' gives deterministic initialisation; 'random' + seed gives multiple-restart behaviour if you loop manually.

## Full Documentation

# omicverse.space.nmf_tissue_zones #

omicverse.space. nmf_tissue_zones ( adata , obsm_key = 'q05_cell_abundance_w_sf' , n_factors = 10 , * , cell_type_names = None , top_k = 5 , obsm_added = 'X_tissue_zones' , factor_prefix = 'zone' , normalize = None , init = 'nndsvd' , max_iter = 500 , tol = 0.0001 , seed = 0 ) [source] #

Discover tissue zones via NMF on a per-spot cell-abundance matrix.

Parameters :

-
adata ( `AnnData `) – Spatial AnnData with a cell-abundance matrix in `adata.obsm `.

-
obsm_key ( `str `(default: `'q05_cell_abundance_w_sf' `)) – Where to read the cell-abundance matrix from. Cell2location writes `q05_cell_abundance_w_sf `(q05 posterior estimate of absolute abundance × size factor) — the recommended input for downstream interpretation. Other deconvolvers may use different keys; pass whatever 2-D float array `adata.obsm `entry you want to factorise.

-
n_factors ( `int `(default: `10 `)) – Number of tissue zones to extract. Cell2location’s tutorial recommends trying several values ( `n_fact = [5, 10, 15, 20] `) and picking the one that separates biology best. Start with around the number of cell types you expect to cluster together.

-
cell_type_names ( `Optional `[ `Sequence `[ `str `]] (default: `None `)) – Explicit names for the cell-type axis. When omitted we read `adata.uns[f'{obsm_key}_names'] `(Cell2location writes this) or fall back to `cell_type_0 ... cell_type_{C-1} `.

-
top_k ( `int `(default: `5 `)) – For each factor, report the `top_k `cell types with the highest loadings in `result.factor_top_cell_types `. Default 5.

-
obsm_added ( `str `(default: `'X_tissue_zones' `)) – Where to write the per-spot factor activations. Default `X_tissue_zones `. Also written back to `adata.obsm[obsm_added] `so downstream plotting (Scanpy `sc.pl.spatial `, `ov.pl.embedding `) can colour spots by zone directly. The run’s metadata ( `n_factors `, `source_obsm `, `cell_type_names `, `factor_names `, `reconstruction_err `) goes to `adata.uns['tissue_zones'][obsm_added] `, so a saved AnnData still says where its zone matrix came from — the array on its own does not.

-
factor_prefix ( `str `(default: `'zone' `)) – Prefix for factor names; the i-th factor is `f'{factor_prefix}_{i+1}' `.

-
normalize ( `Optional `[ `str `] (default: `None `)) – `None `(default) to feed the matrix straight to NMF, or `'rows' `to row-sum-normalise each spot to 1 first — recommended when `obsm_key `carries mapping probabilities or any non-abundance quantity where per-spot total-signal is not biologically meaningful (for example Tangram’s `tangram_ct_pred `). Skip for Cell2location’s `q05_cell_abundance_w_sf `, which is an absolute-abundance scale and should be fed as-is so inter-spot abundance differences are preserved.

-
init ( `str `(default: `'nndsvd' `)) – Forwarded to `sklearn.decomposition.NMF `. `init='nndsvd' `gives deterministic initialisation; `'random' `+ `seed `gives multiple-restart behaviour if you loop manually.

-
max_iter ( `int `(default: `500 `)) – Forwarded to `sklearn.decomposition.NMF `. `init='nndsvd' `gives deterministic initialisation; `'random' `+ `seed `gives multiple-restart behaviour if you loop manually.

-
tol ( `float `(default: `0.0001 `)) – Forwarded to `sklearn.decomposition.NMF `. `init='nndsvd' `gives deterministic initialisation; `'random' `+ `seed `gives multiple-restart behaviour if you loop manually.

-
seed ( `int `(default: `0 `)) – Forwarded to `sklearn.decomposition.NMF `. `init='nndsvd' `gives deterministic initialisation; `'random' `+ `seed `gives multiple-restart behaviour if you loop manually.

Returns :

See the dataclass for attribute details.

Return type :

TissueZones

Notes

-
The abundance matrix must be non-negative . Most deconvolvers produce non-negative output; if your matrix has small negative values (numerical noise) they are clipped to 0 here.

-
This is a lightweight sibling of Cell2location’s `run_colocation `(pyro-backed, Bayesian). The output is qualitatively equivalent — factor loadings and spot activations with the same interpretation — but the sklearn NMF runs in seconds and has no pyro/torch dependency.

References
[ 1 ]
Kleshchevnikov et al., Nat. Biotechnol. 2022 — Cell2location. Tissue-zone discovery via matrix factorisation of the per-spot cell-abundance matrix.
