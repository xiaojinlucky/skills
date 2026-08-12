# omicverse.pp.mde #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.mde`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.mde.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run MDE (Minimum Distortion Embedding) from a latent representation.

## Signature

```text
omicverse.pp. mde ( adata , embedding_dim = 2 , n_neighbors = 15 , basis = 'X_mde' , n_pcs = None , use_rep = None , knn = True , transformer = None , metric = 'euclidean' , verbose = False , key_added = None , random_state = 0 , repulsive_fraction = 0.7 , constraint = None )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object containing a latent representation in adata.obsm .
- `embedding_dim`: ( int , default=2 ) – Number of dimensions in the output embedding.
- `n_neighbors`: ( int , default=15 ) – Number of neighbors used for graph construction in MDE.
- `basis`: ( str , default="X_mde" ) – Key in adata.obsm where the result is stored.
- `n_pcs`: ( int , optional ) – Number of principal components used from use_rep .
- `use_rep`: ( str , optional ) – Input representation key in adata.obsm . Defaults to 'X_pca' .
- `knn`: ( bool , default=True ) – Whether to use k-nearest-neighbor graph initialization.
- `transformer`: ( object , optional ) – Optional neighbor transformer object.
- `metric`: ( str , default="euclidean" ) – Distance metric for neighborhood search.
- `verbose`: ( bool , default=False ) – Whether to print detailed optimization logs.
- `key_added`: ( str , optional ) – Optional key alias for metadata outputs.
- `random_state`: ( int , default=0 ) – Random seed for reproducibility.
- `repulsive_fraction`: ( float , default=0.7 ) – Repulsion weight controlling global separation.
- `constraint`: ( object , optional ) – PyMDE constraint object. Uses pymde.Standardized() when None .

## Full Documentation

# omicverse.pp.mde #

omicverse.pp. mde ( adata , embedding_dim = 2 , n_neighbors = 15 , basis = 'X_mde' , n_pcs = None , use_rep = None , knn = True , transformer = None , metric = 'euclidean' , verbose = False , key_added = None , random_state = 0 , repulsive_fraction = 0.7 , constraint = None ) [source] #

Run MDE (Minimum Distortion Embedding) from a latent representation.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object containing a latent representation in `adata.obsm `.

-
embedding_dim ( int , default=2 ) – Number of dimensions in the output embedding.

-
n_neighbors ( int , default=15 ) – Number of neighbors used for graph construction in MDE.

-
basis ( str , default="X_mde" ) – Key in `adata.obsm `where the result is stored.

-
n_pcs ( int , optional ) – Number of principal components used from `use_rep `.

-
use_rep ( str , optional ) – Input representation key in `adata.obsm `. Defaults to `'X_pca' `.

-
knn ( bool , default=True ) – Whether to use k-nearest-neighbor graph initialization.

-
transformer ( object , optional ) – Optional neighbor transformer object.

-
metric ( str , default="euclidean" ) – Distance metric for neighborhood search.

-
verbose ( bool , default=False ) – Whether to print detailed optimization logs.

-
key_added ( str , optional ) – Optional key alias for metadata outputs.

-
random_state ( int , default=0 ) – Random seed for reproducibility.

-
repulsive_fraction ( float , default=0.7 ) – Repulsion weight controlling global separation.

-
constraint ( object , optional ) – PyMDE constraint object. Uses `pymde.Standardized() `when `None `.

Returns :

Stores the low-dimensional embedding in `adata.obsm[basis] `.

Return type :

None
