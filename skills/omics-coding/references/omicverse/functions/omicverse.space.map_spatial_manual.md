# omicverse.space.map_spatial_manual #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.map_spatial_manual`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.map_spatial_manual.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Manually adjust spatial transcriptomics data alignment.

## Signature

```text
omicverse.space. map_spatial_manual ( adata_rotated , offset )
```

## Parameters

- `adata_rotated`: – AnnData Annotated data matrix containing spatial data to be aligned.
- `offset`: – tuple (dx, dy) tuple specifying the manual offset to apply.

## Full Documentation

# omicverse.space.map_spatial_manual #

omicverse.space. map_spatial_manual ( adata_rotated , offset ) [source] #

Manually adjust spatial transcriptomics data alignment.

This function allows manual adjustment of the alignment between spatial transcriptomics data and the tissue image using specified offsets.

Parameters :

-
adata_rotated – AnnData Annotated data matrix containing spatial data to be aligned.

-
offset – tuple (dx, dy) tuple specifying the manual offset to apply.

Returns :

AnnData

Aligned AnnData object with manually adjusted spatial coordinates.

Notes

-
Useful for fine-tuning automatic alignment results

-
Offset values are in pixel coordinates

-
Positive dx moves spots right, positive dy moves spots down

Examples

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load data
>>> adata = sc.read_visium(...)
>>> # Apply manual offset
>>> adata_aligned = ov.space.map_spatial_manual(
... adata,
... offset=(10, -5) # Move 10 pixels right, 5 pixels up
... )

```
