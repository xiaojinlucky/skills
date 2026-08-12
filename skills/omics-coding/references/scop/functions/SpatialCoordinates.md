# Read spatial coordinates with an explicit coordinate contract

- Package: scop
- Language: R
- Function: `SpatialCoordinates`
- Source: https://mengxu98.github.io/scop/reference/SpatialCoordinates.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/SpatialCoordinates.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Return raw analysis coordinates or display coordinates together with their source and reversible transform. This function does not modify the object.

## Signature

```text
SpatialCoordinates( object, image = NULL, coord.cols = c("col", "row"), space = c("raw", "display"), image_policy = "strict" )
```

## Parameters

- `object`: A `Seurat` object.
- `image`: Optional Seurat image name.
- `coord.cols`: Metadata columns used when no image is available.
- `space`: Coordinate space to return.
- `image_policy`: Multi-image selection policy. The default requires an explicit image when more than one image is available.

## Full Documentation

# Read spatial coordinates with an explicit coordinate contract

## Usage

```text
SpatialCoordinates( object, image = NULL, coord.cols = c("col", "row"), space = c("raw", "display"), image_policy = "strict" )
```

## Description

Return raw analysis coordinates or display coordinates together with their source and reversible transform. This function does not modify the object.

## Value

A plain list with `data`, `source`, and `transform` entries.
