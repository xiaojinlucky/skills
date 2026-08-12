# Get an upstream CellChat-family object

- Package: scop
- Language: R
- Function: `GetCCCObject`
- Source: https://mengxu98.github.io/scop/reference/GetCCCObject.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetCCCObject.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Get an upstream CellChat-family object

## Signature

```text
GetCCCObject( object, method = c("CellChat", "SpatialCellChat"), result.name = NULL, sample = NULL )
```

## Parameters

- `object`: A `Seurat` object.
- `method`: Either `"CellChat"` or `"SpatialCellChat"`.
- `result.name`: A CellChat condition or SpatialCellChat named result.
- `sample`: Spatial sample for SpatialCellChat results.

## Full Documentation

# Get an upstream CellChat-family object

## Usage

```text
GetCCCObject( object, method = c("CellChat", "SpatialCellChat"), result.name = NULL, sample = NULL )
```

## Description

Get an upstream CellChat-family object

## Value

An upstream backend object.
