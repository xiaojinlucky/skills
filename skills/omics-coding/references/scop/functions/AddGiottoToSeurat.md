# Add Giotto results back to Seurat

- Package: scop
- Language: R
- Function: `AddGiottoToSeurat`
- Source: https://mengxu98.github.io/scop/reference/AddGiottoToSeurat.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/AddGiottoToSeurat.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add Giotto results back to Seurat

## Signature

```text
AddGiottoToSeurat( srt, x, result = c("cluster", "hmrf"), name = NULL, tool_name = "Giotto", store_result = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `x`: A `giotto2` workflow object.
- `result`: Giotto result to copy back.
- `name`: Metadata column name to write. If `NULL`, a default name is used.
- `tool_name`: Name used to store the Giotto workflow object in `srt@tools`.
- `store_result`: Whether to store the Giotto workflow object in `srt@tools[[tool_name]]`.

## Full Documentation

# Add Giotto results back to Seurat

## Usage

```text
AddGiottoToSeurat( srt, x, result = c("cluster", "hmrf"), name = NULL, tool_name = "Giotto", store_result = TRUE )
```

## Description

Add Giotto results back to Seurat

## Value

A Seurat object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
g <- structure(
  list(
    source = list(cells = colnames(spatial)),
    results = list(
      cluster = list(
        table = data.frame(
          cell = colnames(spatial),
          cluster = spatial$coda_label,
          row.names = colnames(spatial)
        )
      )
    )
  ),
  class = c("giotto2", "list")
)
spatial <- AddGiottoToSeurat(
  spatial,
  g,
  result = "cluster",
  name = "Giotto_cluster",
  store_result = FALSE
)
SpatialSpotPlot(
  spatial,
  group.by = "Giotto_cluster",
  plot_type = "point",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)
```
