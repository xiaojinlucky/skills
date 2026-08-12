# omicverse.utils.retrieve_layers #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.retrieve_layers`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.retrieve_layers.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Retrieve previously stored X matrix from adata.uns and restore to adata.X.

## Signature

```text
omicverse.utils. retrieve_layers ( adata , layers = 'counts' )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object containing single-cell data.
- `layers`: ( str ) – Layer name used for stored snapshot retrieval.

## Full Documentation

# omicverse.utils.retrieve_layers #

omicverse.utils. retrieve_layers ( adata , layers = 'counts' ) [source] #

Retrieve previously stored X matrix from adata.uns and restore to adata.X.

Parameters :

-
adata ( AnnData ) – AnnData object containing single-cell data.

-
layers ( str ) – Layer name used for stored snapshot retrieval.

Returns :

Restores stored matrix into `adata.X `.

Return type :

None

Examples

```text
>>> import omicverse as ov
>>> # Store original data before preprocessing
>>> ov.utils.store_layers(adata, layers='raw_counts')
>>> # Apply preprocessing
>>> adata = ov.pp.preprocess(adata)
>>> # Retrieve original data
>>> ov.utils.retrieve_layers(adata, layers='raw_counts')

```
