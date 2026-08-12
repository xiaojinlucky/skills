# omicverse.io.read_visium_hd_bin #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.read_visium_hd_bin`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.read_visium_hd_bin.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read Visium HD bin-level output and attach spatial metadata.

## Signature

```text
omicverse.io. read_visium_hd_bin ( path , sample = None , binsize = 16 , count_h5_path = 'filtered_feature_bc_matrix.h5' , count_mtx_dir = 'filtered_feature_bc_matrix' , tissue_positions_path = 'spatial/tissue_positions.parquet' , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' )
```

## Parameters

- `path`: ( str or Path ) – Path to the SpaceRanger output directory.
- `sample`: ( str , optional ) – Sample key stored in adata.uns['spatial'] . If None , inferred from path.
- `binsize`: ( int , default 16 ) – Bin size metadata (for example 2/8/16).
- `count_h5_path`: ( str ) – Relative path to bin-level 10x H5 matrix.
- `count_mtx_dir`: ( str ) – Relative path to bin-level MTX directory (fallback when H5 unavailable).
- `tissue_positions_path`: ( str ) – Relative path to tissue positions table (parquet/csv).
- `hires_image_path`: ( str ) – Relative path to hires tissue image.
- `lowres_image_path`: ( str ) – Relative path to lowres tissue image.
- `scalefactors_path`: ( str ) – Relative path to scalefactors JSON.

## Full Documentation

# omicverse.io.read_visium_hd_bin #

omicverse.io. read_visium_hd_bin ( path , sample = None , binsize = 16 , count_h5_path = 'filtered_feature_bc_matrix.h5' , count_mtx_dir = 'filtered_feature_bc_matrix' , tissue_positions_path = 'spatial/tissue_positions.parquet' , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' ) [source] #

Read Visium HD bin-level output and attach spatial metadata.

Parameters :

-
path ( str or Path ) – Path to the SpaceRanger output directory.

-
sample ( str , optional ) – Sample key stored in `adata.uns['spatial'] `. If `None `, inferred from path.

-
binsize ( int , default 16 ) – Bin size metadata (for example 2/8/16).

-
count_h5_path ( str ) – Relative path to bin-level 10x H5 matrix.

-
count_mtx_dir ( str ) – Relative path to bin-level MTX directory (fallback when H5 unavailable).

-
tissue_positions_path ( str ) – Relative path to tissue positions table (parquet/csv).

-
hires_image_path ( str ) – Relative path to hires tissue image.

-
lowres_image_path ( str ) – Relative path to lowres tissue image.

-
scalefactors_path ( str ) – Relative path to scalefactors JSON.

Returns :

Bin-level AnnData with `obsm['spatial'] `and `uns['spatial'][sample] `metadata.

Return type :

anndata.AnnData
