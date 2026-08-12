# omicverse.space.CellMap #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.CellMap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.CellMap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

SpatRio CellMap class for mapping single cells to spatial coordinates.

## Signature

```text
class omicverse.space. CellMap ( adata_sc , adata_sp , use_rep_sc = 'X_pca' , use_rep_sp = 'X_pca' )
```

## Parameters

- `adata_sc`: ( anndata.AnnData ) – Single-cell reference AnnData.
- `adata_sp`: ( anndata.AnnData ) – Spatial AnnData to receive mapped cells.
- `use_rep_sc`: ( str , default="X_pca" ) – Representation key in adata_sc.obsm used for transport.
- `use_rep_sp`: ( str , default="X_pca" ) – Representation key in adata_sp.obsm used for transport.

## Full Documentation

# omicverse.space.CellMap #

class omicverse.space. CellMap ( adata_sc , adata_sp , use_rep_sc = 'X_pca' , use_rep_sp = 'X_pca' ) [source] #

SpatRio CellMap class for mapping single cells to spatial coordinates.

This class implements optimal transport-based mapping of single cells to spatial coordinates using expression similarity and spatial awareness. It provides methods for both mapping and coordinate assignment.

Parameters :

-
adata_sc ( anndata.AnnData ) – Single-cell reference AnnData.

-
adata_sp ( anndata.AnnData ) – Spatial AnnData to receive mapped cells.

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
>>> # Initialize CellMap
>>> cm = ov.space.CellMap(
... adata_sc=adata_sc,
... adata_sp=adata_sp,
... use_rep_sc='X_pca'
... )

```

__init__ ( adata_sc , adata_sp , use_rep_sc = 'X_pca' , use_rep_sp = 'X_pca' ) [source] #

Initialize CellMap with single-cell and spatial references.

Parameters :

-
adata_sc ( anndata.AnnData ) – Single-cell reference object to be projected into spatial coordinates.

-
adata_sp ( anndata.AnnData ) – Spatial transcriptomics object providing spot locations.

-
use_rep_sc ( str , default="X_pca" ) – Embedding key in `adata_sc.obsm `used for alignment.

-
use_rep_sp ( str , default="X_pca" ) – Embedding key in `adata_sp.obsm `used for alignment.

Methods

`__init__ `(adata_sc, adata_sp[, use_rep_sc, ...])

Initialize CellMap with single-cell and spatial references.

`assign_coord `(**kwargs)

Assign concrete spatial coordinates to mapped single cells.

`map `([sc_type, sp_type, alpha, aware_power, ...])

Map single cells to spatial spots by optimal transport.
