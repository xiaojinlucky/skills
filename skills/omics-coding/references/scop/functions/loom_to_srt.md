# Read a .loom file and convert to a Seurat

- Package: scop
- Language: R
- Function: `loom_to_srt`
- Source: https://mengxu98.github.io/scop/reference/loom_to_srt.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/loom_to_srt.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a .loom file and convert to a Seurat

## Signature

```text
loom_to_srt( path, layers = c("spliced", "unspliced"), verbose = TRUE, chunk_rows = 1000 )
```

## Parameters

- `path`: Path to a .loom file.
- `layers`: Character vector of loom layers to import as additional Seurat assays. Missing layers are skipped with a warning. Default is c("spliced", "unspliced").
- `verbose`: Whether to print the message. Default is TRUE.
- `chunk_rows`: Number of feature rows to read from each matrix dataset per chunk. Larger values can be faster but use more memory.

## Full Documentation

# Read a .loom file and convert to a Seurat

## Usage

```text
loom_to_srt( path, layers = c("spliced", "unspliced"), verbose = TRUE, chunk_rows = 1000 )
```

## Description

Read a .loom file and convert to a Seurat

## Value

A Seurat object.

## Examples

```r
\dontrun{
srt <- loom_to_srt("path/to/data.loom")
srt
}
```
