# Add features data

- Package: scop
- Language: R
- Function: `AddFeaturesData`
- Source: https://mengxu98.github.io/scop/reference/AddFeaturesData.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/AddFeaturesData.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add features data to the Assay, Assay5 or Seurat object.

## Signature

```text
AddFeaturesData(object, ...) AddFeaturesData{Seurat}(object, features, assay = NULL, ...) AddFeaturesData{Assay}(object, features, ...) AddFeaturesData{Assay5}(object, features, ...)
```

## Parameters

- `object`: A Assay, Assay5 or Seurat object.
- `...`: Additional arguments passed to the method.
- `features`: Features data to add.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.

## Full Documentation

# Add features data

## Usage

```text
AddFeaturesData(object, ...) AddFeaturesData{Seurat}(object, features, assay = NULL, ...) AddFeaturesData{Assay}(object, features, ...) AddFeaturesData{Assay5}(object, features, ...)
```

## Description

Add features data to the Assay, Assay5 or Seurat object.

## Value

A Assay, Assay5 or Seurat object.

## Examples

```r
data(pancreas_sub)
features <- GetFeaturesData(pancreas_sub)
pancreas_sub <- AddFeaturesData(pancreas_sub, features)
```
