# Run semla local G spatial autocorrelation

- Package: scop
- Language: R
- Function: `RunSemlaLocalG`
- Source: https://mengxu98.github.io/scop/reference/RunSemlaLocalG.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSemlaLocalG.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Use semla::RunLocalG() on a Staffli-enabled Seurat object. Results are written by semla to metadata or to an assay, depending on store_in_metadata. SCOP provides no dedicated plot for this result; retrieve its schema record with {[=GetSpatialResult]{GetSpatialResult()}} and inspect the recorded output columns or assay.

## Signature

```text
RunSemlaLocalG( srt, features, alternative = NULL, store_in_metadata = TRUE, assay_name = "GiScores", image_type = "tissue_lowres", verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object with spatial image data.
- `features`: Features passed to semla::RunLocalG().
- `alternative`: Alternative hypothesis passed to semla. Use NULL to keep semla's default behavior.
- `store_in_metadata`: Whether semla should store results in metadata.
- `assay_name`: Assay name used by semla when store_in_metadata = FALSE.
- `image_type`: Image scale used by semla::UpdateSeuratForSemla() when the object does not already contain a Staffli object.
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional arguments passed to semla.

## Full Documentation

# Run semla local G spatial autocorrelation

## Usage

```text
RunSemlaLocalG( srt, features, alternative = NULL, store_in_metadata = TRUE, assay_name = "GiScores", image_type = "tissue_lowres", verbose = TRUE, ... )
```

## Description

Use semla::RunLocalG() on a Staffli-enabled Seurat object. Results are written by semla to metadata or to an assay, depending on store_in_metadata. SCOP provides no dedicated plot for this result; retrieve its schema record with {[=GetSpatialResult]{GetSpatialResult()}} and inspect the recorded output columns or assay.

## Value

A Seurat object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial <- Seurat::NormalizeData(spatial, assay = "Spatial", verbose = FALSE)
features <- rownames(spatial)[1:3]
spatial[[paste0(features[1], "_localG")]] <- as.numeric(scale(spatial$x))

SpatialSpotPlot(
  spatial,
  group.by = paste0(features[1], "_localG"),
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- RunSemlaLocalG(
  spatial,
  features = features,
  store_in_metadata = TRUE,
  verbose = FALSE
)
```
