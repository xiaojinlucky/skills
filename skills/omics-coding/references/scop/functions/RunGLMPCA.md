# Run generalized principal components analysis (GLMPCA)

- Package: scop
- Language: R
- Function: `RunGLMPCA`
- Source: https://mengxu98.github.io/scop/reference/RunGLMPCA.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunGLMPCA.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run generalized principal components analysis (GLMPCA)

## Signature

```text
RunGLMPCA(object, ...) RunGLMPCA{Seurat}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.name = "glmpca", reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... ) RunGLMPCA{Assay}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... ) RunGLMPCA{Assay5}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... ) RunGLMPCA{default}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... )
```

## Parameters

- `object`: An object. Can be a Seurat object, an assay object, or a matrix-like object.
- `...`: Additional arguments to be passed to the [glmpca:glmpca]{glmpca::glmpca} function.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Which layer to use. Default is data.
- `features`: A character vector of features to use. Default is NULL.
- `L`: The number of components to be computed. Default is 5.
- `fam`: The family of the generalized linear model to be used. Currently supported values are "poi", "nb", "nb2", "binom", "mult", and "bern". Default is "poi".
- `rev.gmlpca`: Whether to perform reverse GLMPCA (i.e., transpose the input matrix) before running the analysis. Default is FALSE.
- `ndims.print`: The dimensions (number of components) to print in the output. Default is 1:5.
- `nfeatures.print`: The number of features to print in the output. Default is 30.
- `reduction.name`: The name of the reduction to be stored in the Seurat object. Default is "glmpca".
- `reduction.key`: The prefix for the column names of the basis vectors. Default is "GLMPC_".
- `verbose`: Whether to print the message. Default is TRUE.
- `seed.use`: Random seed for reproducibility. Default is 11.

## Full Documentation

# Run generalized principal components analysis (GLMPCA)

## Usage

```text
RunGLMPCA(object, ...) RunGLMPCA{Seurat}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.name = "glmpca", reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... ) RunGLMPCA{Assay}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... ) RunGLMPCA{Assay5}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... ) RunGLMPCA{default}( object, assay = NULL, layer = "counts", features = NULL, L = 5, fam = c("poi", "nb", "nb2", "binom", "mult", "bern"), rev.gmlpca = FALSE, ndims.print = 1:5, nfeatures.print = 30, reduction.key = "GLMPC_", verbose = TRUE, seed.use = 11, ... )
```

## Description

Run generalized principal components analysis (GLMPCA)

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunGLMPCA(pancreas_sub)
CellDimPlot(
  pancreas_sub,
  group.by = "CellType",
  reduction = "glmpca"
)
```
