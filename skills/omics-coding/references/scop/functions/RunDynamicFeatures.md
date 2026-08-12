# Calculates dynamic features for lineages

- Package: scop
- Language: R
- Function: `RunDynamicFeatures`
- Source: https://mengxu98.github.io/scop/reference/RunDynamicFeatures.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunDynamicFeatures.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Calculates dynamic features for lineages

## Signature

```text
RunDynamicFeatures( srt, lineages, features = NULL, suffix = lineages, n_candidates = 1000, minfreq = 5, family = NULL, layer = "counts", assay = NULL, libsize = NULL, fit_method = c("gam", "pretsa"), knot = 0, max_knot_allowed = 10, pretsa_backend = c("cpp", "r"), padjust_method = "fdr", cores = 1, verbose = TRUE, seed = 11 )
```

## Parameters

- `srt`: A Seurat object.
- `lineages`: A character vector specifying the lineage names for which dynamic features should be calculated.
- `features`: A character vector of features to use. If NULL, n_candidates must be provided.
- `suffix`: A character vector specifying the suffix to append to the output layer names for each lineage. Default is the lineage names.
- `n_candidates`: A number of candidate features to select when features is NULL. Default is 1000.
- `minfreq`: An integer specifying the minimum frequency threshold for candidate features. Features with a frequency less than minfreq will be excluded. Default is 5.
- `family`: A character or character vector specifying the family of distributions to use for the GAM. If family is set to NULL, the appropriate family will be automatically determined based on the data. If length(family) is 1, the same family will be used for all features. Otherwise, family must have the same length as features.
- `layer`: Which layer to use. Default is "counts".
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `libsize`: A numeric or numeric vector specifying the library size correction factors for each cell. If NULL, the library size correction factors will be calculated based on the expression matrix. If length(libsize) is 1, the same value will be used for all cells. Otherwise, libsize must have the same length as the number of cells in srt. Default is NULL.
- `fit_method`: The method used for fitting features. Either "gam" (generalized additive models) or "pretsa" (Pattern recognition in Temporal and Spatial Analyses). Default is "gam".
- `knot`: For fit_method = "pretsa": B-spline knots. 0 or "auto". Default is 0.
- `max_knot_allowed`: For fit_method = "pretsa" when knot = "auto": max knots. Default is 10.
- `pretsa_backend`: PreTSA fitting backend. "cpp" batches model selection and fitting; "r" retains the reference implementation.
- `padjust_method`: The method used for p-value adjustment. Default is "fdr".
- `cores`: The number of worker processes to use for parallelization. Default is 1.
- `verbose`: Whether to print the message. Default is TRUE.
- `seed`: Random seed for reproducibility. Default is 11.

## Full Documentation

# Calculates dynamic features for lineages

## Usage

```text
RunDynamicFeatures( srt, lineages, features = NULL, suffix = lineages, n_candidates = 1000, minfreq = 5, family = NULL, layer = "counts", assay = NULL, libsize = NULL, fit_method = c("gam", "pretsa"), knot = 0, max_knot_allowed = 10, pretsa_backend = c("cpp", "r"), padjust_method = "fdr", cores = 1, verbose = TRUE, seed = 11 )
```

## Description

Calculates dynamic features for lineages

## Value

Returns the modified Seurat object with the calculated dynamic features stored in the tools slot.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunSlingshot(
  pancreas_sub,
  group.by = "SubCellType",
  reduction = "UMAP"
)

pancreas_sub <- RunDynamicFeatures(
  pancreas_sub,
  lineages = c("Lineage1", "Lineage2"),
  n_candidates = 200,
  fit_method = "gam"
)

names(
  pancreas_sub@tools$DynamicFeatures_Lineage1
)
head(
  pancreas_sub@tools$DynamicFeatures_Lineage1$DynamicFeatures
)
ht <- DynamicHeatmap(
  pancreas_sub,
  lineages = c("Lineage1", "Lineage2"),
  cell_annotation = "SubCellType",
  n_split = 3,
  reverse_ht = "Lineage1"
)
ht$plot

DynamicPlot(
  pancreas_sub,
  lineages = c("Lineage1", "Lineage2"),
  features = c("Arxes1", "Ncoa2"),
  group.by = "SubCellType",
  compare_lineages = TRUE,
  compare_features = FALSE
)

pancreas_sub <- RunDynamicFeatures(
  pancreas_sub,
  lineages = c("Lineage1", "Lineage2"),
  n_candidates = 200,
  fit_method = "pretsa"
)
head(
  pancreas_sub@tools$DynamicFeatures_Lineage1$DynamicFeatures
)
ht <- DynamicHeatmap(
  pancreas_sub,
  lineages = c("Lineage1", "Lineage2"),
  cell_annotation = "SubCellType",
  n_split = 3,
  reverse_ht = "Lineage1"
)
ht$plot

DynamicPlot(
  pancreas_sub,
  lineages = c("Lineage1", "Lineage2"),
  features = c("Arxes1", "Ncoa2"),
  group.by = "SubCellType",
  compare_lineages = TRUE,
  compare_features = FALSE
)
```
