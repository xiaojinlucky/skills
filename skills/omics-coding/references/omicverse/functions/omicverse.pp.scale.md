# omicverse.pp.scale #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.scale`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.scale.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Scale the input AnnData object.

## Signature

```text
omicverse.pp. scale ( adata , max_value = 10 , layers_add = 'scaled' , to_sparse = False , use_implicit_centering = False , ** kwargs )
```

## Parameters

- `adata`: – Annotated data matrix with n_obs x n_vars shape.
- `max_value`: (default: 10 ) – Maximum value after scaling. Default: 10.
- `layers_add`: (default: 'scaled' ) – Name of the layer to store the scaled data. Default: ‘scaled’. OOM backend only supports layers_add=’scaled’ (the underlying chunked_scale writes a lazy ScaledBackedArray to that fixed key); passing anything else raises ValueError.
- `to_sparse`: (default: False ) – If True, convert the result to csr_matrix format. Default: False. Scaled data is 100% dense, so sparse storage only adds overhead.
- `use_implicit_centering`: (default: False ) – If True and the in-memory adata.X is sparse, store the scaled matrix as a lazy CenteredSparseArray (anndataoom) in adata.uns['_scaled_implicit'] instead of materialising a dense adata.layers['scaled'] . Trades a small dispatch hop in downstream consumers (only ov.pp.pca knows how to read this layout) for n_obs * n_vars * 4 bytes of avoided allocation – at 1M cells x 60606 genes that is ~240 GB, the difference between OOM-killed and completing under a typical 256 GB per-process RSS cap. ov.pp.pca densifies only the HVG-subset slice the SVD actually needs. Default: False (preserves existing behavior). Ignored on the OOM backend (which already uses a lazy ScaledBackedArray ) and on GPU mode.
- `**kwargs`: – Additional arguments passed to scaling functions.

## Full Documentation

# omicverse.pp.scale #

omicverse.pp. scale ( adata , max_value = 10 , layers_add = 'scaled' , to_sparse = False , use_implicit_centering = False , ** kwargs ) [source] #

Scale the input AnnData object.

Parameters :

-
adata – Annotated data matrix with n_obs x n_vars shape.

-
max_value (default: `10 `) – Maximum value after scaling. Default: 10.

-
layers_add (default: `'scaled' `) – Name of the layer to store the scaled data. Default: ‘scaled’. OOM backend only supports layers_add=’scaled’ (the underlying chunked_scale writes a lazy ScaledBackedArray to that fixed key); passing anything else raises ValueError.

-
to_sparse (default: `False `) – If True, convert the result to csr_matrix format. Default: False. Scaled data is 100% dense, so sparse storage only adds overhead.

-
use_implicit_centering (default: `False `) – If True and the in-memory adata.X is sparse, store the scaled matrix as a lazy `CenteredSparseArray `(anndataoom) in `adata.uns['_scaled_implicit'] `instead of materialising a dense `adata.layers['scaled'] `. Trades a small dispatch hop in downstream consumers (only `ov.pp.pca `knows how to read this layout) for `n_obs * n_vars * 4 bytes `of avoided allocation – at 1M cells x 60606 genes that is ~240 GB, the difference between OOM-killed and completing under a typical 256 GB per-process RSS cap. `ov.pp.pca `densifies only the HVG-subset slice the SVD actually needs. Default: False (preserves existing behavior). Ignored on the OOM backend (which already uses a lazy `ScaledBackedArray `) and on GPU mode.

-
**kwargs – Additional arguments passed to scaling functions.

Returns :

Annotated data matrix with n_obs x n_vars shape. Adds a new layer called ‘scaled’ that stores the expression matrix that has been scaled to unit variance and zero mean.

Return type :

adata

Examples

```text
>>> import omicverse as ov
>>> # Scale data with default sparse output
>>> ov.pp.scale(adata, max_value=10)
>>> # Scale data keeping dense format
>>> ov.pp.scale(adata, max_value=10, to_sparse=False)
>>> # Lazy implicit centering for million-cell in-memory pipelines
>>> ov.pp.scale(adata, max_value=10, use_implicit_centering=True)

```
