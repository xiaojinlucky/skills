# Read or convert a stored spatial graph

- Package: scop
- Language: R
- Function: `GetSpatialGraph`
- Source: https://mengxu98.github.io/scop/reference/GetSpatialGraph.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetSpatialGraph.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a graph from a `SpatialNetwork` result without modifying the Seurat object. Graphs can be returned as their complete list representation, a sparse matrix, or a Seurat `Graph` object.

## Signature

```text
GetSpatialGraph( object = NULL, res = NULL, graph.name = NULL, format = c("list", "sparse", "seurat"), value = c("weight", "distance") )
```

## Parameters

- `object`: Optional `Seurat` object containing `SpatialNetwork` results.
- `res`: Optional `SpatialNetwork` result list.
- `graph.name`: Stored graph name. The active graph is used when `NULL`.
- `format`: Output representation.
- `value`: Edge value used for matrix conversions.

## Full Documentation

# Read or convert a stored spatial graph

## Usage

```text
GetSpatialGraph( object = NULL, res = NULL, graph.name = NULL, format = c("list", "sparse", "seurat"), value = c("weight", "distance") )
```

## Description

Read a graph from a `SpatialNetwork` result without modifying the Seurat object. Graphs can be returned as their complete list representation, a sparse matrix, or a Seurat `Graph` object.

## Value

A graph list, `dgCMatrix`, or Seurat `Graph` object.
