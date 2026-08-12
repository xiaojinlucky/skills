# omicverse.utils.refine_label #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.refine_label`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.refine_label.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Refine labels with neighborhood majority voting.

## Signature

```text
omicverse.utils. refine_label ( adata , use_rep = 'spatial' , radius = 50 , key = 'label' )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Annotated data matrix containing labels and coordinates.
- `use_rep`: ( str , default='spatial' ) – Key in adata.obsm containing coordinates for neighborhood search.
- `radius`: ( int , default=50 ) – Number of nearest neighbors used for voting (excluding the cell itself).
- `key`: ( str , default='label' ) – Column name in adata.obs containing original labels.

## Full Documentation

# omicverse.utils.refine_label #

omicverse.utils. refine_label ( adata , use_rep = 'spatial' , radius = 50 , key = 'label' ) [source] #

Refine labels with neighborhood majority voting.

Parameters :

-
adata ( anndata.AnnData ) – Annotated data matrix containing labels and coordinates.

-
use_rep ( str , default='spatial' ) – Key in `adata.obsm `containing coordinates for neighborhood search.

-
radius ( int , default=50 ) – Number of nearest neighbors used for voting (excluding the cell itself).

-
key ( str , default='label' ) – Column name in `adata.obs `containing original labels.

Returns :

Refined labels for all cells in `adata `.

Return type :

list of str
