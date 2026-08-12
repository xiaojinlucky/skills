# Plot CytoTRACE 2 Results

- Package: scop
- Language: R
- Function: `CytoTRACEPlot`
- Source: https://mengxu98.github.io/scop/reference/CytoTRACEPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CytoTRACEPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot CytoTRACE 2 Results

## Signature

```text
CytoTRACEPlot( srt, reduction = NULL, group.by = NULL, combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `reduction`: Which dimensionality reduction to use. If not specified, will use the reduction returned by DefaultReduction.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
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
- `...`: Additional arguments to be passed to CellDimPlot and FeatureDimPlot.

## Full Documentation

# Plot CytoTRACE 2 Results

## Usage

```text
CytoTRACEPlot( srt, reduction = NULL, group.by = NULL, combine = TRUE, nrow = NULL, ncol = NULL, byrow = TRUE, pt.size = NULL, pt.alpha = 1, palette = "Chinese", palcolor = NULL, theme_use = "theme_scop", theme_args = list(), verbose = TRUE, ... )
```

## Description

Plot CytoTRACE 2 Results

## Value

If combine = TRUE, returns a patchwork object combining all plots. If combine = FALSE, returns a named list of ggplot objects: Score: UMAP plot colored by score computed by CytoTRACE2; Potency: UMAP plot colored by potency category computed by CytoTRACE2; Relative: UMAP plot colored by relative score computed by CytoTRACE2; Phenotype: UMAP plot colored by phenotype (if group.by is provided); Boxplot: Boxplot of score computed by CytoTRACE2 corresponding to phenotype (if group.by is provided).

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunCytoTRACE(
  pancreas_sub,
  species = "Mus_musculus",
  backend = "cpp"
)

CytoTRACEPlot(
  pancreas_sub,
  group.by = "CellType",
  xlab = "UMAP_1",
  ylab = "UMAP_2"
)

plots <- CytoTRACEPlot(
  pancreas_sub,
  group.by = "CellType",
  combine = FALSE
)
plots$Boxplot
```
