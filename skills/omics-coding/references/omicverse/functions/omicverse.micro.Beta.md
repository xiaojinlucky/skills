# omicverse.micro.Beta #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Beta`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Beta.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Compute sample × sample distance matrices.

## Signature

```text
class omicverse.micro. Beta ( adata , rarefy_depth = None , seed = 0 )
```

## Parameters

- `adata`: ( AnnData ) – Samples × features AnnData with int counts.
- `rarefy_depth`: ( Optional [ int ] (default: None )) – If set, subsample to this depth before distance calculation (good practice for Bray-Curtis / Jaccard to remove library-size effects). None → use raw counts.
- `seed`: ( int (default: 0 )) – Random seed for rarefaction.

## Full Documentation

# omicverse.micro.Beta #

class omicverse.micro. Beta ( adata , rarefy_depth = None , seed = 0 ) [source] #

Compute sample × sample distance matrices.

Parameters :

-
adata ( `AnnData `) – Samples × features AnnData with int counts.

-
rarefy_depth ( `Optional `[ `int `] (default: `None `)) – If set, subsample to this depth before distance calculation (good practice for Bray-Curtis / Jaccard to remove library-size effects). `None `→ use raw counts.

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

`braycurtis `([rarefy])

Bray-Curtis dissimilarity matrix (samples × samples).

`run `([metric, rarefy, tree_key, write_to_obsp])

Compute the distance matrix.
