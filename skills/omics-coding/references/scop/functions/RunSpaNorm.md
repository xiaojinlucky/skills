# Run SpaNorm spatial normalization

- Package: scop
- Language: R
- Function: `RunSpaNorm`
- Source: https://mengxu98.github.io/scop/reference/RunSpaNorm.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSpaNorm.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Normalize spatial transcriptomics counts with the optional Bioconductor SpaNorm backend and store the normalized expression in a new Seurat assay.

## Signature

```text
RunSpaNorm( srt, assay = NULL, layer = "counts", image = NULL, coord.cols = c("col", "row"), new_assay = "SpaNorm", tool_name = "SpaNorm", store_results = TRUE, store_spe = FALSE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Assay layer used for expression values.
- `image`: Name of the Seurat spatial image used by the spatial workflow. Required when multiple images are present; a single image is selected automatically when NULL.
- `coord.cols`: Metadata coordinate columns used by the spatial workflow when no image is available.
- `new_assay`: Name of the assay used to store SpaNorm-normalized data.
- `tool_name`: Name used to store detailed SpaNorm results in srt@tools.
- `store_results`: Whether to store the full result in srt@tools.
- `store_spe`: Whether to store the backend SpatialExperiment returned by SpaNorm.
- `verbose`: Whether to print the message. Default is TRUE.
- `coordinate_space`: Coordinate system supplied to SpaNorm. The default is raw acquisition coordinates; use "legacy_display" explicitly to reproduce the display-scaled coordinates used before scop 0.9.0.
- `...`: Additional arguments passed to SpaNorm::SpaNorm(), such as sample.p.

## Full Documentation

# Run SpaNorm spatial normalization

## Usage

```text
RunSpaNorm( srt, assay = NULL, layer = "counts", image = NULL, coord.cols = c("col", "row"), new_assay = "SpaNorm", tool_name = "SpaNorm", store_results = TRUE, store_spe = FALSE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Description

Normalize spatial transcriptomics counts with the optional Bioconductor SpaNorm backend and store the normalized expression in a new Seurat assay.

## Value

A Seurat object with SpaNorm-normalized expression stored in new_assay. When store_results = TRUE, parameters, coordinates, features, cells, and optional backend output are stored in srt@tools[[tool_name]].

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial <- Seurat::NormalizeData(spatial, assay = "Spatial", verbose = FALSE)

SpatialSpotPlot(
  spatial,
  features = rownames(spatial)[1:2],
  assay = "Spatial",
  layer = "data",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- RunSpaNorm(
  spatial,
  assay = "Spatial",
  layer = "counts",
  coord.cols = c("x", "y"),
  new_assay = "SpaNorm",
  store_spe = FALSE,
  sample.p = 0.25,
  verbose = FALSE
)

SpatialSpotPlot(
  spatial,
  features = rownames(spatial[["SpaNorm"]])[1:2],
  assay = "SpaNorm",
  layer = "data",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)
```
