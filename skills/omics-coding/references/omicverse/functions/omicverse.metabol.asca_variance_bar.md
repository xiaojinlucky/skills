# omicverse.metabol.asca_variance_bar #

- Package: omicverse
- Language: Python
- Function: `omicverse.metabol.asca_variance_bar`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.metabol.asca_variance_bar.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Horizontal bars of per-effect variance-explained fractions.

## Signature

```text
omicverse.metabol. asca_variance_bar ( asca_result , * , ax = None , figsize = (5.5, 3.0) )
```

## Parameters

- `asca_result`: ( ASCAResult ) – Output of asca() . Reads .effects[name].variance_explained for each named effect plus .residual_ss / .total_ss .
- `ax`: ( Optional [ Axes ] (default: None )) – Standard matplotlib hooks.
- `figsize`: ( tuple [ float , float ] (default: (5.5, 3.0) )) – Standard matplotlib hooks.

## Full Documentation

# omicverse.metabol.asca_variance_bar #

omicverse.metabol. asca_variance_bar ( asca_result , * , ax = None , figsize = (5.5, 3.0) ) [source] #

Horizontal bars of per-effect variance-explained fractions.

Visualises the partition of total sum-of-squares from `omicverse.metabol.asca() `across the named effects (factors and their interactions) plus the residual. The grey “residual” bar at the bottom shows what the model didn’t explain — a useful sanity check: if residual variance dominates, the planned factors don’t capture the dominant signal and the model needs revision.

Parameters :

-
asca_result ( ASCAResult ) – Output of `asca() `. Reads `.effects[name].variance_explained `for each named effect plus `.residual_ss `/ `.total_ss `.

-
ax ( `Optional `[ `Axes `] (default: `None `)) – Standard matplotlib hooks.

-
figsize ( `tuple `[ `float `, `float `] (default: `(5.5, 3.0) `)) – Standard matplotlib hooks.

Returns :

-
(fig, ax) tuple. Bar labels show variance percentage with one

-
decimal place.
