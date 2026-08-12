# omicverse.pp.louvain #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.louvain`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.louvain.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Run Louvain clustering on the precomputed kNN graph.

## Signature

```text
omicverse.pp. louvain ( adata , resolution = None , * , random_state = 0 , key_added = 'louvain' , neighbors_key = None , directed = True , use_weights = False , copy = False , ** kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData object with a neighborhood graph already computed.
- `resolution`: (default: None ) – Resolution γ; higher values yield more, smaller clusters.
- `random_state`: (default: 0 ) – Seed for reproducibility.
- `key_added`: (default: 'louvain' ) – Column in adata.obs to store labels. Default 'louvain' .
- `neighbors_key`: (default: None ) – Key in adata.uns for the neighbor dict. None uses the standard 'neighbors' slot.
- `directed`: (default: True ) – Forwarded to the igraph backend; rarely need tuning.
- `use_weights`: (default: False ) – Forwarded to the igraph backend; rarely need tuning.
- `copy`: (default: False ) – Return a new AnnData instead of modifying in place.
- `**kwargs`: – Forwarded to the underlying backend ( scanpy.tl.louvain or rapids_singlecell.tl.louvain ).

## Full Documentation

# omicverse.pp.louvain #

omicverse.pp. louvain ( adata , resolution = None , * , random_state = 0 , key_added = 'louvain' , neighbors_key = None , directed = True , use_weights = False , copy = False , ** kwargs ) [source] #

Run Louvain clustering on the precomputed kNN graph.

Parameters :

-
adata ( anndata.AnnData ) – AnnData object with a neighborhood graph already computed.

-
resolution (default: `None `) – Resolution γ; higher values yield more, smaller clusters.

-
random_state (default: `0 `) – Seed for reproducibility.

-
key_added (default: `'louvain' `) – Column in `adata.obs `to store labels. Default `'louvain' `.

-
neighbors_key (default: `None `) – Key in `adata.uns `for the neighbor dict. `None `uses the standard `'neighbors' `slot.

-
directed (default: `True `) – Forwarded to the igraph backend; rarely need tuning.

-
use_weights (default: `False `) – Forwarded to the igraph backend; rarely need tuning.

-
copy (default: `False `) – Return a new AnnData instead of modifying in place.

-
**kwargs – Forwarded to the underlying backend ( `scanpy.tl.louvain `or `rapids_singlecell.tl.louvain `).

Notes

In `ov.settings.mode='cpu-gpu-mixed' `this is auto-routed to `ov.pp.leiden `(Louvain has no GPU backend and Leiden is its strict improvement). Labels are still written to `adata.obs[key_added] `so existing notebooks keep working.
