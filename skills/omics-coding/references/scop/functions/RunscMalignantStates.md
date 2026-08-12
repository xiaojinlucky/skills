# Run scMalignantFinder cancer cell state scoring

- Package: scop
- Language: R
- Function: `RunscMalignantStates`
- Source: https://mengxu98.github.io/scop/reference/RunscMalignantStates.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunscMalignantStates.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Score cancer cell state gene sets with scMalignantFinder AUCell utilities and append the resulting activity scores to Seurat metadata.

## Signature

```text
RunscMalignantStates( srt = NULL, adata = NULL, h5ad = NULL, assay = "RNA", layer = "counts", cells = NULL, gene_sets, norm_type = NULL, prefix = "scMalignantState_", return_seurat = !is.null(srt), verbose = TRUE, backend = c("cpp", "python") )
```

## Parameters

- `srt`: A Seurat object.
- `adata`: Optional Python AnnData object.
- `h5ad`: Optional path to an .h5ad file.
- `assay`: Assay used when srt is supplied. Default is "RNA".
- `layer`: Layer used when srt is supplied. Default is "counts".
- `cells`: Optional cells to run. If supplied with srt, results are appended to these cells and other cells receive NA.
- `gene_sets`: Path to a .gmt file containing cancer cell state gene sets, such as Malignant_MPs.Gavish_2023.gmt from the scMalignantFinder resources.
- `norm_type`: Passed to scMalignantFinder. Use TRUE for raw counts that should be library-size normalized; use FALSE for already normalized input. If NULL, defaults to TRUE only for Seurat counts input.
- `prefix`: Optional prefix for output metadata columns. Default preserves the original scMalignantFinder column names.
- `return_seurat`: Whether to return a Seurat object when srt is supplied. If FALSE, returns a data frame of predictions.
- `verbose`: Whether to print the message. Default is TRUE.
- `backend`: State-scoring backend. "cpp" uses a compiled sparse AUCell implementation for Seurat input. "python" retains the official scMalignantFinder path and is used for AnnData or h5ad input.

## Full Documentation

# Run scMalignantFinder cancer cell state scoring

## Usage

```text
RunscMalignantStates( srt = NULL, adata = NULL, h5ad = NULL, assay = "RNA", layer = "counts", cells = NULL, gene_sets, norm_type = NULL, prefix = "scMalignantState_", return_seurat = !is.null(srt), verbose = TRUE, backend = c("cpp", "python") )
```

## Description

Score cancer cell state gene sets with scMalignantFinder AUCell utilities and append the resulting activity scores to Seurat metadata.

## Value

A Seurat object with cancer-state AUCell scores, or a data frame when return_seurat = FALSE.

## Examples

```r
\dontshow{if (FALSE) withAutoprint(\{ # examplesIf}
srt <- RunscMalignantStates(
  srt,
  gene_sets = "path/to/Malignant_MPs.Gavish_2023.gmt"
)
\dontshow{\}) # examplesIf}
```
