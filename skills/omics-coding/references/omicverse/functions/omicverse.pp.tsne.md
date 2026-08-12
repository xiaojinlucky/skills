# omicverse.pp.tsne #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.tsne`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.tsne.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute t-SNE coordinates for cells, dispatching by ov.settings.mode .

## Signature

```text
omicverse.pp. tsne ( adata , n_pcs=None , * , n_components=2 , use_rep=None , perplexity=30 , metric='euclidean' , early_exaggeration=12 , learning_rate=1000 , random_state=<ov.seed-default> , key_added=None , copy=False , n_iter=None , **kwargs )
```

## Parameters

- `adata`: ( anndata.AnnData ) – AnnData with PCA (or another use_rep ) available.
- `n_pcs`: (default: None ) – Number of PCs to use from adata.obsm['X_pca'] .
- `n_components`: ( int (default: 2 )) – Output dimensions (typically 2).
- `use_rep`: ( Optional [ str ] (default: None )) – .obsm key to compute t-SNE on; defaults to X_pca .
- `perplexity`: ( float (default: 30 )) – Controls the effective number of nearest neighbors used to construct the high-D affinities. Typical range 5–50.
- `metric`: ( str (default: 'euclidean' )) – Distance metric for neighbor search. 'euclidean' by default.
- `early_exaggeration`: ( float (default: 12 )) – Scaling applied to P during the early-exaggeration phase (first ~250 iterations). Larger makes clusters tighter in the output.
- `learning_rate`: ( float (default: 1000 )) – Learning rate of the optimiser. 1000 is the sklearn default; the GPU backend auto-rescales to a much smaller value internally.
- `random_state`: (default: <ov.seed-default> ) – Seed for reproducibility.
- `key_added`: ( Optional [ str ] (default: None )) – Target .obsm / .uns key. Defaults to 'X_tsne' / 'tsne' .
- `copy`: ( bool (default: False )) – Return a new AnnData instead of modifying in place.
- `n_iter`: ( Optional [ int ] (default: None )) – Total optimisation iterations. None uses the backend default.
- `**kwargs`: – Forwarded to the backend ( scanpy.tl.tsne , omicverse.pp._tsne.tsne , or rapids_singlecell.tl.tsne ).

## Full Documentation

# omicverse.pp.tsne #

omicverse.pp. tsne ( adata , n_pcs=None , * , n_components=2 , use_rep=None , perplexity=30 , metric='euclidean' , early_exaggeration=12 , learning_rate=1000 , random_state=<ov.seed-default> , key_added=None , copy=False , n_iter=None , **kwargs ) [source] #

Compute t-SNE coordinates for cells, dispatching by `ov.settings.mode `.

Parameters :

-
adata ( anndata.AnnData ) – AnnData with PCA (or another `use_rep `) available.

-
n_pcs (default: `None `) – Number of PCs to use from `adata.obsm['X_pca'] `.

-
n_components ( `int `(default: `2 `)) – Output dimensions (typically 2).

-
use_rep ( `Optional `[ `str `] (default: `None `)) – `.obsm `key to compute t-SNE on; defaults to `X_pca `.

-
perplexity ( `float `(default: `30 `)) – Controls the effective number of nearest neighbors used to construct the high-D affinities. Typical range 5–50.

-
metric ( `str `(default: `'euclidean' `)) – Distance metric for neighbor search. `'euclidean' `by default.

-
early_exaggeration ( `float `(default: `12 `)) – Scaling applied to P during the early-exaggeration phase (first ~250 iterations). Larger makes clusters tighter in the output.

-
learning_rate ( `float `(default: `1000 `)) – Learning rate of the optimiser. `1000 `is the sklearn default; the GPU backend auto-rescales to a much smaller value internally.

-
random_state (default: `<ov.seed-default> `) – Seed for reproducibility.

-
key_added ( `Optional `[ `str `] (default: `None `)) – Target `.obsm `/ `.uns `key. Defaults to `'X_tsne' `/ `'tsne' `.

-
copy ( `bool `(default: `False `)) – Return a new AnnData instead of modifying in place.

-
n_iter ( `Optional `[ `int `] (default: `None `)) – Total optimisation iterations. `None `uses the backend default.

-
**kwargs – Forwarded to the backend ( `scanpy.tl.tsne `, `omicverse.pp._tsne.tsne `, or `rapids_singlecell.tl.tsne `).

Notes

`cpu-gpu-mixed `mode uses our KL-loss native torch t-SNE (see `omicverse/external/torch_tsne.py `) — no `torchdr `dependency.
