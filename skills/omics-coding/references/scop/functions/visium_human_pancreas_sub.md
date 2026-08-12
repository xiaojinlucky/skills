# A human pancreas Visium spatial example dataset

- Package: scop
- Language: R
- Function: `visium_human_pancreas_sub`
- Source: https://mengxu98.github.io/scop/reference/visium_human_pancreas_sub.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/visium_human_pancreas_sub.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

A compact gene-filtered version of a human pancreatic intraepithelial neoplasia (PanIN) 10x Visium dataset from GSE254829. The object keeps the 1986 non-background tissue spots from sample GSM8058244 (PanIN-LG2), with a Spatial assay, a slice1 Visium image, and tissue coordinates in metadata columns x and y. Metadata column coda_label stores the dominant CODA microanatomical component for each spot, and coda_score stores its percentage. Component percentage columns are stored with the coda_ prefix, and the matched CODA table is stored in @tools$GSE254829_coda_table. To keep the package data small and directly usable with the bundled panc8_sub reference, the object retains the top 5000 genes shared with panc8_sub, ranked by total spatial counts.

## Signature

```text
visium_human_pancreas_sub
```

## Parameters

No parameters detected.

## Full Documentation

# A human pancreas Visium spatial example dataset

## Usage

```text
visium_human_pancreas_sub
```

## Description

A compact gene-filtered version of a human pancreatic intraepithelial neoplasia (PanIN) 10x Visium dataset from GSE254829. The object keeps the 1986 non-background tissue spots from sample GSM8058244 (PanIN-LG2), with a Spatial assay, a slice1 Visium image, and tissue coordinates in metadata columns x and y. Metadata column coda_label stores the dominant CODA microanatomical component for each spot, and coda_score stores its percentage. Component percentage columns are stored with the coda_ prefix, and the matched CODA table is stored in @tools$GSE254829_coda_table. To keep the package data small and directly usable with the bundled panc8_sub reference, the object retains the top 5000 genes shared with panc8_sub, ranked by total spatial counts.

## Examples

```r
data(visium_human_pancreas_sub)
SeuratObject::Images(visium_human_pancreas_sub)
head(visium_human_pancreas_sub@meta.data[, c("x", "y")])
SpatialSpotPlot(visium_human_pancreas_sub, group.by = "coda_label")
```
