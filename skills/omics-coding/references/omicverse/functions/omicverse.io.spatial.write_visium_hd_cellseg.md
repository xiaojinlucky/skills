# omicverse.io.spatial.write_visium_hd_cellseg #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.spatial.write_visium_hd_cellseg`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.spatial.write_visium_hd_cellseg.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Export cell-level AnnData to SpaceRanger v4-compatible directory structure.

## Signature

```text
omicverse.io.spatial. write_visium_hd_cellseg ( adata , path , sample = None )
```

## Parameters

- `adata`: ( AnnData ) – Cell-level AnnData from bin_to_cell() or read_visium_hd_seg() . Must have obs["geometry"] (WKT strings) and obsm["spatial"] .
- `path`: ( str or Path ) – Output directory to write SpaceRanger-like structure.
- `sample`: ( str , optional ) – Sample key in adata.uns["spatial"] . If None, uses the first key.

## Full Documentation

# omicverse.io.spatial.write_visium_hd_cellseg #

omicverse.io.spatial. write_visium_hd_cellseg ( adata , path , sample = None ) [source] #

Export cell-level AnnData to SpaceRanger v4-compatible directory structure.

Creates the following output files:

```text
path/
├── filtered_feature_cell_matrix.h5
├── graphclust_annotated_cell_segmentations.geojson
└── spatial/
├── tissue_hires_image.png
├── tissue_lowres_image.png
└── scalefactors_json.json

```

Parameters :

-
adata ( AnnData ) – Cell-level AnnData from `bin_to_cell() `or `read_visium_hd_seg() `. Must have `obs["geometry"] `(WKT strings) and `obsm["spatial"] `.

-
path ( str or Path ) – Output directory to write SpaceRanger-like structure.

-
sample ( str , optional ) – Sample key in `adata.uns["spatial"] `. If None, uses the first key.
