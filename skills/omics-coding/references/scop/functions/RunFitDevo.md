# Run FitDevo developmental potential scoring

- Package: scop
- Language: R
- Function: `RunFitDevo`
- Source: https://mengxu98.github.io/scop/reference/RunFitDevo.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunFitDevo.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run FitDevo developmental potential scoring

## Signature

```text
RunFitDevo( object, assay = NULL, layer = "data", features = NULL, nfeatures = 2000, reference.by = NULL, score.name = "FitDevo_Score", relative.name = "FitDevo_Relative", tool_name = "FitDevo", verbose = TRUE, backend = c("cpp", "r") )
```

## Parameters

- `object`: A Seurat object or expression matrix with genes in rows and cells in columns.
- `assay`: Assay used for Seurat input.
- `layer`: Layer used for Seurat input.
- `features`: Features used for scoring. If NULL, the most variable genes are selected.
- `nfeatures`: Number of variable genes selected when features = NULL.
- `reference.by`: Optional metadata column containing ordered development labels. Numeric values are used directly; factors use their level order.
- `score.name`: Metadata column for the developmental potential score.
- `relative.name`: Metadata column for the relative rank.
- `tool_name`: Name used in srt@tools.
- `verbose`: Whether to print progress messages.
- `backend`: Computation backend. "cpp" avoids materializing the full feature-by-cell rank matrix for supervised scoring; "r" retains the reference implementation.

## Full Documentation

# Run FitDevo developmental potential scoring

## Usage

```text
RunFitDevo( object, assay = NULL, layer = "data", features = NULL, nfeatures = 2000, reference.by = NULL, score.name = "FitDevo_Score", relative.name = "FitDevo_Relative", tool_name = "FitDevo", verbose = TRUE, backend = c("cpp", "r") )
```

## Description

Run FitDevo developmental potential scoring

## Value

A modified Seurat object or a result bundle for matrix input.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunFitDevo(
  pancreas_sub,
  nfeatures = 300
)
FeatureDimPlot(pancreas_sub, features = "FitDevo_Score")
FitDevoPlot(
  pancreas_sub,
  group.by = "SubCellType",
  xlab = "UMAP_1",
  ylab = "UMAP_2"
)
```
