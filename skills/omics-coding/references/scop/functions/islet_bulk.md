# Human pancreatic islet bulk RNA-seq example dataset

- Package: scop
- Language: R
- Function: `islet_bulk`
- Source: https://mengxu98.github.io/scop/reference/islet_bulk.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/islet_bulk.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

A full human pancreatic islet bulk RNA-seq SummarizedExperiment derived from a brefeldin A perturbation study. The object keeps all samples from the published islet arm and stores a symbol-level count matrix that can be used directly in bulk DE and deconvolution examples together with the bundled panc8_sub reference.

## Signature

```text
islet_bulk
```

## Parameters

No parameters detected.

## Full Documentation

# Human pancreatic islet bulk RNA-seq example dataset

## Usage

```text
islet_bulk
```

## Description

A full human pancreatic islet bulk RNA-seq SummarizedExperiment derived from a brefeldin A perturbation study. The object keeps all samples from the published islet arm and stores a symbol-level count matrix that can be used directly in bulk DE and deconvolution examples together with the bundled panc8_sub reference.

## Examples

```r
data(islet_bulk)
SummarizedExperiment::assayNames(islet_bulk)
head(rownames(islet_bulk))
table(SummarizedExperiment::colData(islet_bulk)$condition)
```
