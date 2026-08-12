# omicverse.pl.add_streamplot #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.add_streamplot`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.add_streamplot.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Overlay velocity streamlines on a low-dimensional embedding.

## Signature

```text
omicverse.pl. add_streamplot ( adata , basis = 'X_umap' , velocity_key = 'velocity_S' , density = 1 , smooth = 0.5 , min_mass = 1 , autoscale = True , adjust_for_stream = True , ax = None , arrow_color = 'k' , stream_kwargs = None )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing embedding coordinates and velocity projections.
- `basis`: ( str ) – adata.obsm key for embedding coordinates.
- `velocity_key`: ( str ) – adata.obsm key for velocity vectors in embedding space.
- `density`: ( float ) – Grid density for streamline interpolation.
- `smooth`: ( float ) – Gaussian smoothing applied on velocity grid.
- `min_mass`: ( float ) – Minimum mass threshold used by grid construction.
- `autoscale`: ( bool ) – Whether to autoscale vectors.
- `adjust_for_stream`: ( bool ) – Whether to adjust vectors for streamline plotting.
- `ax`: ( matplotlib.axes.Axes or None ) – Target axes. Uses current axes if None .
- `arrow_color`: ( str ) – Streamline color.
- `stream_kwargs`: ( dict or None ) – Extra keyword arguments passed to Axes.streamplot .

## Full Documentation

# omicverse.pl.add_streamplot #

omicverse.pl. add_streamplot ( adata , basis = 'X_umap' , velocity_key = 'velocity_S' , density = 1 , smooth = 0.5 , min_mass = 1 , autoscale = True , adjust_for_stream = True , ax = None , arrow_color = 'k' , stream_kwargs = None ) [source] #

Overlay velocity streamlines on a low-dimensional embedding.

Parameters :

-
adata ( AnnData ) – AnnData containing embedding coordinates and velocity projections.

-
basis ( str ) – `adata.obsm `key for embedding coordinates.

-
velocity_key ( str ) – `adata.obsm `key for velocity vectors in embedding space.

-
density ( float ) – Grid density for streamline interpolation.

-
smooth ( float ) – Gaussian smoothing applied on velocity grid.

-
min_mass ( float ) – Minimum mass threshold used by grid construction.

-
autoscale ( bool ) – Whether to autoscale vectors.

-
adjust_for_stream ( bool ) – Whether to adjust vectors for streamline plotting.

-
ax ( matplotlib.axes.Axes or None ) – Target axes. Uses current axes if `None `.

-
arrow_color ( str ) – Streamline color.

-
stream_kwargs ( dict or None ) – Extra keyword arguments passed to `Axes.streamplot `.

Returns :

Axes with streamlines.

Return type :

matplotlib.axes.Axes

Examples

```text
>>> ov.pl.embedding(adata, basis='X_umap')
>>> ov.pl.add_streamplot(adata, basis='X_umap', velocity_key='velocity_S')

```
