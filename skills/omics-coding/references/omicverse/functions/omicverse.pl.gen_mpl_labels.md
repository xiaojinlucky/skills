# omicverse.pl.gen_mpl_labels #

- Package: omicverse
- Language: Python
- Function: `omicverse.pl.gen_mpl_labels`
- Source: https://omicverse.readthedocs.io/en/latest/api/reference/omicverse.pl.gen_mpl_labels.html
- Fetched at: 2026-08-03T14:16:23+00:00

## Summary

Add cluster labels at median positions in embedding plots with automatic text positioning.

## Signature

```text
omicverse.pl. gen_mpl_labels ( adata , groupby , exclude = () , basis = 'X_umap' , ax = None , adjust_kwargs = None , text_kwargs = None )
```

## Parameters

- `adata`: ( AnnData object containing single-cell data. )
- `groupby`: ( Column name for grouping in adata.obs. )
- `exclude`: ( Groups to exclude from labeling. Default: ( ) . )
- `basis`: ( Embedding basis name in adata.obsm. Default: 'X_umap'. )
- `ax`: ( Matplotlib axes object. Default: None. )
- `adjust_kwargs`: ( Parameters for adjustText text adjustment. Default: None. )
- `text_kwargs`: ( Parameters for text styling ( None ) )

## Full Documentation

# omicverse.pl.gen_mpl_labels #

omicverse.pl. gen_mpl_labels ( adata , groupby , exclude = () , basis = 'X_umap' , ax = None , adjust_kwargs = None , text_kwargs = None ) [source] #

Add cluster labels at median positions in embedding plots with automatic text positioning.

Parameters :

-
adata ( AnnData object containing single-cell data. )

-
groupby ( Column name for grouping in adata.obs. )

-
exclude ( Groups to exclude from labeling. Default: ( ) . )

-
basis ( Embedding basis name in adata.obsm. Default: 'X_umap'. )

-
ax ( Matplotlib axes object. Default: None. )

-
adjust_kwargs ( Parameters for adjustText text adjustment. Default: None. )

-
text_kwargs ( Parameters for text styling ( None ) )

Returns :

None
