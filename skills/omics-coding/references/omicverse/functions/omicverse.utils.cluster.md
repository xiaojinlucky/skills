# omicverse.utils.cluster #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.cluster`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.cluster.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run a selected clustering backend on single-cell data.

## Signature

```text
omicverse.utils. cluster ( adata , method = 'leiden' , use_rep = 'X_pca' , random_state = 1024 , n_components = None , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Annotated data matrix to be clustered.
- `method`: ( str , default='leiden' ) – Clustering backend. Supported values include 'leiden' , 'louvain' , 'kmeans' , 'GMM' , 'mclust' , 'pymclustR' , 'schist' , 'scICE' , and 'cellcharter' . 'pymclustR' is the pure-Python re-implementation of CRAN mclust (the legacy 'mclust_R' rpy2 backend has been removed).
- `use_rep`: ( str , default='X_pca' ) – Key in adata.obsm used for embedding-based methods such as GMM, K-means, and scICE.
- `random_state`: ( int , default=1024 ) – Random seed used by stochastic clustering methods.
- `n_components`: ( int or None , default=None ) – Number of clusters/components for 'kmeans' , 'GMM' , and 'mclust' .
- `**kwargs`: – Extra keyword arguments forwarded to the selected backend. For method='pymclustR' , key_added selects the output column; the legacy spelling add_key is also accepted.

## Full Documentation

# omicverse.utils.cluster #

omicverse.utils. cluster ( adata , method = 'leiden' , use_rep = 'X_pca' , random_state = 1024 , n_components = None , ** kwargs ) [source] #

Run a selected clustering backend on single-cell data.

Parameters :

-
adata ( anndata.AnnData ) – Annotated data matrix to be clustered.

-
method ( str , default='leiden' ) – Clustering backend. Supported values include `'leiden' `, `'louvain' `, `'kmeans' `, `'GMM' `, `'mclust' `, `'pymclustR' `, `'schist' `, `'scICE' `, and `'cellcharter' `. `'pymclustR' `is the pure-Python re-implementation of CRAN `mclust `(the legacy `'mclust_R' `rpy2 backend has been removed).

-
use_rep ( str , default='X_pca' ) – Key in `adata.obsm `used for embedding-based methods such as GMM, K-means, and scICE.

-
random_state ( int , default=1024 ) – Random seed used by stochastic clustering methods.

-
n_components ( int or None , default=None ) – Number of clusters/components for `'kmeans' `, `'GMM' `, and `'mclust' `.

-
**kwargs – Extra keyword arguments forwarded to the selected backend. For `method='pymclustR' `, `key_added `selects the output column; the legacy spelling `add_key `is also accepted.

Returns :

Returns a fitted scICE or CellCharter model instance for the corresponding methods. Other methods write labels to `adata.obs `and return `None `.

Return type :

object or None

Examples

```text
>>> sc.pp.neighbors(adata, n_neighbors=15, n_pcs=50)
>>> cluster(adata, method='leiden', resolution=1.0)
>>> cluster(adata, method='GMM', n_components=10, use_rep='X_pca')
>>> scice_model = cluster(adata, method='scICE', use_rep='X_pca')
>>> cc_model = cluster(adata, method='cellcharter', n_components=8, use_rep='X_pca')

```
