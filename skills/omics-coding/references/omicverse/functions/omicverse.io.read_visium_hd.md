# omicverse.io.read_visium_hd #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_visium_hd`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_visium_hd.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read 10x Visium HD outputs with a single entry point.

## Signature

```text
omicverse.io. read_visium_hd ( path , data_type = 'bin' , sample = None , binsize = 16 , count_h5_path = 'filtered_feature_bc_matrix.h5' , count_mtx_dir = 'filtered_feature_bc_matrix' , tissue_positions_path = 'spatial/tissue_positions.parquet' , cell_segmentations_path = 'graphclust_annotated_cell_segmentations.geojson' , cell_matrix_h5_path = 'filtered_feature_cell_matrix.h5' , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' )
```

## Parameters

- `path`: ( str or Path ) – Root directory of a Visium HD run (typically the SpaceRanger output folder).
- `data_type`: ( {'bin' , 'cellseg'} , default 'bin' ) – Data mode to load. - 'bin' : bin-level matrix + tissue positions. - 'cellseg' : cell-segmentation polygons + cell matrix.
- `sample`: ( str , optional ) – Sample key used under adata.uns['spatial'][sample] . If not provided, it is inferred by the underlying reader.
- `binsize`: ( int , default 16 ) – Bin size metadata for data_type='bin' .
- `count_h5_path`: ( str , default "filtered_feature_bc_matrix.h5" ) – Relative H5 matrix path for data_type='bin' .
- `count_mtx_dir`: ( str , default "filtered_feature_bc_matrix" ) – Relative matrix directory path for data_type='bin' .
- `tissue_positions_path`: ( str , default "spatial/tissue_positions.parquet" ) – Relative tissue positions path for data_type='bin' .
- `cell_segmentations_path`: ( str , default "graphclust_annotated_cell_segmentations.geojson" ) – Relative segmentation GeoJSON path for data_type='cellseg' .
- `cell_matrix_h5_path`: ( str , default "filtered_feature_cell_matrix.h5" ) – Relative cell matrix path for data_type='cellseg' .
- `hires_image_path`: ( str , default "spatial/tissue_hires_image.png" ) – Relative hires image path (used by both modes).
- `lowres_image_path`: ( str , default "spatial/tissue_lowres_image.png" ) – Relative lowres image path (used by both modes).
- `scalefactors_path`: ( str , default "spatial/scalefactors_json.json" ) – Relative scalefactors JSON path (used by both modes).

## Full Documentation

# omicverse.io.read_visium_hd #

omicverse.io. read_visium_hd ( path , data_type = 'bin' , sample = None , binsize = 16 , count_h5_path = 'filtered_feature_bc_matrix.h5' , count_mtx_dir = 'filtered_feature_bc_matrix' , tissue_positions_path = 'spatial/tissue_positions.parquet' , cell_segmentations_path = 'graphclust_annotated_cell_segmentations.geojson' , cell_matrix_h5_path = 'filtered_feature_cell_matrix.h5' , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' ) [source] #

Read 10x Visium HD outputs with a single entry point.

This function dispatches to: - `read_visium_hd_bin `when `data_type='bin' `- `read_visium_hd_seg `when `data_type='cellseg' `

Parameters :

-
path ( str or Path ) – Root directory of a Visium HD run (typically the SpaceRanger output folder).

-
data_type ( {'bin' , 'cellseg'} , default 'bin' ) – Data mode to load. - `'bin' `: bin-level matrix + tissue positions. - `'cellseg' `: cell-segmentation polygons + cell matrix.

-
sample ( str , optional ) – Sample key used under `adata.uns['spatial'][sample] `. If not provided, it is inferred by the underlying reader.

-
binsize ( int , default 16 ) – Bin size metadata for `data_type='bin' `.

-
count_h5_path ( str , default "filtered_feature_bc_matrix.h5" ) – Relative H5 matrix path for `data_type='bin' `.

-
count_mtx_dir ( str , default "filtered_feature_bc_matrix" ) – Relative matrix directory path for `data_type='bin' `.

-
tissue_positions_path ( str , default "spatial/tissue_positions.parquet" ) – Relative tissue positions path for `data_type='bin' `.

-
cell_segmentations_path ( str , default "graphclust_annotated_cell_segmentations.geojson" ) – Relative segmentation GeoJSON path for `data_type='cellseg' `.

-
cell_matrix_h5_path ( str , default "filtered_feature_cell_matrix.h5" ) – Relative cell matrix path for `data_type='cellseg' `.

-
hires_image_path ( str , default "spatial/tissue_hires_image.png" ) – Relative hires image path (used by both modes).

-
lowres_image_path ( str , default "spatial/tissue_lowres_image.png" ) – Relative lowres image path (used by both modes).

-
scalefactors_path ( str , default "spatial/scalefactors_json.json" ) – Relative scalefactors JSON path (used by both modes).

Returns :

AnnData object with expression matrix, spatial coordinates, and image/scalefactor metadata.

Return type :

AnnData

Raises :

ValueError – If `data_type `is not `'bin' `or `'cellseg' `.

Examples

```text
>>> adata_bin = read_visium_hd("outs", data_type="bin", binsize=16)
>>> adata_cell = read_visium_hd("outs/segmented_outputs", data_type="cellseg")

```
