# RunSlingshot

- Package: scop
- Language: R
- Function: `RunSlingshot`
- Source: https://mengxu98.github.io/scop/reference/RunSlingshot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSlingshot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

RunSlingshot

## Signature

```text
RunSlingshot( srt, group.by, reduction = NULL, dims = NULL, start = NULL, end = NULL, prefix = NULL, reverse = FALSE, align_start = FALSE, show_plot = TRUE, lineage_palette = "Dark2", seed = 11, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `reduction`: Which dimensionality reduction to use. If not specified, will use the reduction returned by DefaultReduction.
- `dims`: The dimensions to use for the Slingshot algorithm. Default is NULL, which uses first two dimensions.
- `start`: The starting group for the Slingshot algorithm. Default is NULL.
- `end`: The ending group for the Slingshot algorithm. Default is NULL.
- `prefix`: The prefix to add to the column names of the resulting pseudotime variable. Default is NULL.
- `reverse`: Logical value indicating whether to reverse the pseudotime variable. Default is FALSE.
- `align_start`: Logical value indicating whether to align the starting pseudotime values at the maximum pseudotime. Default is FALSE.
- `show_plot`: Logical value indicating whether to show the dimensionality plot. Default is TRUE.
- `lineage_palette`: The color palette to use for the lineages in the plot. Default is "Dark2".
- `seed`: Random seed for reproducibility. Default is 11.
- `...`: Additional arguments to be passed to the [slingshot:slingshot]{slingshot::slingshot} function.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# RunSlingshot

## Usage

```text
RunSlingshot( srt, group.by, reduction = NULL, dims = NULL, start = NULL, end = NULL, prefix = NULL, reverse = FALSE, align_start = FALSE, show_plot = TRUE, lineage_palette = "Dark2", seed = 11, ..., verbose = TRUE )
```

## Description

RunSlingshot

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunSlingshot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "UMAP"
)
pancreas_sub <- RunSlingshot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "PCA"
)
CellDimPlot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "UMAP",
  lineages = paste0("Lineage", 1:2),
  lineages_span = 0.1
)

# 3D lineage
pancreas_sub <- RunSlingshot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "StandardpcaUMAP3D"
)
CellDimPlot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "UMAP",
  lineages = paste0("Lineage", 1:2),
  lineages_span = 0.1,
  lineages_trim = c(0.05, 0.95)
)
```
