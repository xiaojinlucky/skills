# omicverse.space.cellcharter #

- Package: omicverse
- Language: Python
- Function: `omicverse.space.cellcharter`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.space.cellcharter.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run a minimal CellCharter workflow on a spatial AnnData object.

## Signature

```text
omicverse.space. cellcharter ( adata , n_clusters , * , use_rep = 'X_pca' , spatial_key = 'spatial' , n_layers = 3 , aggregations = 'mean' , out_key = 'X_cellcharter' , cluster_key = 'cellcharter' , connectivity_key = 'spatial_connectivities' , distances_key = 'spatial_distances' , sample_key = None , build_spatial_graph = True , delaunay = True , n_neighs = 6 , radius = None , trim_long_links = True , distance_percentile = 99.0 , random_state = 1024 , covariance_type = 'full' , backend = 'auto' , batch_size = None , trainer_params = None )
```

## Parameters

- `adata`: ( AnnData )
- `n_clusters`: ( int )
- `use_rep`: ( str (default: 'X_pca' ))
- `spatial_key`: ( str (default: 'spatial' ))
- `n_layers`: ( int (default: 3 ))
- `aggregations`: ( str | list [ str ] (default: 'mean' ))
- `out_key`: ( str (default: 'X_cellcharter' ))
- `cluster_key`: ( str (default: 'cellcharter' ))
- `connectivity_key`: ( str (default: 'spatial_connectivities' ))
- `distances_key`: ( str (default: 'spatial_distances' ))
- `sample_key`: ( Optional [ str ] (default: None ))
- `build_spatial_graph`: ( bool (default: True ))
- `delaunay`: ( bool (default: True ))
- `n_neighs`: ( int (default: 6 ))
- `trim_long_links`: ( bool (default: True ))
- `distance_percentile`: ( float (default: 99.0 ))
- `random_state`: ( int (default: 1024 ))
- `covariance_type`: ( str (default: 'full' ))
- `backend`: ( str (default: 'auto' ))
- `batch_size`: ( Optional [ int ] (default: None ))
- `trainer_params`: ( Optional [ dict ] (default: None ))
- `radius`: Detected from function signature; no parameter description detected.

## Full Documentation

# omicverse.space.cellcharter #

omicverse.space. cellcharter ( adata , n_clusters , * , use_rep = 'X_pca' , spatial_key = 'spatial' , n_layers = 3 , aggregations = 'mean' , out_key = 'X_cellcharter' , cluster_key = 'cellcharter' , connectivity_key = 'spatial_connectivities' , distances_key = 'spatial_distances' , sample_key = None , build_spatial_graph = True , delaunay = True , n_neighs = 6 , radius = None , trim_long_links = True , distance_percentile = 99.0 , random_state = 1024 , covariance_type = 'full' , backend = 'auto' , batch_size = None , trainer_params = None ) [source] #

Run a minimal CellCharter workflow on a spatial AnnData object.

Parameters :

-
adata ( `AnnData `)

-
n_clusters ( `int `)

-
use_rep ( `str `(default: `'X_pca' `))

-
spatial_key ( `str `(default: `'spatial' `))

-
n_layers ( `int `(default: `3 `))

-
aggregations ( `str `| `list `[ `str `] (default: `'mean' `))

-
out_key ( `str `(default: `'X_cellcharter' `))

-
cluster_key ( `str `(default: `'cellcharter' `))

-
connectivity_key ( `str `(default: `'spatial_connectivities' `))

-
distances_key ( `str `(default: `'spatial_distances' `))

-
sample_key ( `Optional `[ `str `] (default: `None `))

-
build_spatial_graph ( `bool `(default: `True `))

-
delaunay ( `bool `(default: `True `))

-
n_neighs ( `int `(default: `6 `))

-
trim_long_links ( `bool `(default: `True `))

-
distance_percentile ( `float `(default: `99.0 `))

-
random_state ( `int `(default: `1024 `))

-
covariance_type ( `str `(default: `'full' `))

-
backend ( `str `(default: `'auto' `))

-
batch_size ( `Optional `[ `int `] (default: `None `))

-
trainer_params ( `Optional `[ `dict `] (default: `None `))
