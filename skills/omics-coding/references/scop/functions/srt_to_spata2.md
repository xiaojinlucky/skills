# Convert Seurat to a native SPATA2 object

- Package: scop
- Language: R
- Function: `srt_to_spata2`
- Source: https://mengxu98.github.io/scop/reference/srt_to_spata2.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/srt_to_spata2.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Convert one Seurat spatial image into a native SPATA2 object without running SPATA2 analyses or changing the input object.

## Signature

```text
srt_to_spata2(srt, image = NULL, ...)
```

## Parameters

- `srt`: A `Seurat` object.
- `image`: Seurat image name. Multi-image objects require an explicit name.
- `...`: Additional arguments passed to `SPATA2::asSPATA2()`.

## Full Documentation

# Convert Seurat to a native SPATA2 object

## Usage

```text
srt_to_spata2(srt, image = NULL, ...)
```

## Description

Convert one Seurat spatial image into a native SPATA2 object without running SPATA2 analyses or changing the input object.

## Value

A native SPATA2 object.
