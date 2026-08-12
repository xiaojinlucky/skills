# Plot stored SpatialCellChat results

- Package: scop
- Language: R
- Function: `SpatialCellChatPlot`
- Source: https://mengxu98.github.io/scop/reference/SpatialCellChatPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SpatialCellChatPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot normalized SpatialCellChat results without rerunning the backend. The network view is a group-aggregated network over group centroids, not a materialized individual cell-by-cell edge table.

## Signature

```text
SpatialCellChatPlot( object, result.name = NULL, sample = NULL, plot_type = c("spatial_network", "lr_spatial", "pathway", "incoming", "outgoing"), signaling = NULL, pairLR.use = NULL, direction = c("outgoing", "incoming"), top_n = 30, point.size = 1.5, palette = "RdBu", palcolor = NULL, title = NULL )
```

## Parameters

- `object`: A `Seurat` object with SpatialCellChat results.
- `result.name`: Stored result name.
- `sample`: Spatial sample. Required when multiple samples are stored.
- `plot_type`: Spatial result view.
- `signaling`: Optional pathway name.
- `pairLR.use`: Optional interaction name.
- `direction`: Score direction for spatial score plots.
- `top_n`: Maximum network edges.
- `point.size`: Coordinate point size.
- `palette, palcolor`: Color palette.
- `title`: Optional title.

## Full Documentation

# Plot stored SpatialCellChat results

## Usage

```text
SpatialCellChatPlot( object, result.name = NULL, sample = NULL, plot_type = c("spatial_network", "lr_spatial", "pathway", "incoming", "outgoing"), signaling = NULL, pairLR.use = NULL, direction = c("outgoing", "incoming"), top_n = 30, point.size = 1.5, palette = "RdBu", palcolor = NULL, title = NULL )
```

## Description

Plot normalized SpatialCellChat results without rerunning the backend. The network view is a group-aggregated network over group centroids, not a materialized individual cell-by-cell edge table.

## Value

A `ggplot` object.
