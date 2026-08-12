# Run Force-Directed Layout (Fruchterman-Reingold algorithm)

- Package: scop
- Language: R
- Function: `RunFR`
- Source: https://mengxu98.github.io/scop/reference/RunFR.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunFR.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Force-Directed Layout (Fruchterman-Reingold algorithm)

## Signature

```text
RunFR(object, ...) RunFR{Seurat}( object, reduction = NULL, dims = NULL, features = NULL, assay = NULL, layer = "data", graph = NULL, neighbor = NULL, k.param = 20, ndim = 2, niter = 500, reduction.name = "FR", reduction.key = "FR_", verbose = TRUE, seed.use = 11L, ... ) RunFR{default}( object, assay = NULL, ndim = 2, niter = 500, reduction.key = "FR_", verbose = TRUE, seed.use = 11L, ... )
```

## Parameters

- `object`: An object. This can be a Seurat object, a Neighbor object, or a Graph object. Default is NULL.
- `...`: Additional arguments to be passed to [igraph:layout_with_fr]{igraph::layout_with_fr}.
- `reduction`: Which dimensionality reduction to use. Default is "pca".
- `dims`: The dimensions to be used. Default is NULL.
- `features`: A character vector of features to use. Default is NULL.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Which layer to use. Default is data.
- `graph`: The name of the Graph object to be used. Default is NULL.
- `neighbor`: The name of the Neighbor object to be used. Default is NULL.
- `k.param`: The number of nearest neighbors to consider. Default is 20.
- `ndim`: The number of dimensions for the force-directed layout. Default is 2.
- `niter`: The number of iterations for the force-directed layout. Default is 500.
- `reduction.name`: The name of the reduction to be stored in the Seurat object. Default is "fr".
- `reduction.key`: The prefix for the column names of the force-directed layout embeddings. Default is "FR_".
- `verbose`: Whether to print the message. Default is TRUE.
- `seed.use`: Random seed for reproducibility. Default is 11.

## Full Documentation

# Run Force-Directed Layout (Fruchterman-Reingold algorithm)

## Usage

```text
RunFR(object, ...) RunFR{Seurat}( object, reduction = NULL, dims = NULL, features = NULL, assay = NULL, layer = "data", graph = NULL, neighbor = NULL, k.param = 20, ndim = 2, niter = 500, reduction.name = "FR", reduction.key = "FR_", verbose = TRUE, seed.use = 11L, ... ) RunFR{default}( object, assay = NULL, ndim = 2, niter = 500, reduction.key = "FR_", verbose = TRUE, seed.use = 11L, ... )
```

## Description

Run Force-Directed Layout (Fruchterman-Reingold algorithm)

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunFR(
  object = pancreas_sub,
  graph = "Standardpca_SNN",
  niter = 100
)
CellDimPlot(
  pancreas_sub,
  group.by = "CellType",
  reduction = "fr"
)
```
