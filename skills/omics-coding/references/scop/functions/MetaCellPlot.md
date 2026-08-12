# Visualize metacell partitions on a dimensionality reduction

- Package: scop
- Language: R
- Function: `MetaCellPlot`
- Source: https://mengxu98.github.io/scop/reference/MetaCellPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/MetaCellPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualize metacell partitions on a dimensionality reduction

## Signature

```text
MetaCellPlot( srt, reduction = NULL, show_cells = FALSE, group.by = NULL, color.by = NULL, dims = c(1, 2), label = FALSE, palette = "Chinese", palcolor = NULL, palette_metacell = "Chinese", palcolor_metacell = NULL, pt.size = 1.2, pt.alpha = 1, cell.alpha = 1, cell.size = 0.7, stroke = 0.5, show_metacell_size = TRUE, metacell_size_range = NULL, cell_param = list(), metacell_param = list(), legend.position = "right", legend.direction = "vertical", theme_use = "theme_scop", theme_args = list(), return_layer = FALSE, ... )
```

## Parameters

- `srt`: A Seurat object with metacell results from RunMetaCell().
- `reduction`: Which dimensionality reduction to use. If not specified, will use the reduction returned by DefaultReduction.
- `show_cells`: Logical. If TRUE, the original single-cell points are drawn as a semi-transparent background layer behind the metacell centroids.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `color.by`: Metadata column in the metacell Seurat used to color centroids. If NULL, metacell centroids use one fixed color.
- `dims`: Dimensions to plot, must be a two-length numeric vector specifying x- and y-dimensions
- `label`: Whether to label the cell groups.
- `palette`: Color palette name. Available palettes can be found in [thisplot:show_palettes]{thisplot::show_palettes}. Default is "Chinese".
- `palcolor`: Custom colors used to create a color palette. Default is NULL.
- `palette_metacell`: Color palette for the metacell centroid layer. Default is "Chinese".
- `palcolor_metacell`: Custom colors for the metacell centroid layer.
- `pt.size`: The size of the points in the plot. Default is NULL, which automatically scales point diameter with the square root of the number of plotted cells while keeping a readable minimum size of 0.3. Automatically sized raster plots use at least a two-pixel radius at the reference raster.dpi = c(512, 512). Point sizes are scaled with raster.dpi, so their relative appearance remains stable when the raster resolution changes. Non-raster point sizes use fixed physical units; increase pt.size proportionally when exporting to an unusually large canvas.
- `pt.alpha`: The transparency of the data points. Default is 1.
- `cell.alpha`: Alpha value for the original single-cell background layer.
- `cell.size`: Point size for the original single-cell background layer.
- `stroke`: Point border stroke width for metacell centroids.
- `show_metacell_size`: Whether to map metacell_size to centroid size.
- `metacell_size_range`: Point-size range used when show_metacell_size = TRUE.
- `cell_param`: A named list of extra arguments passed to {[=CellDimPlot]{CellDimPlot()}} for the original single-cell background layer.
- `metacell_param`: A named list of extra arguments passed to {[=CellDimPlot]{CellDimPlot()}} for the metacell centroid/query layer.
- `legend.position`: The position of legends, one of "none", "left", "right", "bottom", "top". Default is "right".
- `legend.direction`: The direction of the legend in the plot. Can be one of "vertical" or "horizontal".
- `theme_use`: Theme used. Can be a character string or a theme function. Default is "theme_scop".
- `theme_args`: Other arguments passed to the theme_use. Default is list().
- `return_layer`: Logical. If TRUE, returns a named list of ggplot2 layers/scales (cells, fill_scale, centroids, scale_fill, scale_size, labels) instead of a complete plot.
- `...`: Additional arguments passed to {[ggplot2:geom_point]{geom_point()}} for metacell centroids.

## Full Documentation

# Visualize metacell partitions on a dimensionality reduction

## Usage

```text
MetaCellPlot( srt, reduction = NULL, show_cells = FALSE, group.by = NULL, color.by = NULL, dims = c(1, 2), label = FALSE, palette = "Chinese", palcolor = NULL, palette_metacell = "Chinese", palcolor_metacell = NULL, pt.size = 1.2, pt.alpha = 1, cell.alpha = 1, cell.size = 0.7, stroke = 0.5, show_metacell_size = TRUE, metacell_size_range = NULL, cell_param = list(), metacell_param = list(), legend.position = "right", legend.direction = "vertical", theme_use = "theme_scop", theme_args = list(), return_layer = FALSE, ... )
```

## Description

Visualize metacell partitions on a dimensionality reduction

## Value

A ggplot object, or a named list of ggplot2 layers when return_layer = TRUE.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub, verbose = FALSE)
mc <- RunMetaCell(
  pancreas_sub,
  method = "supercell",
  gamma = 20
)

MetaCellPlot(
  mc,
  group.by = "CellType",
  palette_metacell = "ChineseSet8"
)

MetaCellPlot(
  mc,
  group.by = "CellType",
  reduction = "umap",
  palette = "ChineseSet8",
  show_cells = TRUE
)

CellDimPlot(
  pancreas_sub,
  group.by = "CellType"
) +
  MetaCellPlot(
    mc,
    group.by = "CellType",
    return_layer = TRUE,
    palette_metacell = "ChineseSet8"
  )
```
