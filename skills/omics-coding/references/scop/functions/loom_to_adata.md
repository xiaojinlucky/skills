# Read a .loom file as an AnnData object

- Package: scop
- Language: R
- Function: `loom_to_adata`
- Source: https://mengxu98.github.io/scop/reference/loom_to_adata.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/loom_to_adata.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a .loom file as an AnnData object

## Signature

```text
loom_to_adata(path, verbose = TRUE, ...)
```

## Parameters

- `path`: Path to a .loom file (passed to scanpy.read_loom()).
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional arguments passed to scanpy.read_loom().

## Full Documentation

# Read a .loom file as an AnnData object

## Usage

```text
loom_to_adata(path, verbose = TRUE, ...)
```

## Description

Read a .loom file as an AnnData object

## Value

A Python anndata.AnnData object.

## Examples

```r
\dontrun{
adata <- loom_to_adata("path/to/data.loom")
adata
}
```
