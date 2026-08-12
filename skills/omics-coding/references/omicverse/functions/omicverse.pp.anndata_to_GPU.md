# omicverse.pp.anndata_to_GPU #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.anndata_to_GPU`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.anndata_to_GPU.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Migrate AnnData objects to GPU memory for accelerated processing.

## Signature

```text
omicverse.pp. anndata_to_GPU ( adata , * , convert_all = True , copy = False , ** kwargs )
```

## Parameters

- `adata`: – AnnData object containing single-cell data.
- `**kwargs`: – Additional arguments passed to rapids_singlecell.get.anndata_to_GPU.
- `convert_all`: Detected from function signature; no parameter description detected.
- `copy`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.pp.anndata_to_GPU #

omicverse.pp. anndata_to_GPU ( adata , * , convert_all = True , copy = False , ** kwargs ) [source] #

Migrate AnnData objects to GPU memory for accelerated processing.

Parameters :

-
adata – AnnData object containing single-cell data.

-
**kwargs – Additional arguments passed to rapids_singlecell.get.anndata_to_GPU.

Returns :

The function modifies adata in place by moving data to GPU memory.

Return type :

None

Examples

```text
>>> import omicverse as ov
>>> # Initialize GPU mode
>>> ov.settings.gpu_init()
>>> # Move data to GPU
>>> ov.pp.anndata_to_GPU(adata)
>>> # Perform GPU-accelerated analysis
>>> adata = ov.pp.qc(adata)
>>> # Move back to CPU when done
>>> ov.pp.anndata_to_CPU(adata)

```

Parameters :

-
convert_all ( `bool `(default: `True `))

-
copy ( `bool `(default: `False `))
