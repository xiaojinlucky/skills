# omicverse.single.AnnotationRef #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.AnnotationRef`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.AnnotationRef.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Reference-based label transfer helper for single-cell annotation.

## Signature

```text
class omicverse.single. AnnotationRef ( adata_query , adata_ref , celltype_key = 'celltype' )
```

## Parameters

- `adata_query`: ( AnnData ) – Query AnnData that needs cell-type annotation.
- `adata_ref`: ( AnnData ) – Reference AnnData with known cell-type labels.
- `celltype_key`: ( str ) – Column name in adata_ref.obs containing reference cell-type labels.

## Full Documentation

# omicverse.single.AnnotationRef #

class omicverse.single. AnnotationRef ( adata_query , adata_ref , celltype_key = 'celltype' ) [source] #

Reference-based label transfer helper for single-cell annotation.

Parameters :

-
adata_query ( AnnData ) – Query AnnData that needs cell-type annotation.

-
adata_ref ( AnnData ) – Reference AnnData with known cell-type labels.

-
celltype_key ( str ) – Column name in `adata_ref.obs `containing reference cell-type labels.

Returns :

Initializes concatenated query/reference data and checks feature overlap.

Return type :

None

__init__ ( adata_query , adata_ref , celltype_key = 'celltype' ) [source] #

Parameters :

-
adata_query ( `AnnData `)

-
adata_ref ( `AnnData `)

-
celltype_key ( `str `(default: `'celltype' `))

Methods

`__init__ `(adata_query, adata_ref[, celltype_key])

`predict `([method, n_neighbors, pred_key, ...])

Transfer reference labels to query cells using weighted kNN.

`preprocess `([mode, n_HVGs, batch_key])

Preprocess concatenated query/reference data for robust label transfer.

`train `([method])

Train/compute an integrated embedding used for reference label transfer.
