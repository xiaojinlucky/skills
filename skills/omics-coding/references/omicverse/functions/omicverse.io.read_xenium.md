# omicverse.io.read_xenium #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_xenium`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_xenium.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read a 10x Xenium outs directory into an AnnData object.

## Signature

```text
omicverse.io. read_xenium ( path , * , library_id = None , load_image = True , image_key = 'morphology_focus' , image_max_dim = 4096 , load_boundaries = True , cache_file = None )
```

## Parameters

- `path`: ( Union [ str , Path ] ) – The Xenium outs directory (or any directory containing the files above).
- `library_id`: ( Optional [ str ] (default: None )) – Identifier used as the key under adata.uns['spatial'] . Defaults to experiment.xenium ’s region_name / run_name if present, else the directory name.
- `load_image`: ( bool (default: True )) – When True and tifffile is installed, loads the morphology image so omicverse.pl.spatial() can overlay it. The morphology TIFF is large (hundreds of MB); pass False for lightweight tutorials that only need the centroid scatter.
- `image_key`: ( str (default: 'morphology_focus' )) – Which morphology image to load. Accepts: 'morphology_focus' / 'morphology_mip' — V1 layout files at the outs root; falls back to the first V2 channel ( _0000 , DAPI) when V1 files are absent.
- `image_max_dim`: ( int (default: 4096 )) – Xenium OME-TIFFs are multi-resolution pyramids; this is the maximum pixel extent along either axis that we will load. The highest-resolution pyramid level fitting under this cap is used. Default 4096 keeps the in-memory array small while remaining usable for overlay. Pass a larger value (e.g. 8192) for closer crops.
- `load_boundaries`: ( bool (default: True )) – When True and cell_boundaries.parquet / .csv.gz is present, converts per-cell polygon vertices to WKT strings stored in obs['geometry'] — required by omicverse.pl.spatialseg() .
- `cache_file`: ( Union [ str , Path , None ] (default: None )) – Optional path to an .h5ad cache. When set and the file exists, we read it back instead of re-parsing the outs directory (skipping the 10x HDF5 matrix, CSV metadata, and polygon-to-WKT construction). When set and the file does not exist, it is written after the load completes so subsequent calls are fast. Pass None to skip caching.

## Full Documentation

# omicverse.io.read_xenium #

omicverse.io. read_xenium ( path , * , library_id = None , load_image = True , image_key = 'morphology_focus' , image_max_dim = 4096 , load_boundaries = True , cache_file = None ) [source] #

Read a 10x Xenium `outs `directory into an AnnData object.

Handles the standard flat layout shipped by Xenium Onboard Analysis:

```text
outs/
cell_feature_matrix.h5 # gene × cell sparse matrix
cells.csv.gz (or cells.parquet)# per-cell metadata incl. centroids
experiment.xenium # run / panel metadata (JSON)
morphology_focus.ome.tif # V1 focused morphology image (optional)
morphology_focus/ # V2 / Prime morphology folder (optional)
morphology_focus_0000.ome.tif # DAPI
morphology_focus_0001.ome.tif # boundary stain
morphology_focus_0002.ome.tif # interior stain
morphology_focus_0003.ome.tif # 4th channel (Prime panels)

```

Parameters :

-
path ( `Union `[ `str `, `Path `] ) – The Xenium `outs `directory (or any directory containing the files above).

-
library_id ( `Optional `[ `str `] (default: `None `)) – Identifier used as the key under `adata.uns['spatial'] `. Defaults to `experiment.xenium `’s `region_name `/ `run_name `if present, else the directory name.

-
load_image ( `bool `(default: `True `)) – When `True `and `tifffile `is installed, loads the morphology image so `omicverse.pl.spatial() `can overlay it. The morphology TIFF is large (hundreds of MB); pass `False `for lightweight tutorials that only need the centroid scatter.

-
image_key ( `str `(default: `'morphology_focus' `)) –
Which morphology image to load. Accepts:

-
`'morphology_focus' `/ `'morphology_mip' `— V1 layout files at the outs root; falls back to the first V2 channel ( `_0000 `, DAPI) when V1 files are absent.

-
`'morphology_focus_NNNN' `— pick a specific V2 / Prime channel ( `_0000 `DAPI, `_0001 `boundary, `_0002 `interior, `_0003 `alternative) from `morphology_focus/ `. If the requested channel is missing, the reader falls back to the other available channels rather than returning no image.

-
image_max_dim ( `int `(default: `4096 `)) – Xenium OME-TIFFs are multi-resolution pyramids; this is the maximum pixel extent along either axis that we will load. The highest-resolution pyramid level fitting under this cap is used. Default 4096 keeps the in-memory array small while remaining usable for overlay. Pass a larger value (e.g. 8192) for closer crops.

-
load_boundaries ( `bool `(default: `True `)) – When `True `and `cell_boundaries.parquet `/ `.csv.gz `is present, converts per-cell polygon vertices to WKT strings stored in `obs['geometry'] `— required by `omicverse.pl.spatialseg() `.

-
cache_file ( `Union `[ `str `, `Path `, `None `] (default: `None `)) – Optional path to an `.h5ad `cache. When set and the file exists, we read it back instead of re-parsing the outs directory (skipping the 10x HDF5 matrix, CSV metadata, and polygon-to-WKT construction). When set and the file does not exist, it is written after the load completes so subsequent calls are fast. Pass `None `to skip caching.

Returns :

-
`X `: CSR sparse, `int32 `counts (cells × genes)

-
`obs `: cell metadata from `cells.csv.gz `

-
`obsm['spatial'] `: `(n_obs, 2) `cell centroids in microns

-
`var `: gene panel metadata

-

`uns['spatial'][library_id] `:

-
`'images'['hires'] `: morphology image (if loaded)

-
`'scalefactors'['tissue_hires_scalef'] `: `1 / pixel_size `— mapping micron coords to image pixels

-
`'scalefactors'['spot_diameter_fullres'] `: mean cell diameter in fullres (image) pixels, for default spot sizing

-
`'metadata' `: contents of `experiment.xenium `

Return type :

AnnData
