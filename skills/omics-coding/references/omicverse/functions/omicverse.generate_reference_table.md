# omicverse.generate_reference_table #

- Package: omicverse
- Language: Python
- Function: `omicverse.generate_reference_table`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.generate_reference_table.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Generate a standardized reference table from adata.uns['REFERENCE_MANU'] .

## Signature

```text
omicverse. generate_reference_table ( adata )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object that stores method references in uns['REFERENCE_MANU'] .

## Full Documentation

# omicverse.generate_reference_table #

omicverse. generate_reference_table ( adata ) [source] #

Generate a standardized reference table from `adata.uns['REFERENCE_MANU'] `.

Parameters :

adata ( AnnData ) – AnnData object that stores method references in `uns['REFERENCE_MANU'] `.

Returns :

A table with columns `method `, `content `, and `reference `. Returns `None `when no reference metadata is available.

Return type :

pandas.DataFrame |None
