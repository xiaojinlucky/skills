# Run Giotto dimensional reduction

- Package: scop
- Language: R
- Function: `GiottoReduce`
- Source: https://mengxu98.github.io/scop/reference/GiottoReduce.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GiottoReduce.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Giotto dimensional reduction

## Signature

```text
GiottoReduce( x, reduction = c("pca", "umap"), dims = 1:20, name = NULL, features = NULL, params = list(), verbose = TRUE, seed = 11 )
```

## Parameters

- `x`: A `giotto2` workflow object.
- `reduction`: Dimensional reduction to run.
- `dims`: Dimensions to use.
- `name`: Name for the Giotto reduction.
- `features`: Features used for the reduction.
- `params`: Additional parameters passed to the Giotto reduction function.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.

## Full Documentation

# Run Giotto dimensional reduction

## Usage

```text
GiottoReduce( x, reduction = c("pca", "umap"), dims = 1:20, name = NULL, features = NULL, params = list(), verbose = TRUE, seed = 11 )
```

## Description

Run Giotto dimensional reduction

## Value

A `giotto2` workflow object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
embedding <- cbind(
  UMAP_1 = as.numeric(scale(spatial$x)),
  UMAP_2 = as.numeric(scale(spatial$y))
)
rownames(embedding) <- colnames(spatial)
g <- structure(
  list(
    giotto = list(umap = embedding),
    source = list(cells = colnames(spatial), features = rownames(spatial)),
    results = list(
      cluster = list(
        table = data.frame(
          cell = colnames(spatial),
          cluster = spatial$coda_label,
          row.names = colnames(spatial)
        )
      )
    ),
    parameters = list(umap_name = "umap")
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "dim")

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))]
)
g <- GiottoPreprocess(g)
g <- GiottoReduce(g, reduction = "pca", dims = 1:10)
g <- GiottoReduce(g, reduction = "umap", dims = 1:10)
```
