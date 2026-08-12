# omicverse.single.TrajInfer #

- Package: omicverse
- Language: Python
- Function: `omicverse.single.TrajInfer`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.single.TrajInfer.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Trajectory inference class for single-cell data analysis.

## Signature

```text
class omicverse.single. TrajInfer ( adata , basis = 'X_umap' , use_rep = 'X_pca' , n_comps = 50 , n_neighbors = 15 , groupby = 'clusters' )
```

## Parameters

- `adata`: ( AnnData )
- `basis`: ( str (default: 'X_umap' ))
- `use_rep`: ( str (default: 'X_pca' ))
- `n_comps`: ( int (default: 50 ))
- `n_neighbors`: ( int (default: 15 ))
- `groupby`: ( str (default: 'clusters' ))

## Full Documentation

# omicverse.single.TrajInfer #

class omicverse.single. TrajInfer ( adata , basis = 'X_umap' , use_rep = 'X_pca' , n_comps = 50 , n_neighbors = 15 , groupby = 'clusters' ) [source] #

Trajectory inference class for single-cell data analysis.

This class provides methods for inferring developmental trajectories using various algorithms including Palantir, diffusion maps, and Slingshot.

Parameters :

-
adata ( `AnnData `)

-
basis ( `str `(default: `'X_umap' `))

-
use_rep ( `str `(default: `'X_pca' `))

-
n_comps ( `int `(default: `50 `))

-
n_neighbors ( `int `(default: `15 `))

-
groupby ( `str `(default: `'clusters' `))

__init__ ( adata , basis = 'X_umap' , use_rep = 'X_pca' , n_comps = 50 , n_neighbors = 15 , groupby = 'clusters' ) [source] #

Initialize trajectory inference object.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object containing single-cell expression and embeddings.

-
basis ( str ) – Embedding key in `adata.obsm `used for visualization (for example `'X_umap' `).

-
use_rep ( str ) – Representation key in `adata.obsm `used for trajectory inference.

-
n_comps ( int ) – Number of components from `use_rep `used for graph/diffusion computation.

-
n_neighbors ( int ) – Number of neighbors used in graph construction.

-
groupby ( str ) – Cluster/annotation key in `adata.obs `.

Methods

`__init__ `(adata[, basis, use_rep, n_comps, ...])

Initialize trajectory inference object.

`inference `([method])

Perform trajectory inference using specified method.

`palantir_cal_branch `([plot_kwargs, return_fig])

Calculate and plot branch selection for Palantir results.

`palantir_cal_gene_trends `([layers])

Calculate gene expression trends along Palantir trajectories.

`palantir_plot_gene_trends `(genes[, lineages, ...])

Plot gene expression trends along Palantir trajectories.

`palantir_plot_pseudotime `([return_fig])

Plot Palantir pseudotime results.

`set_origin_cells `(origin)

Set origin cell type for trajectory inference.

`set_terminal_cells `(terminal)

Set terminal cell types for trajectory inference.
