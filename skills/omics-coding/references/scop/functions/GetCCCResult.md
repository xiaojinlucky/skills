# Get a standardized or native CCC result

- Package: scop
- Language: R
- Function: `GetCCCResult`
- Source: https://mengxu98.github.io/scop/reference/GetCCCResult.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetCCCResult.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Get a standardized or native CCC result

## Signature

```text
GetCCCResult( srt, method, type = c("primary", "long", "pair", "consensus", "raw", "native"), resource = NULL, condition = NULL, sample = NULL )
```

## Parameters

- `srt`: A Seurat object.
- `method`: A registered CCC method.
- `type`: Result representation.
- `resource`: Optional LIANA resource when retrieving a consensus.
- `condition`: Stored CellChat or SpatialCellChat result name when retrieving a native object.
- `sample`: Stored SpatialCellChat sample when retrieving a native object.

## Full Documentation

# Get a standardized or native CCC result

## Usage

```text
GetCCCResult( srt, method, type = c("primary", "long", "pair", "consensus", "raw", "native"), resource = NULL, condition = NULL, sample = NULL )
```

## Description

Get a standardized or native CCC result

## Value

The requested stored result.
