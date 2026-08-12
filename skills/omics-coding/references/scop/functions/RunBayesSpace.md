# Run BayesSpace spatial clustering

- Package: scop
- Language: R
- Function: `RunBayesSpace`
- Source: https://mengxu98.github.io/scop/reference/RunBayesSpace.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunBayesSpace.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run BayesSpace spatial clustering

## Signature

```text
RunBayesSpace( srt, q, assay = NULL, platform = c("Visium", "VisiumHD", "ST"), image = NULL, use_reduction = NULL, dims = 1:15, preprocess = TRUE, n.PCs = 15, n.HVGs = 2000, skip.PCA = !is.null(use_reduction), spatial_preprocess_params = list(), spatial_cluster_params = list(), cluster_colname = "BayesSpace_cluster", init_colname = "BayesSpace_init", store_sce = TRUE, verbose = TRUE, coord.cols = c("col", "row") )
```

## Parameters

- `srt`: A Seurat object.
- `q`: Number of BayesSpace clusters.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `platform`: Spatial sequencing platform.
- `image`: Name of the Seurat spatial image used to recover spot coordinates when they are not already present in metadata. For regular Visium data with only pixel x/y coordinates, BayesSpace array coordinates are inferred from the spatial grid.
- `use_reduction`: Optional Seurat reduction to pass to BayesSpace as PCA.
- `dims`: Dimensions from use_reduction to use.
- `preprocess`: Whether to run BayesSpace::spatialPreprocess().
- `n.PCs, n.HVGs`: Parameters passed to spatialPreprocess().
- `skip.PCA`: Whether to skip PCA inside spatialPreprocess().
- `spatial_preprocess_params`: Additional parameters passed to BayesSpace::spatialPreprocess().
- `spatial_cluster_params`: Additional parameters passed to BayesSpace::spatialCluster().
- `cluster_colname`: Metadata column used for BayesSpace clusters.
- `init_colname`: Metadata column used for BayesSpace initial clusters.
- `store_sce`: Whether to store the BayesSpace SingleCellExperiment in srt@tools.
- `verbose`: Whether to print the message. Default is TRUE.
- `coord.cols`: Two metadata columns containing raw x/y coordinates when no spatial image is available.

## Full Documentation

# Run BayesSpace spatial clustering

## Usage

```text
RunBayesSpace( srt, q, assay = NULL, platform = c("Visium", "VisiumHD", "ST"), image = NULL, use_reduction = NULL, dims = 1:15, preprocess = TRUE, n.PCs = 15, n.HVGs = 2000, skip.PCA = !is.null(use_reduction), spatial_preprocess_params = list(), spatial_cluster_params = list(), cluster_colname = "BayesSpace_cluster", init_colname = "BayesSpace_init", store_sce = TRUE, verbose = TRUE, coord.cols = c("col", "row") )
```

## Description

Run BayesSpace spatial clustering

## Value

A Seurat object with BayesSpace clusters in metadata and raw results in srt@tools[["BayesSpace"]].

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub
spatial$BayesSpace_cluster <- factor(
  paste0("domain_", (seq_len(ncol(spatial)) - 1) \%\% 3 + 1)
)

SpatialSpotPlot(
  spatial,
  group.by = "BayesSpace_cluster",
  overlay_image = FALSE,
  coord.cols = c("x", "y")
)

spatial <- RunBayesSpace(
  spatial,
  q = 3,
  n.PCs = 5,
  n.HVGs = 200,
  store_sce = FALSE,
  spatial_cluster_params = list(
    nrep = 200,
    burn.in = 50,
    thin = 10,
    save.chain = FALSE
  )
)
table(spatial$BayesSpace_cluster)
```
