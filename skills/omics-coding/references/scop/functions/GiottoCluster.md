# Run Giotto nearest-network clustering

- Package: scop
- Language: R
- Function: `GiottoCluster`
- Source: https://mengxu98.github.io/scop/reference/GiottoCluster.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoCluster.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Giotto nearest-network clustering

## Signature

```text
GiottoCluster( x, method = c("leiden", "louvain"), dims = 1:20, k = 20, resolution = 1, network_name = "scop_NN", cluster_name = NULL, params = list(), verbose = TRUE, seed = 11 )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `method`: Giotto clustering method.
- `dims`: Dimensions used to build the nearest-neighbor network.
- `k`: Number of nearest neighbors.
- `resolution`: Clustering resolution.
- `network_name`: Name for the Giotto nearest-neighbor network.
- `cluster_name`: Name for the Giotto cluster result.
- `params`: Additional parameters passed to the Giotto clustering function.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.

## Full Documentation

# Run Giotto nearest-network clustering

## Usage

```text
GiottoCluster( x, method = c("leiden", "louvain"), dims = 1:20, k = 20, resolution = 1, network_name = "scop_NN", cluster_name = NULL, params = list(), verbose = TRUE, seed = 11 )
```

## Description

Run Giotto nearest-network clustering

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
g <- structure(
  list(
    source = list(cells = colnames(spatial), coordinates = coords),
    results = list(
      cluster = list(
        table = data.frame(
          cell = colnames(spatial),
          cluster = spatial$coda_label,
          row.names = colnames(spatial)
        )
      )
    ),
    parameters = list(k = 8, resolution = 0.4)
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "cluster")

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))]
)
g <- GiottoPreprocess(g)
g <- GiottoReduce(g, reduction = "pca", dims = 1:10)
g <- GiottoCluster(g, dims = 1:10, k = 8, resolution = 0.4)
```
