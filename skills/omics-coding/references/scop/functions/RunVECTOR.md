# Run VECTOR developmental direction inference

- Package: scop
- Language: R
- Function: `RunVECTOR`
- Source: https://mengxu98.github.io/scop/reference/RunVECTOR.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunVECTOR.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run VECTOR developmental direction inference

## Signature

```text
RunVECTOR( object, reduction = NULL, pca.reduction = "pca", dims = 1:2, pca.dims = 1:30, grid.n = 30, arrow.p = 0.9, arrow.ol = 1.5, score.name = "VECTOR_Score", tool_name = "VECTOR", verbose = TRUE, backend = c("cpp", "r") )
```

## Parameters

- `object`: A Seurat object or expression matrix with genes in rows and cells in columns.
- `reduction`: Embedding reduction used for the direction field.
- `pca.reduction`: PCA-like reduction used to score local polarization.
- `dims`: Dimensions from reduction.
- `pca.dims`: Dimensions from pca.reduction.
- `grid.n`: Number of bins per embedding axis.
- `arrow.p`: Distance decay parameter used by the original VECTOR arrow weighting. Larger values keep more distant grid centers influential.
- `arrow.ol`: Arrow vector length multiplier relative to grid spacing.
- `score.name`: Metadata column for the VECTOR score.
- `tool_name`: Name used in srt@tools.
- `verbose`: Whether to print progress messages.
- `backend`: Numerical backend for grid-arrow aggregation. "cpp" avoids materializing the full grid-to-grid distance matrix; "r" is retained as the reference implementation.

## Full Documentation

# Run VECTOR developmental direction inference

## Usage

```text
RunVECTOR( object, reduction = NULL, pca.reduction = "pca", dims = 1:2, pca.dims = 1:30, grid.n = 30, arrow.p = 0.9, arrow.ol = 1.5, score.name = "VECTOR_Score", tool_name = "VECTOR", verbose = TRUE, backend = c("cpp", "r") )
```

## Description

Run VECTOR developmental direction inference

## Value

A modified Seurat object.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunVECTOR(
  pancreas_sub,
  reduction = "umap",
  pca.reduction = "pca",
  verbose = FALSE
)
FeatureDimPlot(pancreas_sub, features = "VECTOR_Score")

VECTORPlot(pancreas_sub, plot_type = "grid")

VECTORPlot(
  pancreas_sub,
  plot_type = "raw",
  group.by = "SubCellType",
  background = "none"
)
```
