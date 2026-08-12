# Convert Seurat to a native Giotto object

- Package: scop
- Language: R
- Function: `srt_to_giotto`
- Source: https://mengxu98.github.io/scop/reference/srt_to_giotto.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_to_giotto.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert one Seurat spatial image into a native Giotto object without running a Giotto workflow or changing the input object.

## Signature

```text
srt_to_giotto(srt, image = NULL, ...)
```

## Parameters

- `srt`: A `Seurat` object.
- `image`: Seurat image name. Multi-image objects require an explicit name.
- `...`: Additional arguments passed to [SeuratToGiotto2()].

## Full Documentation

# Convert Seurat to a native Giotto object

## Usage

```text
srt_to_giotto(srt, image = NULL, ...)
```

## Description

Convert one Seurat spatial image into a native Giotto object without running a Giotto workflow or changing the input object.

## Value

A native Giotto object.
