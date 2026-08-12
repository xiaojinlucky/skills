# Plot benchmark metrics

- Package: scop
- Language: R
- Function: `BenchmarkPlot`
- Source: https://mengxu98.github.io/scop/reference/BenchmarkPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/BenchmarkPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Visualize benchmark results stored in a Seurat object, a summary data.frame, or a benchmark_result object created by {[=RunBenchmark]{RunBenchmark()}}. Spatial benchmark results default to a publication-oriented overview that pairs clustering quality with runtime and peak-memory efficiency. Per-cell metrics such as LISI remain available as feature plots and boxplots.

## Signature

```text
BenchmarkPlot( srt = NULL, data = NULL, features = NULL, metrics = NULL, tool_name = NULL, reduction = NULL, plot_type = c("auto", "overview", "quality", "efficiency", "heatmap", "feature", "boxplot", "bar", "funkyheatmap"), sort_by = c("quality", "method", "runtime", "memory"), show_values = TRUE, show_status = TRUE, resource_scale = c("auto", "linear", "log10"), plot_boxplot = TRUE, boxplot_jitter = FALSE, combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `data`: Optional benchmark_result object or summary benchmark data.frame containing at least metric and value, and optionally method, workflow, and direction.
- `features`: Metadata columns containing per-cell benchmark scores. Default is NULL.
- `metrics`: One or more summary metric names to visualize. Default is NULL, which uses all available summary metrics.
- `tool_name`: Tool entries created by benchmark-related workflows. This can be a character vector. For per-cell metrics, benchmark columns are resolved from tool entries that contain colnames; for summary metrics, entries containing summary or metrics$summary are used.
- `reduction`: Dimensional reduction used for per-cell feature plots. Default is NULL, which uses the reduction stored in tool_name when available, otherwise {[=DefaultReduction]{DefaultReduction()}}.
- `plot_type`: Plot type. "overview", "quality", "efficiency", and "heatmap" consume benchmark_result results. Existing "feature", "boxplot", "bar", and "funkyheatmap" modes remain supported.
- `sort_by`: Method ordering for spatial benchmark plots. "quality" sorts by the mean selected quality metric; other choices sort by method, runtime, or peak memory.
- `show_values`: Whether to print raw metric values on quality and heatmap panels.
- `show_status`: Whether the overview should add a status strip for failed, unavailable, or timed-out methods.
- `resource_scale`: Resource-axis transformation. "auto" independently uses log10 for runtime or memory when positive values span at least tenfold.
- `plot_boxplot`: Whether to add the summary boxplot when per-cell metrics are shown. Default is TRUE.
- `boxplot_jitter`: Whether to overlay jittered points on the boxplot. Default is FALSE.
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

# Plot benchmark metrics

## Usage

```text
BenchmarkPlot( srt = NULL, data = NULL, features = NULL, metrics = NULL, tool_name = NULL, reduction = NULL, plot_type = c("auto", "overview", "quality", "efficiency", "heatmap", "feature", "boxplot", "bar", "funkyheatmap"), sort_by = c("quality", "method", "runtime", "memory"), show_values = TRUE, show_status = TRUE, resource_scale = c("auto", "linear", "log10"), plot_boxplot = TRUE, boxplot_jitter = FALSE, combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), verbose = TRUE, ... )
```

## Description

Visualize benchmark results stored in a Seurat object, a summary data.frame, or a benchmark_result object created by {[=RunBenchmark]{RunBenchmark()}}. Spatial benchmark results default to a publication-oriented overview that pairs clustering quality with runtime and peak-memory efficiency. Per-cell metrics such as LISI remain available as feature plots and boxplots.

## Value

A ggplot, patchwork plot, or funkyheatmap object depending on the selected mode. If combine = FALSE in per-cell mode, a named list of plots is returned.

## Examples

```r
metrics_df <- data.frame(
  method = c("Raw", "Raw", "Harmony", "Harmony"),
  metric = c("batch_ASW_mixing", "celltype_ASW", "batch_ASW_mixing", "celltype_ASW"),
  value = c(0.42, 0.71, 0.68, 0.66)
)
BenchmarkPlot(
  data = metrics_df,
  plot_type = "bar"
)

data("pbmcmultiome_sub", package = "scop")
pbmcmultiome_sub[["MethodA_batch_LISI"]] <-
  seq_len(ncol(pbmcmultiome_sub)) / ncol(pbmcmultiome_sub)
pbmcmultiome_sub[["MethodB_batch_LISI"]] <-
  rev(pbmcmultiome_sub[["MethodA_batch_LISI", drop = TRUE]])
BenchmarkPlot(
  pbmcmultiome_sub,
  features = c("MethodA_batch_LISI", "MethodB_batch_LISI"),
  plot_type = "boxplot"
)
```
