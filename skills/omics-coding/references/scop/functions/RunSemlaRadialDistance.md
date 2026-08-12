# Run semla radial distance analysis

- Package: scop
- Language: R
- Function: `RunSemlaRadialDistance`
- Source: https://mengxu98.github.io/scop/reference/RunSemlaRadialDistance.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSemlaRadialDistance.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Use semla::RadialDistance() to calculate distances from selected spatial regions and write the returned columns to Seurat metadata. SCOP provides no dedicated plot for this result; retrieve its schema record with {[=GetSpatialResult]{GetSpatialResult()}} and inspect the recorded metadata columns.

## Signature

```text
RunSemlaRadialDistance( srt, column_name, selected_groups = NULL, column_suffix = NULL, image_type = "tissue_lowres", verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object with spatial image data.
- `column_name`: Metadata column containing region labels.
- `selected_groups`: Region labels used by semla. If NULL, semla uses all labels in column_name.
- `column_suffix`: Optional suffix for metadata columns returned by semla.
- `image_type`: Image scale used by semla::UpdateSeuratForSemla() when the object does not already contain a Staffli object.
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional arguments passed to semla.

## Full Documentation

# Run semla radial distance analysis

## Usage

```text
RunSemlaRadialDistance( srt, column_name, selected_groups = NULL, column_suffix = NULL, image_type = "tissue_lowres", verbose = TRUE, ... )
```

## Description

Use semla::RadialDistance() to calculate distances from selected spatial regions and write the returned columns to Seurat metadata. SCOP provides no dedicated plot for this result; retrieve its schema record with {[=GetSpatialResult]{GetSpatialResult()}} and inspect the recorded metadata columns.

## Value

A Seurat object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial$region <- ifelse(
  spatial$y > stats::median(spatial$y),
  "upper",
  "lower"
)
upper_center <- c(
  stats::median(spatial$x[spatial$region == "upper"]),
  stats::median(spatial$y[spatial$region == "upper"])
)
spatial$upper_distance <- sqrt(
  (spatial$x - upper_center[1])^2 + (spatial$y - upper_center[2])^2
)

SpatialSpotPlot(
  spatial,
  group.by = "upper_distance",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- RunSemlaRadialDistance(
  spatial,
  column_name = "region",
  selected_groups = "upper",
  column_suffix = "upper_distance",
  verbose = FALSE
)
```
