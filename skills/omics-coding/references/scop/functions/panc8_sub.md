# A subsetted version of human 'panc8' datasets

- Package: scop
- Language: R
- Function: `panc8_sub`
- Source: https://mengxu98.github.io/scop/reference/panc8_sub.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/panc8_sub.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Human pancreatic islet cell datasets produced across four technologies, SMART-Seq2 (E-MTAB-5061), CelSeq (GSE81076), CelSeq2 (GSE85241), and Fluidigm C1 (GSE86469), from https://github.com/satijalab/seurat-data{SeuratData} package. For each data set in panc8, 200 cells were downsampled to form the panc8_sub dataset.

## Signature

```text
panc8_sub
```

## Parameters

No parameters detected.

## Full Documentation

# A subsetted version of human 'panc8' datasets

## Usage

```text
panc8_sub
```

## Description

Human pancreatic islet cell datasets produced across four technologies, SMART-Seq2 (E-MTAB-5061), CelSeq (GSE81076), CelSeq2 (GSE85241), and Fluidigm C1 (GSE86469), from https://github.com/satijalab/seurat-data{SeuratData} package. For each data set in panc8, 200 cells were downsampled to form the panc8_sub dataset.

## Examples

```r
data(pancreas_sub)
thisutils::check_r("satijalab/seurat-data")

InstallData <- thisutils::get_namespace_fun("SeuratData", "InstallData")
InstallData("panc8")
data(panc8)
panc8 <- UpdateSeuratObject(panc8)
set.seed(98)
cells_sub <- unlist(
  lapply(
    split(colnames(panc8), panc8$dataset),
    function(x) sample(x, size = 200)
  )
)
panc8_sub <- subset(panc8, cells = cells_sub)
counts <- GetAssayData5(
  panc8_sub,
  layer = "counts"
)
panc8_sub <- CreateSeuratObject(
  counts = counts,
  meta.data = panc8_sub@meta.data
)
panc8_sub <- panc8_sub[Matrix::rowSums(counts) > 0, ]
panc8_sub <- panc8_sub[toupper(
  rownames(panc8_sub)
) \%in\% toupper(
  rownames(pancreas_sub)
), ]
panc8_sub$celltype <- gsub("_", "-", panc8_sub$celltype)
panc8_sub$celltype <- gsub(" ", "-", panc8_sub$celltype)
use_data <- thisutils::get_namespace_fun("usethis", "use_data")
use_data(
  panc8_sub,
  compress = "xz",
  overwrite = TRUE
)
```
