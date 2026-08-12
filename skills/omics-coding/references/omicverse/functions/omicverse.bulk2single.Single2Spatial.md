# omicverse.bulk2single.Single2Spatial #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk2single.Single2Spatial`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk2single.Single2Spatial.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Deep-learning mapper that projects single-cell profiles onto spatial coordinates.

## Signature

```text
class omicverse.bulk2single. Single2Spatial ( single_data , spatial_data , celltype_key , spot_key = ['xcoord', 'ycoord'] , top_marker_num = 500 , marker_used = True , gpu = 0 )
```

## Parameters

- `single_data`: ( anndata.AnnData ) – Single-cell reference AnnData containing expression and cell types.
- `spatial_data`: ( anndata.AnnData ) – Spatial transcriptomics AnnData used as mapping target.
- `celltype_key`: ( str ) – Column name in single_data.obs containing cell-type labels.
- `spot_key`: ( list ) – Column names in spatial_data.obs storing x/y coordinates.
- `top_marker_num`: ( int ) – Number of marker genes used to train mapping model.
- `marker_used`: ( bool ) – Whether to restrict training features to marker genes.
- `gpu`: ( Union [ int , str ] ) – Compute device selector (CUDA index, 'mps' , or CPU fallback).

## Full Documentation

# omicverse.bulk2single.Single2Spatial #

class omicverse.bulk2single. Single2Spatial ( single_data , spatial_data , celltype_key , spot_key = ['xcoord', 'ycoord'] , top_marker_num = 500 , marker_used = True , gpu = 0 ) [source] #

Deep-learning mapper that projects single-cell profiles onto spatial coordinates.

Parameters :

-
single_data ( anndata.AnnData ) – Single-cell reference AnnData containing expression and cell types.

-
spatial_data ( anndata.AnnData ) – Spatial transcriptomics AnnData used as mapping target.

-
celltype_key ( str ) – Column name in `single_data.obs `containing cell-type labels.

-
spot_key ( list ) – Column names in `spatial_data.obs `storing x/y coordinates.

-
top_marker_num ( int ) – Number of marker genes used to train mapping model.

-
marker_used ( bool ) – Whether to restrict training features to marker genes.

-
gpu ( Union [ int , str ] ) – Compute device selector (CUDA index, `'mps' `, or CPU fallback).

Returns :

Initializes single-cell to spatial mapping workflow.

Return type :

None

Examples

```text
>>> st_model = ov.bulk2single.Single2Spatial(single_data=single_data, spatial_data=st_data, celltype_key="Cell_type")

```

__init__ ( single_data , spatial_data , celltype_key , spot_key = ['xcoord', 'ycoord'] , top_marker_num = 500 , marker_used = True , gpu = 0 ) [source] #

Initialize Single2Spatial model for mapping single cells to spatial coordinates.

Parameters :

-
single_data ( anndata.AnnData ) – Single-cell reference AnnData for source expression profiles.

-
spatial_data ( anndata.AnnData ) – Spatial reference AnnData providing coordinates and spot expression.

-
celltype_key ( str ) – Name of the cell-type annotation column in `single_data.obs `.

-
spot_key ( list ) – Two-column key in `spatial_data.obs `defining x/y coordinates.

-
top_marker_num ( int ) – Number of marker genes selected for mapping.

-
marker_used ( bool ) – Whether marker-based feature selection is enabled.

-
gpu ( Union [ int , str ] ) – Device selector for model training.

Returns :

None

Methods

`__init__ `(single_data, spatial_data, celltype_key)

Initialize Single2Spatial model for mapping single cells to spatial coordinates.

`load `(modelsize[, df_load_dir, ...])

Load a pre-trained Single2Spatial model and perform mapping.

`save `([df_save_dir, df_save_name])

Save the trained Single2Spatial model.

`spot_assess `()

Assess and aggregate predicted spatial data at the spot level.

`train `(spot_num, cell_num[, df_save_dir, ...])

Train the deep neural network for single-cell to spatial mapping.
