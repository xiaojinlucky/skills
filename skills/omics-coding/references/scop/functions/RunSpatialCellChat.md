# Run Spatial CellChat analysis

- Package: scop
- Language: R
- Function: `RunSpatialCellChat`
- Source: https://mengxu98.github.io/scop/reference/RunSpatialCellChat.html
- Raw source: https://raw.githubusercontent.com/mengxu98/scop/main/man/RunSpatialCellChat.Rd
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run the SpatialCellChat v3 backend with explicit micron-scale coordinates, sample isolation, truthful provenance, and schema-v1 storage. Cell-, spot-, and composition-level results retain distinct interpretations.

## Signature

```text
RunSpatialCellChat( srt, group.by, sample.by = NULL, assay = NULL, layer = "data", image = NULL, coord.cols = c("col", "row"), species = c("Homo_sapiens", "Mus_musculus"), database = c("protein", "all", "custom"), custom.db = NULL, technology = c("auto", "visium", "visium_hd", "xenium", "cosmx", "merfish", "generic"), analysis.level = c("auto", "cell", "spot", "composition"), composition = NULL, composition.normalize = TRUE, coordinate.unit = c("auto", "pixel", "micron"), ratio = NULL, tol = NULL, interaction.range = 250, contact.dependent = FALSE, contact.range = NULL, scale.distance = 0.2, min.cells = 10, min.links = 10, avg.type = c("avg", "sum"), do.permutation = TRUE, nboot = 100, seed.use = 1L, result.name = "default", store.object = c("minimal", "full"), overwrite = FALSE, backend = c("cpp", "r"), verbose = TRUE )
```

## Parameters

- `srt`: A `Seurat` object with normalized, non-negative expression and spatial coordinates.
- `group.by`: One metadata column defining cell types for cell-level runs, or spot/domain labels for spot- and composition-level runs. Values must be complete and non-empty.
- `sample.by`: Optional metadata column defining independent spatial samples. Samples are processed separately. When omitted, all observations are treated as one sample.
- `assay, layer`: Assay and normalized expression layer. `assay = NULL` uses the default assay.
- `image`: Spatial image name, or a named character vector mapping samples to images, for example `c(section1 = "slice1", section2 = "slice2")`. Multi-image objects never silently select the first image.
- `coord.cols`: Two metadata coordinate columns used when image coordinates are unavailable.
- `species`: Species used to select the human or mouse signaling database.
- `database`: Signaling database scope: protein interactions, the complete database, or a user-supplied custom database.
- `custom.db`: Custom SpatialCellChat database used only with `database = "custom"`.
- `technology`: Spatial technology. `"auto"` requires exactly one unambiguous technology inferred from the selected image or metadata.
- `analysis.level`: Scientific interpretation of each observation. `"auto"` uses segmentation, technology, and `composition` evidence and errors when the result is ambiguous.
- `composition`: Numeric spot-by-cell-type matrix for composition mode. Row names must match selected spots and columns must match `group.by` labels.
- `composition.normalize`: Whether to normalize positive composition rows to sum to one. When `FALSE`, rows must already sum to one.
- `coordinate.unit`: Unit of the raw input coordinates. Automatic unit selection uses technology-specific rules.
- `ratio`: Positive raw-coordinate-to-micron multiplier. It must be `1` for micron coordinates. For Visium pixels, it may be omitted when one trusted `spot_diameter_fullres` value is available.
- `tol`: Positive spatial tolerance in microns. Visium defaults to `32.5`; cell-resolved and generic technologies require an explicit value.
- `interaction.range`: Maximum signaling range in microns.
- `contact.dependent`: Whether to infer contact-dependent signaling. This is rejected for spot-level analysis.
- `contact.range`: Contact range in microns. Required when contact signaling is enabled for cell-level data.
- `scale.distance`: Positive SpatialCellChat distance scaling parameter.
- `min.cells, min.links`: Positive minimum group size and individual-link count used by backend filtering.
- `avg.type`: Group-level probability aggregation method.
- `do.permutation`: Whether to run the spatial permutation procedure.
- `nboot`: Number of permutation replicates.
- `seed.use`: Random seed passed to the backend.
- `result.name`: Name used within the stored SpatialCellChat result bundle.
- `store.object`: `"minimal"` stores normalized tables, coordinates, and diagnostics. `"full"` additionally stores each upstream backend object.
- `overwrite`: Whether an existing result with the same `result.name` may be replaced.
- `backend`: Backend for unified CCC post-processing only; it does not change the SpatialCellChat inference engine.
- `verbose`: Whether to print progress messages.

## Full Documentation

# Run Spatial CellChat analysis

## Usage

```text
RunSpatialCellChat( srt, group.by, sample.by = NULL, assay = NULL, layer = "data", image = NULL, coord.cols = c("col", "row"), species = c("Homo_sapiens", "Mus_musculus"), database = c("protein", "all", "custom"), custom.db = NULL, technology = c("auto", "visium", "visium_hd", "xenium", "cosmx", "merfish", "generic"), analysis.level = c("auto", "cell", "spot", "composition"), composition = NULL, composition.normalize = TRUE, coordinate.unit = c("auto", "pixel", "micron"), ratio = NULL, tol = NULL, interaction.range = 250, contact.dependent = FALSE, contact.range = NULL, scale.distance = 0.2, min.cells = 10, min.links = 10, avg.type = c("avg", "sum"), do.permutation = TRUE, nboot = 100, seed.use = 1L, result.name = "default", store.object = c("minimal", "full"), overwrite = FALSE, backend = c("cpp", "r"), verbose = TRUE )
```

## Description

Run the SpatialCellChat v3 backend with explicit micron-scale coordinates, sample isolation, truthful provenance, and schema-v1 storage. Cell-, spot-, and composition-level results retain distinct interpretations.

## Value

The input `Seurat` object with a schema-v1 SpatialCellChat bundle in `srt@tools$SpatialCellChat` and standardized CCC results under the distinct method name `"SpatialCellChat"`.

## Examples

```r
# SpatialCellChat is a runtime-optional backend and a full run can be slow.
# The following example uses constructed domain labels only to demonstrate
# the multi-slice interface.
\dontrun{
if (all(unlist(
  thisutils::check_r("jinworks/SpatialCellChat", verbose = FALSE),
  use.names = FALSE
))) {
  data(visium_mouse_brain_slices_sub)
  spatial <- visium_mouse_brain_slices_sub
  spatial$spatial_domain <- ifelse(
    spatial$x <= stats::median(spatial$x), "left", "right"
  )
  spatial <- RunSpatialCellChat(
    spatial,
    group.by = "spatial_domain",
    sample.by = "sample",
    assay = "Spatial",
    image = c(anterior1 = "anterior1", anterior2 = "anterior2"),
    technology = "visium",
    analysis.level = "spot",
    coordinate.unit = "pixel",
    species = "Mus_musculus",
    store.object = "minimal"
  )
  SpatialBackendStatus(backend = "spatialcellchat")
  SpatialResultInfo(spatial, method = "RunSpatialCellChat")
  SpatialCellChatPlot(spatial, sample = "anterior1", plot_type = "incoming")
}
}
```
