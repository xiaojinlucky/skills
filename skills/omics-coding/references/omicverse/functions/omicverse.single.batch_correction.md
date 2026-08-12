# omicverse.single.batch_correction #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.batch_correction`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.batch_correction.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run batch-effect correction for single-cell data integration.

## Signature

```text
omicverse.single. batch_correction ( adata , batch_key , use_rep = 'scaled|original|X_pca' , methods = 'harmony' , n_pcs = 50 , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Input data matrix. Different methods require different preprocessing: for example, scVI typically needs raw counts in adata.layers['counts'] .
- `batch_key`: ( str ) – Column in adata.obs defining batch/domain labels.
- `use_rep`: ( str , default='scaled | original | X_pca' ) – Embedding key used by embedding-based methods (for example Harmony).
- `methods`: ( str , default='harmony' ) – Integration backend. Supported values include 'harmony' , 'combat' , 'scanorama' , 'scVI' , 'scANVI' (semi-supervised VAE; requires labels_key= ), 'totalVI' (joint RNA+protein; requires protein_expression_obsm_key= ), 'scPoli' (scArches conditional VAE; supports cell_type_keys= for prototype learning), 'CellANOVA' , 'Concord' , 'cca' / 'seurat_cca' — the pure-Python port of Seurat::RunCCA (via the pyccasc package, no R / rpy2 required) — and 'rpca' / 'seurat_rpca' — a faithful Python port of Seurat’s IntegrateLayers(method = RPCAIntegration) (reciprocal-PCA anchors, no R required; writes adata.obsm['X_rpca'] ). RPCA accepts features= , reference= , k_anchor= , k_weight= , sd_weight= and orig_rep= (the joint reduction to correct).
- `n_pcs`: ( int , default=50 ) – Number of principal components / canonical components used by the selected backend. For 'cca' this is the number of canonical components ( num_cc in pyccasc terms).
- `**kwargs`: – Additional method-specific keyword arguments passed to the selected backend implementation.

## Full Documentation

# omicverse.single.batch_correction #

omicverse.single. batch_correction ( adata , batch_key , use_rep = 'scaled|original|X_pca' , methods = 'harmony' , n_pcs = 50 , ** kwargs ) [source] #

Run batch-effect correction for single-cell data integration.

Parameters :

-
adata ( anndata.AnnData ) – Input data matrix. Different methods require different preprocessing: for example, `scVI `typically needs raw counts in `adata.layers['counts'] `.

-
batch_key ( str ) – Column in `adata.obs `defining batch/domain labels.

-
use_rep ( str , default='scaled | original | X_pca' ) – Embedding key used by embedding-based methods (for example Harmony).

-
methods ( str , default='harmony' ) – Integration backend. Supported values include `'harmony' `, `'combat' `, `'scanorama' `, `'scVI' `, `'scANVI' `(semi-supervised VAE; requires `labels_key= `), `'totalVI' `(joint RNA+protein; requires `protein_expression_obsm_key= `), `'scPoli' `(scArches conditional VAE; supports `cell_type_keys= `for prototype learning), `'CellANOVA' `, `'Concord' `, `'cca' `/ `'seurat_cca' `— the pure-Python port of `Seurat::RunCCA `(via the pyccasc package, no R / rpy2 required) — and `'rpca' `/ `'seurat_rpca' `— a faithful Python port of Seurat’s `IntegrateLayers(method = RPCAIntegration) `(reciprocal-PCA anchors, no R required; writes `adata.obsm['X_rpca'] `). RPCA accepts `features= `, `reference= `, `k_anchor= `, `k_weight= `, `sd_weight= `and `orig_rep= `(the joint reduction to correct).

-
n_pcs ( int , default=50 ) – Number of principal components / canonical components used by the selected backend. For `'cca' `this is the number of canonical components ( `num_cc `in pyccasc terms).

-
**kwargs – Additional method-specific keyword arguments passed to the selected backend implementation.

Returns :

Returns `adata `for most methods, scVI model object for `'scVI' `, and Concord object for `'Concord' `. The integrated embeddings are written to `adata.obsm `.

Return type :

anndata.AnnData or object
