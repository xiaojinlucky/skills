# ESTIMATE score plots

- Package: scop
- Language: R
- Function: `EstimateScorePlot`
- Source: https://mengxu98.github.io/scop/reference/EstimateScorePlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/EstimateScorePlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualize ESTIMATE stromal, immune, combined ESTIMATE, and tumor-purity scores from a RunESTIMATE() result.

## Signature

```text
EstimateScorePlot( object = NULL, score.data = NULL, group.by = NULL, group.data = NULL, plot_type = c("violin", "box", "heatmap", "cor"), scores = c("StromalScore", "ImmuneScore", "ESTIMATEScore", "TumorPurity"), add_stat = TRUE, ... )
```

## Parameters

- `object`: Optional RunESTIMATE() bundle, SummarizedExperiment, or Seurat object containing ESTIMATE results.
- `score.data`: Optional score matrix or data frame with samples in rows.
- `group.by`: Optional grouping column for grouped violin and box plots.
- `group.data`: Optional named vector or data frame containing sample groups.
- `plot_type`: Plot type.
- `scores`: ESTIMATE score columns to plot.
- `add_stat`: Whether to add group comparison labels to violin or box plots. Requires ggpubr.
- `...`: Additional plotting arguments.

## Full Documentation

# ESTIMATE score plots

## Usage

```text
EstimateScorePlot( object = NULL, score.data = NULL, group.by = NULL, group.data = NULL, plot_type = c("violin", "box", "heatmap", "cor"), scores = c("StromalScore", "ImmuneScore", "ESTIMATEScore", "TumorPurity"), add_stat = TRUE, ... )
```

## Description

Visualize ESTIMATE stromal, immune, combined ESTIMATE, and tumor-purity scores from a RunESTIMATE() result.

## Value

A ggplot object.
