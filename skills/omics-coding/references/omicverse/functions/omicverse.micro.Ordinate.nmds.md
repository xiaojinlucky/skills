# omicverse.micro.Ordinate.nmds #

- Package: omicverse
- Language: Python
- Function: `omicverse.micro.Ordinate.nmds`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.micro.Ordinate.nmds.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Non-metric multi-dimensional scaling on the distance matrix.

## Signature

```text
Ordinate. nmds ( n = 2 , random_state = 0 , write_to_obsm = True )
```

## Parameters

- `n`: ( int , default 2 ) – Output dimensions.
- `random_state`: ( int , default 0 ) – Seeds the four-restart NMDS init for reproducibility.
- `write_to_obsm`: ( bool , default True ) – Persist coords into adata.obsm[f'{dist_key}_nmds'] and the final stress value into adata.uns['micro'] .

## Full Documentation

# omicverse.micro.Ordinate.nmds #

Ordinate. nmds ( n = 2 , random_state = 0 , write_to_obsm = True ) [source] #

Non-metric multi-dimensional scaling on the distance matrix.

Wraps sklearn.manifold.MDS(dissimilarity=’precomputed’) . NMDS preserves rank order rather than absolute distances — typically less distorted on Bray-Curtis / Jaccard than linear PCoA.

Parameters :

-
n ( int , default 2 ) – Output dimensions.

-
random_state ( int , default 0 ) – Seeds the four-restart NMDS init for reproducibility.

-
write_to_obsm ( bool , default True ) – Persist coords into `adata.obsm[f'{dist_key}_nmds'] `and the final stress value into `adata.uns['micro'] `.

Return type :

pd.DataFrame indexed by sample with columns `NMDS1..NMDSn `.
