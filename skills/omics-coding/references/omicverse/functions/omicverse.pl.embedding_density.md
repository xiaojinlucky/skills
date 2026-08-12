# omicverse.pl.embedding_density #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.embedding_density`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.embedding_density.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Plot cluster-specific density on an existing embedding.

## Signature

```text
omicverse.pl. embedding_density ( adata , basis , groupby , target_clusters , ** kwargs )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing embedding coordinates and group labels.
- `basis`: ( str ) – Embedding key (e.g., 'X_umap' ).
- `groupby`: ( str ) – Observation column defining cluster labels.
- `target_clusters`: ( str or list ) – Cluster label(s) to highlight in density map.
- `**kwargs`: – Extra plotting arguments forwarded to embedding .

## Full Documentation

# omicverse.pl.embedding_density #

omicverse.pl. embedding_density ( adata , basis , groupby , target_clusters , ** kwargs ) [source] #

Plot cluster-specific density on an existing embedding.

Parameters :

-
adata ( AnnData ) – AnnData containing embedding coordinates and group labels.

-
basis ( str ) – Embedding key (e.g., `'X_umap' `).

-
groupby ( str ) – Observation column defining cluster labels.

-
target_clusters ( str or list ) – Cluster label(s) to highlight in density map.

-
**kwargs – Extra plotting arguments forwarded to `embedding `.

Returns :

Return value of `embedding(...) `with temporary density color.

Return type :

Any
