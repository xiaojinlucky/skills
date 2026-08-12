# Run doublet-calling with scds

- Package: scop
- Language: R
- Function: `Runscds`
- Source: https://mengxu98.github.io/scop/reference/Runscds.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/Runscds.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run doublet-calling with scds

## Signature

```text
Runscds( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, method = c("hybrid", "cxds", "bcds"), data_type = NULL, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA".
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01.
- `method`: The method to be used for doublet-calling. Options are "hybrid", "cxds", or "bcds".
- `data_type`: Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `...`: Additional arguments passed to the selected scds method.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run doublet-calling with scds

## Usage

```text
Runscds( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, method = c("hybrid", "cxds", "bcds"), data_type = NULL, ..., verbose = TRUE )
```

## Description

Run doublet-calling with scds

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- Runscds(pancreas_sub, method = "hybrid")
CellDimPlot(
  pancreas_sub,
  reduction = "umap",
  group.by = "db.scds_hybrid_class"
)

FeatureDimPlot(
  pancreas_sub,
  reduction = "umap",
  features = "db.scds_hybrid_score"
)
```
