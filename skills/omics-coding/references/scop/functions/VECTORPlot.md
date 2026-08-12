# Plot VECTOR results

- Package: scop
- Language: R
- Function: `VECTORPlot`
- Source: https://mengxu98.github.io/scop/reference/VECTORPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/VECTORPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualize VECTOR grid-level scores or direction arrows on the embedding used by {[=RunVECTOR]{RunVECTOR()}}.

## Signature

```text
VECTORPlot( object, plot_type = c("grid", "raw"), tool_name = "VECTOR", score.name = "VECTOR_Score", group.by = NULL, background = c("auto", "score", "group", "none"), point.size = NULL, point.alpha = 0.7, grid.size = 2, arrow.linewidth = 0.5, arrow.length = grid::unit(0.035, "inches"), arrow.angle = 20, arrow.color = "grey20", title = NULL, subtitle = NULL, xlab = NULL, ylab = NULL, aspect.ratio = 1, legend.position = "right", legend.direction = "vertical", theme_use = "theme_scop", theme_args = list(), ... )
```

## Parameters

- `object`: A Seurat object processed by {[=RunVECTOR]{RunVECTOR()}}.
- `plot_type`: Plot type. "grid" colors occupied grid centers by grid score, and "raw" draws VelocityPlot-style grid arrows.
- `tool_name`: Name used in srt@tools.
- `score.name`: Metadata column containing VECTOR scores.
- `group.by`: Optional metadata column used as the background cell color for direction-field plots.
- `background`: Background for plots. "score" uses {[=FeatureDimPlot]{FeatureDimPlot()}}, "group" uses {[=CellDimPlot]{CellDimPlot()}} and requires group.by, and "none" draws the flow field without cell points.
- `point.size`: Cell point size. If NULL, uses the same default as {[=FeatureDimPlot]{FeatureDimPlot()}}.
- `point.alpha`: Cell point alpha.
- `grid.size`: Grid-center point size.
- `arrow.linewidth`: Direction arrow line width.
- `arrow.length`: Arrow head length passed to {[grid:arrow]{grid::arrow()}}.
- `arrow.angle`: Arrow head angle passed to {[grid:arrow]{grid::arrow()}}.
- `arrow.color`: Direction arrow color.
- `title, subtitle, xlab, ylab`: Plot labels. By default no title is shown.
- `aspect.ratio`: Fixed aspect ratio.
- `legend.position, legend.direction`: Legend position and direction.
- `theme_use, theme_args`: Theme function and arguments.
- `...`: Additional arguments passed to {[=FeatureDimPlot]{FeatureDimPlot()}} or {[=CellDimPlot]{CellDimPlot()}} when a cell background is requested.

## Full Documentation

# Plot VECTOR results

## Usage

```text
VECTORPlot( object, plot_type = c("grid", "raw"), tool_name = "VECTOR", score.name = "VECTOR_Score", group.by = NULL, background = c("auto", "score", "group", "none"), point.size = NULL, point.alpha = 0.7, grid.size = 2, arrow.linewidth = 0.5, arrow.length = grid::unit(0.035, "inches"), arrow.angle = 20, arrow.color = "grey20", title = NULL, subtitle = NULL, xlab = NULL, ylab = NULL, aspect.ratio = 1, legend.position = "right", legend.direction = "vertical", theme_use = "theme_scop", theme_args = list(), ... )
```

## Description

Visualize VECTOR grid-level scores or direction arrows on the embedding used by {[=RunVECTOR]{RunVECTOR()}}.

## Value

A ggplot object.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunVECTOR(pancreas_sub, verbose = FALSE)
VECTORPlot(pancreas_sub, plot_type = "grid")
VECTORPlot(pancreas_sub, plot_type = "raw", group.by = "SubCellType")
```
