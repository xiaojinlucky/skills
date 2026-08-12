# omicverse.pl.contour #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.contour`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.contour.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Overlay a KDE contour for selected clusters on embedding axes.

## Signature

```text
omicverse.pl. contour ( ax , adata , groupby , clusters , basis = 'X_umap' , grid_density = 100 , contour_threshold = 0.1 , ** kwargs )
```

## Parameters

- `ax`: ( matplotlib.axes.Axes ) – Axis where contour lines are drawn.
- `adata`: ( AnnData ) – AnnData containing embedding coordinates and cluster labels.
- `groupby`: ( str ) – Observation column for cluster filtering.
- `clusters`: ( list ) – Cluster labels to include in contour estimation.
- `basis`: ( str , default='X_umap' ) – Embedding key in adata.obsm .
- `grid_density`: ( int , default=100 ) – Resolution of contour estimation grid.
- `contour_threshold`: ( float , default=0.1 ) – Relative density threshold used for outer contour level.
- `**kwargs`: – Additional arguments forwarded to ax.contour .

## Full Documentation

# omicverse.pl.contour #

omicverse.pl. contour ( ax , adata , groupby , clusters , basis = 'X_umap' , grid_density = 100 , contour_threshold = 0.1 , ** kwargs ) [source] #

Overlay a KDE contour for selected clusters on embedding axes.

Parameters :

-
ax ( matplotlib.axes.Axes ) – Axis where contour lines are drawn.

-
adata ( AnnData ) – AnnData containing embedding coordinates and cluster labels.

-
groupby ( str ) – Observation column for cluster filtering.

-
clusters ( list ) – Cluster labels to include in contour estimation.

-
basis ( str , default='X_umap' ) – Embedding key in `adata.obsm `.

-
grid_density ( int , default=100 ) – Resolution of contour estimation grid.

-
contour_threshold ( float , default=0.1 ) – Relative density threshold used for outer contour level.

-
**kwargs – Additional arguments forwarded to `ax.contour `.

Returns :

Axis with contour overlay.

Return type :

matplotlib.axes.Axes
