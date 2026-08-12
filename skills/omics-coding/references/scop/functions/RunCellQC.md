# Run cell-level quality control

- Package: scop
- Language: R
- Function: `RunCellQC`
- Source: https://mengxu98.github.io/scop/reference/RunCellQC.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunCellQC.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run cell-level quality control

## Signature

```text
RunCellQC( srt, assay = "RNA", split.by = NULL, group.by = NULL, return_filtered = FALSE, qc_metrics = c("doublets", "decontX", "atac", "outlier", "umi", "gene", "mito", "ribo", "ribo_mito_ratio", "species"), db_method = "scDblFinder", db_rate = NULL, db_coefficient = 0.01, decontX_threshold = NULL, decontX_batch = NULL, decontX_background = NULL, decontX_background_assay = NULL, decontX_bg_batch = NULL, decontX_assay_name = "decontXcounts", decontX_store_assay = FALSE, decontX_round_counts = TRUE, decontX_args = list(), atac_args = list(), outlier_threshold = c("log10_nCount:lower:2.5", "log10_nCount:higher:5", "log10_nFeature:lower:2.5", "log10_nFeature:higher:5", "featurecount_dist:lower:2.5"), outlier_n = 1, UMI_threshold = 3000, gene_threshold = 1000, mito_threshold = 20, mito_pattern = c("MT-", "Mt-", "mt-"), mito_gene = NULL, ribo_threshold = 50, ribo_pattern = c("RP[SL]\\\+\\\0,1\\\*$", "Rp[sl]\\\+\\\0,1\\\*$", "rp[sl]\\\+\\\0,1\\\*$"), ribo_gene = NULL, ribo_mito_ratio_range = c(1, Inf), species = NULL, species_gene_prefix = NULL, species_percent = 95, seed = 11, verbose = TRUE, hb_range = c(0, 5), hb_pattern = c("HB[^P]", "Hb[^p]", "hb[^p]"), hb_gene = NULL, qc_features = list() )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: The name of the assay to be used for doublet-calling. Default is "RNA".
- `split.by`: Name of a meta.data column used to split the object before QC. Default is NULL. When specified, QC and doublet-calling are performed separately within each split object and merged back afterward.
- `group.by`: Group labels passed to {[=RunDecontX]{RunDecontX()}} when "decontX" is included in qc_metrics. Can be NULL, a meta.data column name, or a vector aligned to cells. Default is NULL.
- `return_filtered`: Logical indicating whether to return a cell-filtered Seurat object. Default is FALSE.
- `qc_metrics`: A character vector specifying the quality control metrics to be applied. Available metrics are "doublets", "decontX", "atac", "outlier", "umi", "gene", "mito", "ribo", "hb", "ribo_mito_ratio", "species", and any rule name supplied in qc_features. Default is c("doublets", "decontX", "outlier", "umi", "gene", "mito", "ribo", "ribo_mito_ratio", "species"). For ChromatinAssay, if .arg qc_metrics is not supplied, the default is "atac".
- `db_method`: Method used for doublet-calling. Can be one of "scDblFinder", "Scrublet", "DoubletDetection", "scds_cxds", "scds_bcds", "scds_hybrid". The resulting doublet labels are aggregated afterward into db_qc and do not affect the thresholds used by the other QC metrics.
- `db_rate`: The expected doublet rate. Default is calculated as ncol(srt) / 1000 * 0.01.
- `db_coefficient`: The coefficient used to calculate the doublet rate. Default is 0.01. Doublet rate is calculated as ncol(srt) / 1000 * db_coefficient.
- `decontX_threshold`: Optional contamination threshold used to filter cells after running {[=RunDecontX]{RunDecontX()}}. Cells with decontX_contamination greater than this value are marked as failed in decontX_qc. Default is NULL, which computes decontX results without filtering cells by contamination.
- `decontX_batch`: Batch labels passed to {[=RunDecontX]{RunDecontX()}} when "decontX" is included in qc_metrics. Default is NULL.
- `decontX_background`: Optional background / empty-droplet input passed to {[=RunDecontX]{RunDecontX()}} when "decontX" is included in qc_metrics. Default is NULL.
- `decontX_background_assay`: Assay name used when decontX_background is a Seurat object or SingleCellExperiment. Default is NULL.
- `decontX_bg_batch`: Batch labels for decontX_background passed to {[=RunDecontX]{RunDecontX()}}. Default is NULL.
- `decontX_assay_name`: Name of the assay used to store decontaminated counts from {[=RunDecontX]{RunDecontX()}}. Default is "decontXcounts".
- `decontX_store_assay`: Whether to store decontaminated counts as a new assay when running {[=RunDecontX]{RunDecontX()}}. Default is FALSE.
- `decontX_round_counts`: Whether to round decontaminated counts before creating the assay in {[=RunDecontX]{RunDecontX()}}. Default is TRUE.
- `decontX_args`: A named list of additional advanced arguments passed to {[=RunDecontX]{RunDecontX()}} when "decontX" is included in qc_metrics. Explicit decontX_* parameters are preferred for common options and take precedence when both are supplied. Default is list().
- `atac_args`: A named list of additional arguments passed to {[=RunATACQC]{RunATACQC()}} when "atac" is included in qc_metrics. Threshold arguments from {[=RunATACQC]{RunATACQC()}} are used to label failed cells in atac_qc, but filtering is deferred to {[=RunCellQC]{RunCellQC()}}. Default is list().
- `outlier_threshold`: A character vector specifying the outlier threshold. Default is c("log10_nCount:lower:2.5", "log10_nCount:higher:5", "log10_nFeature:lower:2.5", "log10_nFeature:higher:5", "featurecount_dist:lower:2.5").
- `outlier_n`: Minimum number of outlier metrics that meet the conditions for determining outlier cells. Default is 1.
- `UMI_threshold`: UMI number threshold. Cells that exceed this threshold will be considered as kept. Default is 3000.
- `gene_threshold`: Gene number threshold. Cells that exceed this threshold will be considered as kept. Default is 1000.
- `mito_threshold`: Percentage of UMI counts of mitochondrial genes. Cells that exceed this threshold will be considered as discarded. Default is 20.
- `mito_pattern`: Regex patterns to match the mitochondrial genes. Default is c("MT-", "Mt-", "mt-").
- `mito_gene`: A defined mitochondrial genes. If features provided, will ignore the mito_pattern matching. Default is NULL.
- `ribo_threshold`: Percentage of UMI counts of ribosomal genes. Cells that exceed this threshold will be considered as discarded. Default is 50.
- `ribo_pattern`: Regex patterns to match the ribosomal genes. Default is {c("RP[SL]\\\+\\\0,1\\\*$", "Rp[sl]\\\+\\\0,1\\\*$", "rp[sl]\\\+\\\0,1\\\*$")}.
- `ribo_gene`: A defined ribosomal genes. If features provided, will ignore the ribo_pattern matching. Default is NULL.
- `ribo_mito_ratio_range`: A numeric vector specifying the range of ribosomal/mitochondrial gene expression ratios for ribo_mito_ratio outlier cells. Default is c(1, Inf).
- `species`: Species used as the suffix of the QC metrics. The first is the species of interest. Default is NULL.
- `species_gene_prefix`: Species gene prefix used to calculate QC metrics for each species. Default is NULL.
- `species_percent`: Percentage of UMI counts of the first species. Cells that exceed this threshold will be considered as kept. Default is 95.
- `seed`: Random seed for reproducibility. Default is 11.
- `verbose`: Whether to print the message. Default is TRUE.
- `hb_range`: A numeric vector specifying the accepted percentage range for hemoglobin features. Values outside the range fail hb_qc when "hb" is included in qc_metrics. Default is c(0, 5).
- `hb_pattern`: Regex patterns used to match hemoglobin features. The defaults match common human, mouse, and lower-case symbols while excluding HBP/hbp genes. Default is c("HB[^P]", "Hb[^p]", "hb[^p]").
- `hb_gene`: A defined set of hemoglobin features. When supplied, these features are used instead of hb_pattern. Default is NULL.
- `qc_features`: A named list defining additional feature-percentage QC rules. Each rule must contain exactly one of features (a character vector) or pattern (one or more regex patterns), plus a numeric range of length two. Providing a rule computes percent.<name>; the rule filters cells and creates <name>_qc only when <name> is included in qc_metrics. Patterns are matched directly against assay feature names and do not receive species prefixes. Rule names cannot collide with built-in QC columns. Default is list().

## Full Documentation

# Run cell-level quality control

## Usage

```text
RunCellQC( srt, assay = "RNA", split.by = NULL, group.by = NULL, return_filtered = FALSE, qc_metrics = c("doublets", "decontX", "atac", "outlier", "umi", "gene", "mito", "ribo", "ribo_mito_ratio", "species"), db_method = "scDblFinder", db_rate = NULL, db_coefficient = 0.01, decontX_threshold = NULL, decontX_batch = NULL, decontX_background = NULL, decontX_background_assay = NULL, decontX_bg_batch = NULL, decontX_assay_name = "decontXcounts", decontX_store_assay = FALSE, decontX_round_counts = TRUE, decontX_args = list(), atac_args = list(), outlier_threshold = c("log10_nCount:lower:2.5", "log10_nCount:higher:5", "log10_nFeature:lower:2.5", "log10_nFeature:higher:5", "featurecount_dist:lower:2.5"), outlier_n = 1, UMI_threshold = 3000, gene_threshold = 1000, mito_threshold = 20, mito_pattern = c("MT-", "Mt-", "mt-"), mito_gene = NULL, ribo_threshold = 50, ribo_pattern = c("RP[SL]\\\+\\\0,1\\\*$", "Rp[sl]\\\+\\\0,1\\\*$", "rp[sl]\\\+\\\0,1\\\*$"), ribo_gene = NULL, ribo_mito_ratio_range = c(1, Inf), species = NULL, species_gene_prefix = NULL, species_percent = 95, seed = 11, verbose = TRUE, hb_range = c(0, 5), hb_pattern = c("HB[^P]", "Hb[^p]", "hb[^p]"), hb_gene = NULL, qc_features = list() )
```

## Description

Run cell-level quality control

## Value

Returns Seurat object with the QC results stored in the meta.data layer.

## Examples

```r
data(pancreas_sub)
pancreas_sub <- RunStandardWorkflow(pancreas_sub)
pancreas_sub <- RunCellQC(
  pancreas_sub,
  qc_metrics = c("umi", "gene", "example_set"),
  qc_features = list(
    example_set = list(
      features = head(rownames(pancreas_sub), 5),
      range = c(0, 0)
    )
  )
)
head(pancreas_sub@meta.data[, c("percent.hb", "percent.example_set")])
# Hemoglobin expression can be biological signal in erythroid samples;
# include "hb" in qc_metrics only when HB-based filtering is appropriate.

CellStatPlot(
  pancreas_sub,
  stat.by = c(
    "umi_qc", "gene_qc", "example_set_qc"
  ),
  plot_type = "upset",
  stat_level = "Fail"
)
```
