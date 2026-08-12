# 3D-Dimensional reduction plot for cell classification visualization.

- Package: scop
- Language: R
- Function: `CellDimPlot3D`
- Source: https://mengxu98.github.io/scop/reference/CellDimPlot3D.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CellDimPlot3D.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plotting cell points on a reduced 3D space and coloring according to the groups of the cells.

## Signature

```text
CellDimPlot3D( srt, group.by, plot_type = c("scatter", "density_surface"), reduction = NULL, dims = c(1, 2, 3), axis_labs = NULL, palette = "Chinese", palcolor = NULL, bg_color = "grey80", pt.size = 1.5, cells.highlight = NULL, cols.highlight = "black", shape.highlight = "circle-open", sizes.highlight = 2, lineages = NULL, lineages_palette = "Dark2", density_n = 200, density_bandwidth = 1, density_threshold = 0.018, density_power = 0.52, density_colors = c("#ffffff", "#edf9fa", "#c7e6ed", "#7faac2", "#294a74", "#11162f", "#7f1025", "#ef3b2c"), density_color_stops = c(0, 0.02, 0.12, 0.35, 0.62, 0.82, 0.93, 1), density_surface_opacity = 0.78, density_label = FALSE, density_label_color = TRUE, density_label_top_n = Inf, density_label_min_distance = 0.08, density_show_axes = TRUE, density_show_colorbar = TRUE, density_show_title = TRUE, span = 0.75, width = NULL, height = NULL, save = NULL, force = FALSE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `plot_type`: Plot type. "scatter" keeps the original 3D cell scatter, while "density_surface" draws an interactive 3D kernel-density surface from the first two requested dimensions.
- `reduction`: Which dimensionality reduction to use. If not specified, will use the reduction returned by DefaultReduction.
- `dims`: Dimensions to plot. For plot_type = "scatter", this must be a three-length numeric vector specifying x-, y- and z-dimensions. For plot_type = "density_surface", the first two dimensions are used as x and y, and density is drawn on the z-axis.
- `axis_labs`: A character vector of length 3 indicating the labels for the axes.
- `palette`: Color palette name. Available palettes can be found in [thisplot:show_palettes]{thisplot::show_palettes}. Default is "Chinese".
- `palcolor`: Custom colors used to create a color palette. Default is NULL.
- `bg_color`: Color value for background(NA) points.
- `pt.size`: The size of the points in the plot. Default is NULL, which automatically scales point diameter with the square root of the number of plotted cells while keeping a readable minimum size of 0.3. Automatically sized raster plots use at least a two-pixel radius at the reference raster.dpi = c(512, 512). Point sizes are scaled with raster.dpi, so their relative appearance remains stable when the raster resolution changes. Non-raster point sizes use fixed physical units; increase pt.size proportionally when exporting to an unusually large canvas.
- `cells.highlight`: A logical or character vector specifying the cells to highlight in the plot. If TRUE, all cells are highlighted. If FALSE, no cells are highlighted. Default is NULL.
- `cols.highlight`: Color used to highlight the cells.
- `shape.highlight`: Shape of the cell to highlight. See https://plotly.com/r/reference/scattergl/#scattergl-marker-symbol{scattergl-marker-symbol}
- `sizes.highlight`: Size of highlighted cell points.
- `lineages`: Lineages/pseudotime to add to the plot. If specified, curves will be fitted using [stats:loess]{stats::loess} method.
- `lineages_palette`: Color palette used for lineages.
- `density_n`: Grid size used by MASS::kde2d() for plot_type = "density_surface".
- `density_bandwidth`: Bandwidth passed to MASS::kde2d(). A single value scales the default x and y bandwidth; a two-length vector supplies absolute x and y bandwidths.
- `density_threshold`: Relative density values below this cutoff are removed from the surface.
- `density_power`: Power transform applied to relative density before plotting. Values below 1 broaden peaks.
- `density_colors`: Colors used for the density surface. The last colors are reserved for the highest density peaks.
- `density_color_stops`: Numeric stops between 0 and 1 for density_colors. By default, red is reserved for the highest density peaks.
- `density_surface_opacity`: Opacity for density surfaces.
- `density_label`: Whether to add group labels to the density surface.
- `density_label_color`: Whether group labels use the same palette as CellDimPlot().
- `density_label_top_n`: Maximum number of group labels to draw.
- `density_label_min_distance`: Minimum distance between labels in the x-y embedding space, expressed as a fraction of the larger embedding range.
- `density_show_axes, density_show_colorbar, density_show_title`: Whether to show axes, colorbar, and title for plot_type = "density_surface".
- `span`: The span of the loess smoother for lineages line.
- `width`: Width in pixels, defaults to automatic sizing.
- `height`: Height in pixels, defaults to automatic sizing.
- `save`: The name of the file to save the plot to. Must end in ".html".
- `force`: Whether to force drawing regardless of maximum levels in any cell group is greater than 100. Default is FALSE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# 3D-Dimensional reduction plot for cell classification visualization.

## Usage

```text
CellDimPlot3D( srt, group.by, plot_type = c("scatter", "density_surface"), reduction = NULL, dims = c(1, 2, 3), axis_labs = NULL, palette = "Chinese", palcolor = NULL, bg_color = "grey80", pt.size = 1.5, cells.highlight = NULL, cols.highlight = "black", shape.highlight = "circle-open", sizes.highlight = 2, lineages = NULL, lineages_palette = "Dark2", density_n = 200, density_bandwidth = 1, density_threshold = 0.018, density_power = 0.52, density_colors = c("#ffffff", "#edf9fa", "#c7e6ed", "#7faac2", "#294a74", "#11162f", "#7f1025", "#ef3b2c"), density_color_stops = c(0, 0.02, 0.12, 0.35, 0.62, 0.82, 0.93, 1), density_surface_opacity = 0.78, density_label = FALSE, density_label_color = TRUE, density_label_top_n = Inf, density_label_min_distance = 0.08, density_show_axes = TRUE, density_show_colorbar = TRUE, density_show_title = TRUE, span = 0.75, width = NULL, height = NULL, save = NULL, force = FALSE, verbose = TRUE )
```

## Description

Plotting cell points on a reduced 3D space and coloring according to the groups of the cells.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(
  pancreas_sub,
  nonlinear_reduction_dims = 3
)
CellDimPlot3D(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "StandardpcaUMAP3D"
)

CellDimPlot3D(
  pancreas_sub,
  group.by = "SubCellType",
  plot_type = "density_surface",
  reduction = "umap",
  dims = c(1, 2),
  density_label = TRUE
)

pancreas_sub <- RunSlingshot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "StandardpcaUMAP3D",
  show_plot = FALSE
)
CellDimPlot3D(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "StandardpcaUMAP3D",
  lineages = "Lineage1"
)
```
