# db_scDblFinder

- Package: scop
- Language: R
- Function: `db_scDblFinder`
- Source: local://scop/0.8.9/db_scDblFinder
- Source mode: installed SCOP runtime documentation
- Fetched at: 2026-07-22T11:04:16+00:00

## Summary

Run doublet-calling with scDblFinder

## Signature

```text
db_scDblFinder( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, data_type = NULL, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA" .
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01 .
- `data_type`: Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `...`: Additional arguments to be passed to scDblFinder::scDblFinder() .
- `verbose`: Whether to print the message. Default is TRUE .

## Full Documentation

db_scDblFinder R Documentation
## Run doublet-calling with scDblFinder

### Description

Run doublet-calling with scDblFinder

### Usage

```text
db_scDblFinder(
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
Additional arguments to be passed to `scDblFinder::scDblFinder() `.
`verbose `
Whether to print the message. Default is `TRUE `.
