# omicverse.pp.log1p #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.log1p`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.log1p.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Log-transform expression values with log(1 + x) .

## Signature

```text
omicverse.pp. log1p ( adata , * , base = None , copy = False , chunked = False , chunk_size = None , layer = None , obsm = None )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object containing expression values.
- `base`: ( Number , optional ) – Logarithm base. Uses natural logarithm when None .
- `copy`: ( bool , default=False ) – If True , return a transformed copy instead of modifying in place.
- `chunked`: ( bool , default=False ) – Whether to transform adata.X by chunks for memory efficiency.
- `chunk_size`: ( int , optional ) – Number of cells per chunk when chunked=True .
- `layer`: ( str , optional ) – Layer name to transform instead of adata.X .
- `obsm`: ( str , optional ) – adata.obsm key to transform instead of adata.X .

## Full Documentation

# omicverse.pp.log1p #

omicverse.pp. log1p ( adata , * , base = None , copy = False , chunked = False , chunk_size = None , layer = None , obsm = None ) [source] #

Log-transform expression values with `log(1 + x) `.

Parameters :

-
adata ( AnnData ) – AnnData object containing expression values.

-
base ( Number , optional ) – Logarithm base. Uses natural logarithm when `None `.

-
copy ( bool , default=False ) – If `True `, return a transformed copy instead of modifying in place.

-
chunked ( bool , default=False ) – Whether to transform `adata.X `by chunks for memory efficiency.

-
chunk_size ( int , optional ) – Number of cells per chunk when `chunked=True `.

-
layer ( str , optional ) – Layer name to transform instead of `adata.X `.

-
obsm ( str , optional ) – `adata.obsm `key to transform instead of `adata.X `.

Returns :

Returns a transformed AnnData when `copy=True `; otherwise modifies `adata `in place and returns `None `.

Return type :

AnnData or None
