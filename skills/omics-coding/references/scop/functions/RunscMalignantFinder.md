# Run scMalignantFinder malignant cell identification

- Package: scop
- Language: R
- Function: `RunscMalignantFinder`
- Source: https://mengxu98.github.io/scop/reference/RunscMalignantFinder.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunscMalignantFinder.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run the Python package scMalignantFinder on a Seurat or AnnData object and append malignant-cell predictions to Seurat metadata. The pretrained model files are not bundled with scop; provide a directory containing model.joblib and ordered_feature.tsv through pretrain_dir.

## Signature

```text
RunscMalignantFinder( srt = NULL, adata = NULL, h5ad = NULL, assay = "RNA", layer = "counts", cells = NULL, pretrain_dir = NULL, train_h5ad_path = NULL, feature_path = NULL, model_method = c("LogisticRegression", "RandomForest", "XGBoost"), norm_type = NULL, use_raw = FALSE, n_thread = 1, prefix = "", return_seurat = !is.null(srt), verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object.
- `adata`: Optional Python AnnData object.
- `h5ad`: Optional path to an .h5ad file.
- `assay`: Assay used when srt is supplied. Default is "RNA".
- `layer`: Layer used when srt is supplied. Default is "counts".
- `cells`: Optional cells to run. If supplied with srt, results are appended to these cells and other cells receive NA.
- `pretrain_dir`: Directory containing pretrained scMalignantFinder model files: model.joblib and ordered_feature.tsv.
- `train_h5ad_path`: Optional training .h5ad file used when training a model from scratch.
- `feature_path`: Optional feature file used when training from scratch.
- `model_method`: Model used when training from scratch. One of "LogisticRegression", "RandomForest", or "XGBoost".
- `norm_type`: Passed to scMalignantFinder. Use TRUE for raw counts that should be library-size normalized; use FALSE for already normalized input. If NULL, defaults to TRUE only for Seurat counts input.
- `use_raw`: Whether to use adata.raw.X when available.
- `n_thread`: Number of threads used by scMalignantFinder.
- `prefix`: Optional prefix for output metadata columns. Default preserves the original scMalignantFinder column names.
- `return_seurat`: Whether to return a Seurat object when srt is supplied. If FALSE, returns a data frame of predictions.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run scMalignantFinder malignant cell identification

## Usage

```text
RunscMalignantFinder( srt = NULL, adata = NULL, h5ad = NULL, assay = "RNA", layer = "counts", cells = NULL, pretrain_dir = NULL, train_h5ad_path = NULL, feature_path = NULL, model_method = c("LogisticRegression", "RandomForest", "XGBoost"), norm_type = NULL, use_raw = FALSE, n_thread = 1, prefix = "", return_seurat = !is.null(srt), verbose = TRUE )
```

## Description

Run the Python package scMalignantFinder on a Seurat or AnnData object and append malignant-cell predictions to Seurat metadata. The pretrained model files are not bundled with scop; provide a directory containing model.joblib and ordered_feature.tsv through pretrain_dir.

## Value

A Seurat object with scMalignantFinder_prediction and malignancy_probability added, or a data frame when return_seurat = FALSE.

## Examples

```r
\dontshow{if (FALSE) withAutoprint(\{ # examplesIf}
data(pancreas_sub)
pancreas_sub <- RunscMalignantFinder(
  pancreas_sub,
  assay = "RNA",
  layer = "counts",
  pretrain_dir = "path/to/pretrained_model"
)
CellDimPlot(pancreas_sub, group.by = "malignancy_probability")
\dontshow{\}) # examplesIf}
```
