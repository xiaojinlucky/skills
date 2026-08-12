# Convert SpatialExperiment to Seurat

- Package: scop
- Language: R
- Function: `spe_to_srt`
- Source: https://mengxu98.github.io/scop/reference/spe_to_srt.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/spe_to_srt.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a Seurat object from a SpatialExperiment, preserving colData and spatial coordinates as metadata columns.

## Signature

```text
spe_to_srt( spe, assay = "Spatial", layer = NULL, coord.cols = c("x", "y"), project = "SpatialExperiment" )
```

## Parameters

- `spe`: A SpatialExperiment or SummarizedExperiment.
- `assay`: Assay name for the created Seurat assay.
- `layer`: Assay from spe to use as counts. If NULL, the first assay is used.
- `coord.cols`: Metadata names used for spatial coordinates in Seurat.
- `project`: Project name passed to Seurat::CreateSeuratObject().

## Full Documentation

# Convert SpatialExperiment to Seurat

## Usage

```text
spe_to_srt( spe, assay = "Spatial", layer = NULL, coord.cols = c("x", "y"), project = "SpatialExperiment" )
```

## Description

Create a Seurat object from a SpatialExperiment, preserving colData and spatial coordinates as metadata columns.

## Value

A Seurat object.
