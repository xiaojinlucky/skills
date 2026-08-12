# Plot scPagwas Scores

- Package: scop
- Language: R
- Function: `PlotscPagwas`
- Source: https://mengxu98.github.io/scop/reference/PlotscPagwas.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/PlotscPagwas.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot the score and adjusted p-value metadata produced by {[=RunscPagwas]{RunscPagwas()}} on an existing Seurat reduction. The plots are returned and can optionally be saved as PDF files.

## Signature

```text
PlotscPagwas( srt, reduction = c("umap", "tsne"), features = NULL, p_threshold = 0.05, output.dir = NULL, width = 7, height = 7, point_size = NULL, palette = "Spectral", palcolor = NULL, significance_palette = "Chinese", significance_palcolor = NULL, do_plot = TRUE )
```

## Parameters

- `srt`: A Seurat object returned by {[=RunscPagwas]{RunscPagwas()}}.
- `reduction`: Reduction used for plotting, either "umap" or "tsne".
- `features`: Numeric scPagwas metadata columns to plot. By default, available gPAS, TRS, and down-TRS score columns are used.
- `p_threshold`: Adjusted p-value threshold used to identify significant cells. Set to NULL to omit the significance plot.
- `output.dir`: Optional directory in which to save PDF files.
- `width, height`: PDF dimensions in inches.
- `point_size`: Point size passed to {[=FeatureDimPlot]{FeatureDimPlot()}} and {[=CellDimPlot]{CellDimPlot()}}.
- `palette, palcolor`: Palette used for continuous scPagwas scores, passed to {[=FeatureDimPlot]{FeatureDimPlot()}}.
- `significance_palette, significance_palcolor`: Palette used for the significance groups, passed to {[=CellDimPlot]{CellDimPlot()}}.
- `do_plot`: Whether to print each plot.

## Full Documentation

# Plot scPagwas Scores

## Usage

```text
PlotscPagwas( srt, reduction = c("umap", "tsne"), features = NULL, p_threshold = 0.05, output.dir = NULL, width = 7, height = 7, point_size = NULL, palette = "Spectral", palcolor = NULL, significance_palette = "Chinese", significance_palcolor = NULL, do_plot = TRUE )
```

## Description

Plot the score and adjusted p-value metadata produced by {[=RunscPagwas]{RunscPagwas()}} on an existing Seurat reduction. The plots are returned and can optionally be saved as PDF files.

## Value

A named list of ggplot objects.
