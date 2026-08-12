# Find the default reduction name in a Seurat object

- Package: scop
- Language: R
- Function: `DefaultReduction`
- Source: https://mengxu98.github.io/scop/reference/DefaultReduction.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/DefaultReduction.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Find the default reduction name in a Seurat object

## Signature

```text
DefaultReduction( srt, pattern = NULL, min_dim = 2, max_distance = 0.1, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `pattern`: Character string containing a regular expression to search for.
- `min_dim`: Minimum dimension threshold.
- `max_distance`: Maximum distance allowed for a match.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Find the default reduction name in a Seurat object

## Usage

```text
DefaultReduction( srt, pattern = NULL, min_dim = 2, max_distance = 0.1, verbose = TRUE )
```

## Description

Find the default reduction name in a Seurat object

## Value

Default reduction name.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
names(pancreas_sub@reductions)

DefaultReduction(pancreas_sub)

DefaultReduction(pancreas_sub, pattern = "pca")

DefaultReduction(pancreas_sub, pattern = "umap")
```
