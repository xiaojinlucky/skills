# Plot a native spatial network

- Package: scop
- Language: R
- Function: `SpatialNetworkPlot`
- Source: https://mengxu98.github.io/scop/reference/SpatialNetworkPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SpatialNetworkPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot a graph produced by [RunSpatialNetwork()]. The graph can be read from a Seurat object or supplied directly as `srt@tools$SpatialNetwork`.

## Signature

```text
SpatialNetworkPlot( object = NULL, res = NULL, graph.name = NULL, group.by = NULL, edge.color = "grey80", edge.linewidth = 0.2, pt.size = NULL, pt.alpha = 1, palette = "Paired", palcolor = NULL, raster = FALSE, raster.dpi = 300, theme_use = "theme_scop", theme_args = list() )
```

## Parameters

- `object`: Optional `Seurat` object containing the graph and metadata.
- `res`: Optional plain result list from `object@tools$SpatialNetwork`.
- `graph.name`: Stored graph name. The active graph is used when `NULL`.
- `group.by`: Node column or Seurat metadata column used for coloring.
- `edge.color, edge.linewidth`: Edge appearance.
- `pt.size, pt.alpha`: Node appearance.
- `palette, palcolor`: Palette name or explicit colors.
- `raster`: Whether to rasterize only the node layer.
- `raster.dpi`: Node rasterization resolution.
- `theme_use, theme_args`: scop theme and its arguments.

## Full Documentation

# Plot a native spatial network

## Usage

```text
SpatialNetworkPlot( object = NULL, res = NULL, graph.name = NULL, group.by = NULL, edge.color = "grey80", edge.linewidth = 0.2, pt.size = NULL, pt.alpha = 1, palette = "Paired", palcolor = NULL, raster = FALSE, raster.dpi = 300, theme_use = "theme_scop", theme_args = list() )
```

## Description

Plot a graph produced by [RunSpatialNetwork()]. The graph can be read from a Seurat object or supplied directly as `srt@tools$SpatialNetwork`.

## Value

A `ggplot` object.
