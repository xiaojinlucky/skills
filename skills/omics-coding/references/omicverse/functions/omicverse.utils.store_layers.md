# omicverse.utils.store_layers #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.store_layers`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.store_layers.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Store the X matrix of AnnData in adata.uns for later retrieval.

## Signature

```text
omicverse.utils. store_layers ( adata , layers = 'counts' )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object containing single-cell data.
- `layers`: ( str ) – Layer name used for stored snapshot.

## Full Documentation

# omicverse.utils.store_layers #

omicverse.utils. store_layers ( adata , layers = 'counts' ) [source] #

Store the X matrix of AnnData in adata.uns for later retrieval.

Parameters :

-
adata ( AnnData ) – AnnData object containing single-cell data.

-
layers ( str ) – Layer name used for stored snapshot.

Returns :

Stores current `adata.X `snapshot into `adata.uns `.

Return type :

None

Examples

```text
>>> import omicverse as ov
>>> # Store original counts before preprocessing
>>> ov.utils.store_layers(adata, layers='raw_counts')
>>> # Apply preprocessing
>>> adata = ov.pp.preprocess(adata)
>>> # Retrieve original data if needed
>>> ov.utils.retrieve_layers(adata, layers='raw_counts')

```
