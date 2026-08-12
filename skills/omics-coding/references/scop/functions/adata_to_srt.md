# Convert an anndata object to a seurat object

- Package: scop
- Language: R
- Function: `adata_to_srt`
- Source: https://mengxu98.github.io/scop/reference/adata_to_srt.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/adata_to_srt.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert an anndata object to a seurat object

## Signature

```text
adata_to_srt(adata, verbose = TRUE)
```

## Parameters

- `adata`: An AnnData object. Can be a Python AnnData object (from scanpy/reticulate``), an AnnDataR6object from theanndatapackage, or anInMemoryAnnDataobject from theanndataR` package.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Convert an anndata object to a seurat object

## Usage

```text
adata_to_srt(adata, verbose = TRUE)
```

## Description

Convert an anndata object to a seurat object

## Examples

```r
\dontrun{
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
adata <- srt_to_adata(pancreas_sub)
adata <- RunPAGA(
  adata = adata,
  group.by = "SubCellType",
  linear_reduction = "X_pca",
  nonlinear_reduction = "X_umap"
)
srt <- adata_to_srt(adata)
srt

# Or convert a h5ad file to Seurat object
sc <- reticulate::import("scanpy")
adata <- sc$read_h5ad("pancreas.h5ad")
srt <- adata_to_srt(adata)
srt
}
```
