# Append a Seurat object to another

- Package: scop
- Language: R
- Function: `srt_append`
- Source: https://mengxu98.github.io/scop/reference/srt_append.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_append.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Append a Seurat object to another

## Signature

```text
srt_append( srt_raw, srt_append, slots = methods::slotNames(srt_append), pattern = NULL, overwrite = FALSE, verbose = TRUE )
```

## Parameters

- `srt_raw`: A Seurat object to be appended.
- `srt_append`: New Seurat object to append.
- `slots`: slots names.
- `pattern`: A character string containing a regular expression. All data with matching names will be considered for appending.
- `overwrite`: Whether to overwrite.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Append a Seurat object to another

## Usage

```text
srt_append( srt_raw, srt_append, slots = methods::slotNames(srt_append), pattern = NULL, overwrite = FALSE, verbose = TRUE )
```

## Description

Append a Seurat object to another
