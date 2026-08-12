# Run Giotto cell proximity enrichment

- Package: scop
- Language: R
- Function: `GiottoCellProximity`
- Source: https://mengxu98.github.io/scop/reference/GiottoCellProximity.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoCellProximity.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Giotto cell proximity enrichment

## Signature

```text
GiottoCellProximity( x, group.by, network_method = c("Delaunay", "kNN"), network_name = NULL, number_of_simulations = 1000, adjust_method = "fdr", params = list(), verbose = TRUE, seed = 11 )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `group.by`: Metadata column containing cell or spot groups.
- `network_method`: Spatial network method.
- `network_name`: Name for the Giotto spatial network.
- `number_of_simulations`: Number of label simulations used by Giotto.
- `adjust_method`: Multiple-testing correction method.
- `params`: Additional parameters passed to `Giotto::cellProximityEnrichment()`.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.

## Full Documentation

# Run Giotto cell proximity enrichment

## Usage

```text
GiottoCellProximity( x, group.by, network_method = c("Delaunay", "kNN"), network_name = NULL, number_of_simulations = 1000, adjust_method = "fdr", params = list(), verbose = TRUE, seed = 11 )
```

## Description

Run Giotto cell proximity enrichment

## Value

A `giotto2` workflow object.

## Examples

```r
proximity <- data.frame(
  group_1 = c("Ductal", "Ductal", "Endocrine", "Stromal"),
  group_2 = c("Endocrine", "Stromal", "Stromal", "Ductal"),
  enrichment = c(1.6, 0.8, 1.3, 0.7),
  p.adj = c(0.01, 0.08, 0.03, 0.12)
)
g <- structure(
  list(
    results = list(cell_proximity = list(table = proximity)),
    parameters = list(network_method = "Delaunay", number_of_simulations = 100)
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "cell_proximity")

data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))]
)
g <- GiottoSpatialNetwork(g)
g <- GiottoCellProximity(g, group.by = "coda_label", number_of_simulations = 100)
```
