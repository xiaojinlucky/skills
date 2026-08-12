# Run smoothclust spatial domain clustering

- Package: scop
- Language: R
- Function: `RunSmoothClust`
- Source: https://mengxu98.github.io/scop/reference/RunSmoothClust.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSmoothClust.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Smooth expression across spatial neighborhoods with the optional smoothclust package, then cluster the smoothed profiles into spatial domains with PCA and k-means.

## Signature

```text
RunSmoothClust( srt, assay = NULL, layer = "data", image = NULL, coord.cols = c("col", "row"), features = NULL, nfeatures = 2000, min_spots = 5, smooth_method = c("uniform", "kernel", "knn"), bandwidth = 0.05, k = 18, truncate = 0.05, cores = 1, n_threads = NULL, n_clusters, n_pcs = 15, center = TRUE, scale = TRUE, nstart = 10, iter.max = 100, algorithm = "Hartigan-Wong", cluster_colname = "SmoothClust_cluster", tool_name = "SmoothClust", store_results = TRUE, store_smoothed = FALSE, seed = 11, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Assay used for expression. If NULL, the default assay is used.
- `layer`: Assay layer used for expression values.
- `image`: Name of the Seurat spatial image. Required when multiple images are present; a single image is selected automatically when NULL.
- `coord.cols`: Metadata coordinate columns used when no Seurat image is available.
- `features`: Features to use. If NULL, current variable features are used; if no variable features are present, the top nfeatures by variance are used.
- `nfeatures`: Number of variance-ranked features to use when features = NULL and no variable features are present.
- `min_spots`: Minimum number of spots with non-zero expression required for a feature to be used.
- `smooth_method`: Smoothing method passed to smoothclust::smoothclust().
- `bandwidth, k, truncate`: Smoothing parameters passed to smoothclust::smoothclust(). bandwidth uses the selected coordinate units; truncate is the backend's dimensionless kernel cutoff, and k and are unitless counts.
- `cores`: Number of workers passed to smoothclust::smoothclust().
- `n_threads`: Deprecated alias for cores.
- `n_clusters`: Number of spatial domains for k-means clustering. This must be supplied explicitly.
- `n_pcs`: Number of principal components used for k-means.
- `center, scale`: Whether to center and scale features before PCA.
- `nstart, iter.max, algorithm`: Parameters passed to stats::kmeans().
- `cluster_colname`: Metadata column used for smoothclust clusters.
- `tool_name`: Name used to store detailed results in srt@tools.
- `store_results`: Whether to store detailed results in srt@tools.
- `store_smoothed`: Whether to store the smoothed expression matrix in srt@tools[[tool_name]]. This can be large.
- `seed`: Random seed used for k-means.
- `verbose`: Whether to print progress messages.
- `coordinate_space`: Coordinate system used for distance-sensitive smoothing and smoothness calculations. The default is raw acquisition coordinates. Use "legacy_display" explicitly to reproduce the display-scaled behavior used before scop 0.9.0.
- `...`: Additional arguments passed to smoothclust::smoothclust().

## Full Documentation

# Run smoothclust spatial domain clustering

## Usage

```text
RunSmoothClust( srt, assay = NULL, layer = "data", image = NULL, coord.cols = c("col", "row"), features = NULL, nfeatures = 2000, min_spots = 5, smooth_method = c("uniform", "kernel", "knn"), bandwidth = 0.05, k = 18, truncate = 0.05, cores = 1, n_threads = NULL, n_clusters, n_pcs = 15, center = TRUE, scale = TRUE, nstart = 10, iter.max = 100, algorithm = "Hartigan-Wong", cluster_colname = "SmoothClust_cluster", tool_name = "SmoothClust", store_results = TRUE, store_smoothed = FALSE, seed = 11, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Description

Smooth expression across spatial neighborhoods with the optional smoothclust package, then cluster the smoothed profiles into spatial domains with PCA and k-means.

## Value

A Seurat object with smoothclust clusters in metadata. When store_results = TRUE, detailed outputs are stored in srt@tools[[tool_name]].

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial$SmoothClust_cluster <- factor(
  paste0("SmoothClust", (seq_len(ncol(spatial)) - 1) \%\% 3 + 1)
)

SpatialSpotPlot(
  spatial,
  group.by = "SmoothClust_cluster",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- Seurat::NormalizeData(spatial, assay = "Spatial", verbose = FALSE)
spatial <- Seurat::FindVariableFeatures(
  spatial,
  assay = "Spatial",
  nfeatures = 200,
  verbose = FALSE
)

spatial <- RunSmoothClust(
  spatial,
  assay = "Spatial",
  n_clusters = 3,
  smooth_method = "knn",
  coord.cols = c("x", "y"),
  k = 6,
  verbose = FALSE
)

table(spatial$SmoothClust_cluster)
```
