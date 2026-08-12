# omicverse.pl.geneset_wordcloud #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.geneset_wordcloud`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.geneset_wordcloud.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Build cluster-wise gene-set word clouds along pseudotime.

## Signature

```text
class omicverse.pl. geneset_wordcloud ( adata , cluster_key , pseudotime , resolution = 1000 , figsize = (4, 10) )
```

## Parameters

- `adata`: ( AnnData ) – AnnData containing feature scores (for example pathway activity or gene programs).
- `cluster_key`: ( str ) – adata.obs key defining cell clusters/groups.
- `pseudotime`: ( str ) – adata.obs key defining pseudotime ordering.
- `resolution`: ( int , optional ) – Vertical grid resolution for stacked plotting.
- `figsize`: ( tuple , optional ) – Figure size for word-cloud visualization.

## Full Documentation

# omicverse.pl.geneset_wordcloud #

class omicverse.pl. geneset_wordcloud ( adata , cluster_key , pseudotime , resolution = 1000 , figsize = (4, 10) ) [source] #

Build cluster-wise gene-set word clouds along pseudotime.

Parameters :

-
adata ( AnnData ) – AnnData containing feature scores (for example pathway activity or gene programs).

-
cluster_key ( str ) – `adata.obs `key defining cell clusters/groups.

-
pseudotime ( str ) – `adata.obs `key defining pseudotime ordering.

-
resolution ( int , optional ) – Vertical grid resolution for stacked plotting.

-
figsize ( tuple , optional ) – Figure size for word-cloud visualization.

Returns :

Initializes word-cloud construction settings.

Return type :

None

Examples

```text
>>> gw_obj = ov.utils.geneset_wordcloud(adata=adata_aucs[:, var_name], cluster_key="g1", pseudotime="pt_via")

```

__init__ ( adata , cluster_key , pseudotime , resolution = 1000 , figsize = (4, 10) ) [source] #

Initialize word-cloud builder from AnnData and grouping metadata.

Methods

`__init__ `(adata, cluster_key, pseudotime[, ...])

Initialize word-cloud builder from AnnData and grouping metadata.

`get `()

Build per-cluster word-cloud objects from dominant features.

`get_geneset `()

Return the feature-to-cluster assignment table used for word-cloud generation.

`get_wordcloud `()

Return generated word-cloud objects.

`plot `()

Plot stacked cluster word clouds ordered by mean pseudotime.

`plot_heatmap `([n_convolve, figwidth, cmap, ...])

Plot cluster word clouds together with a pseudotime-smoothed heatmap.
