# omicverse.pp.anndata_to_CPU #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.anndata_to_CPU`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.anndata_to_CPU.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Migrate AnnData objects from GPU back to CPU memory after analysis.

## Signature

```text
omicverse.pp. anndata_to_CPU ( adata , layer = None , convert_all = True , copy = False )
```

## Parameters

- `adata`: – AnnData object containing single-cell data on GPU.
- `layer`: (default: None ) – Specific layer to convert back to CPU. Default: None (all layers).
- `convert_all`: (default: True ) – Whether to convert all arrays to CPU. Default: True.
- `copy`: (default: False ) – Whether to create a copy during conversion. Default: False.

## Full Documentation

# omicverse.pp.anndata_to_CPU #

omicverse.pp. anndata_to_CPU ( adata , layer = None , convert_all = True , copy = False ) [source] #

Migrate AnnData objects from GPU back to CPU memory after analysis.

Parameters :

-
adata – AnnData object containing single-cell data on GPU.

-
layer (default: `None `) – Specific layer to convert back to CPU. Default: None (all layers).

-
convert_all (default: `True `) – Whether to convert all arrays to CPU. Default: True.

-
copy (default: `False `) – Whether to create a copy during conversion. Default: False.

Returns :

The function modifies adata in place by moving data from GPU to CPU memory.

Return type :

None

Examples

```text
>>> import omicverse as ov
>>> # After GPU processing, move back to CPU
>>> ov.pp.anndata_to_CPU(adata)
>>> # Convert only specific layer
>>> ov.pp.anndata_to_CPU(adata, layer='scaled', convert_all=False)

```
