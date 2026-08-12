# Run Statial Kontextual spatial relationships

- Package: scop
- Language: R
- Function: `RunStatialKontextual`
- Source: https://mengxu98.github.io/scop/reference/RunStatialKontextual.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunStatialKontextual.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Statial::Kontextual() on a spatial Seurat object to quantify pairwise cell or spot label relationships relative to a parent context. Results are stored as a compact SCOP bundle with raw Statial output, standardized summary, and parameters. Statial is an optional Bioconductor dependency installable with BiocManager::install("Statial").

## Signature

```text
RunStatialKontextual( srt, group.by, r, from = NULL, to = NULL, parent = NULL, parent_df = NULL, image = NULL, sample.by = NULL, images = NULL, coord.cols = c("col", "row"), inhom = FALSE, edge_correct = TRUE, window = c("convex", "square", "concave"), window.length = NA_real_, include_original = TRUE, cores = 1, tool_name = "StatialKontextual", store_results = TRUE, store_input = FALSE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Parameters

- `srt`: A Seurat object.
- `group.by`: Metadata column containing cell or spot labels.
- `r`: Numeric radius or radii used by Statial::Kontextual(), expressed in the selected coordinate units.
- `from, to, parent`: Cell or spot labels passed to Statial::Kontextual(). Ignored when parent_df is supplied.
- `parent_df`: Optional data frame from Statial::parentCombinations().
- `image`: Name of the Seurat spatial image. Required when multiple images are present; a single image is selected automatically when NULL.
- `sample.by`: Optional metadata column used as Statial imageID. If NULL, all cells or spots are treated as one image.
- `images`: Optional Statial image filter passed to Kontextual(image = ).
- `coord.cols`: Metadata coordinate columns used when no Seurat image coordinates are available.
- `inhom`: Whether Statial should account for inhomogeneity.
- `edge_correct`: Whether Statial should perform edge correction.
- `window, window.length`: Window arguments passed to Statial::Kontextual(). Numeric window lengths use the selected coordinate units.
- `include_original`: Whether to include original L-function values.
- `cores`: Number of cores passed to Statial::Kontextual().
- `tool_name`: Name used to store results in srt@tools.
- `store_results`: Whether to store results in srt@tools.
- `store_input`: Whether to store the backend input cell table in srt@tools.
- `verbose`: Whether to print the message. Default is TRUE.
- `coordinate_space`: Coordinate system used for spatial relationships. The default is raw acquisition coordinates; "legacy_display" remains an explicit compatibility option.
- `...`: Additional named arguments passed to Statial::Kontextual().

## Full Documentation

# Run Statial Kontextual spatial relationships

## Usage

```text
RunStatialKontextual( srt, group.by, r, from = NULL, to = NULL, parent = NULL, parent_df = NULL, image = NULL, sample.by = NULL, images = NULL, coord.cols = c("col", "row"), inhom = FALSE, edge_correct = TRUE, window = c("convex", "square", "concave"), window.length = NA_real_, include_original = TRUE, cores = 1, tool_name = "StatialKontextual", store_results = TRUE, store_input = FALSE, verbose = TRUE, coordinate_space = c("raw", "legacy_display"), ... )
```

## Description

Run Statial::Kontextual() on a spatial Seurat object to quantify pairwise cell or spot label relationships relative to a parent context. Results are stored as a compact SCOP bundle with raw Statial output, standardized summary, and parameters. Statial is an optional Bioconductor dependency installable with BiocManager::install("Statial").

## Value

A Seurat object with Statial results stored in srt@tools[[tool_name]] when store_results = TRUE.

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub

labels <- unique(as.character(spatial$coda_label))
if (length(labels) >= 2) {
  spatial <- RunStatialKontextual(
    spatial,
    group.by = "coda_label",
    r = 50,
    from = labels[1],
    to = labels[2],
    parent = labels[1:2],
    coord.cols = c("x", "y"),
    verbose = FALSE
  )
  spatial@tools$StatialKontextual$summary
}
```
