# omicverse.space.spatial_neighbors #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.spatial_neighbors`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.spatial_neighbors.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build a spatial neighborhood graph from coordinates stored in adata.obsm .

## Signature

```text
omicverse.space. spatial_neighbors ( adata , spatial_key = 'spatial' , n_neighs = 6 , radius = None , delaunay = False , set_diag = False , key_added = 'spatial' , coord_type = 'generic' , copy = False )
```

## Parameters

- `adata`: – AnnData object with spatial coordinates in adata.obsm[spatial_key] .
- `spatial_key`: ( str (default: 'spatial' )) – Key in adata.obsm that stores 2-D spatial coordinates. Default: ‘spatial’.
- `n_neighs`: ( int (default: 6 )) – Number of nearest spatial neighbors (used when radius is None and delaunay=False ). Default: 6.
- `radius`: (default: None ) – Radius (or (min_radius, max_radius) tuple) for radius-based graph. When set, n_neighs is ignored. Default: None.
- `delaunay`: ( bool (default: False )) – Whether to build the graph from a Delaunay triangulation of the spatial coordinates. When set, n_neighs is ignored. Default: False.
- `set_diag`: ( bool (default: False )) – Whether to include self-loops in the connectivity matrix. Default: False.
- `coord_type`: ( str (default: 'generic' )) – 'generic' (default) keeps every k-nearest neighbour. 'grid' additionally drops edges longer than 1.4 lattice steps, which is what you want on an array platform such as Visium or Stereo-seq: without it, spots on the rim of the tissue reach across the gap to fill their k quota and acquire neighbours they do not touch. On a 400-spot Visium subset the generic graph gives node degrees of 5-10 where the hexagonal lattice allows at most 6. The default is 'generic' so that existing results do not change silently; pass 'grid' for array data, and note that omicverse.space.sepal() assumes a lattice and needs it.
- `key_added`: ( str (default: 'spatial' )) – Prefix for the keys added to adata.obsp and adata.uns . Default: ‘spatial’.
- `copy`: ( bool (default: False )) – If True , return (connectivities, distances) as sparse matrices. Default: False.

## Full Documentation

# omicverse.space.spatial_neighbors #

omicverse.space. spatial_neighbors ( adata , spatial_key = 'spatial' , n_neighs = 6 , radius = None , delaunay = False , set_diag = False , key_added = 'spatial' , coord_type = 'generic' , copy = False ) [source] #

Build a spatial neighborhood graph from coordinates stored in `adata.obsm `.

The resulting connectivity and distance matrices are stored in `adata.obsp['{key_added}_connectivities'] `and `adata.obsp['{key_added}_distances'] `. Graph metadata is written to `adata.uns['{key_added}_neighbors'] `.

Parameters :

-
adata – AnnData object with spatial coordinates in `adata.obsm[spatial_key] `.

-
spatial_key ( `str `(default: `'spatial' `)) – Key in `adata.obsm `that stores 2-D spatial coordinates. Default: ‘spatial’.

-
n_neighs ( `int `(default: `6 `)) – Number of nearest spatial neighbors (used when radius is `None `and `delaunay=False `). Default: 6.

-
radius (default: `None `) – Radius (or `(min_radius, max_radius) `tuple) for radius-based graph. When set, n_neighs is ignored. Default: None.

-
delaunay ( `bool `(default: `False `)) – Whether to build the graph from a Delaunay triangulation of the spatial coordinates. When set, n_neighs is ignored. Default: False.

-
set_diag ( `bool `(default: `False `)) – Whether to include self-loops in the connectivity matrix. Default: False.

-
coord_type ( `str `(default: `'generic' `)) – `'generic' `(default) keeps every k-nearest neighbour. `'grid' `additionally drops edges longer than 1.4 lattice steps, which is what you want on an array platform such as Visium or Stereo-seq: without it, spots on the rim of the tissue reach across the gap to fill their k quota and acquire neighbours they do not touch. On a 400-spot Visium subset the generic graph gives node degrees of 5-10 where the hexagonal lattice allows at most 6. The default is `'generic' `so that existing results do not change silently; pass `'grid' `for array data, and note that `omicverse.space.sepal() `assumes a lattice and needs it.

-
key_added ( `str `(default: `'spatial' `)) – Prefix for the keys added to `adata.obsp `and `adata.uns `. Default: ‘spatial’.

-
copy ( `bool `(default: `False `)) – If `True `, return `(connectivities, distances) `as sparse matrices. Default: False.

Returns :

Modifies adata in-place. Returns matrices when copy is `True `.

Return type :

None or (connectivities, distances)

Examples

```text
>>> import omicverse as ov
>>> ov.space.spatial_neighbors(adata, n_neighs=6)
>>> # radius graph
>>> ov.space.spatial_neighbors(adata, radius=150)

```
