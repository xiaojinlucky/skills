# Plot LISI scores

- Package: scop
- Language: R
- Function: `LISIPlot`
- Source: https://mengxu98.github.io/scop/reference/LISIPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/LISIPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Backward-compatible wrapper around {[=BenchmarkPlot]{BenchmarkPlot()}} for LISI scores. Visualize LISI scores on a dimensional reduction and compare methods with a summary boxplot.

## Signature

```text
LISIPlot( srt, features = NULL, tool_name = NULL, reduction = NULL, plot_boxplot = TRUE, boxplot_jitter = FALSE, combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `features`: Metadata columns containing LISI scores. Default is NULL, which will use columns stored in tool_name, or all metadata columns ending with "_LISI" when tool_name is NULL.
- `tool_name`: Tool entry created by {[=RunLISI]{RunLISI()}}. Default is NULL.
- `reduction`: Dimensional reduction used for feature plots. If NULL, the reduction recorded in tool_name is used when available; otherwise {[=DefaultReduction]{DefaultReduction()}} is used.
- `plot_boxplot`: Whether to add boxplots. Default is TRUE.
- `boxplot_jitter`: Whether to overlay jittered points on boxplots. Default is FALSE.
- `combine`: Combine plots into a single patchwork object. If FALSE, return a list of ggplot objects.
- `nrow`: Number of rows in the combined plot. Default is NULL, which means determined automatically based on the number of plots.
- `ncol`: Number of columns in the combined plot. Default is NULL, which means determined automatically based on the number of plots.
- `byrow`: Whether to arrange the plots by row in the combined plot. Default is TRUE.
- `pt.size`: The size of the points in the plot. Default is NULL, which automatically scales point diameter with the square root of the number of plotted cells while keeping a readable minimum size of 0.3. Automatically sized raster plots use at least a two-pixel radius at the reference raster.dpi = c(512, 512). Point sizes are scaled with raster.dpi, so their relative appearance remains stable when the raster resolution changes. Non-raster point sizes use fixed physical units; increase pt.size proportionally when exporting to an unusually large canvas.
- `pt.alpha`: The transparency of the data points. Default is 1.
- `palette`: Color palette name. Available palettes can be found in [thisplot:show_palettes]{thisplot::show_palettes}. Default is "Chinese".
- `palcolor`: Custom colors used to create a color palette. Default is NULL.
- `theme_use`: Theme used. Can be a character string or a theme function. Default is "theme_scop".
- `theme_args`: Other arguments passed to the theme_use. Default is list().
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: The message to print.

## Full Documentation

# Plot LISI scores

## Usage

```text
LISIPlot( srt, features = NULL, tool_name = NULL, reduction = NULL, plot_boxplot = TRUE, boxplot_jitter = FALSE, combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), verbose = TRUE, ... )
```

## Description

Backward-compatible wrapper around {[=BenchmarkPlot]{BenchmarkPlot()}} for LISI scores. Visualize LISI scores on a dimensional reduction and compare methods with a summary boxplot.

## Value

If combine = TRUE, returns a combined patchwork plot. If combine = FALSE, returns a named list of ggplot objects.
