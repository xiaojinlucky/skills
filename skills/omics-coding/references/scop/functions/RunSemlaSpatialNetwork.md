# Run semla spatial network construction

- Package: scop
- Language: R
- Function: `RunSemlaSpatialNetwork`
- Source: https://mengxu98.github.io/scop/reference/RunSemlaSpatialNetwork.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSemlaSpatialNetwork.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Use the optional semla package as a backend to prepare a Staffli-enabled Seurat object and compute spot-level spatial networks. The network is stored in srt@tools[[tool_name]] when store_results = TRUE. SCOP provides no dedicated plot for this result; retrieve it with {[=GetSpatialResult]{GetSpatialResult()}} and use an existing generic spatial plot when needed.

## Signature

```text
RunSemlaSpatialNetwork( srt, image_type = "tissue_lowres", nNeighbors = 6, maxDist = NULL, minK = 0, coords = "pixels", tool_name = "SemlaSpatialNetwork", store_results = TRUE, verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object with spatial image data.
- `image_type`: Image scale used by semla::UpdateSeuratForSemla() when the object does not already contain a Staffli object.
- `nNeighbors`: Number of nearest spatial neighbors.
- `maxDist`: Optional maximum neighbor distance.
- `minK`: Minimum number of retained neighbors per spot.
- `coords`: Coordinate system passed to semla::GetSpatialNetwork().
- `tool_name`: Name used to store results in srt@tools.
- `store_results`: Whether to store the semla spatial network in srt@tools.
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional arguments passed to semla.

## Full Documentation

# Run semla spatial network construction

## Usage

```text
RunSemlaSpatialNetwork( srt, image_type = "tissue_lowres", nNeighbors = 6, maxDist = NULL, minK = 0, coords = "pixels", tool_name = "SemlaSpatialNetwork", store_results = TRUE, verbose = TRUE, ... )
```

## Description

Use the optional semla package as a backend to prepare a Staffli-enabled Seurat object and compute spot-level spatial networks. The network is stored in srt@tools[[tool_name]] when store_results = TRUE. SCOP provides no dedicated plot for this result; retrieve it with {[=GetSpatialResult]{GetSpatialResult()}} and use an existing generic spatial plot when needed.

## Value

A Seurat object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial@tools$SemlaSpatialNetwork <- list(
  network = data.frame(
    from = colnames(spatial)[1:6],
    to = colnames(spatial)[2:7],
    distance = sqrt(diff(spatial$x[1:7])^2 + diff(spatial$y[1:7])^2)
  )
)

head(spatial@tools$SemlaSpatialNetwork$network)
SpatialSpotPlot(
  spatial,
  group.by = "coda_label",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- RunSemlaSpatialNetwork(
  spatial,
  nNeighbors = 6,
  coords = "pixels",
  verbose = FALSE
)
```
