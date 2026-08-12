# Run Giotto HMRF spatial domains

- Package: scop
- Language: R
- Function: `GiottoHMRF`
- Source: https://mengxu98.github.io/scop/reference/GiottoHMRF.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoHMRF.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Giotto HMRF spatial domains

## Signature

```text
GiottoHMRF( x, spatial_genes = NULL, network_name = "Delaunay_full", k = 20, betas = c(0, 10, 20), hmrf_name = "scop_HMRF", params = list(), verbose = TRUE, seed = 11 )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `spatial_genes`: Spatial genes used by Giotto HMRF.
- `network_name`: Name for the Giotto spatial network.
- `k`: Number of HMRF domains.
- `betas`: HMRF beta values.
- `hmrf_name`: Name for the HMRF result.
- `params`: Additional parameters passed to `Giotto::doHMRF()`.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.

## Full Documentation

# Run Giotto HMRF spatial domains

## Usage

```text
GiottoHMRF( x, spatial_genes = NULL, network_name = "Delaunay_full", k = 20, betas = c(0, 10, 20), hmrf_name = "scop_HMRF", params = list(), verbose = TRUE, seed = 11 )
```

## Description

Run Giotto HMRF spatial domains

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
hmrf_meta <- data.frame(
  cell_ID = colnames(spatial),
  scop_HMRF_k4_b10 = paste0("domain_", as.integer(factor(spatial$coda_label)) \%\% 4 + 1),
  row.names = colnames(spatial)
)
g <- structure(
  list(
    source = list(cells = colnames(spatial), coordinates = coords),
    results = list(
      hmrf = list(
        table = hmrf_meta["scop_HMRF_k4_b10"],
        metadata = hmrf_meta
      )
    )
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "hmrf")

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))]
)
g <- GiottoPreprocess(g)
g <- GiottoSpatialNetwork(g)
g <- GiottoHMRF(
  g,
  spatial_genes = rownames(spatial)[1:30],
  k = 2,
  betas = c(0, 1, 1),
  params = list(numinit = 5)
)
```
