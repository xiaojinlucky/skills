# Build a native spatial network

- Package: scop
- Language: R
- Function: `RunSpatialNetwork`
- Source: https://mengxu98.github.io/scop/reference/RunSpatialNetwork.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSpatialNetwork.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a k-nearest-neighbor or radius spatial network from raw Seurat spatial coordinates. Results are stored as named graphs in `srt@tools$SpatialNetwork`.

## Signature

```text
RunSpatialNetwork( srt, method = c("knn", "radius"), image = NULL, coord.cols = c("col", "row"), k = 6, radius = NULL, graph.name = NULL, overwrite = FALSE, verbose = TRUE )
```

## Parameters

- `srt`: A `Seurat` object.
- `method`: Network method, either `"knn"` or `"radius"`.
- `image`: Seurat image name. A single image is selected automatically; multi-image objects require an explicit value.
- `coord.cols`: Metadata columns used when the object has no image.
- `k`: Number of neighbors for `method = "knn"`.
- `radius`: Positive distance threshold for `method = "radius"`, expressed in the raw coordinate units.
- `graph.name`: Optional graph name. If `NULL`, a deterministic name is generated from the image, method, and method parameter.
- `overwrite`: Whether an existing graph with the same name may be replaced.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Build a native spatial network

## Usage

```text
RunSpatialNetwork( srt, method = c("knn", "radius"), image = NULL, coord.cols = c("col", "row"), k = 6, radius = NULL, graph.name = NULL, overwrite = FALSE, verbose = TRUE )
```

## Description

Build a k-nearest-neighbor or radius spatial network from raw Seurat spatial coordinates. Results are stored as named graphs in `srt@tools$SpatialNetwork`.

## Value

The input `Seurat` object with a `SpatialNetwork` result in `srt@tools`.

## Examples

```r
counts <- matrix(
  c(3, 1, 0, 2, 0, 4, 1, 0, 2, 1, 3, 0),
  nrow = 3,
  dimnames = list(paste0("gene", 1:3), paste0("spot", 1:4))
)
srt <- SeuratObject::CreateSeuratObject(counts)
srt$col <- c(0, 1, 0, 1)
srt$row <- c(0, 0, 1, 1)
srt <- RunSpatialNetwork(srt, k = 2, verbose = FALSE)
SpatialNetworkPlot(srt)
```
