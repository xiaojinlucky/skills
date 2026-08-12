# omicverse.pp.scrublet #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.scrublet`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.scrublet.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Predict cell doublets using Scrublet with optional GPU acceleration.

## Signature

```text
omicverse.pp. scrublet ( adata , adata_sim = None , * , batch_key = None , sim_doublet_ratio = 2.0 , expected_doublet_rate = 0.05 , stdev_doublet_rate = 0.02 , synthetic_doublet_umi_subsampling = 1.0 , knn_dist_metric = 'euclidean' , normalize_variance = True , log_transform = False , mean_center = True , n_prin_comps = 30 , use_approx_neighbors = None , get_doublet_neighbor_parents = False , n_neighbors = None , threshold = None , verbose = True , copy = False , random_state = 0 , use_gpu = False )
```

## Parameters

- `adata`: ( AnnData ) – Observed count matrix (cells x genes) for doublet calling.
- `adata_sim`: ( AnnData , optional ) – Optional pre-simulated doublet AnnData. If None , synthetic doublets are generated from adata .
- `batch_key`: ( str , optional ) – Batch column in adata.obs for per-batch doublet calling.
- `sim_doublet_ratio`: ( float , default=2.0 ) – Number of synthetic doublets relative to observed cells.
- `expected_doublet_rate`: ( float , default=0.05 ) – Prior expected doublet fraction for the experiment.
- `stdev_doublet_rate`: ( float , default=0.02 ) – Standard deviation around the expected doublet rate prior.
- `synthetic_doublet_umi_subsampling`: ( float , default=1.0 ) – UMI subsampling fraction used during synthetic doublet simulation.
- `knn_dist_metric`: ( str or callable , default="euclidean" ) – Distance metric used for nearest-neighbor graph construction.
- `normalize_variance`: ( bool , default=True ) – Whether to variance-normalize features before PCA.
- `log_transform`: ( bool , default=False ) – Whether to log-transform values before PCA.
- `mean_center`: ( bool , default=True ) – Whether to center features before dimensionality reduction.
- `n_prin_comps`: ( int , default=30 ) – Number of principal components used for neighbor graph building.
- `use_approx_neighbors`: ( bool , optional ) – Whether to use approximate nearest neighbors.
- `get_doublet_neighbor_parents`: ( bool , default=False ) – Whether to store parent cell identities of doublet neighbors.
- `n_neighbors`: ( int , optional ) – Number of neighbors for the classifier graph.
- `threshold`: ( float , optional ) – Manual threshold for calling predicted doublets.
- `verbose`: ( bool , default=True ) – Whether to print progress logs.
- `copy`: ( bool , default=False ) – Return a copied AnnData instead of modifying in place.
- `random_state`: ( int or RandomState , default=0 ) – Random seed/state for reproducibility.
- `use_gpu`: ( bool , default=False ) – Whether to use GPU-accelerated PCA path when available.

## Full Documentation

# omicverse.pp.scrublet #

omicverse.pp. scrublet ( adata , adata_sim = None , * , batch_key = None , sim_doublet_ratio = 2.0 , expected_doublet_rate = 0.05 , stdev_doublet_rate = 0.02 , synthetic_doublet_umi_subsampling = 1.0 , knn_dist_metric = 'euclidean' , normalize_variance = True , log_transform = False , mean_center = True , n_prin_comps = 30 , use_approx_neighbors = None , get_doublet_neighbor_parents = False , n_neighbors = None , threshold = None , verbose = True , copy = False , random_state = 0 , use_gpu = False ) [source] #

Predict cell doublets using Scrublet with optional GPU acceleration.

Parameters :

-
adata ( AnnData ) – Observed count matrix (cells x genes) for doublet calling.

-
adata_sim ( AnnData , optional ) – Optional pre-simulated doublet AnnData. If `None `, synthetic doublets are generated from `adata `.

-
batch_key ( str , optional ) – Batch column in `adata.obs `for per-batch doublet calling.

-
sim_doublet_ratio ( float , default=2.0 ) – Number of synthetic doublets relative to observed cells.

-
expected_doublet_rate ( float , default=0.05 ) – Prior expected doublet fraction for the experiment.

-
stdev_doublet_rate ( float , default=0.02 ) – Standard deviation around the expected doublet rate prior.

-
synthetic_doublet_umi_subsampling ( float , default=1.0 ) – UMI subsampling fraction used during synthetic doublet simulation.

-
knn_dist_metric ( str or callable , default="euclidean" ) – Distance metric used for nearest-neighbor graph construction.

-
normalize_variance ( bool , default=True ) – Whether to variance-normalize features before PCA.

-
log_transform ( bool , default=False ) – Whether to log-transform values before PCA.

-
mean_center ( bool , default=True ) – Whether to center features before dimensionality reduction.

-
n_prin_comps ( int , default=30 ) – Number of principal components used for neighbor graph building.

-
use_approx_neighbors ( bool , optional ) – Whether to use approximate nearest neighbors.

-
get_doublet_neighbor_parents ( bool , default=False ) – Whether to store parent cell identities of doublet neighbors.

-
n_neighbors ( int , optional ) – Number of neighbors for the classifier graph.

-
threshold ( float , optional ) – Manual threshold for calling predicted doublets.

-
verbose ( bool , default=True ) – Whether to print progress logs.

-
copy ( bool , default=False ) – Return a copied AnnData instead of modifying in place.

-
random_state ( int or RandomState , default=0 ) – Random seed/state for reproducibility.

-
use_gpu ( bool , default=False ) – Whether to use GPU-accelerated PCA path when available.

Returns :

Returns modified AnnData when `copy=True `; otherwise updates in place and returns `None `.

Return type :

AnnData or None
