# Plot stored spatial deconvolution proportions

- Package: scop
- Language: R
- Function: `SpatialDeconvolutionPlot`
- Source: https://mengxu98.github.io/scop/reference/SpatialDeconvolutionPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SpatialDeconvolutionPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot spot-by-cell-type proportions stored by {[=RunRCTD]{RunRCTD()}}, {[=RunCARD]{RunCARD()}}, {[=RunSPOTlight]{RunSPOTlight()}}, or {[=RunSpatialDWLS]{RunSpatialDWLS()}}. The plot reads a schema-v1 result through {[=GetSpatialResult]{GetSpatialResult()}} and never reruns a deconvolution backend. {[=RunCSIDE]{RunCSIDE()}} is intentionally excluded because its output represents differential or context effects rather than cell-type proportions.

## Signature

```text
SpatialDeconvolutionPlot( srt, tool_name = NULL, cell_types = NULL, plot_type = c("point", "dominant", "pie"), combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, ... )
```

## Parameters

- `srt`: A spatial Seurat object containing a stored deconvolution result.
- `tool_name`: Exact key in srt@tools. If NULL, exactly one compatible stored result must be discoverable.
- `cell_types`: Optional cell types to display. The default uses all stored cell types.
- `plot_type`: Plot proportions as separate point maps, one dominant-type map derived from the stored proportions, or one spot-level pie map.
- `combine`: Whether to combine point maps. If FALSE, return a named list.
- `nrow, ncol, byrow`: Point-map layout controls. When both dimensions are NULL, a near-square layout with at most three columns is used.
- `...`: Additional arguments passed to {[=SpatialSpotPlot]{SpatialSpotPlot()}}.

## Full Documentation

# Plot stored spatial deconvolution proportions

## Usage

```text
SpatialDeconvolutionPlot( srt, tool_name = NULL, cell_types = NULL, plot_type = c("point", "dominant", "pie"), combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, ... )
```

## Description

Plot spot-by-cell-type proportions stored by {[=RunRCTD]{RunRCTD()}}, {[=RunCARD]{RunCARD()}}, {[=RunSPOTlight]{RunSPOTlight()}}, or {[=RunSpatialDWLS]{RunSpatialDWLS()}}. The plot reads a schema-v1 result through {[=GetSpatialResult]{GetSpatialResult()}} and never reruns a deconvolution backend. {[=RunCSIDE]{RunCSIDE()}} is intentionally excluded because its output represents differential or context effects rather than cell-type proportions.

## Value

A ggplot, patchwork, or named list of ggplot objects.

## Examples

```r
data(visium_human_pancreas_sub)
data(pancreas_sub)
shared <- head(intersect(
  rownames(visium_human_pancreas_sub),
  rownames(pancreas_sub)
), 40)
spatial <- RunSpatialDWLS(
  visium_human_pancreas_sub[shared, 1:20],
  reference = pancreas_sub,
  reference_label = "CellType",
  features = shared,
  coord.cols = c("x", "y"),
  normalize = FALSE,
  verbose = FALSE
)
SpatialDeconvolutionPlot(
  spatial,
  tool_name = "SpatialDWLS",
  cell_types = colnames(spatial@tools$SpatialDWLS$proportions)[1],
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)
```
