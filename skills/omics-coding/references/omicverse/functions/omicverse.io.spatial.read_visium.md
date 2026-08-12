# omicverse.io.spatial.read_visium #

- Package: omicverse
- Language: Python
- Function: `omicverse.io.spatial.read_visium`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.io.spatial.read_visium.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Read 10x-Genomics-formatted Visium dataset.

## Signature

```text
omicverse.io.spatial. read_visium ( path , genome = None , * , count_file = 'filtered_feature_bc_matrix.h5' , library_id = None , load_images = True , source_image_path = None , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' )
```

## Parameters

- `path`: ( Union [ str , PathLike ] ) – Path to the Space Ranger output directory (typically outs/ ).
- `genome`: ( Optional [ str ] (default: None )) – Filter expression to genes within this genome.
- `count_file`: ( str (default: 'filtered_feature_bc_matrix.h5' )) – Count matrix filename inside path . Typically 'filtered_feature_bc_matrix.h5' or 'raw_feature_bc_matrix.h5' .
- `library_id`: ( Optional [ str ] (default: None )) – Identifier stored under adata.uns['spatial'] . Inferred from the HDF5 library_ids attribute when not provided.
- `load_images`: ( bool (default: True )) – Whether to load tissue images, scale factors and spatial coordinates.
- `source_image_path`: ( Union [ str , PathLike , None ] (default: None )) – Optional path to the full-resolution source image. Stored in adata.uns['spatial'][library_id]['metadata']['source_image_path'] .
- `hires_image_path`: ( str (default: 'spatial/tissue_hires_image.png' )) – Relative path to the hires tissue image inside path .
- `lowres_image_path`: ( str (default: 'spatial/tissue_lowres_image.png' )) – Relative path to the lowres tissue image inside path .
- `scalefactors_path`: ( str (default: 'spatial/scalefactors_json.json' )) – Relative path to the scalefactors JSON inside path .

## Full Documentation

# omicverse.io.spatial.read_visium #

omicverse.io.spatial. read_visium ( path , genome = None , * , count_file = 'filtered_feature_bc_matrix.h5' , library_id = None , load_images = True , source_image_path = None , hires_image_path = 'spatial/tissue_hires_image.png' , lowres_image_path = 'spatial/tissue_lowres_image.png' , scalefactors_path = 'spatial/scalefactors_json.json' ) [source] #

Read 10x-Genomics-formatted Visium dataset.

In addition to reading regular 10x output, this looks for the `spatial `folder and loads images, coordinates and scale factors. Based on the Space Ranger output docs .

Parameters :

-
path ( `Union `[ `str `, `PathLike `] ) – Path to the Space Ranger output directory (typically `outs/ `).

-
genome ( `Optional `[ `str `] (default: `None `)) – Filter expression to genes within this genome.

-
count_file ( `str `(default: `'filtered_feature_bc_matrix.h5' `)) – Count matrix filename inside path . Typically `'filtered_feature_bc_matrix.h5' `or `'raw_feature_bc_matrix.h5' `.

-
library_id ( `Optional `[ `str `] (default: `None `)) – Identifier stored under `adata.uns['spatial'] `. Inferred from the HDF5 `library_ids `attribute when not provided.

-
load_images ( `bool `(default: `True `)) – Whether to load tissue images, scale factors and spatial coordinates.

-
source_image_path ( `Union `[ `str `, `PathLike `, `None `] (default: `None `)) – Optional path to the full-resolution source image. Stored in `adata.uns['spatial'][library_id]['metadata']['source_image_path'] `.

-
hires_image_path ( `str `(default: `'spatial/tissue_hires_image.png' `)) – Relative path to the hires tissue image inside path .

-
lowres_image_path ( `str `(default: `'spatial/tissue_lowres_image.png' `)) – Relative path to the lowres tissue image inside path .

-
scalefactors_path ( `str `(default: `'spatial/scalefactors_json.json' `)) – Relative path to the scalefactors JSON inside path .

Returns :

Annotated data matrix where observations/cells are named by their

barcode and variables/genes by gene name.

-
X – count matrix

-
obs_names – barcode names

-
var_names – gene/probe names

-
var[‘gene_ids’] – gene IDs

-
var[‘feature_types’] – feature types

-
uns[‘spatial’][library_id][‘images’] – `{'hires': ndarray, 'lowres': ndarray} `

-
uns[‘spatial’][library_id][‘scalefactors’] – parsed scalefactors JSON

-
uns[‘spatial’][library_id][‘metadata’] – chemistry/version info

-
obsm[‘spatial’] – spot pixel coordinates (row, col in full-res image)

Return type :

adata

Examples

```text
>>> import omicverse as ov
>>> adata = ov.io.spatial.read_visium("outs/")
>>> adata = ov.io.spatial.read_visium("outs/", count_file="raw_feature_bc_matrix.h5")

```
