# omicverse.pp.umap #

- Package: omicverse
- Language: Python
- Function: `omicverse.pp.umap`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pp.umap.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute UMAP embedding, dispatching to the best backend for ov.settings.mode .

## Signature

```text
omicverse.pp. umap ( adata , * , min_dist=0.5 , spread=1.0 , n_components=2 , maxiter=None , alpha=1.0 , gamma=1.0 , negative_sample_rate=5 , init_pos=None , random_state=<ov.seed-default> , a=None , b=None , method=None , key_added=None , neighbors_key='neighbors' , copy=False , **kwargs )
```

## Parameters

- `adata`: – Annotated data matrix; neighbors must already be computed.
- `min_dist`: ( float (default: 0.5 )) – Minimum distance between embedded points. Default 0.5 matches scanpy; smaller gives more densely packed clusters.
- `spread`: ( float (default: 1.0 )) – Scale at which embedded points are spread out.
- `n_components`: ( int (default: 2 )) – Output dimensions (2 for typical visualisation).
- `maxiter`: ( Optional [ int ] (default: None )) – Number of edge-SGD passes. Defaults are backend-specific — scanpy uses 200 for N>10k, 500 otherwise.
- `alpha`: ( float (default: 1.0 )) – Initial learning rate of the edge-SGD optimiser. Only used by non-parametric backends.
- `gamma`: ( float (default: 1.0 )) – Weighting for negative samples. Default 1.0 matches scanpy.
- `negative_sample_rate`: ( int (default: 5 )) – Number of negative samples per positive edge. Default 5 .
- `init_pos`: (default: None ) – Embedding initialisation: 'paga' , 'spectral' , 'random' , or an ndarray . None lets the backend pick.
- `random_state`: (default: <ov.seed-default> ) – Seed for reproducibility.
- `a`: ( Optional [ float ] (default: None )) – UMAP curve parameters. None derives them from spread + min_dist via umap.umap_.find_ab_params .
- `b`: ( Optional [ float ] (default: None )) – UMAP curve parameters. None derives them from spread + min_dist via umap.umap_.find_ab_params .
- `method`: ( Optional [ str ] (default: None )) – Explicit backend override, e.g. 'umap' (scanpy/umap-learn), 'pumap' (omicverse’s parametric GPU UMAP), 'torchdr' , 'mde' , 'rapids' . None picks the right default for the current ov.settings.mode .
- `key_added`: ( Optional [ str ] (default: None )) – Key under which to store results; default 'X_umap' / 'umap' .
- `neighbors_key`: ( str (default: 'neighbors' )) – .uns key holding the precomputed neighbor graph.
- `copy`: ( bool (default: False )) – Return a new AnnData instead of modifying in place.
- `**kwargs`: – Forwarded to the underlying backend ( _umap.umap , rapids_singlecell.tl.umap etc.).

## Full Documentation

# omicverse.pp.umap #

omicverse.pp. umap ( adata , * , min_dist=0.5 , spread=1.0 , n_components=2 , maxiter=None , alpha=1.0 , gamma=1.0 , negative_sample_rate=5 , init_pos=None , random_state=<ov.seed-default> , a=None , b=None , method=None , key_added=None , neighbors_key='neighbors' , copy=False , **kwargs ) [source] #

Compute UMAP embedding, dispatching to the best backend for `ov.settings.mode `.

Parameters :

-
adata – Annotated data matrix; neighbors must already be computed.

-
min_dist ( `float `(default: `0.5 `)) – Minimum distance between embedded points. Default `0.5 `matches scanpy; smaller gives more densely packed clusters.

-
spread ( `float `(default: `1.0 `)) – Scale at which embedded points are spread out.

-
n_components ( `int `(default: `2 `)) – Output dimensions (2 for typical visualisation).

-
maxiter ( `Optional `[ `int `] (default: `None `)) – Number of edge-SGD passes. Defaults are backend-specific — scanpy uses 200 for N>10k, 500 otherwise.

-
alpha ( `float `(default: `1.0 `)) – Initial learning rate of the edge-SGD optimiser. Only used by non-parametric backends.

-
gamma ( `float `(default: `1.0 `)) – Weighting for negative samples. Default `1.0 `matches scanpy.

-
negative_sample_rate ( `int `(default: `5 `)) – Number of negative samples per positive edge. Default `5 `.

-
init_pos (default: `None `) – Embedding initialisation: `'paga' `, `'spectral' `, `'random' `, or an `ndarray `. `None `lets the backend pick.

-
random_state (default: `<ov.seed-default> `) – Seed for reproducibility.

-
a ( `Optional `[ `float `] (default: `None `)) – UMAP curve parameters. `None `derives them from `spread `+ `min_dist `via `umap.umap_.find_ab_params `.

-
b ( `Optional `[ `float `] (default: `None `)) – UMAP curve parameters. `None `derives them from `spread `+ `min_dist `via `umap.umap_.find_ab_params `.

-
method ( `Optional `[ `str `] (default: `None `)) – Explicit backend override, e.g. `'umap' `(scanpy/umap-learn), `'pumap' `(omicverse’s parametric GPU UMAP), `'torchdr' `, `'mde' `, `'rapids' `. `None `picks the right default for the current `ov.settings.mode `.

-
key_added ( `Optional `[ `str `] (default: `None `)) – Key under which to store results; default `'X_umap' `/ `'umap' `.

-
neighbors_key ( `str `(default: `'neighbors' `)) – `.uns `key holding the precomputed neighbor graph.

-
copy ( `bool `(default: `False `)) – Return a new AnnData instead of modifying in place.

-
**kwargs – Forwarded to the underlying backend ( `_umap.umap `, `rapids_singlecell.tl.umap `etc.).

Notes

Behaviour by `ov.settings.mode `:

-
`'cpu' `— scanpy / umap-learn (CPU).

-

`'cpu-gpu-mixed' `— GPU non-parametric UMAP (gpuex), which

mirrors the CPU algorithm (same fuzzy graph, lobpcg spectral init, a/b curve, edge-SGD) so the embedding is consistent with cpu mode — unlike the old `pumap `.

-

anything else ( `'gpu' `) — RAPIDS if available, falls back to

pumap on import error.
