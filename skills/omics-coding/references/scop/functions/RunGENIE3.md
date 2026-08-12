# Infer gene regulatory networks with GENIE3

- Package: scop
- Language: R
- Function: `RunGENIE3`
- Source: https://mengxu98.github.io/scop/reference/RunGENIE3.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunGENIE3.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run GENIE3 regulatory network inference and return a standardized adjacency table with columns `TF`, `target`, and `importance`.

## Signature

```text
RunGENIE3(object, ...) RunGENIE3{Seurat}( object, assay = NULL, layer = "counts", regulators = NULL, targets = NULL, max_edges_per_target = Inf, output_file = NULL, cores = 1, force = FALSE, verbose = TRUE, ... ) RunGENIE3{matrix}(object, ...) RunGENIE3{default}( object, regulators = NULL, targets = NULL, genes_in = c("rows", "columns"), max_edges_per_target = Inf, output_file = NULL, cores = 1, force = FALSE, verbose = TRUE, ... )
```

## Parameters

- `object`: A Seurat object or expression matrix.
- `...`: Additional backend-specific arguments.
- `assay`: Assay used when `object` is a Seurat object.
- `layer`: Assay layer used when `object` is a Seurat object.
- `regulators`: Candidate transcription factor genes.
- `targets`: Optional target genes. If `NULL`, all genes are considered.
- `max_edges_per_target`: Maximum incoming regulator edges retained per target. The default `Inf` keeps all positive-importance links.
- `output_file`: Optional path where the adjacency table is written.
- `cores`: Number of workers used by GENIE3.
- `force`: Whether to rebuild existing `output_file`.
- `verbose`: Whether to print progress messages.
- `genes_in`: Matrix orientation for matrix inputs. `"rows"` means genes x cells; `"columns"` means cells x genes.

## Full Documentation

# Infer gene regulatory networks with GENIE3

## Usage

```text
RunGENIE3(object, ...) RunGENIE3{Seurat}( object, assay = NULL, layer = "counts", regulators = NULL, targets = NULL, max_edges_per_target = Inf, output_file = NULL, cores = 1, force = FALSE, verbose = TRUE, ... ) RunGENIE3{matrix}(object, ...) RunGENIE3{default}( object, regulators = NULL, targets = NULL, genes_in = c("rows", "columns"), max_edges_per_target = Inf, output_file = NULL, cores = 1, force = FALSE, verbose = TRUE, ... )
```

## Description

Run GENIE3 regulatory network inference and return a standardized adjacency table with columns `TF`, `target`, and `importance`.

## Value

A data frame with columns `TF`, `target`, and `importance`.
