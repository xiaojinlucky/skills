# Convert Seurat to an internal Giotto workflow object

- Package: scop
- Language: R
- Function: `SeuratToGiotto2`
- Source: https://mengxu98.github.io/scop/reference/SeuratToGiotto2.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SeuratToGiotto2.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Create a `giotto2` object from a Seurat object. The converter is SCT-aware: raw counts remain the default Giotto input, while SCT normalized values are optionally added as an extra Giotto expression layer. The input Seurat object is not modified.

## Signature

```text
SeuratToGiotto2( srt, assay = NULL, layer = "counts", sct.assay = "SCT", use_sct = c("auto", "none", "normalized"), image = NULL, coord.cols = c("x", "y"), features = NULL, conversion_params = list(), use_official = TRUE, verbose = TRUE, seed = 11 )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Assay layer used as the expression matrix.
- `sct.assay`: Name of the SCT assay.
- `use_sct`: How to handle SCT data. `"auto"` keeps counts as the main Giotto expression and records SCT availability. `"none"` ignores SCT. `"normalized"` adds SCT normalized values as an additional expression layer.
- `image`: Name of the Seurat spatial image used by the spatial workflow. Required when multiple images are present; a single image is selected automatically when NULL.
- `coord.cols`: Metadata coordinate columns used by the spatial workflow when no image is available.
- `features`: Features used for PCA and clustering. If NULL, current variable features are used, falling back to all assay features.
- `conversion_params`: Additional parameters passed to Giotto::createGiottoObject().
- `use_official`: Whether to try the official GiottoClass Seurat converter before falling back to the scop-controlled converter.
- `verbose`: Whether to print the message. Default is TRUE.
- `seed`: Random seed for reproducibility. Default is 11.

## Full Documentation

# Convert Seurat to an internal Giotto workflow object

## Usage

```text
SeuratToGiotto2( srt, assay = NULL, layer = "counts", sct.assay = "SCT", use_sct = c("auto", "none", "normalized"), image = NULL, coord.cols = c("x", "y"), features = NULL, conversion_params = list(), use_official = TRUE, verbose = TRUE, seed = 11 )
```

## Description

Create a `giotto2` object from a Seurat object. The converter is SCT-aware: raw counts remain the default Giotto input, while SCT normalized values are optionally added as an extra Giotto expression layer. The input Seurat object is not modified.

## Value

A `giotto2` object.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
g <- structure(
  list(
    giotto = list(
      umap = cbind(
        UMAP_1 = as.numeric(scale(spatial$x)),
        UMAP_2 = as.numeric(scale(spatial$y))
      )
    ),
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
      ),
      spatial_network = list(
        table = data.frame(
          from = colnames(spatial)[1:8],
          to = colnames(spatial)[2:9]
        )
      )
    ),
    active = "cluster"
  ),
  class = c("giotto2", "list")
)

GiottoPlot(g, plot_type = "cluster")
GiottoPlot(g, plot_type = "network")

spatial <- subset(spatial, cells = colnames(spatial)[seq_len(min(200L, ncol(spatial)))])
g <- SeuratToGiotto2(
  spatial,
  assay = "Spatial",
  layer = "counts",
  coord.cols = c("x", "y"),
  verbose = FALSE
)
```
