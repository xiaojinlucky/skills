# omicverse.micro.Alpha #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Alpha`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Alpha.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute and store per-sample alpha-diversity metrics on adata.obs .

## Signature

```text
class omicverse.micro. Alpha ( adata , rarefy_depth = None , seed = 0 )
```

## Parameters

- `adata`: ( AnnData ) – Samples × features AnnData with int counts. The class does NOT modify X ; pass rarefy_depth if you want rarefaction applied only for the diversity calculation.
- `rarefy_depth`: ( Optional [ int ] (default: None )) – If set, subsample to this depth (without replacement) before computing each metric. None → use raw counts.
- `seed`: ( int (default: 0 )) – Random seed for rarefaction.

## Full Documentation

# omicverse.micro.Alpha #

class omicverse.micro. Alpha ( adata , rarefy_depth = None , seed = 0 ) [source] #

Compute and store per-sample alpha-diversity metrics on `adata.obs `.

Parameters :

-
adata ( `AnnData `) – Samples × features AnnData with int counts. The class does NOT modify `X `; pass `rarefy_depth `if you want rarefaction applied only for the diversity calculation.

-
rarefy_depth ( `Optional `[ `int `] (default: `None `)) – If set, subsample to this depth (without replacement) before computing each metric. `None `→ use raw counts.

-
seed ( `int `(default: `0 `)) – Random seed for rarefaction.

__init__ ( adata , rarefy_depth = None , seed = 0 ) [source] #

Parameters :

-
adata ( `AnnData `)

-
rarefy_depth ( `Optional `[ `int `] (default: `None `))

-
seed ( `int `(default: `0 `))

Methods

`__init__ `(adata[, rarefy_depth, seed])

`observed `()

Per-sample observed-OTU count.

`run `([metrics, write_to_obs, tree_key])

Compute the requested alpha metrics.

`shannon `()

Per-sample Shannon entropy.
