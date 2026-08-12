# Dimension estimate diagnostic plot

- Package: scop
- Language: R
- Function: `DimsEstimatePlot`
- Source: https://mengxu98.github.io/scop/reference/DimsEstimatePlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/DimsEstimatePlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Dimension estimate diagnostic plot

## Signature

```text
DimsEstimatePlot( srt, max_pcs = 50, variance_thresholds = c(0.6, 0.7, 0.8, 0.9), reduction = NULL, palcolor = c("#D70440", "#0AA344", "#1772B4"), aspect.ratio = NULL, title = NULL, subtitle = NULL, xlab = "Principal component", theme_use = "theme_scop", theme_args = list(), seed = 11, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object with a PCA-like reduction computed.
- `max_pcs`: Maximum number of PCs to visualize. Default is 50.
- `variance_thresholds`: Numeric vector of variance thresholds to mark. Default is c(0.60, 0.70, 0.80, 0.90).
- `reduction`: Reduction name to inspect. Default is NULL, which automatically selects a PCA-like reduction via {[=DefaultReduction]{DefaultReduction()}} with pattern = "pca".
- `palcolor`: Colors for the selected-PC line, curves, and bars, respectively. Default is c("#D70440", "#0AA344", "#1772B4").
- `aspect.ratio`: Aspect ratio of the plot. Default is NULL.
- `title`: Plot title. When NULL (default), reports the selected number of PCs.
- `subtitle`: Plot subtitle. Default is NULL.
- `xlab`: X-axis label. Default is "Principal component".
- `theme_use`: Theme function used to style the plot. Default is "theme_scop".
- `theme_args`: Other arguments passed to the theme_use.
- `seed`: Random seed. Default is 11.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Dimension estimate diagnostic plot

## Usage

```text
DimsEstimatePlot( srt, max_pcs = 50, variance_thresholds = c(0.6, 0.7, 0.8, 0.9), reduction = NULL, palcolor = c("#D70440", "#0AA344", "#1772B4"), aspect.ratio = NULL, title = NULL, subtitle = NULL, xlab = "Principal component", theme_use = "theme_scop", theme_args = list(), seed = 11, verbose = TRUE )
```

## Description

Dimension estimate diagnostic plot

## Value

A ggplot object showing per-PC explained variance (bars, left axis) and cumulative explained variance (line, right axis).

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
DimsEstimatePlot(pancreas_sub)
```
