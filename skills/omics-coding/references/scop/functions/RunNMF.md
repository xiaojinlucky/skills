# Run NMF (non-negative matrix factorization)

- Package: scop
- Language: R
- Function: `RunNMF`
- Source: https://mengxu98.github.io/scop/reference/RunNMF.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunNMF.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run NMF (non-negative matrix factorization)

## Signature

```text
RunNMF(object, ...) RunNMF{Seurat}( object, assay = NULL, layer = "data", features = NULL, nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.name = "nmf", reduction.key = "BE_", verbose = TRUE, seed.use = 11, cores = 0, ... ) RunNMF{Assay}( object, assay = NULL, layer = "data", features = NULL, nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "BE_", verbose = TRUE, seed.use = 11, cores = 0, ... ) RunNMF{Assay5}( object, assay = NULL, layer = "data", features = NULL, nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "BE_", verbose = TRUE, seed.use = 11, cores = 0, ... ) RunNMF{default}( object, assay = NULL, layer = "data", nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "BE_", verbose = TRUE, cores = 0, seed.use = 11, ... )
```

## Parameters

- `object`: An object. This can be a Seurat object, an Assay object, or a matrix-like object.
- `...`: Additional arguments passed to [RcppML:nmf]{RcppML::nmf} or [NMF:nmf]{NMF::nmf}.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Which layer to use. Default is data.
- `features`: A character vector of features to use. Default is NULL.
- `nbes`: The number of basis vectors (components) to be computed. Default is 50.
- `nmf.method`: The NMF algorithm to be used. Currently supported values are "RcppML" and "NMF". Default is "RcppML".
- `tol`: The tolerance for convergence (only applicable when nmf.method is "RcppML"). Default is 1e-5.
- `maxit`: The maximum number of iterations for convergence (only applicable when nmf.method is "RcppML"). Default is 100.
- `rev.nmf`: Whether to perform reverse NMF (i.e., transpose the input matrix) before running the analysis. Default is FALSE.
- `ndims.print`: The dimensions (number of basis vectors) to print in the output. Default is 1:5.
- `nfeatures.print`: The number of features to print in the output. Default is 30.
- `reduction.name`: The name of the reduction to be stored in the Seurat object. Default is "nmf".
- `reduction.key`: The prefix for the column names of the basis vectors. Default is "BE_".
- `verbose`: Whether to print the message. Default is TRUE.
- `seed.use`: Random seed for reproducibility. Default is 11.
- `cores`: The number of threads to be used in older RcppML releases that expose a global OpenMP thread setter. Newer releases manage their thread count internally. Default is 0.

## Full Documentation

# Run NMF (non-negative matrix factorization)

## Usage

```text
RunNMF(object, ...) RunNMF{Seurat}( object, assay = NULL, layer = "data", features = NULL, nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.name = "nmf", reduction.key = "BE_", verbose = TRUE, seed.use = 11, cores = 0, ... ) RunNMF{Assay}( object, assay = NULL, layer = "data", features = NULL, nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "BE_", verbose = TRUE, seed.use = 11, cores = 0, ... ) RunNMF{Assay5}( object, assay = NULL, layer = "data", features = NULL, nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "BE_", verbose = TRUE, seed.use = 11, cores = 0, ... ) RunNMF{default}( object, assay = NULL, layer = "data", nbes = 50, nmf.method = "RcppML", tol = 1e-05, maxit = 100, rev.nmf = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "BE_", verbose = TRUE, cores = 0, seed.use = 11, ... )
```

## Description

Run NMF (non-negative matrix factorization)

## Examples

```r
library(Matrix)
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunNMF(pancreas_sub)
CellDimPlot(
  pancreas_sub,
  group.by = "CellType",
  reduction = "nmf"
)

FeatureDimPlot(
  pancreas_sub,
  features = c("BE_1", "BE_2", "BE_3"),
  reduction = "UMAP",
  palette = "RdBu",
  xlab = "UMAP_1",
  ylab = "UMAP_2",
  theme_use = "theme_blank"
)

ht_cells <- NMFHeatmap(
  pancreas_sub,
  plot_type = "cells",
  cell_annotation = "CellType"
)
ht_cells$plot

ht_features <- NMFHeatmap(
  pancreas_sub,
  plot_type = "features"
)
ht_features$plot
```
