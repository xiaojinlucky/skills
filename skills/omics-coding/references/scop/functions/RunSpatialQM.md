# Run SpatialQM quality metrics

- Package: scop
- Language: R
- Function: `RunSpatialQM`
- Source: https://mengxu98.github.io/scop/reference/RunSpatialQM.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSpatialQM.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run selected SpatialQM quality-control metrics on a spatial Seurat object and store a compact standardized result bundle in srt@tools. SpatialQM currently expects a RNA assay for object-first metrics, so this wrapper maps the selected assay layer to a temporary RNA assay without modifying the returned object. SpatialQM is an optional GitHub dependency installable with remotes::install_github("Center-for-Spatial-OMICs/SpatialQM").

## Signature

```text
RunSpatialQM( srt, assay = NULL, layer = "counts", metrics = c("n_cells", "tx_per_cell", "max_detection"), features = NULL, sample_id = NULL, platform = NULL, tool_name = "SpatialQM", store_results = TRUE, on_error = c("error", "warning"), verbose = TRUE, ... )
```

## Parameters

- `srt`: A Seurat object.
- `assay`: Assay used for SpatialQM input. If NULL, the default assay is used.
- `layer`: Assay layer used as counts for SpatialQM.
- `metrics`: SpatialQM metrics to run. Supported aliases include "n_cells", "tx_per_cell", "tx_per_area", "tx_per_nuc", "mean_expression", "mean_signal_ratio", "cell_tx_fraction", "max_ratio", "max_detection", "mecr", "morans", "silhouette", "sparsity", and "entropy". The defaults are the object-first metrics supported by the current upstream API without raw transcript or control-probe inputs; other metrics remain explicitly selectable.
- `features`: Optional feature vector passed to metrics that support a features argument.
- `sample_id, platform`: Optional values used to populate missing sample_id and platform metadata columns expected by some SpatialQM metrics.
- `tool_name`: Name used to store results in srt@tools.
- `store_results`: Whether to store results in srt@tools.
- `on_error`: Whether a failed metric should stop the wrapper ("error") or be recorded in the result bundle with a warning ("warning").
- `verbose`: Whether to print the message. Default is TRUE.
- `...`: Additional named arguments passed to SpatialQM metric functions when the installed function exposes matching formal arguments.

## Full Documentation

# Run SpatialQM quality metrics

## Usage

```text
RunSpatialQM( srt, assay = NULL, layer = "counts", metrics = c("n_cells", "tx_per_cell", "max_detection"), features = NULL, sample_id = NULL, platform = NULL, tool_name = "SpatialQM", store_results = TRUE, on_error = c("error", "warning"), verbose = TRUE, ... )
```

## Description

Run selected SpatialQM quality-control metrics on a spatial Seurat object and store a compact standardized result bundle in srt@tools. SpatialQM currently expects a RNA assay for object-first metrics, so this wrapper maps the selected assay layer to a temporary RNA assay without modifying the returned object. SpatialQM is an optional GitHub dependency installable with remotes::install_github("Center-for-Spatial-OMICs/SpatialQM").

## Value

A Seurat object. When store_results = TRUE, results are stored in srt@tools[[tool_name]].

## Examples

```r
data(visium_human_pancreas_sub)
spatial <- visium_human_pancreas_sub

spatial <- RunSpatialQM(
  spatial,
  assay = "Spatial",
  layer = "counts",
  metrics = "n_cells",
  platform = "Visium",
  verbose = FALSE
)
spatial@tools$SpatialQM$summary
```
