# Find features with expression patterns similar to provided features

- Package: scop
- Language: R
- Function: `GetSimilarFeatures`
- Source: https://mengxu98.github.io/scop/reference/GetSimilarFeatures.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetSimilarFeatures.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Find features with expression patterns similar to provided features

## Signature

```text
GetSimilarFeatures( srt, features, n, features_use = rownames(srt), anticorr = FALSE, aggregator = "sum", assay = "RNA", layer = "data", verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `features`: A character vector of feature names.
- `n`: An integer; number of results to return.
- `features_use`: A character vector of features eligible to be returned.
- `anticorr`: Whether to allow negatively correlated features. Default is FALSE.
- `aggregator`: How to combine correlations when finding similar features. Options: "sum" (default), "min" (for "and"-like filter), "max", or "mean".
- `assay`: Which assay to use. Default is "RNA".
- `layer`: Which layer to use. Default is data.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Find features with expression patterns similar to provided features

## Usage

```text
GetSimilarFeatures( srt, features, n, features_use = rownames(srt), anticorr = FALSE, aggregator = "sum", assay = "RNA", layer = "data", verbose = TRUE )
```

## Description

Find features with expression patterns similar to provided features

## Value

character vector.
