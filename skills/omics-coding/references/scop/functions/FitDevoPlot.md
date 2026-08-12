# Plot FitDevo results

- Package: scop
- Language: R
- Function: `FitDevoPlot`
- Source: https://mengxu98.github.io/scop/reference/FitDevoPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/FitDevoPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualize FitDevo developmental potential scores with scop dimensional and grouped summary plots.

## Signature

```text
FitDevoPlot( srt, reduction = NULL, group.by = NULL, score.name = "FitDevo_Score", relative.name = "FitDevo_Relative", combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), ... )
```

## Parameters

- `srt`: A Seurat object processed by {[=RunFitDevo]{RunFitDevo()}}.
- `reduction`: Reduction used by {[=FeatureDimPlot]{FeatureDimPlot()}} and {[=CellDimPlot]{CellDimPlot()}}.
- `group.by`: Optional metadata column used for phenotype and score distribution plots.
- `score.name`: Metadata column containing the FitDevo score.
- `relative.name`: Metadata column containing the FitDevo relative rank.
- `combine`: Whether to combine plots with patchwork.
- `nrow, ncol, byrow`: Layout arguments passed to {[patchwork:wrap_plots]{patchwork::wrap_plots()}}.
- `pt.size, pt.alpha`: Point size and alpha.
- `palette, palcolor`: Palette arguments for grouped plots.
- `theme_use, theme_args`: Theme arguments passed to scop plot helpers.
- `...`: Additional arguments passed to {[=FeatureDimPlot]{FeatureDimPlot()}} and {[=CellDimPlot]{CellDimPlot()}}.

## Full Documentation

# Plot FitDevo results

## Usage

```text
FitDevoPlot( srt, reduction = NULL, group.by = NULL, score.name = "FitDevo_Score", relative.name = "FitDevo_Relative", combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), ... )
```

## Description

Visualize FitDevo developmental potential scores with scop dimensional and grouped summary plots.

## Value

A patchwork object or a named list of ggplot objects.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunFitDevo(pancreas_sub, verbose = FALSE)
FitDevoPlot(pancreas_sub)
```
