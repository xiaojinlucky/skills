# Run doublet-calling with scDblFinder

- Package: scop
- Language: R
- Function: `RunscDblFinder`
- Source: https://mengxu98.github.io/scop/reference/RunscDblFinder.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunscDblFinder.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run doublet-calling with scDblFinder

## Signature

```text
RunscDblFinder( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, data_type = NULL, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA".
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01.
- `data_type`: Optional precomputed result from CheckDataType for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `...`: Additional arguments to be passed to {[scDblFinder:scDblFinder]{scDblFinder::scDblFinder()}}.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run doublet-calling with scDblFinder

## Usage

```text
RunscDblFinder( srt, assay = "RNA", db_rate = ncol(srt)/1000 * 0.01, data_type = NULL, ..., verbose = TRUE )
```

## Description

Run doublet-calling with scDblFinder
