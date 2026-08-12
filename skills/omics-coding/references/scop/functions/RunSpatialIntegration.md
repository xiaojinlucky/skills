# Run multi-sample spatial integration

- Package: scop
- Language: R
- Function: `RunSpatialIntegration`
- Source: https://mengxu98.github.io/scop/reference/RunSpatialIntegration.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSpatialIntegration.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Integrate multi-slice or multi-sample spatial transcriptomics data with an optional spatial backend and store standardized embeddings, domains, and aligned coordinates in a Seurat object.

## Signature

```text
RunSpatialIntegration( object, method = c("PRECAST", "BASS", "SpatialMNN"), sample.by = NULL, assay = NULL, layer = "counts", coord.cols = c("col", "row"), features = NULL, image = NULL, reduction.name = NULL, cluster_colname = NULL, tool_name = "SpatialIntegration", store_results = TRUE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Parameters

- `object`: A merged spatial Seurat object or a list of spatial Seurat objects.
- `method`: Spatial integration backend.
- `sample.by`: Metadata column identifying samples for a merged Seurat object. For list input, list names are copied into this column.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Assay layer used for expression values.
- `coord.cols`: Metadata coordinate columns used by the spatial workflow when no image is available.
- `features`: Features to score. If NULL, current variable features are used; if no variable features are present, all assay features are used.
- `image`: Name of the Seurat spatial image used by the spatial workflow. Required when multiple images are present; a single image is selected automatically when NULL.
- `reduction.name`: Name of the integrated embedding reduction. If NULL, a method-specific name is used.
- `cluster_colname`: Metadata column used for spatial domain labels. If NULL, a method-specific name is used.
- `tool_name`: Name used to store detailed results in srt@tools.
- `store_results`: Whether to store the full result in srt@tools.
- `verbose`: Whether to print the message. Default is TRUE.
- `coordinate_space`: Coordinate system used for integration distances and aligned-coordinate input. The default is raw acquisition coordinates; "legacy_display" remains an explicit compatibility option.
- `...`: Additional backend-specific arguments.

## Full Documentation

# Run multi-sample spatial integration

## Usage

```text
RunSpatialIntegration( object, method = c("PRECAST", "BASS", "SpatialMNN"), sample.by = NULL, assay = NULL, layer = "counts", coord.cols = c("col", "row"), features = NULL, image = NULL, reduction.name = NULL, cluster_colname = NULL, tool_name = "SpatialIntegration", store_results = TRUE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Description

Integrate multi-slice or multi-sample spatial transcriptomics data with an optional spatial backend and store standardized embeddings, domains, and aligned coordinates in a Seurat object.

## Value

A Seurat object with spatial integration results stored in metadata, reductions, and srt@tools[[tool_name]].

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial$sample <- ifelse(spatial$y > stats::median(spatial$y), "slice_a", "slice_b")
spatial$SpatialIntegration_PRECAST_domain <- factor(
  paste0("domain_", (seq_len(ncol(spatial)) - 1) \%\% 3 + 1)
)
embedding <- cbind(
  SI_1 = as.numeric(scale(spatial$x)),
  SI_2 = as.numeric(scale(spatial$y))
)
rownames(embedding) <- colnames(spatial)
spatial[["SpatialIntegration_PRECAST"]] <- SeuratObject::CreateDimReducObject(
  embeddings = embedding,
  key = "SI_",
  assay = "Spatial"
)
spatial$SpatialIntegration_PRECAST_aligned_x <- spatial$x +
  ifelse(spatial$sample == "slice_b", -stats::median(spatial$x), 0)
spatial$SpatialIntegration_PRECAST_aligned_y <- spatial$y
integration_parameters <- list(
  method = "PRECAST",
  sample.by = "sample",
  assay = "Spatial",
  layer = "counts",
  coord.cols = c("x", "y"),
  reduction.name = "SpatialIntegration_PRECAST",
  cluster_colname = "SpatialIntegration_PRECAST_domain",
  aligned_coord_cols = c(
    "SpatialIntegration_PRECAST_aligned_x",
    "SpatialIntegration_PRECAST_aligned_y"
  )
)
spatial@tools$SpatialIntegration <- list(
  active_method = "PRECAST",
  methods = list(PRECAST = list(parameters = integration_parameters)),
  parameters = integration_parameters,
  samples = unique(spatial$sample),
  cells = colnames(spatial)
)

SpatialIntegrationPlot(
  spatial,
  plot_type = "spatial",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)
SpatialIntegrationPlot(spatial, plot_type = "embedding")
SpatialIntegrationPlot(spatial, plot_type = "alignment")
SpatialIntegrationPlot(spatial, plot_type = "composition")

srt <- RunSpatialIntegration(
  object = spatial,
  method = "PRECAST",
  sample.by = "sample",
  assay = "Spatial",
  coord.cols = c("x", "y"),
  features = rownames(spatial)[1:300],
  verbose = FALSE
)
```
