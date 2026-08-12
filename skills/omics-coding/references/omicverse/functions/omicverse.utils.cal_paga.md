# omicverse.utils.cal_paga #

- Package: omicverse
- Language: Python
- Function: `omicverse.utils.cal_paga`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.utils.cal_paga.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute a PAGA graph with optional velocity/time priors.

## Signature

```text
omicverse.utils. cal_paga ( adata , groups = None , vkey = 'velocity' , use_time_prior = True , root_key = None , end_key = None , threshold_root_end_prior = None , minimum_spanning_tree = True , copy = False )
```

## Parameters

- `adata`: ( anndata.AnnData ) – Annotated data matrix with neighborhood graph.
- `groups`: ( str or None ) – Grouping key in adata.obs ; auto-detected when None .
- `vkey`: ( str ) – Velocity layer key used for transition confidence.
- `use_time_prior`: ( str or bool ) – Pseudotime prior key (or True to auto-use velocity pseudotime).
- `root_key`: ( str or None ) – Obs key marking root states.
- `end_key`: ( str or None ) – Obs key marking terminal states.
- `threshold_root_end_prior`: ( float or None ) – Threshold for root/end priors in [0, 1] .
- `minimum_spanning_tree`: ( bool ) – Whether to prune graph to most confident tree-like structure.
- `copy`: ( bool ) – Whether to return a copied AnnData with computed results.

## Full Documentation

# omicverse.utils.cal_paga #

omicverse.utils. cal_paga ( adata , groups = None , vkey = 'velocity' , use_time_prior = True , root_key = None , end_key = None , threshold_root_end_prior = None , minimum_spanning_tree = True , copy = False ) [source] #

Compute a PAGA graph with optional velocity/time priors.

Parameters :

-
adata ( anndata.AnnData ) – Annotated data matrix with neighborhood graph.

-
groups ( str or None ) – Grouping key in `adata.obs `; auto-detected when `None `.

-
vkey ( str ) – Velocity layer key used for transition confidence.

-
use_time_prior ( str or bool ) – Pseudotime prior key (or `True `to auto-use velocity pseudotime).

-
root_key ( str or None ) – Obs key marking root states.

-
end_key ( str or None ) – Obs key marking terminal states.

-
threshold_root_end_prior ( float or None ) – Threshold for root/end priors in `[0, 1] `.

-
minimum_spanning_tree ( bool ) – Whether to prune graph to most confident tree-like structure.

-
copy ( bool ) – Whether to return a copied AnnData with computed results.

Returns :

Copied AnnData if `copy=True `; otherwise results are written in place.

Return type :

anndata.AnnData or None
