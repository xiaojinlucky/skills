# Run mistyR multiview spatial modeling

- Package: scop
- Language: R
- Function: `RunMistyR`
- Source: https://mengxu98.github.io/scop/reference/RunMistyR.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunMistyR.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a small mistyR view composition from a spatial Seurat object, train MISTy models, collect results, and store a standardized result bundle in srt@tools. The intraview is always created from the selected assay layer; optional juxtaview and paraview components describe local and broader spatial context. mistyR is an optional Bioconductor dependency installable with BiocManager::install("mistyR").

## Signature

```text
RunMistyR( srt, assay = NULL, layer = "data", features = NULL, image = NULL, coord.cols = c("col", "row"), views = "para", para_l = 10, para_zoi = 0, para_family = c("gaussian", "exponential", "linear", "constant"), para_approx = 1, para_nn = NULL, juxta_neighbor_thr = 15, view_cached = FALSE, results_folder = NULL, seed = 42, target_subset = NULL, bypass_intra = FALSE, cv_folds = 10, model_cached = FALSE, append = FALSE, tool_name = "MistyR", store_results = TRUE, store_views = FALSE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Assay used for expression. If NULL, the default assay is used.
- `layer`: Assay layer used for expression values.
- `features`: Features used by MISTy. If NULL, variable features are used when available; otherwise all assay features are used.
- `image`: Name of the Seurat spatial image. Required when multiple images are present; a single image is selected automatically when NULL.
- `coord.cols`: Metadata coordinate columns used when no Seurat image coordinates are available.
- `views`: Spatial views to add besides the required intraview. One or both of "para" and "juxta".
- `para_l, para_zoi, para_family, para_approx, para_nn`: Parameters passed to mistyR::add_paraview(). para_l and para_zoi use the selected coordinate units; para_nn is a unitless neighbor count.
- `juxta_neighbor_thr`: Neighbor threshold passed to mistyR::add_juxtaview(), expressed in the selected coordinate units.
- `view_cached`: Whether generated mistyR views should use cache.
- `results_folder`: Folder passed to mistyR::run_misty(). If NULL, a temporary folder is used.
- `seed, target_subset, bypass_intra, cv_folds, model_cached, append`: Parameters passed to mistyR::run_misty().
- `tool_name`: Name used to store results in srt@tools.
- `store_results`: Whether to store results in srt@tools.
- `store_views`: Whether to store the mistyR view composition in srt@tools. This can be large.
- `verbose`: Whether to print the message. Default is TRUE.
- `coordinate_space`: Coordinate system used to build MISTy views. The default is raw acquisition coordinates; "legacy_display" remains an explicit compatibility option.
- `...`: Additional named arguments passed to mistyR::run_misty().

## Full Documentation

# Run mistyR multiview spatial modeling

## Usage

```text
RunMistyR( srt, assay = NULL, layer = "data", features = NULL, image = NULL, coord.cols = c("col", "row"), views = "para", para_l = 10, para_zoi = 0, para_family = c("gaussian", "exponential", "linear", "constant"), para_approx = 1, para_nn = NULL, juxta_neighbor_thr = 15, view_cached = FALSE, results_folder = NULL, seed = 42, target_subset = NULL, bypass_intra = FALSE, cv_folds = 10, model_cached = FALSE, append = FALSE, tool_name = "MistyR", store_results = TRUE, store_views = FALSE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Description

Build a small mistyR view composition from a spatial Seurat object, train MISTy models, collect results, and store a standardized result bundle in srt@tools. The intraview is always created from the selected assay layer; optional juxtaview and paraview components describe local and broader spatial context. mistyR is an optional Bioconductor dependency installable with BiocManager::install("mistyR").

## Value

A Seurat object with results stored in srt@tools[[tool_name]] when store_results = TRUE.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial <- Seurat::NormalizeData(spatial, assay = "Spatial", verbose = FALSE)

spatial <- RunMistyR(
  spatial,
  assay = "Spatial",
  layer = "data",
  features = rownames(spatial)[1:10],
  coord.cols = c("x", "y"),
  views = "para",
  para_l = 5,
  cv_folds = 3,
  verbose = FALSE
)
spatial@tools$MistyR$summary
```
