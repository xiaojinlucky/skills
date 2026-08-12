# Inspect stored spatial results

- Package: scop
- Language: R
- Function: `SpatialResultInfo`
- Source: https://mengxu98.github.io/scop/reference/SpatialResultInfo.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SpatialResultInfo.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read spatial result bundles from a Seurat object's `tools` slot without migrating, renaming, or modifying legacy results.

## Signature

```text
SpatialResultInfo( object, method = NULL, tool_name = NULL, include_empty = FALSE, detail = c("results", "graphs") )
```

## Parameters

- `object`: A `Seurat` object.
- `method`: Optional registered producer or result-family filter.
- `tool_name`: Optional stored tool key filter.
- `include_empty`: Whether to include recognized keys without a logical result payload.
- `detail`: Return one row per result or one row per stored spatial graph.

## Full Documentation

# Inspect stored spatial results

## Usage

```text
SpatialResultInfo( object, method = NULL, tool_name = NULL, include_empty = FALSE, detail = c("results", "graphs") )
```

## Description

Read spatial result bundles from a Seurat object's `tools` slot without migrating, renaming, or modifying legacy results.

## Value

A data frame describing recognized stored spatial results or graphs.
