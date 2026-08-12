# Run spot-level quality control

- Package: scop
- Language: R
- Function: `RunSpotQC`
- Source: https://mengxu98.github.io/scop/reference/RunSpotQC.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSpotQC.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Calculate common spot-level QC metrics for spatial transcriptomics data and label failed spots without running single-cell-specific checks such as doublet calling or ambient RNA decontamination.

## Signature

```text
RunSpotQC( srt, assay = NULL, return_filtered = FALSE, qc_metrics = c("outlier", "umi", "gene", "mito"), outlier_threshold = c("log10_nCount:lower:3", "log10_nFeature:lower:3", "spot_featurecount_dist:lower:3"), outlier_n = 1, UMI_threshold = 500, gene_threshold = 200, mito_threshold = 20, mito_pattern = c("MT-", "Mt-", "mt-"), mito_gene = NULL, verbose = TRUE, seed = 11 )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Which assay to use. If NULL, the default assay of the Seurat object will be used. When the object also contains ChromatinAssay, the default assay and additional ChromatinAssay will be preprocessed sequentially.
- `return_filtered`: Logical indicating whether to return a spot-filtered Seurat object. Default is FALSE.
- `qc_metrics`: QC metrics to apply. Available metrics are "outlier", "umi", "gene", and "mito".
- `outlier_threshold`: Character vector specifying outlier thresholds as "metric:direction:nmads". Available default metrics are "log10_nCount", "log10_nFeature", and "spot_featurecount_dist".
- `outlier_n`: Minimum number of outlier metrics required to fail a spot.
- `UMI_threshold`: Minimum UMI count required to pass "umi" QC.
- `gene_threshold`: Minimum detected gene count required to pass "gene" QC.
- `mito_threshold`: Maximum mitochondrial percentage allowed by "mito" QC.
- `mito_pattern`: Regex patterns used to identify mitochondrial genes.
- `mito_gene`: Optional explicit mitochondrial gene vector. When provided, mito_pattern is ignored.
- `verbose`: Whether to print the message. Default is TRUE.
- `seed`: Random seed for reproducibility.

## Full Documentation

# Run spot-level quality control

## Usage

```text
RunSpotQC( srt, assay = NULL, return_filtered = FALSE, qc_metrics = c("outlier", "umi", "gene", "mito"), outlier_threshold = c("log10_nCount:lower:3", "log10_nFeature:lower:3", "spot_featurecount_dist:lower:3"), outlier_n = 1, UMI_threshold = 500, gene_threshold = 200, mito_threshold = 20, mito_pattern = c("MT-", "Mt-", "mt-"), mito_gene = NULL, verbose = TRUE, seed = 11 )
```

## Description

Calculate common spot-level QC metrics for spatial transcriptomics data and label failed spots without running single-cell-specific checks such as doublet calling or ambient RNA decontamination.

## Value

A Seurat object with spot QC metadata columns.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- RunSpotQC(
  visium_human_pancreas_sub,
  assay = "Spatial"
)
SpatialSpotPlot(spatial, group.by = "SpotQC")
```
