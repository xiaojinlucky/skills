# Plot STdeconvolve topic proportions

- Package: scop
- Language: R
- Function: `STdeconvolvePlot`
- Source: https://mengxu98.github.io/scop/reference/STdeconvolvePlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/STdeconvolvePlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot schema-v1 topic proportions without rerunning the optional backend. Multi-topic point maps use one shared proportion scale and reserve title space above the automatic layout.

## Signature

```text
STdeconvolvePlot( srt, tool_name = "STdeconvolve", topics = NULL, prefix = NULL, plot_type = c("point", "pie"), combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `tool_name`: Exact schema-v1 result key written by RunSTdeconvolve().
- `topics`: Topic names, topic numbers, or metadata columns to plot. If NULL, all topics in the stored result are used.
- `prefix`: Metadata prefix used by RunSTdeconvolve(). If NULL, the prefix is read from the stored result.
- `plot_type`: Plot type. "point" keeps the default spot plot behavior. "pie" draws spot-level pies from numeric metadata columns supplied to group.by or from a numeric matrix/data.frame supplied to values. When group.by is a single "<prefix>_dominant_type" column, matching "<prefix>_prop_*" or "<prefix>_frac_*" numeric metadata columns are used automatically.
- `combine`: Whether to combine point plots. If FALSE, a named list of plots is returned.
- `nrow, ncol, byrow`: Point-plot layout controls. When both nrow and ncol are NULL, a near-square layout with at most three columns is used.
- `...`: Additional arguments passed to SpatialSpotPlot().

## Full Documentation

# Plot STdeconvolve topic proportions

## Usage

```text
STdeconvolvePlot( srt, tool_name = "STdeconvolve", topics = NULL, prefix = NULL, plot_type = c("point", "pie"), combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, ... )
```

## Description

Plot schema-v1 topic proportions without rerunning the optional backend. Multi-topic point maps use one shared proportion scale and reserve title space above the automatic layout.

## Value

A ggplot, patchwork, or list of ggplot objects.

## Examples

```r
thisutils::check_r("JEFworks-Lab/STdeconvolve", verbose = FALSE)
data(visium_human_pancreas_sub)
spatial <- RunSTdeconvolve(
  visium_human_pancreas_sub,
  assay = "Spatial",
  features = rownames(visium_human_pancreas_sub)[1:300],
  k = 3,
  prefix = "STFull",
  tool_name = "STdeconvolveFull",
  verbose = FALSE
)
STdeconvolvePlot(
  spatial,
  tool_name = "STdeconvolveFull",
  topics = 1:2,
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)
```
