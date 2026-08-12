# omicverse.space.map_spatial_auto #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.map_spatial_auto`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.map_spatial_auto.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Automatically map and align spatial transcriptomics data.

## Signature

```text
omicverse.space. map_spatial_auto ( adata_rotated , method = 'phase' )
```

## Parameters

- `adata_rotated`: – AnnData Annotated data matrix containing spatial data to be aligned.
- `method`: (default: 'phase' ) – str, optional (default=’phase’) Alignment method to use: - ‘phase’: Phase correlation-based alignment - ‘feature’: Feature-based alignment - ‘hybrid’: Combination of phase and feature methods

## Full Documentation

# omicverse.space.map_spatial_auto #

omicverse.space. map_spatial_auto ( adata_rotated , method = 'phase' ) [source] #

Automatically map and align spatial transcriptomics data.

This function performs automatic alignment of spatial transcriptomics data with the corresponding tissue image using various alignment methods.

Parameters :

-
adata_rotated – AnnData Annotated data matrix containing spatial data to be aligned.

-
method (default: `'phase' `) – str, optional (default=’phase’) Alignment method to use: - ‘phase’: Phase correlation-based alignment - ‘feature’: Feature-based alignment - ‘hybrid’: Combination of phase and feature methods

Returns :

AnnData

Aligned AnnData object with updated spatial coordinates.

Notes

-
The function automatically selects the best alignment

-
Results can be verified using spatial plotting functions

-
Different methods may work better for different data types

Examples

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load and preprocess data
>>> adata = sc.read_visium(...)
>>> # Perform automatic alignment
>>> adata_aligned = ov.space.map_spatial_auto(
... adata,
... method='phase'
... )

```
