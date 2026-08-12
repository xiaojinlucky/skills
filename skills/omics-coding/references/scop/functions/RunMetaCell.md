# Run metacell partitioning for single-cell data

- Package: scop
- Language: R
- Function: `RunMetaCell`
- Source: https://mengxu98.github.io/scop/reference/RunMetaCell.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunMetaCell.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run metacell partitioning for single-cell data

## Signature

```text
RunMetaCell( srt, method = c("supercell", "seacells", "metacell"), assay = NULL, layer = "counts", gamma = 20, group.by = NULL, envname = NULL, conda = "auto", prefix = "Metacell", tool_name = "Metacell", verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `method`: Metacell construction method. One of "supercell", "seacells", or "metacell".
- `assay`: Assay to use for metacell construction.
- `layer`: Assay layer used to extract the count matrix.
- `gamma`: Metacell granularity parameter. For SuperCell, larger values produce fewer metacells (typical range 10--50). For MetaCell, this is the K parameter controlling the number of metacells. For SEACells, the comparable parameter is passed via ... (e.g. n_metacells).
- `group.by`: Optional metadata column used to build metacells within each group independently (e.g. by sample or cell type), preventing metacells from crossing group boundaries.
- `envname`: Python environment name (SEACells only). Passed to reticulate::use_condaenv() when method = "seacells".
- `conda`: Conda executable path (SEACells only).
- `prefix`: Prefix for metadata columns written to srt.
- `tool_name`: Name of the srt@tools entry.
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional arguments passed to the underlying metacell method.

## Full Documentation

# Run metacell partitioning for single-cell data

## Usage

```text
RunMetaCell( srt, method = c("supercell", "seacells", "metacell"), assay = NULL, layer = "counts", gamma = 20, group.by = NULL, envname = NULL, conda = "auto", prefix = "Metacell", tool_name = "Metacell", verbose = TRUE, ... )
```

## Description

Run metacell partitioning for single-cell data

## Value

A metacell-level Seurat object. The original single-cell Seurat is stored in @misc[["original_srt"]] and the cell-to-metacell membership vector in @misc[["cell_membership"]]. The returned object can be passed directly to any scop function (RunStandardWorkflow(), CellDimPlot(), etc.).

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(
  pancreas_sub,
  nHVF = 500,
  linear_reduction_dims = 20,
  linear_reduction_dims_use = 1:20,
  nonlinear_reduction_dims = 2,
  verbose = FALSE
)

mc1 <- RunMetaCell(
  pancreas_sub,
  method = "supercell",
  gamma = 20
)

MetaCellPlot(mc1, group.by = "CellType")

mc2 <- RunMetaCell(
  pancreas_sub,
  method = "metacell",
  gamma = 20
)

MetaCellPlot(mc2, group.by = "CellType")
```
