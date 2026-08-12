# Get features data

- Package: scop
- Language: R
- Function: `GetFeaturesData`
- Source: https://mengxu98.github.io/scop/reference/GetFeaturesData.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/GetFeaturesData.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Get the data from the Assay, Assay5 or Seurat object.

## Signature

```text
GetFeaturesData(object, ...) GetFeaturesData{Seurat}(object, assay = NULL, ...) GetFeaturesData{Assay}(object, ...) GetFeaturesData{Assay5}(object, ...)
```

## Parameters

- `object`: A Assay, Assay5 or Seurat object.
- `...`: Additional arguments passed to the method.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.

## Full Documentation

# Get features data

## Usage

```text
GetFeaturesData(object, ...) GetFeaturesData{Seurat}(object, assay = NULL, ...) GetFeaturesData{Assay}(object, ...) GetFeaturesData{Assay5}(object, ...)
```

## Description

Get the data from the Assay, Assay5 or Seurat object.

## Value

A data frame containing the features data.

## Examples

```r
data(pancreas_sub)
features <- GetFeaturesData(pancreas_sub)
head(features)
```
