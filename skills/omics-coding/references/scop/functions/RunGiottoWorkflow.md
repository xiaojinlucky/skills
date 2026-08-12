# Run a Giotto workflow

- Package: scop
- Language: R
- Function: `RunGiottoWorkflow`
- Source: https://mengxu98.github.io/scop/reference/RunGiottoWorkflow.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunGiottoWorkflow.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run basic or full Giotto analysis on a `giotto2` object. Seurat input is converted first with [SeuratToGiotto2()].

## Signature

```text
RunGiottoWorkflow( x, steps = c("basic", "full"), group.by = NULL, return_seurat = inherits(x, "Seurat"), store_results = TRUE, tool_name = "Giotto", verbose = TRUE, seed = 11, ... )
```

## Parameters

- `x`: A `giotto2` or Seurat object.
- `steps`: `"basic"` runs preprocessing, PCA/UMAP, nearest-network clustering, and spatial network construction. `"full"` additionally runs spatial genes, spatial modules, optional cell proximity, and HMRF.
- `group.by`: Metadata column used for cell proximity enrichment.
- `return_seurat`: Whether to return a Seurat object when `x` is Seurat. If `FALSE`, returns the internal `giotto2` workflow object.
- `store_results`: Whether to store the internal Giotto workflow object in `srt@tools[[tool_name]]` when returning Seurat.
- `tool_name`: Name used to store the Giotto workflow object in `srt@tools`.
- `verbose`: Whether to print progress messages.
- `seed`: Random seed for reproducible Giotto calls.
- `...`: Passed to [SeuratToGiotto2()] when `x` is Seurat.

## Full Documentation

# Run a Giotto workflow

## Usage

```text
RunGiottoWorkflow( x, steps = c("basic", "full"), group.by = NULL, return_seurat = inherits(x, "Seurat"), store_results = TRUE, tool_name = "Giotto", verbose = TRUE, seed = 11, ... )
```

## Description

Run basic or full Giotto analysis on a `giotto2` object. Seurat input is converted first with [SeuratToGiotto2()].

## Value

A Seurat object by default for Seurat input, otherwise a `giotto2` workflow object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
g <- structure(
  list(
    source = list(
      cells = colnames(spatial),
      features = rownames(spatial),
      coordinates = data.frame(
        cell_ID = colnames(spatial),
        sdimx = spatial$x,
        sdimy = spatial$y
      )
    ),
    results = list(
      cluster = list(
        table = data.frame(
          cluster = paste0("cluster_", (seq_len(ncol(spatial)) - 1) \%\% 3 + 1),
          row.names = colnames(spatial)
        )
      )
    ),
    active = "cluster"
  ),
  class = c("giotto2", "list")
)
GiottoPlot(g, plot_type = "cluster")

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- RunGiottoWorkflow(
  spatial,
  steps = "basic",
  assay = "Spatial",
  layer = "counts",
  coord.cols = c("x", "y"),
  features = rownames(spatial)[seq_len(min(200L, nrow(spatial)))],
  return_seurat = FALSE,
  verbose = FALSE
)
```
