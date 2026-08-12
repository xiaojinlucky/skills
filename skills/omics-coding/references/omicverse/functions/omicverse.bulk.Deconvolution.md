# omicverse.bulk.Deconvolution #

- Package: omicverse
- Language: Python
- Function: `omicverse.bulk.Deconvolution`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.bulk.Deconvolution.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Bulk RNA-seq deconvolution class for inferring cell-type fractions from single-cell references.

## Signature

```text
class omicverse.bulk. Deconvolution ( adata_bulk , adata_single , max_single_cells = 5000 , celltype_key = 'celltype' , cellstate_key = None , gpu = 0 )
```

## Parameters

- `adata_bulk`: ( AnnData ) – Bulk expression matrix with samples in rows and genes in columns.
- `adata_single`: ( AnnData ) – Single-cell reference matrix containing cell-level expression profiles and cell-type annotations used to build signature profiles.
- `max_single_cells`: ( int ) – Maximum number of cells to keep from adata_single . If the reference contains more cells, a random subset is used to control memory/runtime.
- `celltype_key`: ( str ) – Column name in adata_single.obs storing cell-type labels.
- `cellstate_key`: ( str or None ) – Optional column name in adata_single.obs storing finer cell-state labels (used by methods such as BayesPrism).
- `gpu`: ( Union [ int , str ] ) – Compute device selector. Supports CUDA index (for example 0 ), explicit strings such as 'cuda:0' , 'mps' , or 'cpu' .

## Full Documentation

# omicverse.bulk.Deconvolution #

class omicverse.bulk. Deconvolution ( adata_bulk , adata_single , max_single_cells = 5000 , celltype_key = 'celltype' , cellstate_key = None , gpu = 0 ) [source] #

Bulk RNA-seq deconvolution class for inferring cell-type fractions from single-cell references.

Parameters :

-
adata_bulk ( AnnData ) – Bulk expression matrix with samples in rows and genes in columns.

-
adata_single ( AnnData ) – Single-cell reference matrix containing cell-level expression profiles and cell-type annotations used to build signature profiles.

-
max_single_cells ( int ) – Maximum number of cells to keep from `adata_single `. If the reference contains more cells, a random subset is used to control memory/runtime.

-
celltype_key ( str ) – Column name in `adata_single.obs `storing cell-type labels.

-
cellstate_key ( str or None ) – Optional column name in `adata_single.obs `storing finer cell-state labels (used by methods such as BayesPrism).

-
gpu ( Union [ int , str ] ) – Compute device selector. Supports CUDA index (for example `0 `), explicit strings such as `'cuda:0' `, `'mps' `, or `'cpu' `.

Returns :

Initializes deconvolution inputs and builds reference expression profiles.

Return type :

None

Examples

```text
>>> deconv_obj = ov.bulk.Deconvolution(adata_bulk, adata_single, celltype_key="celltype")

```

__init__ ( adata_bulk , adata_single , max_single_cells = 5000 , celltype_key = 'celltype' , cellstate_key = None , gpu = 0 ) [source] #

Parameters :

-
max_single_cells ( `int `(default: `5000 `))

-
celltype_key ( `str `(default: `'celltype' `))

-
cellstate_key ( `Optional `[ `str `] (default: `None `))

-
gpu ( `Union `[ `int `, `str `] (default: `0 `))

Methods

`__init__ `(adata_bulk, adata_single[, ...])

`deconvolution `([method, sep, scaler, ...])

Estimate cell-type composition of bulk RNA-seq samples.
