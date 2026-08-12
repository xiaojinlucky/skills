# db_scds

- Package: scop
- Language: R
- Function: `db_scds`
- Source: local://scop/0.8.9/db_scds
- Source mode: installed SCOP runtime documentation
- Fetched at: 2026-07-22T11:04:16+00:00

## Summary

Run doublet-calling with scds

## Signature

```text
db_scds( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, method = c("hybrid", "cxds", "bcds"), data_type = NULL, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA" .
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01 .
- `method`: The method to be used for doublet-calling. Options are "hybrid" , "cxds" , or "bcds" .
- `data_type`: Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `...`: Additional arguments passed to the selected scds method.
- `verbose`: Whether to print the message. Default is TRUE .

## Full Documentation

db_scds R Documentation
## Run doublet-calling with scds

### Description

Run doublet-calling with scds

### Usage

```text
db_scds(
srt,
assay = "RNA",
db_rate = ncol(srt)/1000 * 0.01,
method = c("hybrid", "cxds", "bcds"),
data_type = NULL,
...,
verbose = TRUE
)

```

### Arguments
`srt `
A Seurat object.
`assay `
The name of the assay to be used for doublet-calling. Default is `"RNA" `.
`db_rate `
The expected doublet rate. Default is calculated as `ncol(srt) / 1000 * 0.01 `.
`method `
The method to be used for doublet-calling. Options are `"hybrid" `, `"cxds" `, or `"bcds" `.
`data_type `
Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
`... `
Additional arguments passed to the selected `scds `method.
`verbose `
Whether to print the message. Default is `TRUE `.

### Examples

```text
data(pancreas_sub)
pancreas_sub <- standard_scop(pancreas_sub)
pancreas_sub <- db_scds(pancreas_sub, method = "hybrid")
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
