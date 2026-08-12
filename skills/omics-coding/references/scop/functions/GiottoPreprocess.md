# Preprocess an internal Giotto workflow object

- Package: scop
- Language: R
- Function: `GiottoPreprocess`
- Source: https://mengxu98.github.io/scop/reference/GiottoPreprocess.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoPreprocess.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Preprocess an internal Giotto workflow object

## Signature

```text
GiottoPreprocess( x, filter_params = list(), norm_params = list(), stat_params = list(), hvf_params = list(), verbose = TRUE, seed = 11 )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `filter_params`: Additional parameters reserved for future filtering.
- `norm_params`: Additional parameters passed to `Giotto::normalizeGiotto()`.
- `stat_params`: Additional parameters passed to `Giotto::addStatistics()`.
- `hvf_params`: Additional parameters passed to `Giotto::calculateHVF()`.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.

## Full Documentation

# Preprocess an internal Giotto workflow object

## Usage

```text
GiottoPreprocess( x, filter_params = list(), norm_params = list(), stat_params = list(), hvf_params = list(), verbose = TRUE, seed = 11 )
```

## Description

Preprocess an internal Giotto workflow object

## Value

A `giotto2` workflow object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
g <- structure(
  list(
    source = list(
      cells = colnames(spatial),
      features = rownames(spatial)[1:100],
      coordinates = data.frame(cell_ID = colnames(spatial), sdimx = spatial$x, sdimy = spatial$y)
    ),
    results = list(),
    active = NULL
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "spatial")

g <- SeuratToGiotto2(
  spatial,
  assay = "Spatial",
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))],
  verbose = FALSE
)
g <- GiottoPreprocess(g, verbose = FALSE)
```
