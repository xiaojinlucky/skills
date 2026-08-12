# omicverse.io.read_visium_hd_seg #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_visium_hd_seg`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_visium_hd_seg.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read Visium HD cell-segmentation output and attach geometries + spatial metadata.

## Signature

```text
omicverse.io. read_visium_hd_seg ( path , sample = None , cell_segmentations_path = 'graphclust_annotated_cell_segmentations.geojson' , count_h5_path = 'filtered_feature_cell_matrix.h5' , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' )
```

## Parameters

- `path`: ( str or Path ) – Path to the cell-segmentation output directory.
- `sample`: ( str , optional ) – Sample key stored in adata.uns['spatial'] . If None , inferred from path.
- `cell_segmentations_path`: ( str ) – Relative path to segmentation GeoJSON.
- `count_h5_path`: ( str ) – Relative path to filtered feature-cell matrix (H5).
- `hires_image_path`: ( str ) – Relative path to hires tissue image.
- `lowres_image_path`: ( str ) – Relative path to lowres tissue image.
- `scalefactors_path`: ( str ) – Relative path to scalefactors JSON.

## Full Documentation

# omicverse.io.read_visium_hd_seg #

omicverse.io. read_visium_hd_seg ( path , sample = None , cell_segmentations_path = 'graphclust_annotated_cell_segmentations.geojson' , count_h5_path = 'filtered_feature_cell_matrix.h5' , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' ) [source] #

Read Visium HD cell-segmentation output and attach geometries + spatial metadata.

Parameters :

-
path ( str or Path ) – Path to the cell-segmentation output directory.

-
sample ( str , optional ) – Sample key stored in `adata.uns['spatial'] `. If `None `, inferred from path.

-
cell_segmentations_path ( str ) – Relative path to segmentation GeoJSON.

-
count_h5_path ( str ) – Relative path to filtered feature-cell matrix (H5).

-
hires_image_path ( str ) – Relative path to hires tissue image.

-
lowres_image_path ( str ) – Relative path to lowres tissue image.

-
scalefactors_path ( str ) – Relative path to scalefactors JSON.

Returns :

Cell-level AnnData with `obsm['spatial'] `, segmentation geometry, and spatial image metadata.

Return type :

anndata.AnnData
