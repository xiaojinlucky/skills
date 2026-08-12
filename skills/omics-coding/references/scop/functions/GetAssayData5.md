# Get expression data from Assay5 or Seurat object

- Package: scop
- Language: R
- Function: `GetAssayData5`
- Source: https://mengxu98.github.io/scop/reference/GetAssayData5.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetAssayData5.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

A re-implementation of the [SeuratObject:GetAssayData]{SeuratObject::GetAssayData} function to compatible with Assay5 objects.

## Signature

```text
GetAssayData5(object, ...) GetAssayData5{Seurat}(object, layer = "counts", assay = NULL, ...) GetAssayData5{Assay5}(object, layer = "counts", ...) GetAssayData5{Assay}(object, layer = "counts", ...)
```

## Parameters

- `object`: An object
- `...`: Additional arguments passed to [SeuratObject:GetAssayData]{SeuratObject::GetAssayData}.
- `layer`: Name of layer to get or set
- `assay`: Specific assay to get data from or set data for; defaults to the [SeuratObject:DefaultAssay]{default assay}

## Full Documentation

# Get expression data from Assay5 or Seurat object

## Usage

```text
GetAssayData5(object, ...) GetAssayData5{Seurat}(object, layer = "counts", assay = NULL, ...) GetAssayData5{Assay5}(object, layer = "counts", ...) GetAssayData5{Assay}(object, layer = "counts", ...)
```

## Description

A re-implementation of the [SeuratObject:GetAssayData]{SeuratObject::GetAssayData} function to compatible with Assay5 objects.

## Value

A matrix or data frame containing the assay data.

## Examples

```r
data(pancreas_sub)
GetAssayData5(
  pancreas_sub,
  layer = "counts",
  assay = "RNA"
)[1:5, 1:5]

data(panc8_sub)
GetAssayData5(
  panc8_sub,
  layer = "counts",
  assay = "RNA"
)[1:5, 1:5]
```
