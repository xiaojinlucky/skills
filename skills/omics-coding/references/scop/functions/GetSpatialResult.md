# Read one stored spatial result

- Package: scop
- Language: R
- Function: `GetSpatialResult`
- Source: https://mengxu98.github.io/scop/reference/GetSpatialResult.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetSpatialResult.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Return a schema-v1 read-only view of a registered spatial result. Legacy results are normalized in the returned copy and are never written back.

## Signature

```text
GetSpatialResult( object, method = NULL, tool_name = NULL, raw = FALSE, validate = TRUE )
```

## Parameters

- `object`: A `Seurat` object.
- `method`: Optional public producer or result family.
- `tool_name`: Optional exact key in `object@tools`.
- `raw`: Whether to return the stored value without normalization.
- `validate`: Whether to validate schema-v1 results before returning.

## Full Documentation

# Read one stored spatial result

## Usage

```text
GetSpatialResult( object, method = NULL, tool_name = NULL, raw = FALSE, validate = TRUE )
```

## Description

Return a schema-v1 read-only view of a registered spatial result. Legacy results are normalized in the returned copy and are never written back.

## Value

A plain spatial result list.
