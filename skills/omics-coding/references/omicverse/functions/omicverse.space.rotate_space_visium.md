# omicverse.space.rotate_space_visium #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.rotate_space_visium`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.rotate_space_visium.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Rotate Visium spatial data image and coordinates by a specified angle.

## Signature

```text
omicverse.space. rotate_space_visium ( adata , angle , center = None , spatial_key = 'spatial' , res = 'hires' , library_id = None , interpolation_order = 1 )
```

## Parameters

- `adata`: – AnnData Annotated data matrix containing Visium spatial data.
- `angle`: – float Rotation angle in degrees (positive for counterclockwise).
- `center`: (default: None ) – tuple, optional (default=None) (x, y) coordinates of rotation center. If None, uses center of spatial coordinates.
- `spatial_key`: (default: 'spatial' ) – str, optional (default=’spatial’) Key in adata.obsm containing spatial coordinates.
- `res`: (default: 'hires' ) – str, optional (default=’hires’) Image resolution to use (‘hires’ or ‘lowres’).
- `library_id`: (default: None ) – str Library ID for the spatial data in adata.uns[‘spatial’].
- `interpolation_order`: (default: 1 ) – int, optional (default=1) Order of interpolation for image rotation: 0: nearest neighbor, 1: bilinear, 3: cubic spline.

## Full Documentation

# omicverse.space.rotate_space_visium #

omicverse.space. rotate_space_visium ( adata , angle , center = None , spatial_key = 'spatial' , res = 'hires' , library_id = None , interpolation_order = 1 ) [source] #

Rotate Visium spatial data image and coordinates by a specified angle.

This function performs rotation of both the tissue image and spot coordinates while maintaining proper alignment and scaling.

Parameters :

-
adata – AnnData Annotated data matrix containing Visium spatial data.

-
angle – float Rotation angle in degrees (positive for counterclockwise).

-
center (default: `None `) – tuple, optional (default=None) (x, y) coordinates of rotation center. If None, uses center of spatial coordinates.

-
spatial_key (default: `'spatial' `) – str, optional (default=’spatial’) Key in adata.obsm containing spatial coordinates.

-
res (default: `'hires' `) – str, optional (default=’hires’) Image resolution to use (‘hires’ or ‘lowres’).

-
library_id (default: `None `) – str Library ID for the spatial data in adata.uns[‘spatial’].

-
interpolation_order (default: `1 `) – int, optional (default=1) Order of interpolation for image rotation: 0: nearest neighbor, 1: bilinear, 3: cubic spline.

Returns :

AnnData

Rotated AnnData object with transformed coordinates and image.

Notes

-
The function preserves the original coordinate system scaling

-
Both image and spot coordinates are rotated around the same center

-
The rotation is performed counterclockwise for positive angles

-
Image interpolation can be adjusted for quality vs speed tradeoff

Examples

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load Visium data
>>> adata = sc.read_visium(...)
>>> # Rotate 45 degrees counterclockwise
>>> adata_rotated = ov.space.rotate_space_visium(
... adata,
... angle=45,
... library_id='V1_Human_Brain'
... )

```
