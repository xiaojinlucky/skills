# Rename features for the Seurat object

- Package: scop
- Language: R
- Function: `RenameFeatures`
- Source: https://mengxu98.github.io/scop/reference/RenameFeatures.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RenameFeatures.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Rename features for the Seurat object

## Signature

```text
RenameFeatures(srt, newnames = NULL, assays = NULL, verbose = TRUE)
```

## Parameters

- `srt`: A Seurat object.
- `newnames`: A vector with the same length of features in Seurat object, or characters named with old features.
- `assays`: Assays to rename.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Rename features for the Seurat object

## Usage

```text
RenameFeatures(srt, newnames = NULL, assays = NULL, verbose = TRUE)
```

## Description

Rename features for the Seurat object

## Examples

```r
data(panc8_sub)
head(rownames(panc8_sub))
# Simply convert genes from human to mouse and preprocess the data
genenames <- make.unique(
  thisutils::capitalize(rownames(panc8_sub),
    force_tolower = TRUE
  )
)
names(genenames) <- rownames(panc8_sub)
panc8_rename <- RenameFeatures(
  panc8_sub,
  newnames = genenames
)
head(rownames(panc8_rename))
```
