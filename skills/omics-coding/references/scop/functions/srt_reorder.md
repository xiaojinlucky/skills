# Reorder idents by the gene expression

- Package: scop
- Language: R
- Function: `srt_reorder`
- Source: https://mengxu98.github.io/scop/reference/srt_reorder.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_reorder.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Reorder idents by the gene expression

## Signature

```text
srt_reorder( srt, features = NULL, reorder_by = NULL, layer = "data", assay = NULL, log = TRUE, distance_metric = "euclidean", verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `features`: A character vector or a named list of features to plot. Features can be gene names in Assay or names of numeric columns in meta.data.
- `reorder_by`: Reorder groups instead of idents.
- `layer`: Which layer to use. Default is data.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `log`: Whether log1p transformation needs to be applied. Default is TRUE.
- `distance_metric`: Metric to compute distance. Default is "euclidean".
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Reorder idents by the gene expression

## Usage

```text
srt_reorder( srt, features = NULL, reorder_by = NULL, layer = "data", assay = NULL, log = TRUE, distance_metric = "euclidean", verbose = TRUE )
```

## Description

Reorder idents by the gene expression

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- srt_reorder(
  pancreas_sub,
  reorder_by = "SubCellType",
  layer = "data"
)
```
