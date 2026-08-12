# Run FWP feature-weight phenotype scoring

- Package: scop
- Language: R
- Function: `RunFWP`
- Source: https://mengxu98.github.io/scop/reference/RunFWP.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunFWP.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run FWP feature-weight phenotype scoring

## Signature

```text
RunFWP( object, assay = NULL, layer = "data", features = NULL, nfeatures = 2000, phenotype.by = NULL, positive = NULL, weights = NULL, score.name = "FWP_Score", tool_name = "FWP", verbose = TRUE )
```

## Parameters

- `object`: A Seurat object or expression matrix with genes in rows and cells in columns.
- `assay`: Assay used for Seurat input.
- `layer`: Layer used for Seurat input.
- `features`: Features used for scoring. If NULL, the most variable genes are selected.
- `nfeatures`: Number of variable genes selected when features = NULL.
- `phenotype.by`: Metadata column used to train feature weights.
- `positive`: Positive phenotype label. If NULL, the last ordered label is used.
- `weights`: Optional named vector of precomputed feature weights.
- `score.name`: Metadata column for the FWP score.
- `tool_name`: Name used in srt@tools.
- `verbose`: Whether to print progress messages.

## Full Documentation

# Run FWP feature-weight phenotype scoring

## Usage

```text
RunFWP( object, assay = NULL, layer = "data", features = NULL, nfeatures = 2000, phenotype.by = NULL, positive = NULL, weights = NULL, score.name = "FWP_Score", tool_name = "FWP", verbose = TRUE )
```

## Description

Run FWP feature-weight phenotype scoring

## Value

A modified Seurat object or a result bundle for matrix input.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub$IsEndocrine <- pancreas_sub$CellType == "Endocrine"
pancreas_sub <- RunFWP(
  pancreas_sub,
  phenotype.by = "IsEndocrine",
  nfeatures = 300
)
FeatureDimPlot(
  pancreas_sub,
  features = "FWP_Score"
) + CellDimPlot(
  pancreas_sub,
  group.by = "IsEndocrine",
  xlab = "UMAP_1",
  ylab = "UMAP_2"
)
```
