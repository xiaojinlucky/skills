# Run bulk or pseudobulk deconvolution

- Package: scop
- Language: R
- Function: `RunDeconvolution`
- Source: https://mengxu98.github.io/scop/reference/RunDeconvolution.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunDeconvolution.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Estimate cell-type proportions from a bulk-like expression matrix stored in a SummarizedExperiment object, using a Seurat reference.

## Signature

```text
RunDeconvolution(object, ...) RunDeconvolution{SummarizedExperiment}( object, reference = NULL, method = c("MuSiC", "BisqueRNA", "BayesPrism", "CIBERSORT"), group.by = NULL, sample.by = NULL, cellstate.by = NULL, bulk_assay = "counts", ref_assay = NULL, ref_layer = "counts", backend = c("cpp", "r"), verbose = TRUE, ... )
```

## Parameters

- `object`: A SummarizedExperiment object containing bulk-like counts.
- `...`: Additional parameters forwarded to the internal deconvolution backend.
- `reference`: A Seurat reference object used to build cell-type profiles. Not required for "CIBERSORT".
- `method`: Deconvolution method. One of "MuSiC", "BisqueRNA", "BayesPrism", or "CIBERSORT".
- `group.by`: Metadata column in reference defining reference cell types.
- `sample.by`: Metadata column in reference defining biological sample / donor IDs. Used by the r backends of MuSiC and BisqueRNA. If NULL, SCOP will try to infer a suitable column automatically.
- `cellstate.by`: Metadata column in reference defining cell states for the r backend of BayesPrism. If NULL, group.by is reused.
- `bulk_assay`: Assay name in object used as the bulk counts matrix.
- `ref_assay`: Assay name in reference used for the reference profiles.
- `ref_layer`: Layer name in reference used for reference counts.
- `backend`: Deconvolution engine backend. "r" uses the original method package implementation. "cpp" selects package C++ implementations when available.
- `verbose`: Whether to print the message. Default is TRUE.

## Full Documentation

# Run bulk or pseudobulk deconvolution

## Usage

```text
RunDeconvolution(object, ...) RunDeconvolution{SummarizedExperiment}( object, reference = NULL, method = c("MuSiC", "BisqueRNA", "BayesPrism", "CIBERSORT"), group.by = NULL, sample.by = NULL, cellstate.by = NULL, bulk_assay = "counts", ref_assay = NULL, ref_layer = "counts", backend = c("cpp", "r"), verbose = TRUE, ... )
```

## Description

Estimate cell-type proportions from a bulk-like expression matrix stored in a SummarizedExperiment object, using a Seurat reference.

## Value

A SummarizedExperiment object with results stored in S4Vectors::metadata(object)[["Deconvolution"]].

## Examples

```r
data(islet_bulk)
islet_bulk <- RunDeconvolution(
  islet_bulk,
  method = "CIBERSORT",
  backend = "cpp",
  perm = 0
)
DeconvolutionPlot(islet_bulk, plot_type = "bar")

DeconvolutionPlot(
  islet_bulk,
  plot_type = "heatmap",
  sample_annotation = "condition",
  sample_split = "condition"
)

DeconvolutionPlot(islet_bulk, plot_type = "box")
```
