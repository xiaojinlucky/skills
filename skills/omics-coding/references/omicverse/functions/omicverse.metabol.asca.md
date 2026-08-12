# omicverse.metabol.asca #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.asca`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.asca.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

ASCA — ANOVA-Simultaneous Component Analysis (Smilde 2005).

## Signature

```text
omicverse.metabol. asca ( adata , * , factors , include_interactions = True , n_components = 2 , n_permutations = 0 , layer = None , center = True , seed = 0 )
```

## Parameters

- `factors`: ( Sequence [ str ] ) – 1–3 column names in adata.obs . Each is treated categorically.
- `include_interactions`: ( bool (default: True )) – Whether to add pairwise A:B interaction terms. Three-way interactions are not computed here — in practice they require far more replicates than a typical metabolomics design supports.
- `n_components`: ( int (default: 2 )) – Number of PCs to retain per effect. Default 2 — enough for the standard ASCA scatter plot.
- `n_permutations`: ( int (default: 0 )) – If > 0, shuffle each factor’s labels that many times and compute the null distribution of effect SS. Reported as p_value . Default 0 (fast; no p-value).
- `layer`: ( Optional [ str ] (default: None )) – AnnData layer name (default None → adata.X ).
- `center`: ( bool (default: True )) – If True (default) subtract the grand mean before decomposition. ASCA as described in Smilde 2005 assumes centered data.
- `seed`: ( int (default: 0 )) – RNG seed for permutation.
- `adata`: ( AnnData )

## Full Documentation

# omicverse.metabol.asca #

omicverse.metabol. asca ( adata , * , factors , include_interactions = True , n_components = 2 , n_permutations = 0 , layer = None , center = True , seed = 0 ) [source] #

ASCA — ANOVA-Simultaneous Component Analysis (Smilde 2005).

Decomposes the mean-centered data matrix into per-factor effect matrices plus (optionally) pairwise interactions and a residual, runs PCA on each effect, and reports variance explained and (optionally) a permutation p-value.

Parameters :

-
factors ( `Sequence `[ `str `] ) – 1–3 column names in `adata.obs `. Each is treated categorically.

-
include_interactions ( `bool `(default: `True `)) – Whether to add pairwise `A:B `interaction terms. Three-way interactions are not computed here — in practice they require far more replicates than a typical metabolomics design supports.

-
n_components ( `int `(default: `2 `)) – Number of PCs to retain per effect. Default 2 — enough for the standard ASCA scatter plot.

-
n_permutations ( `int `(default: `0 `)) – If > 0, shuffle each factor’s labels that many times and compute the null distribution of effect SS. Reported as `p_value `. Default 0 (fast; no p-value).

-
layer ( `Optional `[ `str `] (default: `None `)) – AnnData layer name (default `None `→ `adata.X `).

-
center ( `bool `(default: `True `)) – If True (default) subtract the grand mean before decomposition. ASCA as described in Smilde 2005 assumes centered data.

-
seed ( `int `(default: `0 `)) – RNG seed for permutation.

-
adata ( `AnnData `)

Returns :

Access effects via `result.effects[name] `or call `ASCAResult.summary() `. Names are factor names (e.g. `"treatment" `) or `"A:B" `for interactions.

Return type :

ASCAResult
