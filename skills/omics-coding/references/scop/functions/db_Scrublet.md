# db_Scrublet

- Package: scop
- Language: R
- Function: `db_Scrublet`
- Source: local://scop/0.8.9/db_Scrublet
- Source mode: installed SCOP runtime documentation
- Fetched at: 2026-07-22T11:04:16+00:00

## Summary

Run doublet-calling with Scrublet

## Signature

```text
db_Scrublet( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, data_type = NULL, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA" .
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01 .
- `data_type`: Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `...`: Additional arguments to be passed to scrublet.Scrublet .
- `verbose`: Whether to print the message. Default is TRUE .

## Full Documentation

db_Scrublet R Documentation
## Run doublet-calling with Scrublet

### Description

Run doublet-calling with Scrublet

### Usage

```text
db_Scrublet(
srt,
assay = "RNA",
db_rate = ncol(srt)/1000 * 0.01,
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
`data_type `
Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
`... `
Additional arguments to be passed to scrublet.Scrublet .
`verbose `
Whether to print the message. Default is `TRUE `.

### Examples

```text
## Not run:
data(pancreas_sub)
pancreas_sub <- standard_scop(pancreas_sub)
pancreas_sub <- db_Scrublet(pancreas_sub)
CellDimPlot(
pancreas_sub,
reduction = "umap",
group.by = "db.Scrublet_class"
)

FeatureDimPlot(
pancreas_sub,
reduction = "umap",
features = "db.Scrublet_score"
)

## End(Not run)

```
