# Infer gene regulatory networks with GNIPLR

- Package: scop
- Language: R
- Function: `RunGNIPLR`
- Source: https://mengxu98.github.io/scop/reference/RunGNIPLR.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunGNIPLR.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Infer gene regulatory networks with GNIPLR

## Signature

```text
RunGNIPLR(object, ...) RunGNIPLR{Seurat}( object, assay = NULL, layer = "counts", targets = NULL, correlation_threshold = 0.3, lasso_degree = 30, lasso_alpha = 0.1, max_lag = 3, backend = c("cpp", "python"), max_edges_per_target = Inf, output_file = NULL, work_dir = tempdir(), prefix = "gniplr", envname = "scop_env", conda = "auto", force = FALSE, verbose = TRUE, ... ) RunGNIPLR{matrix}(object, ...) RunGNIPLR{default}( object, targets = NULL, genes_in = c("rows", "columns"), correlation_threshold = 0.3, lasso_degree = 30, lasso_alpha = 0.1, max_lag = 3, backend = c("cpp", "python"), max_edges_per_target = Inf, output_file = NULL, work_dir = tempdir(), prefix = "gniplr", envname = "scop_env", conda = "auto", force = FALSE, verbose = TRUE, ... )
```

## Parameters

- `object`: A Seurat object or expression matrix.
- `...`: Additional backend-specific arguments.
- `assay`: Assay used when `object` is a Seurat object.
- `layer`: Assay layer used when `object` is a Seurat object.
- `targets`: Optional target genes. If `NULL`, all genes are considered.
- `correlation_threshold`: Relative correlation filter used before lagged regression. A gene pair is tested when its absolute correlation is at least this fraction of the maximum absolute correlation for the regulator.
- `lasso_degree`: Polynomial degree used by the LASSO projection step.
- `lasso_alpha`: LASSO regularization strength used by the projection step.
- `max_lag`: Maximum lag used by Granger-style lagged regression. Values above `3` are capped at `3` to match the GNIPLR reference implementation.
- `backend`: Runtime backend. Supports `"cpp"` and `"python"`.
- `max_edges_per_target`: Maximum incoming regulator edges retained per target. The default `Inf` keeps all positive-importance links.
- `output_file`: Optional path where the adjacency table is written.
- `work_dir`: Working directory used by the Python backend.
- `prefix`: Prefix for temporary files.
- `envname`: Python environment used by the Python backend.
- `conda`: Conda-compatible executable used by the Python backend.
- `force`: Whether to rebuild existing `output_file`.
- `verbose`: Whether to print progress messages.
- `genes_in`: Matrix orientation for matrix inputs. `"rows"` means genes x cells; `"columns"` means cells x genes.

## Full Documentation

# Infer gene regulatory networks with GNIPLR

## Usage

```text
RunGNIPLR(object, ...) RunGNIPLR{Seurat}( object, assay = NULL, layer = "counts", targets = NULL, correlation_threshold = 0.3, lasso_degree = 30, lasso_alpha = 0.1, max_lag = 3, backend = c("cpp", "python"), max_edges_per_target = Inf, output_file = NULL, work_dir = tempdir(), prefix = "gniplr", envname = "scop_env", conda = "auto", force = FALSE, verbose = TRUE, ... ) RunGNIPLR{matrix}(object, ...) RunGNIPLR{default}( object, targets = NULL, genes_in = c("rows", "columns"), correlation_threshold = 0.3, lasso_degree = 30, lasso_alpha = 0.1, max_lag = 3, backend = c("cpp", "python"), max_edges_per_target = Inf, output_file = NULL, work_dir = tempdir(), prefix = "gniplr", envname = "scop_env", conda = "auto", force = FALSE, verbose = TRUE, ... )
```

## Description

Infer gene regulatory networks with GNIPLR

## Value

A data frame with columns `TF`, `target`, `importance`, and `pvalue`. The original GNIPLR p-value matrix is stored in `attr(result, "grn_matrix")` when the network is newly inferred.

## Examples

```r
data(pancreas_sub)
expr <- GetAssayData5(
  pancreas_sub,
  assay = SeuratObject::DefaultAssay(pancreas_sub),
  layer = "counts"
)
expr <- as.matrix(expr[, seq_len(8)])
expr <- expr[
  names(sort(apply(expr, 1, stats::var), decreasing = TRUE))[seq_len(5)],
]

grn <- RunGNIPLR(
  expr,
  genes_in = "rows",
  correlation_threshold = 0,
  lasso_degree = 1,
  max_lag = 1,
  max_edges_per_target = 2
)
head(grn)
attr(grn, "grn_matrix")[1:3, 1:3]
```
