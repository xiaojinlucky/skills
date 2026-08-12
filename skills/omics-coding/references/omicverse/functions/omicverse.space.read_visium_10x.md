# omicverse.space.read_visium_10x #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.read_visium_10x`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.read_visium_10x.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read and standardize 10x Visium data with bin2cell-compatible loader.

## Signature

```text
omicverse.space. read_visium_10x ( adata , ** kwargs )
```

## Parameters

- `adata`: ( str or AnnData ) – Input Visium path/object accepted by bin2cell.read_visium .
- `**kwargs`: – Additional arguments forwarded to read_visium .

## Full Documentation

# omicverse.space.read_visium_10x #

omicverse.space. read_visium_10x ( adata , ** kwargs ) [source] #

Read and standardize 10x Visium data with bin2cell-compatible loader.

Parameters :

-
adata ( str or AnnData ) – Input Visium path/object accepted by `bin2cell.read_visium `.

-
**kwargs – Additional arguments forwarded to `read_visium `.

Returns :

Visium AnnData with unique variable names.

Return type :

AnnData
