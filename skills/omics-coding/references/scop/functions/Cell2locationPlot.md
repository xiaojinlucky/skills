# Plot cell2location spatial results

- Package: scop
- Language: R
- Function: `Cell2locationPlot`
- Source: https://mengxu98.github.io/scop/reference/Cell2locationPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/Cell2locationPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot cell2location spatial results

## Signature

```text
Cell2locationPlot( srt, plot_type = c("proportion", "abundance", "dominant", "pie"), cell_types = NULL, prefix = "Cell2location", tool_name = "Cell2location", image = NULL, overlay_image = TRUE, coord.cols = c("col", "row"), ... )
```

## Parameters

- `srt`: A Seurat object returned by {[=RunCell2location]{RunCell2location()}}.
- `plot_type`: Result to draw: normalized proportion, q05 absolute abundance, dominant cell type, or a spot-level proportion pie.
- `cell_types`: Optional cell types to display for abundance, proportion, or pie plots.
- `prefix`: Metadata prefix used by {[=RunCell2location]{RunCell2location()}}.
- `tool_name`: Name of the srt@tools result entry.
- `image`: Name of the Seurat spatial image. Required when multiple images are present; a single image is selected automatically when NULL.
- `overlay_image`: Whether to draw the spatial image beneath spots.
- `coord.cols`: Metadata coordinate columns used when no image is available.
- `...`: Additional arguments passed to {[=SpatialSpotPlot]{SpatialSpotPlot()}}.

## Full Documentation

# Plot cell2location spatial results

## Usage

```text
Cell2locationPlot( srt, plot_type = c("proportion", "abundance", "dominant", "pie"), cell_types = NULL, prefix = "Cell2location", tool_name = "Cell2location", image = NULL, overlay_image = TRUE, coord.cols = c("col", "row"), ... )
```

## Description

Plot cell2location spatial results

## Value

A ggplot, patchwork, or list of plots.

## Examples

```r
\dontrun{
# Result from the official Human Lymph Node example in RunCell2location().
spatial <- readRDS("human_lymph_node_cell2location/official_human_lymph_node.rds")
selected <- names(sort(
  colMeans(spatial@tools$Cell2location$proportions),
  decreasing = TRUE
))[1:6]
Cell2locationPlot(
  spatial,
  plot_type = "proportion",
  cell_types = selected,
  overlay_image = FALSE,
  coord.cols = c("x", "y"),
  ncol = 3
)
Cell2locationPlot(
  spatial,
  plot_type = "dominant",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)
}
```
