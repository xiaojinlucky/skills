# Attempt to recover raw counts from the normalized matrix

- Package: scop
- Language: R
- Function: `RecoverCounts`
- Source: https://mengxu98.github.io/scop/reference/RecoverCounts.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RecoverCounts.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Attempt to recover raw counts from the normalized matrix

## Signature

```text
RecoverCounts( srt, assay = NULL, trans = c("expm1", "exp", "none"), min_count = c(1, 2, 3), tolerance = 0.1, sf = NULL, verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `trans`: The transformation function to applied when data is presumed to be log-normalized.
- `min_count`: Minimum UMI count of genes.
- `tolerance`: When recovering the raw counts, the nCount of each cell is theoretically calculated as an integer. However, due to decimal point preservation during normalization, the calculated nCount is usually a floating point number close to the integer. The tolerance is its difference from the integer. Default is 0.1
- `sf`: Set the scaling factor manually.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Attempt to recover raw counts from the normalized matrix

## Usage

```text
RecoverCounts( srt, assay = NULL, trans = c("expm1", "exp", "none"), min_count = c(1, 2, 3), tolerance = 0.1, sf = NULL, verbose = TRUE )
```

## Description

Attempt to recover raw counts from the normalized matrix

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
raw_counts <- GetAssayData5(
  pancreas_sub,
  assay = "RNA",
  layer = "counts"
)

# Normalized the data
pancreas_sub <- Seurat::NormalizeData(pancreas_sub)

# Now replace counts with the log-normalized data matrix
data <- GetAssayData5(
  pancreas_sub,
  assay = "RNA",
  layer = "data"
)
new_pancreas_sub <- SeuratObject::SetAssayData(
  object = pancreas_sub,
  layer = "counts",
  new.data = data,
  assay = "RNA"
)
# Recover the counts and compare with the raw counts matrix
pancreas_sub <- RecoverCounts(new_pancreas_sub)
new_counts <- GetAssayData5(
  pancreas_sub,
  assay = "RNA",
  layer = "counts"
)
identical(raw_counts, new_counts)
```
