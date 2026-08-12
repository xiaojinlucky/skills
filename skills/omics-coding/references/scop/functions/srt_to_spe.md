# Convert Seurat to SpatialExperiment

- Package: scop
- Language: R
- Function: `srt_to_spe`
- Source: https://mengxu98.github.io/scop/reference/srt_to_spe.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_to_spe.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a lightweight SpatialExperiment from a spatial Seurat object using one assay layer, metadata, and resolved spatial coordinates.

## Signature

```text
srt_to_spe( srt, assay = NULL, layer = "counts", coord.cols = c("col", "row"), image = NULL, include_meta = TRUE, coordinate_space = c("legacy_display", "raw") )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Assay to export. If NULL, the default assay is used.
- `layer`: Assay layer to export.
- `coord.cols`: Metadata coordinate columns. By default, SCOP resolves x/y first and then col/row.
- `image`: Optional Seurat image name. When present, image-derived coordinates are used.
- `include_meta`: Whether to include Seurat metadata as colData.
- `coordinate_space`: Coordinate space exported to spatialCoords. "legacy_display" preserves the historical scaled/y-flipped behavior; "raw" preserves analysis distances.

## Full Documentation

# Convert Seurat to SpatialExperiment

## Usage

```text
srt_to_spe( srt, assay = NULL, layer = "counts", coord.cols = c("col", "row"), image = NULL, include_meta = TRUE, coordinate_space = c("legacy_display", "raw") )
```

## Description

Create a lightweight SpatialExperiment from a spatial Seurat object using one assay layer, metadata, and resolved spatial coordinates.

## Value

A SpatialExperiment.
