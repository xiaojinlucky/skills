# Create a Giotto spatial network

- Package: scop
- Language: R
- Function: `GiottoSpatialNetwork`
- Source: https://mengxu98.github.io/scop/reference/GiottoSpatialNetwork.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoSpatialNetwork.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a Giotto spatial network

## Signature

```text
GiottoSpatialNetwork( x, network_method = c("Delaunay", "kNN"), network_name = NULL, params = list(), verbose = TRUE )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `network_method`: Spatial network method.
- `network_name`: Name for the Giotto spatial network.
- `params`: Additional parameters passed to `Giotto::createSpatialNetwork()`.
- `verbose`: Whether to print progress messages.

## Full Documentation

# Create a Giotto spatial network

## Usage

```text
GiottoSpatialNetwork( x, network_method = c("Delaunay", "kNN"), network_name = NULL, params = list(), verbose = TRUE )
```

## Description

Create a Giotto spatial network

## Value

A `giotto2` workflow object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
coords <- data.frame(
  cell_ID = colnames(spatial),
  sdimx = spatial$x,
  sdimy = spatial$y,
  row.names = colnames(spatial)
)
edges <- data.frame(
  from = colnames(spatial)[1:79],
  to = colnames(spatial)[2:80]
)
g <- structure(
  list(
    source = list(cells = colnames(spatial), coordinates = coords),
    results = list(spatial_network = list(name = "Delaunay_network", table = edges))
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "network")

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))]
)
g <- GiottoSpatialNetwork(g, network_method = "Delaunay")
```
