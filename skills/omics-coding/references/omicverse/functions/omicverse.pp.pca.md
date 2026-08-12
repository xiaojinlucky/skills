# omicverse.pp.pca #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.pca`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.pca.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Performs Principal Component Analysis (PCA) on the data stored in a scanpy AnnData object.

## Signature

```text
omicverse.pp. pca ( adata , n_pcs=50 , layer='scaled' , inplace=True , random_state=<ov.seed-default> , **kwargs )
```

## Parameters

- `adata`: – Annotated data matrix with rows representing cells
- `features.`: ( and columns representing )
- `n_pcs`: (default: 50 ) – Number of principal components to calculate.
- `layer`: ( Defaults to the 'scaled' ) – The name of the layer in adata where the data to be analyzed is stored.
- `layer`: – and falls back to ‘lognorm’ if that layer does not exist.
- `inplace`: Detected from function signature; no parameter description detected.
- `random_state`: Detected from function signature; no parameter description detected.
- `**kwargs`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pp.pca #

omicverse.pp. pca ( adata , n_pcs=50 , layer='scaled' , inplace=True , random_state=<ov.seed-default> , **kwargs ) [source] #

Performs Principal Component Analysis (PCA) on the data stored in a scanpy AnnData object.

Parameters :

-
adata – Annotated data matrix with rows representing cells

-
features. ( and columns representing )

-
n_pcs (default: `50 `) – Number of principal components to calculate.

-
layer ( Defaults to the 'scaled' ) – The name of the layer in adata where the data to be analyzed is stored.

-
layer – and falls back to ‘lognorm’ if that layer does not exist.

:param : and falls back to ‘lognorm’ if that layer does not exist. :param Raises a KeyError if the specified layer is not present.: :type random_state: default: `<ov.seed-default> `:param random_state: Random seed for reproducibility. Defaults to the global

seed set by `ov.set_seed `(else 0).

Returns :

The original AnnData object with the calculated PCA embeddings and other information stored in its obsm , varm ,

and uns fields.

Return type :

adata
