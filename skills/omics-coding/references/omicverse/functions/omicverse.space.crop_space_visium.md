# omicverse.space.crop_space_visium #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.crop_space_visium`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.crop_space_visium.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Crop Visium spatial data to a specific region of interest.

## Signature

```text
omicverse.space. crop_space_visium ( adata , crop_loc , crop_area , library_id , scale , spatial_key = 'spatial' , res = 'hires' )
```

## Parameters

- `adata`: – AnnData Annotated data matrix containing Visium spatial data.
- `crop_loc`: – tuple (x, y) coordinates for the top-left corner of the crop region.
- `crop_area`: – tuple (width, height) of the cropping area in spatial coordinates.
- `library_id`: – str Library ID for the spatial data in adata.uns[‘spatial’].
- `scale`: – float Scale factor for the cropping operation.
- `spatial_key`: (default: 'spatial' ) – str, optional (default=’spatial’) Key in adata.obsm containing spatial coordinates.
- `res`: (default: 'hires' ) – str, optional (default=’hires’) Image resolution to use (‘hires’ or ‘lowres’).

## Full Documentation

# omicverse.space.crop_space_visium #

omicverse.space. crop_space_visium ( adata , crop_loc , crop_area , library_id , scale , spatial_key = 'spatial' , res = 'hires' ) [source] #

Crop Visium spatial data to a specific region of interest.

This function allows cropping of Visium spatial transcriptomics data to focus on a specific region while maintaining proper scaling and coordinate systems.

Parameters :

-
adata – AnnData Annotated data matrix containing Visium spatial data.

-
crop_loc – tuple (x, y) coordinates for the top-left corner of the crop region.

-
crop_area – tuple (width, height) of the cropping area in spatial coordinates.

-
library_id – str Library ID for the spatial data in adata.uns[‘spatial’].

-
scale – float Scale factor for the cropping operation.

-
spatial_key (default: `'spatial' `) – str, optional (default=’spatial’) Key in adata.obsm containing spatial coordinates.

-
res (default: `'hires' `) – str, optional (default=’hires’) Image resolution to use (‘hires’ or ‘lowres’).

Returns :

AnnData

Cropped AnnData object containing only spots within the specified region. The spatial coordinates and image are adjusted accordingly.

Notes

-
The function preserves the original coordinate system scaling

-
The cropped image is stored in adata.uns[‘spatial’][library_id][‘images’][res]

-
Coordinates are automatically adjusted to the new cropped region

Examples

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load Visium data
>>> adata = sc.read_visium(...)
>>> # Crop a 1000x1000 region starting at (500, 500)
>>> adata_cropped = ov.space.crop_space_visium(
... adata,
... crop_loc=(500, 500),
... crop_area=(1000, 1000),
... library_id='V1_Human_Brain',
... scale=1.0
... )

```
