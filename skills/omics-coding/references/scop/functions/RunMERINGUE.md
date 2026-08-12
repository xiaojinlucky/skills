# Run MERINGUE spatial autocorrelation analysis

- Package: scop
- Language: R
- Function: `RunMERINGUE`
- Source: https://mengxu98.github.io/scop/reference/RunMERINGUE.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunMERINGUE.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run MERINGUE spatial autocorrelation, spatial cross-correlation, and spatial module analysis for a spatial Seurat object.

## Signature

```text
RunMERINGUE( srt, assay = NULL, layer = "data", image = NULL, coord.cols = c("col", "row"), features = NULL, mode = c("autocorrelation", "cross_correlation", "modules"), nfeatures = 2000, min_spots = 5, filterDist = NA_real_, binary = TRUE, alternative = "greater", nperm = 0, ncores = 1, pairwise_features = NULL, set_variable_features = FALSE, store_results = TRUE, verbose = TRUE, seed = 11, neighbor_params = list(), moran_params = list(), cross_cor_params = list(), module_params = list(), coordinate_space = c("raw", "legacy_display") )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Assay layer used for expression values.
- `image`: Name of the Seurat spatial image used by the spatial workflow. Required when multiple images are present; a single image is selected automatically when NULL.
- `coord.cols`: Metadata coordinate columns used by the spatial workflow when no image is available.
- `features`: Features to score. If NULL, current variable features are used; if no variable features are present, all assay features are used.
- `mode`: MERINGUE analysis modes to run. "autocorrelation" computes spatial autocorrelation, "cross_correlation" computes pairwise spatial cross-correlation, and "modules" detects spatial gene modules.
- `nfeatures`: Number of top spatial features stored in srt@tools[["SpatialVariableFeatures"]].
- `min_spots`: Minimum number of spots with non-zero expression required for a feature to be tested.
- `filterDist`: Euclidean distance cutoff passed to MERINGUE::getSpatialNeighbors(), expressed in the selected coordinate units.
- `binary`: Whether to binarize the MERINGUE spatial neighbor matrix.
- `alternative`: Alternative hypothesis passed to MERINGUE Moran tests.
- `nperm`: Number of label permutations used for empirical p values. The default 0 skips p-value calculation.
- `ncores`: Number of cores passed to MERINGUE permutation tests.
- `pairwise_features`: Features used for spatial cross-correlation. If NULL, top spatially autocorrelated features are used.
- `set_variable_features`: Whether to set the top spatial features as variable features for assay.
- `store_results`: Whether to store the full result in srt@tools.
- `verbose`: Whether to print the message. Default is TRUE.
- `seed`: Random seed used for permutation tests.
- `neighbor_params, moran_params, cross_cor_params, module_params`: Named lists of additional arguments passed to the corresponding MERINGUE steps.
- `coordinate_space`: Coordinate system used for MERINGUE distances. The default is raw acquisition coordinates; "legacy_display" remains an explicit compatibility option.

## Full Documentation

# Run MERINGUE spatial autocorrelation analysis

## Usage

```text
RunMERINGUE( srt, assay = NULL, layer = "data", image = NULL, coord.cols = c("col", "row"), features = NULL, mode = c("autocorrelation", "cross_correlation", "modules"), nfeatures = 2000, min_spots = 5, filterDist = NA_real_, binary = TRUE, alternative = "greater", nperm = 0, ncores = 1, pairwise_features = NULL, set_variable_features = FALSE, store_results = TRUE, verbose = TRUE, seed = 11, neighbor_params = list(), moran_params = list(), cross_cor_params = list(), module_params = list(), coordinate_space = c("raw", "legacy_display") )
```

## Description

Run MERINGUE spatial autocorrelation, spatial cross-correlation, and spatial module analysis for a spatial Seurat object.

## Value

A Seurat object with MERINGUE results stored in srt@tools[["MERINGUE"]]. Top autocorrelated features are available at srt@tools[["MERINGUE"]]$summary$top_features.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial <- Seurat::NormalizeData(spatial, assay = "Spatial", verbose = FALSE)
spatial@tools[["MERINGUE"]] <- list(
  autocorrelation = data.frame(
    feature = rownames(spatial)[1:4],
    statistic = c(0.42, 0.35, 0.28, 0.22),
    p_value = c(0.001, 0.004, 0.010, 0.020),
    q_value = c(0.004, 0.008, 0.015, 0.030)
  )
)

head(spatial@tools[["MERINGUE"]]$autocorrelation)
SpatialSpotPlot(
  spatial,
  features = spatial@tools[["MERINGUE"]]$autocorrelation$feature[1:2],
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- RunMERINGUE(
  spatial,
  assay = "Spatial",
  coord.cols = c("x", "y"),
  mode = c("autocorrelation", "cross_correlation"),
  nfeatures = 50,
  verbose = FALSE
)
```
