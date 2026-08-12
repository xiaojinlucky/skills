# omicverse.space.Cal_Spatial_Net #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.Cal_Spatial_Net`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.Cal_Spatial_Net.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Construct spatial neighbor networks for spatial integration.

## Signature

```text
omicverse.space. Cal_Spatial_Net ( adata , rad_cutoff = None , k_cutoff = None , max_neigh = 50 , model = 'Radius' , verbose = True )
```

## Parameters

- `adata`: ( AnnData ) – Spatial AnnData containing coordinates in obsm['spatial'] .
- `rad_cutoff`: ( float , optional ) – Radius threshold when model='Radius' .
- `k_cutoff`: ( int , optional ) – Number of nearest neighbors when model='KNN' .
- `max_neigh`: ( int , default=50 ) – Maximum neighbors queried before filtering by model.
- `model`: ( {'Radius' , 'KNN'} , default='Radius' ) – Strategy for building spatial edges.
- `verbose`: ( bool , default=True ) – Whether to print graph statistics.

## Full Documentation

# omicverse.space.Cal_Spatial_Net #

omicverse.space. Cal_Spatial_Net ( adata , rad_cutoff = None , k_cutoff = None , max_neigh = 50 , model = 'Radius' , verbose = True ) [source] #

Construct spatial neighbor networks for spatial integration.

This function builds a spatial neighborhood graph by connecting spots based on their physical distances. It supports both radius-based and k-nearest neighbor approaches for network construction.

Parameters :

-
adata ( AnnData ) – Spatial AnnData containing coordinates in `obsm['spatial'] `.

-
rad_cutoff ( float , optional ) – Radius threshold when `model='Radius' `.

-
k_cutoff ( int , optional ) – Number of nearest neighbors when `model='KNN' `.

-
max_neigh ( int , default=50 ) – Maximum neighbors queried before filtering by model.

-
model ( {'Radius' , 'KNN'} , default='Radius' ) – Strategy for building spatial edges.

-
verbose ( bool , default=True ) – Whether to print graph statistics.

Returns :

-
None – Writes `adata.uns['Spatial_Net'] `and `adata.uns['adj'] `.

-
Notes –

-
For STAligner, adjust rad_cutoff to ensure 5-10 neighbors per spot

-
Includes self-loops in adjacency matrix

-
Uses ball_tree algorithm for efficient neighbor search

-
Memory efficient implementation for large datasets

-
Critical for downstream integration tasks
