# Run scTenifoldKnk in-silico knockout analysis

- Package: scop
- Language: R
- Function: `RunScTenifoldKnk`
- Source: https://mengxu98.github.io/scop/reference/RunScTenifoldKnk.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunScTenifoldKnk.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run scTenifoldKnk in-silico knockout analysis

## Signature

```text
RunscTenifoldKnk( srt, gKO, assay = NULL, layer = "counts", features = NULL, qc = TRUE, qc_mt_threshold = 0.1, qc_min_library_size = 1000, qc_min_cells = 25, nc_lambda = 0, nc_nNet = 10, nc_nCells = 500, nc_nComp = 3, nc_scaleScores = TRUE, nc_symmetric = FALSE, nc_q = 0.9, td_K = 3, td_maxIter = 1000, td_maxError = 1e-05, td_nDecimal = 3, ma_nDim = 2, cores = 1, backend = c("r", "cpp"), store_networks = TRUE, store_manifold = TRUE, tool_name = "scTenifoldKnk", verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `gKO`: Gene symbol or symbols to knock out. All genes must be present after optional feature and QC filtering.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Assay layer used as the count matrix.
- `features`: Optional genes to retain before running network construction. If supplied, gKO is always retained when present in the input assay.
- `qc`: Whether to apply scTenifoldKnk-style quality control.
- `qc_mt_threshold`: Maximum mitochondrial read fraction per cell.
- `qc_min_library_size`: Minimum library size per cell.
- `qc_min_cells`: Minimum number of expressing cells required per gene.
- `nc_lambda, nc_nNet, nc_nCells, nc_nComp, nc_scaleScores, nc_symmetric, nc_q`: Network construction parameters forwarded to scTenifoldNet::makeNetworks().
- `td_K, td_maxIter, td_maxError, td_nDecimal`: Tensor decomposition parameters forwarded to scTenifoldNet::tensorDecomposition().
- `ma_nDim`: Manifold-alignment dimension forwarded to scTenifoldNet::manifoldAlignment().
- `cores`: Number of cores used by native network-construction workers and forwarded to downstream linear algebra where applicable.
- `backend`: r calls scTenifoldKnk::scTenifoldKnk() directly and is the default high-consistency path. cpp follows the upstream scTenifoldNet/scTenifoldKnk network construction, tensor decomposition, manifold alignment, and differential-regulation steps while keeping input handling and result storage inside scop.
- `store_networks`: Whether to keep WT/KO tensor networks in srt@tools.
- `store_manifold`: Whether to keep manifold-alignment coordinates in srt@tools.
- `tool_name`: Name of the srt@tools entry.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run scTenifoldKnk in-silico knockout analysis

## Usage

```text
RunscTenifoldKnk( srt, gKO, assay = NULL, layer = "counts", features = NULL, qc = TRUE, qc_mt_threshold = 0.1, qc_min_library_size = 1000, qc_min_cells = 25, nc_lambda = 0, nc_nNet = 10, nc_nCells = 500, nc_nComp = 3, nc_scaleScores = TRUE, nc_symmetric = FALSE, nc_q = 0.9, td_K = 3, td_maxIter = 1000, td_maxError = 1e-05, td_nDecimal = 3, ma_nDim = 2, cores = 1, backend = c("r", "cpp"), store_networks = TRUE, store_manifold = TRUE, tool_name = "scTenifoldKnk", verbose = TRUE )
```

## Description

Run scTenifoldKnk in-silico knockout analysis

## Value

A Seurat object with scTenifoldKnk results stored in srt@tools[[tool_name]].

## Examples

```r
data(pancreas_sub)
gene_use <- "Pdx1"
counts <- GetAssayData5(
  pancreas_sub,
  assay = "RNA",
  layer = "counts"
)
detected <- names(
  sort(Matrix::rowSums(counts > 0),
    decreasing = TRUE
  )
)
features_use <- unique(c(gene_use, head(detected, 300)))

pancreas_sub <- RunscTenifoldKnk(
  pancreas_sub,
  gKO = gene_use,
  features = features_use,
  qc = FALSE,
  nc_nNet = 3,
  nc_nCells = 200,
  td_maxIter = 200,
  store_networks = FALSE,
  store_manifold = TRUE
)

dr <- pancreas_sub@tools$scTenifoldKnk$diffRegulation
head(dr)

scTenifoldKnkPlot(pancreas_sub, plot_type = "effect")
```
