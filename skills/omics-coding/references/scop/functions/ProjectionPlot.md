# Projection Plot

- Package: scop
- Language: R
- Function: `ProjectionPlot`
- Source: https://mengxu98.github.io/scop/reference/ProjectionPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/ProjectionPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

This function generates a projection plot, which can be used to compare two groups of cells in a dimensionality reduction space.

## Signature

```text
ProjectionPlot( srt_query, srt_ref, query_group = NULL, ref_group = NULL, query_reduction = "ref.embeddings", ref_reduction = srt_query[[query_reduction]]@misc[["reduction.model"]] %||% NULL, query_param = list(palette = "Set1", cells.highlight = TRUE), ref_param = list(palette = "Chinese"), xlim = NULL, ylim = NULL, pt.size = 0.8, stroke.highlight = 0.5, verbose = TRUE )
```

## Parameters

- `srt_query`: An object of class Seurat to be annotated with cell types.
- `srt_ref`: A Seurat object or count matrix representing the reference object. If provided, the similarities will be calculated between cells from the query and reference objects. If not provided, the similarities will be calculated within the query object.
- `query_group`: The grouping variable for the query group cells.
- `ref_group`: The grouping variable for the reference group cells.
- `query_reduction`: The name of the reduction in the query group cells.
- `ref_reduction`: The name of the reduction in the reference group cells.
- `query_param`: A list of parameters for customizing the query group plot. Available parameters: palette (color palette for groups) and cells.highlight (whether to highlight cells).
- `ref_param`: A list of parameters for customizing the reference group plot. Available parameters: palette (color palette for groups) and cells.highlight (whether to highlight cells).
- `xlim`: The x-axis limits for the plot. If not provided, the limits will be calculated based on the data.
- `ylim`: The y-axis limits for the plot. If not provided, the limits will be calculated based on the data.
- `pt.size`: The size of the points in the plot. Default is NULL, which automatically scales point diameter with the square root of the number of plotted cells while keeping a readable minimum size of 0.3. Automatically sized raster plots use at least a two-pixel radius at the reference raster.dpi = c(512, 512). Point sizes are scaled with raster.dpi, so their relative appearance remains stable when the raster resolution changes. Non-raster point sizes use fixed physical units; increase pt.size proportionally when exporting to an unusually large canvas.
- `stroke.highlight`: The size of the stroke highlight for cells.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Projection Plot

## Usage

```text
ProjectionPlot( srt_query, srt_ref, query_group = NULL, ref_group = NULL, query_reduction = "ref.embeddings", ref_reduction = srt_query[[query_reduction]]@misc[["reduction.model"]] %||% NULL, query_param = list(palette = "Set1", cells.highlight = TRUE), ref_param = list(palette = "Chinese"), xlim = NULL, ylim = NULL, pt.size = 0.8, stroke.highlight = 0.5, verbose = TRUE )
```

## Description

This function generates a projection plot, which can be used to compare two groups of cells in a dimensionality reduction space.

## Examples

```r
data(panc8_sub)
panc8_sub <- RunStandardWorkflow(panc8_sub)
srt_ref <- panc8_sub[, panc8_sub$tech != "fluidigmc1"]
srt_query <- panc8_sub[, panc8_sub$tech == "fluidigmc1"]
srt_ref <- RunIntegration(
  srt_ref,
  batch = "tech",
  integration_method = "Uncorrected"
)
CellDimPlot(
  srt_ref,
  group.by = c("celltype", "tech")
)

# Projection
srt_query <- RunKNNMap(
  srt_query = srt_query,
  srt_ref = srt_ref,
  ref_umap = "UncorrectedUMAP2D"
)
ProjectionPlot(
  srt_query = srt_query,
  srt_ref = srt_ref,
  query_group = "celltype",
  ref_group = "celltype"
)
```
