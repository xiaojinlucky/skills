# Run ambient RNA decontamination with decontX

- Package: scop
- Language: R
- Function: `RunDecontX`
- Source: https://mengxu98.github.io/scop/reference/RunDecontX.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunDecontX.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run ambient RNA decontamination with decontX

## Signature

```text
RunDecontX( srt, assay = "RNA", group.by = NULL, batch = NULL, background = NULL, background_assay = NULL, bg_batch = NULL, assay_name = "decontXcounts", store_assay = TRUE, round_counts = FALSE, data_type = NULL, seed = 11, ..., verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for decontamination. Default is "RNA".
- `group.by`: Cell cluster labels passed to {[decontX:decontX]{decontX::decontX()}}. Can be NULL, a meta.data column name, or a vector aligned to cells. Default is NULL.
- `batch`: Batch labels passed to {[decontX:decontX]{decontX::decontX()}}. Can be NULL, a meta.data column name, or a vector aligned to cells. Default is NULL.
- `background`: Optional background / empty-droplet input passed to {[decontX:decontX]{decontX::decontX()}}. Can be a Seurat object, SingleCellExperiment, or count matrix. Default is NULL.
- `background_assay`: Assay name used when background is a Seurat object or SingleCellExperiment. Default is NULL, which falls back to assay for Seurat background and "counts" for SingleCellExperiment background.
- `bg_batch`: Batch labels for background passed to {[decontX:decontX]{decontX::decontX()}}. Can be NULL, a metadata column name, or a vector aligned to the background droplets. Default is NULL.
- `assay_name`: Name of the assay used to store decontaminated counts. Default is "decontXcounts".
- `store_assay`: Whether to store decontaminated counts as a new assay. Default is TRUE.
- `round_counts`: Whether to round decontaminated counts before creating the assay. Default is FALSE.
- `data_type`: Optional precomputed result from {[=CheckDataType]{CheckDataType()}} for the input assay. Primarily used internally to avoid repeated scans of the same count matrix across nested QC calls.
- `seed`: Random seed for reproducibility. Default is 11.
- `...`: Additional arguments passed to {[decontX:decontX]{decontX::decontX()}}.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run ambient RNA decontamination with decontX

## Usage

```text
RunDecontX( srt, assay = "RNA", group.by = NULL, batch = NULL, background = NULL, background_assay = NULL, bg_batch = NULL, assay_name = "decontXcounts", store_assay = TRUE, round_counts = FALSE, data_type = NULL, seed = 11, ..., verbose = TRUE )
```

## Description

Run ambient RNA decontamination with decontX

## Value

Returns a Seurat object with decontX contamination estimates stored in the meta.data, and optional decontaminated counts stored in a new assay.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunDecontX(
  pancreas_sub,
  group.by = "CellType"
)

FeatureStatPlot(
  pancreas_sub,
  stat.by = "decontX_contamination"
)

FeatureDimPlot(
  pancreas_sub,
  features = "decontX_contamination"
)
```
