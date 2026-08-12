# omicverse.pl.ConvexHull #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.ConvexHull`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.ConvexHull.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot the ConvexHull for a cluster in embedding.

## Signature

```text
omicverse.pl. ConvexHull ( adata , basis , cluster_key , hull_cluster , ax , color = None , alpha = 0.2 )
```

## Parameters

- `adata`: ( AnnData ) – AnnData object
- `basis`: ( str ) – str Embedding method in adata.obsm
- `cluster_key`: ( str ) – str Cluster key in adata.obs
- `hull_cluster`: ( str ) – str Cluster to plot for ConvexHull
- `ax`: – matplotlib.axes.Axes Axes object
- `color`: (default: None ) – str, optional (default=None) Color for ConvexHull
- `alpha`: ( float (default: 0.2 )) – float, optional (default=0.2) Alpha for ConvexHull

## Full Documentation

# omicverse.pl.ConvexHull #

omicverse.pl. ConvexHull ( adata , basis , cluster_key , hull_cluster , ax , color = None , alpha = 0.2 ) [source] #

Plot the ConvexHull for a cluster in embedding.

Parameters :

-
adata ( `AnnData `) – AnnData object

-
basis ( `str `) – str Embedding method in adata.obsm

-
cluster_key ( `str `) – str Cluster key in adata.obs

-
hull_cluster ( `str `) – str Cluster to plot for ConvexHull

-
ax – matplotlib.axes.Axes Axes object

-
color (default: `None `) – str, optional (default=None) Color for ConvexHull

-
alpha ( `float `(default: `0.2 `)) – float, optional (default=0.2) Alpha for ConvexHull

Returns :

matplotlib.axes.Axes

Modified axes object

Return type :

ax
