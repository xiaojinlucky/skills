# Run doublet-calling for single cell RNA-seq data.

- Package: scop
- Language: R
- Function: `RunDoubletCalling`
- Source: https://mengxu98.github.io/scop/reference/RunDoubletCalling.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunDoubletCalling.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run doublet-calling for single cell RNA-seq data.

## Signature

```text
RunDoubletCalling( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, db_method = "scDblFinder", data_type = NULL, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA".
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01.
- `db_method`: Method used for doublet-calling. Can be one of "scDblFinder", "Scrublet", "DoubletDetection", "scds_cxds", "scds_bcds", "scds_hybrid".
- `data_type`: Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `...`: Additional arguments to be passed to the corresponding doublet-calling method.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run doublet-calling for single cell RNA-seq data.

## Usage

```text
RunDoubletCalling( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, db_method = "scDblFinder", data_type = NULL, ..., verbose = TRUE )
```

## Description

Run doublet-calling for single cell RNA-seq data.

## Value

Returns a Seurat object with the doublet prediction results and prediction scores stored in the meta.data.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunDoubletCalling(
  pancreas_sub,
  db_method = "scDblFinder"
)
table(pancreas_sub$db.scDblFinder_class)
head(pancreas_sub@meta.data[, c(
  "db.scDblFinder_class", "db.scDblFinder_score"
)])
```
