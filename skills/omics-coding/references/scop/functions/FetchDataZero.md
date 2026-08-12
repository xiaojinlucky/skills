# FetchData but with zeroes for unavailable genes

- Package: scop
- Language: R
- Function: `FetchDataZero`
- Source: https://mengxu98.github.io/scop/reference/FetchDataZero.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/FetchDataZero.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

FetchData but with zeroes for unavailable genes

## Signature

```text
FetchDataZero( srt, features, assay = "RNA", layer = "data", verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `features`: A character vector of feature names.
- `assay`: Which assay to use. Default is "RNA".
- `layer`: Which layer to use. Default is data.
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Other arguments to pass to [Seurat:FetchData]{Seurat::FetchData}.

## Full Documentation

# FetchData but with zeroes for unavailable genes

## Usage

```text
FetchDataZero( srt, features, assay = "RNA", layer = "data", verbose = TRUE, ... )
```

## Description

FetchData but with zeroes for unavailable genes
