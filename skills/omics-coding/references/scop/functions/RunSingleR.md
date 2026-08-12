# Annotate single cells using SingleR

- Package: scop
- Language: R
- Function: `RunSingleR`
- Source: https://mengxu98.github.io/scop/reference/RunSingleR.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSingleR.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Annotate single cells using SingleR

## Signature

```text
RunSingleR( srt_query, srt_ref, query_group = NULL, ref_group = NULL, query_assay = "RNA", ref_assay = "RNA", genes = "de", de.method = "wilcox", sd.thresh = 1, de.n = NULL, aggr.ref = FALSE, aggr.args = list(), quantile = 0.8, fine.tune = TRUE, tune.thresh = 0.05, prune = TRUE, cores = 1, verbose = TRUE )
```

## Parameters

- `srt_query`: An object of class Seurat to be annotated with cell types.
- `srt_ref`: An object of class Seurat storing the reference cells.
- `query_group`: A character vector specifying the column name in the srt_query metadata that represents the cell grouping.
- `ref_group`: A character vector specifying the column name in the srt_ref metadata that represents the cell grouping.
- `query_assay`: A character vector specifying the assay to be used for the query data. Default is the default assay of the srt_query object.
- `ref_assay`: A character vector specifying the assay to be used for the reference data. Default is the default assay of the srt_ref object.
- `genes`: A string containing "de", indicating that markers should be calculated from ref. For back compatibility, other string values are allowed but will be ignored with a deprecation warning. Alternatively, if ref is not a list, genes can be either: A list of lists of character vectors containing DE genes between pairs of labels. A list of character vectors containing marker genes for each label. If ref is a list, genes can be a list of length equal to ref. Each element of the list should be one of the two above choices described for non-list ref, containing markers for labels in the corresponding entry of ref.
- `de.method`: String specifying how DE genes should be detected between pairs of labels. Defaults to "classic", which sorts genes by the log-fold changes and takes the top de.n. Other options are "wilcox" and "t", see Details. Ignored if genes is a list of markers/DE genes.
- `sd.thresh`: Deprecated and ignored.
- `de.n`: An integer scalar specifying the number of DE genes to use when genes="de". If de.method="classic", defaults to 500 * (2/3) ^ log2(N) where N is the number of unique labels. Otherwise, defaults to 10. Ignored if genes is a list of markers/DE genes.
- `aggr.ref, aggr.args`: Arguments controlling the aggregation of the references prior to annotation, see {[SingleR]{trainSingleR}}.
- `quantile`: "quantile" parameter in [SingleR:SingleR]{SingleR::SingleR} function.
- `fine.tune`: "fine.tune" parameter in [SingleR:SingleR]{SingleR::SingleR} function.
- `tune.thresh`: "tune.thresh" parameter in [SingleR:SingleR]{SingleR::SingleR} function.
- `prune`: "prune" parameter in [SingleR:SingleR]{SingleR::SingleR} function.
- `cores`: The number of worker processes to use for parallelization. Default is 1.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Annotate single cells using SingleR

## Usage

```text
RunSingleR( srt_query, srt_ref, query_group = NULL, ref_group = NULL, query_assay = "RNA", ref_assay = "RNA", genes = "de", de.method = "wilcox", sd.thresh = 1, de.n = NULL, aggr.ref = FALSE, aggr.args = list(), quantile = 0.8, fine.tune = TRUE, tune.thresh = 0.05, prune = TRUE, cores = 1, verbose = TRUE )
```

## Description

Annotate single cells using SingleR

## Value

An annotate Seurat object. The annotation results are stored in the singler_annotation column of the meta data, and the corresponding scores are stored in the singler_score column.

## Examples

```r
data(panc8_sub)
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
panc8_sub <- RunStandardWorkflow(panc8_sub)

data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunSingleR(
  srt_query = pancreas_sub,
  srt_ref = panc8_sub,
  query_group = "Standardpca_SNN_res.0.6",
  ref_group = "celltype"
)
CellDimPlot(
  pancreas_sub,
  group.by = c("singler_annotation", "SubCellType")
)

pancreas_sub <- RunSingleR(
  srt_query = pancreas_sub,
  srt_ref = panc8_sub,
  query_group = NULL,
  ref_group = "celltype"
)
CellDimPlot(
  pancreas_sub,
  group.by = c("singler_annotation", "SubCellType"),
  label = TRUE
)

FeatureStatPlot(
  pancreas_sub,
  stat.by = "singler_score",
  group.by = "singler_annotation"
)

ht1 <- CellCorHeatmap(
  srt_query = pancreas_sub,
  srt_ref = pancreas_sub,
  query_group = "SubCellType",
  cluster_rows = TRUE,
  ref_group = "singler_annotation",
  cluster_columns = TRUE,
  width = 2,
  height = 2
)
ht1$plot
```
