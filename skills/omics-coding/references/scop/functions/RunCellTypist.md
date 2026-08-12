# Run CellTypist cell type annotation

- Package: scop
- Language: R
- Function: `RunCellTypist`
- Source: https://mengxu98.github.io/scop/reference/RunCellTypist.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunCellTypist.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

CellTypist is an automated cell type annotation tool for scRNA-seq datasets based on logistic regression classifiers. This function runs CellTypist annotation on a Seurat object or AnnData object.

## Signature

```text
RunCellTypist( srt = NULL, adata = NULL, assay = "RNA", layer = "data", model = "Immune_All_Low.pkl", mode = "best match", p_thres = 0.5, majority_voting = FALSE, over_clustering = NULL, min_prop = 0, use_GPU = FALSE, insert_labels = TRUE, insert_conf = TRUE, insert_conf_by = "predicted_labels", insert_prob = FALSE, insert_decision = FALSE, prefix = "celltypist_", return_seurat = !is.null(srt), verbose = TRUE )
```

## Parameters

- `srt`: A Seurat object. Default is NULL. If provided, adata will be ignored.
- `adata`: Optional AnnData object used as input.
- `assay`: Which assay to use. Default is "RNA".
- `layer`: Which layer to use. Default is data.
- `model`: Model name or path. Default is "Immune_All_Low.pkl". Supports three formats: { Model name (e.g., "Immune_All_Low.pkl"): automatically searched in ~/.celltypist/data/models/ Full path (contains /): use the provided path directly NULL: use default model A summary list returned by {[=TrainCellTypist]{TrainCellTypist()}}: use its model_path }
- `mode`: Prediction mode: "best match" or "prob match". Default is "best match".
- `p_thres`: Probability threshold for "prob match" mode. Default is 0.5.
- `majority_voting`: Whether to use majority voting. Default is FALSE.
- `over_clustering`: Over-clustering result. Can be: String: column name in Seurat metadata or AnnData obs Vector: over-clustering labels NULL: use heuristic over-clustering
- `min_prop`: Minimum proportion for majority voting. Default is 0.
- `use_GPU`: Whether to use GPU for over-clustering. Default is FALSE.
- `insert_labels`: Whether to insert predicted labels. Default is TRUE.
- `insert_conf`: Whether to insert confidence scores. Default is TRUE.
- `insert_conf_by`: Which prediction type to base confidence on. Default is "predicted_labels".
- `insert_prob`: Whether to insert probability matrix. Default is FALSE.
- `insert_decision`: Whether to insert decision matrix. Default is FALSE.
- `prefix`: Prefix for inserted columns. Default is "celltypist_".
- `return_seurat`: Whether to return a Seurat object instead of an anndata object. Default is TRUE.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run CellTypist cell type annotation

## Usage

```text
RunCellTypist( srt = NULL, adata = NULL, assay = "RNA", layer = "data", model = "Immune_All_Low.pkl", mode = "best match", p_thres = 0.5, majority_voting = FALSE, over_clustering = NULL, min_prop = 0, use_GPU = FALSE, insert_labels = TRUE, insert_conf = TRUE, insert_conf_by = "predicted_labels", insert_prob = FALSE, insert_decision = FALSE, prefix = "celltypist_", return_seurat = !is.null(srt), verbose = TRUE )
```

## Description

CellTypist is an automated cell type annotation tool for scRNA-seq datasets based on logistic regression classifiers. This function runs CellTypist annotation on a Seurat object or AnnData object.

## Value

An AnnData object or a Seurat object depending on the return_seurat argument.

## Examples

```r
\dontrun{
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunCellTypist(
  pancreas_sub,
  model = "Developing_Mouse_Brain.pkl"
)
CellDimPlot(
  pancreas_sub,
  group.by = "celltypist_predicted_labels",
  legend.position = "none"
)

# Use prob match mode
pancreas_sub <- RunCellTypist(
  pancreas_sub,
  model = "Developing_Mouse_Brain.pkl",
  mode = "prob match",
  p_thres = 0.5
)

# Use majority voting
pancreas_sub <- RunCellTypist(
  pancreas_sub,
  model = "Developing_Mouse_Brain.pkl",
  majority_voting = TRUE
)
}
```
