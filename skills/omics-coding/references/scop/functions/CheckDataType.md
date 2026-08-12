# Check and report the type of data in Seurat object

- Package: scop
- Language: R
- Function: `CheckDataType`
- Source: https://mengxu98.github.io/scop/reference/CheckDataType.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CheckDataType.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

This function checks and returns a string indicating the type of data. It checks for the presence of infinite values, negative values, and whether the values are floats or integers.

## Signature

```text
CheckDataType(object, ...) CheckDataType{Seurat}(object, layer = "data", assay = NULL, verbose = TRUE, ...) CheckDataType{default}(object, verbose = TRUE, ...)
```

## Parameters

- `object`: A Seurat object or a matrix.
- `...`: The message to print.
- `layer`: Which layer to use. Default is data.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Check and report the type of data in Seurat object

## Usage

```text
CheckDataType(object, ...) CheckDataType{Seurat}(object, layer = "data", assay = NULL, verbose = TRUE, ...) CheckDataType{default}(object, verbose = TRUE, ...)
```

## Description

This function checks and returns a string indicating the type of data. It checks for the presence of infinite values, negative values, and whether the values are floats or integers.

## Value

A string indicating the type of data. Possible values are: "raw_counts", "log_normalized_counts", "raw_normalized_counts", or "unknown".

## Examples

```r
data(pancreas_sub)
CheckDataType(pancreas_sub)
```
