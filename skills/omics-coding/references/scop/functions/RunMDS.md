# Run MDS (multi-dimensional scaling)

- Package: scop
- Language: R
- Function: `RunMDS`
- Source: https://mengxu98.github.io/scop/reference/RunMDS.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunMDS.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run MDS (multi-dimensional scaling)

## Signature

```text
RunMDS(object, ...) RunMDS{Seurat}( object, assay = NULL, layer = "data", features = NULL, nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.name = "mds", reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... ) RunMDS{Assay}( object, assay = NULL, layer = "data", features = NULL, nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... ) RunMDS{Assay5}( object, assay = NULL, layer = "data", features = NULL, nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... ) RunMDS{default}( object, assay = NULL, layer = "data", nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... )
```

## Parameters

- `object`: An object. This can be a Seurat object, an assay object, or a matrix-like object.
- `...`: Additional arguments to be passed to [stats:cmdscale]{stats::cmdscale}, [MASS:isoMDS]{MASS::isoMDS} or [MASS:sammon]{MASS::sammon}.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Which layer to use. Default is data.
- `features`: A character vector of features to use. Default is NULL.
- `nmds`: The number of dimensions to be computed. Default is 50.
- `dist.method`: The distance metric to be used. Currently supported values are "euclidean", "chisquared", "kullback", "jeffreys", "jensen", "manhattan", "maximum", "canberra", "minkowski", and "hamming". Default is "euclidean".
- `mds.method`: The MDS algorithm to be used. Currently supported values are "cmdscale", "isoMDS", and "sammon". Default is "cmdscale".
- `rev.mds`: Whether to perform reverse MDS (i.e., transpose the input matrix) before running the analysis. Default is FALSE.
- `reduction.name`: The name of the reduction to be stored in the Seurat object. Default is "mds".
- `reduction.key`: The prefix for the column names of the basis vectors. Default is "MDS_".
- `verbose`: Whether to print the message. Default is TRUE.
- `seed.use`: Random seed for reproducibility. Default is 11.

## Full Documentation

# Run MDS (multi-dimensional scaling)

## Usage

```text
RunMDS(object, ...) RunMDS{Seurat}( object, assay = NULL, layer = "data", features = NULL, nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.name = "mds", reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... ) RunMDS{Assay}( object, assay = NULL, layer = "data", features = NULL, nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... ) RunMDS{Assay5}( object, assay = NULL, layer = "data", features = NULL, nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... ) RunMDS{default}( object, assay = NULL, layer = "data", nmds = 50, dist.method = "euclidean", mds.method = "cmdscale", rev.mds = FALSE, reduction.key = "MDS_", verbose = TRUE, seed.use = 11, ... )
```

## Description

Run MDS (multi-dimensional scaling)

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunMDS(pancreas_sub)
CellDimPlot(
  pancreas_sub,
  group.by = "CellType",
  reduction = "mds"
)
```
