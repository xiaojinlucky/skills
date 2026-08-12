# Coverage track plot for ATAC data

- Package: scop
- Language: R
- Function: `CoverageTrackPlot`
- Source: https://mengxu98.github.io/scop/reference/CoverageTrackPlot.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/CoverageTrackPlot.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Thin wrapper around Signac::CoveragePlot with scop defaults.

## Signature

```text
CoverageTrackPlot( srt, region, assay = NULL, group.by = NULL, palette = "Chinese", palcolor = NULL, extend.upstream = 1000, extend.downstream = 1000, annotation = TRUE, peaks = TRUE, links = FALSE, tile = FALSE, ranges = NULL, ranges.group.by = NULL, region.highlight = NULL, verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `region`: Genomic region passed to Signac::CoveragePlot.
- `assay`: ATAC assay used for plotting.
- `group.by`: Name of one or more meta.data columns to group (color) cells by.
- `palette`: Color palette name. Available palettes can be found in [thisplot:show_palettes]{thisplot::show_palettes}. Default is "Chinese".
- `palcolor`: Custom colors used to create a color palette. Default is NULL.
- `extend.upstream, extend.downstream`: Distance to extend around the region.
- `annotation, peaks, links`: Whether to show gene annotation, peaks and links.
- `tile`: Whether to show fragment tiles in the coverage plot.
- `ranges`: Optional genomic ranges added as external tracks.
- `ranges.group.by`: Optional grouping variable used for ranges.
- `region.highlight`: Optional genomic ranges highlighted in the locus panel.
- `verbose`: Whether to print progress messages.
- `...`: Additional parameters passed to Signac::CoveragePlot.

## Full Documentation

# Coverage track plot for ATAC data

## Usage

```text
CoverageTrackPlot( srt, region, assay = NULL, group.by = NULL, palette = "Chinese", palcolor = NULL, extend.upstream = 1000, extend.downstream = 1000, annotation = TRUE, peaks = TRUE, links = FALSE, tile = FALSE, ranges = NULL, ranges.group.by = NULL, region.highlight = NULL, verbose = TRUE, ... )
```

## Description

Thin wrapper around Signac::CoveragePlot with scop defaults.

## Value

A coverage plot object.

## Examples

```r
data("pbmcmultiome_sub", package = "scop")
# Coverage plotting requires an ATAC object with valid fragment information.
if (length(Signac::Fragments(pbmcmultiome_sub[["peaks"]])) > 0) {
  CoverageTrackPlot(
    pbmcmultiome_sub,
    region = rownames(pbmcmultiome_sub[["peaks"]])[1],
    assay = "peaks",
    group.by = "CellType"
  )
}
```
