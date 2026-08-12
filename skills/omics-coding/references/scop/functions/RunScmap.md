# Annotate single cells using scmap.

- Package: scop
- Language: R
- Function: `RunScmap`
- Source: https://mengxu98.github.io/scop/reference/RunScmap.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunScmap.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotate single cells using scmap.

## Signature

```text
RunScmap( srt_query, srt_ref, ref_group = NULL, query_assay = "RNA", ref_assay = "RNA", method = "scmapCluster", nfeatures = 500, threshold = 0.5, k = 10, verbose = TRUE )
```

## Parameters

- `srt_query`: An object of class Seurat to be annotated with cell types.
- `srt_ref`: An object of class Seurat storing the reference cells.
- `ref_group`: A character vector specifying the column name in the srt_ref metadata that represents the cell grouping.
- `query_assay`: A character vector specifying the assay to be used for the query data. Default is the default assay of the srt_query object.
- `ref_assay`: A character vector specifying the assay to be used for the reference data. Default is the default assay of the srt_ref object.
- `method`: The method to be used for scmap analysis. Can be any of "scmapCluster" or "scmapCell". Default is "scmapCluster".
- `nfeatures`: The number of top features to be selected. Default is 500.
- `threshold`: The threshold value on similarity to determine if a cell is assigned to a cluster. This should be a value between 0 and 1. Default is 0.5.
- `k`: Number of clusters per group for k-means clustering when method is "scmapCell". Default is 10.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Annotate single cells using scmap.

## Usage

```text
RunScmap( srt_query, srt_ref, ref_group = NULL, query_assay = "RNA", ref_assay = "RNA", method = "scmapCluster", nfeatures = 500, threshold = 0.5, k = 10, verbose = TRUE )
```

## Description

Annotate single cells using scmap.

## Examples

```r
data(panc8_sub)
panc8_sub <- RunStandardWorkflow(panc8_sub)

genenames <- make.unique(
  thisutils::capitalize(
    rownames(panc8_sub),
    force_tolower = TRUE
  )
)
names(genenames) <- rownames(panc8_sub)
panc8_sub <- RenameFeatures(
  panc8_sub,
  newnames = genenames
)
panc8_sub <- CheckDataMerge(
  panc8_sub,
  batch = "tech"
)[["srt_merge"]]

data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunScmap(
  srt_query = pancreas_sub,
  srt_ref = panc8_sub,
  ref_group = "celltype",
  method = "scmapCluster"
)
CellDimPlot(
  pancreas_sub,
  group.by = "scmap_annotation"
)

pancreas_sub <- RunScmap(
  srt_query = pancreas_sub,
  srt_ref = panc8_sub,
  ref_group = "celltype",
  method = "scmapCell"
)
CellDimPlot(
  pancreas_sub,
  group.by = "scmap_annotation"
)
```
