# A small human PBMC multiome example dataset

- Package: scop
- Language: R
- Function: `pbmcmultiome_sub`
- Source: https://mengxu98.github.io/scop/reference/pbmcmultiome_sub.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/pbmcmultiome_sub.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

A near-balanced 500-cell subset of the PBMC multiome dataset from SeuratData, containing paired RNA and peaks assays for package examples and tests. The dataset keeps approximately equal numbers of cells for each major PBMC cell type and retains the top 12000 accessible peaks by total counts within the selected cells. When available, the peaks assay stores a compact hg38 gene annotation derived from EnsDb.Hsapiens.v86 and collapsed to the longest transcript per gene.

## Signature

```text
pbmcmultiome_sub
```

## Parameters

No parameters detected.

## Full Documentation

# A small human PBMC multiome example dataset

## Usage

```text
pbmcmultiome_sub
```

## Description

A near-balanced 500-cell subset of the PBMC multiome dataset from SeuratData, containing paired RNA and peaks assays for package examples and tests. The dataset keeps approximately equal numbers of cells for each major PBMC cell type and retains the top 12000 accessible peaks by total counts within the selected cells. When available, the peaks assay stores a compact hg38 gene annotation derived from EnsDb.Hsapiens.v86 and collapsed to the longest transcript per gene.

## Examples

```r
source("test/data/create_pbmcmultiome_sub.R")
pbmcmultiome_sub <- create_pbmcmultiome_sub()
use_data <- thisutils::get_namespace_fun("usethis", "use_data")
use_data(
  pbmcmultiome_sub,
  compress = "xz",
  overwrite = TRUE
)
```
