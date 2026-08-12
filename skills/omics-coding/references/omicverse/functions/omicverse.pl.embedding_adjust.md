# omicverse.pl.embedding_adjust #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.embedding_adjust`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.embedding_adjust.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Get locations of cluster median and adjust text labels accordingly.

## Signature

```text
omicverse.pl. embedding_adjust ( adata , groupby , exclude = () , basis = 'X_umap' , ax = None , adjust_kwargs = None , text_kwargs = None )
```

## Parameters

- `adata`: – AnnData object
- `groupby`: – str Key in adata.obs for grouping
- `exclude`: (default: () ) – tuple, optional (default=()) Groups to exclude from labeling
- `basis`: (default: 'X_umap' ) – str, optional (default=’X_umap’) Embedding basis key in adata.obsm
- `ax`: (default: None ) – matplotlib.axes.Axes, optional (default=None) Axes object to plot on
- `adjust_kwargs`: (default: None ) – dict, optional (default=None) Arguments for adjust_text function
- `text_kwargs`: (default: None ) – dict, optional (default=None) Arguments for text annotation

## Full Documentation

# omicverse.pl.embedding_adjust #

omicverse.pl. embedding_adjust ( adata , groupby , exclude = () , basis = 'X_umap' , ax = None , adjust_kwargs = None , text_kwargs = None ) [source] #

Get locations of cluster median and adjust text labels accordingly.

Borrowed from scanpy github forum.

Parameters :

-
adata – AnnData object

-
groupby – str Key in adata.obs for grouping

-
exclude (default: `() `) – tuple, optional (default=()) Groups to exclude from labeling

-
basis (default: `'X_umap' `) – str, optional (default=’X_umap’) Embedding basis key in adata.obsm

-
ax (default: `None `) – matplotlib.axes.Axes, optional (default=None) Axes object to plot on

-
adjust_kwargs (default: `None `) – dict, optional (default=None) Arguments for adjust_text function

-
text_kwargs (default: `None `) – dict, optional (default=None) Arguments for text annotation

Returns :

dict

Dictionary of median positions for each group

Return type :

medians
