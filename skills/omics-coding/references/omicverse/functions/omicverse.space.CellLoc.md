# omicverse.space.CellLoc #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.CellLoc`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.CellLoc.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

SpatRio CellLoc class for probabilistic cell localization.

## Signature

```text
class omicverse.space. CellLoc ( adata_sc , adata_sp , use_rep_sc = 'X_pca' , use_rep_sp = 'X_pca' )
```

## Parameters

- `adata_sc`: ( anndata.AnnData ) – Single-cell reference AnnData.
- `adata_sp`: ( anndata.AnnData ) – Spatial AnnData to receive probabilistic localization.
- `use_rep_sc`: ( str , default="X_pca" ) – Representation key in adata_sc.obsm used for transport.
- `use_rep_sp`: ( str , default="X_pca" ) – Representation key in adata_sp.obsm used for transport.

## Full Documentation

# omicverse.space.CellLoc #

class omicverse.space. CellLoc ( adata_sc , adata_sp , use_rep_sc = 'X_pca' , use_rep_sp = 'X_pca' ) [source] #

SpatRio CellLoc class for probabilistic cell localization.

This class extends CellMap with probabilistic filtering based on cell type proportions for more accurate spatial localization. It provides methods for mapping, saving/loading results, and probabilistic assignment.

Parameters :

-
adata_sc ( anndata.AnnData ) – Single-cell reference AnnData.

-
adata_sp ( anndata.AnnData ) – Spatial AnnData to receive probabilistic localization.

-
use_rep_sc ( str , default="X_pca" ) – Representation key in `adata_sc.obsm `used for transport.

-
use_rep_sp ( str , default="X_pca" ) – Representation key in `adata_sp.obsm `used for transport.

-
Attributes –

adata_sc: AnnData

Single-cell RNA sequencing data.

adata_sp: AnnData

Spatial transcriptomics data.

use_rep_sc: str

Representation key for single-cell data.

use_rep_sp: str

Representation key for spatial data.

spatrio_decon: pandas.DataFrame

Deconvolution results after mapping.

spatrio_map: pandas.DataFrame

Coordinate assignment results.

-
Examples –

```text
>>> import scanpy as sc
>>> import omicverse as ov
>>> # Load data
>>> adata_sc = sc.read_h5ad('single_cell.h5ad')
>>> adata_sp = sc.read_h5ad('spatial.h5ad')
>>> # Initialize CellLoc
>>> cl = ov.space.CellLoc(
... adata_sc=adata_sc,
... adata_sp=adata_sp
... )

```

__init__ ( adata_sc , adata_sp , use_rep_sc = 'X_pca' , use_rep_sp = 'X_pca' ) [source] #

Initialize CellLoc for probabilistic cell localization.

Parameters :

-
adata_sc ( anndata.AnnData ) – Single-cell reference object to be localized.

-
adata_sp ( anndata.AnnData ) – Spatial transcriptomics object containing spot coordinates.

-
use_rep_sc ( str , default="X_pca" ) – Embedding key in `adata_sc.obsm `used for mapping.

-
use_rep_sp ( str , default="X_pca" ) – Embedding key in `adata_sp.obsm `used for mapping.

Methods

`__init__ `(adata_sc, adata_sp[, use_rep_sc, ...])

Initialize CellLoc for probabilistic cell localization.

`load_map `(map_info[, sc_type, sp_type, ...])

Load precomputed transport map into the CellLoc instance.

`loc_assign `(**kwargs)

Assign coordinates to filtered CellLoc mappings.

`loc_map `([sc_type, sp_type, alpha, ...])

Run SpatRio mapping for probabilistic localization workflow.

`loc_prob `(spot_cell_prob[, sc_type, sc_prop, ...])

Filter transport assignments by spot-level cell-type probabilities.

`save_map `(path)

Save current mapping table as CSV.
