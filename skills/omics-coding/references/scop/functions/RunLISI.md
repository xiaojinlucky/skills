# Compute LISI scores on a Seurat object

- Package: scop
- Language: R
- Function: `RunLISI`
- Source: https://mengxu98.github.io/scop/reference/RunLISI.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunLISI.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute per-cell Local Inverse Simpson's Index (LISI) scores from a dimensional reduction and store them in the meta.data and tools slots of a Seurat object.

## Signature

```text
RunLISI( srt, reductions = NULL, reduction = NULL, dims = NULL, label_colnames = NULL, prefix = NULL, tool_name = NULL, perplexity = 30, tol = 1e-05, max_iter = 50, overwrite = TRUE, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `reductions`: Character vector of dimensional reductions used to compute LISI. If NULL, {[=DefaultReduction]{DefaultReduction()}} is used.
- `reduction`: Deprecated alias of reductions.
- `dims`: Dimensions to use from the reduction. Default is NULL, which uses all available dimensions.
- `label_colnames`: Character vector of metadata columns used for LISI. If NULL, RunLISI() will try to use srt@misc[["integration_batch"]].
- `prefix`: Prefix used for the stored LISI metadata columns. If NULL, the reduction names are used.
- `tool_name`: Name used to store detailed results in srt@tools. Default is "LISI" when multiple reductions are provided, otherwise paste0(prefix, "_LISI").
- `perplexity`: Effective neighborhood size. Default is 30.
- `tol`: Tolerance used in the binary search for the target perplexity. Default is 1e-5.
- `max_iter`: Maximum number of binary-search iterations. Default is 50.
- `overwrite`: Whether to overwrite existing metadata columns. Default is TRUE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Compute LISI scores on a Seurat object

## Usage

```text
RunLISI( srt, reductions = NULL, reduction = NULL, dims = NULL, label_colnames = NULL, prefix = NULL, tool_name = NULL, perplexity = 30, tol = 1e-05, max_iter = 50, overwrite = TRUE, verbose = TRUE )
```

## Description

Compute per-cell Local Inverse Simpson's Index (LISI) scores from a dimensional reduction and store them in the meta.data and tools slots of a Seurat object.

## Value

A modified Seurat object.

## Examples

```r
data(panc8_sub)
set.seed(1)
demo_embedding <- matrix(
  stats::rnorm(ncol(panc8_sub) * 5),
  nrow = ncol(panc8_sub),
  dimnames = list(colnames(panc8_sub), paste0("DEMO_", 1:5))
)
panc8_sub[["demo"]] <- SeuratObject::CreateDimReducObject(
  embeddings = demo_embedding,
  key = "DEMO_",
  assay = SeuratObject::DefaultAssay(panc8_sub)
)
names(panc8_sub@reductions)

panc8_sub <- RunLISI(
  panc8_sub,
  reductions = "demo",
  label_colnames = "tech",
  perplexity = 10
)
LISIPlot(
  panc8_sub,
  combine = TRUE
)
```
