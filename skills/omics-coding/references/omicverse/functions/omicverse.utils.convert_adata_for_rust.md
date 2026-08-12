# omicverse.utils.convert_adata_for_rust #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.convert_adata_for_rust`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.convert_adata_for_rust.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Rewrite an AnnData object as an .h5ad file that ov.read(..., backend='rust') can open.

## Signature

```text
omicverse.utils. convert_adata_for_rust ( adata , output_file = None , verbose = True , close_file = True )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Input AnnData object to convert.
- `output_file`: ( str or None , default=None ) – Output .h5ad file path. If None , a temporary file is created.
- `verbose`: ( bool , default=True ) – Whether to print conversion progress and diagnostics.
- `close_file`: ( bool , default=True ) – Retained for backward compatibility; ignored (there is no persistent handle).

## Full Documentation

# omicverse.utils.convert_adata_for_rust #

omicverse.utils. convert_adata_for_rust ( adata , output_file = None , verbose = True , close_file = True ) [source] #

Rewrite an AnnData object as an `.h5ad `file that `ov.read(..., backend='rust') `can open.

Sorts CSR/CSC minor indices, strips NaN/Inf, coerces problematic obs/var dtypes, and preserves `obsm `, `varm `, `uns `, `obsp `, `varp `and `layers `.

Parameters :

-
adata ( anndata.AnnData ) – Input AnnData object to convert.

-
output_file ( str or None , default=None ) – Output `.h5ad `file path. If `None `, a temporary file is created.

-
verbose ( bool , default=True ) – Whether to print conversion progress and diagnostics.

-
close_file ( bool , default=True ) – Retained for backward compatibility; ignored (there is no persistent handle).

Returns :

Path to the converted Rust-compatible `.h5ad `file.

Return type :

str
