# Run CytoTRACE 2

- Package: scop
- Language: R
- Function: `RunCytoTRACE`
- Source: https://mengxu98.github.io/scop/reference/RunCytoTRACE.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunCytoTRACE.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Predicts cellular developmental potential from single-cell RNA-seq data using the CytoTRACE 2 algorithm (Kang et al., 2025). By default, this function uses the official CytoTRACE2 R package. Set backend = "cpp" to use the package R/C++ implementation. The algorithm consists of five stages: Preprocessing: Gene orthology mapping, feature selection, ranking, and log2-CPM transformation. GSBN Ensemble Prediction: 19 pre-trained Gene Set Binary Network models predict a continuous developmental potency score (0-1) and a discrete potency category. Diffusion Smoothing: A Markov random-walk-with-restart on a cell-cell similarity graph smooths the raw scores. Binning: Within each potency category, cells are ranked and linearly scaled to corresponding segments of the unit interval. Adaptive kNN Smoothing: PCA-based nearest-neighbor consensus refinement of the final scores.

## Signature

```text
RunCytoTRACE(object, ...) RunCytoTRACE{Seurat}( object, assay = NULL, layer = c("counts", "data"), species = c("Homo_sapiens", "Mus_musculus"), batch_size = 10000, smooth_batch_size = 1000, compute_knn_smoothing = TRUE, cores = 1, backend = c("r", "cpp"), seed = 14, data_dir = NULL, verbose = TRUE, ... ) RunCytoTRACE{default}( object, species = c("Homo_sapiens", "Mus_musculus"), batch_size = 10000, smooth_batch_size = 1000, compute_knn_smoothing = TRUE, cores = 1, backend = c("r", "cpp"), seed = 14, data_dir = NULL, verbose = TRUE, ... )
```

## Parameters

- `object`: An object. This can be a Seurat object or a matrix-like object (genes as rows, cells as columns).
- `...`: Additional arguments passed to the official CytoTRACE2::cytotrace2() call when backend = "r".
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `layer`: Which layer to use. Default is "counts".
- `species`: The species of the input data. Currently supported values are "Homo_sapiens" and "Mus_musculus". Default is "Homo_sapiens".
- `batch_size`: The number of cells to process at once. For datasets with more cells than this value, cells are randomly split into batches and processed independently. No batching if NULL. Default is 10000.
- `smooth_batch_size`: The number of cells per subsample for the diffusion smoothing step. No diffusion subsampling if NULL. Default is 1000.
- `compute_knn_smoothing`: Whether to run the final PCA-based adaptive kNN smoothing step. Set to FALSE for a faster score using the pre-kNN binned CytoTRACE2 output.
- `cores`: Number of cores for parallel processing. Default is 1.
- `backend`: Backend used to run CytoTRACE2. "r" calls the official CytoTRACE2::cytotrace2() implementation and is the default. "cpp" uses the package R/C++ implementation.
- `seed`: Random seed for reproducibility. Default is 14.
- `data_dir`: Path to the directory containing CytoTRACE2 model data files. Used only by backend = "cpp". If NULL, uses model data prepared by PrepareDB(db = "CytoTRACE2"). Default is NULL.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run CytoTRACE 2

## Usage

```text
RunCytoTRACE(object, ...) RunCytoTRACE{Seurat}( object, assay = NULL, layer = c("counts", "data"), species = c("Homo_sapiens", "Mus_musculus"), batch_size = 10000, smooth_batch_size = 1000, compute_knn_smoothing = TRUE, cores = 1, backend = c("r", "cpp"), seed = 14, data_dir = NULL, verbose = TRUE, ... ) RunCytoTRACE{default}( object, species = c("Homo_sapiens", "Mus_musculus"), batch_size = 10000, smooth_batch_size = 1000, compute_knn_smoothing = TRUE, cores = 1, backend = c("r", "cpp"), seed = 14, data_dir = NULL, verbose = TRUE, ... )
```

## Description

Predicts cellular developmental potential from single-cell RNA-seq data using the CytoTRACE 2 algorithm (Kang et al., 2025). By default, this function uses the official CytoTRACE2 R package. Set backend = "cpp" to use the package R/C++ implementation. The algorithm consists of five stages: Preprocessing: Gene orthology mapping, feature selection, ranking, and log2-CPM transformation. GSBN Ensemble Prediction: 19 pre-trained Gene Set Binary Network models predict a continuous developmental potency score (0-1) and a discrete potency category. Diffusion Smoothing: A Markov random-walk-with-restart on a cell-cell similarity graph smooths the raw scores. Binning: Within each potency category, cells are ranked and linearly scaled to corresponding segments of the unit interval. Adaptive kNN Smoothing: PCA-based nearest-neighbor consensus refinement of the final scores.

## Value

When the input is a Seurat object, the function returns a Seurat object with the following metadata columns added: CytoTRACE2_Score: The final predicted cellular potency score (0-1) CytoTRACE2_Potency: The final predicted cellular potency category (Differentiated, Unipotent, Oligopotent, Multipotent, Pluripotent, Totipotent) CytoTRACE2_Relative: The predicted relative order (normalized to 0-1) preKNN_CytoTRACE2_Score: The potency score before KNN smoothing preKNN_CytoTRACE2_Potency: The potency category before KNN smoothing When the input is a matrix or data.frame, the function returns a data.frame with the same columns as above, with cell IDs as row names.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunCytoTRACE(
  pancreas_sub,
  species = "Mus_musculus",
  backend = "cpp"
)

CytoTRACEPlot(
  pancreas_sub,
  xlab = "UMAP_1",
  ylab = "UMAP_2",
  ncol = 2
)
```
