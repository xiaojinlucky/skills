# Read an .h5ad file and convert to a Seurat

- Package: scop
- Language: R
- Function: `h5ad_to_srt`
- Source: https://mengxu98.github.io/scop/reference/h5ad_to_srt.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/h5ad_to_srt.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read an .h5ad file and convert to a Seurat

## Signature

```text
h5ad_to_srt(path, verbose = TRUE, prepare_for_reticulate = TRUE)
```

## Parameters

- `path`: Path to an .h5ad file (passed to anndata.read_h5ad()).
- `verbose`: Whether to print the message. Default is TRUE.
- `prepare_for_reticulate`: If TRUE (default), coerces X and each layer matrix to CSR float64 in Python (avoids invalid dgRMatrix conversion via reticulate). Layers that still fail in {[=adata_to_srt]{adata_to_srt()}} are skipped and reported. Set to FALSE for a plain read_h5ad then convert.

## Full Documentation

# Read an .h5ad file and convert to a Seurat

## Usage

```text
h5ad_to_srt(path, verbose = TRUE, prepare_for_reticulate = TRUE)
```

## Description

Read an .h5ad file and convert to a Seurat

## Value

A Seurat object.

## Examples

```r
\dontrun{
srt <- h5ad_to_srt("path/to/data.h5ad")
srt
}
```
