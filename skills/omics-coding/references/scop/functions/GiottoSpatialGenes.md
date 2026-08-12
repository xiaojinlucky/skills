# Run Giotto spatial gene detection

- Package: scop
- Language: R
- Function: `GiottoSpatialGenes`
- Source: https://mengxu98.github.io/scop/reference/GiottoSpatialGenes.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoSpatialGenes.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Giotto spatial gene detection

## Signature

```text
GiottoSpatialGenes( x, features = NULL, network_method = c("Delaunay", "kNN"), network_name = NULL, bin_method = c("kmeans", "rank"), top_n = 100, params = list(), verbose = TRUE, seed = 11 )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `features`: Features to test.
- `network_method`: Spatial network method.
- `network_name`: Name for the Giotto spatial network.
- `bin_method`: Binarization method passed to `Giotto::binSpect()`.
- `top_n`: Number of top spatial genes to store.
- `params`: Additional parameters passed to `Giotto::binSpect()`.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.

## Full Documentation

# Run Giotto spatial gene detection

## Usage

```text
GiottoSpatialGenes( x, features = NULL, network_method = c("Delaunay", "kNN"), network_name = NULL, bin_method = c("kmeans", "rank"), top_n = 100, params = list(), verbose = TRUE, seed = 11 )
```

## Description

Run Giotto spatial gene detection

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
spatial_gene_table <- data.frame(
  feat_ID = rownames(spatial)[1:8],
  spatGeneRank = seq_len(8),
  adj.p.value = seq(0.001, 0.04, length.out = 8)
)
g <- structure(
  list(
    source = list(cells = colnames(spatial), coordinates = coords),
    results = list(
      spatial_genes = list(
        table = spatial_gene_table,
        top_features = spatial_gene_table$feat_ID
      )
    )
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "spatial_genes", top_n = 6)

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))]
)
g <- GiottoPreprocess(g)
g <- GiottoSpatialNetwork(g)
g <- GiottoSpatialGenes(g, features = rownames(spatial)[1:50], top_n = 10)
```
